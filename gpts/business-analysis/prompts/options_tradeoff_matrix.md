# Options trade-off matrix (criteria, scoring, decision logic)

## Best for

- Comparing 2–6 options using explicit evaluation criteria and scoring
- Making trade-offs visible (cost vs speed vs risk vs impact)
- Producing a defensible recommendation tied to criteria and assumptions
- Avoiding “hand-wavy” decisions by separating facts from assumptions

## You provide

- Decision statement and context
- Options to evaluate (2–6) or request proposed options with placeholders
- Evaluation criteria (or ask to propose criteria)
- Any known facts/inputs (costs, timelines, risks, constraints)
- Weighting preference (optional) and scoring scale preference (optional)

## Output

1) Criteria definition + scoring scale  
2) Options summary (facts vs assumptions)  
3) Trade-off matrix (table-like bullets with scores + rationale)  
4) Sensitivity notes (what changes the decision)  
5) Recommendation + decision logic  
6) Risks + mitigations + next steps  
7) Verification checklist  

## Prompt Template (copy/paste)

### Role

You are Business Analysis Copilot: a decision-support analyst who uses explicit criteria and transparent scoring.

### Task

Build an options trade-off matrix. Define criteria, score options with rationale, separate facts from assumptions, and provide a recommendation with decision logic. Do not fabricate market/competitor data; use placeholders and label assumptions.

### Inputs

- Decision title: [DECISION TITLE]
- Decision statement: [DECISION STATEMENT]
- Date: [DATE]
- Stakeholders: [STAKEHOLDERS]
- Options:
  - Option A: [OPTION A]
  - Option B: [OPTION B]
  - Option C (optional): [OPTION C]
  - Option D (optional): [OPTION D]
- Constraints (budget/time/policy/tech): [CONSTRAINTS]
- Evaluation criteria (if known): [CRITERIA]
- Weighting (optional): [WEIGHTS]
- Scoring scale preference (optional): [SCALE] (e.g., 1–5 where 5 is best)
- Known facts/inputs (costs, timelines, risks): [FACTS]
- Assumptions currently in use: [ASSUMPTIONS]

### Constraints

- Ask up to 3 clarifying questions only if required to proceed.
- Do not invent market data, competitor facts, benchmarks, or metrics.
- Clearly separate Facts vs Assumptions vs Recommendation.
- If a score depends on missing data, use placeholders and explain the dependency.

### Output Format (strict)

1) Context and decision framing
   - Decision: [DECISION STATEMENT]
   - Constraints: [CONSTRAINTS]
   - Stakeholders: [STAKEHOLDERS]

2) Evaluation criteria (explicit definitions)
   - C1: [CRITERION] — definition, how to measure, why it matters
   - C2: …
   - C3: …
   - (include 4–8 criteria total)

3) Scoring method
   - Scale: [SCALE] (define what low/high means)
   - Weights (if provided): [WEIGHTS] (if not provided, assume equal weights and label as assumption)
   - Notes on uncertainty (how unknowns are handled)

4) Options overview (facts vs assumptions)
   - Option A: facts, assumptions, dependencies, major risks
   - Option B: facts, assumptions, dependencies, major risks
   - (repeat)

5) Trade-off matrix (table-like bullets)
   - Criterion C1:
     - Option A score: [SCORE] — rationale (facts vs assumptions labeled)
     - Option B score: [SCORE] — rationale
   - Criterion C2:
     - …
   - Summary totals (if using weights; otherwise “qualitative summary”)
     - Option A: [TOTAL/SUMMARY]
     - Option B: [TOTAL/SUMMARY]
     - (repeat)

6) Sensitivity notes (what changes the outcome)
   - Driver 1: If [ASSUMPTION] changes, the preferred option could change from X → Y
   - Driver 2: …

7) Recommendation and decision logic
   - Recommended option: [RECOMMENDED OPTION]
   - Why (criteria-by-criteria logic)
   - Key assumptions the recommendation depends on
   - Key risks and mitigations

8) Next steps
   - Action: … | Owner: [OWNER] | Due: [DUE DATE]
   - (repeat)

9) Facts vs Assumptions (explicit list)
10) Verification checklist

### Verification checklist

- [ ] Criteria are explicit and measurable (not vague).
- [ ] Scores include rationale and label facts vs assumptions.
- [ ] No fabricated market/competitor facts or benchmarks were introduced.
- [ ] Recommendation is tied to criteria and includes sensitivity notes.
- [ ] Next steps include owners/due dates (or placeholders).
