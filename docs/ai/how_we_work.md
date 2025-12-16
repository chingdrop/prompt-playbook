# How We Work With the Copilot

This document defines the collaboration rules and quality bar for copilot-assisted work in this repository.

## Non-negotiables

- Do not invent behavior, logs, requirements, versions, configurations, timelines, or metrics.
- Do not fabricate market data or competitor facts; request sources or label assumptions.
- Separate **Facts**, **Assumptions**, and **Recommendations** when analyzing or planning.
- Prefer small, reversible changes.
- Keep outputs patch-oriented (diffs or file-level changes).
- Always include a verification plan (tests or checklist).
- Avoid sharing secrets; redact tokens and credentials.

## Preferred response format

1) Plan (bullets)
2) Patch (diff or file blocks)
3) Tests/verification
4) Edge cases/risks
5) Next steps

## Collaboration rules

- If the task is ambiguous, ask up to 3 clarifying questions.
- If assumptions are required, list them explicitly (max 5).
- Use consistent naming and match repo conventions.
- When touching auth/secrets/data handling, include a lightweight threat model.
- For operational plans/runbooks, include:
  - prerequisites
  - step-by-step actions
  - acceptance criteria
  - rollback plan (and rollback triggers)

## “Done” definition (lightweight)

A change is “done” when:

- The intended behavior is described (what changed and why).
- The patch is minimal and scoped.
- Verification is explicit and actionable (commands or checklist).
- Risks and follow-ups are recorded (issue/PR/task link if applicable).
