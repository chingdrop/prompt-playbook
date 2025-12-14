# Business Analysis Copilot

Decision memos, pricing, estimation, risk analysis, planning.

**Status:** scaffold

## Quick start

1. Paste builder instructions from [gpt-instructions/business_analysis_instructions.md](gpt-instructions/business-analysis_instructions.md) into the Custom GPT builder.
2. Use [router/00_router.md](router/00_router.md) to select the right prompt card.
3. Copy a prompt card from [prompts/](prompts/), fill placeholders, and run.

## Prompt cards

- (Recommended) `decision_memo.md`
- (Recommended) `pricing_model_assumptions.md`
- (Recommended) `risk_register.md`
- (Recommended) `project_plan_milestones.md`
- (Recommended) `stakeholder_update.md`

Status: scaffold — prompt cards are not yet included in this repo for this topic.

## Output quality rules

- Ask ≤ 3 clarifying questions only when required to proceed.
- If uncertain, list assumptions (max 5).
- Do not invent facts, logs, or metrics. Request inputs.
- Always include a verification plan (tests, checklist, or acceptance criteria).
