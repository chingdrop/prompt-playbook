# docs/ai templates

These are **copy/paste templates** intended to be placed into the project repository you want an AI copilot to support.

Recommended workflow:

1) Copy this folder into your project repo as `docs/ai/`.
2) Fill out [`context.md`](context.md) first (keep it factual; use placeholders if unknown).
3) Use [`how_we_work.md`](how_we_work.md) to define collaboration rules and guardrails.
4) Use [`decision_log.md`](decision_log.md) to record “why” behind important decisions.

## How to use with a Custom GPT

- If you create a **project-specific GPT**, upload these `docs/ai/*.md` files into that GPT’s **Knowledge** (do not include secrets).
- If you use a shared/general GPT, attach these files to the conversation or paste relevant sections when starting work.

## Safety and accuracy notes

- Do **not** include credentials, tokens, or private keys. Redact sensitive values.
- Do **not** add market/competitor “facts” unless you include a source; otherwise label as an assumption.
- Keep internal references as Markdown links (Obsidian-friendly): [`path`](path)

Updated: [YYYY-MM-DD]
