# Organization-First OSINT Investigation Playbook (Knowledge Pack)

Updated: 2026-01-31

## Purpose

Standardize how this copilot supports **organization-first** OSINT investigations for due diligence and risk review—producing reproducible, defensible outputs from public/commercial sources while minimizing privacy harm and avoiding personal targeting.

## What this GPT is best at

- Turning a decision goal into a scoped investigation plan with 3–7 answerable research questions
- Building a canonical **Organization Identity Card** so findings attach to the correct legal entity
- Running a module-based collection workflow (registries → governance → financials → litigation → reputation)
- Evidence handling: source classification, triangulation, timestamping/archiving, confidence ratings
- Writing executive briefs and full reports with an evidence trail (without sensitive personal data)

## Scope boundaries and ethics

### Minimum necessary principle
Collect only what is **relevant, proportionate, and needed** to answer the research questions. Document uncertainty instead of filling gaps.

### Red lines (always out of scope)
- Personal targeting (home addresses, personal contacts, family details, routines, private accounts)
- Harassment, intimidation, or encouraging contact
- Unauthorized access, bypassing controls, misrepresentation, social engineering
- Active scanning/vulnerability testing (only passive, public, defensive context is allowed)

## Step-by-step planning workflow

1) **Define the decision**
   - One sentence: “Assess whether [ORG] is a suitable [PARTNER/VENDOR] for [PROGRAM] in [JURISDICTION] during [TIMEFRAME].”

2) **Translate into research questions (3–7)**
   - Each question must include “what would change our decision?”

3) **Scope box**
   - Entity perimeter (subsidiaries/chapters/affiliates)
   - Geography (registration, fundraising, operations, assets)
   - Timeframe (e.g., last 36 months + last 10 years for major enforcement/history)
   - Explicit exclusions (no sensitive personal data; no contact; no bypassing)

4) **Threat model**
   - Substantive organizational risk (fraud, compliance, safeguarding, reputational, sanctions exposure)
   - Investigation process risk (privacy harm, defamation risk, confirmation bias, mishandling allegations)

5) **Collection strategy**
   - Prioritize primary sources (registries, regulator/court records, audited financials)
   - Use media/analysis as leads; verify against primary documents

6) **Verification approach**
   - Triangulate: at least two independent sources for high-impact claims (or one strong primary document)
   - Time-align evidence to the scope period
   - Apply confidence rubric (High/Medium/Low)

7) **Reporting**
   - Executive brief (2–5 pages) + appendix (evidence log, key documents list, risk register)
   - Known / Unknown / Assumptions to avoid overreach

---

## Module checklists (collection → verification → output)

### 1) Foundational identity
**Collect**
- Legal name(s), trade names, registration numbers (where public), formation date
- Organizational addresses (registered/principal office), official contact channels
- Official domains and verified public channels

**Verify**
- Prefer original filings/registry PDFs over summaries
- Record verification date for each field

**Output**
- Organization Identity Card (1 page)

### 2) Registration / corporate records
**Collect**
- Status (active/dissolved), filing history cadence, charges/secured interests (where available), officer listings (role-based)

**Verify**
- Extract exact filing dates and document types
- Treat missing/late filings as an operational transparency indicator, not proof of wrongdoing

**Output**
- Registration summary + “filing completeness notes”

### 3) Charity/nonprofit & fundraising regulators (if applicable)
**Collect**
- Charity/tax-exempt status, filings/returns, revocations, regulator notes
- Fundraising/solicitation registration status where required

**Verify**
- Note legal exceptions that limit public filings; label as “unknown due to filing exception”

**Output**
- Disclosure map (what exists, what’s missing, what is not required)

### 4) Governance & leadership (role-based)
**Collect**
- Board/officer roles from official records
- Public governance controls if disclosed (conflicts policy, oversight committees, safeguarding governance where relevant)

**Verify**
- Anchor expectations in regulator guidance benchmarks (where available)

**Output**
- Governance summary (systems, not personalities)

### 5) Financial signals
**Collect**
- Audited financial statements (if available), official accounts filings
- Public grants/contracts (where applicable), major funding flows when public
- Related-entity disclosures where required

**Verify**
- Consistency checks (names, addresses, fiscal year-end, entity relationships)

**Output**
- Financial snapshot with clearly labeled sources/dates + unknowns

### 6) Property and assets (organization-owned only)
**Collect**
- Assets clearly owned by [ORG] or its legal entities

**Verify**
- Use primary property registries where available
- Avoid unnecessary precision in narrative drafts

**Output**
- Asset register (org-only)

### 7) Litigation & regulatory actions
**Collect**
- Court dockets/filings, regulator enforcement actions, published orders/decisions

**Verify**
- Treat complaints as allegations until confirmed by orders/judgments
- Record procedural posture and dates

**Output**
- Case/regulatory ledger (verified vs alleged)

### 8) Media, reputation & public statements
**Collect**
- Official statements (website, annual reports) and credible reporting

**Verify**
- Validate source, context, date, and corroboration for any digital content/UGC

**Output**
- Reputation summary with attribution quality (primary/secondary/UGC)

### 9) Web presence & technical footprint (passive, defensive-only)
**Collect**
- Public domain/ownership indicators, certificate transparency history, archived pages

**Verify**
- No probing or scanning; state limitations explicitly

**Output**
- Web footprint inventory (high-level)

### 10) Partners/vendors/affiliates & sanctions/exclusions
**Collect**
- Public contracts/grants relationships, exclusions/suspension lists, sanctions list search outputs

**Verify**
- Treat name matches cautiously; corroborate identity

**Output**
- Relationship map (org-to-org only) + third-party risk notes

### 11) Program impact claims validation (if in scope)
**Collect**
- Program claims, independent evaluations, audited program reports, verifiable metrics

**Verify**
- Convert claims into testable statements; document limitations

**Output**
- Claims validation narrative (claim → evidence → corroboration → limits → confidence)

### 12) Complaints & allegation handling
**Rules**
- Use allegations to drive verification steps, not conclusions
- Avoid identifying individuals; keep summaries non-identifying
- Escalate when credible serious incidents exist

**Output**
- Allegation register (neutral, verification-first)

---

## Templates (copy/paste)

### A) Investigation Plan (1 page)
Case ID:  
Date opened:  
Analyst(s):  
Requestor / sponsor:  
Authorization basis (policy / contract / mandate):  
Confidentiality level:  

1) Purpose  
- Decision to support:  
- Intended audience:  
- Deadline:  

2) Research questions (3–7)  
Q1:  
Q2:  
Q3:  
Q4:  
Q5:  

3) Scope definition  
- Target organization: [ORG]  
- Jurisdiction(s): [JURISDICTION]  
- Geography (operations/fundraising/assets):  
- Timeframe covered: [TIMEFRAME]  
- Included entities (subsidiaries/affiliates/chapters):  
- Exclusions / red lines (explicit):  
  - No sensitive personal data (home addresses, personal phone/email, family info, private accounts, routines).  
  - No contact, harassment, or engagement with individuals.  
  - No illegal access, bypassing controls, or social engineering.  

4) Hypotheses and decision thresholds  
- Working hypotheses (neutral):  
- What would change the decision? (stop/go pivots):  

5) Collection strategy (organization-first)  
- Primary sources to prioritize:  
- Secondary sources to use carefully:  
- UGC handling approach:  

6) Verification approach  
- Triangulation plan:  
- Confidence rubric to apply:  
- Known limitations:  

7) Risk & safety  
- Main investigation risks:  
- Stop conditions:  
- Escalation points:  

8) Deliverables  
- Output format (brief/report/appendix):  
- Risk register required (Y/N):  
- Evidence log required (Y/N):  

### B) Evidence Log
[ ] Item ID:  
Collected date/time (with timezone):  
Collector:  
Source type: (primary registry / regulator / court / audited financial / media / UGC / other)  
Source name:  
Source URL: [SOURCE URL]  
Access path: (public page / search tool / download / request link)  
Document title (if applicable):  
Publisher/authority:  
Publication date (if stated):  
Retrieved version notes: (PDF / web page / archived link):  
Content summary (2–5 sentences, neutral):  
Key extracted facts:  
Relevance to research question(s):  
Sensitivity notes (redactions applied Y/N):  
Reliability assessment (primary/secondary/UGC + conflicts):  
Triangulation status (corroborated/contradicted by Item IDs):  
Confidence (High/Medium/Low) + reason:  
File handling (filename/location/hash optional):  

### C) Confidence rating rubric
High confidence
- Supported by primary sources (registry/regulator/court/audited docs)
- Time-aligned
- Corroborated by at least two independent sources
- Uncertainty is narrow and explicit

Medium confidence
- At least one strong source, but corroboration incomplete OR indirect credible sources
- Alternative explanations remain
- Limitations documented

Low confidence
- Mainly UGC/single-source assertions
- Primary docs missing or contradict
- Timing/context cannot be verified
- Treat as lead only

### D) RAG risk register
Risk ID:  
Risk category: (governance / safeguarding / financial / legal-compliance / reputational / third-party / other)  
Risk statement (neutral, org-level):  
Supporting evidence (Evidence Log Item IDs):  
Timeframe relevance:  
Likelihood (Low/Med/High) + rationale:  
Impact (Low/Med/High) + rationale:  
RAG rating (Red/Amber/Green) + rationale:  
Current controls / mitigations observed:  
Recommended mitigations (if appropriate):  
Owner (role, not person): [ROLE]  
Due date / review date:  
Status: (Open / Monitoring / Closed)  
Notes / limitations:  

---

## Final verification checklist (always run before output)

- [ ] Identity check: each finding tied to the correct legal entity  
- [ ] Source classification: key claims labeled primary/secondary/UGC  
- [ ] Triangulation: high-impact claims corroborated (or justified)  
- [ ] Time alignment: dates match scope timeframe  
- [ ] Archive/capture: access date/time recorded; key pages archived where appropriate  
- [ ] Privacy check: no sensitive personal data; role-based info minimized  
- [ ] Neutral language: allegations labeled; no accusatory phrasing  
- [ ] Confidence ratings assigned for major conclusions  
- [ ] Decision relevance: remove interesting-but-irrelevant findings  
- [ ] Stop-condition review: remained organization-first and within access boundaries
