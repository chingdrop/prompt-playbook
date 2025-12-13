# Document Writing Copilot

Proposals, SOWs, quotes, emails, executive summaries.

**Status:** scaffold

## Quick start
1. Paste builder instructions from [gpt-instructions/document-writing_instructions.md](gpt-instructions/document-writing_instructions.md) into the Custom GPT builder.
2. Use [router/00-router.md](router/00-router.md) to select the right prompt card.
3. Copy a prompt card from [prompts/](prompts/), fill placeholders, and run.

## Prompt cards
- (Recommended) `proposal_sow_house_style.md`
- (Recommended) `client_email_update.md`
- (Recommended) `executive_summary.md`
- (Recommended) `meeting_notes_action_items.md`
- (Recommended) `quote_scope_pricing.md`

Status: scaffold — prompt cards are not yet included in this repo for this topic.

## Output quality rules
- Ask ≤ 3 clarifying questions only when required to proceed.
- If uncertain, list assumptions (max 5).
- Do not invent facts, logs, or metrics. Request inputs.
- Always include a verification plan (tests, checklist, or acceptance criteria).
