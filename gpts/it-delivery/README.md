# IT Delivery & Troubleshooting Copilot

Windows/M365/Entra/networking diagnostics and delivery plans.

**Status:** scaffold

## Quick start
1. Paste builder instructions from [gpt-instructions/it-delivery_instructions.md](gpt-instructions/it-delivery_instructions.md) into the Custom GPT builder.
2. Use [router/00-router.md](router/00-router.md) to select the right prompt card.
3. Copy a prompt card from [prompts/](prompts/), fill placeholders, and run.

## Prompt cards
- (Recommended) `incident_triage_runbook.md`
- (Recommended) `change_plan_with_rollback.md`
- (Recommended) `m365_tenant_hardening_checklist.md`
- (Recommended) `network_diagnostics_playbook.md`
- (Recommended) `post_incident_report.md`

Status: scaffold — prompt cards are not yet included in this repo for this topic.

## Output quality rules
- Ask ≤ 3 clarifying questions only when required to proceed.
- If uncertain, list assumptions (max 5).
- Do not invent facts, logs, or metrics. Request inputs.
- Always include a verification plan (tests, checklist, or acceptance criteria).
