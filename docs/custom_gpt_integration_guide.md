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

### Minimize Builder drift

- Every update should follow a repeatable “sync” process.
- Keep changes small and reversible.

---

## 2) Initial setup (per topic)

### Step A — Choose a topic

Use the topic index in the root README for the current, authoritative status (complete vs scaffold):

- [`README.md`](../README.md)

Then open the matching topic README:

- [`gpts/career-assets/README.md`](../gpts/career-assets/README.md)
- [`gpts/coding-automation/README.md`](../gpts/coding-automation/README.md)
- [`gpts/document-writing/README.md`](../gpts/document-writing/README.md)
- [`gpts/business-analysis/README.md`](../gpts/business-analysis/README.md)
- [`gpts/it-delivery/README.md`](../gpts/it-delivery/README.md)

If you are not sure which topic to use, run the global router prompt in:

- [`00_router.md`](../00_router.md)

### Step B — Paste builder instructions

Open the topic instructions file under `gpts/<topic>/gpt-instructions/`.

Copy/paste the full instructions file into the Custom GPT Builder “Instructions” field.

### Step C — Upload knowledge pack(s)

If the topic contains `knowledge/*.md`, upload those files into GPT Knowledge.

### Step D — Use the topic router + prompt cards

Use the topic router at:

- `gpts/<topic>/router/00-router.md`

Then run the selected prompt card from:

- `gpts/<topic>/prompts/*.md`

---

## 3) When to sync the Builder

Sync the Custom GPT Builder whenever you change:

- `gpts/<topic>/gpt-instructions/*.md`
- `gpts/<topic>/knowledge/*.md`

If a file is deprecated and replaced, ensure the Builder references the canonical file named in that topic README.

---

## 4) Ongoing operations

- Keep changes small and reversible.
- Update `CHANGELOG.md` for every meaningful change.
- Flag “Builder sync required” when instructions/knowledge changed and the Builder must be updated.

---

## 5) Router usage (topic-level)

The topic router should:

- Pick the best matching prompt card
- Fill the prompt template with placeholders for missing inputs
- Ask up to 3 clarifying questions only if required

---

## 6) Troubleshooting Builder drift

Symptoms of drift:

- GPT behavior does not match repo playbook
- Old instructions still in effect
- Knowledge pack content not reflected

Fix:

- Re-paste the canonical instructions file
- Re-upload knowledge files
- Re-test with 3 representative prompt cards

---

## 7) Suggested “meta-router” prompt (cross-topic)

Use this when you are unsure which topic to use:

1) Classify my request into ONE topic:
   - Career Assets (resume/LinkedIn/outreach/interview)
   - Document Writing (proposals/SOWs/emails/memos)
   - Business Analysis (decision support/pricing/strategy)
   - Coding & Automation (Python/Django/automation)
   - IT Delivery & Troubleshooting (Windows/M365/Entra/networking)

2) Ask up to 3 clarifying questions ONLY if needed.

3) Then respond with:
   - the best matching topic folder under `gpts/`
   - the best matching prompt card filename within that topic
   - the filled-in prompt template with placeholders for missing inputs

---

## 8) Creating a new topic

Create a new topic folder when:

- You have distinct “jobs to be done” that require different outputs and constraints
- The instructions are starting to conflict (e.g. coding vs proposal writing)
- The prompt library has grown beyond ~10–15 core prompt cards

---

## 9) Minimal “definition of done” for a topic

This repo uses the status contract in [`docs/repo_consistency_rules.md`](repo_consistency_rules.md).

A topic is “complete” when it has (minimum):

- A topic README with quick start and prompt card list
- Builder instructions (`gpts/<topic>/gpt-instructions/*.md`)
- A topic router (`gpts/<topic>/router/00-router.md`)
- At least 3 high-value prompt cards (`gpts/<topic>/prompts/*.md`)
- At least 1 knowledge file (`gpts/<topic>/knowledge/*.md`)

A topic is a “scaffold” when it has (minimum):

- A topic README with a status line
- Builder instructions
- A topic router

If any of the above inputs are missing, keep the topic status truthful and leave placeholders in docs until the missing pieces exist.

## 10) Common failure modes (and fixes)

### Failure: generic answers

Fix:

- Use prompt cards with strict output formats
- Provide concrete inputs (logs, diffs, requirements)
- Add verification requirements

### Failure: wrong task mode

Fix:

- Use the router
