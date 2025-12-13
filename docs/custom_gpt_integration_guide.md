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
Pick one:
- `gpts/career-assets/`
- `gpts/coding-automation/`
- (scaffolds): `gpts/business-analysis/`, `gpts/document-writing/`, `gpts/it-delivery/`

Open the topic README first:
- `gpts/<topic>/README.md`

### Step B — Create the Custom GPT
In ChatGPT:
1. Go to **Explore GPTs**
2. Click **Create**
3. Switch to **Configure** (recommended for control)

Set:
- Name: match the topic (e.g., “Coding & Automation Copilot”)
- Description: 1–2 lines, specific to that topic
- Conversation starters: pull from your most common tasks

### Step C — Paste builder instructions
Copy the contents of:
- `gpts/<topic>/gpt-instructions/<file>.md`

Paste into the Builder’s **Instructions** field.

### Step D — Upload knowledge packs
If the topic has knowledge files, upload:
- `gpts/<topic>/knowledge/*.md`

Guidance:
- Prefer one “knowledge pack” file when possible
- If multiple files, keep them narrow and additive

### Step E — Enable capabilities (recommended defaults)
Turn ON:
- File uploads / Advanced Data Analysis (for logs, docs, CSVs)
- Web browsing (when facts may be current/variable or when asked)
- Memory (store stable preferences only; avoid storing sensitive info)

Turn OFF unless needed:
- Image generation
- Canvas

### Step F — Save and test
Save the GPT, then run a small set of tests (see `docs/testing_checklist.md`).

---

## 3) Normal usage workflow

### Use the router
For a topic:
- Open `gpts/<topic>/router/00-router.md`
- Paste the router prompt into chat
- Give a one-sentence request

The router should return:
- The best prompt card filename
- A filled-in prompt template with placeholders for missing inputs
- Up to 3 clarifying questions (only if needed)

### Use prompt cards
- Open the prompt card under `gpts/<topic>/prompts/`
- Copy/paste
- Fill placeholders
- Run

---

## 4) Project repo workflow (Coding & Automation)

When using the Coding & Automation Copilot on a real repo, context quality determines output quality.

Recommended approach:
1. Copy `docs/ai/` into the target project repo as `docs/ai/`
2. Fill `docs/ai/context.md`
3. Use the “Project onboarding” prompt card to build a repo mental model
4. Work via diffs + logs + small deltas rather than uploading the whole repo repeatedly

Templates:
- `docs/ai/context.md`
- `docs/ai/how_we_work.md`
- `docs/ai/decision_log.md`

---

## 5) Maintenance lifecycle

### Change types
1) **Prompt-only change**
- Update prompt cards or router
- Usually does not require Builder changes unless instructions reference new files

2) **Instruction change**
- Requires Builder sync (paste updated Instructions)

3) **Knowledge change**
- Requires Builder sync (re-upload knowledge files)

### Builder sync process (repeatable)
For each affected topic GPT:
1. Open the topic’s `gpt-instructions/` file and copy it
2. In Builder, replace Instructions with the latest version
3. Upload/replace knowledge pack files if changed
4. Save
5. Run the topic’s tests from `docs/testing_checklist.md`

### Versioning
- Use `CHANGELOG.md` to record:
  - What changed
  - Which GPT topics are affected
  - Whether Builder sync is required

Recommended note format:
- “Builder sync required: update Instructions for <topic>”
- “Builder sync required: re-upload Knowledge pack(s) for <topic>”

---

## 6) Quality assurance

Use `docs/testing_checklist.md`:
- Re-run tests any time instructions, routers, or knowledge packs change.
- Spot-check that routers still reference existing prompt card filenames.
- Confirm prompt cards remain copy/paste-ready.

---

## 7) Operational safeguards

### Avoid leaking secrets
- Redact tokens, keys, credentials, and sensitive internal URLs.
- Prefer `env.example` patterns and placeholder variables.

### Do not invent facts
- Prompt cards and instructions should explicitly prohibit fabrication.
- If required inputs are missing, the GPT should ask for them.

---

## 8) When to split a new GPT topic
Create a new topic folder when:
- You have distinct “jobs to be done” that require different outputs and constraints
- The instructions are starting to conflict (e.g., coding vs proposal writing)
- The prompt library has grown beyond ~10–15 core prompt cards

---

## 9) Minimal “definition of done” for a topic
A topic is “complete” when it has:
- A topic README with quick start and prompt card list
- Builder instructions
- A router
- At least 3–8 high-value prompt cards
- A knowledge pack (recommended) for consistent behavior

---

## 10) Common failure modes (and fixes)

### Failure: generic answers
Fix:
- Use prompt cards with strict output formats
- Provide concrete inputs (logs, diffs, requirements)
- Add verification requirements

### Failure: wrong task mode
Fix:
- Use the router first
- Narrow the request (one task at a time)

### Failure: “drift” between repo and Builder
Fix:
- Always record Builder-required changes in `CHANGELOG.md`
- Run the sync process whenever instructions/knowledge changes
