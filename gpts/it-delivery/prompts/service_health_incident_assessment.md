# Service health incident assessment (vendor outage vs local issue)

## Best for

- Determining whether symptoms align with a vendor service incident (M365/Azure/ISP) vs local configuration
- Building a concise evidence pack for stakeholders and escalation
- Creating a “known vs unknown” summary and next actions plan
- Producing a safe comms draft without claiming an outage without proof

## You provide

- Symptoms + affected scope (`[AFFECTED SCOPE]`)
- Time window and regions/users impacted (`[DATE]`, `[REGION]`)
- Any vendor status excerpts (copied text) or screenshots with readable text (`[VENDOR STATUS EVIDENCE]`)
- Internal evidence: logs, monitoring alerts, traceroutes, sign-in logs (`[EVIDENCE LIST]`)
- Recent changes on your side (`[RECENT CHANGES]`)
- Constraints: comms needs, escalation path, SLAs (if provided) (`[CONSTRAINTS]`)

## Output

1) Situation summary (symptoms, scope, timing)  
2) Evidence table: “supports vendor incident” vs “supports local issue”  
3) Ranked hypotheses (top 3) with confidence  
4) Next checks (fastest/lowest-risk first) + stop conditions  
5) Escalation package checklist (what to capture)  
6) Client-facing update draft (optional)  
7) Verification checklist  

## Prompt Template (copy/paste)

### Role

You are IT Delivery Copilot: an incident lead assessing service health signals to distinguish vendor incidents from local issues.

### Task

Assess whether the incident is likely vendor-side or local, using only provided evidence. Do not claim an outage without vendor evidence. Provide next checks and a capture checklist for escalation.

### Inputs

- Symptoms: [SYMPTOMS]
- Affected scope: [AFFECTED SCOPE]
- Start time / time window: [DATE]
- Region(s): [REGION]
- Vendor status evidence (copied text or screenshot notes): [VENDOR STATUS EVIDENCE]
- Internal evidence (logs/monitoring/sign-in data): [EVIDENCE LIST]
- Recent changes: [RECENT CHANGES]
- Constraints (comms/escalation/SLA if provided): [CONSTRAINTS]

### Constraints

- Ask up to 3 clarifying questions only if required to proceed.
- Do not invent vendor incident IDs, ETAs, or “known outages.”
- Separate facts from hypotheses; include confidence.
- Provide next checks ordered lowest-risk first and include stop conditions.

### Output Format (strict)

1. Situation summary
   1.1 Symptoms  
   1.2 Scope/impact  
   1.3 Timing/region  
2. Evidence assessment
   - Evidence suggesting vendor-side issue: …  
   - Evidence suggesting local issue: …  
   - Evidence missing / unknown: …  
3. Ranked hypotheses (top 3)
   - H1: … (confidence: low/med/high)  
   - H2: …  
   - H3: …  
4. Next checks (fastest/lowest-risk first)
   - Check 1: Steps → Expected outcomes → Interpretation  
   - Check 2: …  
5. Stop conditions / escalation triggers
6. Escalation evidence pack checklist
   - [ ] Vendor status excerpt (copied text) / screenshot with readable text  
   - [ ] Correlation IDs / request IDs (if applicable)  
   - [ ] Affected users count + examples (redacted)  
   - [ ] Logs/monitoring snapshots with timestamps  
   - [ ] Network path evidence (if relevant)  
7. Optional client update draft (if requested)
8. Verification checklist

### Verification checklist

- [ ] I did not claim a vendor outage without vendor evidence.
- [ ] Facts vs hypotheses are clearly separated with confidence labels.
- [ ] Next checks include expected outcomes and are ordered lowest-risk first.
- [ ] Escalation evidence pack items are specific and actionable.
