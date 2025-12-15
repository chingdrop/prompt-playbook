# Coding & Automation Copilot

Python/Django implementation, debugging, refactoring, and automation — optimized for production-ready quality, maintainability, and secure defaults.

**Status:** complete

## Quick start

1. Paste builder instructions from [`gpt-instructions/coding_automation_copilot_instructions.md`](gpt-instructions/coding_automation_copilot_instructions.md) into the Custom GPT Builder.
2. Upload [`knowledge/coding_automation_playbook.md`](knowledge/coding_automation_playbook.md) into GPT Knowledge.
3. Use [`router/00_router.md`](router/00_router.md) to select the best prompt card.
4. Copy a prompt card from the [Top prompt cards](#prompt-cards) list below (files live under `prompts/`), fill placeholders, and run.

## Prompt cards

<!-- BEGIN:prompt-cards (auto-generated) -->
- [`automation_cli_tool.md`](prompts/automation_cli_tool.md) — building a small automation/ETL script with predictable behavior
- [`code_review_quality_gate.md`](prompts/code_review_quality_gate.md) — reviewing a PR/snippet and producing actionable improvements
- [`debug_triage_ranked_hypotheses.md`](prompts/debug_triage_ranked_hypotheses.md) — diagnosing errors and unexpected behavior quickly and safely
- [`django_project_bootstrap_best_practices.md`](prompts/django_project_bootstrap_best_practices.md) — starting a Django project/app with sane defaults and security hygiene
- [`git_diff_patch_review.md`](prompts/git_diff_patch_review.md) — tightening a change before PR
- [`implement_feature_spec_to_code.md`](prompts/implement_feature_spec_to_code.md) — implementing a feature with clear acceptance criteria
- [`project_onboarding_context_pack.md`](prompts/project_onboarding_context_pack.md) — starting work on a new repo quickly
- [`refactor_safely_with_tests.md`](prompts/refactor_safely_with_tests.md) — improving maintainability without changing behavior
- [`security_review_threat_model_lite.md`](prompts/security_review_threat_model_lite.md) — quickly identifying security risks in code touching auth/data/secrets
- [`test_plan_and_validation.md`](prompts/test_plan_and_validation.md) — creating a verification plan for a change when tests are missing or unclear
<!-- END:prompt-cards -->

## Output quality rules

- Ask ≤ 3 clarifying questions only when required to proceed.
- If uncertain, list assumptions (max 5).
- Do not invent logs/errors/metrics. Request them.
- Always include a verification plan (tests or checklist).
