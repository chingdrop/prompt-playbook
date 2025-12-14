# Changelog

All notable changes to this prompt playbook monorepo.

## Unreleased

### Additions

- Add CI "playbook lint" to prevent drift (topic completeness, router allowlist, prompt card schema, Quick start link lint).
- Add [`docs/repo_consistency_rules.md`](docs/repo_consistency_rules.md) to document repo conventions.
- Add [`docs/ai/README.md`](docs/ai/README.md) onboarding templates (copy into target project repos).
- Add Coding & Automation prompt cards for project onboarding and git diff review.
- Add manual integration guide ([`docs/custom_gpt_integration_guide.md`](docs/custom_gpt_integration_guide.md)).
- Add testing checklist ([`docs/testing_checklist.md`](docs/testing_checklist.md)).

### Changes

- Standardize README topic statuses and quick-start instructions.
- Mark `gpts/coding-automation/gpt-instructions/coding-automation_instructions.md` as deprecated.
  - Builder sync required: **Only if** your Custom GPT Builder is currently using the deprecated file; otherwise **no** (verify Builder references the canonical instructions file in that topic README).

### Fixes

- Fix root README topic list formatting and remove placeholder ellipses.

## v0.1.0

- Initial monorepo structure with topic playbooks and shared assets.
