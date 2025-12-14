# Document Writing Copilot

Proposals, SOWs, quotes/estimates, client emails, executive summaries, and meeting notes — optimized for business clarity, professional tone, and copy/paste readiness.

**Status:** complete

## Quick start

1. Paste builder instructions from [`gpt-instructions/document_writing_copilot_instructions.md`](gpt-instructions/document_writing_copilot_instructions.md) into the Custom GPT Builder.
2. Upload [`knowledge/document_writing_playbook.md`](knowledge/document_writing_playbook.md) into GPT Knowledge.
3. Use [`router/00-router.md`](router/00-router.md) to select the right prompt card.
4. Copy a prompt card from the [Prompt cards](#prompt-cards) list below (files live under `prompts/`), fill placeholders, and run.

## Prompt cards

- [`proposal_sow_house_style.md`](prompts/proposal_sow_house_style.md)
- [`quote_scope_pricing.md`](prompts/quote_scope_pricing.md)
- [`executive_summary.md`](prompts/executive_summary.md)
- [`client_email_update.md`](prompts/client_email_update.md)
- [`meeting_notes_action_items.md`](prompts/meeting_notes_action_items.md)
- [`requirements_intake_questions.md`](prompts/requirements_intake_questions.md)
- [`rewrite_edit_with_change_log.md`](prompts/rewrite_edit_with_change_log.md)
- [`risk_assumptions_exclusions.md`](prompts/risk_assumptions_exclusions.md)
- [`project_schedule_milestones.md`](prompts/project_schedule_milestones.md)
- [`pricing_table_itemization.md`](prompts/pricing_table_itemization.md)

## Output quality rules

- Ask ≤ 3 clarifying questions only when required to proceed.
- If uncertain, list assumptions (max 5).
- Do not invent facts (dates, terms, pricing, client details). Request inputs.
- Avoid shorthand notation; use clear units and counts.
- Always include a verification checklist (formatting + scope correctness).
