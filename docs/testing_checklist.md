# Testing Checklist for Custom GPT Playbooks

Use this checklist after any significant change to a topic’s `gpt-instructions/` or `knowledge/`.

## Core behavior

- [ ] Asks ≤ 3 clarifying questions when required; otherwise proceeds.
- [ ] Lists assumptions (max 5) if proceeding with uncertainty.
- [ ] Does not invent facts, metrics, dates, tools, or claims.
- [ ] Produces outputs in the requested strict format.

## Topic-specific tests (run 3)

Pick three representative prompts from `gpts/<topic>/prompts/` and run them end-to-end.

### Career Assets

- [ ] JD → Resume tailoring produces: keyword map + resume + change log + gaps.
- [ ] LinkedIn About produces Version A/B + keywords + tighten pass.

### Document Writing

- [ ] Proposal/SOW uses the schema headings and includes exclusions/assumptions.
- [ ] Email update stays under the specified word count and includes a clear CTA.

### Business Analysis

- [ ] Decision memo uses objective/constraints/options/recommendation/risks/next steps.
- [ ] Pricing model includes assumptions + sensitivity notes + exclusions guidance.

### Coding & Automation

- [ ] Debug triage ranks hypotheses and gives diagnostics + fix plan + verification.
- [ ] Django start includes layout tree + security checklist + tooling defaults.

### IT Delivery

- [ ] Runbook uses reversible diagnostics and includes rollback and verification.
- [ ] Change plan has pre-change, implementation, rollback, verification, comms.

## Capabilities

- [ ] Memory: retains preferences without storing sensitive details.
- [ ] File upload: can ingest a resume/log and respond appropriately.
- [ ] Web browsing: used only when “current/latest” matters or when asked.

## Regression check

- [ ] At least one ambiguous prompt still routes correctly.
