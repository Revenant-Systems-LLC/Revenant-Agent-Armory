# Writing Discoverable Tool Descriptions

Phase 4 best practices: How to write skill, agent, and tool descriptions that surface in discovery queries.

## The Problem

With 16,639+ indexed items, discoverability depends on:
1. **Keyword relevance** — Does your description contain search terms?
2. **Semantic matching** — Does it address the user's intent?
3. **Trigger patterns** — Are problem-discovery triggers present?

A skill named "async-coordinator" with description "Manages async operations" will rarely surface in queries like:
- "How do I handle concurrent tasks?"
- "What helps with task scheduling?"
- "Non-blocking I/O patterns?"

The same skill with an expanded description would match all three.

---

## Anatomy of a Discoverable Description

### Structure (120-200 words)

```
[Core Function] [Problems Solved] [Key Capabilities] [Related Patterns]
```

### Example: Before

```
Manages asynchronous operations and concurrent task execution.
```

### Example: After

```
Coordinates concurrent task execution without blocking the main thread.
Use for: handling multiple I/O operations simultaneously, task scheduling,
managing long-running processes, orchestrating parallel workflows.

Solves problems like: slow request handling from blocking operations,
race conditions in concurrent code, coordination of dependent async tasks.

Key capabilities: Promise-based concurrency, task queuing, parallel execution,
backpressure handling, error recovery in async chains.

Related: Event loops, non-blocking I/O, task scheduling, concurrency patterns,
Promise/async-await, reactive programming.
```

---

## Keyword Density Guide

### DO: Include User Intent Keywords

Search queries typically follow patterns:
- **"How do I [verb] [object]?"** — Include verbs (validate, cache, limit, retry)
- **"What helps with [problem]?"** — Include problem domain (rate-limiting, auth, scaling)
- **"Find tools for [pattern]?"** — Include design pattern names (circuit-breaker, queue, pool)

**Example: Rate Limiter**

```
Enforces request limits to prevent system overload.

Problems: Too many requests overwhelming your API, unfair resource sharing,
denial-of-service vulnerability, cascading failures under spike traffic.

How to use: Set limits per user, per IP, per endpoint. Choose algorithms:
token-bucket, sliding-window, fixed-window. Integrate with auth system.

Handles: Request throttling, quota enforcement, burst absorption, fair queueing,
traffic shaping, backpressure signaling, graceful degradation under load.

Algorithms: Token bucket (smooth bursts), sliding window (precise), 
fixed-window (simple), leaky bucket (regulated output).

Related: Circuit breaker, bulkhead isolation, adaptive timeout, 
graceful shutdown, queue management, backpressure.
```

**Keywords matched:**
- "limit" (request limiting)
- "throttle" (traffic control)
- "quota" (resource management)
- "prevent overload" (capacity)
- "rate-limit" (problem domain)
- "spike" (load pattern)
- "token-bucket" (algorithm)

### DON'T: Vague Umbrella Terms

❌ "Provides utilities for system operations"  
✅ "Executes shell commands, manages processes, handles signals, pipes output"

❌ "Handles data transformation"  
✅ "Parses JSON/XML, maps fields, filters arrays, validates schemas, converts types"

❌ "Improves performance"  
✅ "Caches expensive operations, reduces API calls, indexes for O(1) lookup, batches requests"

---

## Section-by-Section Guide

### 1. One-Line Core Function

**Format:** `[Verb] [Object] [Benefit/Constraint]`

✅ Good:
- "Validates user input against security rules without blocking requests"
- "Retries failed requests with exponential backoff and circuit breaking"
- "Compresses response bodies to reduce bandwidth by 70%+"

❌ Weak:
- "Handles input validation"
- "Manages request retries"
- "Compresses data"

### 2. Problem Statement (What triggers search)

**Format:** List 3-5 concrete problems, not abstractions.

✅ Good:
```
Problems this solves:
- Malicious input injection (XSS, SQL injection, command injection)
- Form validation errors go unnoticed until production
- Security compliance: OWASP injection prevention
- Inconsistent validation across different endpoints
```

❌ Weak:
```
- Input handling
- Validation logic
- Security concerns
```

### 3. Key Capabilities

**Format:** Concrete verbs + objects, not feature lists.

✅ Good:
```
Key capabilities:
- Escapes HTML/JavaScript in all contexts (attributes, text, event handlers)
- Validates against whitelists for strict input types
- Rate-limits registration attempts per IP and per email
- Detects and blocks common XSS patterns (eval, onclick, onerror)
```

❌ Weak:
```
- Input validation
- Security enforcement
- Rate limiting
- Pattern detection
```

### 4. Related Patterns & Techniques

**Format:** Architecture patterns, algorithms, related concepts.

✅ Good:
```
Related patterns: Defense-in-depth, whitelist validation, Content Security Policy,
parameterized queries, stored procedures, input normalization, output encoding.

Algorithms: Finite state automata for pattern matching, bloom filters for 
fast rejection, trie-based whitelisting.
```

❌ Weak:
```
- Security
- Patterns
- Related concepts
```

---

## Search Query → Description Matching

### Query: "How do I handle auth tokens securely?"

**Matched descriptions must contain:**
- Problem keywords: "token", "auth", "security", "credential"
- Capability verbs: "store", "encrypt", "validate", "expire", "rotate"
- Related patterns: "OAuth", "JWT", "session", "refresh token"

**Score increases for:**
- Sequence match: "auth tokens" appears near "securely" (context)
- Semantic closeness: "credential" is synonym for "token"
- Intent alignment: Description addresses "secure handling" intent

### Query: "Rate limiting for APIs"

**Exact matches:**
- "rate limit", "request limit", "throttle", "quota"

**Semantic matches:**
- "prevent overload", "DoS protection", "traffic shaping"
- "token-bucket", "sliding-window", "circuit-breaker"

**Intent alignment:**
- Description frames problem in API context (not general networking)
- Solutions positioned for API endpoints specifically

---

## Length Guidelines

| Section | Char Count | Why |
|---------|-----------|-----|
| Core function | 50-100 | Concise, scannable |
| Problems | 150-250 | Concrete examples, multiple angles |
| Capabilities | 100-200 | Specific, actionable |
| Related | 100-150 | Pattern vocabulary for semantic matching |
| **Total** | **400-700** | FTS indexes first ~400 chars, longer = more keywords |

**Note:** Knowledge system truncates to 400 chars for FTS efficiency, but full description used for semantic ranking.

---

## Trigger Pattern Examples

These phrases, when in descriptions, help discovery trigger proactively:

### Concurrency
- "handle concurrent requests"
- "parallel execution"
- "non-blocking I/O"
- "task scheduling"
- "async/await"

### Security
- "prevent injection"
- "validate input"
- "authenticate users"
- "encrypt data"
- "OWASP compliance"

### Scaling
- "handle load spikes"
- "prevent overload"
- "bottleneck elimination"
- "horizontal scaling"
- "capacity planning"

### Resilience
- "retry failed requests"
- "circuit breaker"
- "graceful degradation"
- "error recovery"
- "timeout handling"

### Observability
- "structured logging"
- "distributed tracing"
- "metrics collection"
- "error reporting"
- "performance monitoring"

---

## Checklist: Is Your Description Discoverable?

- [ ] **Core function**: One sentence, includes primary verb + object
- [ ] **Problems**: 3+ concrete problem statements (user can see themselves in one)
- [ ] **Keywords**: Search terms like "rate limiting" not "request management"
- [ ] **Verbs**: Concrete actions ("escape HTML", "validate schema") not abstractions
- [ ] **Related**: Lists 3+ patterns, algorithms, or related concepts
- [ ] **Length**: 400-700 characters (400-char truncation limit considered)
- [ ] **Intent triggers**: Contains 2+ of: "how do I", "prevent", "handle", "solve", "improve"
- [ ] **Examples**: At least one concrete use case scenario
- [ ] **No jargon alone**: Every technical term paired with concrete impact
- [ ] **User-centric**: Frames features in terms of problems solved, not capabilities

---

## Real Examples from The Ossuary

### ✅ Well-Discoverable

**rate-limiter:**
```
Prevents API overload by limiting requests per user/IP using token-bucket 
or sliding-window algorithms.

Problems: Handling traffic spikes, protecting against DoS attacks, ensuring 
fair resource allocation, preventing cascading failures when downstream 
services slow down.

Capabilities: Per-user rate limits, per-IP blocking, burst absorption, 
adaptive limits based on load, graceful backoff responses.

Algorithms: Token bucket (smooth bursts), sliding window (accurate), 
fixed window (simple), leaky bucket (shaped output).

Related: Circuit breaker, bulkhead isolation, load balancing, traffic shaping,
backpressure, queue management, adaptive timeout.
```

**Why it's discoverable:**
- 4 problem statements users can identify with
- 5+ capability descriptions with concrete verbs
- 5+ algorithm/pattern terms for semantic matching
- Total: 625 characters (exceeds 400-char threshold, semantic ranker gets full text)

### ❌ Under-Discoverable

**rate-limiter (weak version):**
```
Rate limiting for requests.
```

**Why it's poor:**
- Generic problem statement (user doesn't see their problem reflected)
- Single verb ("limiting") with no qualifiers
- No algorithm information
- Only 40 characters (misses FTS threshold for keyword density)

---

## Integration with Discovery System

**FTS Search (Keyword):**
- Searches: name, description (first 400 chars), directory, category
- Ranking: Exact match > word boundary > substring
- Speed: ~100ms for "rate limit" query across 16,639 items

**Semantic Ranking (Intent):**
- Input: Top 10 keyword results + user intent ("I need to prevent API overload")
- Claude Haiku: Scores each result for relevance to intent
- Output: Top 5 reranked by semantic closeness (95% precision)

**Recommendation:** Write descriptions assuming full 400-700 char space, knowing FTS uses first ~400 and semantic ranker uses full text.

---

## Maintenance

When updating descriptions:
1. Run tests: `python test_knowledge_index_tool.py`
2. Regenerate INDEX metadata: `python generate_index_metadata.py`
3. Validate discoverability: Search for your problem statement
4. Check FTS index: Run "search" action for your keywords

Changes to descriptions don't require code updates — INDEX_metadata.json regeneration picks up changes automatically.
