# Prompt Playbook (Monorepo)

A single Git repo that contains **one prompt library per Custom GPT topic**, plus shared routers and onboarding templates.

This repo is optimized for **manual Custom GPT setup** (copy/paste instructions + upload knowledge files). API integrations are intentionally out of scope here.

## Structure

- [`shared/`](shared/) – reusable snippets/templates/routers across topics
- `gpts/<topic>/` – each topic contains:
  - `gpt-instructions/` – builder instructions for that Custom GPT
  - `knowledge/` – optional knowledge pack(s) to upload into GPT Knowledge
  - `prompts/` – copy/paste prompt cards
  - `router/` – topic router prompt
  - `README.md` – topic quick start + top prompt cards
- [`docs/`](docs/) – setup guides, testing checklists, and project onboarding templates

## Topics included

- [career-assets](gpts/career-assets/README.md) — **complete** (instructions + knowledge + prompt cards)
- [coding-automation](gpts/coding-automation/README.md) — **complete** (instructions + knowledge + prompt cards)
- [business-analysis](gpts/business-analysis/README.md) — **scaffold** (instructions + router; prompt cards pending)
- [document-writing](gpts/document-writing/README.md) — **scaffold** (instructions + router; prompt cards pending)
- [it-delivery](gpts/it-delivery/README.md) — **scaffold** (instructions + router; prompt cards pending)

## Quick start

1. Open the topic you want, e.g. [`gpts/career-assets/README.md`](gpts/career-assets/README.md).
2. Copy the builder instructions from `gpts/<topic>/gpt-instructions/<file>.md` into the Custom GPT Builder.
3. If present, upload the topic knowledge pack(s) from `gpts/<topic>/knowledge/` into GPT Knowledge.
4. Use `gpts/<topic>/router/00-router.md` to pick the right prompt card.
5. Paste a prompt card from `gpts/<topic>/prompts/` and fill placeholders.

## Manual integration and QA

- Repo consistency rules: [`docs/repo_consistency_rules.md`](docs/repo_consistency_rules.md)
- Manual integration guide: [`docs/custom_gpt_integration_guide.md`](docs/custom_gpt_integration_guide.md)
- Testing checklist: [`docs/testing_checklist.md`](docs/testing_checklist.md)

## Project repo onboarding templates

To make the **Coding & Automation Copilot** effective on a real GitHub project, copy these into the *target project repo*:

- [docs/ai templates](docs/ai/README.md) ([context](docs/ai/context.md), [how we work](docs/ai/how_we_work.md), [decision log](docs/ai/decision_log.md))

Updated: 2025-12-13

## Obsidian
- [`docs/obsidian_notes.md`](docs/obsidian_notes.md)
