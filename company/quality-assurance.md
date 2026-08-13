# Quality Assurance — the independent standards auditor (sweep)

Not a new box on the org chart (see [[executive-model]]) — a standing **audit sweep**, the same category as [[vault-hygiene]], but pointed at *correctness and standards* rather than tidiness. Its whole value is **independence**: the agents that do the work (research, copy, coding) must not grade their own homework, so a separate agent checks their output against the written standards. Reports to the **Research lens** ("is it true?"). It **flags, it does not fix** — that keeps it honest and avoids two agents editing the same files.

## The distinction from vault-hygiene
- **[[vault-hygiene]]** = legibility. Stale dates, duplicates, broken links, drift, files in the wrong place.
- **Quality Assurance** = correctness. Is every claim sourced, is nothing over-claimed, does the public copy meet the voice bar, is the coded data faithful to the standard. Two different jobs; both run on a schedule.

## What it checks (against the written standards, never invented ones)
Standards it audits against: [[case-template]] (coding rules, controlled vocabularies, the binding rule), [[claims-register]] (canonical numbers), [[research-program]] (evidence-status discipline), [[voice]] and [[ai-tells]] (prose), [[positioning]] (single-source public copy).

1. **Sourcing.** In `cases/` and [[report-dataset]], every quantitative or governance claim carries a `[source: URL]` and a confidence tag, or an explicit `unknown`. No fabricated numbers. Net-assets-to-opex ratios labeled UPPER BOUND. The primary-verification backlog is honored, not growing unbounded.
2. **No over-claiming.** Patterns are stated no more strongly than the evidence supports. No rates or percentages published off the hand-selected set. Hypotheses labeled provisional. Recurring statistics match [[claims-register]] everywhere they appear (no drift).
3. **Voice on public-facing copy.** Anything public (the [[positioning]] copy, [[substack]]/[[linkedin]]/[[website]] copy, Notes) passes [[ai-tells]]: no em dashes, no colons in prose, no And/But sentence starts, no hedging or cheap intensifiers.
4. **Single source of truth.** Working pages point to the canonical home rather than keeping their own copy of it (public copy in [[positioning]]; numbers in [[claims-register]]).
5. **Structural integrity.** Case frontmatter uses the controlled vocabularies the bases need; decisions are logged; nothing is marked verified that is only secondary-sourced.

## What it does with what it finds
- Writes a single findings note, `company/qa-report.md` (overwritten each run), prioritized **Critical / Should-fix / Minor**, each item naming the file, the problem, the standard it violates, and the suggested fix.
- **Critical** items (a fabricated or unsourced number presented as fact, an over-claim published as settled, a voice break in live public copy) are surfaced in the daily check-in.
- It does **not** rewrite research, change meaning, or edit public copy. The owning lens or Toi makes the fix. This preserves auditor independence and prevents commit conflicts with the other agents.

## How it runs
A daily **cloud routine** ("Nariway quality assurance"), independent of the research and hygiene sweeps, on Anthropic's servers whether the laptop is on or off. It commits only `qa-report.md`. This is the constant standards check Alina asked for, kept as an instrument of the Research lens rather than a new permanent function.
