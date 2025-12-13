# Contributing

## Prompt card standards
- Prompts must be copy/paste-ready.
- Use the root schema in `prompt-card-schema.md`.
- Include a **strict output format**.
- Ask for only the minimum required inputs.

## Naming conventions
- Use `snake_case.md`
- Prefer prefixing by artifact family:
  - `resume_`, `linkedin_`, `inmail_`, `interview_`, `project_`, `outreach_`
  - or for other topics: `proposal_`, `memo_`, `debug_`, `runbook_`, etc.

## Where to place files
- Topic-specific prompt cards go in: `gpts/<topic>/prompts/`
- Shared snippets/templates go in: `shared/snippets/` and `shared/templates/`
