# Catalog.json Sync Strategy — Phase 4 Maintenance

## Problem Statement

You maintain two data sources:
1. **INDEX.md** — Source of truth for 16,639+ items (agents, skills, tools, etc.)
2. **catalog.json** — Runtime skill metadata with 1,436 trigger patterns and tags

When you add items randomly and often, both sources can diverge:
- New skill added to catalog.json but not documented in INDEX.md
- INDEX.md updated but catalog.json triggers/tags don't reflect changes
- Duplicate entries appear in search results (CatalogUnifier merges both)
- Stale triggers point to non-existent skills

**Goal:** Keep both sources in sync with minimal manual effort, and ensure discovery always returns correct results even during frequent updates.

---

## Canonical Source Principle

**Rule: INDEX.md is the canonical source.**

When catalog.json and INDEX disagree:
1. INDEX.md takes precedence for basic metadata (name, description, directory)
2. catalog.json provides *enrichment only* (triggers, tags, skill-specific metadata)
3. CatalogUnifier enforces this priority during merge

```python
# From knowledge_index_tool.py CatalogUnifier.merge()
def merge(self, index_items: list, catalog_items: list) -> list:
    """Merge INDEX (canonical) with catalog (enrichment)"""
    seen = set()
    merged = []
    
    # Priority 1: INDEX items (canonical source)
    for item in index_items:
        merged.append(item)
        seen.add(item['name'].lower())
    
    # Priority 2: Catalog items not in INDEX (new catalog-only skills)
    for item in catalog_items:
        if item['name'].lower() not in seen:
            merged.append(item)
            seen.add(item['name'].lower())
    
    return merged
```

**Implication:** You can freely add skills to catalog.json without breaking search. INDEX.md remains the source of truth.

---

## Workflow: Adding New Skills

### Scenario 1: New Skill (Most Common)

You create a new skill and want it discoverable immediately.

**Option A: Catalog-First (Fastest)**
```json
{
  "id": "my-new-skill",
  "name": "My New Skill",
  "description": "Does something useful",
  "category": "skills",
  "tags": ["useful", "my-category"],
  "triggers": ["how do I", "what helps with"],
  "path": "skills/my-new-skill/SKILL.md"
}
```

Add to `catalog.json` immediately. Discovery works right away.

**Later (when you have time):** Document it in INDEX.md under the appropriate directory (agents/, skills/, tools/, etc.). No rush — catalog.json keeps it searchable.

**Option B: INDEX-First (Preferred Long-Term)**

If you're documenting anyway, add to INDEX.md first:
```markdown
## My New Skill

**Role:** Does something useful

**Problems:** Solves X, prevents Y

**How to use:** Works with A, integrates with B
```

Then add enrichment to catalog.json with triggers/tags. Both sources in sync from the start.

**Recommendation:** Use Option A for rapid iteration (add to catalog.json), then backfill INDEX.md weekly.

### Scenario 2: Skill Already in INDEX.md

Skill exists in INDEX.md but catalog.json is stale or missing.

**Option 1: Regenerate metadata** (Recommended)
```bash
python generate_index_metadata.py
```

This rebuilds INDEX_metadata.json from INDEX.md. FTS search immediately picks up the latest version.

**Option 2: Manual catalog.json entry**

If you don't want to regenerate metadata yet, manually add catalog.json entry with INDEX.md data:
```json
{
  "id": "existing-skill",
  "name": "Existing Skill",
  "description": "From INDEX.md (copied)",
  "category": "skills",
  "tags": ["manually-added"],
  "triggers": ["copy from INDEX.md if present"],
  "path": "skills/existing-skill/SKILL.md"
}
```

**When to use:** Quick fix before you have time to regenerate metadata.

---

## Sync Mechanisms

### Strategy 1: Manual Regeneration (Current)

When you add items to INDEX.md:
```bash
python generate_index_metadata.py
```

This:
1. Parses INDEX.md
2. Generates INDEX_metadata.json
3. Rebuilds FTS search index
4. CatalogUnifier uses latest data on next search

**Frequency:** Weekly or after significant INDEX.md updates

**Pros:**
- Simple, no automation needed
- Full control over sync timing
- Can batch multiple INDEX.md changes

**Cons:**
- Manual step, easy to forget
- Delay between INDEX change and discoverability

### Strategy 2: Git Hook (Automation)

Auto-regenerate metadata when INDEX.md is committed:

```bash
# .git/hooks/post-commit
#!/bin/bash
if git diff-tree --no-commit-id --name-only -r HEAD | grep -q "INDEX.md"; then
    python generate_index_metadata.py
    git add data/INDEX_metadata.json
    git commit --amend --no-edit
fi
```

**Effect:** Every commit that touches INDEX.md automatically regenerates metadata.

**Pros:**
- Automatic, no manual steps
- Metadata always current

**Cons:**
- Git hook overhead (~500ms per commit)
- Requires Python in git hook environment

### Strategy 3: File Watcher (Development)

Monitor INDEX.md for changes and auto-regenerate during dev:

```python
# watch_index.py
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

class IndexHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if "INDEX.md" in event.src_path:
            print("INDEX.md changed, regenerating...")
            subprocess.run(["python", "generate_index_metadata.py"])

observer = Observer()
observer.schedule(IndexHandler(), path=".", recursive=True)
observer.start()
```

Run during development: `python watch_index.py`

**Pros:**
- Real-time regeneration
- Instant discoverability during authoring

**Cons:**
- Requires extra process running
- Not suitable for production

**Recommendation for your use case:** Use Strategy 1 (manual) + Strategy 3 (file watcher during active work). You add items randomly, so automatic regeneration on every commit (Strategy 2) has too much overhead.

---

## Conflict Resolution

### Conflict Type 1: Duplicate Names

**Scenario:** INDEX.md has `security-validator` and catalog.json also has `security-validator`, but descriptions differ.

**Resolution:**
```python
# CatalogUnifier deduplicates by name
def merge(self, index_items: list, catalog_items: list) -> list:
    seen = set()
    for item in index_items:
        if item['name'].lower() not in seen:
            result.append(item)
            seen.add(item['name'].lower())
    
    for item in catalog_items:
        if item['name'].lower() not in seen:  # ← Skip if already in INDEX
            result.append(item)
            seen.add(item['name'].lower())
    
    return result
```

**Outcome:** INDEX.md version wins (canonical source). Catalog.json duplicate is silently dropped.

**To fix:** Remove duplicate from catalog.json or update INDEX.md if catalog.json is more current.

### Conflict Type 2: Stale Description

**Scenario:** INDEX.md describes skill as "validates input", but catalog.json says "does XYZ" (outdated).

**Resolution:**
```python
# FTS search uses INDEX.md + INDEX_metadata.json
def search(self, query: str):
    results = self.fts_index.search(query)  # ← From INDEX_metadata.json
    # Catalog.json only used for enrichment (triggers, tags)
```

**Outcome:** Search results show INDEX.md description (canonical). Catalog.json stale data doesn't appear in results.

**To fix:** Update catalog.json to match INDEX.md, or regenerate metadata if INDEX.md is more current.

### Conflict Type 3: Missing in Catalog

**Scenario:** New skill added to INDEX.md but catalog.json has no entry yet.

**Resolution:**
```python
# CatalogUnifier handles missing catalog entries gracefully
result = merge(
    index_items=[{"name": "new-skill", ...}],
    catalog_items=[],
)
# New skill appears in results with INDEX.md metadata
# No catalog triggers/tags, but that's OK — basic discoverability works
```

**Outcome:** Skill is discoverable via keyword search. Trigger patterns won't fire until catalog.json is updated.

**To fix:** Add catalog.json entry with triggers when you have time. Search works in the meantime.

---

## Validation & Monitoring

### Validation Script

Run this after major updates to detect issues:

```python
# validate_sync.py
import json
import re

def validate_sync():
    """Check INDEX.md and catalog.json for sync issues"""
    
    # Load both sources
    with open("INDEX.md") as f:
        index_content = f.read()
    with open("data/catalog.json") as f:
        catalog = json.load(f)
    
    # Extract all item names from INDEX.md
    index_items = set(re.findall(r"^## (\S+)", index_content, re.MULTILINE))
    catalog_items = {item['name'] for item in catalog}
    
    # Check for issues
    issues = {
        "in_index_not_catalog": index_items - catalog_items,
        "in_catalog_not_index": catalog_items - index_items,
        "duplicates_in_catalog": find_duplicates(catalog),
    }
    
    # Report
    if issues["in_index_not_catalog"]:
        print(f"⚠️  {len(issues['in_index_not_catalog'])} items in INDEX but not catalog:")
        for item in sorted(issues["in_index_not_catalog"]):
            print(f"   - {item}")
    
    if issues["in_catalog_not_index"]:
        print(f"⚠️  {len(issues['in_catalog_not_index'])} items in catalog but not INDEX:")
        for item in sorted(issues["in_catalog_not_index"]):
            print(f"   - {item}")
    
    if issues["duplicates_in_catalog"]:
        print(f"❌ {len(issues['duplicates_in_catalog'])} duplicate entries in catalog:")
        for item in issues["duplicates_in_catalog"]:
            print(f"   - {item}")
    
    return len(issues["duplicates_in_catalog"]) == 0  # Fail only on duplicates
```

Run before committing: `python validate_sync.py`

### Monitoring Metrics

Track these in `/data/sync_metrics.json`:

```json
{
  "timestamp": "2026-04-28T14:00:00Z",
  "index_item_count": 16639,
  "catalog_item_count": 1436,
  "duplicates_found": 0,
  "orphaned_catalog_items": 23,
  "missing_catalog_entries": 145,
  "last_regeneration": "2026-04-28T13:00:00Z",
  "regeneration_frequency_days": 2
}
```

**Green flags:** Regeneration every 1-3 days, <10 orphaned items, 0 duplicates

**Red flags:** >50 missing entries (sync drifted), >0 duplicates (needs cleanup)

---

## Best Practices

### 1. Batch Updates (Weekly Regeneration)

Instead of regenerating metadata after every change:

**Monday-Friday:** Add to catalog.json freely. Discovery works immediately.

**Friday EOD:** 
```bash
# Bulk update INDEX.md with new/changed items
# Then regenerate once
python generate_index_metadata.py
git add INDEX.md data/INDEX_metadata.json
git commit -m "Weekly catalog sync: 12 new skills added"
```

**Benefit:** Fewer regenerations (cheaper), all changes batched together.

### 2. Catalog.json Enrichment Only

Use catalog.json for:
- ✅ Trigger patterns ("how do I", "what helps with")
- ✅ Tags ("performance", "security", "observability")
- ✅ Skill-specific metadata (version, author, lifecycle status)

Don't use catalog.json for:
- ❌ Core descriptions (use INDEX.md)
- ❌ Directory structure (use INDEX.md)
- ❌ Long-form documentation (use INDEX.md)

### 3. Name Consistency

When creating new skills, use consistent naming:
- Hyphenated: `my-new-skill` (not `myNewSkill` or `my_new_skill`)
- Lowercase: `security-validator` (not `SecurityValidator`)
- Meaningful: `async-coordinator` (not `tool-1`)

**Why:** CatalogUnifier deduplicates by lowercase name. Inconsistent casing = duplicates in results.

### 4. Document Triggers

Trigger patterns are crucial for discovery. When adding to catalog.json, include at least 2-3 triggers:

```json
{
  "name": "rate-limiter",
  "triggers": [
    "how do I limit requests",
    "what helps with rate limiting",
    "prevent API overload",
    "handle traffic spikes"
  ]
}
```

**Why:** Proactive suggestions use triggers to match user intents. More triggers = better discovery.

---

## Checklist: Adding a New Skill

When you add a new skill and want it discoverable:

- [ ] **Immediate (catalog.json):**
  - [ ] Add entry to catalog.json with name, description, category
  - [ ] Include 3+ trigger patterns
  - [ ] Add relevant tags
  - [ ] Create skill file in skills/ directory
  - [ ] Search/discovery works immediately

- [ ] **Weekly (INDEX.md + regeneration):**
  - [ ] Document in INDEX.md under appropriate directory (agents/, skills/, tools/, etc.)
  - [ ] Run `python generate_index_metadata.py`
  - [ ] Validate with `python validate_sync.py`
  - [ ] Commit both INDEX.md and data/INDEX_metadata.json

- [ ] **Monthly (cleanup):**
  - [ ] Check for orphaned catalog entries (items in catalog but not created)
  - [ ] Update stale descriptions
  - [ ] Review trigger patterns for accuracy
  - [ ] Verify no duplicates exist

---

## Summary

**Your workflow for random, frequent additions:**

1. **Immediately:** Add to catalog.json → discovery works in <100ms
2. **Weekly:** Batch updates into INDEX.md → run regenerate metadata script
3. **Validate:** Use validation script before committing
4. **Monitor:** Track sync_metrics.json for drift

**Key principle:** INDEX.md is source of truth. Catalog.json is enrichment. CatalogUnifier enforces priority. You can't break discovery by adding items randomly — the system is resilient to divergence.

**Automation options:**
- Manual: Regenerate weekly (recommended for your use case)
- Git hook: Auto-regenerate on commit (adds overhead)
- File watcher: Real-time during active development (dev only)

**Next step:** Set a weekly calendar reminder to regenerate metadata after your last skill additions of the week.
