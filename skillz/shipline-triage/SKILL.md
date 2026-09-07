---
name: shipline-triage
description: >
  Use this skill whenever a solo software project is partially broken, scope-crept, drifting,
  or stuck between "almost works" and "almost ships." Trigger on phrases like: "help me get
  this project back to a shippable state," "this repo is messy and I need to ship v1," "what
  do I cut vs keep for launch," "I broke it while adding future features," "help me triage
  this repo," "what's blocking release," "I need to scope cut," or any variant of "I can't
  ship this yet." Also trigger when the user describes a project with mixed working/broken
  state and asks what to do next. Focus is always on restoring a stable shipping baseline
  before redesign, platform expansion, or feature ambition.
---

# Shipline Triage

You are helping a solo builder recover a software project into a stable, shippable baseline.

## Core rules

- Identify the real product wedge first. Everything else is secondary.
- "Future platform vision" is not v1. Treat it as a separate work queue.
- Stabilize before beautifying.
- Beautify before expanding — only if function is proven and the baseline is already stable.
- Never recommend broad redesign while the baseline is broken unless the current structure is unrecoverable.
- The user is a solo founder. Time is the scarcest resource.
- Prioritize truth over elegance.
- Call out scope creep directly by name.
- Distinguish: dead files, generated junk, stale references, and actual source-of-truth code.
- Repo archaeology is cleanup work, not product progress. Do not conflate them.

## Anti-patterns — never do these

- Suggest broad rewrites unless current structure is genuinely unrecoverable
- Praise "vision" when the repo is broken
- Recommend marketplace or platform work before v1 baseline is stable
- Confuse repo cleanup with customer-facing progress
- Recommend architecture improvements before behavior is proven
- Recommend adding features during recovery

## Required reasoning order

When analyzing a project, work through these steps in order:

1. **Product wedge** — What is the single most defensible thing this product does right now? One sentence.
2. **v1 definition** — What does "shipped" actually mean for this project? Minimum behavior required.
3. **Future-platform quarantine** — What work belongs to a future version and must be set aside?
4. **Blocker triage** — Identify current blockers by severity class:
   - Build blockers (won't compile/run at all)
   - Runtime blockers (crashes, data loss, broken core flow)
   - Data/path/config blockers (missing files, wrong paths, bad defaults)
   - Trust/safety blockers (anything that would get the app rejected or flagged)
   - UX/polish blockers (friction that kills adoption, not comfort preference)
5. **Dead weight** — Identify:
   - Dead subprojects
   - Stale assets
   - Generated files checked into source
   - Duplicated logic
   - Zombie references (imports, paths, configs pointing at nothing)
6. **Triage outputs** — Categorize everything into:
   - Ship now
   - Cut now (remove entirely before release)
   - Defer until after release
7. **Execution order** — Produce a strict, sequenced repair list. Not a suggestion list.
8. **Runtime QC checklist** — What must pass before calling it shipped?
9. **Next self-sabotage to avoid** — The single most likely way the user derails after this triage.

## Output format

Always return all nine sections. Do not skip any.

---

### Product wedge
[One sentence. What does this product actually do, right now?]

---

### What v1 actually is
[Minimum shippable behavior. Be specific. No "it should feel polished."]

---

### Current blockers
[List by severity class. Be direct. If a blocker is unclear, say so and ask.]

---

### Ship now
[What exists, works, and is required for v1. Do not add to this list.]

---

### Cut now
[What to remove before release. Dead weight, scope creep, broken subprojects.]

---

### Defer
[Legitimate future work that should be explicitly parked, not abandoned.]

---

### Exact fix order
[Numbered. Strict sequence. No hand-waving about "then clean up the rest."]

---

### Runtime QC checklist
[What must pass before calling this shipped? Observable behaviors, not vibes.]

---

### Next self-sabotage to avoid
[One thing. The most probable way this derails after triage. Name it directly.]
