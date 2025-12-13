# Prompt Playbook (Monorepo)

A single Git repo that contains **one prompt library per Custom GPT topic**, plus shared snippets/templates.

## Structure

- `shared/` – reusable snippets, templates, and routers across topics
- `gpts/<topic>/` – each topic contains:
  - `gpt-instructions/` – builder instructions for that Custom GPT
  - `prompts/` – copy/paste prompt cards
  - `router/` – topic router prompt
  - `README.md` – topic quick start

## Topics included

- `career-assets/` (complete, ready to use)
- `document-writing/` (scaffold)
- `business-analysis/` (scaffold)
- `coding-automation/` (scaffold)
- `it-delivery/` (scaffold)

## Quick start

1. Open the topic you want, e.g. `gpts/career-assets/README.md`.
2. Copy the builder instructions from `gpts/<topic>/gpt-instructions/`.
3. Use `gpts/<topic>/router/00-router.md` to pick the right prompt card.
4. Paste a prompt card from `gpts/<topic>/prompts/` and fill placeholders.

Generated: 2025-12-13

## Integration
- See `docs/custom_gpt_integration_guide.md`
- Testing: `docs/testing_checklist.md`
