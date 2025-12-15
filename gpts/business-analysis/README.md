# Business Analysis Copilot

Decision memos and trade-off analysis, pricing models and assumptions, risk registers and mitigation plans, project plans and milestone schedules, stakeholder updates, and KPI framing.

**Status:** complete

## Quick start

1. Paste builder instructions from [`gpt-instructions/business_analysis_instructions.md`](gpt-instructions/business_analysis_instructions.md) into the Custom GPT Builder.
2. Upload [`knowledge/business_analysis_playbook.md`](knowledge/business_analysis_playbook.md) into GPT Knowledge.
3. Use [`router/00_router.md`](router/00_router.md) to select the right prompt card.
4. Copy a prompt card from the [Prompt cards](#prompt-cards) list below (files live under `prompts/`), fill placeholders, and run.

## Prompt cards

<!-- BEGIN:prompt-cards (auto-generated) -->
- [`assumptions_sources_log.md`](prompts/assumptions_sources_log.md) — Creating a single “source of truth” log for facts, assumptions, and open questions
- [`decision_memo_tradeoffs.md`](prompts/decision_memo_tradeoffs.md) — Making a clear recommendation with explicit criteria and trade-offs
- [`kpi_framing_and_targets.md`](prompts/kpi_framing_and_targets.md) — Defining KPIs clearly (formula, unit, owner, cadence)
- [`options_tradeoff_matrix.md`](prompts/options_tradeoff_matrix.md) — Comparing 2–6 options using explicit evaluation criteria and scoring
- [`pricing_model_sensitivity.md`](prompts/pricing_model_sensitivity.md) — Building a pricing model from explicit assumptions (no fabricated market data)
- [`project_plan_milestones.md`](prompts/project_plan_milestones.md) — Building a milestone plan with dependencies and acceptance criteria
- [`risk_register_mitigation.md`](prompts/risk_register_mitigation.md) — Creating a practical risk register with clear mitigations and owners
- [`stakeholder_update_kpi.md`](prompts/stakeholder_update_kpi.md) — Weekly/monthly stakeholder updates that are crisp and decision-oriented
<!-- END:prompt-cards -->

## Output quality rules

- Ask ≤ 3 clarifying questions only when required to proceed.
- Do not fabricate market/competitor facts or benchmarks. Request sources or use placeholders and label assumptions.
- Clearly separate **Facts**, **Assumptions**, and **Recommendations**.
- Use explicit evaluation criteria and decision logic.
- Always include a verification checklist.
