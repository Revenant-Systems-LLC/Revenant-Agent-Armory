# Performance Tuning Guide — Phase 4 Optimization

## Overview

The INDEX knowledge system delivers three layers of discovery:
1. **Keyword search** (~100ms, 80% precision) — FTS5 SQLite, always fast
2. **Semantic ranking** (~500ms, 95% precision) — Claude Haiku API call, primary bottleneck
3. **Proactive suggestions** (automatic) — Triggered opportunistically, must not block

This guide covers optimization strategies for each layer and monitoring to detect regressions.

---

## Layer 1: Keyword Search Optimization

### FTS5 Index Characteristics

**Current performance:**
- First FTS query (index built on-demand): ~200ms
- Subsequent queries: ~50-100ms
- Index size: ~2-3MB for 16,639 items
- Memory footprint: ~5-10MB during session

**Optimization techniques:**

#### 1. Pre-build Index at Startup (Recommended)

Instead of building FTS index on first search, build it during system initialization:

```python
# In knowledge_index_tool.py IndexSearchEngine.__init__()
def __init__(self, metadata_cache):
    self.metadata = metadata_cache
    self._build_fts_index()  # Pre-build instead of lazy-build
    self.first_query_time = None  # No longer needed
```

**Impact:** Eliminates ~200ms cold-start penalty. All queries hit ~50-100ms baseline.

**Cost:** Session startup adds ~200ms (acceptable, one-time cost).

#### 2. Query-Specific Index Pruning

For scoped searches (e.g., "agents only"), build smaller indexes:

```python
def search_scoped(self, query: str, scope: str = "all", limit: int = 10):
    """Search within a category (agents/, skills/, tools/, etc.)"""
    if scope == "all":
        # Use full index (16,639 items)
        return self._search_fts(query, limit)
    else:
        # Build micro-index for scope (e.g., 92 agents)
        # Faster due to smaller dataset
        return self._search_scoped_fts(query, scope, limit)
```

**Impact:** Scoped searches 2-3x faster for large indexes.

**Trade-off:** Extra code complexity. Only implement if scoped search is common.

#### 3. Keyword Frequency Caching

Cache query frequency to identify popular searches:

```python
class SearchAnalytics:
    def __init__(self):
        self.query_cache = {}  # {query: count}
    
    def log_query(self, query: str):
        self.query_cache[query] = self.query_cache.get(query, 0) + 1
    
    def top_queries(self, n: int = 100) -> list:
        return sorted(self.query_cache.items(), key=lambda x: x[1], reverse=True)[:n]
```

Use top 100 queries for pre-ranking in suggest mode.

**Impact:** Pre-computed results for common queries available in <10ms.

---

## Layer 2: Semantic Ranking Optimization

### Bottleneck Analysis

Current semantic ranking:
- Claude Haiku API latency: ~300-400ms (network round-trip)
- Token usage: ~50-100 tokens per ranking call
- Cost: ~$0.0025 per ranking (25K tokens/$1)
- Precision benefit: +15% over keyword-only (95% vs 80%)

### Optimization 1: Intent Pattern Caching

Cache common intent patterns and their top results:

```python
class IntentCache:
    def __init__(self):
        self.cache = {}  # {intent_hash: [results]}
        self.hit_count = {}
    
    def get(self, intent: str) -> list | None:
        key = hash(intent.lower())
        if key in self.cache:
            self.hit_count[key] = self.hit_count.get(key, 0) + 1
            return self.cache[key]
        return None
    
    def populate_top_intents(self, semantic_ranker):
        """Pre-cache top 100 intent patterns"""
        intents = [
            "rate limiting",
            "authentication",
            "caching",
            "async handling",
            "logging",
            # ... top 100 from analytics
        ]
        for intent in intents:
            self.cache[hash(intent.lower())] = semantic_ranker.rank(intent, limit=5)
```

**Impact:** 
- Cache hit rate: ~40-60% (common intents repeat)
- Latency improvement: 500ms → 10ms for cached intents
- Trade-off: 500KB memory for 100 cached intent results

**Implementation:** Add to SemanticRanker in knowledge_index_tool.py.

### Optimization 2: Batch Ranking Requests

Group multiple ranking requests into single API call:

```python
def rank_batch(self, intents: list[str], limit: int = 5) -> dict:
    """Rank multiple intents in one API call"""
    # Instead of N calls @ 500ms each = N * 500ms
    # Single call @ 800ms for batch of 10
    
    prompt = """
    Rank the following results for each intent:
    
    Intent 1: "{}": {}
    Intent 2: "{}": {}
    ...
    """.format(intents[0], results[0], intents[1], results[1])
    
    response = call_haiku_api(prompt)
    return parse_batch_results(response)
```

**Impact:**
- 10 intents: 5,000ms (sequential) → 800ms (batched) = 6.25x speedup
- Cost unchanged (same tokens)

**Trade-off:** More complex prompt engineering. Only worthwhile for bulk suggestions.

### Optimization 3: Adaptive Thresholding

Skip semantic ranking for high-confidence keyword matches:

```python
def suggest_with_adaptive_threshold(self, intent: str, limit: int = 5):
    """Use keyword-only if confidence already high"""
    keyword_results = self.search(intent, limit=10)
    
    # If top 3 keywords are >0.9 relevance, skip Haiku call
    avg_score = sum(r['score'] for r in keyword_results[:3]) / 3
    if avg_score > 0.85:
        return keyword_results[:limit]  # Skip $0.0025 API call
    
    # Otherwise, rank semantically
    return self.semantic_ranker.rank(intent, keyword_results, limit=limit)
```

**Impact:**
- Skips 30-40% of Haiku calls (high-confidence keyword matches)
- Latency improvement: 500ms → 100ms for skipped calls
- Cost savings: 30-40% reduction in ranking fees

**Precision trade-off:** Minimal (<1% precision loss for high-confidence matches).

---

## Layer 3: Proactive Suggestion Optimization

### Issue: Blocking Calls in Skill Manager

Current suggest_skills_for_intent() is synchronous, blocking user response:

```python
# SLOW: Blocks response for 500ms
def on_user_intent(intent: str):
    suggestions = suggest_skills_for_intent(intent)  # ← 500ms wait
    return response_with_suggestions(suggestions)
```

### Solution: Async Suggestions (Non-Blocking)

Move suggestion ranking to background:

```python
import asyncio

async def on_user_intent_async(intent: str):
    # 1. Keyword search (instant, ~100ms)
    keyword_results = search(intent, limit=5)
    
    # 2. Return response immediately with keywords
    response = respond_now(keyword_results)
    
    # 3. Start Haiku ranking in background (non-blocking)
    asyncio.create_task(rank_and_update_response(intent, response))
    
    return response

async def rank_and_update_response(intent: str, response_obj):
    """Runs in background, updates response after ranking completes"""
    ranked = semantic_ranker.rank(intent, limit=5)
    response_obj.add_ranked_suggestions(ranked)  # Updates response in-place
```

**Impact:**
- User sees keyword suggestions instantly (~100ms)
- Ranked suggestions appear 400ms later (perceived as "progressive enhancement")
- No blocking latency from semantic ranking

**Trade-off:** Suggests appearance complexity (response evolves). Acceptable for discovery.

---

## Monitoring & Metrics

### Essential Metrics

```python
class DiscoveryMetrics:
    def __init__(self):
        self.query_latencies = []        # [ms]
        self.ranking_latencies = []      # [ms]
        self.cache_hits = 0
        self.cache_misses = 0
        self.api_call_count = 0
        self.api_cost = 0.0
    
    def record_search(self, query: str, latency_ms: float):
        self.query_latencies.append(latency_ms)
    
    def record_ranking(self, latency_ms: float, cached: bool = False):
        self.ranking_latencies.append(latency_ms)
        if cached:
            self.cache_hits += 1
        else:
            self.cache_misses += 1
            self.api_call_count += 1
            self.api_cost += 0.0025  # Per Haiku call
    
    def summary(self):
        return {
            "search_p50": percentile(self.query_latencies, 50),
            "search_p99": percentile(self.query_latencies, 99),
            "ranking_p50": percentile(self.ranking_latencies, 50),
            "ranking_p99": percentile(self.ranking_latencies, 99),
            "cache_hit_rate": self.cache_hits / (self.cache_hits + self.cache_misses),
            "total_api_cost": self.api_cost,
        }
```

### Regression Detection

Add to test suite (test_knowledge_index_tool.py):

```python
def test_performance_sla():
    """Regression test: Ensure performance SLAs maintained"""
    metrics = DiscoveryMetrics()
    
    # Run 100 searches
    for query in [
        "rate limiting", "authentication", "caching", 
        # ... 97 more common queries
    ]:
        metrics.record_search(query, search_latency(query))
    
    summary = metrics.summary()
    
    # SLA checks
    assert summary["search_p99"] < 200, f"Search p99 exceeded: {summary['search_p99']}ms"
    assert summary["ranking_p50"] < 600, f"Ranking p50 exceeded"
    assert summary["cache_hit_rate"] > 0.4, f"Cache hit rate too low"
```

Run after each code change to detect regressions.

---

## Cache Strategy

### INDEX_metadata.json Invalidation

```python
class CacheManager:
    CACHE_PATH = "/data/INDEX_metadata.json"
    CACHE_TTL = 3600  # 1 hour
    
    def should_regenerate(self) -> bool:
        """Decide if INDEX_metadata.json needs regeneration"""
        # Check 1: File missing
        if not os.path.exists(self.CACHE_PATH):
            return True
        
        # Check 2: Cache too old (>1 hour)
        mtime = os.path.getmtime(self.CACHE_PATH)
        if time.time() - mtime > self.CACHE_TTL:
            return True
        
        # Check 3: INDEX.md changed (check hash)
        current_hash = hash_file("INDEX.md")
        cached_hash = self.load_metadata().get("_source_hash")
        if current_hash != cached_hash:
            return True
        
        return False
    
    def regenerate_if_needed(self):
        """Lazy regeneration on startup or when stale"""
        if self.should_regenerate():
            generate_index_metadata()  # ~1-2s one-time cost
```

**Invalidation triggers:**
1. Cache file missing or corrupted
2. Time-based TTL (1 hour)
3. INDEX.md hash changes (source updated)

### FTS Index Lifecycle

```python
class SearchEngine:
    def __init__(self):
        self._fts_index = None
    
    @property
    def fts_index(self):
        """Lazy FTS index initialization"""
        if self._fts_index is None:
            self._build_fts_index()
        return self._fts_index
    
    def clear_cache(self):
        """Force FTS rebuild on next search"""
        self._fts_index = None
        # Used if INDEX_metadata.json regenerated mid-session
```

---

## Implementation Checklist

Phase 4 Performance Optimization:

- [ ] **Pre-build FTS index at startup** (Quick win, ~200ms improvement)
- [ ] **Add IntentCache for common patterns** (40-60% cache hit rate)
- [ ] **Implement adaptive thresholding** (30-40% Haiku call reduction)
- [ ] **Add DiscoveryMetrics for monitoring** (Regression detection)
- [ ] **Add performance regression tests** (SLA enforcement)
- [ ] **Implement async ranking** (Non-blocking suggestions, nice-to-have)
- [ ] **Query-scoped indexes** (If scoped search becomes common)

**Quick-win order:**
1. Pre-build FTS (5 min, biggest latency impact)
2. Metrics + regression tests (10 min, long-term value)
3. Adaptive thresholding (10 min, cost reduction)
4. IntentCache (15 min, hit rate improvement)

---

## Monitoring Dashboard (Future)

For ongoing observability, track these metrics in production:

```json
{
  "timestamp": "2026-04-28T12:00:00Z",
  "search": {
    "latency_p50_ms": 75,
    "latency_p99_ms": 180,
    "queries_per_hour": 1250
  },
  "ranking": {
    "latency_p50_ms": 480,
    "latency_p99_ms": 750,
    "cache_hit_rate": 0.52,
    "api_calls_per_hour": 320,
    "cost_per_hour_usd": 0.80
  },
  "suggestions": {
    "proactive_triggers_per_hour": 480,
    "avg_suggestions_per_trigger": 3.2,
    "click_through_rate": 0.34
  }
}
```

Store in `/data/metrics.json` for trend analysis.

---

## Summary

**Primary optimization targets:**
1. **FTS startup cost** → Pre-build index (biggest single-session impact)
2. **Semantic ranking latency** → Adaptive thresholding + caching (best throughput improvement)
3. **Cost** → Cache + adaptive thresholding (30-40% cost reduction possible)

**Expected outcomes after full Phase 4 optimization:**
- Keyword search: ~100ms (unchanged, already optimal)
- Semantic ranking: ~200ms avg (down from 500ms via caching + adaptive threshold)
- Proactive suggestions: <100ms perceived (non-blocking via async)
- Cost: ~60% reduction in API spend (~$0.30/hr → $0.12/hr estimated)
- Precision: Maintained at 95% (adaptive threshold has <1% precision loss)
