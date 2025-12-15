# Builder Sync Registry (Custom GPT Deployments)

This file tracks which repo artifacts are currently deployed into Custom GPTs in the ChatGPT Builder.
The repo is the source of truth; the Builder configuration must be manually synced.

Updated: [YYYY-MM-DD]

---

## What counts as a “deployment” here

A “deployment” is a Custom GPT configured in the Builder with:

- Instructions pasted from a repo file
- Knowledge files uploaded from the repo

Because Builder content does not auto-update from Git, drift is expected unless tracked.

---

## Sync policy (repo → builder)

A Builder sync is required when any of the following change for a topic:

- `gpts/<topic>/gpt-instructions/<topic>_instructions.md`
- `gpts/<topic>/knowledge/<topic>_playbook.md`

Strongly recommended to sync when:

- `gpts/<topic>/router/00_router.md` changes materially (routing/allowlist changes)
- prompt cards change in a way that impacts operating behavior or strict output formats

### Required bookkeeping when a sync is needed

When canonical instructions/knowledge change:

1) Add a `CHANGELOG.md` entry that includes: **Builder sync required**
2) Update this file (`docs/builder_sync.md`) for the affected GPT(s)

---

## Deployment registry

Fields:

- GPT Name: Name shown in Builder
- Topic: `gpts/<topic>/`
- Instructions: canonical repo path pasted into Builder
- Knowledge: canonical repo path(s) uploaded into Builder
- Capabilities: note key toggles (Web, Files/Data Analysis, etc.)
- Last synced: date of last Builder update (use ISO: YYYY-MM-DD)
- Repo ref: git commit/tag that was synced (recommended)
- Owner: human accountable for keeping it current
- Status: `in_sync` | `sync_required` | `unknown`
- Notes: anything relevant (extra knowledge files, exceptions, etc.)

### GPT 1

- GPT Name: Business Analysis Copilot
- Topic: `gpts/business-analysis/`
- Instructions: `gpts/business-analysis/gpt-instructions/business_analysis_instructions.md`
- Knowledge:
  - `gpts/business-analysis/knowledge/business_analysis_playbook.md`
- Capabilities: WEB: ON | FILES/DATA: ON
- Last synced: 2025-12-14
- Repo ref (commit/tag): [GIT COMMIT OR TAG]
- Owner: CH
- Status: in_sync
- Notes: -

### GPT 2

- GPT Name: Career Assets Copilot
- Topic: `gpts/career-assets/`
- Instructions: `gpts/career-assets/gpt-instructions/career_assets_instructions.md`
- Knowledge:
  - `gpts/career-assets/knowledge/career_assets_playbook.md`
- Capabilities: WEB: ON | FILES/DATA: ON
- Last synced: 2025-12-14
- Repo ref (commit/tag): [GIT COMMIT OR TAG]
- Owner: CH
- Status: in_sync
- Notes: -

### GPT 3

- GPT Name: Coding & Automation Copilot
- Topic: `gpts/coding-automation/`
- Instructions: `gpts/coding-automation/gpt-instructions/coding_automation_instructions.md`
- Knowledge:
  - `gpts/coding-automation/knowledge/coding_automation_playbook.md`
- Capabilities: WEB: ON | FILES/DATA: ON
- Last synced: 2025-12-14
- Repo ref (commit/tag): [GIT COMMIT OR TAG]
- Owner: CH
- Status: in_sync
- Notes: —

### GPT 4

- GPT Name: Document Writing Copilot
- Topic: `gpts/document-writing/`
- Instructions: `gpts/document-writing/gpt-instructions/document_writing_instructions.md`
- Knowledge:
  - `gpts/document-writing/knowledge/document_writing_playbook.md`
- Capabilities: WEB: ON | FILES/DATA: ON
- Last synced: 2025-12-14
- Repo ref (commit/tag): [GIT COMMIT OR TAG]
- Owner: CH
- Status: in_sync
- Notes: —

### GPT 5

- GPT Name: IT Delivery Copilot
- Topic: `gpts/it-delivery/`
- Instructions: `gpts/it-delivery/gpt-instructions/it_delivery_instructions.md`
- Knowledge:
  - `gpts/it-delivery/knowledge/it_delivery_playbook.md`
- Capabilities: WEB: ON | FILES/DATA: ON
- Last synced: 2025-12-14
- Repo ref (commit/tag): [GIT COMMIT OR TAG]
- Owner: CH
- Status: in_sync
- Notes: -

---

## How to perform a Builder sync (manual checklist)

For the affected GPT in the Builder:

- [ ] Open GPT → Configure
- [ ] Replace the Instructions field by pasting the canonical instructions file contents
- [ ] Remove outdated knowledge uploads (if applicable)
- [ ] Upload the canonical knowledge playbook file(s)
- [ ] Confirm capabilities match the topic guardrails
- [ ] Save
- [ ] Update `docs/builder_sync.md` (Last synced + Repo ref + Status=in_sync)
- [ ] Update `CHANGELOG.md` entry (or mark sync completed if you track that)

---

## Drift triage (if behavior seems “wrong”)

- [ ] Verify Builder Instructions match the canonical instructions file
- [ ] Verify Builder Knowledge includes the canonical playbook (and no unintended outdated files)
- [ ] Verify topic router allowlist matches actual prompt filenames
- [ ] Run 1–2 prompt cards end-to-end and confirm strict output sections appear
