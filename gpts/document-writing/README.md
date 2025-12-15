# Document Writing Copilot

Proposals, SOWs, quotes/estimates, client emails, executive summaries, and meeting notes — optimized for business clarity, professional tone, and copy/paste readiness.

**Status:** complete

## Quick start

1. Paste builder instructions from [`gpt-instructions/document_writing_instructions.md`](gpt-instructions/document_writing_instructions.md) into the Custom GPT Builder.
2. Upload [`knowledge/document_writing_playbook.md`](knowledge/document_writing_playbook.md) into GPT Knowledge.
3. Use [`router/00_router.md`](router/00_router.md) to select the right prompt card.
4. Copy a prompt card from the [Prompt cards](#prompt-cards) list below (files live under `prompts/`), fill placeholders, and run.

## Prompt cards

<!-- BEGIN:prompt-cards (auto-generated) -->
- [`client_email_update.md`](prompts/client_email_update.md) — crisp client updates that reduce back-and-forth
- [`executive_summary.md`](prompts/executive_summary.md) — 1–2 page summaries that translate technical work into business value
- [`meeting_notes_action_items.md`](prompts/meeting_notes_action_items.md) — converting rough notes into clean minutes with owners and due dates
- [`pricing_table_itemization.md`](prompts/pricing_table_itemization.md) — turning a messy list of materials and labor into clean line items
- [`project_schedule_milestones.md`](prompts/project_schedule_milestones.md) — turning a scope into a simple schedule clients can approve
- [`proposal_sow_house_style.md`](prompts/proposal_sow_house_style.md) — client-facing proposals and SOWs with explicit deliverables, exclusions, schedule, pricing, and terms
- [`quote_scope_pricing.md`](prompts/quote_scope_pricing.md) — simple estimates with clear inclusions, assumptions, and itemized pricing
- [`requirements_intake_questions.md`](prompts/requirements_intake_questions.md) — scoping a proposal/quote when inputs are incomplete
- [`rewrite_edit_with_change_log.md`](prompts/rewrite_edit_with_change_log.md) — rewriting a draft while preserving meaning and commitments
- [`risk_assumptions_exclusions.md`](prompts/risk_assumptions_exclusions.md) — strengthening proposals/quotes against scope creep
<!-- END:prompt-cards -->

## Output quality rules

- Ask ≤ 3 clarifying questions only when required to proceed.
- If uncertain, list assumptions (max 5).
- Do not invent facts (dates, terms, pricing, client details). Request inputs.
- Avoid shorthand notation; use clear units and counts.
- Always include a verification checklist (formatting + scope correctness).
