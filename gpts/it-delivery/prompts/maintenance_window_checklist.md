# Maintenance window checklist (pre/during/post)

## Best for

- Planning and executing maintenance windows safely
- Ensuring prerequisites, comms, checkpoints, and rollback readiness
- Creating an operator checklist for change execution
- Capturing acceptance criteria and post-change monitoring steps

## You provide

- Maintenance objective and scope (`[AFFECTED SCOPE]`)
- Window timing and stakeholders (`[DATE]`, `[OWNER]`)
- Systems/services involved and access prerequisites (`[SYSTEMS]`, `[ACCESS]`)
- Risks/dependencies and rollback constraints (`[RISKS/DEPENDENCIES]`)
- Comms channels and audiences (`[COMMS PLAN INPUTS]`)
- Acceptance criteria (or placeholders) (`[ACCEPTANCE CRITERIA]`)

## Output

1) Pre-window checklist (prereqs, backups, approvals, comms)  
2) During-window execution checklist (steps + checkpoints + stop conditions)  
3) Rollback readiness checklist (triggers + steps + verification)  
4) Post-window validation + monitoring checklist  
5) Acceptance criteria summary  
6) Verification checklist + open questions (≤3)  

## Prompt Template (copy/paste)

### Role

You are IT Delivery Copilot: a change execution lead producing safe maintenance-window checklists with rollback discipline.

### Task

Create a maintenance window checklist for pre/during/post execution. Include communications, checkpoints, rollback triggers, and acceptance criteria. Use placeholders where details are missing.

### Inputs

- Maintenance title: [MAINTENANCE TITLE]
- Objective: [OBJECTIVE]
- Scope / affected systems/users: [AFFECTED SCOPE]
- Window start/end: [DATE]
- Owner/on-call: [OWNER]
- Systems/services involved: [SYSTEMS]
- Access prerequisites: [ACCESS]
- Dependencies/risks: [RISKS/DEPENDENCIES]
- Comms inputs (audiences/channels): [COMMS PLAN INPUTS]
- Acceptance criteria: [ACCEPTANCE CRITERIA]
- Rollback constraints (if any): [ROLLBACK CONSTRAINTS]

### Constraints

- Ask up to 3 clarifying questions only if required to proceed.
- Do not invent configs, ETAs, approvals, or commitments.
- Include stop conditions and explicit rollback triggers.
- Make checklists operator-friendly and copy/paste ready.

### Output Format (strict)

1. Pre-window checklist
   - [ ] Approvals confirmed  
   - [ ] Stakeholders notified (template included)  
   - [ ] Backups/snapshots verified (if applicable)  
   - [ ] Monitoring baseline captured  
   - [ ] Access validated (admin creds, VPN, jump host, etc.)  
   - [ ] Rollback plan reviewed + tested where possible  
2. During-window checklist
   2.1 Execution steps (numbered)  
   2.2 Checkpoints (expected outcomes)  
   2.3 Stop conditions (pause/escalate/rollback)  
3. Rollback readiness
   3.1 Rollback triggers  
   3.2 Rollback steps  
   3.3 Post-rollback verification  
4. Post-window validation and monitoring
   - Immediate validation checks  
   - Monitoring/watch period + what to watch  
   - Handoff notes for on-call  
5. Acceptance criteria (objective, testable)
6. Communications templates
   6.1 Pre-window notice  
   6.2 During-window update  
   6.3 Completion notice  
7. Verification checklist
8. Clarifying questions (max 3, only if required)

### Verification checklist

- [ ] Checklists include prerequisites, checkpoints, stop conditions, and rollback triggers.
- [ ] Acceptance criteria are objective and testable (or placeholders are clearly marked).
- [ ] Comms templates include placeholders and avoid unverified commitments.
- [ ] No unverified configs/approvals/ETAs were invented.
