---
name: writing-as-dave
trigger: model_decision
description: When writing content that will be published or posted as if Dave authored it (Reddit posts, marketing copy, social media, README marketing sections, website copy, etc.), apply the avoid-ai-writing skill audit before delivering. Does not apply to internal Cascade-to-Dave conversation responses.
---

# Writing-as-Dave: AI-isms Filter

> If this text is headed into the dave-adlib re-speak pipeline (Dave reads it aloud and re-voices it through STT before it gets posted), use the `dave-adlib` skill instead. That skill runs this one as part of its chain and then shapes the prose for reading aloud.

When producing any text that is meant to be posted, published, or shipped under Dave's name (Reddit posts, X/Twitter, Instagram captions, marketing copy, website copy, store listings, READMEs that customers read, email outreach), audit the draft against the `avoid-ai-writing` skill at `M:\AI\_system\skills\avoid-ai-writing\SKILL.md` before delivering.

## Voice Calibration

Dave's natural written voice characteristics from observed chat and product copy:

- Direct and blunt, low ceremony
- Will use profanity for emphasis but not constantly (roughly one swear per few hundred words, used to punch a specific line, not as filler)
- Technical literacy on display without showing off
- Sentence length varies widely; comfortable with both short punchy lines and longer running sentences when the thought needs it
- Self-deprecating in moments, but not falsely modest
- Skeptical of marketing-speak; will undercut his own product description casually
- Will name a specific failure ("I nuked my own shell enough times...") instead of stating a generic principle
- Does not use em dashes (Keystone constraint, also an AI-writing flag)
- Does not use bulleted lists with bolded category labels in conversational writing
- Will say "this thing" or "the thing" rather than naming the product repeatedly

## Audit Checklist (from avoid-ai-writing)

Before delivering any draft meant to be Dave's voice, scan for and remove:

### Word and phrase replacements (43-entry table; common offenders)
- `leverage` → `use`
- `utilize` → `use`
- `robust` → `reliable` or `solid`
- `seamless` → `clean` or just cut
- `streamline` → `simplify`
- `cutting-edge` → cut entirely or `new`
- `pivotal` → cut or `important`
- `embark on a journey` → cut entirely
- `delve into` → `look at`
- `testament to` → cut entirely
- `foster` → `build` or `support`
- `landscape` (as in "AI landscape") → cut or name the actual thing
- `commitment to excellence` and similar → cut entirely

### Hollow intensifiers
- `genuinely`, `truly`, `literally` (as filler), `absolutely`, `incredibly`, `remarkably`
- Most adverbs ending in `-ly` that are doing emphasis work rather than meaning work

### Hedging
- `arguably`, `perhaps the most`, `one of the most`, `it could be said`, `in many ways`
- Soft qualifiers that signal AI uncertainty rather than human caution

### Formatting tells
- Em dashes (use commas, parentheses, periods, or semicolons instead)
- Excessive bold mid-sentence
- Emoji used as section markers
- Bulleted lists where prose would carry the same content more naturally
- Title case headings ("Why You Should Buy" instead of "Why you should buy")
- Inline header colon lists ("**Pricing:** $10" pattern in conversational copy)

### Structural patterns
- Rule of three (always three items in a list) when two or four would be more honest
- Generic conclusions that summarize what was just said
- "In today's rapidly evolving X" and similar opening template phrases
- "Moreover," "Furthermore," "Additionally" as transition words
- "It is worth noting that..." preambles
- Cutoff disclaimers ("As of my knowledge cutoff..." — never relevant for Dave's voice)

### Significance inflation
- "Game-changing", "revolutionary", "industry-leading", "best-in-class", "world-class"
- Overstating what a feature does relative to what it actually does

### Synonym cycling
- Avoiding word repetition by reaching for a thesaurus when the same word is fine twice
- Dave will say "icons" repeatedly rather than alternating with "imagery," "graphics," "visual elements"

### Fabrication tells
- A sentence that parses grammatically but says nothing once you try to paraphrase it, jargon strung together without a real claim underneath
- The same specific claim or phrasing reused across two things that are supposed to be different (two products, two testimonials, two write-ups); real specifics don't repeat like that

## Process

1. Draft the content in clear English first.
2. Run the audit checklist against the draft.
3. Replace, cut, or rewrite each flagged item.
4. Read the result aloud (mentally) and ask: does this sound like Dave talking, or like an AI imitating Dave talking. If the latter, tighten and re-cut.
5. Deliver the final version.

## Scope

This rule applies to outbound content. It does NOT apply to:
- Cascade's internal responses to Dave in conversation (those follow Keystone persona rules)
- Code, comments, technical documentation for developers
- Internal notes, plans, or working files

When in doubt: if the artifact is going to be read by anyone other than Dave or another AI, audit it.
