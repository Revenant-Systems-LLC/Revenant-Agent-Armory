# AI-Armory Index

**Location:** B:\AI-Armory
**Generated:** 2026-08-24, after the full recategorization pass (approved by Dave, executed same session)
**Files:** 11,773 across 19 active categories (post junk-purge 2026-08-24)
**Supersedes:** ARMORY-INDEX-2026-07-12.md (kept at root as refill provenance) and the legacy ARMORY-INDEX.md (staged in `_junk-review\legacy-root`)

> **SOP (the Windsurf rule):** Read THIS index first. Pull ONLY what the task needs. NEVER absorb, walk, or bulk-load the whole Armory. Selective pull = scoped agency; token cost is the guardrail. (Nomos Logos, Immutables 5.)

## Categories

| Category | Dirs | Files | What it actually holds (verified against contents 2026-08-24) |
|---|---:|---:|---|
| .rev-agentz | 54 | 122 | Dave's agent-home snapshot (`.openclaw`: agents, workspaces, identity, reference library) |
| adapterz | 13 | 36 | Per-tool adapters + installer TS (claude-code, codex, cursor, gemini-cli, kiro, zed, ECC-integrations) |
| agentz | 10 | 149 | Agent/subagent definitions: 72 loose .md + claude-code-best-practice (9), ECC (67), gstack (1) |
| apiz | 19 | 21 | API catalogs by domain (one file each) + `settings\` (the Apify catalog generator) |
| cheatsheetz | 0 | 60 | Language/tool cheatsheets, multi-format (.docx/.js/.txt triplets + Python sheets) |
| codez | 18 | 778 | **Harvested source code (reference implementations).** See breakdown below |
| commandz | 2 | 182 | Slash commands: 82 loose + ECC (94), ponytail (6) |
| contextz | 44 | 113 | Captured system prompts (system-prompts-and-models, 107) + ECC contexts + dev/research/review.md |
| docz | 4 | 24 | Docs: ai-alignment reading (10), getting-started, dive-deep, troubleshooting, loose guides |
| hookz | 4 | 47 | Hooks: `claude-hook-router\` (30: routing/session/formatters .mjs system), ECC (4), ponytail (11), 2 loose examples |
| marketplacez | 319 | 544 | Marketplace bundles: claude-plugins-official (363), thedotmack (181) |
| mcpz | 3 | 6 | MCP servers/configs: ponytail (5), ECC-mcp-configs (1) |
| planz | 1 | 2 | ECC-workflows only (session transcripts staged out) |
| pluginz | 398 | 1098 | Plugins, one folder per plugin + README + marketplaces.zip (no extracted twin) |
| resourcez | 759 | 4027 | Reference data: open-design-design-systems (4005), claude-cookbooks-patterns (9), ECC schemas/manifests (13) |
| rulez | 27 | 147 | Coding/behavioral rules: ECC (122), common, golang, python, typescript + README |
| skill-pakz | 234 | 398 | **RS Skill Packs (product):** 10 pack dirs + sale zips + RS-PACK-MANIFEST.md |
| skillz | 1882 | 3148 | Skills, one folder per skill. Namespaces: awesome-claude-skills (1141), ui-ux-pro-max-skill (476), ECC (449), open-design (356), gstack (338), skills-repo (70) + ~130 individual skills |
| templatez | 211 | 868 | Templates/scaffolds: open-design design-templates (747, many in SKILL.md format by design), prompt-templates (107), templates (10), ECC-scaffolds (3) |

**Root files:** this index · ARMORY-INDEX-2026-07-12.md (refill provenance) · THE_RESOURCES_TABLE_NEW.csv (refill table)

## codez breakdown (new category, 2026-08-24)

Reassembled from 11 dissolved pseudo-categories (gatewayz, platformz, toolz, cliz, scriptz, testz, tickerz, maintainerz, dataz, assetz, formatterz) plus loose strays — each was an organ of one of two codebases:

- `codez\openclaw-hermes\` — Hermes/OpenClaw agent-framework source: `core` (51: adapters, credential pool, memory manager), `gateway` (211), `platforms` (41: discord/dingtalk/bluebubbles...), `tools` (70), `tests-cli` (155), `tests-agent` (74), `tests-skills` (7)
- `codez\awesome-repo-automation\` — awesome-claude-code/skills repo machinery: `scripts` (57), `tests` (5), `ticker` (4), `resource-pipeline` (7), `maintainer-docs` (22), `catalog-data` (62), `assets` (12)

## Junk purge record (2026-08-24, Dave-approved "delete all", executed same day)

`_junk-review\` (253 files) deleted in full after Dave rotated the exposed OpenAI key. Contents at deletion: secrets (3: assandtitties.txt key file, id_ed25519 + .pub), twin zips (24), pluginz cache/state/data (163), planz transcripts + dead Ossuary specs (20), git .sample hooks (14), retired law-stub copies (11), .vs Visual Studio cache (13), K-Lite installers (2), legacy ARMORY-INDEX.md (1), coding-teacher(backup) (1), empty dir shells (1 desktop.ini). No delete is silent: full manifest was shown and approved before execution; per-batch record in `M:\birds-of-odin\AGENT-LOG.md`.

## Moved OUT of the Armory (2026-08-24, approved)

- `.rev-agentz\.ollama` (51.9 GB Ollama model blobs, 64 files) → `B:\ollama-models\rev-agentz-ollama\`
- `OSSUARY_INDEX.md` (10 MB, maps the dead C:\The-Ossuary tree) → `B:\The-Ossuary\OSSUARY_INDEX.md`

## Open items for Dave

1. `codez\openclaw-hermes\tools\__pycache__` (3 files) is compiled residue — delete candidate, left in place.
2. `B:\ollama-models\rev-agentz-ollama\` (50.7 GB, 12 third-party models) — keep/delete pending Dave's call; diff vs live install done 2026-08-24 (4 of 12 duplicate the live C: store, all 12 re-pullable while published).

## Ledger (loss-proofing)

Baseline 2026-08-24 pre-reorg: 12,090 files. Post-reorg: 12,025 in Armory + 64 (ollama, moved out) + 1 (Ossuary index, moved out) = 12,090 — zero loss, all same-volume Move-Item renames, batch-verified. Post-purge: 11,773 in Armory (12,025 − 253 approved deletions + this index file).
