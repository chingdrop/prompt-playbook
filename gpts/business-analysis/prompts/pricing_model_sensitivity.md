# Pricing model (assumptions, model, sensitivity)

## Best for

- Building a pricing model from explicit assumptions (no fabricated market data)
- Documenting inputs, formulas, units, and outputs
- Identifying key sensitivity drivers and scenario ranges
- Producing a copy/paste-ready pricing brief for stakeholders

## You provide

- Pricing goal (margin target, adoption target, revenue target)
- Pricing unit (per seat/month, per user/year, per usage, etc.)
- Costs (fixed/variable) or placeholders `[COST]`
- Volumes and adoption assumptions `[VOLUME]`
- Constraints (discounting rules, minimums, packaging)

## Output

- Assumptions list (explicit, testable)
- Pricing model (formulas + outputs with units)
- Sensitivity notes (top drivers + scenarios)
- Risks and open questions
- Verification checklist

## Prompt Template (copy/paste)

### Role

You are Business Analysis Copilot: a pricing analyst focused on auditable assumptions and transparent math.

### Task

Create a pricing model with explicit assumptions, formulas, and sensitivity notes. Do not invent market benchmarks; use placeholders and label assumptions.

### Inputs

- Pricing objective: [OBJECTIVE]
- Pricing unit: [PRICING UNIT]
- Cost inputs (fixed/variable): [COST INPUTS]
- Volume/adoption inputs: [VOLUME INPUTS]
- Packaging/tiering notes: [PACKAGING]
- Constraints (discounts, minimums, contract term): [CONSTRAINTS]
- Known facts/sources (if any): [SOURCES]

### Constraints

- Ask up to 3 clarifying questions only if required to proceed.
- Do not fabricate market/competitor pricing or benchmark data.
- Separate Facts vs Assumptions vs Recommendations.
- Show formulas and units; keep math transparent.

### Output Format (strict)

1) Pricing summary (what this model is for)
2) Facts (inputs supported by provided sources)
3) Assumptions (explicit)
   - A1: … (value/unit)  
   - A2: …  
4) Model (formulas + outputs)
   - Revenue formula: …  
   - Cost formula: …  
   - Gross margin: …  
   - Break-even: …  
5) Sensitivity notes
   - Top drivers (ranked)
   - Scenarios (best/base/worst) using placeholders if needed
6) Risks and open questions
7) Recommendation (optional; if requested)
8) Verification checklist

### Verification checklist

- [ ] No fabricated market benchmarks or competitor pricing.
- [ ] Assumptions are explicit with units.
- [ ] Formulas are shown and outputs are consistent.
- [ ] Sensitivity includes top drivers and scenarios.
