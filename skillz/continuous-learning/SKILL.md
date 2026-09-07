---
name: continuous-learning
description: Automatically extract reusable patterns from Claude Code sessions and save them as learned skills for future use.
origin: ECC
---

# Continuous Learning Skill

Automatically evaluates Claude Code sessions at the end and extracts reusable patterns that can be saved as learned skills.

## When to Activate

- Setting up automatic pattern extraction from Claude Code sessions
- Configuring the Stop hook for session evaluation
- Reviewing or editing learned skills in `~/.claude/skills/learned/`
- Adjusting extraction thresholds or pattern categories
- Comparing the v1 (this) and v2 (instinct-based) approaches

## How It Works

This skill runs as a **Stop hook** at the end of each session:

1. **Session Evaluation**: Checks whether the session has enough messages (default: 10+)
2. **Pattern Detection**: Identifies extractable patterns from the session
3. **Skill Extraction**: Saves useful patterns to `~/.claude/skills/learned/`

## Configuration

Edit `config.json` to customize:

```json
{
  "min_session_length": 10,
  "extraction_threshold": "medium",
  "auto_approve": false,
  "learned_skills_path": "~/.claude/skills/learned/",
  "patterns_to_detect": [
    "error_resolution",
    "user_corrections",
    "workarounds",
    "debugging_techniques",
    "project_specific"
  ],
  "ignore_patterns": [
    "simple_typos",
    "one_time_fixes",
    "external_api_issues"
  ]
}
```

## Pattern Types

| Pattern | Description |
|---------|-------------|
| `error_resolution` | How specific errors were resolved |
| `user_corrections` | Patterns from user corrections |
| `workarounds` | Solutions to framework/library quirks |
| `debugging_techniques` | Effective debugging approaches |
| `project_specific` | Project-specific conventions |

## Hook Setup

Add to your `~/.claude/settings.json`:

```json
{
  "hooks": {
    "Stop": [{
      "matcher": "*",
      "hooks": [{
        "type": "command",
        "command": "~/.claude/skills/continuous-learning/evaluate-session.sh"
      }]
    }]
  }
}
```

## Why a Stop Hook?

- **Lightweight**: Runs once at the end of the session
- **Non-blocking**: Doesn't add latency to every message
- **Full Context**: Has access to the complete session record

## Related

- [The Longform Guide](https://x.com/affaanmustafa/status/2014040193557471352) - Continuous learning section
- `/learn` command - Manual mid-session pattern extraction

---

## Comparison Notes (Research: January 2025)

### vs Homunculus

Homunculus v2 takes a more sophisticated approach:

| Feature | Our Approach | Homunculus v2 |
|---------|--------------|---------------|
| Observation | Stop hook (end of session) | PreToolUse/PostToolUse hooks (100% reliable) |
| Analysis | Main context | Background agent (Haiku) |
| Granularity | Full skills | Atomic "instincts" |
| Confidence | None | 0.3-0.9 weighted |
| Evolution | Directly to skill | Instincts → clustering → skill/command/agent |
| Sharing | None | Export/import instincts |

**Key insight from Homunculus:**
> "v1 relied on skills for observation. Skills are probabilistic—they trigger roughly 50-80% of the time. v2 uses hooks for observation (100% reliable) and instincts as the atomic unit of learned behavior."

### Potential v2 Improvements

1. **Instinct-based learning** - Smaller, atomic behaviors with confidence scoring
2. **Background observer** - A Haiku agent that analyzes in parallel
3. **Confidence decay** - Instincts lose confidence when contradicted
4. **Domain tagging** - code-style, testing, git, debugging, etc.
5. **Evolution path** - Clustering related instincts into skills/commands

See `docs/continuous-learning-v2-spec.md` for the full spec.
