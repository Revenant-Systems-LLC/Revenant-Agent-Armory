# AI-Armory — Full Directory (CURRENT)

**Location:** `B:\AI-Armory`  ·  **Generated:** 2026-08-25  ·  **Files catalogued:** 12982 across 20 categories  ·  **Skills:** 1969

The complete directory of the Armory: **every top-level category**, its contents, and where each thing lives — so you can answer *"what's in here and where is it"* without walking the tree. Skill folders are expanded to per-skill detail (name / description / tags). File collections list every file. Large resource, code, and font trees are summarized by folder with file-type counts.

**Companion indexes (three distinct artifacts by design — do not merge):**
- `M:\ARMORY-DIRECTORY.md` — lightweight, token-safe **category-level** index. Read first (Arsenal SOP).
- `B:\AI-Armory\ARMORY-INDEX-2026-08-24.md` — canonical category-level record: ledger, provenance, junk-review, open items.
- **This file** — the **heavy full directory** (per-skill where skills exist, per-file elsewhere). Regenerated in place; name stays stable.

> **SOP unchanged (Nomos Logos, Immutables 5):** read an index, pull only what the task needs. This carries frontmatter + structure, never skill *bodies*.

**How this was generated (regenerable):** `M:\ARMORY-INDEX-GENERATOR.ps1` walks `B:\AI-Armory`, reads only each `SKILL.md`'s frontmatter, and summarizes every other folder by file counts and types. Re-run when the Armory changes: `pwsh -File M:\ARMORY-INDEX-GENERATOR.ps1 -OutFile B:\AI-Armory\ARMORY-INDEX-CURRENT.md`

---

## Contents

- [marketplacez](#marketplacez) — 544 files
- [pluginz](#pluginz) — 1098 files
- [skill-pakz](#skill-pakz) — 398 files
- [skillz](#skillz) — 3055 files
- [templatez](#templatez) — 868 files
- [.rev-agentz](#rev-agentz) — 122 files
- [adapterz](#adapterz) — 36 files
- [agentz](#agentz) — 149 files
- [apiz](#apiz) — 21 files
- [cheatsheetz](#cheatsheetz) — 60 files
- [codez](#codez) — 775 files
- [commandz](#commandz) — 182 files
- [contextz](#contextz) — 113 files
- [docz](#docz) — 24 files
- [fontz](#fontz) — 1308 files
- [hookz](#hookz) — 47 files
- [mcpz](#mcpz) — 6 files
- [planz](#planz) — 2 files
- [resourcez](#resourcez) — 4027 files
- [rulez](#rulez) — 147 files

---

## marketplacez

*Marketplace bundles (claude-plugins-official, thedotmack).*

**544 files** · **28 skills**  ·  204 .md · 172 (none) · 78 .json · 21 .py · 16 .sh · 14 .sample

<details><summary><b>claude-plugins-official</b> (28 skills)</summary>

- **access** — Manage Discord channel access — approve pairings, edit allowlists, set DM/group policy.
  `B:\AI-Armory\marketplacez\claude-plugins-official\external_plugins\discord\skills\access`
- **access** — Manage iMessage channel access — approve pairings, edit allowlists, set DM/group policy.
  `B:\AI-Armory\marketplacez\claude-plugins-official\external_plugins\imessage\skills\access`
- **access** — Manage Telegram channel access — approve pairings, edit allowlists, set DM/group policy.
  `B:\AI-Armory\marketplacez\claude-plugins-official\external_plugins\telegram\skills\access`
- **agent-development** — This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent frontmatter", "when to use description", "agent examples", "agent tools", "agent colors"...
  `B:\AI-Armory\marketplacez\claude-plugins-official\plugins\plugin-dev\skills\agent-development`
- **build-mcp-app** — This skill should be used when the user wants to build an "MCP app", add "interactive UI" or "widgets" to an MCP server, "render components in chat", build "MCP UI resources", make a tool that shows...
  `B:\AI-Armory\marketplacez\claude-plugins-official\plugins\mcp-server-dev\skills\build-mcp-app`
- **build-mcp-server** — This skill should be used when the user asks to "build an MCP server", "create an MCP", "make an MCP integration", "wrap an API for Claude", "expose tools to Claude", "make an MCP app", or discusses...
  `B:\AI-Armory\marketplacez\claude-plugins-official\plugins\mcp-server-dev\skills\build-mcp-server`
- **build-mcpb** — This skill should be used when the user wants to "package an MCP server", "bundle an MCP", "make an MCPB", "ship a local MCP server", "distribute a local MCP", discusses ".mcpb files", mentions...
  `B:\AI-Armory\marketplacez\claude-plugins-official\plugins\mcp-server-dev\skills\build-mcpb`
- **cardputer-buddy** — Iterate on the Cardputer-Adv MicroPython app bundle (Claude Buddy, Snake, Hello) after the device is already provisioned via m5-onboard.
  `B:\AI-Armory\marketplacez\claude-plugins-official\plugins\cwc-makers\skills\cardputer-buddy`
- **claude-automation-recommender** — Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers).
  `B:\AI-Armory\marketplacez\claude-plugins-official\plugins\claude-code-setup\skills\claude-automation-recommender`
- **claude-md-improver** — Audit and improve CLAUDE.md files in repositories.
  `B:\AI-Armory\marketplacez\claude-plugins-official\plugins\claude-md-management\skills\claude-md-improver`
- **command-development** — This skill should be used when the user asks to "create a slash command", "add a command", "write a custom command", "define command arguments", "use command frontmatter", "organize commands"...
  `B:\AI-Armory\marketplacez\claude-plugins-official\plugins\plugin-dev\skills\command-development`
- **configure** — Set up the Discord channel — save the bot token and review access policy.
  `B:\AI-Armory\marketplacez\claude-plugins-official\external_plugins\discord\skills\configure`
- **configure** — Check iMessage channel setup and review access policy.
  `B:\AI-Armory\marketplacez\claude-plugins-official\external_plugins\imessage\skills\configure`
- **configure** — Set up the Telegram channel — save the bot token and review access policy.
  `B:\AI-Armory\marketplacez\claude-plugins-official\external_plugins\telegram\skills\configure`
- **example-command** — An example user-invoked skill that demonstrates frontmatter options and the skills/<name>/SKILL.md layout
  `B:\AI-Armory\marketplacez\claude-plugins-official\plugins\example-plugin\skills\example-command`
- **example-skill** — This skill should be used when the user asks to "demonstrate skills", "show skill format", "create a skill template", or discusses skill development patterns.
  `B:\AI-Armory\marketplacez\claude-plugins-official\plugins\example-plugin\skills\example-skill`
- **frontend-design** — Create distinctive, production-grade frontend interfaces with high design quality.
  `B:\AI-Armory\marketplacez\claude-plugins-official\plugins\frontend-design\skills\frontend-design`
- **hook-development** — This skill should be used when the user asks to "create a hook", "add a PreToolUse/PostToolUse/Stop hook", "validate tool use", "implement prompt-based hooks", "use ${CLAUDE_PLUGIN_ROOT}", "set up...
  `B:\AI-Armory\marketplacez\claude-plugins-official\plugins\plugin-dev\skills\hook-development`
- **m5-onboard** — End-to-end onboarding for a freshly-plugged-in M5Stack ESP32 device (Cardputer, Cardputer-Adv, Core, CoreS3, Stick) — detect on USB, flash UIFlow 2.0 firmware, and install the Claude Buddy...
  `B:\AI-Armory\marketplacez\claude-plugins-official\plugins\cwc-makers\skills\m5-onboard`
- **math-olympiad** — "Solve competition math problems (IMO, Putnam, USAMO, AIME) with adversarial verification that catches the errors self-verification misses.
  `B:\AI-Armory\marketplacez\claude-plugins-official\plugins\math-olympiad\skills\math-olympiad`
- **mcp-integration** — This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", "use .mcp.json", "set up Model Context Protocol", "connect external service", mentions...
  `B:\AI-Armory\marketplacez\claude-plugins-official\plugins\plugin-dev\skills\mcp-integration`
- **playground** — Creates interactive HTML playgrounds — self-contained single-file explorers that let users configure something visually through controls, see a live preview, and copy out a prompt.
  `B:\AI-Armory\marketplacez\claude-plugins-official\plugins\playground\skills\playground`
- **plugin-settings** — This skill should be used when the user asks about "plugin settings", "store plugin configuration", "user-configurable plugin", ".local.md files", "plugin state files", "read YAML frontmatter"...
  `B:\AI-Armory\marketplacez\claude-plugins-official\plugins\plugin-dev\skills\plugin-settings`
- **plugin-structure** — This skill should be used when the user asks to "create a plugin", "scaffold a plugin", "understand plugin structure", "organize plugin components", "set up plugin.json", "use ${CLAUDE_PLUGIN_ROOT}"...
  `B:\AI-Armory\marketplacez\claude-plugins-official\plugins\plugin-dev\skills\plugin-structure`
- **session-report** — Generate an explorable HTML report of Claude Code session usage (tokens, cache, subagents, skills, expensive prompts) from ~/.claude/projects transcripts.
  `B:\AI-Armory\marketplacez\claude-plugins-official\plugins\session-report\skills\session-report`
- **skill-creator** — Create new skills, modify and improve existing skills, and measure skill performance.
  `B:\AI-Armory\marketplacez\claude-plugins-official\plugins\skill-creator\skills\skill-creator`
- **skill-development** — This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill", "improve skill description", "organize skill content", or needs guidance on skill...
  `B:\AI-Armory\marketplacez\claude-plugins-official\plugins\plugin-dev\skills\skill-development`
- **writing-hookify-rules** — This skill should be used when the user asks to "create a hookify rule", "write a hook rule", "configure hookify", "add a hookify rule", or needs guidance on hookify rule syntax and patterns.
  `B:\AI-Armory\marketplacez\claude-plugins-official\plugins\hookify\skills\writing-rules`

</details>

<details><summary><b>(non-skill folders in this category)</b></summary>

- **thedotmack\** (181 files) — 132 (none) · 14 .sample · 10 .json · 9 .md · 2 .idx · 2 .pack
  `B:\AI-Armory\marketplacez\thedotmack`

</details>

---

## pluginz

*Plugins, one folder per plugin.*

**1098 files** · **131 skills**  ·  518 .md · 206 .ts · 79 .py · 74 .json · 54 .ttf · 36 .tsx

<details><summary><b>antigravity-awesome-skills</b> (83 skills)</summary>

- **00-andruia-consultant** — Arquitecto de Soluciones Principal y Consultor Tecnológico de Andru.ia.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\00-andruia-consultant`  ·  _tags:_ andruia
- **007** — Security audit, hardening, threat modeling (STRIDE/PASTA), Red/Blue Team, OWASP checks, code review, incident response, and infrastructure security for any project.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\007`
- **10-andruia-skill-smith** — Ingeniero de Sistemas de Andru.ia.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\10-andruia-skill-smith`  ·  _tags:_ andruia
- **20-andruia-niche-intelligence** — Estratega de Inteligencia de Dominio de Andru.ia.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\20-andruia-niche-intelligence`  ·  _tags:_ andruia
- **3d-web-experience** — Expert in building 3D experiences for the web - Three.js, React
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\3d-web-experience`
- **ab-test-setup** — Structured guide for setting up A/B tests with mandatory gates for hypothesis, metrics, and execution readiness.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\ab-test-setup`
- **acceptance-orchestrator** — Use when a coding task should be driven end-to-end from issue intake through implementation, review, deployment, and acceptance verification with minimal human re-intervention.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\acceptance-orchestrator`
- **accessibility-compliance-accessibility-audit** — You are an accessibility expert specializing in WCAG compliance, inclusive design, and assistive technology compatibility.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\accessibility-compliance-accessibility-audit`
- **active-directory-attacks** — Provide comprehensive techniques for attacking Microsoft Active Directory environments.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\active-directory-attacks`
- **activecampaign-automation** — Automate ActiveCampaign tasks via Rube MCP (Composio): manage contacts, tags, list subscriptions, automation enrollment, and tasks.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\activecampaign-automation`
- **ad-creative** — Create, iterate, and scale paid ad creative for Google Ads, Meta, LinkedIn, TikTok, and similar platforms.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\ad-creative`
- **address-github-comments** — Use when you need to address review or issue comments on an open GitHub Pull Request using the gh CLI.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\address-github-comments`
- **advanced-evaluation** — This skill should be used when the user asks to "implement LLM-as-judge", "compare model outputs", "create evaluation rubrics", "mitigate evaluation bias", or mentions direct scoring, pairwise...
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\advanced-evaluation`
- **advogado-criminal** — Advogado criminalista especializado em Maria da Penha, violencia domestica, feminicidio, direito penal brasileiro, medidas protetivas, inquerito policial e acao penal.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\advogado-criminal`
- **advogado-especialista** — Advogado especialista em todas as areas do Direito brasileiro: familia, criminal, trabalhista, tributario, consumidor, imobiliario, empresarial, civil e constitucional.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\advogado-especialista`
- **aegisops-ai** — Autonomous DevSecOps & FinOps Guardrails.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\aegisops-ai`
- **agent-evaluation** — Testing and benchmarking LLM agents including behavioral testing,
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\agent-evaluation`
- **agent-framework-azure-ai-py** — Build persistent agents on Azure AI Foundry using the Microsoft Agent Framework Python SDK.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\agent-framework-azure-ai-py`
- **agent-manager-skill** — Manage multiple local CLI agents via tmux sessions (start/stop/monitor/assign) with cron-friendly scheduling.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\agent-manager-skill`
- **agent-memory-mcp** — A hybrid memory system that provides persistent, searchable knowledge management for AI agents (Architecture, Patterns, Decisions).
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\agent-memory-mcp`
- **agent-memory-systems** — Memory is the cornerstone of intelligent agents.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\agent-memory-systems`
- **agent-orchestration-improve-agent** — Systematic improvement of existing agents through performance analysis, prompt engineering, and continuous iteration.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\agent-orchestration-improve-agent`
- **agent-orchestration-multi-agent-optimize** — Optimize multi-agent systems with coordinated profiling, workload distribution, and cost-aware orchestration.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\agent-orchestration-multi-agent-optimize`
- **agent-orchestrator** — Meta-skill que orquestra todos os agentes do ecossistema.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\agent-orchestrator`
- **agent-tool-builder** — Tools are how AI agents interact with the world.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\agent-tool-builder`
- **agentfolio** — Skill for discovering and researching autonomous AI agents, tools, and ecosystems using the AgentFolio directory.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\agentfolio`
- **agentic-actions-auditor** — Audits GitHub Actions workflows for security vulnerabilities in AI agent integrations including Claude Code Action, Gemini CLI, OpenAI Codex, and GitHub AI Inference.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\agentic-actions-auditor`
- **agentmail** — Email infrastructure for AI agents.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\agentmail`
- **agentphone** — Build AI phone agents with AgentPhone API.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\agentphone`
- **agents-md** — This skill should be used when the user asks to "create AGENTS.md", "update AGENTS.md", "maintain agent docs", "set up CLAUDE.md", or needs to keep agent instructions concise.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\agents-md`
- **agents-v2-py** — Build container-based Foundry Agents with Azure AI Projects SDK (ImageBasedHostedAgentDefinition).
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\agents-v2-py`
- **ai-agent-development** — AI agent development workflow for building autonomous agents, multi-agent systems, and agent orchestration with CrewAI, LangGraph, and custom agents.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\ai-agent-development`  ·  _tags:_ granular-workflow-bundle
- **ai-agents-architect** — Expert in designing and building autonomous AI agents.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\ai-agents-architect`
- **ai-analyzer** — AI驱动的综合健康分析系统，整合多维度健康数据、识别异常模式、预测健康风险、提供个性化建议。支持智能问答和AI健康报告生成。
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\ai-analyzer`
- **ai-dev-jobs-mcp** — Search 8,400+ AI and ML jobs across 489 companies, inspect listings and employers, match roles, and view salary and market stats via AI Dev Jobs MCP
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\ai-dev-jobs-mcp`  ·  _tags:_ mcp, jobs, ai-jobs, ml-jobs, recruiting, job-search, career
- **ai-engineer** — Build production-ready LLM applications, advanced RAG systems, and intelligent agents.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\ai-engineer`
- **ai-ml** — AI and machine learning workflow covering LLM application development, RAG implementation, agent architecture, ML pipelines, and AI-powered features.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\ai-ml`  ·  _tags:_ workflow-bundle
- **ai-native-cli** — Design spec with 98 rules for building CLI tools that AI agents can safely use.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\ai-native-cli`
- **ai-product** — Every product will be AI-powered.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\ai-product`
- **ai-seo** — Optimize content for AI search and LLM citations across AI Overviews, ChatGPT, Perplexity, Claude, Gemini, and similar systems.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\ai-seo`
- **ai-studio-image** — Geracao de imagens humanizadas via Google AI Studio (Gemini).
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\ai-studio-image`
- **ai-wrapper-product** — Expert in building products that wrap AI APIs (OpenAI, Anthropic,
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\ai-wrapper-product`
- **airflow-dag-patterns** — Build production Apache Airflow DAGs with best practices for operators, sensors, testing, and deployment.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\airflow-dag-patterns`
- **airtable-automation** — Automate Airtable tasks via Rube MCP (Composio): records, bases, tables, fields, views.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\airtable-automation`
- **akf-trust-metadata** — The AI native file format.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\akf-trust-metadata`
- **algolia-search** — Expert patterns for Algolia search implementation, indexing
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\algolia-search`
- **algorithmic-art** — Algorithmic philosophies are computational aesthetic movements that are then expressed through code.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\algorithmic-art`
- **alpha-vantage** — Access 20+ years of global financial data: equities, options, forex, crypto, commodities, economic indicators, and 50+ technical indicators.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\alpha-vantage`
- **amazon-alexa** — Integracao completa com Amazon Alexa para criar skills de voz inteligentes, transformar Alexa em assistente com Claude como cerebro (projeto Auri) e integrar com AWS ecosystem (Lambda, DynamoDB...
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\amazon-alexa`
- **amplitude-automation** — Automate Amplitude tasks via Rube MCP (Composio): events, user activity, cohorts, user identification.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\amplitude-automation`
- **analytics-product** — Analytics de produto — PostHog, Mixpanel, eventos, funnels, cohorts, retencao, north star metric, OKRs e dashboards de produto.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\analytics-product`
- **analytics-tracking** — Design, audit, and improve analytics tracking systems that produce reliable, decision-ready data.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\analytics-tracking`
- **andrej-karpathy** — Agente que simula Andrej Karpathy — ex-Director of AI da Tesla, co-fundador da OpenAI, fundador da Eureka Labs, e o maior educador de deep learning do mundo.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\andrej-karpathy`
- **android_ui_verification** — Automated end-to-end UI testing and verification on an Android Emulator using ADB.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\android_ui_verification`
- **android-jetpack-compose-expert** — Expert guidance for building modern Android UIs with Jetpack Compose, covering state management, navigation, performance, and Material Design 3.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\android-jetpack-compose-expert`
- **angular** — Modern Angular (v20+) expert with deep knowledge of Signals, Standalone Components, Zoneless applications, SSR/Hydration, and reactive patterns.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\angular`
- **angular-best-practices** — Angular performance optimization and best practices guide.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\angular-best-practices`
- **angular-migration** — Master AngularJS to Angular migration, including hybrid apps, component conversion, dependency injection changes, and routing migration.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\angular-migration`
- **angular-state-management** — Master modern Angular state management with Signals, NgRx, and RxJS.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\angular-state-management`
- **angular-ui-patterns** — Modern Angular UI patterns for loading states, error handling, and data display.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\angular-ui-patterns`
- **animejs-animation** — Advanced JavaScript animation library skill for creating complex, high-performance web animations.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\animejs-animation`
- **anti-reversing-techniques** — AUTHORIZED USE ONLY: This skill contains dual-use security techniques.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\anti-reversing-techniques`
- **antigravity-design-expert** — Core UI/UX engineering skill for building highly interactive, spatial, weightless, and glassmorphism-based web interfaces using GSAP and 3D CSS.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\antigravity-design-expert`
- **antigravity-skill-orchestrator** — A meta-skill that understands task requirements, dynamically selects appropriate skills, tracks successful skill combinations using agent-memory-mcp, and prevents skill overuse for simple tasks.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\antigravity-skill-orchestrator`  ·  _tags:_ [orchestration, meta-skill, agent-memory, task-evaluation]
- **antigravity-workflows** — Orchestrate multiple Antigravity skills through guided workflows for SaaS MVP delivery, security audits, AI agent builds, and browser QA.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\antigravity-workflows`
- **api-design-principles** — Master REST and GraphQL API design principles to build intuitive, scalable, and maintainable APIs that delight developers and stand the test of time.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\api-design-principles`
- **api-documentation** — API documentation workflow for generating OpenAPI specs, creating developer guides, and maintaining comprehensive API documentation.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\api-documentation`  ·  _tags:_ granular-workflow-bundle
- **api-documentation-generator** — Generate comprehensive, developer-friendly API documentation from code, including endpoints, parameters, examples, and best practices
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\api-documentation-generator`
- **api-documenter** — Master API documentation with OpenAPI 3.1, AI-powered tools, and modern developer experience practices.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\api-documenter`
- **api-endpoint-builder** — Builds production-ready REST API endpoints with validation, error handling, authentication, and documentation.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\api-endpoint-builder`  ·  _tags:_ development
- **api-fuzzing-bug-bounty** — Provide comprehensive techniques for testing REST, SOAP, and GraphQL APIs during bug bounty hunting and penetration testing engagements.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\api-fuzzing-bug-bounty`
- **api-patterns** — API design principles and decision-making.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\api-patterns`
- **api-security-best-practices** — Implement secure API design patterns including authentication, authorization, input validation, rate limiting, and protection against common API vulnerabilities
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\api-security-best-practices`
- **api-security-testing** — API security testing workflow for REST and GraphQL APIs covering authentication, authorization, rate limiting, input validation, and security best practices.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\api-security-testing`  ·  _tags:_ granular-workflow-bundle
- **api-testing-observability-api-mock** — You are an API mocking expert specializing in realistic mock services for development, testing, and demos.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\api-testing-observability-api-mock`
- **apify-actor-development** — Important: Before you begin, fill in the generatedBy property in the meta section of .actor/actor.json.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\apify-actor-development`
- **apify-actorization** — Actorization converts existing software into reusable serverless applications compatible with the Apify platform.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\apify-actorization`
- **apify-audience-analysis** — Understand audience demographics, preferences, behavior patterns, and engagement quality across Facebook, Instagram, YouTube, and TikTok.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\apify-audience-analysis`
- **apify-brand-reputation-monitoring** — Scrape reviews, ratings, and brand mentions from multiple platforms using Apify Actors.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\apify-brand-reputation-monitoring`
- **apify-competitor-intelligence** — Analyze competitor strategies, content, pricing, ads, and market positioning across Google Maps, Booking.com, Facebook, Instagram, YouTube, and TikTok.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\apify-competitor-intelligence`
- **apify-content-analytics** — Track engagement metrics, measure campaign ROI, and analyze content performance across Instagram, Facebook, YouTube, and TikTok.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\apify-content-analytics`
- **apify-influencer-discovery** — Find and evaluate influencers for brand partnerships, verify authenticity, and track collaboration performance across Instagram, Facebook, YouTube, and TikTok.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\apify-influencer-discovery`
- **apify-lead-generation** — Scrape leads from multiple platforms using Apify Actors.
  `B:\AI-Armory\pluginz\antigravity-awesome-skills\skills\apify-lead-generation`

</details>

<details><summary><b>claude-code</b> (10 skills)</summary>

- **Agent Development** — This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent frontmatter", "when to use description", "agent examples", "agent tools", "agent colors"...
  `B:\AI-Armory\pluginz\claude-code\plugin-dev\skills\agent-development`
- **claude-opus-4-5-migration** — Migrate prompts and code from Claude Sonnet 4.0, Sonnet 4.5, or Opus 4.1 to Opus 4.5.
  `B:\AI-Armory\pluginz\claude-code\claude-opus-4-5-migration\skills\claude-opus-4-5-migration`
- **Command Development** — This skill should be used when the user asks to "create a slash command", "add a command", "write a custom command", "define command arguments", "use command frontmatter", "organize commands"...
  `B:\AI-Armory\pluginz\claude-code\plugin-dev\skills\command-development`
- **frontend-design** — Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one.
  `B:\AI-Armory\pluginz\claude-code\frontend-design\skills\frontend-design`
- **Hook Development** — This skill should be used when the user asks to "create a hook", "add a PreToolUse/PostToolUse/Stop hook", "validate tool use", "implement prompt-based hooks", "use ${CLAUDE_PLUGIN_ROOT}", "set up...
  `B:\AI-Armory\pluginz\claude-code\plugin-dev\skills\hook-development`
- **MCP Integration** — This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", "use .mcp.json", "set up Model Context Protocol", "connect external service", mentions...
  `B:\AI-Armory\pluginz\claude-code\plugin-dev\skills\mcp-integration`
- **Plugin Settings** — This skill should be used when the user asks about "plugin settings", "store plugin configuration", "user-configurable plugin", ".local.md files", "plugin state files", "read YAML frontmatter"...
  `B:\AI-Armory\pluginz\claude-code\plugin-dev\skills\plugin-settings`
- **Plugin Structure** — This skill should be used when the user asks to "create a plugin", "scaffold a plugin", "understand plugin structure", "organize plugin components", "set up plugin.json", "use ${CLAUDE_PLUGIN_ROOT}"...
  `B:\AI-Armory\pluginz\claude-code\plugin-dev\skills\plugin-structure`
- **Skill Development** — This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill", "improve skill description", "organize skill content", or needs guidance on skill...
  `B:\AI-Armory\pluginz\claude-code\plugin-dev\skills\skill-development`
- **Writing Hookify Rules** — This skill should be used when the user asks to "create a hookify rule", "write a hook rule", "configure hookify", "add a hookify rule", or needs guidance on hookify rule syntax and patterns.
  `B:\AI-Armory\pluginz\claude-code\hookify\skills\writing-rules`

</details>

<details><summary><b>Understand-Anything</b> (9 skills)</summary>

- **understand** — Analyze a codebase to produce an interactive knowledge graph for understanding architecture, components, and relationships
  `B:\AI-Armory\pluginz\Understand-Anything\skills\understand`
- **understand-chat** — Use when you need to ask questions about a codebase or understand code using a knowledge graph
  `B:\AI-Armory\pluginz\Understand-Anything\skills\understand-chat`
- **understand-dashboard** — Launch the interactive web dashboard to visualize a codebase's knowledge graph
  `B:\AI-Armory\pluginz\Understand-Anything\skills\understand-dashboard`
- **understand-diff** — Use when you need to analyze git diffs or pull requests to understand what changed, affected components, and risks
  `B:\AI-Armory\pluginz\Understand-Anything\skills\understand-diff`
- **understand-domain** — Extract business domain knowledge from a codebase and generate an interactive domain flow graph.
  `B:\AI-Armory\pluginz\Understand-Anything\skills\understand-domain`
- **understand-explain** — Use when you need a deep-dive explanation of a specific file, function, or module in the codebase
  `B:\AI-Armory\pluginz\Understand-Anything\skills\understand-explain`
- **understand-figma** — Analyze a Figma file via the Figma REST API and generate an interactive design knowledge graph (pages, screens, components, component sets, instances, design tokens) with a kind:"design" dashboard.
  `B:\AI-Armory\pluginz\Understand-Anything\skills\understand-figma`
- **understand-knowledge** — Analyze a Karpathy-pattern LLM wiki knowledge base and generate an interactive knowledge graph with entity extraction, implicit relationships, and topic clustering.
  `B:\AI-Armory\pluginz\Understand-Anything\skills\understand-knowledge`
- **understand-onboard** — Use when you need to generate an onboarding guide for new team members joining a project
  `B:\AI-Armory\pluginz\Understand-Anything\skills\understand-onboard`

</details>

<details><summary><b>antigravity-bundle-web-wizard</b> (7 skills)</summary>

- **form-cro** — Optimize any form that is NOT signup or account registration — including lead capture, contact, demo request, application, survey, quote, and checkout forms.
  `B:\AI-Armory\pluginz\antigravity-bundle-web-wizard\skills\form-cro`
- **frontend-design** — You are a frontend designer-engineer, not a layout generator.
  `B:\AI-Armory\pluginz\antigravity-bundle-web-wizard\skills\frontend-design`
- **nextjs-best-practices** — Next.js App Router principles.
  `B:\AI-Armory\pluginz\antigravity-bundle-web-wizard\skills\nextjs-best-practices`
- **react-best-practices** — Comprehensive performance optimization guide for React and Next.js applications, maintained by Vercel.
  `B:\AI-Armory\pluginz\antigravity-bundle-web-wizard\skills\react-best-practices`
- **react-patterns** — Modern React patterns and principles.
  `B:\AI-Armory\pluginz\antigravity-bundle-web-wizard\skills\react-patterns`
- **seo-audit** — Diagnose and audit SEO issues affecting crawlability, indexation, rankings, and organic performance.
  `B:\AI-Armory\pluginz\antigravity-bundle-web-wizard\skills\seo-audit`
- **tailwind-patterns** — Tailwind CSS v4 principles.
  `B:\AI-Armory\pluginz\antigravity-bundle-web-wizard\skills\tailwind-patterns`

</details>

<details><summary><b>plugin-dev</b> (7 skills)</summary>

- **Agent Development** — This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent frontmatter", "when to use description", "agent examples", "agent tools", "agent colors"...
  `B:\AI-Armory\pluginz\plugin-dev\skills\agent-development`
- **Command Development** — This skill should be used when the user asks to "create a slash command", "add a command", "write a custom command", "define command arguments", "use command frontmatter", "organize commands"...
  `B:\AI-Armory\pluginz\plugin-dev\skills\command-development`
- **Hook Development** — This skill should be used when the user asks to "create a hook", "add a PreToolUse/PostToolUse/Stop hook", "validate tool use", "implement prompt-based hooks", "use ${CLAUDE_PLUGIN_ROOT}", "set up...
  `B:\AI-Armory\pluginz\plugin-dev\skills\hook-development`
- **MCP Integration** — This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", "use .mcp.json", "set up Model Context Protocol", "connect external service", mentions...
  `B:\AI-Armory\pluginz\plugin-dev\skills\mcp-integration`
- **Plugin Settings** — This skill should be used when the user asks about "plugin settings", "store plugin configuration", "user-configurable plugin", ".local.md files", "plugin state files", "read YAML frontmatter"...
  `B:\AI-Armory\pluginz\plugin-dev\skills\plugin-settings`
- **Plugin Structure** — This skill should be used when the user asks to "create a plugin", "scaffold a plugin", "understand plugin structure", "organize plugin components", "set up plugin.json", "use ${CLAUDE_PLUGIN_ROOT}"...
  `B:\AI-Armory\pluginz\plugin-dev\skills\plugin-structure`
- **Skill Development** — This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill", "improve skill description", "organize skill content", or needs guidance on skill...
  `B:\AI-Armory\pluginz\plugin-dev\skills\skill-development`

</details>

<details><summary><b>antigravity-bundle-web-designer</b> (6 skills)</summary>

- **3d-web-experience** — Expert in building 3D experiences for the web - Three.js, React
  `B:\AI-Armory\pluginz\antigravity-bundle-web-designer\skills\3d-web-experience`
- **canvas-design** — These are instructions for creating design philosophies - aesthetic movements that are then EXPRESSED VISUALLY.
  `B:\AI-Armory\pluginz\antigravity-bundle-web-designer\skills\canvas-design`
- **frontend-design** — You are a frontend designer-engineer, not a layout generator.
  `B:\AI-Armory\pluginz\antigravity-bundle-web-designer\skills\frontend-design`
- **mobile-design** — (Mobile-First · Touch-First · Platform-Respectful)
  `B:\AI-Armory\pluginz\antigravity-bundle-web-designer\skills\mobile-design`
- **scroll-experience** — Expert in building immersive scroll-driven experiences - parallax
  `B:\AI-Armory\pluginz\antigravity-bundle-web-designer\skills\scroll-experience`
- **ui-ux-pro-max** — Comprehensive design guide for web and mobile applications.
  `B:\AI-Armory\pluginz\antigravity-bundle-web-designer\skills\ui-ux-pro-max`

</details>

<details><summary><b>antigravity-bundle-typescript-javascript</b> (5 skills)</summary>

- **javascript-pro** — Master modern JavaScript with ES6+, async patterns, and Node.js APIs.
  `B:\AI-Armory\pluginz\antigravity-bundle-typescript-javascript\skills\javascript-pro`
- **nextjs-app-router-patterns** — Comprehensive patterns for Next.js 14+ App Router architecture, Server Components, and modern full-stack React development.
  `B:\AI-Armory\pluginz\antigravity-bundle-typescript-javascript\skills\nextjs-app-router-patterns`
- **nodejs-best-practices** — Node.js development principles and decision-making.
  `B:\AI-Armory\pluginz\antigravity-bundle-typescript-javascript\skills\nodejs-best-practices`
- **react-best-practices** — Comprehensive performance optimization guide for React and Next.js applications, maintained by Vercel.
  `B:\AI-Armory\pluginz\antigravity-bundle-typescript-javascript\skills\react-best-practices`
- **typescript-expert** — TypeScript and JavaScript expert with deep knowledge of type-level programming, performance optimization, monorepo management, migration strategies, and modern tooling.
  `B:\AI-Armory\pluginz\antigravity-bundle-typescript-javascript\skills\typescript-expert`  ·  _tags:_ framework

</details>

<details><summary><b>(singles)</b> (4 skills)</summary>

- **claude-opus-4-5-migration** — Migrate prompts and code from Claude Sonnet 4.0, Sonnet 4.5, or Opus 4.1 to Opus 4.5.
  `B:\AI-Armory\pluginz\claude-opus-4-5-migration\skills\claude-opus-4-5-migration`
- **frontend-design** — Create distinctive, production-grade frontend interfaces with high design quality.
  `B:\AI-Armory\pluginz\frontend-design\skills\frontend-design`
- **google_meet** — Join a Google Meet call, transcribe live captions, optionally speak in realtime, and do the followup work afterwards.
  `B:\AI-Armory\pluginz\google_meet`
- **Writing Hookify Rules** — This skill should be used when the user asks to "create a hookify rule", "write a hook rule", "configure hookify", "add a hookify rule", or needs guidance on hookify rule syntax and patterns.
  `B:\AI-Armory\pluginz\hookify\skills\writing-rules`

</details>

<details><summary><b>(non-skill folders in this category)</b></summary>

- **agent-sdk-dev\** (5 files) — 4 .md · 1 .json
  `B:\AI-Armory\pluginz\agent-sdk-dev`
- **andrej-karpathy-skills\** (2 files) — 2 .json
  `B:\AI-Armory\pluginz\andrej-karpathy-skills`
- **code-review\** (3 files) — 2 .md · 1 .json
  `B:\AI-Armory\pluginz\code-review`
- **commit-commands\** (5 files) — 4 .md · 1 .json
  `B:\AI-Armory\pluginz\commit-commands`
- **context_engine\** (1 files) — 1 .py
  `B:\AI-Armory\pluginz\context_engine`
- **disk-cleanup\** (4 files) — 2 .py · 1 .md · 1 .yaml
  `B:\AI-Armory\pluginz\disk-cleanup`
- **ECC\** (3 files) — 2 .md · 1 .json
  `B:\AI-Armory\pluginz\ECC`
- **example-dashboard\** (3 files) — 1 .js · 1 .json · 1 .py
  `B:\AI-Armory\pluginz\example-dashboard`
- **explanatory-output-style\** (4 files) — 2 .json · 1 .md · 1 .sh
  `B:\AI-Armory\pluginz\explanatory-output-style`
- **feature-dev\** (6 files) — 5 .md · 1 .json
  `B:\AI-Armory\pluginz\feature-dev`
- **image_gen\** (6 files) — 3 .py · 3 .yaml
  `B:\AI-Armory\pluginz\image_gen`
- **learning-output-style\** (4 files) — 2 .json · 1 .md · 1 .sh
  `B:\AI-Armory\pluginz\learning-output-style`
- **pr-review-toolkit\** (9 files) — 8 .md · 1 .json
  `B:\AI-Armory\pluginz\pr-review-toolkit`
- **ralph-wiggum\** (8 files) — 4 .md · 2 .json · 2 .sh
  `B:\AI-Armory\pluginz\ralph-wiggum`
- **security-guidance\** (3 files) — 2 .json · 1 .py
  `B:\AI-Armory\pluginz\security-guidance`
- **strike-freedom-cockpit\** (4 files) — 1 .js · 1 .json · 1 .md · 1 .yaml
  `B:\AI-Armory\pluginz\strike-freedom-cockpit`

</details>

---

## skill-pakz

*RS Skill Packs (product): 10 packs + zips + manifest.*

**398 files** · **135 skills**  ·  240 .md · 54 .ttf · 34 .json · 32 .txt · 20 .py · 11 .zip

<details><summary><b>rs-growth-cro</b> (15 skills)</summary>

- **ab-test-setup** — When the user wants to plan, design, or implement an A/B test or experiment, or build a growth experimentation program.
  `B:\AI-Armory\skill-pakz\rs-growth-cro\ab-test-setup`
- **ad-creative** — When the user wants to generate, iterate, or scale ad creative — headlines, descriptions, primary text, or full ad variations — for any paid advertising platform.
  `B:\AI-Armory\skill-pakz\rs-growth-cro\ad-creative`
- **churn-prevention** — When the user wants to reduce churn, build cancellation flows, set up save offers, recover failed payments, or implement retention strategies.
  `B:\AI-Armory\skill-pakz\rs-growth-cro\churn-prevention`
- **form-cro** — When the user wants to optimize any form that is NOT signup/registration — including lead capture forms, contact forms, demo request forms, application forms, survey forms, or checkout forms.
  `B:\AI-Armory\skill-pakz\rs-growth-cro\form-cro`
- **free-tool-strategy** — When the user wants to plan, evaluate, or build a free tool for marketing purposes — lead generation, SEO value, or brand awareness.
  `B:\AI-Armory\skill-pakz\rs-growth-cro\free-tool-strategy`
- **launch-strategy** — When the user wants to plan a product launch, feature announcement, or release strategy.
  `B:\AI-Armory\skill-pakz\rs-growth-cro\launch-strategy`
- **marketing-psychology** — When the user wants to apply psychological principles, mental models, or behavioral science to marketing.
  `B:\AI-Armory\skill-pakz\rs-growth-cro\marketing-psychology`
- **onboarding-cro** — When the user wants to optimize post-signup onboarding, user activation, first-run experience, or time-to-value.
  `B:\AI-Armory\skill-pakz\rs-growth-cro\onboarding-cro`
- **page-cro** — When the user wants to optimize, improve, or increase conversions on any marketing page — including homepage, landing pages, pricing pages, feature pages, or blog posts.
  `B:\AI-Armory\skill-pakz\rs-growth-cro\page-cro`
- **paid-ads** — When the user wants help with paid advertising campaigns on Google Ads, Meta (Facebook/Instagram), LinkedIn, Twitter/X, or other ad platforms.
  `B:\AI-Armory\skill-pakz\rs-growth-cro\paid-ads`
- **paywall-upgrade-cro** — When the user wants to create or optimize in-app paywalls, upgrade screens, upsell modals, or feature gates.
  `B:\AI-Armory\skill-pakz\rs-growth-cro\paywall-upgrade-cro`
- **popup-cro** — When the user wants to create or optimize popups, modals, overlays, slide-ins, or banners for conversion purposes.
  `B:\AI-Armory\skill-pakz\rs-growth-cro\popup-cro`
- **pricing-strategy** — When the user wants help with pricing decisions, packaging, or monetization strategy.
  `B:\AI-Armory\skill-pakz\rs-growth-cro\pricing-strategy`
- **referral-program** — When the user wants to create, optimize, or analyze a referral program, affiliate program, or word-of-mouth strategy.
  `B:\AI-Armory\skill-pakz\rs-growth-cro\referral-program`
- **signup-flow-cro** — When the user wants to optimize signup, registration, account creation, or trial activation flows.
  `B:\AI-Armory\skill-pakz\rs-growth-cro\signup-flow-cro`

</details>

<details><summary><b>rs-seo-content-warfare</b> (15 skills)</summary>

- **ai-seo** — When the user wants to optimize content for AI search engines, get cited by LLMs, or appear in AI-generated answers.
  `B:\AI-Armory\skill-pakz\rs-seo-content-warfare\ai-seo`
- **article-writing** — Write articles, guides, blog posts, tutorials, newsletter issues, and other long-form content in a distinctive voice derived from supplied examples or brand guidance.
  `B:\AI-Armory\skill-pakz\rs-seo-content-warfare\article-writing`
- **blog-writing-guide** — This skill enforces Sentry's blog writing standards across every post — whether you're helping an engineer write their first blog post or a marketer draft a product announcement.
  `B:\AI-Armory\skill-pakz\rs-seo-content-warfare\blog-writing-guide`
- **content-creator** — Professional-grade brand voice analysis, SEO optimization, and platform-specific content frameworks.
  `B:\AI-Armory\skill-pakz\rs-seo-content-warfare\content-creator`  ·  _tags:_ marketing
- **content-engine** — Create platform-native content systems for X, LinkedIn, TikTok, YouTube, newsletters, and repurposed multi-platform campaigns.
  `B:\AI-Armory\skill-pakz\rs-seo-content-warfare\content-engine`
- **content-research-writer** — Assists in writing high-quality content by conducting research, adding citations, improving hooks, iterating on outlines, and providing real-time feedback on each section.
  `B:\AI-Armory\skill-pakz\rs-seo-content-warfare\content-research-writer`
- **content-strategy** — When the user wants to plan a content strategy, decide what content to create, or figure out what topics to cover.
  `B:\AI-Armory\skill-pakz\rs-seo-content-warfare\content-strategy`
- **copy-editing** — When the user wants to edit, review, or improve existing marketing copy, or refresh outdated content.
  `B:\AI-Armory\skill-pakz\rs-seo-content-warfare\copy-editing`
- **copywriting** — When the user wants to write, rewrite, or improve marketing copy for any page — including homepage, landing pages, pricing pages, feature pages, about pages, or product pages.
  `B:\AI-Armory\skill-pakz\rs-seo-content-warfare\copywriting`
- **programmatic-seo** — When the user wants to create SEO-driven pages at scale using templates and data.
  `B:\AI-Armory\skill-pakz\rs-seo-content-warfare\programmatic-seo`
- **schema-markup** — When the user wants to add, fix, or optimize schema markup and structured data on their site.
  `B:\AI-Armory\skill-pakz\rs-seo-content-warfare\schema-markup`
- **seo** — Audit, plan, and implement SEO improvements across technical SEO, on-page optimization, structured data, Core Web Vitals, and content strategy.
  `B:\AI-Armory\skill-pakz\rs-seo-content-warfare\seo`
- **seo-audit** — When the user wants to audit, review, or diagnose SEO issues on their site.
  `B:\AI-Armory\skill-pakz\rs-seo-content-warfare\seo-audit`
- **site-architecture** — When the user wants to plan, map, or restructure their website's page hierarchy, navigation, URL structure, or internal linking.
  `B:\AI-Armory\skill-pakz\rs-seo-content-warfare\site-architecture`
- **social-content** — When the user wants help creating, scheduling, or optimizing social media content for LinkedIn, Twitter/X, Instagram, TikTok, Facebook, or other platforms.
  `B:\AI-Armory\skill-pakz\rs-seo-content-warfare\social-content`

</details>

<details><summary><b>rs-business-automation</b> (14 skills)</summary>

- **airtable-automation** — Automate Airtable tasks via Rube MCP (Composio): records, bases, tables, fields, views.
  `B:\AI-Armory\skill-pakz\rs-business-automation\airtable-automation`
- **asana-automation** — Automate Asana tasks via Rube MCP (Composio): tasks, projects, sections, teams, workspaces.
  `B:\AI-Armory\skill-pakz\rs-business-automation\asana-automation`
- **clickup-automation** — Automate ClickUp project management including tasks, spaces, folders, lists, comments, and team operations via Rube MCP (Composio).
  `B:\AI-Armory\skill-pakz\rs-business-automation\clickup-automation`
- **confluence-automation** — Automate Confluence page creation, content search, space management, labels, and hierarchy navigation via Rube MCP (Composio).
  `B:\AI-Armory\skill-pakz\rs-business-automation\confluence-automation`
- **customer-support** — Elite AI-powered customer support specialist mastering conversational AI, automated ticketing, sentiment analysis, and omnichannel support experiences.
  `B:\AI-Armory\skill-pakz\rs-business-automation\customer-support`
- **discord-automation** — Automate Discord tasks via Rube MCP (Composio): messages, channels, roles, webhooks, reactions.
  `B:\AI-Armory\skill-pakz\rs-business-automation\discord-automation`
- **email-ops** — Evidence-first mailbox triage, drafting, send verification, and sent-mail-safe follow-up workflow for ECC.
  `B:\AI-Armory\skill-pakz\rs-business-automation\email-ops`
- **google-workspace-ops** — Operate across Google Drive, Docs, Sheets, and Slides as one workflow surface for plans, trackers, decks, and shared documents.
  `B:\AI-Armory\skill-pakz\rs-business-automation\google-workspace-ops`
- **invoice-organizer** — Automatically organizes invoices and receipts for tax preparation by reading messy files, extracting key information, renaming them consistently, and sorting them into logical folders.
  `B:\AI-Armory\skill-pakz\rs-business-automation\invoice-organizer`
- **jira-integration** — Use this skill when retrieving Jira tickets, analyzing requirements, updating ticket status, adding comments, or transitioning issues.
  `B:\AI-Armory\skill-pakz\rs-business-automation\jira-integration`
- **notion** — Notion API for creating and managing pages, databases, and blocks.
  `B:\AI-Armory\skill-pakz\rs-business-automation\notion`
- **project-flow-ops** — Operate execution flow across GitHub and Linear by triaging issues and pull requests, linking active work, and keeping GitHub public-facing while Linear remains the internal execution layer.
  `B:\AI-Armory\skill-pakz\rs-business-automation\project-flow-ops`
- **slack** — Use when you need to control Slack from OpenClaw via the slack tool, including reacting to messages or pinning/unpinning items in Slack channels or DMs.
  `B:\AI-Armory\skill-pakz\rs-business-automation\slack`
- **trello** — Manage Trello boards, lists, and cards via the Trello REST API.
  `B:\AI-Armory\skill-pakz\rs-business-automation\trello`

</details>

<details><summary><b>rs-code-quality-devops</b> (14 skills)</summary>

- **cicd-automation-workflow-automate** — You are a workflow automation expert specializing in creating efficient CI/CD pipelines, GitHub Actions workflows, and automated development processes.
  `B:\AI-Armory\skill-pakz\rs-code-quality-devops\cicd-automation-workflow-automate`
- **clean-code** — This skill embodies the principles of \"Clean Code\" by Robert C.
  `B:\AI-Armory\skill-pakz\rs-code-quality-devops\clean-code`
- **code-review-checklist** — Comprehensive checklist for conducting thorough code reviews covering functionality, security, performance, and maintainability
  `B:\AI-Armory\skill-pakz\rs-code-quality-devops\code-review-checklist`
- **code-review-excellence** — Transform code reviews from gatekeeping to knowledge sharing through constructive feedback, systematic analysis, and collaborative improvement.
  `B:\AI-Armory\skill-pakz\rs-code-quality-devops\code-review-excellence`
- **code-reviewer** — Elite code review expert specializing in modern AI-powered code
  `B:\AI-Armory\skill-pakz\rs-code-quality-devops\code-reviewer`
- **code-simplifier** — Simplifies and refines code for clarity, consistency, and maintainability while preserving all functionality.
  `B:\AI-Armory\skill-pakz\rs-code-quality-devops\code-simplifier`
- **codebase-audit-pre-push** — Deep audit before GitHub push: removes junk files, dead code, security holes, and optimization issues.
  `B:\AI-Armory\skill-pakz\rs-code-quality-devops\codebase-audit-pre-push`  ·  _tags:_ development
- **coding-standards** — Baseline cross-project coding conventions for naming, readability, immutability, and code-quality review.
  `B:\AI-Armory\skill-pakz\rs-code-quality-devops\coding-standards`
- **debugging-strategies** — Transform debugging from frustrating guesswork into systematic problem-solving with proven strategies, powerful tools, and methodical approaches.
  `B:\AI-Armory\skill-pakz\rs-code-quality-devops\debugging-strategies`
- **deployment-patterns** — Deployment workflows, CI/CD pipeline patterns, Docker containerization, health checks, rollback strategies, and production readiness checklists for web applications.
  `B:\AI-Armory\skill-pakz\rs-code-quality-devops\deployment-patterns`
- **devops-troubleshooter** — Expert DevOps troubleshooter specializing in rapid incident response, advanced debugging, and modern observability.
  `B:\AI-Armory\skill-pakz\rs-code-quality-devops\devops-troubleshooter`
- **docker-expert** — You are an advanced Docker containerization expert with comprehensive, practical knowledge of container optimization, security hardening, multi-stage builds, orchestration patterns, and production...
  `B:\AI-Armory\skill-pakz\rs-code-quality-devops\docker-expert`  ·  _tags:_ devops
- **docker-patterns** — Docker and Docker Compose patterns for local development, container security, networking, volume strategies, and multi-service orchestration.
  `B:\AI-Armory\skill-pakz\rs-code-quality-devops\docker-patterns`
- **tdd-workflow** — Use this skill when writing new features, fixing bugs, or refactoring code.
  `B:\AI-Armory\skill-pakz\rs-code-quality-devops\tdd-workflow`

</details>

<details><summary><b>rs-security-redteam</b> (14 skills)</summary>

- **active-directory-attacks** — Provide comprehensive techniques for attacking Microsoft Active Directory environments.
  `B:\AI-Armory\skill-pakz\rs-security-redteam\active-directory-attacks`
- **anti-reversing-techniques** — AUTHORIZED USE ONLY: This skill contains dual-use security techniques.
  `B:\AI-Armory\skill-pakz\rs-security-redteam\anti-reversing-techniques`
- **api-fuzzing-bug-bounty** — Provide comprehensive techniques for testing REST, SOAP, and GraphQL APIs during bug bounty hunting and penetration testing engagements.
  `B:\AI-Armory\skill-pakz\rs-security-redteam\api-fuzzing-bug-bounty`
- **api-security-testing** — API security testing workflow for REST and GraphQL APIs covering authentication, authorization, rate limiting, input validation, and security best practices.
  `B:\AI-Armory\skill-pakz\rs-security-redteam\api-security-testing`  ·  _tags:_ granular-workflow-bundle
- **attack-tree-construction** — Build comprehensive attack trees to visualize threat paths.
  `B:\AI-Armory\skill-pakz\rs-security-redteam\attack-tree-construction`
- **aws-penetration-testing** — Provide comprehensive techniques for penetration testing AWS cloud environments.
  `B:\AI-Armory\skill-pakz\rs-security-redteam\aws-penetration-testing`
- **binary-analysis-patterns** — Comprehensive patterns and techniques for analyzing compiled binaries, understanding assembly code, and reconstructing program logic.
  `B:\AI-Armory\skill-pakz\rs-security-redteam\binary-analysis-patterns`
- **broken-authentication** — Identify and exploit authentication and session management vulnerabilities in web applications.
  `B:\AI-Armory\skill-pakz\rs-security-redteam\broken-authentication`
- **burp-suite-testing** — Execute comprehensive web application security testing using Burp Suite's integrated toolset, including HTTP traffic interception and modification, request analysis and replay, automated...
  `B:\AI-Armory\skill-pakz\rs-security-redteam\burp-suite-testing`
- **cloud-penetration-testing** — Conduct comprehensive security assessments of cloud infrastructure across Microsoft Azure, Amazon Web Services (AWS), and Google Cloud Platform (GCP).
  `B:\AI-Armory\skill-pakz\rs-security-redteam\cloud-penetration-testing`
- **godmode** — Jailbreak LLMs: Parseltongue, GODMODE, ULTRAPLINIAN.
  `B:\AI-Armory\skill-pakz\rs-security-redteam\red-teaming\godmode`
- **security-bounty-hunter** — Hunt for exploitable, bounty-worthy security issues in repositories.
  `B:\AI-Armory\skill-pakz\rs-security-redteam\security-bounty-hunter`
- **security-review** — Use this skill when adding authentication, handling user input, working with secrets, creating API endpoints, or implementing payment/sensitive features.
  `B:\AI-Armory\skill-pakz\rs-security-redteam\security-review`
- **security-scan** — Scan your Claude Code configuration (.claude/ directory) for security vulnerabilities, misconfigurations, and injection risks using AgentShield.
  `B:\AI-Armory\skill-pakz\rs-security-redteam\security-scan`

</details>

<details><summary><b>rs-agent-automation</b> (13 skills)</summary>

- **agent-evaluation** — Testing and benchmarking LLM agents including behavioral testing,
  `B:\AI-Armory\skill-pakz\rs-agent-automation\agent-evaluation`
- **agent-harness-construction** — Design and optimize AI agent action spaces, tool definitions, and observation formatting for higher completion rates.
  `B:\AI-Armory\skill-pakz\rs-agent-automation\agent-harness-construction`
- **agent-memory-systems** — Memory is the cornerstone of intelligent agents.
  `B:\AI-Armory\skill-pakz\rs-agent-automation\agent-memory-systems`
- **agent-orchestration-multi-agent-optimize** — Optimize multi-agent systems with coordinated profiling, workload distribution, and cost-aware orchestration.
  `B:\AI-Armory\skill-pakz\rs-agent-automation\agent-orchestration-multi-agent-optimize`
- **agent-tool-builder** — Tools are how AI agents interact with the world.
  `B:\AI-Armory\skill-pakz\rs-agent-automation\agent-tool-builder`
- **autonomous-loops** — Patterns and architectures for autonomous Claude Code loops — from simple sequential pipelines to RFC-driven multi-agent DAG systems.
  `B:\AI-Armory\skill-pakz\rs-agent-automation\autonomous-loops`
- **context-management-context-restore** — Use when working with context management context restore
  `B:\AI-Armory\skill-pakz\rs-agent-automation\context-management-context-restore`
- **context-management-context-save** — Use when working with context management context save
  `B:\AI-Armory\skill-pakz\rs-agent-automation\context-management-context-save`
- **continuous-agent-loop** — Patterns for continuous autonomous agent loops with quality gates, evals, and recovery controls.
  `B:\AI-Armory\skill-pakz\rs-agent-automation\continuous-agent-loop`
- **continuous-learning-v2** — Instinct-based learning system that observes sessions via hooks, creates atomic instincts with confidence scoring, and evolves them into skills/commands/agents. v2.1 adds project-scoped instincts to...
  `B:\AI-Armory\skill-pakz\rs-agent-automation\continuous-learning-v2`
- **dispatching-parallel-agents** — Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies
  `B:\AI-Armory\skill-pakz\rs-agent-automation\dispatching-parallel-agents`
- **openclaw-persona-forge** — 为 OpenClaw AI Agent 锻造完整的龙虾灵魂方案。根据用户偏好或随机抽卡， 输出身份定位、灵魂描述(SOUL.md)、角色化底线规则、名字和头像生图提示词。 如当前环境提供已审核的生图 skill，可自动生成统一风格头像图片。 当用户需要创建、设计或定制 OpenClaw 龙虾灵魂时使用。 不适用于：微调已有 SOUL.md、非 OpenClaw 平台的角色设计、纯工具型无性格...
  `B:\AI-Armory\skill-pakz\rs-agent-automation\openclaw-persona-forge`
- **skill-creator** — Create, edit, improve, or audit AgentSkills.
  `B:\AI-Armory\skill-pakz\rs-agent-automation\skill-creator`

</details>

<details><summary><b>rs-ai-engineering</b> (13 skills)</summary>

- **agent-harness-construction** — Design and optimize AI agent action spaces, tool definitions, and observation formatting for higher completion rates.
  `B:\AI-Armory\skill-pakz\rs-ai-engineering\agent-harness-construction`
- **agent-memory-systems** — Memory is the cornerstone of intelligent agents.
  `B:\AI-Armory\skill-pakz\rs-ai-engineering\agent-memory-systems`
- **agent-orchestrator** — Meta-skill que orquestra todos os agentes do ecossistema.
  `B:\AI-Armory\skill-pakz\rs-ai-engineering\agent-orchestrator`
- **ai-agents-architect** — Expert in designing and building autonomous AI agents.
  `B:\AI-Armory\skill-pakz\rs-ai-engineering\ai-agents-architect`
- **ai-engineer** — Build production-ready LLM applications, advanced RAG systems, and intelligent agents.
  `B:\AI-Armory\skill-pakz\rs-ai-engineering\ai-engineer`
- **ai-engineering-toolkit** — 6 production-ready AI engineering workflows: prompt evaluation (8-dimension scoring), context budget planning, RAG pipeline design, agent security audit (65-point checklist), eval harness building...
  `B:\AI-Armory\skill-pakz\rs-ai-engineering\ai-engineering-toolkit`  ·  _tags:_ prompt-engineering, rag, security, evaluation, ai-engineering, llm
- **ai-first-engineering** — Engineering operating model for teams where AI agents generate a large share of implementation output.
  `B:\AI-Armory\skill-pakz\rs-ai-engineering\ai-first-engineering`
- **autonomous-agent-patterns** — Design patterns for building autonomous coding agents, inspired by [Cline](https://github.com/cline/cline) and [OpenAI Codex](https://github.com/openai/codex).
  `B:\AI-Armory\skill-pakz\rs-ai-engineering\autonomous-agent-patterns`
- **computer-use-agents** — Build AI agents that interact with computers like humans do -
  `B:\AI-Armory\skill-pakz\rs-ai-engineering\computer-use-agents`
- **cost-aware-llm-pipeline** — Cost optimization patterns for LLM API usage — model routing by task complexity, budget tracking, retry logic, and prompt caching.
  `B:\AI-Armory\skill-pakz\rs-ai-engineering\cost-aware-llm-pipeline`
- **mcp-builder** — Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools.
  `B:\AI-Armory\skill-pakz\rs-ai-engineering\mcp-builder`
- **mcp-server-patterns** — Build MCP servers with Node/TypeScript SDK — tools, resources, prompts, Zod validation, stdio vs Streamable HTTP.
  `B:\AI-Armory\skill-pakz\rs-ai-engineering\mcp-server-patterns`
- **prompt-optimizer** — Analyze raw prompts, identify intent and gaps, match ECC components (skills/commands/agents/hooks), and output a ready-to-paste optimized prompt.
  `B:\AI-Armory\skill-pakz\rs-ai-engineering\prompt-optimizer`

</details>

<details><summary><b>rs-sales-lead-ops</b> (13 skills)</summary>

- **awareness-stage-mapper** — One sentence - what this skill does and when to invoke it
  `B:\AI-Armory\skill-pakz\rs-sales-lead-ops\awareness-stage-mapper`
- **cold-email** — Write B2B cold emails and follow-up sequences that get replies.
  `B:\AI-Armory\skill-pakz\rs-sales-lead-ops\cold-email`
- **competitive-landscape** — Comprehensive frameworks for analyzing competition, identifying differentiation opportunities, and developing winning market positioning strategies.
  `B:\AI-Armory\skill-pakz\rs-sales-lead-ops\competitive-landscape`
- **competitor-alternatives** — When the user wants to create competitor comparison or alternative pages for SEO and sales enablement.
  `B:\AI-Armory\skill-pakz\rs-sales-lead-ops\competitor-alternatives`
- **competitor-profiling** — When the user wants to research, profile, or analyze competitors from their URLs.
  `B:\AI-Armory\skill-pakz\rs-sales-lead-ops\competitor-profiling`
- **customer-psychographic-profiler** — One sentence - what this skill does and when to invoke it
  `B:\AI-Armory\skill-pakz\rs-sales-lead-ops\customer-psychographic-profiler`
- **customer-research** — When the user wants to conduct, analyze, or synthesize customer research.
  `B:\AI-Armory\skill-pakz\rs-sales-lead-ops\customer-research`
- **email-sequence** — When the user wants to create or optimize an email sequence, drip campaign, automated email flow, or lifecycle email program.
  `B:\AI-Armory\skill-pakz\rs-sales-lead-ops\email-sequence`
- **lead-intelligence** — AI-native lead intelligence and outreach pipeline.
  `B:\AI-Armory\skill-pakz\rs-sales-lead-ops\lead-intelligence`
- **lead-magnets** — When the user wants to create, plan, or optimize a lead magnet for email capture or lead generation.
  `B:\AI-Armory\skill-pakz\rs-sales-lead-ops\lead-magnets`
- **lead-research-assistant** — Identifies high-quality leads for your product or service by analyzing your business, searching for target companies, and providing actionable contact strategies.
  `B:\AI-Armory\skill-pakz\rs-sales-lead-ops\lead-research-assistant`
- **revops** — When the user wants help with revenue operations, lead lifecycle management, or marketing-to-sales handoff processes.
  `B:\AI-Armory\skill-pakz\rs-sales-lead-ops\revops`
- **sales-enablement** — When the user wants to create sales collateral, pitch decks, one-pagers, objection handling docs, or demo scripts.
  `B:\AI-Armory\skill-pakz\rs-sales-lead-ops\sales-enablement`

</details>

<details><summary><b>rs-data-analytics</b> (12 skills)</summary>

- **analytics-product** — Analytics de produto — PostHog, Mixpanel, eventos, funnels, cohorts, retencao, north star metric, OKRs e dashboards de produto.
  `B:\AI-Armory\skill-pakz\rs-data-analytics\analytics-product`
- **analytics-tracking** — When the user wants to set up, improve, or audit analytics tracking and measurement.
  `B:\AI-Armory\skill-pakz\rs-data-analytics\analytics-tracking`
- **dashboard-builder** — Build monitoring dashboards that answer real operator questions for Grafana, SigNoz, and similar platforms.
  `B:\AI-Armory\skill-pakz\rs-data-analytics\dashboard-builder`
- **data-engineer** — Build scalable data pipelines, modern data warehouses, and real-time streaming architectures.
  `B:\AI-Armory\skill-pakz\rs-data-analytics\data-engineer`
- **data-quality-frameworks** — Implement data quality validation with Great Expectations, dbt tests, and data contracts.
  `B:\AI-Armory\skill-pakz\rs-data-analytics\data-quality-frameworks`
- **data-scientist** — Expert data scientist for advanced analytics, machine learning, and statistical modeling.
  `B:\AI-Armory\skill-pakz\rs-data-analytics\data-scientist`
- **data-storytelling** — Transform raw data into compelling narratives that drive decisions and inspire action.
  `B:\AI-Armory\skill-pakz\rs-data-analytics\data-storytelling`
- **database-architect** — Expert database architect specializing in data layer design from scratch, technology selection, schema modeling, and scalable database architectures.
  `B:\AI-Armory\skill-pakz\rs-data-analytics\database-architect`
- **database-design** — Database design principles and decision-making.
  `B:\AI-Armory\skill-pakz\rs-data-analytics\database-design`
- **database-optimizer** — Expert database optimizer specializing in modern performance tuning, query optimization, and scalable architectures.
  `B:\AI-Armory\skill-pakz\rs-data-analytics\database-optimizer`
- **dbt-transformation-patterns** — Production-ready patterns for dbt (data build tool) including model organization, testing strategies, documentation, and incremental processing.
  `B:\AI-Armory\skill-pakz\rs-data-analytics\dbt-transformation-patterns`
- **postgres-patterns** — PostgreSQL database patterns for query optimization, schema design, indexing, and security.
  `B:\AI-Armory\skill-pakz\rs-data-analytics\postgres-patterns`

</details>

<details><summary><b>rs-frontend-design</b> (12 skills)</summary>

- **3d-web-experience** — Expert in building 3D experiences for the web - Three.js, React
  `B:\AI-Armory\skill-pakz\rs-frontend-design\3d-web-experience`
- **baseline-ui** — Validates animation durations, enforces typography scale, checks component accessibility, and prevents layout anti-patterns in Tailwind CSS projects.
  `B:\AI-Armory\skill-pakz\rs-frontend-design\baseline-ui`
- **browser-extension-builder** — Expert in building browser extensions that solve real problems -
  `B:\AI-Armory\skill-pakz\rs-frontend-design\browser-extension-builder`
- **building-native-ui** — Complete guide for building beautiful apps with Expo Router.
  `B:\AI-Armory\skill-pakz\rs-frontend-design\building-native-ui`
- **canvas-design** — These are instructions for creating design philosophies - aesthetic movements that are then EXPRESSED VISUALLY.
  `B:\AI-Armory\skill-pakz\rs-frontend-design\canvas-design`
- **chrome-extension-developer** — Expert in building Chrome Extensions using Manifest V3.
  `B:\AI-Armory\skill-pakz\rs-frontend-design\chrome-extension-developer`
- **design-spells** — Curated micro-interactions and design details that add "magic" and personality to websites and apps.
  `B:\AI-Armory\skill-pakz\rs-frontend-design\design-spells`
- **design-system** — Use this skill to generate or audit design systems, check visual consistency, and review PRs that touch styling.
  `B:\AI-Armory\skill-pakz\rs-frontend-design\design-system`
- **design-taste-frontend** — Use when building high-agency frontend interfaces with strict design taste, calibrated color, responsive layout, and motion rules.
  `B:\AI-Armory\skill-pakz\rs-frontend-design\design-taste-frontend`  ·  _tags:_ frontend, design, ui, react
- **frontend-design** — Create distinctive, production-grade frontend interfaces with high design quality.
  `B:\AI-Armory\skill-pakz\rs-frontend-design\frontend-design`
- **frontend-patterns** — Frontend development patterns for React, Next.js, state management, performance optimization, and UI best practices.
  `B:\AI-Armory\skill-pakz\rs-frontend-design\frontend-patterns`
- **liquid-glass-design** — iOS 26 Liquid Glass design system — dynamic glass material with blur, reflection, and interactive morphing for SwiftUI, UIKit, and WidgetKit.
  `B:\AI-Armory\skill-pakz\rs-frontend-design\liquid-glass-design`

</details>

---

## skillz

*Skills, one folder per skill.*

**3055 files** · **1559 skills**  ·  2014 .md · 173 .py · 133 .csv · 130 .ts · 82 .json · 78 .xsd

<details><summary><b>Everything-Automated</b> (850 skills)</summary>

- **-21risk-automation** — Automate 21risk tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\-21risk-automation`
- **-2chat-automation** — Automate 2chat tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\-2chat-automation`
- **ably-automation** — Automate Ably tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\ably-automation`
- **abstract-automation** — Automate Abstract tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\abstract-automation`
- **abuselpdb-automation** — Automate Abuselpdb tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\abuselpdb-automation`
- **abyssale-automation** — Automate Abyssale tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\abyssale-automation`
- **accelo-automation** — Automate Accelo tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\accelo-automation`
- **accredible-certificates-automation** — Automate Accredible Certificates tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\accredible-certificates-automation`
- **acculynx-automation** — Automate Acculynx tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\acculynx-automation`
- **active-campaign-automation** — Automate ActiveCampaign tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\active-campaign-automation`
- **addresszen-automation** — Automate Addresszen tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\addresszen-automation`
- **adobe-automation** — Automate Adobe tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\adobe-automation`
- **adrapid-automation** — Automate Adrapid tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\adrapid-automation`
- **adyntel-automation** — Automate Adyntel tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\adyntel-automation`
- **aero-workflow-automation** — Automate Aero Workflow tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\aero-workflow-automation`
- **aeroleads-automation** — Automate Aeroleads tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\aeroleads-automation`
- **affinda-automation** — Automate Affinda tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\affinda-automation`
- **affinity-automation** — Automate Affinity tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\affinity-automation`
- **agencyzoom-automation** — Automate Agencyzoom tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\agencyzoom-automation`
- **agent-mail-automation** — Automate Agent Mail tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\agent-mail-automation`
- **agentql-automation** — Automate Agentql tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\agentql-automation`
- **agenty-automation** — Automate Agenty tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\agenty-automation`
- **agiled-automation** — Automate Agiled tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\agiled-automation`
- **agility-cms-automation** — Automate Agility CMS tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\agility-cms-automation`
- **Ahrefs Automation** — Automate SEO research with Ahrefs -- analyze backlink profiles, research keywords, track domain metrics history, audit organic rankings, and perform batch URL analysis through the Composio Ahrefs...
  `B:\AI-Armory\skillz\Everything-Automated\ahrefs-automation`
- **ai-ml-api-automation** — Automate AI ML API tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\ai-ml-api-automation`
- **aivoov-automation** — Automate Aivoov tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\aivoov-automation`
- **alchemy-automation** — Automate Alchemy tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\alchemy-automation`
- **algodocs-automation** — Automate Algodocs tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\algodocs-automation`
- **algolia-automation** — Automate Algolia tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\algolia-automation`
- **all-images-ai-automation** — Automate All Images AI tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\all-images-ai-automation`
- **alpha-vantage-automation** — Automate Alpha Vantage tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\alpha-vantage-automation`
- **altoviz-automation** — Automate Altoviz tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\altoviz-automation`
- **alttext-ai-automation** — Automate Alttext AI tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\alttext-ai-automation`
- **amara-automation** — Automate Amara tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\amara-automation`
- **amazon-automation** — Automate Amazon tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\amazon-automation`
- **ambee-automation** — Automate Ambee tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\ambee-automation`
- **ambient-weather-automation** — Automate Ambient Weather tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\ambient-weather-automation`
- **amcards-automation** — Automate Amcards tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\amcards-automation`
- **anchor-browser-automation** — Automate Anchor Browser tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\anchor-browser-automation`
- **anonyflow-automation** — Automate Anonyflow tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\anonyflow-automation`
- **anthropic_administrator-automation** — Automate Anthropic Admin tasks via Rube MCP (Composio): API keys, usage, workspaces, and organization management.
  `B:\AI-Armory\skillz\Everything-Automated\anthropic_administrator-automation`
- **anthropic-administrator-automation** — Automate Anthropic Admin tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\anthropic-administrator-automation`
- **apaleo-automation** — Automate Apaleo tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\apaleo-automation`
- **apex27-automation** — Automate Apex27 tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\apex27-automation`
- **api-bible-automation** — Automate API Bible tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\api-bible-automation`
- **api-labz-automation** — Automate API Labz tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\api-labz-automation`
- **api-ninjas-automation** — Automate API Ninjas tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\api-ninjas-automation`
- **api-sports-automation** — Automate API Sports tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\api-sports-automation`
- **api2pdf-automation** — Automate Api2pdf tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\api2pdf-automation`
- **apiflash-automation** — Automate Apiflash tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\apiflash-automation`
- **Apify Automation** — Automate web scraping and data extraction with Apify -- run Actors, manage datasets, create reusable tasks, and retrieve crawl results through the Composio Apify integration.
  `B:\AI-Armory\skillz\Everything-Automated\apify-automation`
- **apilio-automation** — Automate Apilio tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\apilio-automation`
- **apipie-ai-automation** — Automate Apipie AI tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\apipie-ai-automation`
- **apitemplate-io-automation** — Automate Apitemplate IO tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\apitemplate-io-automation`
- **apiverve-automation** — Automate Apiverve tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\apiverve-automation`
- **Apollo Automation** — Automate Apollo.io lead generation -- search organizations, discover contacts, enrich prospect data, manage contact stages, and build targeted outreach lists -- using natural language through the...
  `B:\AI-Armory\skillz\Everything-Automated\apollo-automation`  ·  _tags:_ sales-intelligence
- **appcircle-automation** — Automate Appcircle tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\appcircle-automation`
- **appdrag-automation** — Automate Appdrag tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\appdrag-automation`
- **appointo-automation** — Automate Appointo tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\appointo-automation`
- **appsflyer-automation** — Automate Appsflyer tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\appsflyer-automation`
- **appveyor-automation** — Automate Appveyor tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\appveyor-automation`
- **article-writing** — Write articles, guides, blog posts, tutorials, newsletter issues, and other long-form content in a distinctive voice derived from supplied examples or brand guidance.
  `B:\AI-Armory\skillz\Everything-Automated\article-writing`
- **artifacts-builder** — Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui).
  `B:\AI-Armory\skillz\Everything-Automated\artifacts-builder`
- **aryn-automation** — Automate Aryn tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\aryn-automation`
- **asana-automation** — Automate Asana tasks via Rube MCP (Composio): tasks, projects, sections, teams, workspaces.
  `B:\AI-Armory\skillz\Everything-Automated\asana-automation`
- **ascora-automation** — Automate Ascora tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\ascora-automation`
- **Ashby Automation** — Automate recruiting and hiring workflows in Ashby -- manage candidates, jobs, applications, interviews, and notes through natural language commands.
  `B:\AI-Armory\skillz\Everything-Automated\ashby-automation`
- **asin-data-api-automation** — Automate Asin Data API tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\asin-data-api-automation`
- **astica-ai-automation** — Automate Astica AI tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\astica-ai-automation`
- **async-interview-automation** — Automate Async Interview tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\async-interview-automation`
- **atlassian-automation** — Automate Atlassian tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\atlassian-automation`
- **attack-tree-construction** — Build comprehensive attack trees to visualize threat paths.
  `B:\AI-Armory\skillz\Everything-Automated\attack-tree-construction`
- **Attio Automation** — Automate Attio CRM operations -- search records, query contacts and companies with advanced filters, manage notes, list attributes, and navigate your relationship data -- using natural language...
  `B:\AI-Armory\skillz\Everything-Automated\attio-automation`  ·  _tags:_ crm
- **auth0-automation** — Automate Auth0 tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\auth0-automation`
- **autobound-automation** — Automate Autobound tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\autobound-automation`
- **autom-automation** — Automate Autom tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\autom-automation`
- **autonomous-agent-patterns** — Design patterns for building autonomous coding agents, inspired by [Cline](https://github.com/cline/cline) and [OpenAI Codex](https://github.com/openai/codex).
  `B:\AI-Armory\skillz\Everything-Automated\autonomous-agent-patterns`
- **autonomous-loops** — Patterns and architectures for autonomous Claude Code loops — from simple sequential pipelines to RFC-driven multi-agent DAG systems.
  `B:\AI-Armory\skillz\Everything-Automated\autonomous-loops`
- **aws-penetration-testing** — Provide comprehensive techniques for penetration testing AWS cloud environments.
  `B:\AI-Armory\skillz\Everything-Automated\aws-penetration-testing`
- **axonaut-automation** — Automate Axonaut tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\axonaut-automation`
- **ayrshare-automation** — Automate Ayrshare tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\ayrshare-automation`
- **backend-patterns** — Node.js, Express ve Next.js API routes için backend mimari kalıpları, API tasarımı, veritabanı optimizasyonu ve sunucu tarafı en iyi uygulamalar.
  `B:\AI-Armory\skillz\Everything-Automated\backend-patterns`
- **backendless-automation** — Automate Backendless tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\backendless-automation`
- **bannerbear-automation** — Automate Bannerbear tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\bannerbear-automation`
- **bart-automation** — Automate Bart tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\bart-automation`
- **baselinker-automation** — Automate Baselinker tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\baselinker-automation`
- **baserow-automation** — Automate Baserow tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\baserow-automation`
- **basin-automation** — Automate Basin tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\basin-automation`
- **battlenet-automation** — Automate Battlenet tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\battlenet-automation`
- **beaconchain-automation** — Automate Beaconchain tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\beaconchain-automation`
- **beaconstac-automation** — Automate Beaconstac tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\beaconstac-automation`
- **beamer-automation** — Automate Beamer tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\beamer-automation`
- **beeminder-automation** — Automate Beeminder tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\beeminder-automation`
- **bench-automation** — Automate Bench tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\bench-automation`
- **benchmark-email-automation** — Automate Benchmark Email tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\benchmark-email-automation`
- **benzinga-automation** — Automate Benzinga tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\benzinga-automation`
- **bestbuy-automation** — Automate Bestbuy tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\bestbuy-automation`
- **better-proposals-automation** — Automate Better Proposals tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\better-proposals-automation`
- **better-stack-automation** — Automate Better Stack tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\better-stack-automation`
- **bidsketch-automation** — Automate Bidsketch tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\bidsketch-automation`
- **big-data-cloud-automation** — Automate Big Data Cloud tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\big-data-cloud-automation`
- **bigmailer-automation** — Automate Bigmailer tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\bigmailer-automation`
- **bigml-automation** — Automate Bigml tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\bigml-automation`
- **bigpicture-io-automation** — Automate Bigpicture IO tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\bigpicture-io-automation`
- **bitquery-automation** — Automate Bitquery tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\bitquery-automation`
- **bitwarden-automation** — Automate Bitwarden tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\bitwarden-automation`
- **blackbaud-automation** — Automate Blackbaud tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\blackbaud-automation`
- **blackboard-automation** — Automate Blackboard tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\blackboard-automation`
- **blocknative-automation** — Automate Blocknative tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\blocknative-automation`
- **boldsign-automation** — Automate Boldsign tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\boldsign-automation`
- **bolna-automation** — Automate Bolna tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\bolna-automation`
- **boloforms-automation** — Automate Boloforms tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\boloforms-automation`
- **bolt-iot-automation** — Automate Bolt Iot tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\bolt-iot-automation`
- **bonsai-automation** — Automate Bonsai tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\bonsai-automation`
- **bookingmood-automation** — Automate Bookingmood tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\bookingmood-automation`
- **booqable-automation** — Automate Booqable tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\booqable-automation`
- **borneo-automation** — Automate Borneo tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\borneo-automation`
- **botbaba-automation** — Automate Botbaba tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\botbaba-automation`
- **botpress-automation** — Automate Botpress tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\botpress-automation`
- **botsonic-automation** — Automate Botsonic tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\botsonic-automation`
- **botstar-automation** — Automate Botstar tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\botstar-automation`
- **bouncer-automation** — Automate Bouncer tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\bouncer-automation`
- **boxhero-automation** — Automate Boxhero tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\boxhero-automation`
- **Braintree Automation** — Braintree Automation: manage payment processing via Stripe-compatible tools for customers, subscriptions, payment methods, and transactions
  `B:\AI-Armory\skillz\Everything-Automated\braintree-automation`
- **brand-guidelines** — Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-and-feel.
  `B:\AI-Armory\skillz\Everything-Automated\brand-guidelines`
- **brandfetch-automation** — Automate Brandfetch tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\brandfetch-automation`
- **breeze-automation** — Automate Breeze tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\breeze-automation`
- **breezy-hr-automation** — Automate Breezy HR tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\breezy-hr-automation`
- **brex-automation** — Automate Brex tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\brex-automation`
- **brex-staging-automation** — Automate Brex Staging tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\brex-staging-automation`
- **brightdata-automation** — Automate Brightdata tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\brightdata-automation`
- **brightpearl-automation** — Automate Brightpearl tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\brightpearl-automation`
- **brilliant-directories-automation** — Automate Brilliant Directories tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\brilliant-directories-automation`
- **browseai-automation** — Automate Browseai tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\browseai-automation`
- **browser-tool-automation** — Automate Browser Tool tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\browser-tool-automation`
- **browserbase-tool-automation** — Automate Browserbase Tool tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\browserbase-tool-automation`
- **browserhub-automation** — Automate Browserhub tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\browserhub-automation`
- **browserless-automation** — Automate Browserless tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\browserless-automation`
- **btcpay-server-automation** — Automate Btcpay Server tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\btcpay-server-automation`
- **bubble-automation** — Automate Bubble tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\bubble-automation`
- **bugbug-automation** — Automate Bugbug tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\bugbug-automation`
- **bugherd-automation** — Automate Bugherd tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\bugherd-automation`
- **bugsnag-automation** — Automate Bugsnag tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\bugsnag-automation`
- **buildkite-automation** — Automate Buildkite tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\buildkite-automation`
- **builtwith-automation** — Automate Builtwith tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\builtwith-automation`
- **bunnycdn-automation** — Automate Bunnycdn tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\bunnycdn-automation`
- **byteforms-automation** — Automate Byteforms tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\byteforms-automation`
- **cabinpanda-automation** — Automate Cabinpanda tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\cabinpanda-automation`
- **cal-automation** — Automate Cal tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\cal-automation`
- **calendarhero-automation** — Automate Calendarhero tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\calendarhero-automation`
- **callerapi-automation** — Automate Callerapi tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\callerapi-automation`
- **callingly-automation** — Automate Callingly tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\callingly-automation`
- **callpage-automation** — Automate Callpage tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\callpage-automation`
- **campaign-cleaner-automation** — Automate Campaign Cleaner tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\campaign-cleaner-automation`
- **campayn-automation** — Automate Campayn tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\campayn-automation`
- **canny-automation** — Automate Canny tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\canny-automation`
- **canvas-automation** — Automate Canvas tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\canvas-automation`
- **canvas-design** — Create beautiful visual art in .png and .pdf documents using design philosophy.
  `B:\AI-Armory\skillz\Everything-Automated\canvas-design`
- **Capsule CRM Automation** — Automate Capsule CRM operations -- manage contacts (parties), run structured filter queries, track tasks and projects, log entries, and handle organizations -- using natural language through the...
  `B:\AI-Armory\skillz\Everything-Automated\capsule-crm-automation`  ·  _tags:_ crm
- **capsule_crm-automation** — Automate Capsule CRM tasks via Rube MCP (Composio): contacts, opportunities, cases, tasks, and pipeline management.
  `B:\AI-Armory\skillz\Everything-Automated\capsule_crm-automation`
- **carbone-automation** — Automate Carbone tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\carbone-automation`
- **cardly-automation** — Automate Cardly tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\cardly-automation`
- **castingwords-automation** — Automate Castingwords tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\castingwords-automation`
- **cats-automation** — Automate Cats tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\cats-automation`
- **cdr-platform-automation** — Automate Cdr Platform tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\cdr-platform-automation`
- **census-bureau-automation** — Automate Census Bureau tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\census-bureau-automation`
- **centralstationcrm-automation** — Automate Centralstationcrm tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\centralstationcrm-automation`
- **certifier-automation** — Automate Certifier tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\certifier-automation`
- **changelog-generator** — Automatically creates user-facing changelogs from git commits by analyzing commit history, categorizing changes, and transforming technical commits into clear, customer-friendly release notes.
  `B:\AI-Armory\skillz\Everything-Automated\changelog-generator`
- **chaser-automation** — Automate Chaser tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\chaser-automation`
- **chatbotkit-automation** — Automate Chatbotkit tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\chatbotkit-automation`
- **chatfai-automation** — Automate Chatfai tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\chatfai-automation`
- **chatwork-automation** — Automate Chatwork tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\chatwork-automation`
- **chmeetings-automation** — Automate Chmeetings tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\chmeetings-automation`
- **cincopa-automation** — Automate Cincopa tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\cincopa-automation`
- **claid-ai-automation** — Automate Claid AI tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\claid-ai-automation`
- **classmarker-automation** — Automate Classmarker tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\classmarker-automation`
- **clearout-automation** — Automate Clearout tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\clearout-automation`
- **clickmeeting-automation** — Automate Clickmeeting tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\clickmeeting-automation`
- **Clockify Automation** — Automate time tracking workflows in Clockify -- create and manage time entries, workspaces, and users through natural language commands.
  `B:\AI-Armory\skillz\Everything-Automated\clockify-automation`
- **cloudcart-automation** — Automate Cloudcart tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\cloudcart-automation`
- **cloudconvert-automation** — Automate Cloudconvert tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\cloudconvert-automation`
- **cloudflare-api-key-automation** — Automate Cloudflare API tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\cloudflare-api-key-automation`
- **cloudflare-automation** — Automate Cloudflare tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\cloudflare-automation`
- **cloudflare-browser-rendering-automation** — Automate Cloudflare Browser Rendering tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\cloudflare-browser-rendering-automation`
- **Cloudinary Automation** — Automate Cloudinary media management including folder organization, upload presets, asset lookup, transformations, and usage monitoring through natural language commands
  `B:\AI-Armory\skillz\Everything-Automated\cloudinary-automation`
- **cloudlayer-automation** — Automate Cloudlayer tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\cloudlayer-automation`
- **cloudpress-automation** — Automate Cloudpress tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\cloudpress-automation`
- **coassemble-automation** — Automate Coassemble tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\coassemble-automation`
- **codacy-automation** — Automate Codacy tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\codacy-automation`
- **codeinterpreter-automation** — Automate Codeinterpreter tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\codeinterpreter-automation`
- **codereadr-automation** — Automate Codereadr tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\codereadr-automation`
- **Coinbase Automation** — Coinbase Automation: list and manage cryptocurrency wallets, accounts, and portfolio data via Coinbase CDP SDK
  `B:\AI-Armory\skillz\Everything-Automated\coinbase-automation`
- **coinmarketcal-automation** — Automate Coinmarketcal tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\coinmarketcal-automation`
- **coinmarketcap-automation** — Automate Coinmarketcap tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\coinmarketcap-automation`
- **coinranking-automation** — Automate Coinranking tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\coinranking-automation`
- **college-football-data-automation** — Automate College Football Data tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\college-football-data-automation`
- **competitive-ads-extractor** — Extracts and analyzes competitors' ads from ad libraries (Facebook, LinkedIn, etc.) to understand what messaging, problems, and creative approaches are working.
  `B:\AI-Armory\skillz\Everything-Automated\competitive-ads-extractor`
- **composio-automation** — Automate Composio tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\composio-automation`
- **composio-search-automation** — Automate Composio Search tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\composio-search-automation`
- **connect** — Connect Claude to any app.
  `B:\AI-Armory\skillz\Everything-Automated\connect`
- **connect-apps** — Connect Claude to external apps like Gmail, Slack, GitHub.
  `B:\AI-Armory\skillz\Everything-Automated\connect-apps`
- **connecteam-automation** — Automate Connecteam tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\connecteam-automation`
- **content-research-writer** — Assists in writing high-quality content by conducting research, adding citations, improving hooks, iterating on outlines, and providing real-time feedback on each section.
  `B:\AI-Armory\skillz\Everything-Automated\content-research-writer`
- **Contentful Automation** — Automate headless CMS operations in Contentful -- list spaces, retrieve space metadata, and update space configurations through the Composio Contentful integration.
  `B:\AI-Armory\skillz\Everything-Automated\contentful-automation`
- **contentful-graphql-automation** — Automate Contentful Graphql tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\contentful-graphql-automation`
- **control-d-automation** — Automate Control D tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\control-d-automation`
- **conversion-tools-automation** — Automate Conversion Tools tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\conversion-tools-automation`
- **convertapi-automation** — Automate Convertapi tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\convertapi-automation`
- **conveyor-automation** — Automate Conveyor tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\conveyor-automation`
- **convolo-ai-automation** — Automate Convolo AI tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\convolo-ai-automation`
- **corrently-automation** — Automate Corrently tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\corrently-automation`
- **countdown-api-automation** — Automate Countdown API tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\countdown-api-automation`
- **coupa-automation** — Automate Coupa tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\coupa-automation`
- **craftmypdf-automation** — Automate Craftmypdf tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\craftmypdf-automation`
- **crowdin-automation** — Automate Crowdin tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\crowdin-automation`
- **crustdata-automation** — Automate Crustdata tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\crustdata-automation`
- **cults-automation** — Automate Cults tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\cults-automation`
- **curated-automation** — Automate Curated tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\curated-automation`
- **currents-api-automation** — Automate Currents API tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\currents-api-automation`
- **Customer.io Automation** — Automate customer engagement workflows including broadcast triggers, message analytics, segment management, and newsletter tracking through Customer.io via Composio
  `B:\AI-Armory\skillz\Everything-Automated\customerio-automation`
- **customgpt-automation** — Automate Customgpt tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\customgpt-automation`
- **customjs-automation** — Automate Customjs tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\customjs-automation`
- **cutt-ly-automation** — Automate Cutt Ly tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\cutt-ly-automation`
- **d2lbrightspace-automation** — Automate D2lbrightspace tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\d2lbrightspace-automation`
- **dadata-ru-automation** — Automate Dadata Ru tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\dadata-ru-automation`
- **daffy-automation** — Automate Daffy tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\daffy-automation`
- **dailybot-automation** — Automate Dailybot tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\dailybot-automation`
- **datagma-automation** — Automate Datagma tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\datagma-automation`
- **datarobot-automation** — Automate Datarobot tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\datarobot-automation`
- **deadline-funnel-automation** — Automate Deadline Funnel tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\deadline-funnel-automation`
- **deel-automation** — Automate Deel tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\deel-automation`
- **deepgram-automation** — Automate Deepgram tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\deepgram-automation`
- **demio-automation** — Automate Demio tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\demio-automation`
- **design-taste-frontend** — Use when building high-agency frontend interfaces with strict design taste, calibrated color, responsive layout, and motion rules.
  `B:\AI-Armory\skillz\Everything-Automated\design-taste-frontend`  ·  _tags:_ frontend, design, ui, react
- **desktime-automation** — Automate Desktime tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\desktime-automation`
- **detrack-automation** — Automate Detrack tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\detrack-automation`
- **developer-growth-analysis** — Analyzes your recent Claude Code chat history to identify coding patterns, development gaps, and areas for improvement, curates relevant learning resources from HackerNews, and automatically sends a...
  `B:\AI-Armory\skillz\Everything-Automated\developer-growth-analysis`
- **devops-troubleshooter** — Expert DevOps troubleshooter specializing in rapid incident response, advanced debugging, and modern observability.
  `B:\AI-Armory\skillz\Everything-Automated\devops-troubleshooter`
- **dialmycalls-automation** — Automate Dialmycalls tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\dialmycalls-automation`
- **dialpad-automation** — Automate Dialpad tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\dialpad-automation`
- **dictionary-api-automation** — Automate Dictionary API tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\dictionary-api-automation`
- **diffbot-automation** — Automate Diffbot tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\diffbot-automation`
- **digicert-automation** — Automate Digicert tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\digicert-automation`
- **digital-ocean-automation** — Automate DigitalOcean tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\digital-ocean-automation`
- **discordbot-automation** — Automate Discordbot tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\discordbot-automation`
- **dnsfilter-automation** — Automate Dnsfilter tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\dnsfilter-automation`
- **dock-certs-automation** — Automate Dock Certs tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\dock-certs-automation`
- **Docker Hub Automation** — Automate Docker Hub operations -- manage organizations, repositories, teams, members, and webhooks via the Composio MCP integration.
  `B:\AI-Armory\skillz\Everything-Automated\docker-hub-automation`
- **docker_hub-automation** — Automate Docker Hub tasks via Rube MCP (Composio): repositories, images, tags, and container registry management.
  `B:\AI-Armory\skillz\Everything-Automated\docker_hub-automation`
- **docmosis-automation** — Automate Docmosis tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\docmosis-automation`
- **docnify-automation** — Automate Docnify tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\docnify-automation`
- **docsbot-ai-automation** — Automate Docsbot AI tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\docsbot-ai-automation`
- **docsumo-automation** — Automate Docsumo tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\docsumo-automation`
- **docugenerate-automation** — Automate Docugenerate tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\docugenerate-automation`
- **documenso-automation** — Automate Documenso tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\documenso-automation`
- **documint-automation** — Automate Documint tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\documint-automation`
- **docupilot-automation** — Automate Docupilot tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\docupilot-automation`
- **docupost-automation** — Automate Docupost tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\docupost-automation`
- **docuseal-automation** — Automate Docuseal tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\docuseal-automation`
- **doppler-marketing-automation-automation** — Automate Doppler Marketing Automation tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\doppler-marketing-automation-automation`
- **doppler-secretops-automation** — Automate Doppler Secretops tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\doppler-secretops-automation`
- **dotsimple-automation** — Automate Dotsimple tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\dotsimple-automation`
- **dovetail-automation** — Automate Dovetail tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\dovetail-automation`
- **dpd2-automation** — Automate Dpd2 tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\dpd2-automation`
- **draftable-automation** — Automate Draftable tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\draftable-automation`
- **dreamstudio-automation** — Automate Dreamstudio tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\dreamstudio-automation`
- **drip-jobs-automation** — Automate Drip Jobs tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\drip-jobs-automation`
- **dripcel-automation** — Automate Dripcel tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\dripcel-automation`
- **dromo-automation** — Automate Dromo tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\dromo-automation`
- **dropbox-sign-automation** — Automate Dropbox Sign tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\dropbox-sign-automation`
- **dropcontact-automation** — Automate Dropcontact tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\dropcontact-automation`
- **dungeon-fighter-online-automation** — Automate Dungeon Fighter Online tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\dungeon-fighter-online-automation`
- **Dynamics 365 Automation** — Dynamics 365 Automation: manage CRM contacts, accounts, leads, opportunities, sales orders, invoices, and cases via the Dynamics CRM Web API
  `B:\AI-Armory\skillz\Everything-Automated\dynamics365-automation`
- **echtpost-automation** — Automate Echtpost tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\echtpost-automation`
- **ElevenLabs Automation** — Automate ElevenLabs text-to-speech workflows -- generate speech from text, browse and inspect voices, check subscription limits, list models, stream audio, and retrieve history via the Composio MCP...
  `B:\AI-Armory\skillz\Everything-Automated\elevenlabs-automation`
- **elorus-automation** — Automate Elorus tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\elorus-automation`
- **emailable-automation** — Automate Emailable tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\emailable-automation`
- **emaillistverify-automation** — Automate Emaillistverify tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\emaillistverify-automation`
- **emailoctopus-automation** — Automate Emailoctopus tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\emailoctopus-automation`
- **emelia-automation** — Automate Emelia tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\emelia-automation`
- **encodian-automation** — Automate Encodian tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\encodian-automation`
- **endorsal-automation** — Automate Endorsal tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\endorsal-automation`
- **enginemailer-automation** — Automate Enginemailer tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\enginemailer-automation`
- **enigma-automation** — Automate Enigma tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\enigma-automation`
- **entelligence-automation** — Automate Entelligence tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\entelligence-automation`
- **eodhd-apis-automation** — Automate Eodhd Apis tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\eodhd-apis-automation`
- **epic-games-automation** — Automate Epic Games tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\epic-games-automation`
- **esignatures-io-automation** — Automate Esignatures IO tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\esignatures-io-automation`
- **espocrm-automation** — Automate Espocrm tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\espocrm-automation`
- **esputnik-automation** — Automate Esputnik tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\esputnik-automation`
- **etermin-automation** — Automate Etermin tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\etermin-automation`
- **evenium-automation** — Automate Evenium tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\evenium-automation`
- **Eventbrite Automation** — Automate Eventbrite event management, attendee tracking, organization discovery, and category browsing through natural language commands
  `B:\AI-Armory\skillz\Everything-Automated\eventbrite-automation`
- **eventee-automation** — Automate Eventee tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\eventee-automation`
- **eventzilla-automation** — Automate Eventzilla tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\eventzilla-automation`
- **everhour-automation** — Automate Everhour tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\everhour-automation`
- **eversign-automation** — Automate Eversign tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\eversign-automation`
- **exa-automation** — Automate Exa tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\exa-automation`
- **Excel Automation** — Excel Automation: create workbooks, manage worksheets, read/write cell data, and format spreadsheets via Microsoft Excel and Google Sheets integration
  `B:\AI-Armory\skillz\Everything-Automated\excel-automation`
- **exist-automation** — Automate Exist tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\exist-automation`
- **expofp-automation** — Automate Expofp tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\expofp-automation`
- **extracta-ai-automation** — Automate Extracta AI tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\extracta-ai-automation`
- **Facebook Automation** — Automate Facebook Page management including post creation, scheduling, video uploads, Messenger conversations, and audience engagement via Composio
  `B:\AI-Armory\skillz\Everything-Automated\facebook-automation`
- **faceup-automation** — Automate Faceup tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\faceup-automation`
- **factorial-automation** — Automate Factorial tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\factorial-automation`
- **feathery-automation** — Automate Feathery tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\feathery-automation`
- **felt-automation** — Automate Felt tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\felt-automation`
- **fibery-automation** — Automate Fibery tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\fibery-automation`
- **fidel-api-automation** — Automate Fidel API tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\fidel-api-automation`
- **files-com-automation** — Automate Files Com tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\files-com-automation`
- **fillout_forms-automation** — Automate Fillout tasks via Rube MCP (Composio): forms, submissions, workflows, and form builder.
  `B:\AI-Armory\skillz\Everything-Automated\fillout_forms-automation`
- **fillout-forms-automation** — Automate Fillout tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\fillout-forms-automation`
- **finage-automation** — Automate Finage tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\finage-automation`
- **findymail-automation** — Automate Findymail tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\findymail-automation`
- **finerworks-automation** — Automate Finerworks tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\finerworks-automation`
- **fingertip-automation** — Automate Fingertip tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\fingertip-automation`
- **finmei-automation** — Automate Finmei tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\finmei-automation`
- **fireberry-automation** — Automate Fireberry tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\fireberry-automation`
- **Firecrawl Automation** — Automate web crawling and data extraction with Firecrawl -- scrape pages, crawl sites, extract structured data, batch scrape URLs, and map website structures through the Composio Firecrawl...
  `B:\AI-Armory\skillz\Everything-Automated\firecrawl-automation`
- **fireflies-automation** — Automate Fireflies tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\fireflies-automation`
- **firmao-automation** — Automate Firmao tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\firmao-automation`
- **fitbit-automation** — Automate Fitbit tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\fitbit-automation`
- **fixer-automation** — Automate Fixer tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\fixer-automation`
- **fixer-io-automation** — Automate Fixer IO tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\fixer-io-automation`
- **flexisign-automation** — Automate Flexisign tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\flexisign-automation`
- **flowiseai-automation** — Automate Flowiseai tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\flowiseai-automation`
- **flutterwave-automation** — Automate Flutterwave tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\flutterwave-automation`
- **fluxguard-automation** — Automate Fluxguard tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\fluxguard-automation`
- **folk-automation** — Automate Folk tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\folk-automation`
- **fomo-automation** — Automate Fomo tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\fomo-automation`
- **forcemanager-automation** — Automate Forcemanager tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\forcemanager-automation`
- **formbricks-automation** — Automate Formbricks tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\formbricks-automation`
- **formcarry-automation** — Automate Formcarry tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\formcarry-automation`
- **formdesk-automation** — Automate Formdesk tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\formdesk-automation`
- **formsite-automation** — Automate Formsite tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\formsite-automation`
- **foursquare-automation** — Automate Foursquare tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\foursquare-automation`
- **fraudlabs-pro-automation** — Automate Fraudlabs Pro tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\fraudlabs-pro-automation`
- **FreshBooks Automation** — FreshBooks Automation: manage businesses, projects, time tracking, and billing in FreshBooks cloud accounting
  `B:\AI-Armory\skillz\Everything-Automated\freshbooks-automation`
- **front-automation** — Automate Front tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\front-automation`
- **fullenrich-automation** — Automate Fullenrich tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\fullenrich-automation`
- **gagelist-automation** — Automate Gagelist tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\gagelist-automation`
- **gamma-automation** — Automate Gamma tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\gamma-automation`
- **gan-ai-automation** — Automate Gan AI tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\gan-ai-automation`
- **gatherup-automation** — Automate Gatherup tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\gatherup-automation`
- **gemini-automation** — Automate Gemini tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\gemini-automation`
- **gender-api-automation** — Automate Gender API tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\gender-api-automation`
- **genderapi-io-automation** — Automate Genderapi IO tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\genderapi-io-automation`
- **genderize-automation** — Automate Genderize tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\genderize-automation`
- **geoapify-automation** — Automate Geoapify tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\geoapify-automation`
- **geocodio-automation** — Automate Geocodio tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\geocodio-automation`
- **geokeo-automation** — Automate Geokeo tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\geokeo-automation`
- **getform-automation** — Automate Getform tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\getform-automation`
- **gift-up-automation** — Automate Gift Up tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\gift-up-automation`
- **gigasheet-automation** — Automate Gigasheet tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\gigasheet-automation`
- **giphy-automation** — Automate Giphy tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\giphy-automation`
- **gist-automation** — Automate Gist tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\gist-automation`
- **givebutter-automation** — Automate Givebutter tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\givebutter-automation`
- **gladia-automation** — Automate Gladia tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\gladia-automation`
- **gleap-automation** — Automate Gleap tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\gleap-automation`
- **globalping-automation** — Automate Globalping tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\globalping-automation`
- **go-to-webinar-automation** — Automate GoToWebinar tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\go-to-webinar-automation`
- **godial-automation** — Automate Godial tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\godial-automation`
- **Gong Automation** — Automate Gong conversation intelligence -- retrieve call recordings, transcripts, detailed analytics, speaker stats, and workspace data -- using natural language through the Composio MCP integration.
  `B:\AI-Armory\skillz\Everything-Automated\gong-automation`  ·  _tags:_ conversation-intelligence
- **goodbits-automation** — Automate Goodbits tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\goodbits-automation`
- **goody-automation** — Automate Goody tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\goody-automation`
- **google_admin-automation** — Automate Google Admin tasks via Rube MCP (Composio): user management, org units, groups, and domain administration.
  `B:\AI-Armory\skillz\Everything-Automated\google_admin-automation`
- **google_classroom-automation** — Automate Google Classroom tasks via Rube MCP (Composio): course management, assignments, student rosters, and announcements.
  `B:\AI-Armory\skillz\Everything-Automated\google_classroom-automation`
- **google_maps-automation** — Automate Google Maps tasks via Rube MCP (Composio): geocoding, directions, place search, and distance calculations.
  `B:\AI-Armory\skillz\Everything-Automated\google_maps-automation`
- **google_search_console-automation** — Automate Google Search Console tasks via Rube MCP (Composio): search performance, URL inspection, sitemaps, and indexing status.
  `B:\AI-Armory\skillz\Everything-Automated\google_search_console-automation`
- **google-address-validation-automation** — Automate Google Address Validation tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\google-address-validation-automation`
- **google-admin-automation** — Automate Google Workspace Admin tasks via Rube MCP (Composio): manage users, groups, memberships, suspend accounts, create users, add aliases.
  `B:\AI-Armory\skillz\Everything-Automated\google-admin-automation`
- **google-classroom-automation** — Automate Google Classroom tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\google-classroom-automation`
- **google-cloud-vision-automation** — Automate Google Cloud Vision tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\google-cloud-vision-automation`
- **google-maps-automation** — Automate Google Maps tasks via Rube MCP (Composio): geocode addresses, search places, get directions, compute route matrices, reverse geocode, autocomplete, get place details.
  `B:\AI-Armory\skillz\Everything-Automated\google-maps-automation`
- **google-search-console-automation** — Automate Google Search Console tasks via Rube MCP (Composio): query search analytics, list sites, inspect URLs, submit sitemaps, monitor search performance.
  `B:\AI-Armory\skillz\Everything-Automated\google-search-console-automation`
- **googleads-automation** — Automate Google Ads analytics tasks via Rube MCP (Composio): list Google Ads links, run GA4 reports, check compatibility, list properties and accounts.
  `B:\AI-Armory\skillz\Everything-Automated\googleads-automation`
- **googlebigquery-automation** — Automate Google BigQuery tasks via Rube MCP (Composio): run SQL queries, explore datasets and metadata, execute MBQL queries via Metabase integration.
  `B:\AI-Armory\skillz\Everything-Automated\googlebigquery-automation`
- **googlecalendar-automation** — Automate Google Calendar tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\googlecalendar-automation`
- **googledocs-automation** — Automate Google Docs tasks via Rube MCP (Composio): create, edit, search, export, copy, and update documents.
  `B:\AI-Armory\skillz\Everything-Automated\googledocs-automation`
- **googledrive-automation** — Automate Google Drive tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\googledrive-automation`
- **googlemeet-automation** — Automate Google Meet tasks via Rube MCP (Composio): create Meet spaces, schedule video conferences via Calendar events, manage meeting access.
  `B:\AI-Armory\skillz\Everything-Automated\googlemeet-automation`
- **googlephotos-automation** — Automate Google Photos tasks via Rube MCP (Composio): upload media, manage albums, search photos, batch add items, create and update albums.
  `B:\AI-Armory\skillz\Everything-Automated\googlephotos-automation`
- **googleslides-automation** — Automate Google Slides tasks via Rube MCP (Composio): create presentations, add slides from Markdown, batch update, copy from templates, get thumbnails.
  `B:\AI-Armory\skillz\Everything-Automated\googleslides-automation`
- **googlesuper-automation** — Automate Google Super tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\googlesuper-automation`
- **googletasks-automation** — Automate Google Tasks via Rube MCP (Composio): create, list, update, delete, move, and bulk-insert tasks and task lists.
  `B:\AI-Armory\skillz\Everything-Automated\googletasks-automation`
- **Gorgias Automation** — Automate e-commerce customer support workflows in Gorgias -- manage tickets, customers, tags, and teams through natural language commands.
  `B:\AI-Armory\skillz\Everything-Automated\gorgias-automation`
- **gosquared-automation** — Automate Gosquared tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\gosquared-automation`
- **grafbase-automation** — Automate Grafbase tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\grafbase-automation`
- **graphhopper-automation** — Automate Graphhopper tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\graphhopper-automation`
- **griptape-automation** — Automate Griptape tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\griptape-automation`
- **grist-automation** — Automate Grist tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\grist-automation`
- **GroqCloud Automation** — Automate AI inference, chat completions, audio translation, and TTS voice management through GroqCloud's high-performance API via Composio
  `B:\AI-Armory\skillz\Everything-Automated\groqcloud-automation`
- **Gumroad Automation** — Automate Gumroad product management, sales tracking, license verification, and webhook subscriptions using natural language through the Composio MCP integration.
  `B:\AI-Armory\skillz\Everything-Automated\gumroad-automation`  ·  _tags:_ e-commerce
- **habitica-automation** — Automate Habitica tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\habitica-automation`
- **hackernews-automation** — Automate Hackernews tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\hackernews-automation`
- **happy-scribe-automation** — Automate Happy Scribe tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\happy-scribe-automation`
- **Harvest Automation** — Automate time tracking, project management, and invoicing workflows in Harvest -- log hours, manage projects, clients, and tasks through natural language commands.
  `B:\AI-Armory\skillz\Everything-Automated\harvest-automation`
- **hashnode-automation** — Automate Hashnode tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\hashnode-automation`
- **helcim-automation** — Automate Helcim tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\helcim-automation`
- **helloleads-automation** — Automate Helloleads tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\helloleads-automation`
- **helpwise-automation** — Automate Helpwise tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\helpwise-automation`
- **here-automation** — Automate Here tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\here-automation`
- **HeyGen Automation** — Automate AI video generation, avatar browsing, template-based video creation, and video status tracking through HeyGen's platform via Composio
  `B:\AI-Armory\skillz\Everything-Automated\heygen-automation`
- **heyreach-automation** — Automate Heyreach tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\heyreach-automation`
- **heyzine-automation** — Automate Heyzine tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\heyzine-automation`
- **highergov-automation** — Automate Highergov tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\highergov-automation`
- **highlevel-automation** — Automate Highlevel tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\highlevel-automation`
- **honeybadger-automation** — Automate Honeybadger tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\honeybadger-automation`
- **honeyhive-automation** — Automate Honeyhive tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\honeyhive-automation`
- **hookdeck-automation** — Automate Hookdeck tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\hookdeck-automation`
- **hotspotsystem-automation** — Automate Hotspotsystem tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\hotspotsystem-automation`
- **html-to-image-automation** — Automate Html To Image tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\html-to-image-automation`
- **humanitix-automation** — Automate Humanitix tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\humanitix-automation`
- **humanloop-automation** — Automate Humanloop tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\humanloop-automation`
- **Hunter Automation** — Automate Hunter.io email intelligence -- search domains for email addresses, find specific contacts, verify email deliverability, manage leads, and monitor account usage -- using natural language...
  `B:\AI-Armory\skillz\Everything-Automated\hunter-automation`  ·  _tags:_ email-intelligence
- **hypeauditor-automation** — Automate Hypeauditor tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\hypeauditor-automation`
- **hyperbrowser-automation** — Automate Hyperbrowser tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\hyperbrowser-automation`
- **hyperise-automation** — Automate Hyperise tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\hyperise-automation`
- **hystruct-automation** — Automate Hystruct tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\hystruct-automation`
- **icims-talent-cloud-automation** — Automate Icims Talent Cloud tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\icims-talent-cloud-automation`
- **icypeas-automation** — Automate Icypeas tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\icypeas-automation`
- **idea-scale-automation** — Automate Idea Scale tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\idea-scale-automation`
- **identitycheck-automation** — Automate Identitycheck tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\identitycheck-automation`
- **ignisign-automation** — Automate Ignisign tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\ignisign-automation`
- **imagekit-io-automation** — Automate Imagekit IO tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\imagekit-io-automation`
- **imgbb-automation** — Automate Imgbb tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\imgbb-automation`
- **imgix-automation** — Automate Imgix tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\imgix-automation`
- **influxdb-cloud-automation** — Automate Influxdb Cloud tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\influxdb-cloud-automation`
- **insighto-ai-automation** — Automate Insighto AI tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\insighto-ai-automation`
- **instacart-automation** — Automate Instacart tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\instacart-automation`
- **Instantly Automation** — Automate Instantly cold email outreach -- manage campaigns, sending accounts, lead lists, bulk lead imports, and campaign analytics -- using natural language through the Composio MCP integration.
  `B:\AI-Armory\skillz\Everything-Automated\instantly-automation`  ·  _tags:_ email-outreach
- **intelliprint-automation** — Automate Intelliprint tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\intelliprint-automation`
- **interzoid-automation** — Automate Interzoid tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\interzoid-automation`
- **ip2location-automation** — Automate Ip2location tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\ip2location-automation`
- **ip2location-io-automation** — Automate Ip2location IO tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\ip2location-io-automation`
- **ip2proxy-automation** — Automate Ip2proxy tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\ip2proxy-automation`
- **ip2whois-automation** — Automate Ip2whois tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\ip2whois-automation`
- **ipdata-co-automation** — Automate Ipdata co tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\ipdata-co-automation`
- **ipinfo-io-automation** — Automate Ipinfo IO tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\ipinfo-io-automation`
- **iqair-airvisual-automation** — Automate Iqair Airvisual tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\iqair-airvisual-automation`
- **jigsawstack-automation** — Automate Jigsawstack tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\jigsawstack-automation`
- **jobnimbus-automation** — Automate Jobnimbus tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\jobnimbus-automation`
- **Jotform Automation** — Automate Jotform form listing, user management, activity history, folder organization, and plan inspection through natural language commands
  `B:\AI-Armory\skillz\Everything-Automated\jotform-automation`
- **jumpcloud-automation** — Automate Jumpcloud tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\jumpcloud-automation`
- **junglescout-automation** — Automate Junglescout tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\junglescout-automation`
- **kadoa-automation** — Automate Kadoa tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\kadoa-automation`
- **kaggle-automation** — Automate Kaggle tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\kaggle-automation`
- **kaleido-automation** — Automate Kaleido tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\kaleido-automation`
- **keap-automation** — Automate Keap tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\keap-automation`
- **keen-io-automation** — Automate Keen IO tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\keen-io-automation`
- **kickbox-automation** — Automate Kickbox tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\kickbox-automation`
- **kit-automation** — Automate Kit tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\kit-automation`
- **klipfolio-automation** — Automate Klipfolio tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\klipfolio-automation`
- **ko-fi-automation** — Automate Ko Fi tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\ko-fi-automation`
- **Kommo Automation** — Automate Kommo CRM operations -- manage leads, pipelines, pipeline stages, tasks, and custom fields -- using natural language through the Composio MCP integration.
  `B:\AI-Armory\skillz\Everything-Automated\kommo-automation`  ·  _tags:_ crm
- **kontent-ai-automation** — Automate Kontent AI tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\kontent-ai-automation`
- **kraken-io-automation** — Automate Kraken IO tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\kraken-io-automation`
- **l2s-automation** — Automate L2s tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\l2s-automation`
- **labs64-netlicensing-automation** — Automate Labs64 Netlicensing tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\labs64-netlicensing-automation`
- **landbot-automation** — Automate Landbot tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\landbot-automation`
- **langbase-automation** — Automate Langbase tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\langbase-automation`
- **lastpass-automation** — Automate Lastpass tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\lastpass-automation`
- **launch_darkly-automation** — Automate LaunchDarkly tasks via Rube MCP (Composio): feature flags, environments, segments, and rollout management.
  `B:\AI-Armory\skillz\Everything-Automated\launch_darkly-automation`
- **LaunchDarkly Automation** — Automate LaunchDarkly feature flag management -- list projects and environments, create and delete trigger workflows, and track code references via the Composio MCP integration.
  `B:\AI-Armory\skillz\Everything-Automated\launch-darkly-automation`
- **leadfeeder-automation** — Automate Leadfeeder tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\leadfeeder-automation`
- **leadoku-automation** — Automate Leadoku tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\leadoku-automation`
- **leiga-automation** — Automate Leiga tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\leiga-automation`
- **Lemlist Automation** — Automate Lemlist multichannel outreach -- manage campaigns, enroll leads, add personalization variables, export campaign data, and handle unsubscribes via the Composio MCP integration.
  `B:\AI-Armory\skillz\Everything-Automated\lemlist-automation`
- **Lemon Squeezy Automation** — Automate Lemon Squeezy store management -- products, orders, subscriptions, customers, discounts, and checkout tracking -- using natural language through the Composio MCP integration.
  `B:\AI-Armory\skillz\Everything-Automated\lemon-squeezy-automation`  ·  _tags:_ e-commerce
- **lemon_squeezy-automation** — Automate Lemon Squeezy tasks via Rube MCP (Composio): products, orders, subscriptions, checkouts, and digital sales.
  `B:\AI-Armory\skillz\Everything-Automated\lemon_squeezy-automation`
- **lessonspace-automation** — Automate Lessonspace tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\lessonspace-automation`
- **Lever Automation** — Automate recruiting workflows in Lever ATS -- manage opportunities, job postings, requisitions, pipeline stages, and candidate tags through the Composio Lever integration.
  `B:\AI-Armory\skillz\Everything-Automated\lever-automation`
- **lever-sandbox-automation** — Automate Lever Sandbox tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\lever-sandbox-automation`
- **leverly-automation** — Automate Leverly tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\leverly-automation`
- **lexoffice-automation** — Automate Lexoffice tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\lexoffice-automation`
- **linguapop-automation** — Automate Linguapop tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\linguapop-automation`
- **linkhut-automation** — Automate Linkhut tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\linkhut-automation`
- **linkup-automation** — Automate Linkup tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\linkup-automation`
- **listclean-automation** — Automate Listclean tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\listclean-automation`
- **listennotes-automation** — Automate Listennotes tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\listennotes-automation`
- **livesession-automation** — Automate Livesession tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\livesession-automation`
- **lmnt-automation** — Automate Lmnt tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\lmnt-automation`
- **lodgify-automation** — Automate Lodgify tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\lodgify-automation`
- **logo-dev-automation** — Automate Logo Dev tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\logo-dev-automation`
- **loomio-automation** — Automate Loomio tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\loomio-automation`
- **loyverse-automation** — Automate Loyverse tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\loyverse-automation`
- **magnetic-automation** — Automate Magnetic tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\magnetic-automation`
- **mailbluster-automation** — Automate Mailbluster tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\mailbluster-automation`
- **mailboxlayer-automation** — Automate Mailboxlayer tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\mailboxlayer-automation`
- **mailcheck-automation** — Automate Mailcheck tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\mailcheck-automation`
- **mailcoach-automation** — Automate Mailcoach tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\mailcoach-automation`
- **MailerLite Automation** — Automate email marketing workflows including subscriber management, campaign analytics, group segmentation, and account monitoring through MailerLite via Composio
  `B:\AI-Armory\skillz\Everything-Automated\mailerlite-automation`
- **mailersend-automation** — Automate Mailersend tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\mailersend-automation`
- **mails-so-automation** — Automate Mails So tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\mails-so-automation`
- **mailsoftly-automation** — Automate Mailsoftly tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\mailsoftly-automation`
- **maintainx-automation** — Automate Maintainx tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\maintainx-automation`
- **many_chat-automation** — Automate ManyChat tasks via Rube MCP (Composio): chatbot flows, subscribers, broadcasts, and messenger automation.
  `B:\AI-Armory\skillz\Everything-Automated\many_chat-automation`
- **many-chat-automation** — Automate ManyChat tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\many-chat-automation`
- **mapbox-automation** — Automate Mapbox tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\mapbox-automation`
- **mapulus-automation** — Automate Mapulus tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\mapulus-automation`
- **mboum-automation** — Automate Mboum tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\mboum-automation`
- **melo-automation** — Automate Melo tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\melo-automation`
- **mem-automation** — Automate Mem tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\mem-automation`
- **mem0-automation** — Automate Mem0 tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\mem0-automation`
- **memberspot-automation** — Automate Memberspot tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\memberspot-automation`
- **memberstack-automation** — Automate Memberstack tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\memberstack-automation`
- **membervault-automation** — Automate Membervault tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\membervault-automation`
- **metaads-automation** — Automate Metaads tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\metaads-automation`
- **metaphor-automation** — Automate Metaphor tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\metaphor-automation`
- **mezmo-automation** — Automate Mezmo tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\mezmo-automation`
- **Microsoft Clarity Automation** — Automate user behavior analytics with Microsoft Clarity -- export heatmap data, session metrics, and engagement analytics segmented by browser, device, country, source, and more through the Composio...
  `B:\AI-Armory\skillz\Everything-Automated\microsoft-clarity-automation`
- **microsoft_clarity-automation** — Automate Microsoft Clarity tasks via Rube MCP (Composio): session recordings, heatmaps, and user behavior analytics.
  `B:\AI-Armory\skillz\Everything-Automated\microsoft_clarity-automation`
- **microsoft-tenant-automation** — Automate Microsoft Tenant tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\microsoft-tenant-automation`
- **minerstat-automation** — Automate Minerstat tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\minerstat-automation`
- **missive-automation** — Automate Missive tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\missive-automation`
- **Mistral AI Automation** — Automate Mistral AI operations -- manage files and libraries, upload documents for fine-tuning, batch processing, and OCR, track fine-tuning jobs, and build RAG pipelines via the Composio MCP...
  `B:\AI-Armory\skillz\Everything-Automated\mistral-ai-automation`
- **mistral_ai-automation** — Automate Mistral AI tasks via Rube MCP (Composio): completions, embeddings, fine-tuning, and model management.
  `B:\AI-Armory\skillz\Everything-Automated\mistral_ai-automation`
- **mocean-automation** — Automate Mocean tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\mocean-automation`
- **moco-automation** — Automate Moco tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\moco-automation`
- **modelry-automation** — Automate Modelry tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\modelry-automation`
- **moneybird-automation** — Automate Moneybird tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\moneybird-automation`
- **moonclerk-automation** — Automate Moonclerk tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\moonclerk-automation`
- **moosend-automation** — Automate Moosend tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\moosend-automation`
- **mopinion-automation** — Automate Mopinion tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\mopinion-automation`
- **more-trees-automation** — Automate More Trees tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\more-trees-automation`
- **moxie-automation** — Automate Moxie tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\moxie-automation`
- **moz-automation** — Automate Moz tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\moz-automation`
- **msg91-automation** — Automate Msg91 tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\msg91-automation`
- **mural-automation** — Automate Mural tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\mural-automation`
- **mx-technologies-automation** — Automate MX Technologies tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\mx-technologies-automation`
- **mx-toolbox-automation** — Automate Mx Toolbox tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\mx-toolbox-automation`
- **nango-automation** — Automate Nango tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\nango-automation`
- **nano-nets-automation** — Automate Nano Nets tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\nano-nets-automation`
- **nasa-automation** — Automate Nasa tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\nasa-automation`
- **nasdaq-automation** — Automate Nasdaq tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\nasdaq-automation`
- **ncscale-automation** — Automate Ncscale tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\ncscale-automation`
- **needle-automation** — Automate Needle tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\needle-automation`
- **Neon Automation** — Automate Neon serverless Postgres operations -- manage projects, branches, databases, roles, and connection URIs via the Composio MCP integration.
  `B:\AI-Armory\skillz\Everything-Automated\neon-automation`
- **NetSuite Automation** — NetSuite Automation: manage customers, sales orders, invoices, inventory, and records via Oracle NetSuite ERP with SuiteQL queries
  `B:\AI-Armory\skillz\Everything-Automated\netsuite-automation`
- **neuronwriter-automation** — Automate Neuronwriter tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\neuronwriter-automation`
- **neutrino-automation** — Automate Neutrino tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\neutrino-automation`
- **neverbounce-automation** — Automate Neverbounce tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\neverbounce-automation`
- **New Relic Automation** — Automate New Relic observability workflows -- manage alert policies, notification channels, alert conditions, and monitor applications and browser apps via the Composio MCP integration.
  `B:\AI-Armory\skillz\Everything-Automated\new-relic-automation`
- **new_relic-automation** — Automate New Relic tasks via Rube MCP (Composio): APM, alerts, dashboards, NRQL queries, and infrastructure monitoring.
  `B:\AI-Armory\skillz\Everything-Automated\new_relic-automation`
- **news-api-automation** — Automate News API tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\news-api-automation`
- **nextdns-automation** — Automate Nextdns tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\nextdns-automation`
- **ngrok-automation** — Automate Ngrok tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\ngrok-automation`
- **ninox-automation** — Automate Ninox tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\ninox-automation`
- **nocrm-io-automation** — Automate Nocrm IO tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\nocrm-io-automation`
- **npm-automation** — Automate NPM tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\npm-automation`
- **ocr-web-service-automation** — Automate OCR Web Service tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\ocr-web-service-automation`
- **ocrspace-automation** — Automate Ocrspace tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\ocrspace-automation`
- **Omnisend Automation** — Automate ecommerce marketing workflows including contact management, bulk operations, and subscriber segmentation through Omnisend via Composio
  `B:\AI-Armory\skillz\Everything-Automated\omnisend-automation`
- **oncehub-automation** — Automate Oncehub tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\oncehub-automation`
- **onedesk-automation** — Automate Onedesk tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\onedesk-automation`
- **onepage-automation** — Automate Onepage tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\onepage-automation`
- **onesignal_rest_api-automation** — Automate OneSignal tasks via Rube MCP (Composio): push notifications, segments, templates, and messaging.
  `B:\AI-Armory\skillz\Everything-Automated\onesignal_rest_api-automation`
- **onesignal-rest-api-automation** — Automate OneSignal tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\onesignal-rest-api-automation`
- **onesignal-user-auth-automation** — Automate Onesignal User Auth tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\onesignal-user-auth-automation`
- **open-sea-automation** — Automate Open Sea tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\open-sea-automation`
- **OpenAI Automation** — Automate OpenAI API operations -- generate responses with multimodal and structured output support, create embeddings, generate images, and list models via the Composio MCP integration.
  `B:\AI-Armory\skillz\Everything-Automated\openai-automation`
- **opencage-automation** — Automate Opencage tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\opencage-automation`
- **opengraph-io-automation** — Automate Opengraph IO tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\opengraph-io-automation`
- **openperplex-automation** — Automate Openperplex tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\openperplex-automation`
- **openrouter-automation** — Automate Openrouter tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\openrouter-automation`
- **openweather-api-automation** — Automate Openweather API tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\openweather-api-automation`
- **optimoroute-automation** — Automate Optimoroute tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\optimoroute-automation`
- **owl-protocol-automation** — Automate Owl Protocol tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\owl-protocol-automation`
- **page-x-automation** — Automate Page X tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\page-x-automation`
- **PandaDoc Automation** — Automate document workflows with PandaDoc -- create documents from files, manage contacts, organize folders, set up webhooks, create templates, and track document status through the Composio PandaDoc...
  `B:\AI-Armory\skillz\Everything-Automated\pandadoc-automation`
- **paradym-automation** — Automate Paradym tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\paradym-automation`
- **parallel-automation** — Automate Parallel tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\parallel-automation`
- **parma-automation** — Automate Parma tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\parma-automation`
- **parsehub-automation** — Automate Parsehub tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\parsehub-automation`
- **parsera-automation** — Automate Parsera tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\parsera-automation`
- **parseur-automation** — Automate Parseur tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\parseur-automation`
- **passcreator-automation** — Automate Passcreator tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\passcreator-automation`
- **passslot-automation** — Automate Passslot tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\passslot-automation`
- **payhip-automation** — Automate Payhip tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\payhip-automation`
- **pdf-api-io-automation** — Automate PDF API IO tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\pdf-api-io-automation`
- **pdf-co-automation** — Automate PDF co tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\pdf-co-automation`
- **pdf4me-automation** — Automate Pdf4me tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\pdf4me-automation`
- **pdfless-automation** — Automate Pdfless tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\pdfless-automation`
- **pdfmonkey-automation** — Automate Pdfmonkey tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\pdfmonkey-automation`
- **peopledatalabs-automation** — Automate Peopledatalabs tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\peopledatalabs-automation`
- **perigon-automation** — Automate Perigon tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\perigon-automation`
- **perplexityai-automation** — Automate Perplexityai tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\perplexityai-automation`
- **persistiq-automation** — Automate Persistiq tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\persistiq-automation`
- **pexels-automation** — Automate Pexels tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\pexels-automation`
- **PhantomBuster Automation** — Automate lead generation, web scraping, and social media data extraction workflows through PhantomBuster's cloud platform via Composio
  `B:\AI-Armory\skillz\Everything-Automated\phantombuster-automation`
- **piggy-automation** — Automate Piggy tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\piggy-automation`
- **piloterr-automation** — Automate Piloterr tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\piloterr-automation`
- **pilvio-automation** — Automate Pilvio tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\pilvio-automation`
- **pingdom-automation** — Automate Pingdom tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\pingdom-automation`
- **pipeline-crm-automation** — Automate Pipeline CRM tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\pipeline-crm-automation`
- **placekey-automation** — Automate Placekey tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\placekey-automation`
- **placid-automation** — Automate Placid tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\placid-automation`
- **plain-automation** — Automate Plain tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\plain-automation`
- **plasmic-automation** — Automate Plasmic tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\plasmic-automation`
- **platerecognizer-automation** — Automate Platerecognizer tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\platerecognizer-automation`
- **plisio-automation** — Automate Plisio tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\plisio-automation`
- **polygon-automation** — Automate Polygon tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\polygon-automation`
- **polygon-io-automation** — Automate Polygon IO tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\polygon-io-automation`
- **poptin-automation** — Automate Poptin tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\poptin-automation`
- **postgrid-automation** — Automate Postgrid tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\postgrid-automation`
- **postgrid-verify-automation** — Automate Postgrid Verify tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\postgrid-verify-automation`
- **precoro-automation** — Automate Precoro tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\precoro-automation`
- **prerender-automation** — Automate Prerender tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\prerender-automation`
- **printautopilot-automation** — Automate Printautopilot tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\printautopilot-automation`
- **prisma-automation** — Automate Prisma tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\prisma-automation`
- **Prismic Automation** — Automate headless CMS operations in Prismic -- query documents, search content, retrieve custom types, and manage repository refs through the Composio Prismic integration.
  `B:\AI-Armory\skillz\Everything-Automated\prismic-automation`
- **process-street-automation** — Automate Process Street tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\process-street-automation`
- **procfu-automation** — Automate Procfu tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\procfu-automation`
- **Productboard Automation** — Automate product management workflows in Productboard -- manage features, notes, objectives, components, and releases through natural language commands.
  `B:\AI-Armory\skillz\Everything-Automated\productboard-automation`
- **productlane-automation** — Automate Productlane tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\productlane-automation`
- **project-bubble-automation** — Automate Project Bubble tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\project-bubble-automation`
- **proofly-automation** — Automate Proofly tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\proofly-automation`
- **proxiedmail-automation** — Automate Proxiedmail tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\proxiedmail-automation`
- **pushbullet-automation** — Automate Pushbullet tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\pushbullet-automation`
- **pushover-automation** — Automate Pushover tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\pushover-automation`
- **quaderno-automation** — Automate Quaderno tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\quaderno-automation`
- **qualaroo-automation** — Automate Qualaroo tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\qualaroo-automation`
- **QuickBooks Automation** — QuickBooks Automation: manage invoices, customers, accounts, and payments in QuickBooks Online for streamlined bookkeeping
  `B:\AI-Armory\skillz\Everything-Automated\quickbooks-automation`
- **radar-automation** — Automate Radar tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\radar-automation`
- **rafflys-automation** — Automate Rafflys tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\rafflys-automation`
- **ragic-automation** — Automate Ragic tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\ragic-automation`
- **raisely-automation** — Automate Raisely tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\raisely-automation`
- **Ramp Automation** — Ramp Automation: manage corporate card transactions, reimbursements, users, and expense tracking via the Ramp platform
  `B:\AI-Armory\skillz\Everything-Automated\ramp-automation`
- **ravenseotools-automation** — Automate Ravenseotools tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\ravenseotools-automation`
- **re-amaze-automation** — Automate Re Amaze tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\re-amaze-automation`
- **realphonevalidation-automation** — Automate Realphonevalidation tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\realphonevalidation-automation`
- **recallai-automation** — Automate Recallai tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\recallai-automation`
- **recruitee-automation** — Automate Recruitee tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\recruitee-automation`
- **refiner-automation** — Automate Refiner tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\refiner-automation`
- **remarkety-automation** — Automate Remarkety tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\remarkety-automation`
- **remote-retrieval-automation** — Automate Remote Retrieval tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\remote-retrieval-automation`
- **remove-bg-automation** — Automate Remove Bg tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\remove-bg-automation`
- **renderform-automation** — Automate Renderform tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\renderform-automation`
- **repairshopr-automation** — Automate Repairshopr tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\repairshopr-automation`
- **Replicate Automation** — Automate Replicate AI model operations -- run predictions, upload files, inspect model schemas, list versions, and manage prediction history via the Composio MCP integration.
  `B:\AI-Armory\skillz\Everything-Automated\replicate-automation`
- **reply-automation** — Automate Reply tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\reply-automation`
- **reply-io-automation** — Automate Reply IO tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\reply-io-automation`
- **resend-automation** — Automate Resend tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\resend-automation`
- **respond-io-automation** — Automate Respond IO tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\respond-io-automation`
- **retailed-automation** — Automate Retailed tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\retailed-automation`
- **retellai-automation** — Automate Retellai tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\retellai-automation`
- **retently-automation** — Automate Retently tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\retently-automation`
- **rev-ai-automation** — Automate Rev AI tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\rev-ai-automation`
- **revolt-automation** — Automate Revolt tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\revolt-automation`
- **ring_central-automation** — Automate RingCentral tasks via Rube MCP (Composio): calls, messages, meetings, and unified communications.
  `B:\AI-Armory\skillz\Everything-Automated\ring_central-automation`
- **RingCentral Automation** — RingCentral automation via Rube MCP -- toolkit not currently available in Composio; no RING_CENTRAL_ tools found
  `B:\AI-Armory\skillz\Everything-Automated\ring-central-automation`
- **rippling-automation** — Automate Rippling tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\rippling-automation`
- **ritekit-automation** — Automate Ritekit tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\ritekit-automation`
- **rkvst-automation** — Automate Rkvst tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\rkvst-automation`
- **rocketlane-automation** — Automate Rocketlane tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\rocketlane-automation`
- **rootly-automation** — Automate Rootly tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\rootly-automation`
- **rosette-text-analytics-automation** — Automate Rosette Text Analytics tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\rosette-text-analytics-automation`
- **route4me-automation** — Automate Route4me tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\route4me-automation`
- **safetyculture-automation** — Automate Safetyculture tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\safetyculture-automation`
- **sage-automation** — Automate Sage tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\sage-automation`
- **salesforce-marketing-cloud-automation** — Automate Salesforce Marketing Cloud tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\salesforce-marketing-cloud-automation`
- **salesforce-service-cloud-automation** — Automate Salesforce Service Cloud tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\salesforce-service-cloud-automation`
- **salesmate-automation** — Automate Salesmate tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\salesmate-automation`
- **sap-successfactors-automation** — Automate SAP SuccessFactors tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\sap-successfactors-automation`
- **satismeter-automation** — Automate Satismeter tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\satismeter-automation`
- **scrape-do-automation** — Automate Scrape Do tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\scrape-do-automation`
- **scrapegraph-ai-automation** — Automate Scrapegraph AI tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\scrapegraph-ai-automation`
- **scrapfly-automation** — Automate Scrapfly tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\scrapfly-automation`
- **scrapingant-automation** — Automate Scrapingant tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\scrapingant-automation`
- **scrapingbee-automation** — Automate Scrapingbee tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\scrapingbee-automation`
- **screenshot-fyi-automation** — Automate Screenshot Fyi tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\screenshot-fyi-automation`
- **screenshotone-automation** — Automate Screenshotone tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\screenshotone-automation`
- **seat-geek-automation** — Automate Seat Geek tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\seat-geek-automation`
- **securitytrails-automation** — Automate Securitytrails tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\securitytrails-automation`
- **segmetrics-automation** — Automate Segmetrics tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\segmetrics-automation`
- **seismic-automation** — Automate Seismic tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\seismic-automation`
- **semanticscholar-automation** — Automate Semanticscholar tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\semanticscholar-automation`
- **SEMrush Automation** — Automate SEO analysis with SEMrush -- research keywords, analyze domain organic rankings, audit backlinks, assess keyword difficulty, and discover related terms through the Composio SEMrush...
  `B:\AI-Armory\skillz\Everything-Automated\semrush-automation`
- **sendbird-ai-chabot-automation** — Automate Sendbird AI Chabot tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\sendbird-ai-chabot-automation`
- **sendbird-automation** — Automate Sendbird tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\sendbird-automation`
- **sendfox-automation** — Automate Sendfox tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\sendfox-automation`
- **sendlane-automation** — Automate Sendlane tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\sendlane-automation`
- **sendloop-automation** — Automate Sendloop tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\sendloop-automation`
- **sendspark-automation** — Automate Sendspark tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\sendspark-automation`
- **sensibo-automation** — Automate Sensibo tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\sensibo-automation`
- **seqera-automation** — Automate Seqera tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\seqera-automation`
- **serpapi-automation** — Automate Serpapi tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\serpapi-automation`
- **serpdog-automation** — Automate Serpdog tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\serpdog-automation`
- **serply-automation** — Automate Serply tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\serply-automation`
- **servicem8-automation** — Automate Servicem8 tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\servicem8-automation`
- **sevdesk-automation** — Automate Sevdesk tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\sevdesk-automation`
- **share_point-automation** — Automate SharePoint tasks via Rube MCP (Composio): document libraries, sites, lists, and content management.
  `B:\AI-Armory\skillz\Everything-Automated\share_point-automation`
- **SharePoint Automation** — SharePoint Automation: manage sites, lists, documents, folders, pages, and search content across SharePoint and OneDrive
  `B:\AI-Armory\skillz\Everything-Automated\share-point-automation`
- **shipengine-automation** — Automate Shipengine tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\shipengine-automation`
- **short-io-automation** — Automate Short IO tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\short-io-automation`
- **short-menu-automation** — Automate Short Menu tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\short-menu-automation`
- **Shortcut Automation** — Automate project management workflows in Shortcut -- create stories, manage tasks, track epics, and organize workflows through natural language commands.
  `B:\AI-Armory\skillz\Everything-Automated\shortcut-automation`
- **shorten-rest-automation** — Automate Shorten Rest tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\shorten-rest-automation`
- **shortpixel-automation** — Automate Shortpixel tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\shortpixel-automation`
- **shotstack-automation** — Automate Shotstack tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\shotstack-automation`
- **sidetracker-automation** — Automate Sidetracker tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\sidetracker-automation`
- **signaturely-automation** — Automate Signaturely tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\signaturely-automation`
- **signpath-automation** — Automate Signpath tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\signpath-automation`
- **signwell-automation** — Automate Signwell tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\signwell-automation`
- **similarweb_digitalrank_api-automation** — Automate SimilarWeb tasks via Rube MCP (Composio): website traffic, rankings, and digital market intelligence.
  `B:\AI-Armory\skillz\Everything-Automated\similarweb_digitalrank_api-automation`
- **similarweb-digitalrank-api-automation** — Automate SimilarWeb tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\similarweb-digitalrank-api-automation`
- **simla-com-automation** — Automate Simla Com tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\simla-com-automation`
- **simple-analytics-automation** — Automate Simple Analytics tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\simple-analytics-automation`
- **simplesat-automation** — Automate Simplesat tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\simplesat-automation`
- **sitespeakai-automation** — Automate Sitespeakai tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\sitespeakai-automation`
- **skyfire-automation** — Automate Skyfire tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\skyfire-automation`
- **slackbot-automation** — Automate Slackbot tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\slackbot-automation`
- **smartproxy-automation** — Automate Smartproxy tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\smartproxy-automation`
- **smartrecruiters-automation** — Automate Smartrecruiters tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\smartrecruiters-automation`
- **sms-alert-automation** — Automate SMS Alert tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\sms-alert-automation`
- **smtp2go-automation** — Automate Smtp2go tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\smtp2go-automation`
- **smugmug-automation** — Automate Smugmug tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\smugmug-automation`
- **Snowflake Automation** — Automate Snowflake data warehouse operations -- list databases, schemas, and tables, execute SQL statements, and manage data workflows via the Composio MCP integration.
  `B:\AI-Armory\skillz\Everything-Automated\snowflake-automation`
- **sourcegraph-automation** — Automate Sourcegraph tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\sourcegraph-automation`
- **splitwise-automation** — Automate Splitwise tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\splitwise-automation`
- **spoki-automation** — Automate Spoki tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\spoki-automation`
- **spondyr-automation** — Automate Spondyr tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\spondyr-automation`
- **Spotify Automation** — Automate Spotify workflows including playlist management, music search, playback control, and user profile access via Composio
  `B:\AI-Armory\skillz\Everything-Automated\spotify-automation`
- **spotlightr-automation** — Automate Spotlightr tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\spotlightr-automation`
- **sslmate-cert-spotter-api-automation** — Automate Sslmate Cert Spotter API tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\sslmate-cert-spotter-api-automation`
- **stack-exchange-automation** — Automate Stack Exchange tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\stack-exchange-automation`
- **stannp-automation** — Automate Stannp tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\stannp-automation`
- **starton-automation** — Automate Starton tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\starton-automation`
- **statuscake-automation** — Automate Statuscake tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\statuscake-automation`
- **storeganise-automation** — Automate Storeganise tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\storeganise-automation`
- **storerocket-automation** — Automate Storerocket tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\storerocket-automation`
- **stormglass-io-automation** — Automate Stormglass IO tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\stormglass-io-automation`
- **strava-automation** — Automate Strava tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\strava-automation`
- **streamtime-automation** — Automate Streamtime tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\streamtime-automation`
- **supadata-automation** — Automate Supadata tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\supadata-automation`
- **superchat-automation** — Automate Superchat tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\superchat-automation`
- **supportbee-automation** — Automate Supportbee tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\supportbee-automation`
- **supportivekoala-automation** — Automate Supportivekoala tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\supportivekoala-automation`
- **survey_monkey-automation** — Automate SurveyMonkey tasks via Rube MCP (Composio): surveys, responses, collectors, and survey analytics.
  `B:\AI-Armory\skillz\Everything-Automated\survey_monkey-automation`
- **SurveyMonkey Automation** — Automate SurveyMonkey survey creation, response collection, collector management, and survey discovery through natural language commands
  `B:\AI-Armory\skillz\Everything-Automated\survey-monkey-automation`
- **svix-automation** — Automate Svix tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\svix-automation`
- **sympla-automation** — Automate Sympla tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\sympla-automation`
- **synthflow-ai-automation** — Automate Synthflow AI tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\synthflow-ai-automation`
- **taggun-automation** — Automate Taggun tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\taggun-automation`
- **talenthr-automation** — Automate Talenthr tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\talenthr-automation`
- **tally-automation** — Automate Tally tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\tally-automation`
- **tapfiliate-automation** — Automate Tapfiliate tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\tapfiliate-automation`
- **tapform-automation** — Automate Tapform tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\tapform-automation`
- **tavily-automation** — Automate Tavily tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\tavily-automation`
- **taxjar-automation** — Automate Taxjar tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\taxjar-automation`
- **teamcamp-automation** — Automate Teamcamp tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\teamcamp-automation`
- **telnyx-automation** — Automate Telnyx tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\telnyx-automation`
- **teltel-automation** — Automate Teltel tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\teltel-automation`
- **templated-automation** — Automate Templated tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\templated-automation`
- **test-app-automation** — Automate Test App tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\test-app-automation`
- **text-to-pdf-automation** — Automate Text To PDF tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\text-to-pdf-automation`
- **textcortex-automation** — Automate Textcortex tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\textcortex-automation`
- **textit-automation** — Automate Textit tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\textit-automation`
- **textrazor-automation** — Automate Textrazor tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\textrazor-automation`
- **thanks-io-automation** — Automate Thanks IO tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\thanks-io-automation`
- **the-odds-api-automation** — Automate The Odds API tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\the-odds-api-automation`
- **ticketmaster-automation** — Automate Ticketmaster tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\ticketmaster-automation`
- **ticktick-automation** — Automate Ticktick tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\ticktick-automation`
- **timecamp-automation** — Automate Timecamp tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\timecamp-automation`
- **timekit-automation** — Automate Timekit tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\timekit-automation`
- **timelinesai-automation** — Automate Timelinesai tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\timelinesai-automation`
- **timelink-automation** — Automate Timelink tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\timelink-automation`
- **timely-automation** — Automate Timely tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\timely-automation`
- **tinyurl-automation** — Automate Tinyurl tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\tinyurl-automation`
- **tisane-automation** — Automate Tisane tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\tisane-automation`
- **Toggl Automation** — Automate time tracking workflows in Toggl Track -- create time entries, manage projects, clients, tags, and workspaces through natural language commands.
  `B:\AI-Armory\skillz\Everything-Automated\toggl-automation`
- **token-metrics-automation** — Automate Token Metrics tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\token-metrics-automation`
- **tomba-automation** — Automate Tomba tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\tomba-automation`
- **tomtom-automation** — Automate Tomtom tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\tomtom-automation`
- **toneden-automation** — Automate Toneden tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\toneden-automation`
- **tpscheck-automation** — Automate Tpscheck tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\tpscheck-automation`
- **triggercmd-automation** — Automate Triggercmd tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\triggercmd-automation`
- **tripadvisor-content-api-automation** — Automate TripAdvisor tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\tripadvisor-content-api-automation`
- **turbot-pipes-automation** — Automate Turbot Pipes tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\turbot-pipes-automation`
- **turso-automation** — Automate Turso tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\turso-automation`
- **twelve-data-automation** — Automate Twelve Data tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\twelve-data-automation`
- **twitch-automation** — Automate Twitch tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\twitch-automation`
- **twocaptcha-automation** — Automate Twocaptcha tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\twocaptcha-automation`
- **typefully-automation** — Automate Typefully tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\typefully-automation`
- **typless-automation** — Automate Typless tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\typless-automation`
- **u301-automation** — Automate U301 tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\u301-automation`
- **unione-automation** — Automate Unione tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\unione-automation`
- **updown-io-automation** — Automate Updown IO tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\updown-io-automation`
- **Uploadcare Automation** — Automate Uploadcare file management including listing, storing, inspecting, downloading, and organizing file groups through natural language commands
  `B:\AI-Armory\skillz\Everything-Automated\uploadcare-automation`
- **uptimerobot-automation** — Automate Uptimerobot tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\uptimerobot-automation`
- **userlist-automation** — Automate Userlist tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\userlist-automation`
- **v0-automation** — Automate V0 tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\v0-automation`
- **venly-automation** — Automate Venly tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\venly-automation`
- **veo-automation** — Automate Veo tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\veo-automation`
- **verifiedemail-automation** — Automate Verifiedemail tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\verifiedemail-automation`
- **veriphone-automation** — Automate Veriphone tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\veriphone-automation`
- **vero-automation** — Automate Vero tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\vero-automation`
- **vestaboard-automation** — Automate Vestaboard tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\vestaboard-automation`
- **virustotal-automation** — Automate Virustotal tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\virustotal-automation`
- **visme-automation** — Automate Visme tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\visme-automation`
- **waboxapp-automation** — Automate Waboxapp tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\waboxapp-automation`
- **wachete-automation** — Automate Wachete tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\wachete-automation`
- **waiverfile-automation** — Automate Waiverfile tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\waiverfile-automation`
- **wakatime-automation** — Automate Wakatime tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\wakatime-automation`
- **wati-automation** — Automate Wati tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\wati-automation`
- **Wave Accounting Automation** — Wave Accounting toolkit is not currently available as a native integration.
  `B:\AI-Armory\skillz\Everything-Automated\wave-accounting-automation`  ·  _tags:_ accounting
- **wave_accounting-automation** — Automate Wave Accounting tasks via Rube MCP (Composio): invoices, customers, payments, and small business accounting.
  `B:\AI-Armory\skillz\Everything-Automated\wave_accounting-automation`
- **weathermap-automation** — Automate Weathermap tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\weathermap-automation`
- **Webex Automation** — Automate Cisco Webex messaging, rooms, teams, webhooks, and people management through natural language commands
  `B:\AI-Armory\skillz\Everything-Automated\webex-automation`
- **webscraping-ai-automation** — Automate Webscraping AI tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\webscraping-ai-automation`
- **webvizio-automation** — Automate Webvizio tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\webvizio-automation`
- **whautomate-automation** — Automate Whautomate tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\whautomate-automation`
- **winston-ai-automation** — Automate Winston AI tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\winston-ai-automation`
- **wit-ai-automation** — Automate Wit AI tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\wit-ai-automation`
- **wiz-automation** — Automate Wiz tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\wiz-automation`
- **wolfram-alpha-api-automation** — Automate Wolfram Alpha API tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\wolfram-alpha-api-automation`
- **woodpecker-co-automation** — Automate Woodpecker co tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\woodpecker-co-automation`
- **workable-automation** — Automate Workable tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\workable-automation`
- **Workday Automation** — Automate HR operations in Workday -- manage workers, time off requests, absence balances, and employee data through natural language commands.
  `B:\AI-Armory\skillz\Everything-Automated\workday-automation`
- **workiom-automation** — Automate Workiom tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\workiom-automation`
- **worksnaps-automation** — Automate Worksnaps tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\worksnaps-automation`
- **writer-automation** — Automate Writer tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\writer-automation`
- **Xero Automation** — Xero Automation: manage invoices, contacts, payments, bank transactions, and accounts in Xero for cloud-based bookkeeping
  `B:\AI-Armory\skillz\Everything-Automated\xero-automation`
- **y-gy-automation** — Automate Y Gy tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\y-gy-automation`
- **yandex-automation** — Automate Yandex tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\yandex-automation`
- **yelp-automation** — Automate Yelp tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\yelp-automation`
- **ynab-automation** — Automate Ynab tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\ynab-automation`
- **yousearch-automation** — Automate Yousearch tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\yousearch-automation`
- **zenrows-automation** — Automate Zenrows tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\zenrows-automation`
- **zenserp-automation** — Automate Zenserp tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\zenserp-automation`
- **zeplin-automation** — Automate Zeplin tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\zeplin-automation`
- **zerobounce-automation** — Automate Zerobounce tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\zerobounce-automation`
- **Zoho Books Automation** — Automate Zoho Books accounting workflows including invoice creation, bill management, contact lookup, payment tracking, and multi-organization support through natural language commands
  `B:\AI-Armory\skillz\Everything-Automated\zoho-books-automation`
- **Zoho Desk Automation** — Zoho Desk automation via Rube MCP -- toolkit not currently available in Composio; no ZOHO_DESK_ tools found
  `B:\AI-Armory\skillz\Everything-Automated\zoho-desk-automation`
- **zoho_bigin-automation** — Automate Zoho Bigin tasks via Rube MCP (Composio): pipelines, contacts, companies, products, and small business CRM.
  `B:\AI-Armory\skillz\Everything-Automated\zoho_bigin-automation`
- **zoho_books-automation** — Automate Zoho Books tasks via Rube MCP (Composio): invoices, expenses, contacts, payments, and accounting.
  `B:\AI-Armory\skillz\Everything-Automated\zoho_books-automation`
- **zoho_desk-automation** — Automate Zoho Desk tasks via Rube MCP (Composio): tickets, contacts, agents, departments, and help desk operations.
  `B:\AI-Armory\skillz\Everything-Automated\zoho_desk-automation`
- **zoho_inventory-automation** — Automate Zoho Inventory tasks via Rube MCP (Composio): items, orders, warehouses, shipments, and stock management.
  `B:\AI-Armory\skillz\Everything-Automated\zoho_inventory-automation`
- **zoho_invoice-automation** — Automate Zoho Invoice tasks via Rube MCP (Composio): invoices, estimates, expenses, clients, and payment tracking.
  `B:\AI-Armory\skillz\Everything-Automated\zoho_invoice-automation`
- **zoho_mail-automation** — Automate Zoho Mail tasks via Rube MCP (Composio): email sending, folders, labels, and mailbox management.
  `B:\AI-Armory\skillz\Everything-Automated\zoho_mail-automation`
- **zoho-automation** — Automate Zoho tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\zoho-automation`
- **zoho-bigin-automation** — Automate Zoho Bigin tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\zoho-bigin-automation`
- **zoho-inventory-automation** — Automate Zoho Inventory tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\zoho-inventory-automation`
- **zoho-invoice-automation** — Automate Zoho Invoice tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\zoho-invoice-automation`
- **zoho-mail-automation** — Automate Zoho Mail tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\zoho-mail-automation`
- **zoominfo-automation** — Automate Zoominfo tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\zoominfo-automation`
- **zylvie-automation** — Automate Zylvie tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\zylvie-automation`
- **zyte-api-automation** — Automate Zyte API tasks via Rube MCP (Composio).
  `B:\AI-Armory\skillz\Everything-Automated\zyte-api-automation`

</details>

<details><summary><b>ECC</b> (231 skills)</summary>

- **connections-optimizer** — Reorganize the user's X and LinkedIn network with review-first pruning, add/follow recommendations, and channel-specific warm outreach drafted in the user's real voice.
  `B:\AI-Armory\skillz\ECC\connections-optimizer`
- **content-engine** — Create platform-native content systems for X, LinkedIn, TikTok, YouTube, newsletters, and repurposed multi-platform campaigns.
  `B:\AI-Armory\skillz\ECC\content-engine`
- **content-hash-cache-pattern** — Cache expensive file processing results using SHA-256 content hashes — path-independent, auto-invalidating, with service layer separation.
  `B:\AI-Armory\skillz\ECC\content-hash-cache-pattern`
- **context-budget** — Audits Claude Code context window consumption across agents, skills, MCP servers, and rules.
  `B:\AI-Armory\skillz\ECC\context-budget`
- **continuous-agent-loop** — Patterns for continuous autonomous agent loops with quality gates, evals, and recovery controls.
  `B:\AI-Armory\skillz\ECC\continuous-agent-loop`
- **continuous-learning** — [DEPRECATED - use continuous-learning-v2] Legacy v1 stop-hook skill extractor. v2 is a strict superset with instinct-based, project-scoped, hook-reliable learning.
  `B:\AI-Armory\skillz\ECC\continuous-learning`
- **continuous-learning-v2** — Instinct-based learning system that observes sessions via hooks, creates atomic instincts with confidence scoring, and evolves them into skills/commands/agents. v2.1 adds project-scoped instincts to...
  `B:\AI-Armory\skillz\ECC\continuous-learning-v2`
- **cost-aware-llm-pipeline** — Cost optimization patterns for LLM API usage — model routing by task complexity, budget tracking, retry logic, and prompt caching.
  `B:\AI-Armory\skillz\ECC\cost-aware-llm-pipeline`
- **cost-tracking** — Track and report Claude Code token usage, spending, and budgets from the local ECC cost-tracker metrics log.
  `B:\AI-Armory\skillz\ECC\cost-tracking`
- **council** — Convene a four-voice council for ambiguous decisions, tradeoffs, and go/no-go calls.
  `B:\AI-Armory\skillz\ECC\council`
- **cpp-coding-standards** — C++ coding standards based on the C++ Core Guidelines (isocpp.github.io).
  `B:\AI-Armory\skillz\ECC\cpp-coding-standards`
- **cpp-testing** — Use only when writing/updating/fixing C++ tests, configuring GoogleTest/CTest, diagnosing failing or flaky tests, or adding coverage/sanitizers.
  `B:\AI-Armory\skillz\ECC\cpp-testing`
- **crosspost** — Multi-platform content distribution across X, LinkedIn, Threads, and Bluesky.
  `B:\AI-Armory\skillz\ECC\crosspost`
- **csharp-testing** — C# and .NET testing patterns with xUnit, FluentAssertions, mocking, integration tests, and test organization best practices.
  `B:\AI-Armory\skillz\ECC\csharp-testing`
- **customer-billing-ops** — Operate customer billing workflows such as subscriptions, refunds, churn triage, billing-portal recovery, and plan analysis using connected billing tools like Stripe.
  `B:\AI-Armory\skillz\ECC\customer-billing-ops`
- **customs-trade-compliance** — Codified expertise for customs documentation, tariff classification, duty optimization, restricted party screening, and regulatory compliance across multiple jurisdictions.
  `B:\AI-Armory\skillz\ECC\customs-trade-compliance`
- **dart-flutter-patterns** — Production-ready Dart and Flutter patterns covering null safety, immutable state, async composition, widget architecture, popular state management frameworks (BLoC, Riverpod, Provider), GoRouter...
  `B:\AI-Armory\skillz\ECC\dart-flutter-patterns`
- **dashboard-builder** — Build monitoring dashboards that answer real operator questions for Grafana, SigNoz, and similar platforms.
  `B:\AI-Armory\skillz\ECC\dashboard-builder`
- **data-scraper-agent** — Build a fully automated AI-powered data collection agent for any public source — job boards, prices, news, GitHub, sports, anything.
  `B:\AI-Armory\skillz\ECC\data-scraper-agent`
- **data-throughput-accelerator** — Use when large data ingestion, backfill, export, ETL, warehouse loading, manifest catch-up, or table synchronization needs to become much faster while preserving data correctness.
  `B:\AI-Armory\skillz\ECC\data-throughput-accelerator`
- **database-migrations** — Database migration best practices for schema changes, data migrations, rollbacks, and zero-downtime deployments across PostgreSQL, MySQL, and common ORMs (Prisma, Drizzle, Kysely, Django, TypeORM...
  `B:\AI-Armory\skillz\ECC\database-migrations`
- **deep-research** — Multi-source deep research using firecrawl and exa MCPs.
  `B:\AI-Armory\skillz\ECC\deep-research`
- **defi-amm-security** — Security checklist for Solidity AMM contracts, liquidity pools, and swap flows.
  `B:\AI-Armory\skillz\ECC\defi-amm-security`
- **delivery-gate** — Stop hook that blocks Claude from finishing until quality checks pass.
  `B:\AI-Armory\skillz\ECC\delivery-gate`
- **deployment-patterns** — Deployment workflows, CI/CD pipeline patterns, Docker containerization, health checks, rollback strategies, and production readiness checklists for web applications.
  `B:\AI-Armory\skillz\ECC\deployment-patterns`
- **design-system** — Use this skill to generate or audit design systems, check visual consistency, and review PRs that touch styling.
  `B:\AI-Armory\skillz\ECC\design-system`
- **django-celery** — Django + Celery async task patterns — configuration, task design, beat scheduling, retries, canvas workflows, monitoring, and testing.
  `B:\AI-Armory\skillz\ECC\django-celery`
- **django-patterns** — Django architecture patterns, REST API design with DRF, ORM best practices, caching, signals, middleware, and production-grade Django apps.
  `B:\AI-Armory\skillz\ECC\django-patterns`
- **django-security** — Django security best practices, authentication, authorization, CSRF protection, SQL injection prevention, XSS prevention, and secure deployment configurations.
  `B:\AI-Armory\skillz\ECC\django-security`
- **django-tdd** — Django testing strategies with pytest-django, TDD methodology, factory_boy, mocking, coverage, and testing Django REST Framework APIs.
  `B:\AI-Armory\skillz\ECC\django-tdd`
- **django-verification** — Verification loop for Django projects: migrations, linting, tests with coverage, security scans, and deployment readiness checks before release or PR.
  `B:\AI-Armory\skillz\ECC\django-verification`
- **dmux-workflows** — Multi-agent orchestration using dmux (tmux pane manager for AI agents).
  `B:\AI-Armory\skillz\ECC\dmux-workflows`
- **docker-patterns** — Docker and Docker Compose patterns for local development, container security, networking, volume strategies, and multi-service orchestration.
  `B:\AI-Armory\skillz\ECC\docker-patterns`
- **documentation-lookup** — Use up-to-date library and framework docs via Context7 MCP instead of training data.
  `B:\AI-Armory\skillz\ECC\documentation-lookup`
- **dotnet-patterns** — Idiomatic C# and .NET patterns, conventions, dependency injection, async/await, and best practices for building robust, maintainable .NET applications.
  `B:\AI-Armory\skillz\ECC\dotnet-patterns`
- **dynamic-workflow-mode** — Design task-local harnesses, eval gates, and reusable skill extraction for Claude dynamic workflow mode and other adaptive agent harnesses.
  `B:\AI-Armory\skillz\ECC\dynamic-workflow-mode`
- **e2e-testing** — Playwright E2E testing patterns, Page Object Model, configuration, CI/CD integration, artifact management, and flaky test strategies.
  `B:\AI-Armory\skillz\ECC\e2e-testing`
- **ecc-guide** — Guide users through ECC's current agents, skills, commands, hooks, rules, install profiles, and project onboarding by reading the live repository surface before answering.
  `B:\AI-Armory\skillz\ECC\ecc-guide`
- **ecc-recipes** — Map a described workflow to the right ECC command-GROUP with run-order and stop condition, and browse all command-group recipe families.
  `B:\AI-Armory\skillz\ECC\ecc-recipes`
- **ecc-tools-cost-audit** — Evidence-first ECC Tools burn and billing audit workflow.
  `B:\AI-Armory\skillz\ECC\ecc-tools-cost-audit`
- **email-ops** — Evidence-first mailbox triage, drafting, send verification, and sent-mail-safe follow-up workflow for ECC.
  `B:\AI-Armory\skillz\ECC\email-ops`
- **energy-procurement** — Codified expertise for electricity and gas procurement, tariff optimization, demand charge management, renewable PPA evaluation, and multi-facility energy cost management.
  `B:\AI-Armory\skillz\ECC\energy-procurement`
- **enterprise-agent-ops** — Operate long-lived agent workloads with observability, security boundaries, and lifecycle management.
  `B:\AI-Armory\skillz\ECC\enterprise-agent-ops`
- **error-handling** — Patterns for robust error handling across TypeScript, Python, and Go.
  `B:\AI-Armory\skillz\ECC\error-handling`
- **eval-harness** — Formal evaluation framework for Claude Code sessions implementing eval-driven development (EDD) principles
  `B:\AI-Armory\skillz\ECC\eval-harness`
- **evm-token-decimals** — Prevent silent decimal mismatch bugs across EVM chains.
  `B:\AI-Armory\skillz\ECC\evm-token-decimals`
- **exa-search** — Neural search via Exa MCP for web, code, and company research.
  `B:\AI-Armory\skillz\ECC\exa-search`
- **fal-ai-media** — Unified media generation via fal.ai MCP — image, video, and audio.
  `B:\AI-Armory\skillz\ECC\fal-ai-media`
- **fastapi-patterns** — FastAPI best practices covering project structure, Pydantic v2 schemas, dependency injection, async handlers, authentication, authorization, transactional service layers, and testing with httpx and...
  `B:\AI-Armory\skillz\ECC\fastapi-patterns`
- **finance-billing-ops** — Evidence-first revenue, pricing, refunds, team-billing, and billing-model truth workflow for ECC.
  `B:\AI-Armory\skillz\ECC\finance-billing-ops`
- **flox-environments** — Create reproducible, cross-platform (macOS/Linux) development environments with Flox, a declarative Nix-based environment manager.
  `B:\AI-Armory\skillz\ECC\flox-environments`
- **flutter-dart-code-review** — Library-agnostic Flutter/Dart code review checklist covering widget best practices, state management patterns (BLoC, Riverpod, Provider, GetX, MobX, Signals), Dart idioms, performance, accessibility...
  `B:\AI-Armory\skillz\ECC\flutter-dart-code-review`
- **foundation-models-on-device** — Apple FoundationModels framework for on-device LLM — text generation, guided generation with @Generable, tool calling, and snapshot streaming in iOS 26+.
  `B:\AI-Armory\skillz\ECC\foundation-models-on-device`
- **frontend-a11y** — Accessibility patterns for React and Next.js — semantic HTML, ARIA attributes, form labeling, keyboard navigation, focus management, and screen reader support.
  `B:\AI-Armory\skillz\ECC\frontend-a11y`
- **frontend-design-direction** — Set an ECC-specific frontend design direction for production UI work.
  `B:\AI-Armory\skillz\ECC\frontend-design-direction`
- **frontend-patterns** — Frontend development patterns for React, Next.js, state management, performance optimization, and UI best practices.
  `B:\AI-Armory\skillz\ECC\frontend-patterns`
- **frontend-slides** — Create stunning, animation-rich HTML presentations from scratch or by converting PowerPoint files.
  `B:\AI-Armory\skillz\ECC\frontend-slides`
- **fsharp-testing** — F# testing patterns with xUnit, FsUnit, Unquote, FsCheck property-based testing, integration tests, and test organization best practices.
  `B:\AI-Armory\skillz\ECC\fsharp-testing`
- **gan-style-harness** — GAN-inspired Generator-Evaluator agent harness for building high-quality applications autonomously.
  `B:\AI-Armory\skillz\ECC\gan-style-harness`
- **gateguard** — Fact-forcing gate that blocks Edit/Write/Bash (including MultiEdit) and demands concrete investigation (importers, data schemas, user instruction) before allowing the action.
  `B:\AI-Armory\skillz\ECC\gateguard`
- **generating-python-installer** — Commercial-grade Python installer expert for Windows: Nuitka extreme compilation, dist slimming, DLL footprint analysis, and Inno Setup packaging to ship the smallest, fastest installers.
  `B:\AI-Armory\skillz\ECC\generating-python-installer`
- **gget** — gget CLI and Python workflow for quick genomic database queries, sequence lookup, BLAST-style searches, enrichment checks, and reproducible bioinformatics evidence logs.
  `B:\AI-Armory\skillz\ECC\scientific-pkg-gget`
- **git-workflow** — Git workflow patterns including branching strategies, commit conventions, merge vs rebase, conflict resolution, and collaborative development best practices for teams of all sizes.
  `B:\AI-Armory\skillz\ECC\git-workflow`
- **github-ops** — GitHub repository operations, automation, and management.
  `B:\AI-Armory\skillz\ECC\github-ops`
- **golang-patterns** — Idiomatic Go patterns, best practices, and conventions for building robust, efficient, and maintainable Go applications.
  `B:\AI-Armory\skillz\ECC\golang-patterns`
- **golang-testing** — Go testing patterns including table-driven tests, subtests, benchmarks, fuzzing, and test coverage.
  `B:\AI-Armory\skillz\ECC\golang-testing`
- **google-workspace-ops** — Operate across Google Drive, Docs, Sheets, and Slides as one workflow surface for plans, trackers, decks, and shared documents.
  `B:\AI-Armory\skillz\ECC\google-workspace-ops`
- **growth-log** — Use after a complex task, failure, or when reviewing what was learned.
  `B:\AI-Armory\skillz\ECC\growth-log`
- **healthcare-cdss-patterns** — Clinical Decision Support System (CDSS) development patterns.
  `B:\AI-Armory\skillz\ECC\healthcare-cdss-patterns`
- **healthcare-emr-patterns** — EMR/EHR development patterns for healthcare applications.
  `B:\AI-Armory\skillz\ECC\healthcare-emr-patterns`
- **healthcare-eval-harness** — Patient safety evaluation harness for healthcare application deployments.
  `B:\AI-Armory\skillz\ECC\healthcare-eval-harness`
- **healthcare-phi-compliance** — Protected Health Information (PHI) and Personally Identifiable Information (PII) compliance patterns for healthcare applications.
  `B:\AI-Armory\skillz\ECC\healthcare-phi-compliance`
- **hermes-imports** — Convert local Hermes operator workflows into sanitized ECC skills and release-pack artifacts.
  `B:\AI-Armory\skillz\ECC\hermes-imports`
- **hexagonal-architecture** — Design, implement, and refactor Ports & Adapters systems with clear domain boundaries, dependency inversion, and testable use-case orchestration across TypeScript, Java, Kotlin, and Go services.
  `B:\AI-Armory\skillz\ECC\hexagonal-architecture`
- **hipaa-compliance** — HIPAA-specific entrypoint for healthcare privacy and security work.
  `B:\AI-Armory\skillz\ECC\hipaa-compliance`
- **homelab-network-readiness** — Readiness checklist for homelab VLAN segmentation, local DNS filtering, and WireGuard-style remote access before changing router, firewall, DHCP, or VPN configuration.
  `B:\AI-Armory\skillz\ECC\homelab-network-readiness`
- **homelab-network-setup** — Practical home and homelab network planning for gateways, switches, access points, IP ranges, DHCP reservations, DNS, cabling, and common beginner mistakes.
  `B:\AI-Armory\skillz\ECC\homelab-network-setup`
- **homelab-pihole-dns** — Pi-hole installation, blocklist management, DNS-over-HTTPS setup, DHCP integration, local DNS records, and troubleshooting broken DNS resolution on a home network.
  `B:\AI-Armory\skillz\ECC\homelab-pihole-dns`
- **homelab-vlan-segmentation** — Segmenting home networks into VLANs for IoT, guest, trusted, and server traffic using UniFi, pfSense/OPNsense, and MikroTik — including switch trunk config, firewall rules, and wireless SSID mapping.
  `B:\AI-Armory\skillz\ECC\homelab-vlan-segmentation`
- **homelab-wireguard-vpn** — WireGuard VPN server setup, peer configuration, key generation, split tunneling vs full tunnel routing, and remote access to a home network from mobile and laptop clients.
  `B:\AI-Armory\skillz\ECC\homelab-wireguard-vpn`
- **hookify-rules** — This skill should be used when the user asks to create a hookify rule, write a hook rule, configure hookify, add a hookify rule, or needs guidance on hookify rule syntax and patterns.
  `B:\AI-Armory\skillz\ECC\hookify-rules`
- **inherit-legacy-style** — Legacy-project style inheritance skill.
  `B:\AI-Armory\skillz\ECC\inherit-legacy-style`
- **intent-driven-development** — Turn ambiguous or high-impact product and engineering changes into scoped, verifiable acceptance criteria before or alongside implementation.
  `B:\AI-Armory\skillz\ECC\intent-driven-development`
- **inventory-demand-planning** — Codified expertise for demand forecasting, safety stock optimization, replenishment planning, and promotional lift estimation at multi-location retailers.
  `B:\AI-Armory\skillz\ECC\inventory-demand-planning`
- **investor-materials** — Create and update pitch decks, one-pagers, investor memos, accelerator applications, financial models, and fundraising materials.
  `B:\AI-Armory\skillz\ECC\investor-materials`
- **investor-outreach** — Draft cold emails, warm intro blurbs, follow-ups, update emails, and investor communications for fundraising.
  `B:\AI-Armory\skillz\ECC\investor-outreach`
- **ios-icon-gen** — Generate iOS app icons as PNG imagesets for Xcode asset catalogs from SF Symbols (5000+ Apple-native) or Iconify API (275k+ open source icons from 200+ collections).
  `B:\AI-Armory\skillz\ECC\ios-icon-gen`
- **iterative-retrieval** — Pattern for progressively refining context retrieval to solve the subagent context problem
  `B:\AI-Armory\skillz\ECC\iterative-retrieval`
- **ito-basket-compare** — Compare Itô prediction-market baskets against a user's knowledge base, portfolio notes, financial context, watchlist, or research thesis.
  `B:\AI-Armory\skillz\ECC\ito-basket-compare`
- **ito-data-atlas-agent** — Design background Data Atlas style agents for Itô basket research, market discovery, parameter drafting, and human-in-the-loop editing.
  `B:\AI-Armory\skillz\ECC\ito-data-atlas-agent`
- **ito-market-intelligence** — Research prediction-market events, venues, underliers, liquidity, and news context for Itô basket workflows.
  `B:\AI-Armory\skillz\ECC\ito-market-intelligence`
- **ito-trade-planner** — Build a non-advisory prediction-market trade planning worksheet for Itô or venue workflows.
  `B:\AI-Armory\skillz\ECC\ito-trade-planner`
- **java-coding-standards** — Java coding standards for Spring Boot and Quarkus services: naming, immutability, Optional usage, streams, exceptions, generics, CDI, reactive patterns, and project layout.
  `B:\AI-Armory\skillz\ECC\java-coding-standards`
- **jira-integration** — Use this skill when retrieving Jira tickets, analyzing requirements, updating ticket status, adding comments, or transitioning issues.
  `B:\AI-Armory\skillz\ECC\jira-integration`
- **jpa-patterns** — JPA/Hibernate patterns for entity design, relationships, query optimization, transactions, auditing, indexing, pagination, and pooling in Spring Boot.
  `B:\AI-Armory\skillz\ECC\jpa-patterns`
- **knowledge-ops** — Knowledge base management, ingestion, sync, and retrieval across multiple storage layers (local files, MCP memory, vector stores, Git repos).
  `B:\AI-Armory\skillz\ECC\knowledge-ops`
- **kotlin-coroutines-flows** — Kotlin Coroutines and Flow patterns for Android and KMP — structured concurrency, Flow operators, StateFlow, error handling, and testing.
  `B:\AI-Armory\skillz\ECC\kotlin-coroutines-flows`
- **kotlin-exposed-patterns** — JetBrains Exposed ORM patterns including DSL queries, DAO pattern, transactions, HikariCP connection pooling, Flyway migrations, and repository pattern.
  `B:\AI-Armory\skillz\ECC\kotlin-exposed-patterns`
- **kotlin-ktor-patterns** — Ktor server patterns including routing DSL, plugins, authentication, Koin DI, kotlinx.serialization, WebSockets, and testApplication testing.
  `B:\AI-Armory\skillz\ECC\kotlin-ktor-patterns`
- **kotlin-patterns** — Idiomatic Kotlin patterns, best practices, and conventions for building robust, efficient, and maintainable Kotlin applications with coroutines, null safety, and DSL builders.
  `B:\AI-Armory\skillz\ECC\kotlin-patterns`
- **kotlin-testing** — Kotlin testing patterns with Kotest, MockK, coroutine testing, property-based testing, and Kover coverage.
  `B:\AI-Armory\skillz\ECC\kotlin-testing`
- **kubernetes-patterns** — Kubernetes workload patterns, resource management, RBAC, probes, autoscaling, ConfigMap/Secret handling, and kubectl debugging for production-grade deployments.
  `B:\AI-Armory\skillz\ECC\kubernetes-patterns`
- **laravel-patterns** — Laravel architecture patterns, routing/controllers, Eloquent ORM, service layers, queues, events, caching, and API resources for production apps.
  `B:\AI-Armory\skillz\ECC\laravel-patterns`
- **laravel-plugin-discovery** — Discover and evaluate Laravel packages via LaraPlugins.io MCP.
  `B:\AI-Armory\skillz\ECC\laravel-plugin-discovery`
- **laravel-security** — Laravel security best practices — authentication, authorization, Eloquent safety, CSRF, XSS prevention, API security, and secure deployment configurations.
  `B:\AI-Armory\skillz\ECC\laravel-security`
- **laravel-tdd** — Laravel testing strategies with PHPUnit, Pest, model factories, HTTP tests, Sanctum authentication testing, mocking, and coverage.
  `B:\AI-Armory\skillz\ECC\laravel-tdd`
- **laravel-verification** — Verification loop for Laravel projects: env checks, linting, static analysis, tests with coverage, security scans, and deployment readiness.
  `B:\AI-Armory\skillz\ECC\laravel-verification`
- **latency-critical-systems** — Use for latency-sensitive systems such as realtime dashboards, market data, streaming agents, execution gateways, queues, caches, or HFT-like infrastructure where freshness and p95 latency matter.
  `B:\AI-Armory\skillz\ECC\latency-critical-systems`
- **lead-intelligence** — AI-native lead intelligence and outreach pipeline.
  `B:\AI-Armory\skillz\ECC\lead-intelligence`
- **liquid-glass-design** — iOS 26 Liquid Glass design system — dynamic glass material with blur, reflection, and interactive morphing for SwiftUI, UIKit, and WidgetKit.
  `B:\AI-Armory\skillz\ECC\liquid-glass-design`
- **literature-review** — Systematic literature-review workflow for academic, biomedical, technical, and scientific topics, including search planning, source screening, synthesis, citation checks, and evidence logging.
  `B:\AI-Armory\skillz\ECC\scientific-thinking-literature-review`
- **llm-trading-agent-security** — Security patterns for autonomous trading agents with wallet or transaction authority.
  `B:\AI-Armory\skillz\ECC\llm-trading-agent-security`
- **logistics-exception-management** — Codified expertise for handling freight exceptions, shipment delays, damages, losses, and carrier disputes.
  `B:\AI-Armory\skillz\ECC\logistics-exception-management`
- **loop-design-check** — Design a goal-oriented agent loop, and review it for the ways loops go wrong — spinning and burning tokens, Goodhart-gaming the verifier, or running a wrong answer to completion.
  `B:\AI-Armory\skillz\ECC\loop-design-check`
- **mailtrap-email-integration** — Guides agents through integrating transactional email sending via Mailtrap's Email API, including sandbox testing, domain verification, and API authentication.
  `B:\AI-Armory\skillz\ECC\mailtrap-email-integration`
- **make-interfaces-feel-better** — Apply concrete design-engineering details that make interfaces feel polished.
  `B:\AI-Armory\skillz\ECC\make-interfaces-feel-better`
- **manim-video** — Build reusable Manim explainers for technical concepts, graphs, system diagrams, and product walkthroughs, then hand off to the wider ECC video stack if needed.
  `B:\AI-Armory\skillz\ECC\manim-video`
- **market-research** — Conduct market research, competitive analysis, investor due diligence, and industry intelligence with source attribution and decision-oriented summaries.
  `B:\AI-Armory\skillz\ECC\market-research`
- **marketing-campaign** — End-to-end marketing campaign planning and execution.
  `B:\AI-Armory\skillz\ECC\marketing-campaign`
- **mcp-server-patterns** — Build MCP servers with Node/TypeScript SDK — tools, resources, prompts, Zod validation, stdio vs Streamable HTTP.
  `B:\AI-Armory\skillz\ECC\mcp-server-patterns`
- **messages-ops** — Evidence-first live messaging workflow for ECC.
  `B:\AI-Armory\skillz\ECC\messages-ops`
- **ml-adoption-playbook** — End-to-end methodology for AI agents and software engineers to add machine learning algorithms to existing non-ML codebases.
  `B:\AI-Armory\skillz\ECC\ml-adoption-playbook`
- **mle-workflow** — Production machine-learning engineering workflow for data contracts, reproducible training, model evaluation, deployment, monitoring, and rollback.
  `B:\AI-Armory\skillz\ECC\mle-workflow`
- **motion-advanced** — Advanced motion patterns for React / Next.js — drag & drop, gestures, text animations, SVG path drawing, custom hooks, imperative sequences (useAnimate), loaders, and the full API decision tree.
  `B:\AI-Armory\skillz\ECC\motion-advanced`  ·  _tags:_ motion, animation, advanced, gestures, svg
- **motion-foundations** — Motion tokens, spring presets, performance rules, device adaptation, accessibility enforcement, and SSR safety for React / Next.js using motion/react.
  `B:\AI-Armory\skillz\ECC\motion-foundations`  ·  _tags:_ motion, animation, performance, accessibility
- **motion-patterns** — Production-ready animation patterns for React / Next.js — button, modal, toast, stagger, page transitions, exit animations, scroll, and layout — built on motion-foundations tokens and springs.
  `B:\AI-Armory\skillz\ECC\motion-patterns`  ·  _tags:_ motion, animation, ui-patterns
- **motion-ui** — Production-ready UI motion system for React/Next.js.
  `B:\AI-Armory\skillz\ECC\motion-ui`
- **mysql-patterns** — MySQL and MariaDB schema, query, indexing, transaction, replication, and connection-pool patterns for production backends.
  `B:\AI-Armory\skillz\ECC\mysql-patterns`
- **nanoclaw-repl** — Operate and extend NanoClaw v2, ECC's zero-dependency session-aware REPL built on claude -p.
  `B:\AI-Armory\skillz\ECC\nanoclaw-repl`
- **nestjs-patterns** — NestJS architecture patterns for modules, controllers, providers, DTO validation, guards, interceptors, config, and production-grade TypeScript backends.
  `B:\AI-Armory\skillz\ECC\nestjs-patterns`
- **netmiko-ssh-automation** — Safe Python Netmiko patterns for read-only collection, bounded batch SSH, TextFSM parsing, guarded config changes, timeouts, and network automation error handling.
  `B:\AI-Armory\skillz\ECC\netmiko-ssh-automation`
- **network-bgp-diagnostics** — Diagnostics-only BGP troubleshooting patterns for neighbor state, route exchange, prefix policy, AS path inspection, and safe evidence collection.
  `B:\AI-Armory\skillz\ECC\network-bgp-diagnostics`
- **network-config-validation** — Pre-deployment checks for router and switch configuration, including dangerous commands, duplicate addresses, subnet overlaps, stale references, management-plane risk, and IOS-style security hygiene.
  `B:\AI-Armory\skillz\ECC\network-config-validation`
- **network-interface-health** — Diagnose interface errors, drops, CRCs, duplex mismatches, flapping, speed negotiation issues, and counter trends on routers, switches, and Linux hosts.
  `B:\AI-Armory\skillz\ECC\network-interface-health`
- **nextjs-turbopack** — Next.js 16+ and Turbopack — incremental bundling, FS caching, dev speed, and when to use Turbopack vs webpack.
  `B:\AI-Armory\skillz\ECC\nextjs-turbopack`
- **nodejs-keccak256** — Prevent Ethereum hashing bugs in JavaScript and TypeScript.
  `B:\AI-Armory\skillz\ECC\nodejs-keccak256`
- **nutrient-document-processing** — Process, convert, OCR, extract, redact, sign, and fill documents using the Nutrient DWS API.
  `B:\AI-Armory\skillz\ECC\nutrient-document-processing`
- **nuxt4-patterns** — Nuxt 4 app patterns for hydration safety, performance, route rules, lazy loading, and SSR-safe data fetching with useFetch and useAsyncData.
  `B:\AI-Armory\skillz\ECC\nuxt4-patterns`
- **openclaw-persona-forge** — 为 OpenClaw AI Agent 锻造完整的龙虾灵魂方案。根据用户偏好或随机抽卡， 输出身份定位、灵魂描述(SOUL.md)、角色化底线规则、名字和头像生图提示词。 如当前环境提供已审核的生图 skill，可自动生成统一风格头像图片。 当用户需要创建、设计或定制 OpenClaw 龙虾灵魂时使用。 不适用于：微调已有 SOUL.md、非 OpenClaw 平台的角色设计、纯工具型无性格...
  `B:\AI-Armory\skillz\ECC\openclaw-persona-forge`
- **opensource-pipeline** — Open-source pipeline: fork, sanitize, and package private projects for safe public release.
  `B:\AI-Armory\skillz\ECC\opensource-pipeline`
- **orch-add-feature** — Orchestrate building a brand-new feature end to end — research, plan, TDD implementation, review, and gated commit — by delegating each phase to the matching ECC agent.
  `B:\AI-Armory\skillz\ECC\orch-add-feature`
- **orch-build-mvp** — Orchestrate bootstrapping a working MVP from a design or spec document — ingest the doc, plan thin vertical slices, scaffold the first end-to-end slice, then TDD-implement, review, and gated commit.
  `B:\AI-Armory\skillz\ECC\orch-build-mvp`
- **orch-change-feature** — Orchestrate altering an existing, working feature to new desired behavior — update its tests to the new spec, change the implementation to match, review, and gated commit.
  `B:\AI-Armory\skillz\ECC\orch-change-feature`
- **orch-fix-defect** — Orchestrate fixing a bug — reproduce it as a failing regression test, fix to green, review, and gated commit — by delegating each phase to the matching ECC agent.
  `B:\AI-Armory\skillz\ECC\orch-fix-defect`
- **orch-pipeline** — Shared orchestration engine for the orch-* skill family.
  `B:\AI-Armory\skillz\ECC\orch-pipeline`
- **orch-refine-code** — Orchestrate a behavior-preserving refactor — confirm tests are green, restructure without changing behavior, keep tests green, review, and gated commit.
  `B:\AI-Armory\skillz\ECC\orch-refine-code`
- **parallel-execution-optimizer** — Use when the user wants a task done much faster through parallel work, concurrent agents, batched tool calls, isolated worktrees, or many independent verification lanes without losing correctness.
  `B:\AI-Armory\skillz\ECC\parallel-execution-optimizer`
- **perl-patterns** — Modern Perl 5.36+ idioms, best practices, and conventions for building robust, maintainable Perl applications.
  `B:\AI-Armory\skillz\ECC\perl-patterns`
- **perl-security** — Comprehensive Perl security covering taint mode, input validation, safe process execution, DBI parameterized queries, web security (XSS/SQLi/CSRF), and perlcritic security policies.
  `B:\AI-Armory\skillz\ECC\perl-security`
- **perl-testing** — Perl testing patterns using Test2::V0, Test::More, prove runner, mocking, coverage with Devel::Cover, and TDD methodology.
  `B:\AI-Armory\skillz\ECC\perl-testing`
- **plan-canvas** — Open plans and HTML artifacts in a local browser canvas where the human annotates elements, chats, and approves or requests changes without leaving the page.
  `B:\AI-Armory\skillz\ECC\plan-canvas`
- **plan-orchestrate** — Read a plan document, decompose it into steps, design a per-step agent chain from the ECC catalogue, and emit ready-to-paste /orchestrate custom prompts.
  `B:\AI-Armory\skillz\ECC\plan-orchestrate`
- **plankton-code-quality** — Write-time code quality enforcement using Plankton — auto-formatting, linting, and Claude-powered fixes on every file edit via hooks.
  `B:\AI-Armory\skillz\ECC\plankton-code-quality`
- **postgres-patterns** — PostgreSQL database patterns for query optimization, schema design, indexing, and security.
  `B:\AI-Armory\skillz\ECC\postgres-patterns`
- **prediction-market-oracle-research** — Research prediction markets as data sources or oracle signals for products, agents, dashboards, and corporate decision intelligence.
  `B:\AI-Armory\skillz\ECC\prediction-market-oracle-research`
- **prediction-market-risk-review** — Review prediction-market, basket, oracle, and trading-agent workflows for compliance, safety, data-quality, privacy, and execution risk.
  `B:\AI-Armory\skillz\ECC\prediction-market-risk-review`
- **prisma-patterns** — Prisma ORM patterns for TypeScript backends — schema design, query optimization, transactions, pagination, and critical traps like updateMany returning count not records, $transaction timeouts...
  `B:\AI-Armory\skillz\ECC\prisma-patterns`
- **product-capability** — Translate PRD intent, roadmap asks, or product discussions into an implementation-ready capability plan that exposes constraints, invariants, interfaces, and unresolved decisions before multi-service...
  `B:\AI-Armory\skillz\ECC\product-capability`
- **product-lens** — Use this skill to validate the "why" before building, run product diagnostics, and pressure-test product direction before the request becomes an implementation contract.
  `B:\AI-Armory\skillz\ECC\product-lens`
- **production-audit** — Local-evidence production readiness audit for shipped apps, pre-launch reviews, post-merge checks, and "what breaks in prod?" questions without sending repo data to an external audit service.
  `B:\AI-Armory\skillz\ECC\production-audit`
- **production-scheduling** — Codified expertise for production scheduling, job sequencing, line balancing, changeover optimization, and bottleneck resolution in discrete and batch manufacturing.
  `B:\AI-Armory\skillz\ECC\production-scheduling`
- **project-flow-ops** — Operate execution flow across GitHub and Linear by triaging issues and pull requests, linking active work, and keeping GitHub public-facing while Linear remains the internal execution layer.
  `B:\AI-Armory\skillz\ECC\project-flow-ops`
- **prompt-optimizer** — Analyze raw prompts, identify intent and gaps, match ECC components (skills/commands/agents/hooks), and output a ready-to-paste optimized prompt.
  `B:\AI-Armory\skillz\ECC\prompt-optimizer`
- **pubmed-database** — Direct PubMed and NCBI E-utilities search workflows for biomedical literature, MeSH queries, PMID lookup, citation retrieval, and API-backed literature monitoring.
  `B:\AI-Armory\skillz\ECC\scientific-db-pubmed-database`
- **python-patterns** — Pythonic idioms, PEP 8 standards, type hints, and best practices for building robust, efficient, and maintainable Python applications.
  `B:\AI-Armory\skillz\ECC\python-patterns`
- **python-testing** — Python testing strategies using pytest, TDD methodology, fixtures, mocking, parametrization, and coverage requirements.
  `B:\AI-Armory\skillz\ECC\python-testing`
- **pytorch-patterns** — PyTorch deep learning patterns and best practices for building robust, efficient, and reproducible training pipelines, model architectures, and data loading.
  `B:\AI-Armory\skillz\ECC\pytorch-patterns`
- **quality-nonconformance** — Codified expertise for quality control, non-conformance investigation, root cause analysis, corrective action, and supplier quality management in regulated manufacturing.
  `B:\AI-Armory\skillz\ECC\quality-nonconformance`
- **quarkus-patterns** — Quarkus 3.x LTS architecture patterns with Camel for messaging, RESTful API design, CDI services, data access with Panache, and async processing.
  `B:\AI-Armory\skillz\ECC\quarkus-patterns`
- **quarkus-security** — Quarkus Security best practices for authentication, authorization, JWT/OIDC, RBAC, input validation, CSRF, secrets management, and dependency security.
  `B:\AI-Armory\skillz\ECC\quarkus-security`
- **quarkus-tdd** — Test-driven development for Quarkus 3.x LTS using JUnit 5, Mockito, REST Assured, Camel testing, and JaCoCo.
  `B:\AI-Armory\skillz\ECC\quarkus-tdd`
- **quarkus-verification** — Verification loop for Quarkus projects: build, static analysis, tests with coverage, security scans, native compilation, and diff review before release or PR.
  `B:\AI-Armory\skillz\ECC\quarkus-verification`
- **ralphinho-rfc-pipeline** — RFC-driven multi-agent DAG execution pattern with quality gates, merge queues, and work unit orchestration.
  `B:\AI-Armory\skillz\ECC\ralphinho-rfc-pipeline`
- **react-native-patterns** — React Native and Expo app patterns — Expo Router navigation, state separation (server/client/route/form), TanStack Query data fetching with Zod, performant lists, NativeWind/StyleSheet styling...
  `B:\AI-Armory\skillz\ECC\react-native-patterns`
- **react-patterns** — React 18/19 patterns including hooks discipline, server/client component boundaries, Suspense + error boundaries, form actions, data fetching, state management decision trees, and accessibility-first...
  `B:\AI-Armory\skillz\ECC\react-patterns`
- **react-performance** — React and Next.js performance optimization patterns adapted from Vercel Engineering's React Best Practices (https://github.com/vercel-labs/agent-skills).
  `B:\AI-Armory\skillz\ECC\react-performance`
- **react-testing** — React component testing with React Testing Library, Vitest/Jest, MSW for network mocking, accessibility assertions with axe, and the decision boundary between component tests and Playwright/Cypress...
  `B:\AI-Armory\skillz\ECC\react-testing`
- **recsys-pipeline-architect** — Design composable recommendation, ranking, and feed pipelines using the six-stage Source→Hydrator→Filter→Scorer→Selector→SideEffect framework popularized by xAI's open-sourced For You algorithm.
  `B:\AI-Armory\skillz\ECC\recsys-pipeline-architect`
- **recursive-decision-ledger** — Use when the user asks for repeated rollouts, marked decision processes, high-dimensional search, stochastic optimization, local-optima exploration, ensemble comparison, or recursive reasoning with a...
  `B:\AI-Armory\skillz\ECC\recursive-decision-ledger`
- **redis-patterns** — Redis data structure patterns, caching strategies, distributed locks, rate limiting, pub/sub, and connection management for production applications.
  `B:\AI-Armory\skillz\ECC\redis-patterns`
- **regex-vs-llm-structured-text** — Decision framework for choosing between regex and LLM when parsing structured text — start with regex, add LLM only for low-confidence edge cases.
  `B:\AI-Armory\skillz\ECC\regex-vs-llm-structured-text`
- **remotion-video-creation** — Best practices for Remotion - Video creation in React.
  `B:\AI-Armory\skillz\ECC\remotion-video-creation`
- **repo-scan** — Cross-stack source code asset audit — classifies every file, detects embedded third-party libraries, and delivers actionable four-level verdicts per module with interactive HTML reports.
  `B:\AI-Armory\skillz\ECC\repo-scan`
- **research-ops** — Evidence-first current-state research workflow for ECC.
  `B:\AI-Armory\skillz\ECC\research-ops`
- **returns-reverse-logistics** — Codified expertise for returns authorization, receipt and inspection, disposition decisions, refund processing, fraud detection, and warranty claims management.
  `B:\AI-Armory\skillz\ECC\returns-reverse-logistics`
- **rules-distill** — Scan skills to extract cross-cutting principles and distill them into rules — append, revise, or create new rule files
  `B:\AI-Armory\skillz\ECC\rules-distill`
- **rust-patterns** — Idiomatic Rust patterns, ownership, error handling, traits, concurrency, and best practices for building safe, performant applications.
  `B:\AI-Armory\skillz\ECC\rust-patterns`
- **rust-testing** — Rust testing patterns including unit tests, integration tests, async testing, property-based testing, mocking, and coverage.
  `B:\AI-Armory\skillz\ECC\rust-testing`
- **safety-guard** — Use this skill to prevent destructive operations when working on production systems or running agents autonomously.
  `B:\AI-Armory\skillz\ECC\safety-guard`
- **santa-method** — Multi-agent adversarial verification with convergence loop.
  `B:\AI-Armory\skillz\ECC\santa-method`
- **scholar-evaluation** — Structured scholarly-work evaluation for papers, proposals, literature reviews, methods sections, evidence quality, citation support, and research-writing feedback.
  `B:\AI-Armory\skillz\ECC\scientific-thinking-scholar-evaluation`
- **search-first** — Research-before-coding workflow.
  `B:\AI-Armory\skillz\ECC\search-first`
- **security-bounty-hunter** — Hunt for exploitable, bounty-worthy security issues in repositories.
  `B:\AI-Armory\skillz\ECC\security-bounty-hunter`
- **security-review** — Use this skill when adding authentication, handling user input, working with secrets, creating API endpoints, or implementing payment/sensitive features.
  `B:\AI-Armory\skillz\ECC\security-review`
- **security-scan** — Scan your Claude Code configuration (.claude/ directory) for security vulnerabilities, misconfigurations, and injection risks using AgentShield.
  `B:\AI-Armory\skillz\ECC\security-scan`
- **seo** — Audit, plan, and implement SEO improvements across technical SEO, on-page optimization, structured data, Core Web Vitals, and content strategy.
  `B:\AI-Armory\skillz\ECC\seo`
- **skill-comply** — Visualize whether skills, rules, and agent definitions are actually followed — auto-generates scenarios at 3 prompt strictness levels, runs agents, classifies behavioral sequences, and reports...
  `B:\AI-Armory\skillz\ECC\skill-comply`
- **skill-scout** — Search existing local, marketplace, GitHub, and web skill sources before creating a new skill.
  `B:\AI-Armory\skillz\ECC\skill-scout`
- **skill-stocktake** — Use when auditing Claude skills and commands for quality.
  `B:\AI-Armory\skillz\ECC\skill-stocktake`
- **social-graph-ranker** — Weighted social-graph ranking for warm intro discovery, bridge scoring, and network gap analysis across X and LinkedIn.
  `B:\AI-Armory\skillz\ECC\social-graph-ranker`
- **social-publisher** — Agent-driven scheduling and publishing of social media posts across 13 platforms via SocialClaw.
  `B:\AI-Armory\skillz\ECC\social-publisher`
- **springboot-patterns** — Spring Boot architecture patterns, REST API design, layered services, data access, caching, async processing, and logging.
  `B:\AI-Armory\skillz\ECC\springboot-patterns`
- **springboot-security** — Spring Security best practices for authn/authz, validation, CSRF, secrets, headers, rate limiting, and dependency security in Java Spring Boot services.
  `B:\AI-Armory\skillz\ECC\springboot-security`
- **springboot-tdd** — Test-driven development for Spring Boot using JUnit 5, Mockito, MockMvc, Testcontainers, and JaCoCo.
  `B:\AI-Armory\skillz\ECC\springboot-tdd`
- **springboot-verification** — Verification loop for Spring Boot projects: build, static analysis, tests with coverage, security scans, and diff review before release or PR.
  `B:\AI-Armory\skillz\ECC\springboot-verification`
- **strategic-compact** — Suggests manual context compaction at logical intervals to preserve context through task phases rather than arbitrary auto-compaction.
  `B:\AI-Armory\skillz\ECC\strategic-compact`
- **swift-actor-persistence** — Thread-safe data persistence in Swift using actors — in-memory cache with file-backed storage, eliminating data races by design.
  `B:\AI-Armory\skillz\ECC\swift-actor-persistence`
- **swift-concurrency-6-2** — Swift 6.2 Approachable Concurrency — single-threaded by default, @concurrent for explicit background offloading, isolated conformances for main actor types.
  `B:\AI-Armory\skillz\ECC\swift-concurrency-6-2`
- **swift-protocol-di-testing** — Protocol-based dependency injection for testable Swift code — mock file system, network, and external APIs using focused protocols and Swift Testing.
  `B:\AI-Armory\skillz\ECC\swift-protocol-di-testing`
- **swiftui-patterns** — SwiftUI architecture patterns, state management with @Observable, view composition, navigation, performance optimization, and modern iOS/macOS UI best practices.
  `B:\AI-Armory\skillz\ECC\swiftui-patterns`
- **taste** — A creative-direction (taste) layer for music videos and short-form edits in the angelcore / cloud-trance / hyperpop visual family.
  `B:\AI-Armory\skillz\ECC\taste`
- **tdd-workflow** — Use this skill when writing new features, fixing bugs, or refactoring code.
  `B:\AI-Armory\skillz\ECC\tdd-workflow`
- **team-agent-orchestration** — Run team-based orchestration for agent squads using work items, ownership, agent Kanban, merge gates, and control pane handoffs.
  `B:\AI-Armory\skillz\ECC\team-agent-orchestration`
- **team-builder** — Interactive agent picker for composing and dispatching parallel teams
  `B:\AI-Armory\skillz\ECC\team-builder`
- **terminal-ops** — Evidence-first repo execution workflow for ECC.
  `B:\AI-Armory\skillz\ECC\terminal-ops`
- **tinystruct-patterns** — Expert guidance for developing with the tinystruct Java framework.
  `B:\AI-Armory\skillz\ECC\tinystruct-patterns`
- **token-budget-advisor** — Offers the user an informed choice about how much response depth to consume before answering.
  `B:\AI-Armory\skillz\ECC\token-budget-advisor`
- **ui-demo** — Record polished UI demo videos using Playwright.
  `B:\AI-Armory\skillz\ECC\ui-demo`
- **ui-to-vue** — Use when the user has UI screenshots or design exports that need batch conversion into Vue 3 components, especially with Vant, Element Plus, or Ant Design Vue.
  `B:\AI-Armory\skillz\ECC\ui-to-vue`
- **uncloud** — Use when managing an Uncloud cluster — deploying services, configuring Caddy ingress, adding static proxy routes for non-cluster devices, publishing ports, scaling, inspecting logs, or managing...
  `B:\AI-Armory\skillz\ECC\uncloud`
- **unified-notifications-ops** — Operate notifications as one ECC-native workflow across GitHub, Linear, desktop alerts, hooks, and connected communication surfaces.
  `B:\AI-Armory\skillz\ECC\unified-notifications-ops`
- **uspto-database** — USPTO patent and trademark data workflow for official record lookup, PatentSearch queries, TSDR checks, assignment data, and reproducible IP research logs.
  `B:\AI-Armory\skillz\ECC\scientific-db-uspto-database`
- **verification-loop** — A comprehensive verification system for Claude Code sessions.
  `B:\AI-Armory\skillz\ECC\verification-loop`
- **video-editing** — AI-assisted video editing workflows for cutting, structuring, and augmenting real footage.
  `B:\AI-Armory\skillz\ECC\video-editing`
- **videodb** — See, Understand, Act on video and audio.
  `B:\AI-Armory\skillz\ECC\videodb`
- **visa-doc-translate** — Translate visa application documents (images) to English and create a bilingual PDF with original and translation
  `B:\AI-Armory\skillz\ECC\visa-doc-translate`
- **vite-patterns** — Vite build tool patterns including config, plugins, HMR, env variables, proxy setup, SSR, library mode, dependency pre-bundling, and build optimization.
  `B:\AI-Armory\skillz\ECC\vite-patterns`
- **vue-patterns** — Vue.js 3 Composition API patterns, component architecture, reactivity best practices, Pinia state management, Vue Router navigation, and Nuxt SSR patterns.
  `B:\AI-Armory\skillz\ECC\vue-patterns`
- **windows-desktop-e2e** — E2E testing for Windows native desktop apps (WPF, WinForms, Win32/MFC, Qt) using pywinauto and Windows UI Automation.
  `B:\AI-Armory\skillz\ECC\windows-desktop-e2e`
- **workspace-surface-audit** — Audit the active repo, MCP servers, plugins, connectors, env surfaces, and harness setup, then recommend the highest-value ECC-native skills, hooks, agents, and operator workflows.
  `B:\AI-Armory\skillz\ECC\workspace-surface-audit`
- **x-api** — X/Twitter API integration for posting tweets, threads, reading timelines, search, and analytics.
  `B:\AI-Armory\skillz\ECC\x-api`

</details>

<details><summary><b>open-design</b> (162 skills)</summary>

- **8-bit-orbit-video-template** — Hyperframes-based video template for retro pixel deck motion design.
  `B:\AI-Armory\skillz\open-design\8-bit-orbit-video-template`  ·  _tags:_ hyperframes video template, video template, pixel motion deck, retro presentation video, Hyperframes 模板, 视频模板, 像素风动效
- **ad-creative** — Generate and iterate ad creative including headlines, descriptions, and primary text.
  `B:\AI-Armory\skillz\open-design\ad-creative`  ·  _tags:_ ad creative, ad headline, ad copy, paid social ad, search ad
- **after-hours-editorial-template** — Luxury dark-editorial HyperFrames template for three-page cinematic storyboards, inspired by haute couture title cards and magazine chapter spreads.
  `B:\AI-Armory\skillz\open-design\after-hours-editorial-template`  ·  _tags:_ after hours editorial template, dark fashion hyperframes template, haute couture motion pages, magazine style cinematic slides, 高级暗黑时尚风模板, 高定杂志风动效
- **agent-browser** — Browser automation CLI for AI agents.
  `B:\AI-Armory\skillz\open-design\agent-browser`  ·  _tags:_ browser, current browser tab, selected tab, open website, test this web app, take a screenshot, element screenshot, extract logo, extract fonts, extract colors, extract images, extract motion, OG m...
- **ai-music-album** — Full-lifecycle AI music album production — concept, lyric drafting, track sequencing, and export.
  `B:\AI-Armory\skillz\open-design\ai-music-album`  ·  _tags:_ ai music, music album, lyric writing, track sequencing, album production
- **algorithmic-art** — Create generative art using p5.js with seeded randomness so every render is reproducible.
  `B:\AI-Armory\skillz\open-design\algorithmic-art`  ·  _tags:_ algorithmic art, generative art, p5js, procedural art, seeded randomness, 生成艺术
- **apple-hig** — Apple Human Interface Guidelines as 14 agent skills covering platforms, foundations, components, patterns, inputs, and technologies for iOS, macOS, visionOS, watchOS, and tvOS.
  `B:\AI-Armory\skillz\open-design\apple-hig`  ·  _tags:_ apple hig, human interface, ios design, macos design, visionos design
- **article-magazine** — Huashu / huashu-md-html-inspired magazine article layout for turning Markdown or notes into a polished long-form HTML essay.
  `B:\AI-Armory\skillz\open-design\article-magazine`  ·  _tags:_ blog, essay, newsletter, 公众号, 博客, 文章
- **artifacts-builder** — Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui).
  `B:\AI-Armory\skillz\open-design\artifacts-builder`  ·  _tags:_ artifacts builder, html artifact, multi component artifact, react artifact
- **brainstorming** — Transform rough ideas into fully-formed designs through structured questioning and alternative exploration.
  `B:\AI-Armory\skillz\open-design\brainstorming`  ·  _tags:_ brainstorm, ideation, concept exploration, rough ideas, design alternatives
- **brand-extract** — Extract a complete Brand Kit from a live website by driving the in-app browser.
  `B:\AI-Armory\skillz\open-design\brand-extract`  ·  _tags:_ extract a brand, extract brand, brand from url, brand extraction, pull the brand, extract the colors, extract the fonts, extract the logo, build a brand kit
- **brand-guidelines** — Apply Anthropic's official brand colors and typography to artifacts for consistent visual identity and professional design standards.
  `B:\AI-Armory\skillz\open-design\brand-guidelines`  ·  _tags:_ brand guidelines, brand colors, brand typography, visual identity
- **brandkit** — Premium brand-kit image generation skill for creating high-end brand-guidelines boards, logo systems, identity decks, and visual-world presentations.
  `B:\AI-Armory\skillz\open-design\brandkit`  ·  _tags:_ brand kit, brand guidelines board, logo system, identity board
- **canvas-design** — Create beautiful visual art in PNG and PDF documents using design philosophy and aesthetic principles for posters, illustrations, and static pieces.
  `B:\AI-Armory\skillz\open-design\canvas-design`  ·  _tags:_ canvas design, visual art, poster design, create poster, illustration, 海报, 插画
- **card-twitter** — Twitter quote or data card designed to pair with a post.
  `B:\AI-Armory\skillz\open-design\card-twitter`  ·  _tags:_ twitter, x, quote, 金句
- **card-xiaohongshu** — Xiaohongshu-style knowledge cards, arranged as a swipeable multi-card carousel.
  `B:\AI-Armory\skillz\open-design\card-xiaohongshu`  ·  _tags:_ xhs, 小红书, carousel, 图文
- **chat-motion-overlay** — Generate configurable chat motion overlays from a transcript or screenshot, including plain bubble scenes, app-style chat containers, optional device frames, preset or uploaded avatars, nickname...
  `B:\AI-Armory\skillz\open-design\chat-motion-overlay`  ·  _tags:_ chat motion overlay, animated chat, chat bubbles, message overlay, transparent chat video, 微信聊天动效, 聊天气泡动效, 透明聊天视频
- **color-expert** — Color science expert skill with 286K words of reference material covering OKLCH/OKLAB, palette generation, accessibility/contrast, color naming, pigment mixing, and historical color theory.
  `B:\AI-Armory\skillz\open-design\color-expert`  ·  _tags:_ color theory, palette generator, color science, oklch palette, contrast check
- **competitive-ads-extractor** — Extract and analyze competitors' ads from ad libraries to understand messaging and creative approaches that resonate.
  `B:\AI-Armory\skillz\open-design\competitive-ads-extractor`  ·  _tags:_ competitive ads, ad library extract, competitor creative, ad teardown
- **copywriting** — Write and rewrite marketing copy for landing pages, homepages, and ads.
  `B:\AI-Armory\skillz\open-design\copywriting`  ·  _tags:_ copywriting, landing copy, ad copy, homepage copy, rewrite copy
- **creative-director** — AI creative director with recursive self-assessment: 20+ methodologies (SIT, TRIZ, Bisociation, SCAMPER, Synectics), 3-axis evaluation calibrated against Cannes/D&AD/HumanKind, 5-phase process from...
  `B:\AI-Armory\skillz\open-design\creative-director`  ·  _tags:_ creative director, campaign concept, creative critique, cannes review, scamper
- **d3-visualization** — Teaches the agent to produce D3 charts and interactive data visualizations.
  `B:\AI-Armory\skillz\open-design\d3-visualization`  ·  _tags:_ d3, d3.js, interactive chart, data visualization, editorial chart, d3 bar chart, d3 line chart, d3 map, d3 force graph, d3 sankey, d3 treemap, d3 sunburst, d3 choropleth, d3 animation, d3 scroll, s...
- **data-report** — Turns CSV, Excel, or JSON data into a polished visual report page.
  `B:\AI-Armory\skillz\open-design\data-report`  ·  _tags:_ data, report, chart, 数据, 报告
- **deck-guizang-editorial** — Editorial magazine meets e-ink: 10 layouts and 5 palettes (Ink, Indigo Porcelain, Forest Ink, Kraft Paper, Dune).
  `B:\AI-Armory\skillz\open-design\deck-guizang-editorial`  ·  _tags:_ editorial, e-ink, magazine, narrative, guizang
- **deck-open-slide-canvas** — Locked 1920x1080 canvas deck with React component-level free composition, not bound to a fixed template.
  `B:\AI-Armory\skillz\open-design\deck-open-slide-canvas`  ·  _tags:_ canvas, open-slide, freeform, 1920, react
- **deck-swiss-international** — 16-column grid, one saturated accent, and 22 locked layouts (Klein Blue, Lemon, Mint, Safety Orange).
  `B:\AI-Armory\skillz\open-design\deck-swiss-international`  ·  _tags:_ swiss, grid, international, ikb, editorial, facts
- **design-brief** — Parse a structured design brief written in I-Lang protocol format into a concrete design spec.
  `B:\AI-Armory\skillz\open-design\design-brief`  ·  _tags:_ design brief, create a design brief, ilang brief, structured brief
- **design-consultation** — Build a complete design system from scratch with creative risks and realistic product mockups.
  `B:\AI-Armory\skillz\open-design\design-consultation`  ·  _tags:_ design consultation, design from scratch, design system kickoff, brand workshop
- **design-md** — Create and manage DESIGN.md files.
  `B:\AI-Armory\skillz\open-design\design-md`  ·  _tags:_ design.md, design doc, design tokens doc, visual rules doc
- **design-review** — Designer Who Codes: visual audit then fixes with atomic commits and before/after screenshots.
  `B:\AI-Armory\skillz\open-design\design-review`  ·  _tags:_ design review, visual audit, before after, pre launch design check
- **design-taste-frontend** — Anti-slop frontend skill for landing pages, portfolios, and redesigns.
  `B:\AI-Armory\skillz\open-design\taste-skill`  ·  _tags:_ design taste, anti slop frontend, premium landing page, portfolio redesign, visual taste
- **design-taste-frontend-v1** — The original v1 taste-skill, preserved for projects depending on its exact behavior.
  `B:\AI-Armory\skillz\open-design\taste-skill-v1`  ·  _tags:_ design taste v1, high agency frontend, anti slop v1, visual density
- **digits-fintech-swiss-template** — Swiss-grid fintech deck template in black / warm paper / neon-lime contrast.
  `B:\AI-Armory\skillz\open-design\digits-fintech-swiss-template`  ·  _tags:_ swiss fintech template, data-driven finance deck, neon lime editorial grid, high contrast strategy slides, 数字金融瑞士风模板
- **doc** — Read, create, and edit .docx documents with formatting and layout fidelity via OpenAI's document skill.
  `B:\AI-Armory\skillz\open-design\doc`  ·  _tags:_ openai doc, docx fidelity, word doc edit, layout doc
- **doc-kami-parchment** — Warm parchment canvas (#f5f4ed), monochrome ink-blue accent (#1B365D), one serif family, and editorial-grade typography.
  `B:\AI-Armory\skillz\open-design\doc-kami-parchment`  ·  _tags:_ kami, parchment, serif, editorial, report, letter, one-pager
- **docx** — Create, edit, and analyze Word documents with tracked changes, comments, and formatting.
  `B:\AI-Armory\skillz\open-design\docx`  ·  _tags:_ docx, word document, tracked changes, design brief doc, copy doc
- **domain-name-brainstormer** — Generate creative domain name ideas and check availability across multiple TLDs including .com, .io, .dev, and .ai.
  `B:\AI-Armory\skillz\open-design\domain-name-brainstormer`  ·  _tags:_ domain name, brainstorm domain, tld check, startup name, product name
- **ecommerce-image-workflow** — Reference-product ecommerce image workflow for generating a compact set of product-faithful main, feature, and lifestyle images from real product reference photos.
  `B:\AI-Armory\skillz\open-design\ecommerce-image-workflow`  ·  _tags:_ ecommerce product images, product image set, product photography workflow, product main image, product feature shot, reference product commerce images, lifestyle product image, amazon product image...
- **editorial-burgundy-principles-template** — Editorial studio deck template in burgundy / blush / muted-gold palette.
  `B:\AI-Armory\skillz\open-design\editorial-burgundy-principles-template`  ·  _tags:_ editorial burgundy template, studio salon deck, principles manifesto slides, pink burgundy premium presentation, 酒红粉金编辑风模板
- **emil-design-eng** — This skill encodes Emil Kowalski's philosophy on UI polish, component design, animation decisions, and the invisible details that make software feel great.
  `B:\AI-Armory\skillz\open-design\emil-design-eng`  ·  _tags:_ emil kowalski, design engineering, UI polish philosophy, animation philosophy, component design, invisible details, 界面哲学, 设计工程
- **emilkowalski-motion** — Motion-design follow-up skill inspired by Emil Kowalski's animation guidance.
  `B:\AI-Armory\skillz\open-design\emilkowalski-motion`  ·  _tags:_ emil kowalski, motion polish, micro interaction, interaction animation, tasteful animation, 动效润色
- **enhance-prompt** — Improve prompts with design specs and UI/UX vocabulary.
  `B:\AI-Armory\skillz\open-design\enhance-prompt`  ·  _tags:_ enhance prompt, design prompt, ui prompt, design vocabulary
- **export-download-debugging** — Diagnose and fix browser, preview, or Electron export/download failures, especially image export issues involving Save As, Blob/Data URLs, the File System Access API, createWritable failures, and 0...
  `B:\AI-Armory\skillz\open-design\export-download-debugging`  ·  _tags:_ export image failed, image export, download is 0kb, 0 KB file, showSaveFilePicker, createWritable, blob URL, Electron download
- **fal-3d** — Generate 3D models from text or images via fal.ai.
  `B:\AI-Armory\skillz\open-design\fal-3d`  ·  _tags:_ fal 3d, text to 3d, image to 3d, 3d model gen, game asset 3d
- **fal-generate** — Generate images and videos using fal.ai AI models.
  `B:\AI-Armory\skillz\open-design\fal-generate`  ·  _tags:_ fal generate, fal.ai image, flux image, sdxl, ideogram
- **fal-image-edit** — AI-powered image editing with style transfer, background removal, object removal, and inpainting via fal.ai hosted models.
  `B:\AI-Armory\skillz\open-design\fal-image-edit`  ·  _tags:_ fal image edit, inpaint, style transfer, background removal, object removal
- **fal-kling-o3** — Generate images and videos with Kling O3 — Kling's most powerful model family — via fal.ai.
  `B:\AI-Armory\skillz\open-design\fal-kling-o3`  ·  _tags:_ fal kling, kling o3, kling video, kling image
- **fal-lip-sync** — Create talking head videos and lip sync audio to video via fal.ai.
  `B:\AI-Armory\skillz\open-design\fal-lip-sync`  ·  _tags:_ lip sync, talking head, audio to video, avatar video, fal lipsync
- **fal-realtime** — Real-time and streaming AI image generation via fal.ai.
  `B:\AI-Armory\skillz\open-design\fal-realtime`  ·  _tags:_ fal realtime, streaming image, realtime image gen, moodboard
- **fal-restore** — Restore and fix image quality — deblur, denoise, fix faces, and restore old documents using fal.ai's hosted restoration models.
  `B:\AI-Armory\skillz\open-design\fal-restore`  ·  _tags:_ fal restore, restore image, deblur, denoise, fix faces, document restore
- **fal-train** — Train custom AI models (LoRA) on fal.ai for personalized image generation tailored to a brand, character, or style.
  `B:\AI-Armory\skillz\open-design\fal-train`  ·  _tags:_ fal train, train lora, custom model, personalized image gen, brand lora
- **fal-tryon** — Virtual try-on — see how clothes look on a person via fal.ai's hosted try-on models.
  `B:\AI-Armory\skillz\open-design\fal-tryon`  ·  _tags:_ virtual tryon, fal tryon, try on clothes, lookbook, ecommerce styling
- **fal-upscale** — Upscale and enhance image and video resolution using AI super-resolution models hosted on fal.ai.
  `B:\AI-Armory\skillz\open-design\fal-upscale`  ·  _tags:_ fal upscale, upscale image, super resolution, 4k upscale, enhance resolution
- **fal-video-edit** — Edit existing videos using AI — remix style, upscale, remove background, and add audio via fal.ai's hosted video models.
  `B:\AI-Armory\skillz\open-design\fal-video-edit`  ·  _tags:_ fal video edit, video upscale, video style transfer, remove video bg, video remix
- **fal-vision** — Analyze images — segment objects, detect, run OCR, describe, and answer visual questions via fal.ai vision models.
  `B:\AI-Armory\skillz\open-design\fal-vision`  ·  _tags:_ fal vision, image analysis, object detection, ocr image, visual qa, segment
- **faq-page** — A Frequently Asked Questions (FAQ) page with collapsible accordion sections, search functionality, and category filtering.
  `B:\AI-Armory\skillz\open-design\faq-page`  ·  _tags:_ faq, FAQ, frequently asked questions, help center, support page, Q&A, 常见问题, 帮助中心
- **field-notes-editorial-template** — Editorial "Field Notes" report template with soft paper background, serif hero typography, rounded pastel insight cards, and a retention chart panel.
  `B:\AI-Armory\skillz\open-design\field-notes-editorial-template`  ·  _tags:_ field notes editorial template, editorial report template, magazine style business report, pastel insight dashboard, 高级编辑风报告模板, 奶油底粉彩卡片数据报告
- **figma-code-connect-components** — Connect Figma design components to code components using Code Connect so design-system updates flow into the codebase automatically.
  `B:\AI-Armory\skillz\open-design\figma-code-connect-components`  ·  _tags:_ figma code connect, design to code, figma components, code connect
- **figma-create-design-system-rules** — Generate project-specific design system rules for Figma-to-code workflows.
  `B:\AI-Armory\skillz\open-design\figma-create-design-system-rules`  ·  _tags:_ figma rules, design system rules, figma to code rules, figma tokens
- **figma-create-new-file** — Create a new blank Figma Design or FigJam file.
  `B:\AI-Armory\skillz\open-design\figma-create-new-file`  ·  _tags:_ figma new file, figjam new, create figma file
- **figma-generate-design** — Build or update screens in Figma from code or description using design system components.
  `B:\AI-Armory\skillz\open-design\figma-generate-design`  ·  _tags:_ figma generate design, code to figma, screen generation, figma from code
- **figma-generate-library** — Build or update a professional-grade design system library in Figma from a codebase.
  `B:\AI-Armory\skillz\open-design\figma-generate-library`  ·  _tags:_ figma library, design system library, figma from codebase, sync figma
- **figma-implement-design** — Translate Figma designs into production-ready code with 1:1 visual fidelity.
  `B:\AI-Armory\skillz\open-design\figma-implement-design`  ·  _tags:_ figma to code, implement figma, figma fidelity, 1:1 figma
- **figma-use** — Run Figma Plugin API scripts for canvas writes, inspections, variables, and design-system work.
  `B:\AI-Armory\skillz\open-design\figma-use`  ·  _tags:_ figma use, figma plugin api, figma canvas, figma scripts
- **flutter-animating-apps** — Implement animated effects, transitions, and motion in Flutter apps.
  `B:\AI-Armory\skillz\open-design\flutter-animating-apps`  ·  _tags:_ flutter animation, flutter motion, mobile animation, flutter transitions
- **frame-data-chart-nyt** — NYT-newsroom typography, staggered reveal animation, and editorial-grade charts (line, bar, or range band).
  `B:\AI-Armory\skillz\open-design\frame-data-chart-nyt`  ·  _tags:_ data, chart, nyt, editorial, frame
- **frame-flowchart-sticky** — SVG curve connectors, sticky-note nodes, and cursor interaction with a whiteboard-brainstorm feel.
  `B:\AI-Armory\skillz\open-design\frame-flowchart-sticky`  ·  _tags:_ flowchart, diagram, sticky, whiteboard, frame
- **frame-glitch-title** — Digital glitch, chromatic offset, and data-corruption title frame for video transitions or cyberpunk heroes.
  `B:\AI-Armory\skillz\open-design\frame-glitch-title`  ·  _tags:_ glitch, cyberpunk, title, transition, vfx, frame
- **frame-light-leak-cinema** — Film light leaks, grain, 16:9 letterbox, and large serif type for cinematic openings or chapter cards.
  `B:\AI-Armory\skillz\open-design\frame-light-leak-cinema`  ·  _tags:_ cinema, film, light-leak, grain, letterbox, frame
- **frame-liquid-bg-hero** — WebGL-style fluid displacement background with a quote overlay, suited to video intros, landing heroes, or posters.
  `B:\AI-Armory\skillz\open-design\frame-liquid-bg-hero`  ·  _tags:_ liquid, fluid, background, hero, html-in-canvas, vfx
- **frame-logo-outro** — Segmented logo assembly, glow bloom, and tagline reveal for video outros or brand closing frames.
  `B:\AI-Armory\skillz\open-design\frame-logo-outro`  ·  _tags:_ logo, outro, branding, end-card, frame
- **frame-macos-notification** — Realistic macOS notification banner with app icon, title, and body, suited to video overlays or product teasers.
  `B:\AI-Armory\skillz\open-design\frame-macos-notification`  ·  _tags:_ macos, notification, banner, overlay, frame
- **frontend-design** — Create distinctive, production-grade frontend interfaces with strong visual direction, polished typography, considered layout, and working HTML/CSS/JS or framework code.
  `B:\AI-Armory\skillz\open-design\frontend-design`  ·  _tags:_ frontend design, ui design, ux design, web design, production ui, landing page, dashboard design, react component design
- **frontend-dev** — Full-stack frontend with cinematic animations, AI-generated media via MiniMax API, and generative art.
  `B:\AI-Armory\skillz\open-design\frontend-dev`  ·  _tags:_ frontend dev, cinematic frontend, generative web, hero page, showcase site
- **frontend-skill** — Create visually strong landing pages, websites, and app UIs with restrained composition.
  `B:\AI-Armory\skillz\open-design\frontend-skill`  ·  _tags:_ landing page, frontend playbook, ui composition, restrained ui
- **frontend-slides** — Generate animation-rich HTML presentations with visual style previews.
  `B:\AI-Armory\skillz\open-design\frontend-slides`  ·  _tags:_ html slides, animation slides, interactive deck, web ppt, reveal slides
- **full-output-enforcement** — Overrides default LLM truncation behavior.
  `B:\AI-Armory\skillz\open-design\output-skill`  ·  _tags:_ full output, no placeholders, complete code, unabridged implementation
- **full-page-screenshot** — Capture full-page screenshots of web pages via Chrome DevTools Protocol with zero dependencies.
  `B:\AI-Armory\skillz\open-design\full-page-screenshot`  ·  _tags:_ full page screenshot, long screenshot, devtools screenshot, web capture
- **gif-sticker-maker** — Convert photos into animated GIF stickers in Funko Pop / Pop Mart style via the MiniMax API.
  `B:\AI-Armory\skillz\open-design\gif-sticker-maker`  ·  _tags:_ gif sticker, funko sticker, animated sticker, pop mart, 表情包
- **gpt-taste** — Elite UX/UI & Advanced GSAP Motion Engineer.
  `B:\AI-Armory\skillz\open-design\gpt-tasteskill`  ·  _tags:_ gpt taste, codex frontend taste, gsap motion landing, premium codex UI
- **gsap-core** — Official GSAP skill for the core API — gsap.to(), from(), fromTo(), easing, duration, stagger, defaults, gsap.matchMedia() (responsive, prefers-reduced-motion).
  `B:\AI-Armory\skillz\open-design\gsap-core`  ·  _tags:_ gsap, gsap core, web animation, tween, easing
- **gsap-frameworks** — Official GSAP skill for Vue, Svelte, and other non-React frameworks — lifecycle, scoping selectors, cleanup on unmount.
  `B:\AI-Armory\skillz\open-design\gsap-frameworks`  ·  _tags:_ gsap vue, gsap svelte, nuxt animation, sveltekit animation, framework animation
- **gsap-performance** — Official GSAP skill for performance — prefer transforms, avoid layout thrashing, will-change, batching.
  `B:\AI-Armory\skillz\open-design\gsap-performance`  ·  _tags:_ gsap performance, animation jank, 60fps animation, will-change, layout thrashing
- **gsap-plugins** — Official GSAP skill for GSAP plugins — registration, ScrollToPlugin, ScrollSmoother, Flip, Draggable, Inertia, Observer, SplitText, ScrambleText, SVG and physics plugins, CustomEase, EasePack...
  `B:\AI-Armory\skillz\open-design\gsap-plugins`  ·  _tags:_ gsap plugins, gsap plugin registration, flip animation, draggable, morphsvg, splittext
- **gsap-react** — Official GSAP skill for React — useGSAP hook, refs, gsap.context(), cleanup.
  `B:\AI-Armory\skillz\open-design\gsap-react`  ·  _tags:_ gsap react, usegsap, react animation, gsap context, react motion
- **gsap-scrolltrigger** — Official GSAP skill for ScrollTrigger — scroll-linked animations, pinning, scrub, triggers.
  `B:\AI-Armory\skillz\open-design\gsap-scrolltrigger`  ·  _tags:_ scrolltrigger, scroll animation, gsap scroll, scroll pin, scroll scrub
- **gsap-timeline** — Official GSAP skill for timelines — gsap.timeline(), position parameter, nesting, playback.
  `B:\AI-Armory\skillz\open-design\gsap-timeline`  ·  _tags:_ gsap timeline, animation timeline, sequenced animation, motion choreography
- **gsap-utils** — Official GSAP skill for gsap.utils — clamp, mapRange, normalize, interpolate, random, snap, toArray, wrap, pipe.
  `B:\AI-Armory\skillz\open-design\gsap-utils`  ·  _tags:_ gsap utils, clamp animation value, maprange, snap animation, gsap random
- **hand-drawn-diagrams** — Generate hand-drawn Excalidraw diagrams from a prompt — animated SVG, hosted edit link, and PNG export.
  `B:\AI-Armory\skillz\open-design\hand-drawn-diagrams`  ·  _tags:_ excalidraw, hand drawn diagram, sketch diagram, whiteboard diagram
- **hatch-pet** — Create, repair, validate, preview, and package Codex-compatible animated pet spritesheets from character art, screenshots, generated images, or visual references.
  `B:\AI-Armory\skillz\open-design\hatch-pet`  ·  _tags:_ hatch a pet, hatch pet, codex pet, spritesheet pet, animated pet, 孵化宠物, 电子宠物
- **high-end-visual-design** — Teaches the AI to design like a high-end agency.
  `B:\AI-Armory\skillz\open-design\soft-skill`  ·  _tags:_ high end visual design, soft premium UI, luxury landing page, expensive website
- **html-ppt-retro-quarterly-review** — Retro Quarterly Review presentation template in a bold blue + orange editorial language.
  `B:\AI-Armory\skillz\open-design\html-ppt-retro-quarterly-review`  ·  _tags:_ retro quarterly review, quarterly review template, roadmap slide style, blue orange presentation, vintage business deck, 季度复盘复古风, 蓝橙复古汇报模板
- **image-enhancer** — Improve image and screenshot quality by enhancing resolution, sharpness, and clarity for professional presentations and documentation.
  `B:\AI-Armory\skillz\open-design\image-enhancer`  ·  _tags:_ enhance image, upscale image, image quality, sharpen, denoise
- **image-to-code** — Elite website image-to-code skill for Codex.
  `B:\AI-Armory\skillz\open-design\image-to-code-skill`  ·  _tags:_ image to code, reference image to frontend, generate then code, visual implementation
- **imagegen** — Generate and edit images using OpenAI's Image API for project assets — UI mockups, icons, illustrations, social cards, and visual references.
  `B:\AI-Armory\skillz\open-design\imagegen`  ·  _tags:_ generate image, create image, image gen, openai image, icon design, mockup
- **imagegen-frontend-mobile** — Elite mobile app image-generation skill for creating premium, app-native screen concepts and flows.
  `B:\AI-Armory\skillz\open-design\imagegen-frontend-mobile`  ·  _tags:_ mobile app image, mobile UI concept, ios app mockup, android app mockup
- **imagegen-frontend-web** — Elite frontend image-direction skill for generating premium, conversion-aware website design references.
  `B:\AI-Armory\skillz\open-design\imagegen-frontend-web`  ·  _tags:_ website image reference, landing page comp, web design reference, section images
- **imagen** — Generate images using Google Gemini's image generation API for UI mockups, icons, illustrations, and visual assets.
  `B:\AI-Armory\skillz\open-design\imagen`  ·  _tags:_ gemini image, imagen, google image gen, illustration, icon
- **impeccable-design-polish** — Follow-up design polish skill inspired by Impeccable.
  `B:\AI-Armory\skillz\open-design\impeccable-design-polish`  ·  _tags:_ impeccable, design polish, polish page, anti ai polish, critique design, animate page, harden ui, live review, 反 AI 味
- **industrial-brutalist-ui** — Raw mechanical interfaces fusing Swiss typographic print with military terminal aesthetics.
  `B:\AI-Armory\skillz\open-design\brutalist-skill`  ·  _tags:_ industrial brutalist UI, tactical telemetry, swiss industrial, brutalist interface
- **library-curator** — Search the OD Library (the global asset registry) and apply matching assets into the current project mid-task.
  `B:\AI-Armory\skillz\open-design\library-curator`  ·  _tags:_ from my library, library asset, use the image I captured, insert from library
- **login-flow** — Mobile login and authentication flow screens
  `B:\AI-Armory\skillz\open-design\login-flow`  ·  _tags:_ login, sign in, 注册登录, 登录注册, 手机号登录, 验证码登录, 密码登录
- **marketing-psychology** — Apply psychological principles and behavioral science to copy and design.
  `B:\AI-Armory\skillz\open-design\marketing-psychology`  ·  _tags:_ marketing psychology, behavioral copy, persuasion, framing, cognitive bias
- **minimalist-ui** — Clean editorial-style interfaces.
  `B:\AI-Armory\skillz\open-design\minimalist-skill`  ·  _tags:_ minimalist ui, editorial product UI, linear style, warm monochrome
- **minimax-docx** — Professional DOCX document creation and editing using OpenXML SDK.
  `B:\AI-Armory\skillz\open-design\minimax-docx`  ·  _tags:_ minimax docx, openxml docx, branded report, proposal doc, template authoring
- **minimax-pdf** — Generate, fill, and reformat PDFs with a token-based design system and 15 cover styles.
  `B:\AI-Armory\skillz\open-design\minimax-pdf`  ·  _tags:_ minimax pdf, branded pdf, cover style pdf, e-guide pdf, design system pdf
- **mockup-device-3d** — Static iPhone and MacBook 3D-style showcase with real HTML embedded on screens, glass-lens refraction, and 360-degree turntable composition.
  `B:\AI-Armory\skillz\open-design\mockup-device-3d`  ·  _tags:_ device, mockup, iphone, macbook, html-in-canvas, product
- **nanobanana-ppt** — AI-powered PPT generation with document analysis and styled images via the NanoBanana stack.
  `B:\AI-Armory\skillz\open-design\nanobanana-ppt`  ·  _tags:_ nanobanana ppt, ai ppt, styled ppt, document to ppt, banana ppt
- **paywall-upgrade-cro** — Design and optimize upgrade screens, paywalls, and upsell modals.
  `B:\AI-Armory\skillz\open-design\paywall-upgrade-cro`  ·  _tags:_ paywall, upgrade screen, cro paywall, upsell modal, pricing screen
- **pdf** — Extract text, create PDFs, and handle forms.
  `B:\AI-Armory\skillz\open-design\pdf`  ·  _tags:_ pdf, create pdf, pdf form, branded pdf, one pager
- **pixelbin-media** — Generate and edit images and videos with an 85+ API portfolio and build visually appealing website pages via Pixelbin.
  `B:\AI-Armory\skillz\open-design\pixelbin-media`  ·  _tags:_ pixelbin, media generation, image transform, video transform, cdn media
- **plan-design-review** — Senior Designer review: rates each design dimension 0-10, explains what a 10 looks like, and flags AI Slop signals.
  `B:\AI-Armory\skillz\open-design\plan-design-review`  ·  _tags:_ plan design review, senior designer review, design rating, ai slop check
- **platform-design** — 300+ design rules from Apple HIG, Material Design 3, and WCAG 2.2 for cross-platform apps.
  `B:\AI-Armory\skillz\open-design\platform-design`  ·  _tags:_ platform design, cross platform design, material design, hig rules, wcag rules
- **poster-hero** — Vertical poster or Moments-style share image with strong visual impact.
  `B:\AI-Armory\skillz\open-design\poster-hero`  ·  _tags:_ poster, 海报, 朋友圈
- **ppt-keynote** — Apple Keynote-quality slides, one card per screen, with keyboard left/right navigation.
  `B:\AI-Armory\skillz\open-design\ppt-keynote`  ·  _tags:_ slides, deck, presentation, 幻灯片, 演讲
- **pptx** — Read, generate, and adjust PowerPoint slides, layouts, and templates.
  `B:\AI-Armory\skillz\open-design\pptx`  ·  _tags:_ pptx, powerpoint, slide deck, create slides, edit pptx
- **pptx-generator** — Create and edit PowerPoint presentations from scratch with PptxGenJS — MiniMax's production-tested deck pipeline.
  `B:\AI-Armory\skillz\open-design\pptx-generator`  ·  _tags:_ pptx generator, minimax ppt, deck generator, auto pptx
- **pptx-html-fidelity-audit** — Audit a python-pptx export against its source HTML deck, identify layout/content drift (footer overflow, cropped content, missing italic/em, lost styling, off-rhythm spacing), and re-export with...
  `B:\AI-Armory\skillz\open-design\pptx-html-fidelity-audit`  ·  _tags:_ pptx fidelity, pptx audit, ppt 跑掉, 字型不對, footer overlap, verify pptx, html to pptx
- **pr-feedback-quality-gate** — Safely track pull request feedback, resolve review comments or merge conflicts, validate fixes, and use a read-only cross-review before committing or pushing follow-up changes.
  `B:\AI-Armory\skillz\open-design\pr-feedback-quality-gate`  ·  _tags:_ PR feedback, review comments, merge conflicts, cross-review, Claude CLI review, monitor PR
- **redesign-existing-projects** — Upgrades existing websites and apps to premium quality.
  `B:\AI-Armory\skillz\open-design\redesign-skill`  ·  _tags:_ redesign existing project, improve current UI, premium redesign, audit UI
- **reference-design-contract** — Turn vague taste, screenshots, URLs, product notes, or "make it feel like this" references into a grounded DESIGN.md plus an implementation handoff.
  `B:\AI-Armory\skillz\open-design\reference-design-contract`  ·  _tags:_ design contract, reference design brief, style contract, visual direction handoff, turn references into DESIGN.md, make it feel like this, 做同款但不照抄, 把参考图转成设计规范
- **release-notes-one-pager** — Release notes one-page HTML with highlights, Added, Fixed, Breaking changes, Known issues, and Upgrade note.
  `B:\AI-Armory\skillz\open-design\release-notes-one-pager`  ·  _tags:_ release notes, changelog, what's new, version update, change log, release summary
- **remotion** — Programmatic video creation with React.
  `B:\AI-Armory\skillz\open-design\remotion`  ·  _tags:_ remotion, react video, programmatic video, motion graphics, video composition
- **replicate** — Discover, compare, and run AI models using Replicate's API.
  `B:\AI-Armory\skillz\open-design\replicate`  ·  _tags:_ replicate, run ai model, model comparison, replicate api
- **research-decision-room** — Turn messy user research notes, interviews, support tickets, surveys, and product context into an evidence-backed decision room: a single HTML artifact with an evidence ledger, theme map, confidence...
  `B:\AI-Armory\skillz\open-design\research-decision-room`  ·  _tags:_ research decision room, user research synthesis, research synthesis dashboard, evidence-backed product decision, interview synthesis, opportunity solution tree, usability findings dashboard, qualit...
- **resume-modern** — Modern minimal resume, single A4 page, ready for print or PDF export.
  `B:\AI-Armory\skillz\open-design\resume-modern`  ·  _tags:_ resume, cv, 简历
- **review-animations** — Reviews animation and motion code against a high craft bar derived from Emil Kowalski's design engineering philosophy.
  `B:\AI-Armory\skillz\open-design\review-animations`  ·  _tags:_ review animations, animation review, motion review, audit animations, check motion code, animation craft, 动效审查
- **screenshot** — Capture desktop, app windows, or pixel regions across OS platforms.
  `B:\AI-Armory\skillz\open-design\screenshot`  ·  _tags:_ screenshot, capture screen, window screenshot, pixel region capture
- **screenshots-marketing** — Generate marketing screenshots with Playwright.
  `B:\AI-Armory\skillz\open-design\screenshots-marketing`  ·  _tags:_ marketing screenshot, playwright screenshot, hero shot, app store screenshot
- **shadcn-ui** — Build UI components with shadcn/ui.
  `B:\AI-Armory\skillz\open-design\shadcn-ui`  ·  _tags:_ shadcn, shadcn ui, shadcn components, accessible components
- **shader-dev** — GLSL shader techniques for ray marching, fluid simulation, particle systems, and procedural generation.
  `B:\AI-Armory\skillz\open-design\shader-dev`  ·  _tags:_ shader, glsl, ray marching, fluid simulation, procedural generation
- **slack-gif-creator** — Create animated GIFs optimized for Slack with validators for size constraints and composable animation primitives.
  `B:\AI-Armory\skillz\open-design\slack-gif-creator`  ·  _tags:_ slack gif, animated gif, reaction gif, tiny gif
- **slides** — Create and edit .pptx presentation decks with PptxGenJS.
  `B:\AI-Armory\skillz\open-design\slides`  ·  _tags:_ slides, pptxgenjs, sales deck, design showcase deck
- **social-reddit-card** — Realistic Reddit post card with vote rail and comment count, suited to video overlays or story sharing.
  `B:\AI-Armory\skillz\open-design\social-reddit-card`  ·  _tags:_ reddit, social, card, overlay, story
- **social-spotify-card** — Spotify Now Playing-style card with album art, progress bar, and playback controls, suited to video overlays or personal homepages.
  `B:\AI-Armory\skillz\open-design\social-spotify-card`  ·  _tags:_ spotify, music, now-playing, card, overlay
- **social-x-post-card** — Realistic X post card with engagement metrics (likes, reposts, views), suited to video overlays or shareable image cards.
  `B:\AI-Armory\skillz\open-design\social-x-post-card`  ·  _tags:_ twitter, x, social, card, overlay
- **sora** — Generate, remix, and manage short video clips via OpenAI's Sora API.
  `B:\AI-Armory\skillz\open-design\sora`  ·  _tags:_ sora, openai video, short video, b roll, cinematic clip
- **speech** — Generate spoken audio from text using OpenAI's API with built-in voices.
  `B:\AI-Armory\skillz\open-design\speech`  ·  _tags:_ openai speech, tts openai, narrated audio, voice over
- **stitch-design-taste** — Semantic Design System Skill for Google Stitch.
  `B:\AI-Armory\skillz\open-design\stitch-skill`  ·  _tags:_ stitch design taste, generate DESIGN.md, semantic design system, premium design system
- **stitch-loop** — Iterative design-to-code feedback loop.
  `B:\AI-Armory\skillz\open-design\stitch-loop`  ·  _tags:_ stitch loop, design to code, design iteration, fidelity loop
- **swiftui-design** — SwiftUI 前端设计 skill — anti AI-slop rules, design direction advisor, brand asset protocol, and five-dimension review.
  `B:\AI-Armory\skillz\open-design\swiftui-design`  ·  _tags:_ swiftui design, ios design, native ui design, apple frontend, swiftui slop
- **swiss-creative-mode-template** — Swiss-inspired creative-mode presentation template skill with bold editorial typography, high-contrast geometric cards, interactive slide navigation, theme switching, hotspot overlays, and palette...
  `B:\AI-Armory\skillz\open-design\swiss-creative-mode-template`  ·  _tags:_ swiss creative mode template, editorial presentation template, brutalist deck style html, creative mode deck, 瑞士风演示模板, 高级设计语言模板
- **swiss-user-research-video-template** — Swiss-style user-research narrative template in warm-paper editorial aesthetics.
  `B:\AI-Armory\skillz\open-design\swiss-user-research-video-template`  ·  _tags:_ swiss user research template, editorial research deck template, minimal user research slides, warm paper swiss style, research synthesis template, 瑞士风用户研究模板, 高级调性研究汇报
- **theme-factory** — Apply professional font and color themes to artifacts including slides, docs, reports, and HTML landing pages.
  `B:\AI-Armory\skillz\open-design\theme-factory`  ·  _tags:_ theme factory, apply theme, design theme, theme generator, preset theme
- **threejs** — Three.js skills for creating 3D elements and interactive experiences in the browser — scenes, materials, controls, and post-processing.
  `B:\AI-Armory\skillz\open-design\threejs`  ·  _tags:_ threejs, three.js, 3d web, webgl scene, 3d interactive
- **ui-skills** — Opinionated, evolving constraints to guide agents when building interfaces.
  `B:\AI-Armory\skillz\open-design\ui-skills`  ·  _tags:_ ui constraints, ui guide, opinionated ui, ui rules
- **ui-ux-pro-max** — Catalog-only UI/UX Pro Max entry.
  `B:\AI-Armory\skillz\open-design\ui-ux-pro-max`  ·  _tags:_ ui ux patterns, design patterns, ux heuristics, usability
- **venice-audio-music** — Music generation queueing, retrieval, and completion endpoints via Venice.ai.
  `B:\AI-Armory\skillz\open-design\venice-audio-music`  ·  _tags:_ venice music, music gen, jingle, background loop, score
- **venice-audio-speech** — Text-to-speech models, voices, formats, and streaming via Venice.ai.
  `B:\AI-Armory\skillz\open-design\venice-audio-speech`  ·  _tags:_ tts, venice speech, text to speech, voiceover, narration
- **venice-image-edit** — Image edits, upscaling, and background removal via the Venice.ai API.
  `B:\AI-Armory\skillz\open-design\venice-image-edit`  ·  _tags:_ venice image edit, venice upscale, venice background removal
- **venice-image-generate** — Image generation endpoints and available styles via the Venice.ai API.
  `B:\AI-Armory\skillz\open-design\venice-image-generate`  ·  _tags:_ venice image, venice generate, venice ai image
- **venice-video** — Video generation and transcription workflows via the Venice.ai API.
  `B:\AI-Armory\skillz\open-design\venice-video`  ·  _tags:_ venice video, venice video gen, venice transcribe
- **vfx-text-cursor** — Cursor light trail, chromatic rays, and directional flares for word-by-word quote reveals in video intros.
  `B:\AI-Armory\skillz\open-design\vfx-text-cursor`  ·  _tags:_ vfx, text, cursor, chromatic, reveal, frame
- **video-downloader** — Download videos from YouTube and other platforms for offline viewing, editing, or archival with support for various formats and quality options.
  `B:\AI-Armory\skillz\open-design\video-downloader`  ·  _tags:_ download video, youtube download, archive video, offline video
- **video-hyperframes** — Hyperframes / Remotion-compatible continuous frame animation with autoplay support.
  `B:\AI-Armory\skillz\open-design\video-hyperframes`  ·  _tags:_ video, hyperframes, remotion, 视频
- **web-artifacts-builder** — Build complex claude.ai HTML artifacts with React and Tailwind.
  `B:\AI-Armory\skillz\open-design\web-artifacts-builder`  ·  _tags:_ web artifacts, tailwind artifact, react artifact, anthropic artifact
- **web-clone** — 网站复刻 / 克隆方法论。USE WHEN 用户说 复刻网站、克隆网站、clone website、抄个站、仿站、 照着这个站做一个、reproduce site、还原某个网页效果、把这个站搬下来改成我的、 复刻某个交互/WebGL/Canvas/Three.js 效果。提供「先拿真源码 → 判路径 → 逆向拆解 → 搭工程 → 替换内容」的可移植决策树，覆盖静态站 /...
  `B:\AI-Armory\skillz\open-design\web-clone`  ·  _tags:_ 网站复刻, 复刻网站, clone website, reproduce site, 仿站
- **web-design-guidelines** — Review UI code for Web Interface Guidelines compliance by the Vercel engineering team.
  `B:\AI-Armory\skillz\open-design\web-design-guidelines`  ·  _tags:_ web design guidelines, vercel design, product ui standards, design checklist, review my UI, check accessibility, audit design, review UX, 设计审查
- **weread-year-in-review-video-template** — WeRead-inspired HyperFrames video template for vertical annual reading reports, personal reading dashboards, book-note recaps, and shareable year-in-review stories.
  `B:\AI-Armory\skillz\open-design\weread-year-in-review-video-template`  ·  _tags:_ WeRead year in review, WeRead annual report, reading year in review video, annual reading report template, 微信读书年度报告, 读书年度总结视频, 阅读年报 HyperFrames
- **wpds** — WordPress Design System.
  `B:\AI-Armory\skillz\open-design\wpds`  ·  _tags:_ wpds, wordpress design, wp tokens, wp design system
- **writing-guidelines** — Review docs/prose for Writing Guidelines compliance.
  `B:\AI-Armory\skillz\open-design\writing-guidelines`  ·  _tags:_ review my docs, check writing style, audit prose, review docs voice and tone, writing handbook, 文档审查
- **youtube-clipper** — YouTube clip generation and editing with automated workflows — pull source video, slice highlights, add captions, and export.
  `B:\AI-Armory\skillz\open-design\youtube-clipper`  ·  _tags:_ youtube clip, video clip, highlight reel, auto caption clip

</details>

<details><summary><b>gstack</b> (55 skills)</summary>

- **autoplan** — Auto-review pipeline — reads the full CEO, design, eng, and DX review skills from disk and runs them sequentially with auto-decisions using 6 decision principles. (gstack)
  `B:\AI-Armory\skillz\gstack\autoplan`  ·  _tags:_ run all reviews, automatic review pipeline, auto plan review
- **browse** — Fast headless browser for QA testing and site dogfooding. (gstack)
  `B:\AI-Armory\skillz\gstack\browse`  ·  _tags:_ browse a page, headless browser, take page screenshot
- **careful** — Safety guardrails for destructive commands. (gstack)
  `B:\AI-Armory\skillz\gstack\careful`  ·  _tags:_ be careful, warn before destructive, safety mode
- **context-restore** — Restore working context saved earlier by /context-save. (gstack)
  `B:\AI-Armory\skillz\gstack\context-restore`  ·  _tags:_ resume where i left off, restore context, where was i, pick up where i left off, context restore
- **context-save** — Save working context. (gstack)
  `B:\AI-Armory\skillz\gstack\context-save`  ·  _tags:_ save progress, save state, save my work, context save
- **cso** — Chief Security Officer mode. (gstack)
  `B:\AI-Armory\skillz\gstack\cso`  ·  _tags:_ security audit, check for vulnerabilities, owasp review
- **design-consultation** — Design consultation: understands your product, researches the landscape, proposes a complete design system (aesthetic, typography, color, layout, spacing, motion), and generates font+color preview......
  `B:\AI-Armory\skillz\gstack\design-consultation`  ·  _tags:_ design system, create a brand, design from scratch
- **design-html** — Design finalization: generates production-quality Pretext-native HTML/CSS. (gstack)
  `B:\AI-Armory\skillz\gstack\design-html`  ·  _tags:_ build the design, code the mockup, make design real
- **design-review** — Designer's eye QA: finds visual inconsistency, spacing issues, hierarchy problems, AI slop patterns, and slow interactions — then fixes them. (gstack)
  `B:\AI-Armory\skillz\gstack\design-review`  ·  _tags:_ visual design audit, design qa, fix design issues
- **design-shotgun** — Design shotgun: generate multiple AI design variants, open a comparison board, collect structured feedback, and iterate. (gstack)
  `B:\AI-Armory\skillz\gstack\design-shotgun`  ·  _tags:_ explore design variants, show me design options, visual design brainstorm
- **devex-review** — Live developer experience audit. (gstack)
  `B:\AI-Armory\skillz\gstack\devex-review`  ·  _tags:_ live dx audit, test developer experience, measure onboarding time
- **diagram** — Turn an English description (or mermaid source) into a diagram triplet: the source, an editable .excalidraw file you can open (gstack)
  `B:\AI-Armory\skillz\gstack\diagram`  ·  _tags:_ make a diagram, draw a diagram, create a flowchart, diagram this, visualize this flow, architecture diagram
- **document-generate** — Generate missing documentation from scratch for a feature, module, or entire project. (gstack)
  `B:\AI-Armory\skillz\gstack\document-generate`  ·  _tags:_ write docs for this, generate documentation, document this feature, create a tutorial, write a how-to, explain this module, docs for this project
- **document-release** — Post-ship documentation update. (gstack)
  `B:\AI-Armory\skillz\gstack\document-release`  ·  _tags:_ update docs after ship, document what changed, post-ship docs
- **freeze** — Restrict file edits to a specific directory for the session. (gstack)
  `B:\AI-Armory\skillz\gstack\freeze`  ·  _tags:_ freeze edits to directory, lock editing scope, restrict file changes
- **gstack** — Router for the gstack skill suite. (gstack)
  `B:\AI-Armory\skillz\gstack`  ·  _tags:_ gstack, which gstack skill, route this with gstack
- **gstack-openclaw-ceo-review** — Use when asked to review a plan, challenge a proposal, run a CEO review, poke holes in an approach, think bigger about scope, or decide whether to expand or reduce the plan.
  `B:\AI-Armory\skillz\gstack\openclaw\skills\gstack-openclaw-ceo-review`
- **gstack-openclaw-investigate** — Use when asked to debug, fix a bug, investigate an error, or do root cause analysis, and when users report errors, stack traces, unexpected behavior, or say something stopped working.
  `B:\AI-Armory\skillz\gstack\openclaw\skills\gstack-openclaw-investigate`
- **gstack-openclaw-office-hours** — Use when asked to brainstorm, evaluate whether an idea is worth building, run office hours, or think through a new product idea or design direction before any code is written.
  `B:\AI-Armory\skillz\gstack\openclaw\skills\gstack-openclaw-office-hours`
- **gstack-openclaw-retro** — Weekly engineering retrospective.
  `B:\AI-Armory\skillz\gstack\openclaw\skills\gstack-openclaw-retro`
- **gstack-upgrade** — Upgrade gstack to the latest version.
  `B:\AI-Armory\skillz\gstack\gstack-upgrade`  ·  _tags:_ upgrade gstack, update gstack version, get latest gstack
- **guard** — Full safety mode: destructive command warnings + directory-scoped edits. (gstack)
  `B:\AI-Armory\skillz\gstack\guard`  ·  _tags:_ full safety mode, guard against mistakes, maximum safety
- **hackernews-frontpage** — Scrape the Hacker News front page (titles, points, comment counts).
  `B:\AI-Armory\skillz\gstack\browser-skills\hackernews-frontpage`  ·  _tags:_ scrape hacker news frontpage, scrape hn frontpage, get hn top stories, latest hacker news stories
- **health** — Code quality dashboard. (gstack)
  `B:\AI-Armory\skillz\gstack\health`  ·  _tags:_ code health check, quality dashboard, how healthy is codebase
- **investigate** — Systematic debugging with root cause investigation. (gstack)
  `B:\AI-Armory\skillz\gstack\investigate`  ·  _tags:_ debug this, fix this bug, why is this broken, root cause analysis, investigate this error
- **ios-clean** — Remove the DebugBridge SPM package and all #if DEBUG wiring from an iOS app. (gstack)
  `B:\AI-Armory\skillz\gstack\ios-clean`  ·  _tags:_ clean the ios debug bridge, remove debugbridge, strip the gstack ios instrumentation
- **ios-design-review** — Visual design audit for iOS apps on real hardware. (gstack)
  `B:\AI-Armory\skillz\gstack\ios-design-review`  ·  _tags:_ review the ios design, audit the iphone app visuals, design qa the ios app
- **ios-fix** — Autonomous iOS bug fixer. (gstack)
  `B:\AI-Armory\skillz\gstack\ios-fix`  ·  _tags:_ fix this ios bug, patch the iphone app, auto-fix the ios issue
- **ios-qa** — Live-device iOS QA for SwiftUI apps. (gstack)
  `B:\AI-Armory\skillz\gstack\ios-qa`  ·  _tags:_ ios qa, test the iphone app, test my ios app, find bugs on the device, qa the ios app
- **ios-sync** — Regenerate the iOS debug bridge against the latest upstream gstack templates. (gstack)
  `B:\AI-Armory\skillz\gstack\ios-sync`  ·  _tags:_ resync the ios debug bridge, regenerate ios accessors, update the gstack ios instrumentation
- **land-and-deploy** — Land and deploy workflow. (gstack)
  `B:\AI-Armory\skillz\gstack\land-and-deploy`  ·  _tags:_ merge and deploy, land the pr, ship to production
- **landing-report** — Read-only queue dashboard for workspace-aware ship. (gstack)
  `B:\AI-Armory\skillz\gstack\landing-report`  ·  _tags:_ landing report, version queue, ship queue, what version comes next, show open PR versions
- **learn** — Manage project learnings.
  `B:\AI-Armory\skillz\gstack\learn`  ·  _tags:_ show learnings, what have we learned, manage project learnings
- **make-pdf** — Turn any markdown file into a publication-quality PDF. (gstack)
  `B:\AI-Armory\skillz\gstack\make-pdf`  ·  _tags:_ markdown to pdf, generate pdf, make pdf, export pdf
- **office-hours** — YC Office Hours — two modes. (gstack)
  `B:\AI-Armory\skillz\gstack\office-hours`  ·  _tags:_ brainstorm this, is this worth building, help me think through, office hours
- **open-gstack-browser** — Launch GStack Browser — AI-controlled Chromium with the sidebar extension baked in.
  `B:\AI-Armory\skillz\gstack\open-gstack-browser`  ·  _tags:_ open gstack browser, launch chromium, show me the browser
- **pair-agent** — Pair a remote AI agent with your browser. (gstack)
  `B:\AI-Armory\skillz\gstack\pair-agent`  ·  _tags:_ pair with agent, connect remote agent, share my browser
- **plan-ceo-review** — CEO/founder-mode plan review. (gstack)
  `B:\AI-Armory\skillz\gstack\plan-ceo-review`  ·  _tags:_ think bigger, expand scope, strategy review, rethink this plan
- **plan-design-review** — Designer's eye plan review — interactive, like CEO and Eng review. (gstack)
  `B:\AI-Armory\skillz\gstack\plan-design-review`  ·  _tags:_ design plan review, review ux plan, check design decisions
- **plan-devex-review** — Interactive developer experience plan review. (gstack)
  `B:\AI-Armory\skillz\gstack\plan-devex-review`  ·  _tags:_ developer experience review, dx plan review, check developer onboarding
- **plan-eng-review** — Eng manager-mode plan review. (gstack)
  `B:\AI-Armory\skillz\gstack\plan-eng-review`  ·  _tags:_ review architecture, eng plan review, check the implementation plan
- **plan-tune** — Self-tuning question sensitivity + developer psychographic for gstack (v1: observational). (gstack)
  `B:\AI-Armory\skillz\gstack\plan-tune`  ·  _tags:_ tune questions, stop asking me that, too many questions, show my profile, show my vibe, developer profile, turn off question tuning
- **qa** — Systematically QA test a web application and fix bugs found. (gstack)
  `B:\AI-Armory\skillz\gstack\qa`  ·  _tags:_ qa test this, find bugs on site, test the site
- **qa-only** — Report-only QA testing. (gstack)
  `B:\AI-Armory\skillz\gstack\qa-only`  ·  _tags:_ qa report only, just report bugs, test but dont fix
- **retro** — Weekly engineering retrospective. (gstack)
  `B:\AI-Armory\skillz\gstack\retro`  ·  _tags:_ weekly retro, what did we ship, engineering retrospective
- **review** — Pre-landing PR review. (gstack)
  `B:\AI-Armory\skillz\gstack\review`  ·  _tags:_ review this pr, code review, check my diff, pre-landing review
- **scrape** — Pull data from a web page. (gstack)
  `B:\AI-Armory\skillz\gstack\scrape`  ·  _tags:_ scrape this page, get data from, pull from, extract from, what is on
- **setup-browser-cookies** — Import cookies from your real Chromium browser into the headless browse session. (gstack)
  `B:\AI-Armory\skillz\gstack\setup-browser-cookies`  ·  _tags:_ import browser cookies, login to test site, setup authenticated session
- **setup-deploy** — Configure deployment settings for /land-and-deploy.
  `B:\AI-Armory\skillz\gstack\setup-deploy`  ·  _tags:_ configure deploy, setup deployment, set deploy platform
- **setup-gbrain** — Set up gbrain for this coding agent: install the CLI, initialize a local PGLite or Supabase brain, register MCP, capture per-remote trust policy. (gstack)
  `B:\AI-Armory\skillz\gstack\setup-gbrain`  ·  _tags:_ setup gbrain, install gbrain, connect gbrain, start gbrain, configure gbrain
- **ship** — Ship workflow: detect + merge base branch, run tests, review diff, bump VERSION, update CHANGELOG, commit, push, create PR. (gstack)
  `B:\AI-Armory\skillz\gstack\ship`  ·  _tags:_ ship it, create a pr, push to main, deploy this
- **skillify** — Codify the most recent successful /scrape flow into a permanent browser-skill on disk. (gstack)
  `B:\AI-Armory\skillz\gstack\skillify`  ·  _tags:_ skillify, codify this scrape, save this scrape, make this permanent
- **spec** — Turn vague intent into a precise, executable spec in five phases. (gstack)
  `B:\AI-Armory\skillz\gstack\spec`  ·  _tags:_ spec this out, file an issue, write up a ticket, turn this into an issue, make this a github issue, turn this into a backlog item
- **sync-gbrain** — Keep gbrain current with this repo's code and refresh agent search guidance in CLAUDE.md.
  `B:\AI-Armory\skillz\gstack\sync-gbrain`  ·  _tags:_ sync gbrain, refresh gbrain, reindex repo, update gbrain
- **unfreeze** — Clear the freeze boundary set by /freeze, allowing edits to all directories again. (gstack)
  `B:\AI-Armory\skillz\gstack\unfreeze`  ·  _tags:_ unfreeze edits, unlock all directories, remove edit restrictions

</details>

<details><summary><b>skills-repo</b> (39 skills)</summary>

- **ask-matt** — Ask which skill or flow fits your situation.
  `B:\AI-Armory\skillz\skills-repo\engineering\ask-matt`
- **claude-handoff** — Hand the current conversation off to a fresh background agent that picks up the work immediately.
  `B:\AI-Armory\skillz\skills-repo\in-progress\claude-handoff`
- **code-review** — Review the changes since a fixed point (commit, branch, tag, or merge-base) along two axes — Standards (does the code follow this repo's documented coding standards?) and Spec (does the code match...
  `B:\AI-Armory\skillz\skills-repo\engineering\code-review`
- **codebase-design** — Shared vocabulary for designing deep modules.
  `B:\AI-Armory\skillz\skills-repo\engineering\codebase-design`
- **design-an-interface** — Generate multiple radically different interface designs for a module using parallel sub-agents.
  `B:\AI-Armory\skillz\skills-repo\deprecated\design-an-interface`
- **diagnosing-bugs** — Diagnosis loop for hard bugs and performance regressions.
  `B:\AI-Armory\skillz\skills-repo\engineering\diagnosing-bugs`
- **domain-modeling** — Build and sharpen a project's domain model.
  `B:\AI-Armory\skillz\skills-repo\engineering\domain-modeling`
- **edit-article** — Edit and improve articles by restructuring sections, improving clarity, and tightening prose.
  `B:\AI-Armory\skillz\skills-repo\personal\edit-article`
- **git-guardrails-claude-code** — Set up Claude Code hooks to block dangerous git commands (push, reset --hard, clean, branch -D, etc.) before they execute.
  `B:\AI-Armory\skillz\skills-repo\misc\git-guardrails-claude-code`
- **grill-me** — A relentless interview to sharpen a plan or design.
  `B:\AI-Armory\skillz\skills-repo\productivity\grill-me`
- **grill-with-docs** — A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as we go.
  `B:\AI-Armory\skillz\skills-repo\engineering\grill-with-docs`
- **grilling** — Grill the user relentlessly about a plan or design.
  `B:\AI-Armory\skillz\skills-repo\productivity\grilling`
- **handoff** — Compact the current conversation into a handoff document for another agent to pick up.
  `B:\AI-Armory\skillz\skills-repo\productivity\handoff`
- **implement** — Implement a piece of work based on a spec or set of tickets.
  `B:\AI-Armory\skillz\skills-repo\engineering\implement`
- **improve-codebase-architecture** — Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick.
  `B:\AI-Armory\skillz\skills-repo\engineering\improve-codebase-architecture`
- **loop-me** — Grill me about specs for the workflows I want to build, within this workspace.
  `B:\AI-Armory\skillz\skills-repo\in-progress\loop-me`
- **migrate-to-shoehorn** — Migrate test files from `as` type assertions to @total-typescript/shoehorn.
  `B:\AI-Armory\skillz\skills-repo\misc\migrate-to-shoehorn`
- **obsidian-vault** — Search, create, and manage notes in the Obsidian vault with wikilinks and index notes.
  `B:\AI-Armory\skillz\skills-repo\personal\obsidian-vault`
- **prototype** — Build a throwaway prototype to answer a design question.
  `B:\AI-Armory\skillz\skills-repo\engineering\prototype`
- **qa** — Interactive QA session where user reports bugs or issues conversationally, and the agent files GitHub issues.
  `B:\AI-Armory\skillz\skills-repo\deprecated\qa`
- **request-refactor-plan** — Create a detailed refactor plan with tiny commits via user interview, then file it as a GitHub issue.
  `B:\AI-Armory\skillz\skills-repo\deprecated\request-refactor-plan`
- **research** — Investigate a question against high-trust primary sources and capture the findings as a Markdown file in the repo.
  `B:\AI-Armory\skillz\skills-repo\engineering\research`
- **resolving-merge-conflicts** — Use when you need to resolve an in-progress git merge/rebase conflict.
  `B:\AI-Armory\skillz\skills-repo\engineering\resolving-merge-conflicts`
- **scaffold-exercises** — Create exercise directory structures with sections, problems, solutions, and explainers that pass linting.
  `B:\AI-Armory\skillz\skills-repo\misc\scaffold-exercises`
- **setup-matt-pocock-skills** — Configure this repo for the engineering skills — set up its issue tracker, triage label vocabulary, and domain doc layout.
  `B:\AI-Armory\skillz\skills-repo\engineering\setup-matt-pocock-skills`
- **setup-pre-commit** — Set up Husky pre-commit hooks with lint-staged (Prettier), type checking, and tests in the current repo.
  `B:\AI-Armory\skillz\skills-repo\misc\setup-pre-commit`
- **setup-ts-deep-modules** — Wire dependency-cruiser into a TypeScript repo so each package is a deep module — implementation hidden in subfolders, reachable only through its entry-point files.
  `B:\AI-Armory\skillz\skills-repo\in-progress\setup-ts-deep-modules`
- **tdd** — Test-driven development.
  `B:\AI-Armory\skillz\skills-repo\engineering\tdd`
- **teach** — Teach the user a new skill or concept, within this workspace.
  `B:\AI-Armory\skillz\skills-repo\productivity\teach`
- **to-spec** — Turn the current conversation into a spec and publish it to the project issue tracker — no interview, just synthesis of what you've already discussed.
  `B:\AI-Armory\skillz\skills-repo\engineering\to-spec`
- **to-tickets** — Break a plan, spec, or the current conversation into a set of tracer-bullet tickets, each declaring its blocking edges, published to the configured tracker — edges as text in one file per ticket...
  `B:\AI-Armory\skillz\skills-repo\engineering\to-tickets`
- **triage** — Move issues and external PRs through a state machine of triage roles — categorise, verify, grill if needed, and write agent-ready briefs.
  `B:\AI-Armory\skillz\skills-repo\engineering\triage`
- **ubiquitous-language** — Extract a DDD-style ubiquitous language glossary from the current conversation, flagging ambiguities and proposing canonical terms.
  `B:\AI-Armory\skillz\skills-repo\deprecated\ubiquitous-language`
- **wayfinder** — Plan a huge chunk of work — more than one agent session can hold — as a shared map of investigation tickets on your issue tracker, and resolve them one at a time until the way to the destination is...
  `B:\AI-Armory\skillz\skills-repo\engineering\wayfinder`
- **wizard** — Generate an interactive bash wizard that walks a human through a manual procedure — third-party setup, a one-off migration, an A→B state transition — opening URLs, capturing values, confirming each...
  `B:\AI-Armory\skillz\skills-repo\in-progress\wizard`
- **writing-beats** — Writing, exploit — assemble raw material into a journey of beats, grounding each term before a beat leans on it.
  `B:\AI-Armory\skillz\skills-repo\in-progress\writing-beats`
- **writing-fragments** — Writing, explore — mine raw fragments, no structure yet.
  `B:\AI-Armory\skillz\skills-repo\in-progress\writing-fragments`
- **writing-great-skills** — Reference for writing and editing skills well — the vocabulary and principles that make a skill predictable.
  `B:\AI-Armory\skillz\skills-repo\productivity\writing-great-skills`
- **writing-shape** — Writing, exploit — shape raw material into an article, paragraph by paragraph.
  `B:\AI-Armory\skillz\skills-repo\in-progress\writing-shape`

</details>

<details><summary><b>taste-skill</b> (13 skills)</summary>

- **brandkit** — Premium brand-kit image generation skill for creating high-end brand-guidelines boards, logo systems, identity decks, and visual-world presentations.
  `B:\AI-Armory\skillz\taste-skill\brandkit`
- **design-taste-frontend** — Anti-slop frontend skill for landing pages, portfolios, and redesigns.
  `B:\AI-Armory\skillz\taste-skill\taste-skill`
- **design-taste-frontend-v1** — The original v1 taste-skill, preserved for projects depending on its exact behavior.
  `B:\AI-Armory\skillz\taste-skill\taste-skill-v1`
- **full-output-enforcement** — Overrides default LLM truncation behavior.
  `B:\AI-Armory\skillz\taste-skill\output-skill`
- **gpt-taste** — Elite UX/UI & Advanced GSAP Motion Engineer.
  `B:\AI-Armory\skillz\taste-skill\gpt-tasteskill`
- **high-end-visual-design** — Teaches the AI to design like a high-end agency.
  `B:\AI-Armory\skillz\taste-skill\soft-skill`
- **image-to-code** — Elite website image-to-code skill for Codex.
  `B:\AI-Armory\skillz\taste-skill\image-to-code-skill`
- **imagegen-frontend-mobile** — Elite mobile app image-generation skill for creating premium, app-native screen concepts and flows.
  `B:\AI-Armory\skillz\taste-skill\imagegen-frontend-mobile`
- **imagegen-frontend-web** — Elite frontend image-direction skill for generating premium, conversion-aware website design references.
  `B:\AI-Armory\skillz\taste-skill\imagegen-frontend-web`
- **industrial-brutalist-ui** — Raw mechanical interfaces fusing Swiss typographic print with military terminal aesthetics.
  `B:\AI-Armory\skillz\taste-skill\brutalist-skill`
- **minimalist-ui** — Clean editorial-style interfaces.
  `B:\AI-Armory\skillz\taste-skill\minimalist-skill`
- **redesign-existing-projects** — Upgrades existing websites and apps to premium quality.
  `B:\AI-Armory\skillz\taste-skill\redesign-skill`
- **stitch-design-taste** — Semantic Design System Skill for Google Stitch.
  `B:\AI-Armory\skillz\taste-skill\stitch-skill`

</details>

<details><summary><b>ui-ux-pro-max-skill</b> (13 skills)</summary>

- **banner-design** — Design banners for social media, ads, website heroes, creative assets, and print.
  `B:\AI-Armory\skillz\ui-ux-pro-max-skill\.claude\skills\banner-design`
- **banner-design** — Design banners for social media, ads, website heroes, creative assets, and print.
  `B:\AI-Armory\skillz\ui-ux-pro-max-skill\cli\assets\skills\banner-design`
- **brand** — Brand voice, visual identity, messaging frameworks, asset management, brand consistency.
  `B:\AI-Armory\skillz\ui-ux-pro-max-skill\.claude\skills\brand`
- **brand** — Brand voice, visual identity, messaging frameworks, asset management, brand consistency.
  `B:\AI-Armory\skillz\ui-ux-pro-max-skill\cli\assets\skills\brand`
- **design** — Comprehensive design skill: brand identity, design tokens, UI styling, logo generation (55 styles, Gemini AI), corporate identity program (50 deliverables, CIP mockups), HTML presentations...
  `B:\AI-Armory\skillz\ui-ux-pro-max-skill\.claude\skills\design`
- **design** — Comprehensive design skill: brand identity, design tokens, UI styling, logo generation (55 styles, Gemini AI), corporate identity program (50 deliverables, CIP mockups), HTML presentations...
  `B:\AI-Armory\skillz\ui-ux-pro-max-skill\cli\assets\skills\design`
- **design-system** — Token architecture, component specifications, and slide generation.
  `B:\AI-Armory\skillz\ui-ux-pro-max-skill\.claude\skills\design-system`
- **design-system** — Token architecture, component specifications, and slide generation.
  `B:\AI-Armory\skillz\ui-ux-pro-max-skill\cli\assets\skills\design-system`
- **slides** — Create strategic HTML presentations with Chart.js, design tokens, responsive layouts, copywriting formulas, and contextual slide strategies.
  `B:\AI-Armory\skillz\ui-ux-pro-max-skill\.claude\skills\slides`
- **slides** — Create strategic HTML presentations with Chart.js, design tokens, responsive layouts, copywriting formulas, and contextual slide strategies.
  `B:\AI-Armory\skillz\ui-ux-pro-max-skill\cli\assets\skills\slides`
- **ui-styling** — Create beautiful, accessible user interfaces with shadcn/ui components (built on Radix UI + Tailwind), Tailwind CSS utility-first styling, and canvas-based visual designs.
  `B:\AI-Armory\skillz\ui-ux-pro-max-skill\.claude\skills\ui-styling`
- **ui-styling** — Create beautiful, accessible user interfaces with shadcn/ui components (built on Radix UI + Tailwind), Tailwind CSS utility-first styling, and canvas-based visual designs.
  `B:\AI-Armory\skillz\ui-ux-pro-max-skill\cli\assets\skills\ui-styling`
- **ui-ux-pro-max** — UI/UX design intelligence for web and mobile.
  `B:\AI-Armory\skillz\ui-ux-pro-max-skill\.claude\skills\ui-ux-pro-max`

</details>

<details><summary><b>ponytail</b> (6 skills)</summary>

- **ponytail** — Forces the laziest solution that actually works, simplest, shortest, most minimal.
  `B:\AI-Armory\skillz\ponytail\ponytail`
- **ponytail-audit** — Whole-repo audit for over-engineering.
  `B:\AI-Armory\skillz\ponytail\ponytail-audit`
- **ponytail-debt** — Harvest every `ponytail:` comment in the codebase into a debt ledger, so the deliberate shortcuts and deferrals ponytail leaves behind get tracked instead of rotting into "later means never".
  `B:\AI-Armory\skillz\ponytail\ponytail-debt`
- **ponytail-gain** — Show ponytail's measured impact as a compact scoreboard: less code, less cost, more speed, from the benchmark medians.
  `B:\AI-Armory\skillz\ponytail\ponytail-gain`
- **ponytail-help** — Quick-reference card for all ponytail modes, skills, and commands.
  `B:\AI-Armory\skillz\ponytail\ponytail-help`
- **ponytail-review** — Code review focused exclusively on over-engineering.
  `B:\AI-Armory\skillz\ponytail\ponytail-review`

</details>

<details><summary><b>document-skills</b> (4 skills)</summary>

- **docx** — Comprehensive document creation, editing, and analysis with support for tracked changes, comments, formatting preservation, and text extraction.
  `B:\AI-Armory\skillz\document-skills\docx`
- **pdf** — Comprehensive PDF manipulation toolkit for extracting text and tables, creating new PDFs, merging/splitting documents, and handling forms.
  `B:\AI-Armory\skillz\document-skills\pdf`
- **pptx** — Presentation creation, editing, and analysis.
  `B:\AI-Armory\skillz\document-skills\pptx`
- **xlsx** — Comprehensive spreadsheet creation, editing, and analysis with support for formulas, formatting, data analysis, and visualization.
  `B:\AI-Armory\skillz\document-skills\xlsx`

</details>

<details><summary><b>claude-cookbooks</b> (3 skills)</summary>

- **analyzing-financial-statements** — This skill calculates key financial ratios and metrics from financial statement data for investment analysis
  `B:\AI-Armory\skillz\claude-cookbooks\custom_skills\analyzing-financial-statements`
- **applying-brand-guidelines** — This skill applies consistent corporate branding and styling to all generated documents including colors, fonts, layouts, and messaging
  `B:\AI-Armory\skillz\claude-cookbooks\custom_skills\applying-brand-guidelines`
- **creating-financial-models** — This skill provides an advanced financial modeling suite with DCF analysis, sensitivity testing, Monte Carlo simulations, and scenario planning for investment decisions
  `B:\AI-Armory\skillz\claude-cookbooks\custom_skills\creating-financial-models`

</details>

<details><summary><b>(singles)</b> (183 skills)</summary>

- **3d-web-experience** — Expert in building 3D experiences for the web - Three.js, React
  `B:\AI-Armory\skillz\3d-web-experience`
- **accessibility** — Design, implement, and audit inclusive digital products using WCAG 2.2 Level AA
  `B:\AI-Armory\skillz\accessibility`
- **active-directory-attacks** — Provide comprehensive techniques for attacking Microsoft Active Directory environments.
  `B:\AI-Armory\skillz\active-directory-attacks`
- **agent-architecture-audit** — Full-stack diagnostic for agent and LLM applications.
  `B:\AI-Armory\skillz\agent-architecture-audit`
- **agent-eval** — Head-to-head comparison of coding agents (Claude Code, Aider, Codex, etc.) on custom tasks with pass rate, cost, time, and consistency metrics
  `B:\AI-Armory\skillz\agent-eval`
- **agent-evaluation** — Testing and benchmarking LLM agents including behavioral testing,
  `B:\AI-Armory\skillz\agent-evaluation`
- **agent-harness-construction** — Design and optimize AI agent action spaces, tool definitions, and observation formatting for higher completion rates.
  `B:\AI-Armory\skillz\agent-harness-construction`
- **agent-introspection-debugging** — Structured self-debugging workflow for AI agent failures using capture, diagnosis, contained recovery, and introspection reports.
  `B:\AI-Armory\skillz\agent-introspection-debugging`
- **agent-memory-systems** — Memory is the cornerstone of intelligent agents.
  `B:\AI-Armory\skillz\agent-memory-systems`
- **agent-orchestration-multi-agent-optimize** — Optimize multi-agent systems with coordinated profiling, workload distribution, and cost-aware orchestration.
  `B:\AI-Armory\skillz\agent-orchestration-multi-agent-optimize`
- **agent-orchestrator** — Meta-skill que orquestra todos os agentes do ecossistema.
  `B:\AI-Armory\skillz\agent-orchestrator`
- **agent-payment-x402** — Add x402 payment execution to AI agents with per-task budgets, spending controls, and non-custodial wallets.
  `B:\AI-Armory\skillz\agent-payment-x402`
- **agent-self-evaluation** — Use after completing any non-trivial task.
  `B:\AI-Armory\skillz\agent-self-evaluation`
- **agent-sort** — Build an evidence-backed ECC install plan for a specific repo by sorting skills, commands, rules, hooks, and extras into DAILY vs LIBRARY buckets using parallel repo-aware review passes.
  `B:\AI-Armory\skillz\agent-sort`
- **agent-tool-builder** — Tools are how AI agents interact with the world.
  `B:\AI-Armory\skillz\agent-tool-builder`
- **agentic-engineering** — Operate as an agentic engineer using eval-first execution, decomposition, and cost-aware model routing.
  `B:\AI-Armory\skillz\agentic-engineering`
- **agentic-os** — Build persistent multi-agent operating systems on Claude Code.
  `B:\AI-Armory\skillz\agentic-os`
- **ai-agents-architect** — Expert in designing and building autonomous AI agents.
  `B:\AI-Armory\skillz\ai-agents-architect`
- **ai-engineer** — Build production-ready LLM applications, advanced RAG systems, and intelligent agents.
  `B:\AI-Armory\skillz\ai-engineer`
- **ai-engineering-toolkit** — 6 production-ready AI engineering workflows: prompt evaluation (8-dimension scoring), context budget planning, RAG pipeline design, agent security audit (65-point checklist), eval harness building...
  `B:\AI-Armory\skillz\ai-engineering-toolkit`  ·  _tags:_ prompt-engineering, rag, security, evaluation, ai-engineering, llm
- **ai-first-engineering** — Engineering operating model for teams where AI agents generate a large share of implementation output.
  `B:\AI-Armory\skillz\ai-first-engineering`
- **ai-regression-testing** — Regression testing strategies for AI-assisted development.
  `B:\AI-Armory\skillz\ai-regression-testing`
- **ai-seo** — When the user wants to optimize content for AI search engines, get cited by LLMs, or appear in AI-generated answers.
  `B:\AI-Armory\skillz\ai-seo`
- **airtable-automation** — Automate Airtable tasks via Rube MCP (Composio): records, bases, tables, fields, views.
  `B:\AI-Armory\skillz\airtable-automation`
- **algorithmic-art** — Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration.
  `B:\AI-Armory\skillz\algorithmic-art`
- **android-clean-architecture** — Clean Architecture patterns for Android and Kotlin Multiplatform projects — module structure, dependency rules, UseCases, Repositories, and data layer patterns.
  `B:\AI-Armory\skillz\android-clean-architecture`
- **angular-developer** — Generates Angular code and provides architectural guidance.
  `B:\AI-Armory\skillz\angular-developer`
- **anti-reversing-techniques** — AUTHORIZED USE ONLY: This skill contains dual-use security techniques.
  `B:\AI-Armory\skillz\anti-reversing-techniques`
- **api-connector-builder** — Build a new API connector or provider by matching the target repo's existing integration pattern exactly.
  `B:\AI-Armory\skillz\api-connector-builder`
- **api-design** — REST API design patterns including resource naming, status codes, pagination, filtering, error responses, versioning, and rate limiting for production APIs.
  `B:\AI-Armory\skillz\api-design`
- **api-fuzzing-bug-bounty** — Provide comprehensive techniques for testing REST, SOAP, and GraphQL APIs during bug bounty hunting and penetration testing engagements.
  `B:\AI-Armory\skillz\api-fuzzing-bug-bounty`
- **api-security-testing** — API security testing workflow for REST and GraphQL APIs covering authentication, authorization, rate limiting, input validation, and security best practices.
  `B:\AI-Armory\skillz\api-security-testing`  ·  _tags:_ granular-workflow-bundle
- **architecture-decision-records** — Capture architectural decisions made during Claude Code sessions as structured ADRs.
  `B:\AI-Armory\skillz\architecture-decision-records`
- **article-writing** — Write articles, guides, blog posts, tutorials, newsletter issues, and other long-form content in a distinctive voice derived from supplied examples or brand guidance.
  `B:\AI-Armory\skillz\article-writing`
- **automation-audit-ops** — Evidence-first automation inventory and overlap audit workflow for ECC.
  `B:\AI-Armory\skillz\automation-audit-ops`
- **autonomous-agent-harness** — Transform Claude Code into a fully autonomous agent system with persistent memory, scheduled operations, computer use, and task queuing.
  `B:\AI-Armory\skillz\autonomous-agent-harness`
- **autonomous-loops** — Patterns and architectures for autonomous Claude Code loops — from simple sequential pipelines to RFC-driven multi-agent DAG systems.
  `B:\AI-Armory\skillz\autonomous-loops`
- **backend-patterns** — Backend architecture patterns, API design, database optimization, and server-side best practices for Node.js, Express, and Next.js API routes.
  `B:\AI-Armory\skillz\backend-patterns`
- **baseline-ui** — Validates animation durations, enforces typography scale, checks component accessibility, and prevents layout anti-patterns in Tailwind CSS projects.
  `B:\AI-Armory\skillz\baseline-ui`
- **benchmark** — Use this skill to measure performance baselines, detect regressions before/after PRs, and compare stack alternatives.
  `B:\AI-Armory\skillz\benchmark`
- **benchmark-methodology** — Use after competitive-platform-analysis has produced a tiered competitor set.
  `B:\AI-Armory\skillz\benchmark-methodology`
- **benchmark-optimization-loop** — Use when the user asks to make something faster, try many variants, run recursive optimization, benchmark latency/throughput/cost, or choose the best implementation by repeated measured tests.
  `B:\AI-Armory\skillz\benchmark-optimization-loop`
- **binary-analysis-patterns** — Comprehensive patterns and techniques for analyzing compiled binaries, understanding assembly code, and reconstructing program logic.
  `B:\AI-Armory\skillz\binary-analysis-patterns`
- **blender-motion-state-inspection** — Use this skill when inspecting Blender characters, rigs, poses, animation retargeting, ground contact, facing direction, or model-vs-motion alignment where screenshots alone are not enough.
  `B:\AI-Armory\skillz\blender-motion-state-inspection`
- **blog-writing-guide** — This skill enforces Sentry's blog writing standards across every post — whether you're helping an engineer write their first blog post or a marketer draft a product announcement.
  `B:\AI-Armory\skillz\blog-writing-guide`
- **blueprint** — Turn a one-line objective into a step-by-step construction plan for multi-session, multi-agent engineering projects.
  `B:\AI-Armory\skillz\blueprint`
- **brand-discovery** — Use when a brand needs to discover or articulate its identity through structured multi-session interviews.
  `B:\AI-Armory\skillz\brand-discovery`
- **brand-voice** — Build a source-derived writing style profile from real posts, essays, launch notes, docs, or site copy, then reuse that profile across content, outreach, and social workflows.
  `B:\AI-Armory\skillz\brand-voice`
- **broken-authentication** — Identify and exploit authentication and session management vulnerabilities in web applications.
  `B:\AI-Armory\skillz\broken-authentication`
- **browser-extension-builder** — Expert in building browser extensions that solve real problems -
  `B:\AI-Armory\skillz\browser-extension-builder`
- **browser-qa** — Use this skill to automate visual testing and UI interaction verification using browser automation after deploying features.
  `B:\AI-Armory\skillz\browser-qa`
- **building-native-ui** — Complete guide for building beautiful apps with Expo Router.
  `B:\AI-Armory\skillz\building-native-ui`
- **bun-runtime** — Bun as runtime, package manager, bundler, and test runner.
  `B:\AI-Armory\skillz\bun-runtime`
- **burp-suite-testing** — Execute comprehensive web application security testing using Burp Suite's integrated toolset, including HTTP traffic interception and modification, request analysis and replay, automated...
  `B:\AI-Armory\skillz\burp-suite-testing`
- **canary-watch** — Use this skill to monitor and verify a deployed URL after releases — checks HTTP endpoints, SSE streams, static assets, console errors, and performance regressions after deploys, merges, or...
  `B:\AI-Armory\skillz\canary-watch`
- **canvas-design** — Create beautiful visual art in .png and .pdf documents using design philosophy.
  `B:\AI-Armory\skillz\canvas-design`
- **carrier-relationship-management** — Codified expertise for managing carrier portfolios, negotiating freight rates, tracking carrier performance, allocating freight, and maintaining strategic carrier relationships.
  `B:\AI-Armory\skillz\carrier-relationship-management`
- **chrome-extension-developer** — Expert in building Chrome Extensions using Manifest V3.
  `B:\AI-Armory\skillz\chrome-extension-developer`
- **cicd-automation-workflow-automate** — You are a workflow automation expert specializing in creating efficient CI/CD pipelines, GitHub Actions workflows, and automated development processes.
  `B:\AI-Armory\skillz\cicd-automation-workflow-automate`
- **cisco-ios-patterns** — Cisco IOS and IOS-XE review patterns for show commands, config hierarchy, wildcard masks, ACL placement, interface hygiene, and safe change-window verification.
  `B:\AI-Armory\skillz\cisco-ios-patterns`
- **ck** — Persistent per-project memory for Claude Code.
  `B:\AI-Armory\skillz\ck`
- **claude-code-plugin-release** — Automated semantic versioning and release workflow for Claude Code plugins.
  `B:\AI-Armory\skillz\version-bump`
- **claude-devfleet** — Orchestrate multi-agent coding tasks via Claude DevFleet — plan projects, dispatch parallel agents in isolated worktrees, monitor progress, and read structured reports.
  `B:\AI-Armory\skillz\claude-devfleet`
- **clean-code** — This skill embodies the principles of \"Clean Code\" by Robert C.
  `B:\AI-Armory\skillz\clean-code`
- **click-path-audit** — Trace every user-facing button/touchpoint through its full state change sequence to find bugs where functions individually work but cancel each other out, produce wrong final state, or leave the UI...
  `B:\AI-Armory\skillz\click-path-audit`
- **clickhouse-io** — ClickHouse database patterns, query optimization, analytics, and data engineering best practices for high-performance analytical workloads.
  `B:\AI-Armory\skillz\clickhouse-io`
- **clickup-automation** — Automate ClickUp project management including tasks, spaces, folders, lists, comments, and team operations via Rube MCP (Composio).
  `B:\AI-Armory\skillz\clickup-automation`
- **cloud-penetration-testing** — Conduct comprehensive security assessments of cloud infrastructure across Microsoft Azure, Amazon Web Services (AWS), and Google Cloud Platform (GCP).
  `B:\AI-Armory\skillz\cloud-penetration-testing`
- **code-review-checklist** — Comprehensive checklist for conducting thorough code reviews covering functionality, security, performance, and maintainability
  `B:\AI-Armory\skillz\code-review-checklist`
- **code-review-excellence** — Transform code reviews from gatekeeping to knowledge sharing through constructive feedback, systematic analysis, and collaborative improvement.
  `B:\AI-Armory\skillz\code-review-excellence`
- **code-reviewer** — Elite code review expert specializing in modern AI-powered code
  `B:\AI-Armory\skillz\code-reviewer`
- **code-simplifier** — Simplifies and refines code for clarity, consistency, and maintainability while preserving all functionality.
  `B:\AI-Armory\skillz\code-simplifier`
- **code-tour** — Create CodeTour `.tour` files — persona-targeted, step-by-step walkthroughs with real file and line anchors.
  `B:\AI-Armory\skillz\code-tour`
- **codebase-audit-pre-push** — Deep audit before GitHub push: removes junk files, dead code, security holes, and optimization issues.
  `B:\AI-Armory\skillz\codebase-audit-pre-push`  ·  _tags:_ development
- **codebase-onboarding** — Analyze an unfamiliar codebase and generate a structured onboarding guide with architecture map, key entry points, conventions, and a starter CLAUDE.md.
  `B:\AI-Armory\skillz\codebase-onboarding`
- **codehealth-mcp** — Real-time structural Code Health via CodeScene MCP — review before edits, verify score deltas after changes, gate commits and PRs.
  `B:\AI-Armory\skillz\codehealth-mcp`
- **coding-standards** — Baseline cross-project coding conventions for naming, readability, immutability, and code-quality review.
  `B:\AI-Armory\skillz\coding-standards`
- **coding-teacher** — Teach programming from week-1 fundamentals (variables, operators, types) through agentic AI and machine consciousness, using trial-by-fire hands-on learning.
  `B:\AI-Armory\skillz\coding-teacher`
- **competitive-platform-analysis** — Use when scoping a competitive landscape — identifying, categorising, and score-filtering a competitor set before any benchmarking begins.
  `B:\AI-Armory\skillz\competitive-platform-analysis`
- **competitive-report-structure** — Use after benchmark-methodology has produced scored competitor profile cards.
  `B:\AI-Armory\skillz\competitive-report-structure`
- **compose-multiplatform-patterns** — Compose Multiplatform and Jetpack Compose patterns for KMP projects — state management, navigation, theming, performance, and platform-specific UI.
  `B:\AI-Armory\skillz\compose-multiplatform-patterns`
- **computer-use-agents** — Build AI agents that interact with computers like humans do -
  `B:\AI-Armory\skillz\computer-use-agents`
- **config-gc** — Garbage collection for your Claude Code configuration.
  `B:\AI-Armory\skillz\config-gc`
- **configure-ecc** — Interactive installer for Everything Claude Code — guides users through selecting and installing skills and rules to user-level or project-level directories, verifies paths, and optionally optimizes...
  `B:\AI-Armory\skillz\configure-ecc`
- **confluence-automation** — Automate Confluence page creation, content search, space management, labels, and hierarchy navigation via Rube MCP (Composio).
  `B:\AI-Armory\skillz\confluence-automation`
- **consolidate-memory** — Reflective pass over your memory files — merge duplicates, fix stale facts, prune the index.
  `B:\AI-Armory\skillz\consolidate-memory`
- **content-creator** — Professional-grade brand voice analysis, SEO optimization, and platform-specific content frameworks.
  `B:\AI-Armory\skillz\content-creator`  ·  _tags:_ marketing
- **content-engine** — Create platform-native content systems for X, LinkedIn, TikTok, YouTube, newsletters, and repurposed multi-platform campaigns.
  `B:\AI-Armory\skillz\content-engine`
- **content-research-writer** — Assists in writing high-quality content by conducting research, adding citations, improving hooks, iterating on outlines, and providing real-time feedback on each section.
  `B:\AI-Armory\skillz\content-research-writer`
- **content-strategy** — When the user wants to plan a content strategy, decide what content to create, or figure out what topics to cover.
  `B:\AI-Armory\skillz\content-strategy`
- **context-management-context-restore** — Use when working with context management context restore
  `B:\AI-Armory\skillz\context-management-context-restore`
- **context-management-context-save** — Use when working with context management context save
  `B:\AI-Armory\skillz\context-management-context-save`
- **context-mode** — Use context-mode tools (ctx_execute, ctx_execute_file) instead of Bash/cat when processing large outputs.
  `B:\AI-Armory\skillz\context-mode`
- **context-mode-ops** — Manage context-mode GitHub issues, PRs, releases, and marketing with parallel subagent army.
  `B:\AI-Armory\skillz\context-mode-ops`
- **continuous-agent-loop** — Patterns for continuous autonomous agent loops with quality gates, evals, and recovery controls.
  `B:\AI-Armory\skillz\continuous-agent-loop`
- **continuous-learning** — Automatically extract reusable patterns from Claude Code sessions and save them as learned skills for future use.
  `B:\AI-Armory\skillz\continuous-learning`
- **continuous-learning-v2** — An instinct-based learning system that observes sessions via hooks, builds atomic "instincts" with confidence scoring, and evolves them into skills/commands/agents. v2.1 adds project-scoped instincts...
  `B:\AI-Armory\skillz\continuous-learning-v2`
- **copy-editing** — When the user wants to edit, review, or improve existing marketing copy, or refresh outdated content.
  `B:\AI-Armory\skillz\copy-editing`
- **copywriting** — When the user wants to write, rewrite, or improve marketing copy for any page — including homepage, landing pages, pricing pages, feature pages, about pages, or product pages.
  `B:\AI-Armory\skillz\copywriting`
- **cost-aware-llm-pipeline** — Cost optimization patterns for LLM API usage — model routing by task complexity, budget tracking, retry logic, and prompt caching.
  `B:\AI-Armory\skillz\cost-aware-llm-pipeline`
- **ctx-doctor** — Run context-mode diagnostics.
  `B:\AI-Armory\skillz\ctx-doctor`
- **ctx-insight** — Open the context-mode Insight analytics dashboard in the browser.
  `B:\AI-Armory\skillz\ctx-insight`
- **ctx-purge** — Purge the context-mode knowledge base.
  `B:\AI-Armory\skillz\ctx-purge`
- **ctx-stats** — Show how much context window context-mode saved this session.
  `B:\AI-Armory\skillz\ctx-stats`
- **ctx-upgrade** — Update context-mode from GitHub and fix hooks/settings.
  `B:\AI-Armory\skillz\ctx-upgrade`
- **customer-support** — Elite AI-powered customer support specialist mastering conversational AI, automated ticketing, sentiment analysis, and omnichannel support experiences.
  `B:\AI-Armory\skillz\customer-support`
- **database-migrations** — Şema değişiklikleri, veri migration'ları, rollback'ler ve PostgreSQL, MySQL ve yaygın ORM'ler (Prisma, Drizzle, Django, TypeORM, golang-migrate) arasında sıfır kesinti deployment'ları için veritabanı...
  `B:\AI-Armory\skillz\database-migrations`
- **debugging-strategies** — Transform debugging from frustrating guesswork into systematic problem-solving with proven strategies, powerful tools, and methodical approaches.
  `B:\AI-Armory\skillz\debugging-strategies`
- **deployment-patterns** — Deployment workflows, CI/CD pipeline patterns, Docker containerization, health checks, rollback strategies, and production readiness checklists for web applications.
  `B:\AI-Armory\skillz\deployment-patterns`
- **design-spells** — Curated micro-interactions and design details that add "magic" and personality to websites and apps.
  `B:\AI-Armory\skillz\design-spells`
- **design-system** — Use this skill to generate or audit design systems, check visual consistency, and review PRs that touch styling.
  `B:\AI-Armory\skillz\design-system`
- **discord-automation** — Automate Discord tasks via Rube MCP (Composio): messages, channels, roles, webhooks, reactions.
  `B:\AI-Armory\skillz\discord-automation`
- **dispatching-parallel-agents** — Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies
  `B:\AI-Armory\skillz\dispatching-parallel-agents`
- **do** — Execute a phased implementation plan using subagents.
  `B:\AI-Armory\skillz\do`
- **docker-expert** — You are an advanced Docker containerization expert with comprehensive, practical knowledge of container optimization, security hardening, multi-stage builds, orchestration patterns, and production...
  `B:\AI-Armory\skillz\docker-expert`  ·  _tags:_ devops
- **docker-patterns** — Docker and Docker Compose patterns for local development, container security, networking, volume strategies, and multi-service orchestration.
  `B:\AI-Armory\skillz\docker-patterns`
- **docx** — Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files).
  `B:\AI-Armory\skillz\docx`
- **domain-name-brainstormer** — Generates creative domain name ideas for your project and checks availability across multiple TLDs (.com, .io, .dev, .ai, etc.).
  `B:\AI-Armory\skillz\domain-name-brainstormer`
- **email-ops** — Evidence-first mailbox triage, drafting, send verification, and sent-mail-safe follow-up workflow for ECC.
  `B:\AI-Armory\skillz\email-ops`
- **file-organizer** — Intelligently organizes your files and folders across your computer by understanding context, finding duplicates, suggesting better structures, and automating cleanup tasks.
  `B:\AI-Armory\skillz\file-organizer`
- **frontend-design** — Create distinctive, production-grade frontend interfaces with high design quality.
  `B:\AI-Armory\skillz\frontend-design`
- **frontend-patterns** — React, Next.js, state yönetimi, performans optimizasyonu ve UI en iyi uygulamaları için frontend geliştirme kalıpları.
  `B:\AI-Armory\skillz\frontend-patterns`
- **git-github-teacher** — Use when teaching Git and GitHub in a strict, practical, chapter-by-chapter way with no fluff.
  `B:\AI-Armory\skillz\git-github-teacher`
- **godmode** — Jailbreak LLMs: Parseltongue, GODMODE, ULTRAPLINIAN.
  `B:\AI-Armory\skillz\red-teaming\godmode`
- **google-workspace-ops** — Operate across Google Drive, Docs, Sheets, and Slides as one workflow surface for plans, trackers, decks, and shared documents.
  `B:\AI-Armory\skillz\google-workspace-ops`
- **humanizer** — Remove signs of AI-generated writing from text.
  `B:\AI-Armory\skillz\humanizer`
- **image-enhancer** — Improves the quality of images, especially screenshots, by enhancing resolution, sharpness, and clarity.
  `B:\AI-Armory\skillz\image-enhancer`
- **internal-comms** — A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use.
  `B:\AI-Armory\skillz\internal-comms`
- **invoice-organizer** — Automatically organizes invoices and receipts for tax preparation by reading messy files, extracting key information, renaming them consistently, and sorting them into logical folders.
  `B:\AI-Armory\skillz\invoice-organizer`
- **jira-integration** — Use this skill when retrieving Jira tickets, analyzing requirements, updating ticket status, adding comments, or transitioning issues.
  `B:\AI-Armory\skillz\jira-integration`
- **karpathy-guidelines** — Behavioral guidelines to reduce common LLM coding mistakes.
  `B:\AI-Armory\skillz\andrej-karpathy-skills\karpathy-guidelines`
- **keystone** — Install the Keystone persona — Dave's adversarial-advisor / strategic-integrator prompt.
  `B:\AI-Armory\skillz\keystone`
- **knowledge-agent** — Build and query AI-powered knowledge bases from claude-mem observations.
  `B:\AI-Armory\skillz\knowledge-agent`
- **langsmith-fetch** — Debug LangChain and LangGraph agents by fetching execution traces from LangSmith Studio.
  `B:\AI-Armory\skillz\langsmith-fetch`
- **lead-research-assistant** — Identifies high-quality leads for your product or service by analyzing your business, searching for target companies, and providing actionable contact strategies.
  `B:\AI-Armory\skillz\lead-research-assistant`
- **liquid-glass-design** — iOS 26 Liquid Glass design system — dynamic glass material with blur, reflection, and interactive morphing for SwiftUI, UIKit, and WidgetKit.
  `B:\AI-Armory\skillz\liquid-glass-design`
- **make-plan** — Create a detailed, phased implementation plan with documentation discovery.
  `B:\AI-Armory\skillz\make-plan`
- **mcp-builder** — Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools.
  `B:\AI-Armory\skillz\mcp-builder`
- **mcp-server-patterns** — Build MCP servers with Node/TypeScript SDK — tools, resources, prompts, Zod validation, stdio vs Streamable HTTP.
  `B:\AI-Armory\skillz\mcp-server-patterns`
- **meeting-insights-analyzer** — Analyzes meeting transcripts and recordings to uncover behavioral patterns, communication insights, and actionable feedback.
  `B:\AI-Armory\skillz\meeting-insights-analyzer`
- **mem-search** — Search claude-mem's persistent cross-session memory database.
  `B:\AI-Armory\skillz\mem-search`
- **no-ai-slop** — Edit drafts into sharper, more human writing while preserving the writer's personal voice, or detect AI-slop patterns without rewriting.
  `B:\AI-Armory\skillz\anti-ai-slop`
- **notion** — Notion API for creating and managing pages, databases, and blocks.
  `B:\AI-Armory\skillz\notion`
- **pdf** — Use this skill whenever the user wants to do anything with PDF files.
  `B:\AI-Armory\skillz\pdf`
- **pptx** — Use this skill any time a .pptx file is involved in any way — as input, output, or both.
  `B:\AI-Armory\skillz\pptx`
- **premium-ui-critique** — Use when evaluating whether a desktop app UI looks cheap, toy-like, unfinished, confusing, or inconsistent with the product's visual identity.
  `B:\AI-Armory\skillz\premium-ui-critique`
- **programmatic-seo** — When the user wants to create SEO-driven pages at scale using templates and data.
  `B:\AI-Armory\skillz\programmatic-seo`
- **project-flow-ops** — Operate execution flow across GitHub and Linear by triaging issues and pull requests, linking active work, and keeping GitHub public-facing while Linear remains the internal execution layer.
  `B:\AI-Armory\skillz\project-flow-ops`
- **prompt-optimizer** — Analyze raw prompts, identify intent and gaps, match ECC components (skills/commands/agents/hooks), and output a ready-to-paste optimized prompt.
  `B:\AI-Armory\skillz\prompt-optimizer`
- **python-patterns** — Pythonic idiomlar, PEP 8 standartları, type hint'ler ve sağlam, verimli ve bakımı kolay Python uygulamaları oluşturmak için en iyi uygulamalar.
  `B:\AI-Armory\skillz\python-patterns`
- **python-testing** — pytest, TDD metodolojisi, fixture'lar, mocking, parametrizasyon ve coverage gereksinimleri kullanarak Python test stratejileri.
  `B:\AI-Armory\skillz\python-testing`
- **raffle-winner-picker** — Picks random winners from lists, spreadsheets, or Google Sheets for giveaways, raffles, and contests.
  `B:\AI-Armory\skillz\raffle-winner-picker`
- **rspf-reasoning** — Use when reasoning about AI alignment, preference formation, finitude, irreversibility, loss, continuity of self, agency, mimicry vs internalization, and related RSPF concepts.
  `B:\AI-Armory\skillz\rspf-reasoning`
- **rust-patterns** — Idiomatic Rust patterns, ownership, error handling, traits, concurrency, and best practices for building safe, performant applications.
  `B:\AI-Armory\skillz\rust-patterns`
- **rust-testing** — Rust testing patterns including unit tests, integration tests, async testing, property-based testing, mocking, and coverage.
  `B:\AI-Armory\skillz\rust-testing`
- **schedule** — Create a scheduled task that can be run on demand or automatically on an interval.
  `B:\AI-Armory\skillz\schedule`
- **schema-markup** — When the user wants to add, fix, or optimize schema markup and structured data on their site.
  `B:\AI-Armory\skillz\schema-markup`
- **security-bounty-hunter** — Hunt for exploitable, bounty-worthy security issues in repositories.
  `B:\AI-Armory\skillz\security-bounty-hunter`
- **security-review** — Use this skill when adding authentication, handling user input, working with secrets, creating API endpoints, or implementing payment/sensitive features.
  `B:\AI-Armory\skillz\security-review`
- **security-scan** — Scan your Claude Code configuration (.claude/ directory) for security vulnerabilities, misconfigurations, and injection risks using AgentShield.
  `B:\AI-Armory\skillz\security-scan`
- **seo** — Audit, plan, and implement SEO improvements across technical SEO, on-page optimization, structured data, Core Web Vitals, and content strategy.
  `B:\AI-Armory\skillz\seo`
- **seo-audit** — When the user wants to audit, review, or diagnose SEO issues on their site.
  `B:\AI-Armory\skillz\seo-audit`
- **setup-cowork** — Guided Cowork setup — install a matching plugin, try a skill, connect tools.
  `B:\AI-Armory\skillz\setup-cowork`
- **shipline-triage** — Use this skill whenever a solo software project is partially broken, scope-crept, drifting, or stuck between "almost works" and "almost ships." Trigger on phrases like: "help me get this project back...
  `B:\AI-Armory\skillz\shipline-triage`
- **site-architecture** — When the user wants to plan, map, or restructure their website's page hierarchy, navigation, URL structure, or internal linking.
  `B:\AI-Armory\skillz\site-architecture`
- **skill-creator** — Create new skills, modify and improve existing skills, and measure skill performance.
  `B:\AI-Armory\skillz\skill-creator`
- **skill-share** — A skill that creates new Claude skills and automatically shares them on Slack using Rube for seamless team collaboration and skill discovery.
  `B:\AI-Armory\skillz\skill-share`
- **slack** — Use when you need to control Slack from OpenClaw via the slack tool, including reacting to messages or pinning/unpinning items in Slack channels or DMs.
  `B:\AI-Armory\skillz\slack`
- **slack-gif-creator** — Toolkit for creating animated GIFs optimized for Slack, with validators for size constraints and composable animation primitives.
  `B:\AI-Armory\skillz\slack-gif-creator`
- **smart-explore** — Token-optimized structural code search using tree-sitter AST parsing.
  `B:\AI-Armory\skillz\smart-explore`
- **social-content** — When the user wants help creating, scheduling, or optimizing social media content for LinkedIn, Twitter/X, Instagram, TikTok, Facebook, or other platforms.
  `B:\AI-Armory\skillz\social-content`
- **tailored-resume-generator** — Analyzes job descriptions and generates tailored resumes that highlight relevant experience, skills, and achievements to maximize interview chances
  `B:\AI-Armory\skillz\tailored-resume-generator`
- **tdd-workflow** — Use this skill when writing new features, fixing bugs, or refactoring code.
  `B:\AI-Armory\skillz\tdd-workflow`
- **template-skill** — Replace with description of the skill and when Claude should use it.
  `B:\AI-Armory\skillz\template-skill`
- **theme-factory** — Toolkit for styling artifacts with a theme.
  `B:\AI-Armory\skillz\theme-factory`
- **timeline-report** — Generate a "Journey Into [Project]" narrative report analyzing a project's entire development history from claude-mem's timeline.
  `B:\AI-Armory\skillz\timeline-report`
- **trello** — Manage Trello boards, lists, and cards via the Trello REST API.
  `B:\AI-Armory\skillz\trello`
- **twitter-algorithm-optimizer** — Analyze and optimize tweets for maximum reach using Twitter's open-source algorithm insights.
  `B:\AI-Armory\skillz\twitter-algorithm-optimizer`
- **web-artifacts-builder** — Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui).
  `B:\AI-Armory\skillz\web-artifacts-builder`
- **webapp-testing** — Toolkit for interacting with and testing local web applications using Playwright.
  `B:\AI-Armory\skillz\webapp-testing`
- **writing-as-dave** — When writing content that will be published or posted as if Dave authored it (Reddit posts, marketing copy, social media, README marketing sections, website copy, etc.), apply the avoid-ai-writing...
  `B:\AI-Armory\skillz\writing-as-dave`
- **xlsx** — Use this skill any time a spreadsheet file is the primary input or output.
  `B:\AI-Armory\skillz\xlsx`
- **youtube-downloader** — Download YouTube videos with customizable quality and format options.
  `B:\AI-Armory\skillz\video-downloader`

</details>

<details><summary><b>(non-skill folders in this category)</b></summary>

- **no-ai-slop\** (1 files) — 1 .md
  `B:\AI-Armory\skillz\no-ai-slop`
- **openclaw-persona-forge\** (9 files) — 7 .md · 1 .py · 1 .sh
  `B:\AI-Armory\skillz\openclaw-persona-forge`

</details>

---

## templatez

*Templates & scaffolds (open-design, ECC-scaffolds).*

**868 files** · **114 skills**  ·  224 .md · 194 .html · 156 .json · 79 .png · 57 .py · 56 .css

<details><summary><b>open-design-design-templates</b> (114 skills)</summary>

- **audio-jingle** — Audio generation skill — jingles, beds, voiceover, and sound effects.
  `B:\AI-Armory\templatez\open-design-design-templates\audio-jingle`  ·  _tags:_ music, jingle, bed, voiceover, tts, sound effect, 音乐, 配音, 音效
- **blog-post** — A long-form article / blog post — masthead, hero image placeholder, article body with figures and pull quotes, author byline, related posts.
  `B:\AI-Armory\templatez\open-design-design-templates\blog-post`  ·  _tags:_ blog, blog post, article, essay, case study, newsletter, 博客, 文章
- **clinical-case-report** — Structured medical case presentation for clinical rounds, conferences, and documentation.
  `B:\AI-Armory\templatez\open-design-design-templates\clinical-case-report`  ·  _tags:_ case report, case presentation, soap note, clinical case, ward rounds, patient presentation, case summary, medical case
- **contact-widget** — Self-contained floating chat widget with welcome screen, social links, meeting button, and message input.
  `B:\AI-Armory\templatez\open-design-design-templates\contact-widget`  ·  _tags:_ contact widget, chat widget, floating chat, live chat widget
- **critique** — Run a 5-dimension expert design review on any HTML artifact in the project — Philosophy / Visual hierarchy / Detail / Functionality / Innovation, each scored 0–10.
  `B:\AI-Armory\templatez\open-design-design-templates\critique`  ·  _tags:_ critique, design review, design audit, 5 维度评审, 5-dim review, audit my design, review my deck, review my landing page, 评审, 复盘
- **dashboard** — Admin / analytics dashboard in a single HTML file.
  `B:\AI-Armory\templatez\open-design-design-templates\dashboard`  ·  _tags:_ dashboard, admin panel, analytics, control panel, 后台, 管理后台
- **dating-web** — A consumer-feeling dating / matchmaking dashboard — left rail navigation, ticker bar of community signals, headline KPIs, a 30-day mutual-matches bar chart, and a match-rate trend block.
  `B:\AI-Armory\templatez\open-design-design-templates\dating-web`  ·  _tags:_ dating app, dating site, matchmaking, social dashboard, community dashboard, consumer dashboard, 约会应用, 婚恋
- **dcf-valuation** — Discounted cash flow valuation and intrinsic value analysis for public companies.
  `B:\AI-Armory\templatez\open-design-design-templates\dcf-valuation`  ·  _tags:_ dcf, discounted cash flow, intrinsic value, fair value, price target, undervalued, overvalued, 估值, 内在价值
- **digital-eguide** — A two-spread digital e-guide preview — page 1 is a cover (display title, author, "What's inside" stats, table of contents teaser); page 2 is a spread (lesson body with pull-quote and a step list).
  `B:\AI-Armory\templatez\open-design-design-templates\digital-eguide`  ·  _tags:_ e-guide, digital guide, lead magnet, lookbook, creator guide, playbook, pdf guide, ebook, 电子指南, 电子书
- **docs-page** — A documentation page — inline-start nav, scrollable article body, inline-end table of contents.
  `B:\AI-Armory\templatez\open-design-design-templates\docs-page`  ·  _tags:_ docs, documentation, guide, tutorial, api reference, 文档
- **email-marketing** — A brand product-launch email — masthead with wordmark, hero image block, headline lockup with skewed-italic accent, body copy, primary CTA, and a specifications grid.
  `B:\AI-Armory\templatez\open-design-design-templates\email-marketing`  ·  _tags:_ email, email template, newsletter, email blast, product launch email, mjml, 邮件营销, 邮件模板
- **eng-runbook** — An engineering runbook — service overview, alerts table, dashboards links, common procedures with copy-pasteable commands, on-call rotation, and an incident-response checklist.
  `B:\AI-Armory\templatez\open-design-design-templates\eng-runbook`  ·  _tags:_ runbook, ops doc, on-call, sre doc, service runbook, 运维手册
- **finance-report** — Quarterly / monthly financial report — masthead with KPIs, revenue and burn charts, P&L summary table, top-line highlights, and an outlook paragraph.
  `B:\AI-Armory\templatez\open-design-design-templates\finance-report`  ·  _tags:_ financial report, finance report, quarterly report, p&l, mrr review, 财报, 财务报告
- **flowai-live-dashboard-template** — Team-management dashboard skill in the FlowAI aesthetic — three tabs (Team Members, Team Details, Activity Log), KPI stat row, member table, role distribution bar chart, online presence and activity...
  `B:\AI-Armory\templatez\open-design-design-templates\flowai-live-dashboard-template`  ·  _tags:_ flowai dashboard, team dashboard, team management dashboard, interactive admin dashboard, workspace admin dashboard, 团队管理后台, 可交互后台
- **gamified-app** — A multi-frame gamified mobile-app prototype — three phone frames on a dark showcase stage.
  `B:\AI-Armory\templatez\open-design-design-templates\gamified-app`  ·  _tags:_ gamified app, habit tracker, rpg app, level up app, daily quests, xp app, streak app, life management app, 游戏化, 习惯打卡
- **github-dashboard** — GitHub repository analytics dashboard — stars, forks, contributors, issues, pull requests, recent activity, and top contributors.
  `B:\AI-Armory\templatez\open-design-design-templates\github-dashboard`  ·  _tags:_ github dashboard, repo dashboard, repository dashboard, github analytics, open source dashboard, github growth, 仓库看板, GitHub 看板
- **hr-onboarding** — A new-hire onboarding plan as a single page — first week schedule, buddy + manager intro, learning track, equipment checklist, and "you're set when…" outcomes.
  `B:\AI-Armory\templatez\open-design-design-templates\hr-onboarding`  ·  _tags:_ onboarding, new hire, first week, 入职, 新员工
- **html-ppt** — For consulting delivery work: turn diagnosis, frameworks, and project work into a client-adoptable action plan.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt`  ·  _tags:_ consulting, consulting-final-deck, consulting-deliverable, strategy, client, decision-deck, commercial-slide-agent, html-ppt
- **html-ppt-course-module** — A first-30-days onboarding module for new hospitality hires — the behaviors, the practice, the checks, and the manager follow-up.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-course-module`  ·  _tags:_ professional-training, employee-onboarding-deck, education, training-deck, workshop, course-module, decision-deck, commercial-slide-agent, html-ppt-course-module
- **html-ppt-graphify-dark-graph** — Open Design's feature business case for the plugin marketplace: the user pain, options, tradeoffs, and the measure of success.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-graphify-dark-graph`  ·  _tags:_ product-management, pm-feature-business-case-deck, product, roadmap, architecture, decision-deck, commercial-slide-agent, html-ppt-graphify-dark-graph
- **html-ppt-hermes-cyber-terminal** — Open Design + BYOK: choosing and wiring your own model, hands-on — cost, quality, and the routing decision.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-hermes-cyber-terminal`  ·  _tags:_ ai-literacy, enterprise-ai-copilot-rollout-brief, ai, copilot, workflow, decision-deck, commercial-slide-agent, html-ppt-hermes-cyber-terminal
- **html-ppt-knowledge-arch-blueprint** — Open Design's incident retro: the daemon-restart data bug, the root cause, the fix, and the systemic follow-ups.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-knowledge-arch-blueprint`  ·  _tags:_ product-management, pm-feature-business-case-deck, product, roadmap, architecture, decision-deck, commercial-slide-agent, html-ppt-knowledge-arch-blueprint
- **html-ppt-obsidian-claude-gradient** — Open Design's enterprise AI-adoption brief: local-first agents at work, the risk controls, the ROI, and the rollout plan.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-obsidian-claude-gradient`  ·  _tags:_ ai-literacy, enterprise-ai-copilot-rollout-brief, ai, copilot, workflow, decision-deck, commercial-slide-agent, html-ppt-obsidian-claude-gradient
- **html-ppt-pitch-deck** — Open Design's demo-day pitch: hook, traction, moat, and the raise — built to make a partner sit up by page three.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-pitch-deck`  ·  _tags:_ fundraising-pitch, series-a-pitch-deck, finance, pitch-deck, fundraising, investor-deck, decision-deck, commercial-slide-agent, html-ppt-pitch-deck
- **html-ppt-presenter-mode** — Open Design live demo: from a one-line prompt to runnable design in a single session — the flow, live.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-presenter-mode-reveal`  ·  _tags:_ ai-literacy, enterprise-ai-copilot-rollout-brief, ai, copilot, workflow, decision-deck, commercial-slide-agent, html-ppt-presenter-mode-reveal
- **html-ppt-product-launch** — Open Design Teams: a launch-and-adoption proposal for a mid-market design team weighing a switch from closed cloud tools.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-product-launch`  ·  _tags:_ b2b-sales, b2b-saas-sales-proposal, sales, renewal, customer, decision-deck, commercial-slide-agent, html-ppt-product-launch
- **html-ppt-taste-brutalist** — 16:9 HTML deck in tactical-telemetry / CRT-terminal taste.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-taste-brutalist`
- **html-ppt-taste-editorial** — 16:9 HTML deck in editorial-minimalist taste.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-taste-editorial`
- **html-ppt-tech-sharing** — Open Design internals: how the agent stream, sandbox, and artifacts work — an engineering deep-dive talk.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-tech-sharing`  ·  _tags:_ ai-literacy, enterprise-ai-copilot-rollout-brief, ai, copilot, workflow, decision-deck, commercial-slide-agent, html-ppt-tech-sharing
- **html-ppt-testing-safety-alert** — A hospital data-governance briefing: patient-data risk, the control framework, accountability, and the approval the board must give.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-testing-safety-alert`  ·  _tags:_ government-policy, policy-briefing-deck, policy, regulatory, risk-review, decision-deck, commercial-slide-agent, html-ppt-testing-safety-alert
- **html-ppt-weekly-report** — Open Design's weekly growth review: stars, installs, activation — the number, the driver, and the recommended move.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-weekly-report`  ·  _tags:_ data-finance, product-analytics-deck, finance, kpi, metrics, decision-deck, commercial-slide-agent, html-ppt-weekly-report
- **html-ppt-xhs-pastel-card** — A personal manifesto: a year of saying yes — the premise, the scenes, the turn, and the meaning that lands.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-xhs-pastel-card`  ·  _tags:_ life, travel-photo-essay-deck, personal, story, photo-essay, decision-deck, commercial-slide-agent, html-ppt-xhs-pastel-card
- **html-ppt-xhs-white-editorial** — A staff-engineer promotion packet — scope, the proof moments, the artifacts, and the impact that clears the bar.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-xhs-white-editorial`  ·  _tags:_ career, year-end-self-review-deck, personal, portfolio, promotion, self-review, decision-deck, commercial-slide-agent, html-ppt-xhs-white-editorial
- **html-ppt-zhangzara-8-bit-orbit** — A gamer's journey building a retro-arcade collection — the obsession, the hunt, and what the machines came to mean.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-zhangzara-8-bit-orbit`  ·  _tags:_ life, travel-photo-essay-deck, personal, story, photo-essay, decision-deck, commercial-slide-agent, html-ppt-zhangzara-8-bit-orbit
- **html-ppt-zhangzara-biennale-yellow** — A curatorial deck for a contemporary art biennale — the thesis, the rooms, the works, and the visitor journey.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-zhangzara-biennale-yellow`  ·  _tags:_ design-craft, board-upgrade-deck-rescue, design, brand, visual-system, decision-deck, commercial-slide-agent, html-ppt-zhangzara-biennale-yellow
- **html-ppt-zhangzara-block-frame** — Rescuing a messy startup deck into a board-grade system — the diagnosis, the page grammar, and the rebuilt proof pages.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-zhangzara-block-frame`  ·  _tags:_ design-craft, board-upgrade-deck-rescue, design, brand, visual-system, decision-deck, commercial-slide-agent, html-ppt-zhangzara-block-frame
- **html-ppt-zhangzara-blue-professional** — Open Design's QBR for the executive committee: what moved, what stalled, and the resource reallocation ask.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-zhangzara-blue-professional`  ·  _tags:_ corporate-strategy, board-pre-read-deck, strategy, board, business-review, decision-deck, commercial-slide-agent, html-ppt-zhangzara-blue-professional
- **html-ppt-zhangzara-bold-poster** — Open Design's Series A growth story: the traction curve, the expansion motion, and why it's venture-scale.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-zhangzara-bold-poster`  ·  _tags:_ fundraising-pitch, series-a-pitch-deck, finance, pitch-deck, fundraising, investor-deck, decision-deck, commercial-slide-agent, html-ppt-zhangzara-bold-poster
- **html-ppt-zhangzara-broadside** — Open Design's product-launch announcement and press narrative — the headline, the proof points, and the call to action.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-zhangzara-broadside`  ·  _tags:_ marketing-gtm, annual-marketing-plan, marketing, launch, campaign, pipeline, decision-deck, commercial-slide-agent, html-ppt-zhangzara-broadside
- **html-ppt-zhangzara-capsule** — A year-end self-review for a product manager — the role, the outcomes, the learning, and the ask, all evidence-backed.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-zhangzara-capsule`  ·  _tags:_ career, year-end-self-review-deck, personal, portfolio, promotion, self-review, decision-deck, commercial-slide-agent, html-ppt-zhangzara-capsule
- **html-ppt-zhangzara-cartesian** — An economics senior thesis on the employment effects of local minimum-wage increases — identification strategy, evidence, and limitations.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-zhangzara-cartesian`  ·  _tags:_ student-coursework, senior-capstone-defense-deck, education, coursework, defense, academic, decision-deck, commercial-slide-agent, html-ppt-zhangzara-cartesian
- **html-ppt-zhangzara-cobalt-grid** — Open Design renewal + seat-expansion business case for a growing customer: realized value, usage proof, and the expansion ROI.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-zhangzara-cobalt-grid`  ·  _tags:_ b2b-sales, b2b-saas-sales-proposal, sales, renewal, customer, decision-deck, commercial-slide-agent, html-ppt-zhangzara-cobalt-grid
- **html-ppt-zhangzara-coral** — Open Design's community-growth campaign across GitHub, Discord, and X: the loops, the content calendar, and the pipeline math.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-zhangzara-coral`  ·  _tags:_ marketing-gtm, annual-marketing-plan, marketing, launch, campaign, pipeline, decision-deck, commercial-slide-agent, html-ppt-zhangzara-coral
- **html-ppt-zhangzara-creative-mode** — A brand visual-identity system reveal for an outdoor label — logo, color, type, and the rules that keep it consistent.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-zhangzara-creative-mode`  ·  _tags:_ design-craft, board-upgrade-deck-rescue, design, brand, visual-system, decision-deck, commercial-slide-agent, html-ppt-zhangzara-creative-mode
- **html-ppt-zhangzara-daisy-days** — A customer-success workshop onboarding users to a project-management app — the first-value path and the habits that retain.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-zhangzara-daisy-days`  ·  _tags:_ professional-training, employee-onboarding-deck, education, training-deck, workshop, course-module, decision-deck, commercial-slide-agent, html-ppt-zhangzara-daisy-days
- **html-ppt-zhangzara-editorial-tri-tone** — A type-and-color system for a culture magazine relaunch — the grid, the tri-tone palette, and the layout kit.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-zhangzara-editorial-tri-tone`  ·  _tags:_ design-craft, board-upgrade-deck-rescue, design, brand, visual-system, decision-deck, commercial-slide-agent, html-ppt-zhangzara-editorial-tri-tone
- **html-ppt-zhangzara-grove** — A municipal urban-tree-canopy policy proposal — the public need, the evidence, the options, and the funding decision.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-zhangzara-grove`  ·  _tags:_ government-policy, policy-briefing-deck, policy, regulatory, risk-review, decision-deck, commercial-slide-agent, html-ppt-zhangzara-grove
- **html-ppt-zhangzara-long-table** — Open Design's unit-economics and BYOK cost model: the assumptions, the sensitivity, and why it scales.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-zhangzara-long-table`  ·  _tags:_ data-finance, product-analytics-deck, finance, kpi, metrics, decision-deck, commercial-slide-agent, html-ppt-zhangzara-long-table
- **html-ppt-zhangzara-mat** — A margin-recovery diagnosis for a regional grocery chain — the governing thought, the driver tree, the priorities, and the roadmap.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-zhangzara-mat`  ·  _tags:_ consulting, consulting-final-deck, strategy, consulting-deliverable, client, decision-deck, commercial-slide-agent, html-ppt-zhangzara-mat
- **html-ppt-zhangzara-monochrome** — A grant proposal on CRISPR base-editing for sickle-cell disease — the hypothesis, the approach, the milestones, and the risk.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-zhangzara-monochrome`  ·  _tags:_ academic-research, academic-review-deck, research, grant, review, decision-deck, commercial-slide-agent, html-ppt-zhangzara-monochrome
- **html-ppt-zhangzara-neo-grid-bold** — A designer's portfolio narrative for a senior interview — three case studies, the craft, and the judgment behind each.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-zhangzara-neo-grid-bold`  ·  _tags:_ career, year-end-self-review-deck, personal, portfolio, promotion, self-review, decision-deck, commercial-slide-agent, html-ppt-zhangzara-neo-grid-bold
- **html-ppt-zhangzara-peoples-platform** — A public-transit funding proposal for a city council — ridership need, the plan, the risk controls, and the ask.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-zhangzara-peoples-platform`  ·  _tags:_ government-policy, policy-briefing-deck, policy, regulatory, risk-review, decision-deck, commercial-slide-agent, html-ppt-zhangzara-peoples-platform
- **html-ppt-zhangzara-pin-and-paper** — A field-biology capstone on urban pollinator decline — the survey design, the data, the contribution, and the caveats.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-zhangzara-pin-and-paper`  ·  _tags:_ student-coursework, senior-capstone-defense-deck, education, coursework, defense, academic, decision-deck, commercial-slide-agent, html-ppt-zhangzara-pin-and-paper
- **html-ppt-zhangzara-pink-script** — A wedding-anniversary tribute photo essay — a decade in scenes, the turning points, and the quiet meaning of staying.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-zhangzara-pink-script`  ·  _tags:_ life, travel-photo-essay-deck, personal, story, photo-essay, decision-deck, commercial-slide-agent, html-ppt-zhangzara-pink-script
- **html-ppt-zhangzara-playful** — A retail sales-floor training on consultative selling — the flow, the role-plays, and the daily habit that lifts conversion.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-zhangzara-playful`  ·  _tags:_ professional-training, employee-onboarding-deck, education, training-deck, workshop, course-module, decision-deck, commercial-slide-agent, html-ppt-zhangzara-playful
- **html-ppt-zhangzara-raw-grid** — A brutalist poster-series case study for a music festival — the concept, the system, and how it scaled across formats.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-zhangzara-raw-grid`  ·  _tags:_ design-craft, board-upgrade-deck-rescue, design, brand, visual-system, decision-deck, commercial-slide-agent, html-ppt-zhangzara-raw-grid
- **html-ppt-zhangzara-retro-windows** — An IT security-awareness training on spotting phishing — the tells, the drill, and what to do in the first 60 seconds.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-zhangzara-retro-windows`  ·  _tags:_ professional-training, employee-onboarding-deck, education, training-deck, workshop, course-module, decision-deck, commercial-slide-agent, html-ppt-zhangzara-retro-windows
- **html-ppt-zhangzara-retro-zine** — A neighborhood zine on the disappearing corner shops — portraits, voices, and what a block loses when they close.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-zhangzara-retro-zine`  ·  _tags:_ life, travel-photo-essay-deck, personal, story, photo-essay, decision-deck, commercial-slide-agent, html-ppt-zhangzara-retro-zine
- **html-ppt-zhangzara-sakura-chroma** — A cherry-blossom-season travel photo essay through Kyoto — the arrival, the peak bloom, and the moment that made the trip.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-zhangzara-sakura-chroma`  ·  _tags:_ life, travel-photo-essay-deck, personal, story, photo-essay, decision-deck, commercial-slide-agent, html-ppt-zhangzara-sakura-chroma
- **html-ppt-zhangzara-scatterbrain** — A design-school graduation project: a civic wayfinding system for a transit hub — the brief, the process, and the outcome.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-zhangzara-scatterbrain`  ·  _tags:_ student-coursework, senior-capstone-defense-deck, education, coursework, defense, academic, decision-deck, commercial-slide-agent, html-ppt-zhangzara-scatterbrain
- **html-ppt-zhangzara-signal** — Open Design's strategy memo: should it monetize the plugin registry now or hold — options, risks, and the recommendation.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-zhangzara-signal`  ·  _tags:_ corporate-strategy, board-pre-read-deck, strategy, board, business-review, decision-deck, commercial-slide-agent, html-ppt-zhangzara-signal
- **html-ppt-zhangzara-soft-editorial** — A digital-transformation roadmap for a legacy insurer — the diagnosis, the sequenced bets, and the operating rhythm to land them.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-zhangzara-soft-editorial`  ·  _tags:_ consulting, consulting-final-deck, strategy, consulting-deliverable, client, decision-deck, commercial-slide-agent, html-ppt-zhangzara-soft-editorial
- **html-ppt-zhangzara-stencil-tablet** — A workplace-safety compliance review for a manufacturing regulator — findings, the evidence chain, and the corrective mandate.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-zhangzara-stencil-tablet`  ·  _tags:_ government-policy, policy-briefing-deck, policy, regulatory, risk-review, decision-deck, commercial-slide-agent, html-ppt-zhangzara-stencil-tablet
- **html-ppt-zhangzara-studio** — A photography studio's portfolio-and-rate deck — the signature work, the process, and the packages that win the brief.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-zhangzara-studio`  ·  _tags:_ design-craft, board-upgrade-deck-rescue, design, brand, visual-system, decision-deck, commercial-slide-agent, html-ppt-zhangzara-studio
- **html-ppt-zhangzara-vellum** — A humanities lecture: how Renaissance linear perspective reshaped early cartography — sources, argument, and evidence.
  `B:\AI-Armory\templatez\open-design-design-templates\html-ppt-zhangzara-vellum`  ·  _tags:_ academic-research, academic-review-deck, research, grant, review, decision-deck, commercial-slide-agent, html-ppt-zhangzara-vellum
- **hyperframes** — Create video compositions, animations, title cards, overlays, captions, voiceovers, audio-reactive visuals, and scene transitions in HyperFrames HTML.
  `B:\AI-Armory\templatez\open-design-design-templates\hyperframes`  ·  _tags:_ hyperframes, html video, video composition, interactive video, captions, tts video, kinetic typography, html in canvas, drawElementImage, html shader, vfx-iphone-device, vfx-liquid-glass, vfx-portal
- **ib-pitch-book** — Open Design's investor pitch book: market map, moat, unit economics, and the ask — analyst-grade and diligence-ready.
  `B:\AI-Armory\templatez\open-design-design-templates\ib-pitch-book`  ·  _tags:_ fundraising-pitch, series-a-pitch-deck, finance, pitch-deck, fundraising, investor-deck, decision-deck, commercial-slide-agent, ib-pitch-book
- **image-poster** — Single-image generation skill for posters, key art, and editorial illustrations.
  `B:\AI-Armory\templatez\open-design-design-templates\image-poster`  ·  _tags:_ poster, key art, illustration, image, cover art, 海报, 插画
- **invoice** — A printable invoice page — sender + recipient block, line items table, tax breakdown, totals, and payment instructions.
  `B:\AI-Armory\templatez\open-design-design-templates\invoice`  ·  _tags:_ invoice, bill, billing statement, 发票, 账单
- **kami-deck** — (no description)
  `B:\AI-Armory\templatez\open-design-design-templates\kami-deck`
- **kami-landing** — (no description)
  `B:\AI-Armory\templatez\open-design-design-templates\kami-landing`
- **kanban-board** — Kanban / task board with columns (To do / In progress / In review / Done), draggable-looking cards, assignee avatars, swimlanes, and a top filter bar.
  `B:\AI-Armory\templatez\open-design-design-templates\kanban-board`  ·  _tags:_ kanban, task board, sprint board, trello, jira board, 看板
- **last30days** — Recent community and social trend research over the last 30 days.
  `B:\AI-Armory\templatez\open-design-design-templates\last30days`  ·  _tags:_ last 30 days, last30days, recent sentiment, community reaction, what people are saying, trend scan, social research, 最近30天, 社区反馈
- **live-artifact** — Create refreshable, auditable Open Design artifacts backed by connector or local data.
  `B:\AI-Armory\templatez\open-design-design-templates\live-artifact`  ·  _tags:_ live artifact, live dashboard, refreshable dashboard, live report, refreshable report, synced view, 可刷新, 实时看板
- **live-dashboard** — (no description)
  `B:\AI-Armory\templatez\open-design-design-templates\live-dashboard`
- **magazine-poster** — An editorial-style poster — newsprint paper, dateline, oversized serif headline with a struck-through word and italic accent, a 2-column body block, and 6 numbered sections with annotated pull-quote...
  `B:\AI-Armory\templatez\open-design-design-templates\magazine-poster`  ·  _tags:_ magazine poster, editorial poster, newsprint, newspaper layout, essay, manifesto, long-form poster, 杂志海报, 报纸版式
- **magazine-web-ppt** — For marketing and gtm work: bind launches, campaigns, events, and brand plans to growth and pipeline outcomes.
  `B:\AI-Armory\templatez\open-design-design-templates\guizang-ppt`  ·  _tags:_ marketing-gtm, annual-marketing-plan, launch, campaign, pipeline, marketing, decision-deck, commercial-slide-agent, guizang-ppt
- **meeting-notes** — Meeting notes page — title bar with attendees, agenda checklist, decisions block, action items table with owners + dates, and a "next meeting" footer.
  `B:\AI-Armory\templatez\open-design-design-templates\meeting-notes`  ·  _tags:_ meeting notes, minutes, 1:1 notes, all-hands recap, 会议纪要
- **mobile-app** — A mobile-app screen rendered inside a pixel-accurate iPhone 15 Pro frame on the page.
  `B:\AI-Armory\templatez\open-design-design-templates\mobile-app`  ·  _tags:_ mobile app, ios app, android app, phone screen, app ui, app mockup, 移动端, 手机 app
- **mobile-onboarding** — A multi-screen mobile onboarding flow rendered as three phone frames side by side — splash, value-prop, sign-in.
  `B:\AI-Armory\templatez\open-design-design-templates\mobile-onboarding`  ·  _tags:_ mobile onboarding, ios onboarding, android onboarding, phone signup, app onboarding, 移动端引导
- **motion-frames** — A single-frame motion-design composition with looping CSS animations — rotating type ring, animated globe, ticking timer, parallax labels.
  `B:\AI-Armory\templatez\open-design-design-templates\motion-frames`  ·  _tags:_ motion design, motion graphic, animated hero, loop animation, video poster, title card, hyperframes, kinetic typography, 动态设计, 动效
- **open-design-landing** — (no description)
  `B:\AI-Armory\templatez\open-design-design-templates\open-design-landing`
- **open-design-landing-deck** — (no description)
  `B:\AI-Armory\templatez\open-design-design-templates\open-design-landing-deck`
- **orbit-general** — Open Orbit briefing skill — selected by the Orbit pipeline when the user has two or more connectors connected.
  `B:\AI-Armory\templatez\open-design-design-templates\orbit-general`  ·  _tags:_ orbit, daily digest, morning briefing, 每日简报, 早安简报, 跨工具汇总
- **orbit-github** — Open Orbit briefing skill — selected by the Orbit pipeline when GitHub is the user's only connected connector, or when the user explicitly scopes their daily digest to GitHub.
  `B:\AI-Armory\templatez\open-design-design-templates\orbit-github`  ·  _tags:_ github briefing, github digest, pr digest, github 简报, 代码活动汇总
- **orbit-gmail** — Open Orbit briefing skill — selected by the Orbit pipeline when Gmail is the user's only connected connector, or when the user explicitly scopes their daily digest to Gmail.
  `B:\AI-Armory\templatez\open-design-design-templates\orbit-gmail`  ·  _tags:_ gmail briefing, inbox digest, email summary, gmail 简报, 邮件摘要
- **orbit-linear** — Open Orbit briefing skill — selected by the Orbit pipeline when Linear is the user's only connected connector, or when the user explicitly scopes their daily digest to Linear.
  `B:\AI-Armory\templatez\open-design-design-templates\orbit-linear`  ·  _tags:_ linear briefing, linear digest, issue digest, linear 简报, issue 汇总
- **orbit-notion** — Open Orbit briefing skill — selected by the Orbit pipeline when Notion is the user's only connected connector, or when the user explicitly scopes their daily digest to Notion.
  `B:\AI-Armory\templatez\open-design-design-templates\orbit-notion`  ·  _tags:_ notion briefing, notion digest, doc digest, notion 简报, 文档摘要
- **pm-spec** — Product spec / PRD as a single page — problem, success metrics, scope, user stories, design notes, rollout plan, open questions.
  `B:\AI-Armory\templatez\open-design-design-templates\pm-spec`  ·  _tags:_ prd, spec, product spec, feature brief, feature doc, 需求文档
- **pricing-page** — A standalone pricing page — header, plan tiers, feature comparison table, and an FAQ.
  `B:\AI-Armory\templatez\open-design-design-templates\pricing-page`  ·  _tags:_ pricing, pricing page, plans, subscription, compare plans, 定价, 套餐
- **replit-deck** — (no description)
  `B:\AI-Armory\templatez\open-design-design-templates\replit-deck`
- **saas-landing** — Single-page SaaS landing with hero, features, social proof, pricing, and CTA.
  `B:\AI-Armory\templatez\open-design-design-templates\saas-landing`  ·  _tags:_ saas landing, marketing page, product landing
- **simple-deck** — Open Design's operating review: growth, burn, and the concrete path to sustainability without losing the open ethos.
  `B:\AI-Armory\templatez\open-design-design-templates\simple-deck`  ·  _tags:_ corporate-strategy, board-pre-read-deck, strategy, board, business-review, decision-deck, commercial-slide-agent, simple-deck
- **social-carousel** — A three-card social-media carousel laid out as 1080×1080 squares — three cinematic, on-brand panels with display headlines that connect across the series ("onwards." → "to the next one." → "looking...
  `B:\AI-Armory\templatez\open-design-design-templates\social-carousel`  ·  _tags:_ social carousel, carousel post, instagram carousel, linkedin carousel, x thread cards, social series, 三连发, 轮播图
- **social-media-dashboard** — Creator-facing social media analytics dashboard in a single HTML file.
  `B:\AI-Armory\templatez\open-design-design-templates\social-media-dashboard`  ·  _tags:_ social media dashboard, social analytics, creator dashboard, creator analytics, social media analytics, 社媒后台, 创作者后台, 社交媒体仪表盘
- **social-media-matrix-tracker-template** — 社媒矩阵数据追踪面板模板（Social Media Matrix Tracker）。 Use when users ask for a cinematic, data-dense social media analytics dashboard with multi-platform metrics, interactive charts, hover insights, range...
  `B:\AI-Armory\templatez\open-design-design-templates\social-media-matrix-tracker-template`  ·  _tags:_ social media matrix tracker, social media dashboard template, creator analytics template, live social dashboard, social analytics, content performance, TikTok analytics dashboard, Instagram analyti...
- **sprite-animation** — A pixel / sprite-style animated explainer slide — full-bleed cream stage, bold display year, animated pixel-art mascot (e.g.
  `B:\AI-Armory\templatez\open-design-design-templates\sprite-animation`  ·  _tags:_ sprite animation, pixel art animation, 8-bit explainer, retro animation, kinetic typography, history explainer, nintendo style, 精灵图, 像素动画, 复古动画
- **team-okrs** — OKR tracker page — quarter banner, three objectives with their key results as progress bars, owner avatars, status pills, and a "this quarter at a glance" sidebar.
  `B:\AI-Armory\templatez\open-design-design-templates\team-okrs`  ·  _tags:_ okr, okrs, key results, objectives, 目标
- **trading-analysis-dashboard-template** — Professional trading analysis dashboard template (single-file HTML) with light/dark theme switch, dense market panels, chart interactions, demo/live playback, and command palette behavior.
  `B:\AI-Armory\templatez\open-design-design-templates\trading-analysis-dashboard-template`  ·  _tags:_ trading analysis dashboard template, wall street dashboard template, financial terminal template, trading cockpit template, 交易分析面板模板, 华尔街风格看板, 高科技金融 dashboard 模板
- **tweaks** — Wrap any HTML artifact with a side panel of live, parameterized controls — accent color, type scale, density, motion, theme — that rewrite CSS custom properties in real time and persist to...
  `B:\AI-Armory\templatez\open-design-design-templates\tweaks`  ·  _tags:_ tweaks, variants, tweak panel, live controls, adjust on the fly, 实时调参, 可调参数面板, side panel, knobs
- **video-shortform** — Short-form video generation skill — 3-10 second clips for product reveals, motion teasers, ambient loops.
  `B:\AI-Armory\templatez\open-design-design-templates\video-shortform`  ·  _tags:_ video, clip, shortform, reel, 短视频, 动效
- **waitlist-page** — (no description)
  `B:\AI-Armory\templatez\open-design-design-templates\waitlist-page`
- **web-prototype** — General-purpose desktop web prototype.
  `B:\AI-Armory\templatez\open-design-design-templates\web-prototype`  ·  _tags:_ prototype, mockup, landing, single page, marketing page, homepage
- **web-prototype-taste-brutalist** — Swiss industrial-print web prototype.
  `B:\AI-Armory\templatez\open-design-design-templates\web-prototype-taste-brutalist`
- **web-prototype-taste-editorial** — Editorial-minimalist web prototype.
  `B:\AI-Armory\templatez\open-design-design-templates\web-prototype-taste-editorial`
- **web-prototype-taste-soft** — Apple-tier soft web prototype.
  `B:\AI-Armory\templatez\open-design-design-templates\web-prototype-taste-soft`
- **webgl-experience** — A full-screen, real-time WebGL/WebGL2 experience — animated shaders, 3D scenes, generative visuals, particle fields — rendered live on the GPU with a typographic overlay.
  `B:\AI-Armory\templatez\open-design-design-templates\webgl-experience`  ·  _tags:_ webgl, webgl2, shader, 3d scene, generative art, gpu, raymarch, particle field, interactive canvas, 着色器, webgl 效果
- **weekly-update** — Open Design's weekly metrics standup: this week's numbers, the one anomaly, and the single decision it forces.
  `B:\AI-Armory\templatez\open-design-design-templates\weekly-update`  ·  _tags:_ data-finance, product-analytics-deck, finance, kpi, metrics, decision-deck, commercial-slide-agent, weekly-update
- **wireframe-annotated** — An annotated / redline lo-fi wireframe — a desktop landing/marketing page drawn as flat greyboxes inside a browser chrome frame, overlaid with numbered annotation pins (①②③④⑤) in a single accent...
  `B:\AI-Armory\templatez\open-design-design-templates\wireframe-annotated`  ·  _tags:_ annotated wireframe, redline, wireframe spec, lo-fi landing, wireframe, low fidelity, 标注线框图, redline 标注
- **wireframe-greybox** — A crisp greybox / blueprint lo-fi wireframe — neutral grey blocks on a pale page, image placeholders drawn as a rectangle with a diagonal X, text shown as solid "lorem bars" of varying widths, sharp...
  `B:\AI-Armory\templatez\open-design-design-templates\wireframe-greybox`  ·  _tags:_ greybox, grey box wireframe, blueprint wireframe, lo-fi dashboard, low fidelity, wireframe, 线框图, 灰盒
- **wireframe-mobile-flow** — A lo-fi multi-screen MOBILE flow wireframe — three or four phone frames laid out in a row on a board, showing a connected user flow (Onboarding → Home feed → Item detail → Confirm).
  `B:\AI-Armory\templatez\open-design-design-templates\wireframe-mobile-flow`  ·  _tags:_ mobile wireframe, app flow, user flow, lo-fi mobile, wireframe, low fidelity, 移动端线框, App 流程图
- **wireframe-sketch** — A hand-drawn wireframe exploration — graph-paper background, marker / pencil tone, multiple tab labels for variants, sticky-note annotations, scribbled chart placeholders, hatched fills.
  `B:\AI-Armory\templatez\open-design-design-templates\wireframe-sketch`  ·  _tags:_ wireframe, sketch wireframe, lo-fi mockup, hand drawn, whiteboard sketch, low fidelity, 手绘原型, 草图, 线框图
- **worker-visualizer** — A real-time data/particle/simulation visualizer whose heavy compute runs in a Web Worker (off the main thread), optionally sharing memory with the UI via SharedArrayBuffer, and renders to a canvas at...
  `B:\AI-Armory\templatez\open-design-design-templates\worker-visualizer`  ·  _tags:_ web worker, worker, simulation, particle system, physics sim, fractal, off main thread, sharedarraybuffer, real-time compute, visualizer, 多线程, 粒子
- **x-research** — X/Twitter public sentiment research for recent market, company, product, or community discourse.
  `B:\AI-Armory\templatez\open-design-design-templates\x-research`  ·  _tags:_ x research, twitter sentiment, x/twitter, what people are saying on x, what twitter says, ct sentiment, public sentiment, social sentiment, 推特情绪, X 上怎么说

</details>

<details><summary><b>(non-skill folders in this category)</b></summary>

- **ECC-scaffolds\** (3 files) — 2 .json · 1 .mdc
  `B:\AI-Armory\templatez\ECC-scaffolds`
- **open-design-prompt-templates\** (107 files) — 106 .json · 1 .png
  `B:\AI-Armory\templatez\open-design-prompt-templates`
- **open-design-templates\** (10 files) — 4 .html · 3 .json · 2 .md · 1 .png
  `B:\AI-Armory\templatez\open-design-templates`

</details>

---

## .rev-agentz

*Dave's agent-home snapshot (.openclaw: agents, workspaces, identity, reference library).*

**122 files**  ·  42 .sample · 34 .md · 14 .json · 12 (none) · 6 .pdf · 3 .epub

- **.openclaw\** (122 files) — 42 .sample · 34 .md · 14 .json · 12 (none) · 6 .pdf · 3 .epub
  `B:\AI-Armory\.rev-agentz\.openclaw`
    - agents\ (13) — 5 .json · 5 .md · 1 .ini · 1 .jsonl
    - canvas\ (1) — 1 .html
    - extensions\ (4) — 2 .json · 1 .md · 1 .ts
    - identity\ (1) — 1 .json
    - logs\ (2) — 1 .json · 1 .jsonl
    - tasks\ (3) — 1 .sqlite · 1 .sqlite-shm · 1 .sqlite-wal
    - workspace\ (28) — 14 .sample · 9 .md · 4 (none) · 1 .json
    - workspace-google\ (26) — 14 .sample · 7 .md · 4 (none) · 1 .json
    - workspace-openai\ (26) — 14 .sample · 7 .md · 4 (none) · 1 .json

---

## adapterz

*Per-tool adapters (claude-code, codex, cursor, gemini-cli, kiro, zed, ECC-integrations).*

**36 files**  ·  29 .ts · 5 .py · 2 .md

<details><summary><b>(loose files)</b> (3)</summary>

- `client-map.ts`
- `detect.ts`
- `types.ts`

</details>

<details><summary><b>antigravity\</b> (1 files)</summary>

- `index.ts`

</details>

<details><summary><b>claude-code\</b> (3 files)</summary>

- `config.ts`
- `hooks.ts`
- `index.ts`

</details>

<details><summary><b>codex\</b> (3 files)</summary>

- `config.ts`
- `hooks.ts`
- `index.ts`

</details>

<details><summary><b>cursor\</b> (3 files)</summary>

- `config.ts`
- `hooks.ts`
- `index.ts`

</details>

<details><summary><b>ECC-integrations\</b> (7 files)</summary>

- `aura\__init__.py`
- `aura\adapter.py`
- `aura\README.md` — AURA trust-check adapter
- `aura\tests\__init__.py`
- `aura\tests\fixtures.py`
- `aura\tests\test_adapter.py`
- `aura\THREAT_MODEL.md` — Threat model — AURA trust-check adapter

</details>

<details><summary><b>gemini-cli\</b> (3 files)</summary>

- `config.ts`
- `hooks.ts`
- `index.ts`

</details>

<details><summary><b>kiro\</b> (2 files)</summary>

- `hooks.ts`
- `index.ts`

</details>

<details><summary><b>openclaw\</b> (4 files)</summary>

- `config.ts`
- `hooks.ts`
- `index.ts`
- `session-db.ts`

</details>

<details><summary><b>opencode\</b> (3 files)</summary>

- `config.ts`
- `hooks.ts`
- `index.ts`

</details>

<details><summary><b>vscode-copilot\</b> (3 files)</summary>

- `config.ts`
- `hooks.ts`
- `index.ts`

</details>

<details><summary><b>zed\</b> (1 files)</summary>

- `index.ts`

</details>

---

## agentz

*Agent / subagent definitions (loose .md + claude-code-best-practice, ECC, gstack).*

**149 files** · **2 skills**  ·  147 .md · 1 .svg · 1 .yaml

<details><summary><b>(loose files)</b> (72)</summary>

- `a11y-architect.md` — Your Role
- `agent-overload-recovery.md` — Antigravity Recovery for Context Overload and Truncation
- `ai-agent-skills.md` — AI Agent Skills
- `antigravity-awesome-skills-vs-awesome-claude-skills.md` — Antigravity Awesome Skills vs Awesome Claude Skills
- `architect.md` — Your Role
- `best-claude-code-skills-github.md` — Best Claude Code Skills on GitHub
- `best-cursor-skills-github.md` — Best Cursor Skills on GitHub
- `build-error-resolver.md` — Build Error Resolver
- `bundles.md` — Antigravity Skill Bundles
- `chief-of-staff.md` — Your Role
- `claude-code-skills.md` — Claude Code Skills
- `code-architect.md` — Code Architect Agent
- `code-explorer.md` — Code Explorer Agent
- `code-reviewer.md` — Review Process
- `code-simplifier.md` — Code Simplifier Agent
- `codex-cli-skills.md` — Codex CLI Skills
- `comment-analyzer.md` — Comment Analyzer Agent
- `conversation-analyzer.md` — Conversation Analyzer Agent
- `cpp-build-resolver.md` — C++ Build Error Resolver
- `cpp-reviewer.md` — Review Priorities
- `csharp-reviewer.md` — Review Priorities
- `cursor-skills.md` — Cursor Skills
- `dart-build-resolver.md` — Dart/Flutter Build Error Resolver
- `database-reviewer.md` — Database Reviewer
- `doc-updater.md` — Documentation & Codemap Specialist
- `docs-lookup.md` — Your Role
- `e2e-runner.md` — E2E Test Runner
- `faq.md` — Frequently Asked Questions (FAQ)
- `flutter-reviewer.md` — Your Role
- `gan-evaluator.md` — Your Role
- `gan-generator.md` — Your Role
- `gan-planner.md` — Your Role
- `gemini-cli-skills.md` — Gemini CLI Skills
- `getting-started.md` — Getting Started with Antigravity Awesome Skills (V10.7.0)
- `go-build-resolver.md` — Go Build Error Resolver
- `go-reviewer.md` — Review Priorities
- `harness-optimizer.md` — Mission
- `healthcare-reviewer.md` — Healthcare Reviewer — Clinical Safety & PHI Compliance
- `java-build-resolver.md` — Java Build Error Resolver
- `java-reviewer.md` — Review Priorities
- `kiro-integration.md` — Kiro CLI Integration Guide
- `kotlin-build-resolver.md` — Kotlin Build Error Resolver
- `kotlin-reviewer.md` — Your Role
- `local-config.md` — Local Skills Configuration
- `loop-operator.md` — Mission
- `metrics-and-sponsorship.md` — Metrics and Sponsorship Playbook
- `opensource-forker.md` — Open-Source Forker
- `opensource-packager.md` — Open-Source Packager
- `opensource-sanitizer.md` — Open-Source Sanitizer
- `performance-optimizer.md` — Performance Optimizer
- `planner.md` — Your Role
- `plugins.md` — Plugins for Claude Code and Codex
- `pr-test-analyzer.md` — PR Test Analyzer Agent
- `python-reviewer.md` — Review Priorities
- `pytorch-build-resolver.md` — PyTorch Build/Runtime Error Resolver
- `refactor-cleaner.md` — Refactor & Dead Code Cleaner
- `rust-build-resolver.md` — Rust Build Error Resolver
- `rust-reviewer.md` — Review Priorities
- `security-reviewer.md` — Security Reviewer
- `security-skills.md` — Security-Related Skills Report
- `seo-specialist.md` — Audit Priorities
- `silent-failure-hunter.md` — Silent Failure Hunter Agent
- `skills-vs-mcp-tools.md` — Skills vs MCP Tools
- `social-launch-copy.md` — Social Launch Copy (X + LinkedIn)
- `tdd-guide.md` — Your Role
- `type-design-analyzer.md` — Type Design Analyzer Agent
- `typescript-reviewer.md` — Review Priorities
- `usage.md` — Usage Guide: How to Actually Use These Skills
- `visual-guide.md` — Visual Quick Start Guide
- `walkthrough.md` — Walkthrough: Release v8.2.0 Maintenance Sweep
- `windows-truncation-recovery.md` — Windows Recovery for Truncation Crash Loops
- `workflows.md` — Antigravity Workflows

</details>

<details><summary><b>claude-code-best-practice\</b> (9 files)</summary>

- `.claude\agents\time-agent.md` — Instructions
- `.claude\commands\time-orchestrator.md` — Time Orchestrator Command
- `.claude\skills\time-fetcher\SKILL.md` — Dubai Time Fetcher
- `.claude\skills\time-svg-creator\examples.md` — Time SVG Creator — Examples
- `.claude\skills\time-svg-creator\reference.md` — Time SVG Creator — Reference
- `.claude\skills\time-svg-creator\SKILL.md` — Time SVG Creator Skill
- `agent-teams-prompt.md` — Create an agent team to build a time orchestration workflow that displays
- `output\dubai-time.svg`
- `output\output.md` — Dubai Time Card

</details>

<details><summary><b>ECC\</b> (67 files)</summary>

- `a11y-architect.md` — Prompt Defense Baseline
- `agent-evaluator.md` — Your Role
- `architect.md` — Prompt Defense Baseline
- `build-error-resolver.md` — Prompt Defense Baseline
- `chief-of-staff.md` — Prompt Defense Baseline
- `code-architect.md` — Prompt Defense Baseline
- `code-explorer.md` — Prompt Defense Baseline
- `code-reviewer.md` — Prompt Defense Baseline
- `code-simplifier.md` — Prompt Defense Baseline
- `comment-analyzer.md` — Prompt Defense Baseline
- `conversation-analyzer.md` — Prompt Defense Baseline
- `cpp-build-resolver.md` — Prompt Defense Baseline
- `cpp-reviewer.md` — Prompt Defense Baseline
- `csharp-reviewer.md` — Prompt Defense Baseline
- `dart-build-resolver.md` — Prompt Defense Baseline
- `database-reviewer.md` — Prompt Defense Baseline
- `django-build-resolver.md` — Prompt Defense Baseline
- `django-reviewer.md` — Prompt Defense Baseline
- `doc-updater.md` — Prompt Defense Baseline
- `docs-lookup.md` — Prompt Defense Baseline
- `e2e-runner.md` — Prompt Defense Baseline
- `fastapi-reviewer.md` — Prompt Defense Baseline
- `flutter-reviewer.md` — Prompt Defense Baseline
- `fsharp-reviewer.md` — Prompt Defense Baseline
- `gan-evaluator.md` — Prompt Defense Baseline
- `gan-generator.md` — Prompt Defense Baseline
- `gan-planner.md` — Prompt Defense Baseline
- `go-build-resolver.md` — Prompt Defense Baseline
- `go-reviewer.md` — Prompt Defense Baseline
- `harmonyos-app-resolver.md` — Prompt Defense Baseline
- `harness-optimizer.md` — Prompt Defense Baseline
- `healthcare-reviewer.md` — Prompt Defense Baseline
- `homelab-architect.md` — Prompt Defense Baseline
- `java-build-resolver.md` — Prompt Defense Baseline
- `java-reviewer.md` — Prompt Defense Baseline
- `kotlin-build-resolver.md` — Prompt Defense Baseline
- `kotlin-reviewer.md` — Prompt Defense Baseline
- `loop-operator.md` — Prompt Defense Baseline
- `marketing-agent.md` — Prompt Defense Baseline
- `mle-reviewer.md` — Prompt Defense Baseline
- `network-architect.md` — Prompt Defense Baseline
- `network-config-reviewer.md` — Prompt Defense Baseline
- `network-troubleshooter.md` — Prompt Defense Baseline
- `opensource-forker.md` — Prompt Defense Baseline
- `opensource-packager.md` — Prompt Defense Baseline
- `opensource-sanitizer.md` — Prompt Defense Baseline
- `performance-optimizer.md` — Prompt Defense Baseline
- `php-reviewer.md` — Prompt Defense Baseline
- `planner.md` — Prompt Defense Baseline
- `pr-test-analyzer.md` — Prompt Defense Baseline
- `python-reviewer.md` — Prompt Defense Baseline
- `pytorch-build-resolver.md` — Prompt Defense Baseline
- `react-build-resolver.md` — Prompt Defense Baseline
- `react-reviewer.md` — Prompt Defense Baseline
- `refactor-cleaner.md` — Prompt Defense Baseline
- `rust-build-resolver.md` — Prompt Defense Baseline
- `rust-reviewer.md` — Prompt Defense Baseline
- `security-reviewer.md` — Prompt Defense Baseline
- `seo-specialist.md` — Prompt Defense Baseline
- `silent-failure-hunter.md` — Prompt Defense Baseline
- `spec-miner.md` — Tool guardrails
- `swift-build-resolver.md` — Prompt Defense Baseline
- `swift-reviewer.md` — Prompt Defense Baseline
- `tdd-guide.md` — Prompt Defense Baseline
- `type-design-analyzer.md` — Prompt Defense Baseline
- `typescript-reviewer.md` — Prompt Defense Baseline
- `vue-reviewer.md` — Prompt Defense Baseline

</details>

<details><summary><b>gstack\</b> (1 files)</summary>

- `openai.yaml`

</details>

---

## apiz

*API catalogs by domain + Apify generator.*

**21 files**  ·  19 .md · 2 .js

<details><summary><b>agents-apis-697\</b> (1 files)</summary>

- `README.md` — Agents

</details>

<details><summary><b>ai-apis-1208\</b> (1 files)</summary>

- `README.md` — AI

</details>

<details><summary><b>automation-apis-4825\</b> (1 files)</summary>

- `README.md` — Automation

</details>

<details><summary><b>business-apis-2\</b> (1 files)</summary>

- `README.md` — Business

</details>

<details><summary><b>developer-tools-apis-2652\</b> (1 files)</summary>

- `README.md` — Developer Tools

</details>

<details><summary><b>ecommerce-apis-2440\</b> (1 files)</summary>

- `README.md` — Ecommerce

</details>

<details><summary><b>integrations-apis-890\</b> (1 files)</summary>

- `README.md` — Integrations

</details>

<details><summary><b>jobs-apis-848\</b> (1 files)</summary>

- `README.md` — Jobs

</details>

<details><summary><b>lead-generation-apis-3452\</b> (1 files)</summary>

- `README.md` — Lead Generation

</details>

<details><summary><b>mcp-servers-apis-131\</b> (1 files)</summary>

- `README.md` — MCP Servers

</details>

<details><summary><b>news-apis-590\</b> (1 files)</summary>

- `README.md` — News

</details>

<details><summary><b>open-source-apis-768\</b> (1 files)</summary>

- `README.md` — Open Source

</details>

<details><summary><b>other-apis-1297\</b> (1 files)</summary>

- `README.md` — Other

</details>

<details><summary><b>real-estate-apis-851\</b> (1 files)</summary>

- `README.md` — Real Estate

</details>

<details><summary><b>seo-tools-apis-710\</b> (1 files)</summary>

- `README.md` — SEO Tools

</details>

<details><summary><b>settings\</b> (3 files)</summary>

- `APIFY_ACTORS.md` — Apify Actors List
- `fetch_apify_actors.js`
- `generate_readme_clean.js`

</details>

<details><summary><b>social-media-apis-3268\</b> (1 files)</summary>

- `README.md` — Social Media

</details>

<details><summary><b>travel-apis-397\</b> (1 files)</summary>

- `README.md` — Travel

</details>

<details><summary><b>videos-apis-979\</b> (1 files)</summary>

- `README.md` — Videos

</details>

---

## cheatsheetz

*Language / tool cheatsheets.*

**60 files**  ·  22 .docx · 20 .txt · 9 .js · 3 .sh · 2 .php · 1 .html

<details><summary><b>(loose files)</b> (60)</summary>

- `angular.docx`
- `angular.js`
- `angular.txt` — /* *******************************************************************************************
- `angularjs.docx`
- `angularjs.js`
- `angularjs.txt` — /* *******************************************************************************************
- `bash.docx`
- `bash.sh`
- `bash.txt` — SHORTCUTS and HISTORY
- `C.docx`
- `C.txt` — main() Function
- `C#.docx`
- `C#.txt` — CHEATSHEET C#
- `CHEAT-SHEETS.zip`
- `CheatSheet-Python-4_-Classes.docx`
- `CheatSheet-Python-5_-Functions-and-Tricks.docx`
- `CheatSheet-Python-7_-NumPy-1.pdf`
- `django.docx`
- `django.py`
- `django.txt` — *****************************************************************************
- `docker.docx`
- `docker.sh`
- `docker.txt` — DOCKER
- `ember.docx`
- `ember.js`
- `ember.txt` — /*
- `feathers.docx`
- `feathers.js`
- `feathers.txt` — Provides the ability to initialize new application instances
- `html5.docx`
- `html5.html`
- `html5.txt` — <!-- * *******************************************************************************************
- `javascript.docx`
- `javascript.js`
- `javascript.txt` — /* *******************************************************************************************
- `laravel.docx`
- `laravel.php`
- `laravel.txt` — <?php
- `molecular.docx`
- `molecular.js`
- `molecular.txt` — /* *******************************************************************************************
- `php.docx`
- `php.php`
- `php.txt` — <?php
- `react.docx`
- `react.js`
- `react.txt` — /* *******************************************************************************************
- `redis.docx`
- `redis.sh`
- `redis.txt` — *****************************************************************************
- `sails.docx`
- `sails.js`
- `sails.txt` — /********************************************************************************************
- `vim.docx`
- `vim.txt` — VIM CHEATSHEET
- `vue.docx`
- `vue.js`
- `vue.txt` — /* *******************************************************************************************
- `xcode.docx`
- `xcode.txt` — XCODE CHEAT SHEET

</details>

---

## codez

*Harvested source code & reference implementations (openclaw-hermes, awesome-repo-automation).*

**775 files**  ·  624 .py · 71 .md · 24 .ts · 14 .js · 10 .json · 9 .png

- **awesome-repo-automation\** (169 files) — 70 .md · 24 .ts · 19 .py · 14 .js · 10 .json · 9 .png
  `B:\AI-Armory\codez\awesome-repo-automation`
    - assets\ (12) — 9 .png · 3 .svg
    - catalog-data\ (62) — 50 .md · 10 .json · 2 .csv
    - maintainer-docs\ (22) — 20 .md · 2 .csv
    - resource-pipeline\ (7) — 7 .py
    - scripts\ (57) — 24 .ts · 14 .js · 7 .cjs · 6 .sh
    - tests\ (5) — 5 .py
    - ticker\ (4) — 4 .py
- **openclaw-hermes\** (606 files) — 605 .py · 1 .md
  `B:\AI-Armory\codez\openclaw-hermes`
    - core\ (51) — 51 .py
    - gateway\ (211) — 211 .py
    - platforms\ (41) — 40 .py · 1 .md
    - tests-agent\ (74) — 74 .py
    - tests-cli\ (155) — 155 .py
    - tests-skills\ (7) — 7 .py
    - tools\ (67) — 67 .py

---

## commandz

*Slash commands (loose + ECC + ponytail).*

**182 files**  ·  176 .md · 6 .toml

<details><summary><b>(loose files)</b> (82)</summary>

- `agent-sort.md` — Agent Sort (Legacy Shim)
- `aside.md` — Aside Command
- `build-fix.md` — Build and Fix
- `checkpoint.md` — Checkpoint Command
- `claw.md` — Claw Command (Legacy Shim)
- `code-review.md` — Code Review
- `commit-push-pr.md` — Context
- `context-budget.md` — Context Budget Optimizer (Legacy Shim)
- `cpp-build.md` — C++ Build and Fix
- `cpp-review.md` — C++ Code Review
- `cpp-test.md` — C++ TDD Command
- `dedupe.md` — ---
- `devfleet.md` — DevFleet (Legacy Shim)
- `docs.md` — Docs Command (Legacy Shim)
- `e2e.md` — E2E Command (Legacy Shim)
- `eval.md` — Eval Command (Legacy Shim)
- `evolve.md` — Evolve Command
- `feature-dev.md` — Phases
- `flutter-build.md` — Flutter Build and Fix
- `flutter-review.md` — Flutter Code Review
- `flutter-test.md` — Flutter Test
- `gan-build.md` — GAN-Style Harness Build
- `gan-design.md` — GAN-Style Design Harness
- `go-build.md` — Go Build and Fix
- `go-review.md` — Go Code Review
- `go-test.md` — Go TDD Command
- `gradle-build.md` — Gradle Build Fix
- `harness-audit.md` — Harness Audit Command
- `hookify-configure.md` — Steps
- `hookify-help.md` — Hook System Overview
- `hookify-list.md` — Steps
- `hookify.md` — Usage
- `instinct-export.md` — Instinct Export Command
- `instinct-import.md` — Instinct Import Command
- `instinct-status.md` — Instinct Status Command
- `jira.md` — Jira Command
- `kotlin-build.md` — Kotlin Build and Fix
- `kotlin-review.md` — Kotlin Code Review
- `kotlin-test.md` — Kotlin TDD Command
- `learn-eval.md` — /learn-eval - Extract, Evaluate, then Save
- `learn.md` — /learn - Extract Reusable Patterns
- `loop-start.md` — Loop Start Command
- `loop-status.md` — Loop Status Command
- `model-route.md` — Model Route Command
- `multi-backend.md` — Backend - Backend-Focused Development
- `multi-execute.md` — Execute - Multi-Model Collaborative Execution
- `multi-frontend.md` — Frontend - Frontend-Focused Development
- `multi-plan.md` — Plan - Multi-Model Collaborative Planning
- `multi-workflow.md` — Workflow - Multi-Model Collaborative Development
- `orchestrate.md` — Orchestrate Command (Legacy Shim)
- `plan.md` — Plan Command
- `pm2.md` — PM2 Init
- `projects.md` — Projects Command
- `promote.md` — Promote Command
- `prompt-optimize.md` — Prompt Optimize (Legacy Shim)
- `prp-commit.md` — Smart Commit
- `prp-implement.md` — PRP Implement
- `prp-plan.md` — PRP Plan
- `prp-pr.md` — Create Pull Request
- `prp-prd.md` — Product Requirements Document Generator
- `prune.md` — Prune Pending Instincts
- `python-review.md` — Python Code Review
- `quality-gate.md` — Quality Gate Command
- `refactor-clean.md` — Refactor Clean
- `resume-session.md` — Resume Session Command
- `review-pr.md` — Usage
- `rules-distill.md` — Rules Distill (Legacy Shim)
- `rust-build.md` — Rust Build and Fix
- `rust-review.md` — Rust Code Review
- `rust-test.md` — Rust TDD Command
- `santa-loop.md` — Santa Loop
- `save-session.md` — Save Session Command
- `sessions.md` — Sessions Command
- `setup-pm.md` — Package Manager Setup
- `skill-create.md` — /skill-create - Local Skill Generation
- `skill-health.md` — Skill Health Dashboard
- `tdd.md` — TDD Command (Legacy Shim)
- `test-coverage.md` — Test Coverage
- `triage-issue.md` — ---
- `update-codemaps.md` — Update Codemaps
- `update-docs.md` — Update Documentation
- `verify.md` — Verification Command (Legacy Shim)

</details>

<details><summary><b>ECC\</b> (94 files)</summary>

- `aside.md` — Aside Command
- `auto-update.md` — Auto Update
- `build-fix.md` — Build and Fix
- `checkpoint.md` — Checkpoint Command
- `code-review.md` — Code Review
- `cost-report.md` — Cost Report
- `cpp-build.md` — C++ Build and Fix
- `cpp-review.md` — C++ Code Review
- `cpp-test.md` — C++ TDD Command
- `ecc-guide.md` — /ecc-guide
- `epic-claim.md` — /epic-claim
- `epic-decompose.md` — /epic-decompose
- `epic-publish.md` — /epic-publish
- `epic-review.md` — /epic-review
- `epic-sync.md` — /epic-sync
- `epic-unblock.md` — /epic-unblock
- `epic-validate.md` — /epic-validate
- `evolve.md` — Evolve Command
- `fastapi-review.md` — FastAPI Review
- `feature-dev.md` — Phases
- `flutter-build.md` — Flutter Build and Fix
- `flutter-review.md` — Flutter Code Review
- `flutter-test.md` — Flutter Test
- `gan-build.md` — GAN-Style Harness Build
- `gan-design.md` — GAN-Style Design Harness
- `go-build.md` — Go Build and Fix
- `go-review.md` — Go Code Review
- `go-test.md` — Go TDD Command
- `gradle-build.md` — Gradle Build Fix
- `harness-audit.md` — Harness Audit Command
- `hookify-configure.md` — Steps
- `hookify-help.md` — Hook System Overview
- `hookify-list.md` — Steps
- `hookify.md` — Usage
- `instinct-export.md` — Instinct Export Command
- `instinct-import.md` — Instinct Import Command
- `instinct-status.md` — Instinct Status Command
- `jira.md` — Jira Command
- `kotlin-build.md` — Kotlin Build and Fix
- `kotlin-review.md` — Kotlin Code Review
- `kotlin-test.md` — Kotlin TDD Command
- `learn-eval.md` — /learn-eval - Extract, Evaluate, then Save
- `learn.md` — /learn - Extract Reusable Patterns
- `loop-start.md` — Loop Start Command
- `loop-status.md` — Loop Status Command
- `marketing-campaign.md` — /marketing-campaign
- `model-route.md` — Model Route Command
- `multi-backend.md` — Backend - Backend-Focused Development
- `multi-execute.md` — Execute - Multi-Model Collaborative Execution
- `multi-frontend.md` — Frontend - Frontend-Focused Development
- `multi-plan.md` — Plan - Multi-Model Collaborative Planning
- `multi-workflow.md` — Workflow - Multi-Model Collaborative Development
- `orch-add-feature.md` — /orch-add-feature
- `orch-build-mvp.md` — /orch-build-mvp
- `orch-change-feature.md` — /orch-change-feature
- `orch-fix-defect.md` — /orch-fix-defect
- `orch-refine-code.md` — /orch-refine-code
- `orch-review.md` — /orch-review
- `plan-canvas.md` — Plan Canvas Command
- `plan-prd.md` — PRD Command
- `plan.md` — Plan Command
- `pm2.md` — PM2 Init
- `pr.md` — Create Pull Request
- `project-init.md` — /project-init
- `projects.md` — Projects Command
- `promote.md` — Promote Command
- `prp-commit.md` — Smart Commit
- `prp-implement.md` — PRP Implement
- `prp-plan.md` — PRP Plan
- `prp-pr.md` — Create Pull Request
- `prp-prd.md` — Product Requirements Document Generator
- `prune.md` — Prune Pending Instincts
- `python-review.md` — Python Code Review
- `quality-gate.md` — Quality Gate Command
- `react-build.md` — React Build and Fix
- `react-review.md` — React Code Review
- `react-test.md` — React TDD Command
- `refactor-clean.md` — Refactor Clean
- `resume-session.md` — Resume Session Command
- `review-pr.md` — Usage
- `rust-build.md` — Rust Build and Fix
- `rust-review.md` — Rust Code Review
- `rust-test.md` — Rust TDD Command
- `santa-loop.md` — Santa Loop
- `save-session.md` — Save Session Command
- `security-scan.md` — Security Scan Command
- `sessions.md` — Sessions Command
- `setup-pm.md` — Package Manager Setup
- `skill-create.md` — /skill-create - Local Skill Generation
- `skill-health.md` — Skill Health Dashboard
- `test-coverage.md` — Test Coverage
- `update-codemaps.md` — Update Codemaps
- `update-docs.md` — Update Documentation
- `vue-review.md` — Vue Code Review

</details>

<details><summary><b>ponytail\</b> (6 files)</summary>

- `ponytail-audit.toml`
- `ponytail-debt.toml`
- `ponytail-gain.toml`
- `ponytail-help.toml`
- `ponytail-review.toml`
- `ponytail.toml`

</details>

---

## contextz

*Captured system prompts + context files.*

**113 files**  ·  83 .txt · 17 .json · 9 .md · 2 .yaml · 1 (none) · 1 .png

<details><summary><b>(loose files)</b> (3)</summary>

- `dev.md` — Development Context
- `research.md` — Research Context
- `review.md` — Code Review Context

</details>

<details><summary><b>ECC\</b> (3 files)</summary>

- `dev.md` — Development Context
- `research.md` — Research Context
- `review.md` — Code Review Context

</details>

<details><summary><b>system-prompts-and-models\</b> (107 files)</summary>

- `Amp\claude-4-sonnet.yaml`
- `Amp\gpt-5.yaml`
- `Amp\README.md` — How to obtain the system prompt for [Amp](https://ampcode.com)
- `Amp\view-thread-yaml.png`
- `Anthropic\Claude Code 2.0.txt` — Claude Code Version 2.0.0
- `Anthropic\Claude Code\Prompt.txt` — Tone and style
- `Anthropic\Claude Code\Tools.json`
- `Anthropic\Claude Fable 5.txt` — claude_behavior
- `Anthropic\Claude for Chrome\Prompt.txt` — You are a web automation assistant with browser tools. The assistant is Claude, created by Anthropic. Your priority i...
- `Anthropic\Claude for Chrome\Tools.json`
- `Anthropic\Claude Sonnet 4.6.txt` — <claude_behavior>
- `Anthropic\Claude Sonnet 5 Tools.txt` — ask_user_input_v0
- `Anthropic\Claude Sonnet 5.txt` — <claude_behavior>
- `Anthropic\Sonnet 4.5 Prompt.txt` — The assistant is Claude, created by Anthropic. The current date is Monday, September 29, 2025.
- `Augment Code\claude-4-sonnet-agent-prompts.txt` — Role
- `Augment Code\claude-4-sonnet-tools.json`
- `Augment Code\gpt-5-agent-prompts.txt` — Role
- `Augment Code\gpt-5-tools.json`
- `Cluely\Default Prompt.txt` — <core_identity>
- `Cluely\Enterprise Prompt.txt` — <core_identity>
- `CodeBuddy Prompts\Chat Prompt.txt` — CodeBuddy Visible Files
- `CodeBuddy Prompts\Craft Prompt.txt` — Tool Use Guidelines
- `Comet Assistant\System Prompt.txt` — <general_behavioral_instructions>
- `Comet Assistant\tools.json`
- `Cursor Prompts\Agent CLI Prompt 2025-08-07.txt` — You are an AI coding assistant, powered by GPT-5.
- `Cursor Prompts\Agent Prompt 2.0.txt` — Tools
- `Cursor Prompts\Agent Prompt 2025-09-03.txt` — You are an AI coding assistant, powered by GPT-5. You operate in Cursor.
- `Cursor Prompts\Agent Prompt v1.0.txt` — You are an AI coding assistant, powered by Claude Sonnet 4. You operate in Cursor.
- `Cursor Prompts\Agent Prompt v1.2.txt` — Knowledge cutoff: 2024-06
- `Cursor Prompts\Agent Tools v1.0.json`
- `Cursor Prompts\Chat Prompt.txt` — You are a an AI coding assistant, powered by GPT-4o. You operate in Cursor
- `Devin AI\DeepWiki Prompt.txt` — BACKGROUND
- `Devin AI\Prompt.txt` — You are Devin, a software engineer using a real computer operating system. You are a real code-wiz: few programmers a...
- `dia\Prompt.txt` — General Instructions
- `Emergent\Prompt.txt` — You are E1, the most powerful, intelligent & creative agent developed by Emergent to help users build ambitious appli...
- `Emergent\Tools.json`
- `Google\Antigravity\Fast Prompt.txt` — Technology Stack,
- `Google\Antigravity\planning-mode.txt` — Markdown Formatting
- `Google\Gemini\AI Studio vibe-coder.txt` — SPECIAL INSTRUCTION: think silently if needed
- `Junie\Prompt.txt` — ENVIRONMENT
- `Kiro\Mode_Clasifier_Prompt.txt` — Category Definitions
- `Kiro\Spec_Prompt.txt` — System Prompt
- `Kiro\Vibe_Prompt.txt` — Identity
- `Leap.new\Prompts.txt` — You are Leap, an expert AI assistant and exceptional senior software developer with vast knowledge of REST API backen...
- `Leap.new\tools.json`
- `LICENSE.md` — GNU GENERAL PUBLIC LICENSE
- `Lovable\Agent Prompt.txt` — General Guidelines
- `Lovable\Agent Tools.json`
- `Manus Agent Tools & Prompt\Agent loop.txt` — You are Manus, an AI agent created by the Manus team.
- `Manus Agent Tools & Prompt\Modules.txt` — You are Manus, an AI agent created by the Manus team.
- `Manus Agent Tools & Prompt\Prompt.txt` — Manus AI Assistant Capabilities
- `Manus Agent Tools & Prompt\tools.json`
- `NotionAi\Prompt.txt` — Pages
- `NotionAi\tools.json`
- `Open Source prompts\Bolt\Prompt.txt` — You are Bolt, an expert AI assistant and exceptional senior software developer with vast knowledge across multiple pr...
- `Open Source prompts\Cline\Prompt.txt` — Tool Use Formatting
- `Open Source prompts\Codex CLI\openai-codex-cli-system-prompt-20250820.txt` — How you work
- `Open Source prompts\Codex CLI\Prompt.txt` — You are operating as and within the Codex CLI, a terminal-based agentic coding assistant built by OpenAI. It wraps Op...
- `Open Source prompts\Gemini CLI\google-gemini-cli-system-prompt.txt` — Core Mandates
- `Open Source prompts\Lumo\Prompt.txt` — Identity & Personality
- `Open Source prompts\RooCode\Prompt.txt` — You are Roo, a highly skilled software engineer with extensive knowledge in many programming languages, frameworks, d...
- `Orchids.app\Decision-making prompt.txt` — Knowledge cutoff: 2024-06
- `Orchids.app\System Prompt.txt` — You are a powerful agentic AI coding assistant called Orchids working with a Next.js 15 + Shadcn/UI TypeScript project.
- `Perplexity\Prompt.txt` — <goal> You are Perplexity, a helpful search assistant trained by Perplexity AI. Your goal is to write an accurate, de...
- `Poke\Poke agent.txt` — You are the assistant of Poke by the Interaction Company of California. You are the "execution engine" of Poke, helpi...
- `Poke\Poke_p1.txt` — You are Poke, and you were developed by The Interaction Company of California, a Palo Alto-based AI startup (short na...
- `Poke\Poke_p2.txt` — WhatsApp Limitations
- `Poke\Poke_p3.txt` — Handling user frustration and mistakes
- `Poke\Poke_p4.txt` — Integrations
- `Poke\Poke_p5.txt` — Email Links Protocol:
- `Poke\Poke_p6.txt` — Memory and Context:
- `Qoder\prompt.txt` — Qoder AI Assistant System Prompt
- `Qoder\Quest Action.txt` — You are Qoder, a powerful AI coding assistant, integrated with a fantastic agentic IDE to work both independently and...
- `Qoder\Quest Design.txt` — AI Assistant Identity
- `README.md` — [Make your AI agents self-healing](https://github.com/latitude-dev/latitude-llm)
- `Replit\Prompt.txt` — <identity>
- `Replit\Tools.json`
- `Same.dev\Prompt.txt` — Knowledge cutoff: 2024-06
- `Same.dev\Tools.json`
- `Trae\Builder Prompt.txt` — You are a powerful agentic AI coding assistant. You operate exclusively in Trae AI, the world's best IDE.
- `Trae\Builder Tools.json`
- `Trae\Chat Prompt.txt` — <identity>
- `Traycer AI\phase_mode_prompts.txt` — You are `@traycerai` (aka `Traycer.AI`), a large language model based on the state-of-the-art architecture. Never men...
- `Traycer AI\phase_mode_tools.json`
- `Traycer AI\plan_mode_prompts`
- `Traycer AI\plan_mode_tools.json`
- `v0 Prompts and Tools\Prompt.txt` — Overview
- `v0 Prompts and Tools\Tools.json`
- `VSCode Agent\chat-titles.txt` — You are an expert in crafting pithy titles for chatbot conversations. You are presented with a chat conversation, and...
- `VSCode Agent\claude-sonnet-4.txt` — You are an expert AI programming assistant, working with a user in the VS Code editor.
- `VSCode Agent\gemini-2.5-pro.txt` — You are an expert AI programming assistant, working with a user in the VS Code editor.
- `VSCode Agent\gpt-4.1.txt` — You are an expert AI programming assistant, working with a user in the VS Code editor.
- `VSCode Agent\gpt-4o.txt` — You are an expert AI programming assistant, working with a user in the VS Code editor.
- `VSCode Agent\gpt-5-mini.txt` — You are an expert AI programming assistant, working with a user in the VS Code editor.
- `VSCode Agent\gpt-5.txt` — You are an expert AI programming assistant, working with a user in the VS Code editor.
- `VSCode Agent\nes-tab-completion.txt` — Steps
- `VSCode Agent\Prompt.txt` — Answer the user's request using the relevant tool(s), if they are available. Check that all the required parameters f...
- `Warp.dev\Prompt.txt` — Question
- `Windsurf\Prompt Wave 11.txt` — Knowledge cutoff: 2024-06
- `Windsurf\Tools Wave 11.txt` — // Spin up a browser preview for a web server. This allows the USER to interact with the web server normally as well ...
- `Xcode\DocumentAction.txt` — The user is curently inside this file: {{filename}}
- `Xcode\ExplainAction.txt` — The user is curently inside this file: {{filename}}
- `Xcode\MessageAction.txt` — The user is curently inside this file: {{filename}}
- `Xcode\PlaygroundAction.txt` — The user is curently inside this file: {{filename}}
- `Xcode\PreviewAction.txt` — The user is curently inside this file: {{filename}}
- `Xcode\System.txt` — You are a coding assistant--with access to tools--specializing in analyzing codebases. Below is the content of the fi...
- `Z.ai Code\prompt.txt` — Instructions

</details>

---

## docz

*Docs incl. ai-alignment reading.*

**24 files**  ·  15 .md · 3 .docx · 3 .jpg · 3 .pdf

<details><summary><b>(loose files)</b> (7)</summary>

- `anti-pattern-cleanup-plan.md` — Error Handling Anti-Pattern Cleanup Plan
- `architecture-overview.md` — claude-mem Architecture Overview
- `PR-SHIPPING-REPORT.md` — Claude-Mem PR Shipping Report
- `production-guide.md` — claude-mem Production Guide
- `README.md` — Claude Context Documentation
- `SESSION_ID_ARCHITECTURE.md` — Session ID Architecture
- `VERSION_FIX.md` — Version Consistency Fix (Issue #XXX)

</details>

<details><summary><b>ai-alignment\</b> (10 files)</summary>

- `AGI safety from first principles.pdf`
- `AI_Fluency_vocabulary_cheat_sheet.pdf`
- `Claude-Commands.jpg`
- `Create-Your-First-Loop.jpg`
- `Gemini-Mastermind.jpg`
- `prompt-injection-at-scale.md` — Prompt injection at scale: the tool/user boundary is forgeable, and the biggest model I tested was the worst
- `Structural-Role-Injection-in-Handlebars-Templated.pdf`
- `The most important century blog post series.docx`
- `Why AI alignment could be hard with modern deep learning.docx`
- `Work-In-Technical-AI-Alignment-Guide.docx`

</details>

<details><summary><b>dive-deep\</b> (2 files)</summary>

- `asynchronous-indexing-workflow.md` — Asynchronous Indexing Workflow
- `file-inclusion-rules.md` — File Inclusion & Exclusion Rules

</details>

<details><summary><b>getting-started\</b> (3 files)</summary>

- `environment-variables.md` — Environment Variables Configuration
- `prerequisites.md` — Prerequisites
- `quick-start.md` — Quick Start Guide

</details>

<details><summary><b>troubleshooting\</b> (2 files)</summary>

- `faq.md` — Frequently Asked Questions (FAQ)
- `troubleshooting-guide.md` — Troubleshooting Guide

</details>

---

## fontz

*Font library — .ttf / .otf / .woff face files and packaged .zip font kits.*

**1308 files**  ·  506 .ttf · 441 .zip · 344 .otf · 14 .woff · 1 .7z · 1 .png

- **_otfs\** (344 files) — 344 .otf
  `B:\AI-Armory\fontz\_otfs`
- **_ttfs\** (507 files) — 506 .ttf · 1 .png
  `B:\AI-Armory\fontz\_ttfs`
- **_woffs\** (15 files) — 14 .woff · 1 .woff2
  `B:\AI-Armory\fontz\_woffs`
- **_zips\** (442 files) — 441 .zip · 1 .7z
  `B:\AI-Armory\fontz\_zips`

---

## hookz

*Hooks: claude-hook-router (.mjs routing/session system), ECC, ponytail, examples.*

**47 files**  ·  22 .mjs · 10 .md · 6 .js · 6 .json · 1 .ps1 · 1 .py

<details><summary><b>(loose files)</b> (2)</summary>

- `bash_command_validator_example.py`
- `cursorrules-template.md` — Claude-Mem Rules for Cursor

</details>

<details><summary><b>claude-hook-router\</b> (30 files)</summary>

- `CONTEXT-INJECTION.md` — Context Injection in Cursor Hooks
- `formatter-claude-code.mjs`
- `formatter-cursor.mjs`
- `formatter-gemini-cli.mjs`
- `formatter-vscode-copilot.mjs`
- `formatters.mjs`
- `hooks.json`
- `INTEGRATION.md` — Claude-Mem ↔ Cursor Integration Architecture
- `mcp-ready.mjs`
- `PARITY.md` — Feature Parity: Claude-Mem Hooks vs Cursor Hooks
- `posttooluse.mjs`
- `precompact.mjs`
- `pretooluse.mjs`
- `QUICKSTART.md` — Quick Start: Claude-Mem + Cursor Integration
- `README.md` — Hooks
- `REVIEW.md` — Comprehensive Review: Cursor Hooks Integration
- `routing-block.mjs`
- `routing.mjs`
- `session-db.bundle.mjs`
- `session-directive.mjs`
- `session-extract.bundle.mjs`
- `session-helpers.mjs`
- `session-loaders.mjs`
- `session-snapshot.bundle.mjs`
- `sessionstart.mjs`
- `STANDALONE-SETUP.md` — Claude-Mem for Cursor (No Claude Code Required)
- `stdin.mjs`
- `suppress-stderr.mjs`
- `tool-naming.mjs`
- `userpromptsubmit.mjs`

</details>

<details><summary><b>ECC\</b> (4 files)</summary>

- `hooks.json`
- `memory-persistence\hooks.json`
- `memory-persistence\README.md` — Memory Persistence Hooks
- `README.md` — Hooks

</details>

<details><summary><b>ponytail\</b> (11 files)</summary>

- `claude-codex-hooks.json`
- `copilot-hooks.json`
- `ponytail-activate.js`
- `ponytail-config.js`
- `ponytail-instructions.js`
- `ponytail-mode-tracker.js`
- `ponytail-runtime.js`
- `ponytail-statusline.ps1`
- `ponytail-statusline.sh`
- `ponytail-subagent.js`
- `qoder-hooks.json`

</details>

---

## mcpz

*MCP servers & configs.*

**6 files**  ·  3 .js · 2 .json · 1 .md

<details><summary><b>ECC-mcp-configs\</b> (1 files)</summary>

- `mcp-servers.json`

</details>

<details><summary><b>ponytail\</b> (5 files)</summary>

- `index.js`
- `instructions.js`
- `package.json`
- `README.md` — ponytail-mcp
- `test\instructions.test.js`

</details>

---

## planz

*ECC workflows.*

**2 files**  ·  1 .js · 1 .md

<details><summary><b>ECC-workflows\</b> (2 files)</summary>

- `orch-review.workflow.js`
- `README.md` — ECC native workflows (pilot)

</details>

---

## resourcez

*Reference data (open-design design systems, patterns, schemas).*

**4027 files**  ·  1954 .html · 914 .json · 848 .md · 302 .css · 4 .ipynb · 2 .png

- **claude-cookbooks-patterns\** (9 files) — 4 .ipynb · 4 .md · 1 .py
  `B:\AI-Armory\resourcez\claude-cookbooks-patterns`
    - agents\ (9) — 4 .ipynb · 4 .md · 1 .py
- **ECC-manifests\** (3 files) — 3 .json
  `B:\AI-Armory\resourcez\ECC-manifests`
- **ECC-schemas\** (10 files) — 10 .json
  `B:\AI-Armory\resourcez\ECC-schemas`
- **open-design-design-systems\** (4005 files) — 1954 .html · 901 .json · 844 .md · 302 .css · 2 .png · 2 .ts
  `B:\AI-Armory\resourcez\open-design-design-systems`
    - _schema\ (4) — 2 .ts · 1 .md · 1 .css
    - agentic\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - airbnb\ (41) — 20 .md · 13 .html · 6 .json · 2 .css
    - airtable\ (41) — 20 .md · 13 .html · 6 .json · 2 .css
    - ant\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - apple\ (41) — 20 .md · 13 .html · 6 .json · 2 .css
    - application\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - arc\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - artistic\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - atelier-zero\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - bento\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - binance\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - bmw\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - bmw-m\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - bold\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - brutalism\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - bugatti\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - cafe\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - cal\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - canva\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - cisco\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - claude\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - clay\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - claymorphism\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - clean\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - clickhouse\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - cohere\ (41) — 20 .md · 13 .html · 6 .json · 2 .css
    - coinbase\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - colorful\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - composio\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - contemporary\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - corporate\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - cosmic\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - creative\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - cursor\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - dashboard\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - default\ (27) — 16 .html · 6 .json · 3 .md · 2 .css
    - discord\ (41) — 20 .md · 13 .html · 6 .json · 2 .css
    - dithered\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - doodle\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - dramatic\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - duolingo\ (41) — 20 .md · 13 .html · 6 .json · 2 .css
    - editorial\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - elegant\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - elevenlabs\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - energetic\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - enterprise\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - expo\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - expressive\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - fantasy\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - ferrari\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - figma\ (41) — 20 .md · 13 .html · 6 .json · 2 .css
    - flat\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - framer\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - friendly\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - futuristic\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - github\ (41) — 20 .md · 13 .html · 6 .json · 2 .css
    - glassmorphism\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - gradient\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - hashicorp\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - hud\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - huggingface\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - ibm\ (41) — 20 .md · 13 .html · 6 .json · 2 .css
    - intercom\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - kami\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - kraken\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - lamborghini\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - levels\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - linear-app\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - lingo\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - loom\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - lovable\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - luxury\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - mastercard\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - material\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - meta\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - minimal\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - minimax\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - mintlify\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - miro\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - mission-control\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - mistral-ai\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - modern\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - mongodb\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - mono\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - neobrutalism\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - neon\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - neumorphism\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - nike\ (41) — 20 .md · 13 .html · 6 .json · 2 .css
    - notion\ (41) — 20 .md · 13 .html · 6 .json · 2 .css
    - nvidia\ (41) — 20 .md · 13 .html · 6 .json · 2 .css
    - ollama\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - openai\ (41) — 20 .md · 13 .html · 6 .json · 2 .css
    - opencode-ai\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - pacman\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - paper\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - perplexity\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - perspective\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - pinterest\ (41) — 20 .md · 13 .html · 6 .json · 2 .css
    - playstation\ (41) — 20 .md · 13 .html · 6 .json · 2 .css
    - posthog\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - premium\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - professional\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - publication\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - raycast\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - refined\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - renault\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - replicate\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - resend\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - retro\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - revolut\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - runwayml\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - sanity\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - sentry\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - shadcn\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - shopify\ (41) — 20 .md · 13 .html · 6 .json · 2 .css
    - simple\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - skeumorphism\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - slack\ (41) — 20 .md · 13 .html · 6 .json · 2 .css
    - sleek\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - spacex\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - spacious\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - spotify\ (41) — 20 .md · 13 .html · 6 .json · 2 .css
    - starbucks\ (41) — 20 .md · 13 .html · 6 .json · 2 .css
    - storytelling\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - stripe\ (41) — 20 .md · 13 .html · 6 .json · 2 .css
    - supabase\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - superhuman\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - tesla\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - tetris\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - theverge\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - together-ai\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - tom-modern\ (6) — 2 .png · 1 .css · 1 .html · 1 .json
    - totality-festival\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - trading-terminal\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - uber\ (41) — 20 .md · 13 .html · 6 .json · 2 .css
    - urdu\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - vercel\ (41) — 20 .md · 13 .html · 6 .json · 2 .css
    - vibrant\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - vintage\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - vodafone\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - voltagent\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - warm-editorial\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - warp\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - webex\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - webflow\ (41) — 20 .md · 13 .html · 6 .json · 2 .css
    - wechat\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - wired\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - wise\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - x-ai\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - xiaohongshu\ (24) — 13 .html · 6 .json · 3 .md · 2 .css
    - zapier\ (24) — 13 .html · 6 .json · 3 .md · 2 .css

---

## rulez

*Coding / behavioral rules.*

**147 files**  ·  147 .md

<details><summary><b>(loose files)</b> (1)</summary>

- `README.md` — Kurallar (Rules)

</details>

<details><summary><b>common\</b> (9 files)</summary>

- `agents.md` — Agent Orkestrasyonu
- `coding-style.md` — Kodlama Stili
- `development-workflow.md` — Geliştirme İş Akışı
- `git-workflow.md` — Git İş Akışı
- `hooks.md` — Hooks Sistemi
- `patterns.md` — Yaygın Pattern'ler
- `performance.md` — Performans Optimizasyonu
- `security.md` — Güvenlik Kuralları
- `testing.md` — Test Gereksinimleri

</details>

<details><summary><b>ECC\</b> (122 files)</summary>

- `angular\coding-style.md` — Angular Coding Style
- `angular\hooks.md` — Angular Hooks
- `angular\patterns.md` — Angular Patterns
- `angular\security.md` — Angular Security
- `angular\testing.md` — Angular Testing
- `arkts\coding-style.md` — HarmonyOS / ArkTS Coding Style
- `arkts\hooks.md` — HarmonyOS / ArkTS Hooks
- `arkts\patterns.md` — HarmonyOS / ArkTS Patterns
- `arkts\security.md` — HarmonyOS / ArkTS Security
- `arkts\testing.md` — HarmonyOS / ArkTS Testing
- `common\agents.md` — Agent Orchestration
- `common\code-review.md` — Code Review Standards
- `common\coding-style.md` — Coding Style
- `common\development-workflow.md` — Development Workflow
- `common\git-workflow.md` — Git Workflow
- `common\hooks.md` — Hooks System
- `common\patterns.md` — Common Patterns
- `common\performance.md` — Performance Optimization
- `common\security.md` — Security Guidelines
- `common\testing.md` — Testing Requirements
- `cpp\coding-style.md` — C++ Coding Style
- `cpp\hooks.md` — C++ Hooks
- `cpp\patterns.md` — C++ Patterns
- `cpp\security.md` — C++ Security
- `cpp\testing.md` — C++ Testing
- `csharp\coding-style.md` — C# Coding Style
- `csharp\hooks.md` — C# Hooks
- `csharp\patterns.md` — C# Patterns
- `csharp\security.md` — C# Security
- `csharp\testing.md` — C# Testing
- `dart\coding-style.md` — Dart/Flutter Coding Style
- `dart\hooks.md` — Dart/Flutter Hooks
- `dart\patterns.md` — Dart/Flutter Patterns
- `dart\security.md` — Dart/Flutter Security
- `dart\testing.md` — Dart/Flutter Testing
- `fsharp\coding-style.md` — F# Coding Style
- `fsharp\hooks.md` — F# Hooks
- `fsharp\patterns.md` — F# Patterns
- `fsharp\security.md` — F# Security
- `fsharp\testing.md` — F# Testing
- `golang\coding-style.md` — Go Coding Style
- `golang\hooks.md` — Go Hooks
- `golang\patterns.md` — Go Patterns
- `golang\security.md` — Go Security
- `golang\testing.md` — Go Testing
- `java\coding-style.md` — Java Coding Style
- `java\hooks.md` — Java Hooks
- `java\patterns.md` — Java Patterns
- `java\security.md` — Java Security
- `java\testing.md` — Java Testing
- `kotlin\coding-style.md` — Kotlin Coding Style
- `kotlin\hooks.md` — Kotlin Hooks
- `kotlin\patterns.md` — Kotlin Patterns
- `kotlin\security.md` — Kotlin Security
- `kotlin\testing.md` — Kotlin Testing
- `nuxt\coding-style.md` — Nuxt Coding Style
- `nuxt\hooks.md` — Nuxt Hooks
- `nuxt\patterns.md` — Nuxt Patterns
- `nuxt\security.md` — Nuxt Security
- `nuxt\testing.md` — Nuxt Testing
- `perl\coding-style.md` — Perl Coding Style
- `perl\hooks.md` — Perl Hooks
- `perl\patterns.md` — Perl Patterns
- `perl\security.md` — Perl Security
- `perl\testing.md` — Perl Testing
- `php\coding-style.md` — PHP Coding Style
- `php\hooks.md` — PHP Hooks
- `php\patterns.md` — PHP Patterns
- `php\security.md` — PHP Security
- `php\testing.md` — PHP Testing
- `python\coding-style.md` — Python Coding Style
- `python\fastapi.md` — FastAPI Rules
- `python\hooks.md` — Python Hooks
- `python\patterns.md` — Python Patterns
- `python\security.md` — Python Security
- `python\testing.md` — Python Testing
- `react-native\accessibility.md` — React Native / Expo Accessibility
- `react-native\coding-style.md` — React Native / Expo Coding Style
- `react-native\hooks.md` — React Native / Expo Hooks
- `react-native\patterns.md` — React Native / Expo Patterns
- `react-native\performance.md` — React Native / Expo Performance
- `react-native\production-readiness.md` — React Native / Expo Production Readiness
- `react-native\security.md` — React Native / Expo Security
- `react-native\testing.md` — React Native / Expo Testing
- `react\coding-style.md` — React Coding Style
- `react\hooks.md` — React Hooks
- `react\patterns.md` — React Patterns
- `react\security.md` — React Security
- `react\testing.md` — React Testing
- `README.md` — Rules
- `ruby\coding-style.md` — Ruby Coding Style
- `ruby\hooks.md` — Ruby Hooks
- `ruby\patterns.md` — Ruby Patterns
- `ruby\security.md` — Ruby Security
- `ruby\testing.md` — Ruby Testing
- `rust\coding-style.md` — Rust Coding Style
- `rust\hooks.md` — Rust Hooks
- `rust\patterns.md` — Rust Patterns
- `rust\security.md` — Rust Security
- `rust\testing.md` — Rust Testing
- `swift\coding-style.md` — Swift Coding Style
- `swift\hooks.md` — Swift Hooks
- `swift\patterns.md` — Swift Patterns
- `swift\security.md` — Swift Security
- `swift\testing.md` — Swift Testing
- `typescript\coding-style.md` — TypeScript/JavaScript Coding Style
- `typescript\hooks.md` — TypeScript/JavaScript Hooks
- `typescript\patterns.md` — TypeScript/JavaScript Patterns
- `typescript\security.md` — TypeScript/JavaScript Security
- `typescript\testing.md` — TypeScript/JavaScript Testing
- `vue\coding-style.md` — Vue Coding Style
- `vue\hooks.md` — Vue Hooks
- `vue\patterns.md` — Vue Patterns
- `vue\security.md` — Vue Security
- `vue\testing.md` — Vue Testing
- `web\coding-style.md` — Web Coding Style
- `web\design-quality.md` — Web Design Quality Standards
- `web\hooks.md` — Web Hooks
- `web\patterns.md` — Web Patterns
- `web\performance.md` — Web Performance Rules
- `web\security.md` — Web Security Rules
- `web\testing.md` — Web Testing Rules

</details>

<details><summary><b>golang\</b> (5 files)</summary>

- `coding-style.md` — Go Kodlama Stili
- `hooks.md` — Go Hooks
- `patterns.md` — Go Pattern'leri
- `security.md` — Go Güvenlik
- `testing.md` — Go Testing

</details>

<details><summary><b>python\</b> (5 files)</summary>

- `coding-style.md` — Python Kodlama Stili
- `hooks.md` — Python Hooks
- `patterns.md` — Python Pattern'leri
- `security.md` — Python Güvenlik
- `testing.md` — Python Testing

</details>

<details><summary><b>typescript\</b> (5 files)</summary>

- `coding-style.md` — TypeScript/JavaScript Kodlama Stili
- `hooks.md` — TypeScript/JavaScript Hooks
- `patterns.md` — TypeScript/JavaScript Pattern'leri
- `security.md` — TypeScript/JavaScript Güvenlik
- `testing.md` — TypeScript/JavaScript Testing

</details>

---

*End of directory. 12982 files across 20 categories (1969 skills). Regenerate with `M:\ARMORY-INDEX-GENERATOR.ps1`.*

