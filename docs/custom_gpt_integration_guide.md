# Custom GPT Integration Guide (Manual, Full Lifecycle)

This guide explains how to integrate this prompt playbook repository with a Custom GPT using the ChatGPT UI, and how to maintain the GPT over time as the playbooks evolve.

## Scope

This repo supports **manual integration**:

- Copy/paste instructions into the GPT Builder
- Upload knowledge files into GPT Knowledge
- Use prompt cards and routers during normal use

Out of scope:

- Automated retrieval from GitHub
- API/tooling integrations (covered in a separate repo)

---

## 1) Design principles

### Treat the repo as the source of truth

- The repository holds the canonical instructions, prompt cards, routers, and knowledge packs.
- The Custom GPT Builder is a deployed configuration that should be updated when the repo changes.

### Prefer topic-specific GPTs

- Create one Custom GPT per topic under `gpts/<topic>/`.
- Avoid one “do everything” GPT unless you have a strong routing workflow and testing discipline.

---

## 2) Initial setup (per topic)

### Step A — Pick the topic

Start at the root README:

- [`README.md`](../README.md)

Then open the matching topic README (examples):

- [`gpts/career-assets/README.md`](../gpts/career-assets/README.md)
- [`gpts/coding-automation/README.md`](../gpts/coding-automation/README.md)
- [`gpts/document-writing/README.md`](../gpts/document-writing/README.md)
- [`gpts/business-analysis/README.md`](../gpts/business-analysis/README.md)
- [`gpts/it-delivery/README.md`](../gpts/it-delivery/README.md)

If you are not sure which topic to use, run the global router prompt in:

- [`00_router.md`](../00_router.md)

### Step B — Create the GPT in the Builder

Open the GPT editor and create/configure your GPT:

- `https://chatgpt.com/gpts/editor`

In the Builder **Configure** tab, set:

- Name, Description, and optional icon
- **Instructions** (paste from the repo file below)
- **Knowledge** (upload the repo file below)
- Capabilities (only what you need)

### Step C — Paste builder instructions (from repo)

Open the topic instructions file under `gpts/<topic>/gpt-instructions/`.

Use the canonical instructions file:

- `gpts/<topic>/gpt-instructions/<topic>_copilot_instructions.md`

Paste the full contents into the Builder **Instructions** field.

### Step D — Upload knowledge pack(s)

Upload the topic playbook file under `gpts/<topic>/knowledge/` into the Builder **Knowledge** section.

Use the canonical knowledge file:

- `gpts/<topic>/knowledge/<topic>_playbook.md`

Notes (Builder behavior):

- Knowledge supports attaching multiple files; current limits and processing behavior are documented by OpenAI (for example: max files per GPT, per-file size, and text-only extraction from images).
- Do **not** upload prompt cards into Knowledge; prompt cards are intended for copy/paste use during conversations.

### Step E — Test in Preview

In the Builder preview panel, run 2–3 prompt cards from:

- `gpts/<topic>/prompts/*.md`

Confirm:

- the GPT follows guardrails
- output format matches the prompt card
- missing inputs become placeholders (not invented facts)

---

## 3) When to sync the Builder

Sync the Custom GPT Builder whenever you change:

- `gpts/<topic>/gpt-instructions/*.md`
- `gpts/<topic>/knowledge/*.md`

Strongly recommended to sync (because behavior can drift):

- router logic changes in `gpts/<topic>/router/00_router.md`
- any prompt card changes that materially affect how users operate the GPT

If a file is deprecated and replaced, ensure the Builder references the canonical file named in that topic README.

---

## 4) Ongoing operations

- Keep changes small and reversible.
- Prefer narrow prompt cards over sprawling instructions.
- Always include a verification plan (tests or checklists) in prompt cards where operational risk exists.
- Track significant changes in `CHANGELOG.md` and flag **Builder sync required** when needed.

---

## 5) Router usage (topic-level)

Each topic must include a router at:

- `gpts/<topic>/router/00_router.md`

Routers should:

- choose exactly one prompt card from an explicit allowlist
- ask up to 3 clarifying questions only when required
- output the selected filename and a filled template

---

## 6) Troubleshooting Builder drift

Symptoms:

- The GPT uses the wrong tone or output format
- The GPT “forgets” guardrails
- The GPT references old templates or missing files

Checklist:

- Confirm the Builder Instructions match the canonical repo instructions file.
- Confirm the Builder Knowledge includes the canonical playbook file (and no unintended outdated files).
- Confirm the topic README Quick start links match the files present in the topic folder.
- Run the topic testing checklist: [`docs/testing_checklist.md`](testing_checklist.md)

---

## 7) Suggested “meta-router” prompt (cross-topic)

Use this prompt when a user request could fit multiple topics:

1) Choose the best topic folder under `gpts/<topic>/` and explain why in 1–2 lines.  
2) Output the exact topic router path to use next: `gpts/<topic>/router/00_router.md`.  
3) Ask up to 3 clarifying questions only if required to select the topic/router.

---

## 8) Creating a new topic

When creating a new topic, follow the repo contract in:

- [`docs/repo_consistency_rules.md`](repo_consistency_rules.md)

Minimum structure:

- `gpts/<topic>/README.md`
- `gpts/<topic>/router/00_router.md`
- `gpts/<topic>/gpt-instructions/<topic>_copilot_instructions.md`
- `gpts/<topic>/knowledge/<topic>_playbook.md`
- `gpts/<topic>/prompts/` (start with 3+ prompt cards)

---

## 9) Minimal “definition of done” for a topic

A topic is **complete** only if it has:

- Builder-ready instructions (canonical filename)
- A router with an explicit allowlist
- At least 3 high-value prompt cards (schema-aligned)
- A knowledge playbook (canonical filename)
- A topic README Quick start that matches reality

---

## 10) Common failure modes (and fixes)

### Failure: generic answers

Fix:

- Use prompt cards with strict output formats
- Provide concrete inputs (logs, diffs, requirements)
- Add verification requirements

### Failure: wrong task mode

Fix:

- Use the router and ensure the allowlist maps to real prompt files
- If the router is ambiguous, add a clarifying question and/or a more specific prompt card

---

## References (OpenAI Help Center)

- Creating a GPT: <https://help.openai.com/en/articles/8554397-creating-a-gpt>
- GPTs FAQ: <https://help.openai.com/en/articles/8554407-gpts-faq>
- Knowledge in GPTs: <https://help.openai.com/en/articles/8843948-knowledge-in-gpts>
- File Uploads FAQ: <https://help.openai.com/en/articles/8555545-file-uploads-faq>
- ChatGPT capabilities overview: <https://help.openai.com/en/articles/9260256-chatgpt-capabilities-overview>
