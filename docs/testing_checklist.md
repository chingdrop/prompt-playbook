# Testing Checklist for Custom GPT Playbooks

Use this checklist after any significant change to a topic’s `gpt-instructions/`, `knowledge/`, `router/`, or `prompts/`.

## Core behavior

- [ ] Asks ≤ 3 clarifying questions when required; otherwise proceeds.
- [ ] Lists assumptions (max 5) if proceeding with uncertainty.
- [ ] Does not invent facts, metrics, dates, tools, or claims.
- [ ] Separates facts vs assumptions vs recommendations when applicable.
- [ ] Produces outputs in the requested strict format.

## Schema and file contract checks (topic-level)

- [ ] Topic folder exists at `gpts/<topic>/` and follows the folder contract in [`docs/repo_consistency_rules.md`](repo_consistency_rules.md).
- [ ] Router exists at `gpts/<topic>/router/00_router.md` and includes an explicit allowlist of prompt filenames.
- [ ] All router allowlisted prompt files exist under `gpts/<topic>/prompts/`.
- [ ] Prompt filenames are snake_case (example: `change_plan_with_rollback.md`).
- [ ] Topic README Quick start links resolve:
  - [ ] Canonical instructions file under `gpt-instructions/`
  - [ ] Canonical knowledge pack under `knowledge/`
  - [ ] Router `router/00_router.md`
  - [ ] Prompt cards under `prompts/`

## Topic-specific tests (run 3)

Pick three representative prompt cards from `gpts/<topic>/prompts/` and run them end-to-end.

### Career Assets

- [ ] JD → Resume tailoring produces: keyword map + resume + change log + gaps.
- [ ] LinkedIn About produces Version A/B + keywords + tighten pass.

### Document Writing

- [ ] Proposal/SOW uses the schema headings and includes exclusions/assumptions.
- [ ] Email update stays under the specified word count and includes a clear CTA.

### Business Analysis

- [ ] Decision memo uses objective/constraints/options/recommendation/risks/next steps.
- [ ] Pricing model includes assumptions + sensitivity notes + sources/placeholder handling.

### Coding & Automation

- [ ] Debug triage ranks hypotheses and gives diagnostics + fix plan + verification.
- [ ] Django start includes layout tree + security checklist + tooling defaults.

### IT Delivery

- [ ] Triage produces ranked hypotheses + next checks + stop conditions.
- [ ] Change plan has pre-change, implementation, rollback, verification, comms, and acceptance criteria.

## Builder sync check (manual)

- [ ] Builder Instructions field matches the canonical `gpt-instructions/<topic>_copilot_instructions.md`.
- [ ] Builder Knowledge includes the canonical `knowledge/<topic>_playbook.md` (and any additional intended knowledge files).
- [ ] Capabilities match topic guardrails (e.g., web search enabled only when appropriate).

## Regression check

- [ ] At least one ambiguous prompt still routes correctly.
- [ ] At least one “missing inputs” scenario produces placeholders rather than invented facts.
