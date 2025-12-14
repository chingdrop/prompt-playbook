# IT Delivery Copilot

Incident triage and diagnostics (Windows, M365/Entra, networking), change planning with rollback, implementation runbooks and checklists, post-incident reports (PIR), and client-facing status updates — technical but readable.

**Status:** complete

## Quick start

1. Paste builder instructions from [`gpt-instructions/it_delivery_copilot_instructions.md`](gpt-instructions/it_delivery_copilot_instructions.md) into the Custom GPT Builder.
2. Upload [`knowledge/it_delivery_playbook.md`](knowledge/it_delivery_playbook.md) into GPT Knowledge.
3. Use [`router/00_router.md`](router/00_router.md) to select the right prompt card.
4. Copy a prompt card from the [Prompt cards](#prompt-cards) list below (files live under `prompts/`), fill placeholders, and run.

## Prompt cards

- [`incident_triage_diagnostics.md`](prompts/incident_triage_diagnostics.md)
- [`windows_endpoint_triage.md`](prompts/windows_endpoint_triage.md)
- [`m365_entra_issue_triage.md`](prompts/m365_entra_issue_triage.md)
- [`network_connectivity_triage.md`](prompts/network_connectivity_triage.md)
- [`service_health_incident_assessment.md`](prompts/service_health_incident_assessment.md)
- [`change_plan_with_rollback.md`](prompts/change_plan_with_rollback.md)
- [`implementation_runbook.md`](prompts/implementation_runbook.md)
- [`maintenance_window_checklist.md`](prompts/maintenance_window_checklist.md)
- [`post_incident_report_pir.md`](prompts/post_incident_report_pir.md)
- [`client_status_update.md`](prompts/client_status_update.md)

## Output quality rules

- Ask ≤ 3 clarifying questions only when required to proceed.
- If uncertain, list assumptions (max 5) and the next data needed.
- Do not invent facts (configs, settings, event IDs, tenant state, timelines). Request logs and exact evidence.
- Always include verification steps and stop conditions when troubleshooting.
- For changes: always include rollback and acceptance criteria.
