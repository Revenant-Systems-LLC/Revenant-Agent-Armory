# AI-Agent-Armory Directory Index

**Location:** B:\AI-Armory
**Updated:** 2026-08-01 (counts re-measured against disk)
**Total files:** 12030 across 29 top-level categories

> **SOP (the Windsurf rule):** Read THIS index first. Pull ONLY the skills/agents/plugins the task needs. NEVER absorb, walk, or bulk-load the whole Armory. Selective pull = scoped agency; the token cost is the guardrail.

## Categories (live counts)

| Category | Subfolders | Files | Purpose |
|---|---:|---:|---|
| .rev-agentz | 82 | 192 | Revenant agent bundles |
| .vs | 6 | 13 |  |
| adapterz | 13 | 36 | Per-tool adapters (claude-code, codex, cursor...) |
| agentz | 11 | 274 | Agent / subagent definitions |
| apiz | 19 | 21 | API catalogs by domain |
| assetz | 0 | 12 | Assets |
| cheatsheetz | 0 | 41 | Language / tool cheatsheets |
| cliz | 0 | 155 | CLI references |
| commandz | 2 | 182 | Slash commands |
| contextz | 44 | 114 | Context files & captured system prompts |
| dataz | 0 | 62 | Data catalogs |
| docz | 3 | 14 | Docs |
| gatewayz | 0 | 211 | Gateway / channel delivery system |
| hookz | 4 | 61 | Hooks (git + Claude Code lifecycle) |
| maintainz | 0 | 20 | Maintenance |
| marketplacez | 319 | 544 | Marketplace bundles |
| mcpz | 3 | 6 | MCP servers & configs |
| planz | 1 | 22 | Plans & workflows |
| platformz | 1 | 41 | Platform integrations |
| pluginz | 451 | 1267 | Plugins (one folder per plugin) |
| resourcez | 759 | 4034 | Reference data (patterns, schemas, design tokens) |
| rulez | 27 | 147 | Coding / behavioral rules |
| scriptz | 0 | 57 | Utility scripts |
| skill-pakz | 234 | 398 | Productized RS Skill Packs |
| skillz | 1885 | 3159 | Skills (one folder per skill, SKILL.md) |
| templatez | 211 | 868 | Templates, scaffolds, prompt/design templates |
| testz | 0 | 5 | Tests |
| tickerz | 0 | 4 | Tickers |
| toolz | 1 | 70 | Python tool modules |

## 2026-07-12 Refill (source provenance)

Harvested copy-only (robocopy, no move/mirror) from 14 repos in M:\Projects, namespaced by source inside each category. Existing pre-refill content untouched.

| Source (M:\Projects\) | Landed in | Files |
|---|---|---:|
| andrej-karpathy-skills\skills | skillz\andrej-karpathy-skills | 1 |
| awesome-claude-skills | skillz\awesome-claude-skills | 1141 |
| claude-cookbooks\skills | skillz\claude-cookbooks | 33 |
| ECC\skills | skillz\ECC | 449 |
| open-design\skills | skillz\open-design | 356 |
| skills\skills | skillz\skills-repo | 70 |
| taste-skill\skills | skillz\taste-skill | 15 |
| ponytail\skills | skillz\ponytail | 6 |
| gstack | skillz\gstack | 338 |
| ui-ux-pro-max-skill | skillz\ui-ux-pro-max-skill | 474 |
| ECC\agents | agentz\ECC | 67 |
| gstack\agents | agentz\gstack | 1 |
| claude-code-best-practice\agent-teams | agentz\claude-code-best-practice | 9 |
| ECC\commands | commandz\ECC | 94 |
| ponytail\commands | commandz\ponytail | 6 |
| ECC\hooks | hookz\ECC | 4 |
| ponytail\hooks | hookz\ponytail | 11 |
| claude-code\plugins | pluginz\claude-code | 149 |
| ECC\plugins | pluginz\ECC | 3 |
| Understand-Anything\understand-anything-plugin | pluginz\Understand-Anything | 348 |
| andrej-karpathy-skills\.claude-plugin | pluginz\andrej-karpathy-skills | 2 |
| ECC\rules | rulez\ECC | 122 |
| ECC\contexts | contextz\ECC | 3 |
| system-prompts-and-models-of-ai-tools | contextz\system-prompts-and-models | 107 |
| open-design\prompt-templates | templatez\open-design-prompt-templates | 107 |
| open-design\templates | templatez\open-design-templates | 10 |
| open-design\design-templates | templatez\open-design-design-templates | 747 |
| ECC\scaffolds | templatez\ECC-scaffolds | 3 |
| claude-cookbooks\patterns | resourcez\claude-cookbooks-patterns | 9 |
| ECC\schemas | resourcez\ECC-schemas | 10 |
| ECC\manifests | resourcez\ECC-manifests | 3 |
| open-design\design-systems | resourcez\open-design-design-systems | 4005 |
| ECC\integrations | adapterz\ECC-integrations | 7 |
| ECC\workflows | planz\ECC-workflows | 2 |
| ponytail\ponytail-mcp | mcpz\ponytail | 5 |
| ECC\mcp-configs | mcpz\ECC-mcp-configs | 1 |

**Refill total:** 8718 files. **UI/design cluster for hackathon:** skillz\ui-ux-pro-max-skill, skillz\taste-skill, skillz\open-design, skillz\gstack (design-review), templatez\open-design-*, resourcez\open-design-design-systems.

*Dave extracted `claude-code-best-practice` (13) and its `tips` (120) from `rulez` by hand: they are important enough to keep outside the arsenal. They now live at `M:\birds-of-odin\references\claude-code-best-practice`. Removed from the counts above so no future audit reports them missing.*

## Governance (pointer only, not law)
Law lives only at `C:\Program Files\ClaudeCode\NOMOS-LOGOS.md`.
The root files `CLAUDE.md`, `BOUNDARIES.md`, `GITHUB-GAURDRAILS.md` and
`REPO-POLICY.md` are retired stubs and archive residue. They are void as law
and are kept only as history. Note: legacy ARMORY-INDEX.md (old AI/Products/Projects layout) is superseded by this file; left in place pending owner OK to replace.
