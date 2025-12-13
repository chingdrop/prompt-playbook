# Manual Integration Guide: Custom GPT ↔ Prompt Playbooks

This repo is the **source of truth** for prompt playbooks. Integration is **manual via the GPT Builder UI** (no APIs).

Audience: experienced technical professionals with limited AI/ML background.

Updated: 2025-12-13

---

## What you are integrating

Each topic folder under `gpts/<topic>/` contains:

- `gpt-instructions/` – paste into the Custom GPT Builder **Instructions**
- `knowledge/` – upload these files into the Custom GPT Builder **Knowledge** (optional but recommended)
- `router/` – a router prompt to pick the right prompt card
- `prompts/` – prompt cards you copy/paste into chat

Shared assets live under `shared/`:
- `shared/snippets/` – reusable blocks
- `shared/templates/` – output schemas
- `shared/router/00-router.md` – global router prompt
- `shared/knowledge-formatting.md` – conventions for knowledge files

---

## 1) Prerequisites

- ChatGPT account with Custom GPT creation access.
- This repo cloned locally (or browsable in GitHub).
- A target topic selected (example: `career-assets`).

---

## 2) Create a Custom GPT (per topic)

Create one Custom GPT per topic (recommended for consistency):

1. Open **GPT Builder** → **Create** (or **My GPTs** → **Create**).
2. Switch to **Configure**.
3. Set:
   - **Name**: e.g., “Career Assets Copilot”
   - **Description**: one sentence from the topic README
4. In **Instructions**:
   - paste the topic instruction file from:  
     `gpts/<topic>/gpt-instructions/*.md`

---

## 3) Upload Knowledge files (recommended)

1. In the GPT Builder **Knowledge** section:
   - Upload all files from: `gpts/<topic>/knowledge/`

Optional (only if you want the GPT to “know” shared schemas/snippets without you pasting them):
- `shared/templates/*`
- `shared/snippets/*`

---

## 4) Enable capabilities (recommended defaults)

In the GPT Builder **Capabilities**:

- **Memory:** ON  
  Use for preference retention (tone, length, recurring artifacts). Avoid storing sensitive client data.

- **File uploads / Advanced Data Analysis:** ON  
  Recommended because it improves file handling and supports user uploads (resumes, logs, docs).

- **Web browsing:** ON  
  Useful for “latest/current” requests and external fact checks.

Practice: use web browsing only when asked for recency or when facts could have changed.

---

## 5) Add conversation starters (quality-of-life)

Add 3–6 per topic using the topic README’s “Top prompt cards” as starters.

Example for `career-assets`:
- “Tailor my resume to this job description (ATS-safe).”
- “Write my LinkedIn About for a Security Engineer role.”
- “Draft an InMail to the hiring manager with my portfolio.”

---

## 6) Daily use flow (recommended)

1. Start with the topic router prompt:
   - `gpts/<topic>/router/00-router.md`
2. The router should select the best prompt card under `gpts/<topic>/prompts/`.
3. Copy/paste that card into the chat and fill placeholders.
4. Iterate:
   - answer follow-up questions
   - re-run with updated inputs
   - use `shared/snippets/tighten_pass.md` for final polish

---

## 7) Maintenance lifecycle (repo → GPT)

Integration is manual. Treat Git as your system of record.

### What to update in GPT Builder

- If you change `gpt-instructions/`:
  - update the GPT Builder **Instructions** (copy/paste)
  - re-test with 3 representative prompts

- If you change `knowledge/`:
  - re-upload the updated file(s) into GPT Builder Knowledge
  - keep filenames stable where possible

- If you change `prompts/`:
  - no GPT Builder change required (prompt cards are copy/paste artifacts)
  - optionally update conversation starters

### Release discipline (recommended)

- Maintain `CHANGELOG.md`
- Tag releases (`v0.1.0`, `v0.2.0`, …)
- When a release changes builder instructions, note “Builder sync required” in the changelog.

---

## 8) Testing checklist

Use [docs/testing_checklist.md](testing_checklist.md) after changes that affect behavior or outputs.

---

## 9) Scaling to more topics

- Keep one Custom GPT per topic.
- Avoid mixing unrelated jobs-to-be-done into one GPT.
- If a topic grows too large, split it into two GPTs and mirror the same folder structure under `gpts/`.
