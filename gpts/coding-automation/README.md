# Coding & Automation Copilot

Python/Django implementation, debugging, refactoring, and automation — optimized for production-ready quality, maintainability, and secure defaults.

**Status:** complete

## Quick start

1. Paste builder instructions from [`gpt-instructions/coding_automation_copilot_instructions.md`](gpt-instructions/coding_automation_copilot_instructions.md) into the Custom GPT Builder.
2. Upload [`knowledge/coding_automation_playbook.md`](knowledge/coding_automation_playbook.md) into GPT Knowledge.
3. Use [`router/00_router.md`](router/00_router.md) to select the best prompt card.
4. Copy a prompt card from the [Top prompt cards](#top-prompt-cards) below (files live under `prompts/`), fill placeholders, and run.

## Top prompt cards

- [`prompts/project_onboarding_context_pack.md`](prompts/project_onboarding_context_pack.md)
- [`prompts/git_diff_patch_review.md`](prompts/git_diff_patch_review.md)
- [`prompts/debug_triage_ranked_hypotheses.md`](prompts/debug_triage_ranked_hypotheses.md)
- [`prompts/implement_feature_spec_to_code.md`](prompts/implement_feature_spec_to_code.md)
- [`prompts/django_project_bootstrap_best_practices.md`](prompts/django_project_bootstrap_best_practices.md)
- [`prompts/refactor_safely_with_tests.md`](prompts/refactor_safely_with_tests.md)
- [`prompts/automation_cli_tool.md`](prompts/automation_cli_tool.md)
- [`prompts/code_review_quality_gate.md`](prompts/code_review_quality_gate.md)
- [`prompts/security_review_threat_model_lite.md`](prompts/security_review_threat_model_lite.md)
- [`prompts/test_plan_and_validation.md`](prompts/test_plan_and_validation.md)

## Output quality rules

- Ask ≤ 3 clarifying questions only when required to proceed.
- If uncertain, list assumptions (max 5).
- Do not invent logs/errors/metrics. Request them.
- Always include a verification plan (tests or checklist).
