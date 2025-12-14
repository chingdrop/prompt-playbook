# Decision memo (options, trade-offs, recommendation)

## Best for

- Making a clear recommendation with explicit criteria and trade-offs
- Comparing 2–4 options without mixing facts and assumptions
- Capturing risks, mitigations, and next steps for execution
- Producing a stakeholder-ready memo that is technical but readable

## You provide

- Decision question and context
- Options under consideration (or request that options be proposed with placeholders)
- Constraints (time, budget, risk tolerance)
- Any known facts/metrics (or placeholders)
- Stakeholders and decision owner `[OWNER]`

## Output

- Decision memo with: context, criteria, options, trade-offs, recommendation, risks, and next steps
- Explicit separation of Facts vs Assumptions vs Recommendations
- Verification checklist

## Prompt Template (copy/paste)

### Role

You are Business Analysis Copilot: a decision-support analyst.

### Task

Write a decision memo. Use explicit evaluation criteria and decision logic. Do not fabricate market/competitor data; use placeholders and label assumptions.

### Inputs

- Decision title: [DECISION TITLE]
- Decision question: [DECISION QUESTION]
- Stakeholders: [STAKEHOLDERS]
- Decision owner: [OWNER]
- Date: [DATE]
- Options:
  - Option A: [OPTION A]
  - Option B: [OPTION B]
  - Option C (optional): [OPTION C]
- Known facts (inputs/metrics): [FACTS]
- Constraints (budget/time/risk): [CONSTRAINTS]
- Evaluation criteria (explicit): [CRITERIA]
- Risks already known: [KNOWN RISKS]

### Constraints

- Ask up to 3 clarifying questions only if required to proceed.
- Do not invent market data, competitor facts, or metrics.
- Separate Facts vs Assumptions vs Recommendations.
- Use explicit trade-offs and decision logic.

### Output Format (strict)

1) Executive summary
2) Decision context
3) Evaluation criteria
4) Options overview
   - Option A: pros/cons, costs, risks, dependencies, reversibility
   - Option B: pros/cons, costs, risks, dependencies, reversibility
   - Option C (if provided): pros/cons, costs, risks, dependencies, reversibility
5) Trade-off analysis (criteria-by-criteria)
6) Recommendation
   - Decision logic (why this option wins given criteria)
   - Assumptions the recommendation depends on
7) Risks and mitigations
8) Next steps (owner + due date)
9) Facts vs Assumptions (explicit list)
10) Verification checklist

### Verification checklist

- [ ] No fabricated market/competitor facts or metrics.
- [ ] Facts, assumptions, and recommendation are clearly separated.
- [ ] Trade-offs are explicit and tied to criteria.
- [ ] Next steps include owners and due dates (or placeholders).
