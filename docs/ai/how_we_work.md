# How We Work With the Copilot

## Non-negotiables
- Do not invent behavior, logs, requirements, or versions.
- Prefer small, reversible changes.
- Always include a verification plan (tests or checklist).
- Keep outputs patch-oriented (diffs or file-level changes).
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
