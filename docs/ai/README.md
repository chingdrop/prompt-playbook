# docs/ai templates

These are **copy/paste templates** intended to live in a project repository (recommended location: `docs/ai/`) so an AI copilot can work with accurate context and consistent guardrails.

## What's included

- [`context.md`](context.md) — factual project context (source of truth; start here)
- [`how_we_work.md`](how_we_work.md) — collaboration rules and quality bar for copilot-assisted work
- [`decision_log.md`](decision_log.md) — lightweight decision records (“ADRs-lite”) to capture *why* choices were made

## Recommended workflow

1) Copy this folder into your project repo as `docs/ai/`.
2) Fill out [`context.md`](context.md) first (keep it factual; use placeholders if unknown).
3) Customize [`how_we_work.md`](how_we_work.md) to match your team’s conventions.
4) Use [`decision_log.md`](decision_log.md) for any decision that would be expensive to re-litigate later.

## How to use with a Custom GPT

- For a **project-specific GPT**, upload the markdown files in `docs/ai/` (for example `docs/ai/*.md`) into that GPT’s **Knowledge**. Do not include secrets.
- For a shared/general GPT, attach these files to the conversation or paste relevant sections when starting work.

## Safety and accuracy notes

- Do **not** include credentials, tokens, private keys, or customer/PHI/PII. Redact sensitive values.
- Do **not** add market/competitor “facts” unless you include a source; otherwise label content as an assumption.
- Keep internal references as markdown links: [`path/to/file.md`](path/to/file.md)

Last updated: [YYYY-MM-DD]
