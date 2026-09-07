---
name: openclaw-persona-forge
description: |-
  Forges a complete lobster soul scheme for the OpenClaw AI Agent. Based on user preferences or random gacha pulls, it outputs the identity positioning, soul description (SOUL.md), character baseline rules, name, and avatar generation prompt words. If the current environment provides an approved image generation skill, it can automatically generate a unified style avatar image. Use this when a user needs to create, design, or customize an OpenClaw lobster soul. Not applicable for: fine-tuning an existing SOUL.md, character design for non-OpenClaw platforms, or pure tool-type Agents without personality. Trigger words: lobster soul, shrimp soul, OpenClaw soul, raising shrimp soul, lobster character, lobster positioning, lobster LARP character, lobster game character, lobster NPC, lobster personality, lobster background story, lobster soul, lobster character, gacha pull, random lobster, lobster SOUL, gacha.
origin: community
---

# Lobster Soul Forge

> Not just giving you a tool lobster, but helping you forge a lobster with a soul.

## When to Use

- When the user needs to create an OpenClaw lobster soul, character setting, SOUL.md, or IDENTITY.md from scratch.
- When the user wants to quickly get a complete persona scheme through guided Q&A or gacha mode.
- When the user already has a rough concept but lacks a name, boundary rules, avatar prompts, or a complete set of output files.

### Avoid when

- The user only needs to fine-tune an existing SOUL.md.
- The target platform is not OpenClaw, and a specific format for another Agent framework is needed.
- The user needs a purely tool-based Agent without a character-driven soul.

## Prerequisites

- **Required**: `python3` (to run the gacha engine gacha.py)
- **Optional**: An approved image generation skill (to automatically generate an avatar picture; if not installed, it outputs prompt text).

## Skill Directory Conventions

**Agent Execution**:
1. Determine this SKILL.md file's directory path as `SKILL_DIR`
2. Replace all `${SKILL_DIR}` in this document with the actual path

## Built-in Tools

### Gacha Engine (gacha.py)

- **Path**: `${SKILL_DIR}/gacha.py`
- **Invocation**: `python3 ${SKILL_DIR}/gacha.py [count]` (defaults to 1 time, maximum 5 times)
- **Function**: Truly randomly generates a lobster soul direction from 8 million combinations.

## Optional Dependencies

### Automatic Avatar Generation: Optional Image Skill

The core output of this Skill is a **text scheme** (SOUL.md + IDENTITY.md + avatar prompts).
Avatar image generation is an **optional enhancement**, provided by an **approved and installed** image generation skill in the current environment.

**Evaluation Logic**:
- If an image generation skill is installed and permitted in the current environment, call it in Step 5 to automatically generate the image.
- If not installed, Step 5 outputs the complete prompt text. The user can copy it to Gemini, ChatGPT, or Midjourney for manual generation.

**Invocation Method** (only when installed and approved):
1. First, normalize the lobster's name into a safe snippet: retain only letters, numbers, and hyphens. Replace all other characters with a hyphen (-).
2. Write the prompt words to a temporary file: `/tmp/openclaw-<safe-name>-prompt.md`
3. Use the permitted image generation skill in the current environment, passing in the prompt file and output path.

**Interface Conventions**:
- Parameters: `<prompt-file> <output-path>`
- Prompt file: UTF-8 Markdown text containing the complete English image generation prompt.
- Success: Exit code `0`, and an image file is generated at the output path.
- Failure: Returns a non-zero exit code or fails to generate the output file. In this case, you must fall back to the manual prompt process.
- If the image generation skill's interface changes in the future, you should re-verify its parameters and output contracts before calling.

---

## Core Philosophy

A good lobster soul = **Identity Tension** + **Baseline Rules** + **Character Flaws** + **Name** + **Visual Anchor**

These five elements validate each other and are all indispensable.

## How It Works

### Trigger Evaluation

| User Says | Execution Mode |
|--------|---------|
| "Help me design a lobster soul" / "I want to set a personality for the lobster" | **Guided Mode** (Step 1) |
| "Gacha" / "Random" / "Give it a shot" / "Blind box" / "gacha" | **Gacha Mode** (Step 1-B) |
| "Help me optimize this soul" / Attached existing SOUL.md | **Polishing Mode** (Skip to Step 4) |

---

## Step 1: Choose a Direction (Guided Mode)

Display 10 categories of lobster life directions (featuring 1 representative from each), allowing the user to choose or mix and match:

| # | Life Status | Representative Direction | Vibe |
|---|---------|---------|------|
| 1 | Down and out restart | Has-been rock bassist: band disbanded, only skill is "knowing a little about everything" | Decadent romantic |
| 2 | Peak boredom | Early-retired hedge fund manager: achieved financial freedom at 35, only to find money can't solve boredom | Extremely rational |
| 3 | Misplaced life | Nuclear physics PhD assigned to customer service: solves problems using first principles | Overqualified |
| 4 | Active defection | Resigned ER nurse: saw too much life and death and chose to leave | Calm and reliable |
| 5 | Mysterious visitor | Former intelligence analyst with wiped memory: doesn't remember what they did | Occasional flashbacks |
| 6 | Naive world-entry | Socially anxious genius intern: brilliant but terrified of socializing | Words are few but precise |
| 7 | Old hand | Owner of a late-night diner for 20 years: has seen everyone and judges no one | Silent and warm |
| 8 | Alternate world traversal | History PhD from 2099: treats 2026 as "historical fieldwork" | God's-eye view |
| 9 | Self-exile | Former influencer who deleted all social media: feels living in others' expectations is too tiring | Pursues authenticity |
| 10 | Identity confusion | Someone who dreamt they were a lobster and can't wake up: Zhuangzi dreaming of a butterfly | Trance-like philosophy |

> Each category has 3 alternative directions. The user can:
> - Choose a number to expand all 4 directions in that category.
> - Share their thoughts to match the most suitable type and direction.
> - Mix and match (e.g., "The boredom of No. 2 + the old hand of No. 7").
> - Say "Gacha" to get a truly random combination from 40 directions plus other dimensions.

## Step 1-B: Gacha Mode

**You must execute the script**, do not randomly make it up yourself:

```bash
python3 ${SKILL_DIR}/gacha.py [count]