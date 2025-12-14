# Career Assets Copilot

Resumes, LinkedIn, outreach, project case studies, interview prep, and offer negotiation.
**Status:** complete

## Quick start

1. Paste builder instructions from [gpt-instructions/career-assets_instructions.md](gpt-instructions/career-assets_instructions.md) into the Custom GPT builder.
2. Upload [knowledge/career_assets_playbook.md](knowledge/career_assets_playbook.md) into GPT Knowledge.
3. Use [router/00-router.md](router/00-router.md) to select the right prompt card.
4. Copy a prompt card from [prompts/](prompts/), fill placeholders, and run.

## Prompt cards

- `resume_tailor_ats.md` — Tailor resume to a JD (ATS-safe, truthful)
- `resume_rewrite_baseline.md` — Baseline resume rewrite for a target role family
- `linkedin_about.md` — LinkedIn headline + About (A/B versions)
- `cover_letter.md` — Short cover letter mapped to the JD
- `outreach_email_hiring_manager.md` — Personalized hiring manager email
- `recruiter_agency_pitch.md` — Recruiter/agency pitch email + connection note
- `interview_prep.md` — Structured interview prep + cheat sheet
- `offer_comparison_negotiation.md` — Offer comparison + negotiation templates

## Output quality rules

- Ask ≤ 3 clarifying questions only when required to proceed.
- If uncertain, list assumptions (max 5).
- Do not invent facts, logs, or metrics. Request inputs.
- Always include a verification plan (tests, checklist, or acceptance criteria).
