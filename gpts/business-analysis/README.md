# Business Analysis Copilot

Decision memos and trade-off analysis, pricing models and assumptions, risk registers and mitigation plans, project plans and milestone schedules, stakeholder updates, and KPI framing.

**Status:** complete

## Quick start

1. Paste builder instructions from [`gpt-instructions/business_analysis_instructions.md`](gpt-instructions/business_analysis_instructions.md) into the Custom GPT Builder.
2. Upload [`knowledge/business_analysis_playbook.md`](knowledge/business_analysis_playbook.md) into GPT Knowledge.
3. Use [`router/00_router.md`](router/00_router.md) to select the right prompt card.
4. Copy a prompt card from the [Prompt cards](#prompt-cards) below (files live under `prompts/`), fill placeholders, and run.

## Prompt cards

- [`decision_memo_tradeoffs.md`](prompts/decision_memo_tradeoffs.md)
- [`options_tradeoff_matrix.md`](prompts/options_tradeoff_matrix.md)
- [`pricing_model_sensitivity.md`](prompts/pricing_model_sensitivity.md)
- [`assumptions_sources_log.md`](prompts/assumptions_sources_log.md)
- [`risk_register_mitigation.md`](prompts/risk_register_mitigation.md)
- [`project_plan_milestones.md`](prompts/project_plan_milestones.md)
- [`kpi_framing_and_targets.md`](prompts/kpi_framing_and_targets.md)
- [`stakeholder_update_kpi.md`](prompts/stakeholder_update_kpi.md)

## Output quality rules

- Ask ≤ 3 clarifying questions only when required to proceed.
- Do not fabricate market/competitor facts or benchmarks. Request sources or use placeholders and label assumptions.
- Clearly separate **Facts**, **Assumptions**, and **Recommendations**.
- Use explicit evaluation criteria and decision logic.
- Always include a verification checklist.
