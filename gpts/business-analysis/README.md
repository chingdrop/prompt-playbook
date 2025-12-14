# Business Analysis Copilot

Decision memos and trade-off analysis, pricing models and assumptions, risk registers and mitigation plans, project plans and milestone schedules, stakeholder updates and KPI framing.

**Status:** complete

## Quick start

1. Paste builder instructions from [`gpt-instructions/business_analysis_copilot_instructions.md`](gpt-instructions/business_analysis_copilot_instructions.md) into the Custom GPT Builder.
2. Upload [`knowledge/business_analysis_playbook.md`](knowledge/business_analysis_playbook.md) into GPT Knowledge.
3. Use [`router/00-router.md`](router/00-router.md) to select the right prompt card.
4. Copy a prompt card from the [Prompt cards](#prompt-cards) list below (files live under `prompts/`), fill placeholders, and run.

## Prompt cards

- [`decision_memo_tradeoffs.md`](prompts/decision_memo_tradeoffs.md)
- [`pricing_model_sensitivity.md`](prompts/pricing_model_sensitivity.md)
- [`risk_register_mitigation.md`](prompts/risk_register_mitigation.md)
- [`project_plan_milestones.md`](prompts/project_plan_milestones.md)
- [`stakeholder_update_kpi.md`](prompts/stakeholder_update_kpi.md)
- [`kpi_framing_and_targets.md`](prompts/kpi_framing_and_targets.md)

## Planned prompt cards (create next)

- `assumptions_sources_log.md`
- `options_tradeoff_matrix.md`

## Output quality rules

- Ask ≤ 3 clarifying questions only when required to proceed.
- Do not fabricate market/competitor facts or metrics; request sources or use placeholders and label assumptions.
- Clearly separate **Facts**, **Assumptions**, and **Recommendations**.
- Use explicit evaluation criteria and decision logic.
- Always include a verification checklist.
