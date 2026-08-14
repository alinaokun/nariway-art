# QA Report — 2026-08-14

**Verdict:** Sourcing discipline in `cases/` and `report-dataset.md` is genuinely strong (every quantitative claim carries a source and confidence tag, upper-bound ratios are consistently labeled, gaps are honestly `unknown`), and public-facing copy in `positioning.md` / the live LinkedIn and Substack bios is voice-clean. The real problems are structural: five early "pilot" case files were never migrated to the controlled vocabulary `case-template.md` later locked, and in three of those cases the frontmatter now contradicts the authoritative coding sitting in `report-dataset.md` for the same case. One of those five also overstates its verification status. Nothing found is a fabricated number or a published over-claim.

---

## CRITICAL

1. **`cases/neue-galerie.md` frontmatter claims a verification level the case doesn't have.** `verification: verified` is not a value in `case-template.md`'s controlled vocabulary (`Provisional` · `Spot-verified` · `Primary-verified`), and it overstates confidence: `report-dataset.md` entry #3 (this same case, Neue Galerie → The Met) codes it **Spot-verified**, with the Met press-release source flagged "re-fetch; was 429" and all dollar figures `unknown`. This is the exact pattern the QA remit calls out: something marked `verified` that is actually only secondary/spot-sourced. **Fix:** change the frontmatter to `verification: spot-verified` to match `report-dataset.md`.

---

## SHOULD-FIX

2. **Five pilot-era case files (`sample: designed-10`) were never synced to the locked case-template vocabulary, and three now contradict `report-dataset.md`'s own coding of the same cases.** Standard: `case-template.md`'s binding rule that controlled-vocabulary values must come from the fixed lists "so the vocabulary stays stable across all ~80 rows," and `Cases.base`'s Pipeline/Board views render these exact frontmatter fields, so an invalid or contradictory value silently miscodes the pathway/outcome charts.
   - `cases/terra.md`: `pathway: museum-dissolved` (not a pathway value — the vocab describes disposition forms, not outcomes) and `outcome: collapsed` (not in the `outcome_category` list). `report-dataset.md` #7 codes this same case `pathway: found-standalone-museum`, `outcome: closed-dispersed`. **Fix:** correct both fields to match.
   - `cases/neue-galerie.md`: `pathway: merge-for-perpetuity` (invalid; should be `merger-into-institution`) and `outcome: pivot` (invalid; `report-dataset.md` #3 codes this case's outcome as **merged**, not pivoted). **Fix:** correct both fields.
   - `cases/di-rosa.md`: `pathway: museum+park` (invalid; `report-dataset.md` #9 and the template both use `found-art-park`). **Fix:** correct the field.
   - `cases/mcnay.md`: `pathway: house-to-museum` (invalid; should be `found-house-museum`), `verification: in-progress` (not a template value), and `decision_owner: founder-self` (not in the H7A vocab; `case-template.md`'s own McNay worked example, sourced from `mcnay-packet.md`, codes `decision_owner: collector-alone` for this exact case). **Fix:** correct all three fields.
   - `cases/souls-grown-deep.md`, `cases/terra.md`, `cases/di-rosa.md`: `decision_owner: unknown` — "unknown" is not one of the 13 allowed `decision_owner` values (the vocab's gap value is `no-identifiable-person`). For Souls Grown Deep this also contradicts `report-dataset.md` #1, which codes decision **foundation-executive** for that case.
   The correct values already exist in `report-dataset.md` / `case-template.md` for four of these five cases — this is a one-time sync pass, not new research.

3. **A decision marked "awaiting Alina" has actually been made and implemented.** `company/decisions/2026-08-12-email-delivery.md` still reads "Status, awaiting Alina" at the top, but `company/it.md` confirms the Resend option it recommends is now **LIVE** ("Transactional email. Resend... LIVE for the daily Signals and check-in emails via the pipeline below... proven working 2026-08-14"). Standard: QA remit (f), settled decisions in `company/decisions/` should not still read open. **Fix:** update the status line to record the decision as accepted/implemented.

4. **Drafted public copy for alinaokun.com uses em dashes, and the live-page punctuation was never actually checked.** `marketing/website.md`'s "finalized copy, 2026-08-13" block for the Projects and Writing sections is written entirely in em-dash bullets ("Nariway — Independent work on...", "The Brief Experiment — A history of...", "Luminary Leadership — Co-authored.", etc.). The later "LIVE revised, confirmed 2026-08-14" verification pass says structure matches the live page but explicitly flags: "Could not verify exact About-text punctuation from a paraphrase, worth a quick self-check against the no-em-dash / no-colon rule." So this is public copy destined for (or possibly already on) a live site that has never actually cleared the `voice.md`/`ai-tells.md` em-dash ban. **Fix:** rewrite the bulleted lines without em dashes, and close the open punctuation check against the actual live page.

5. **The primary-verification backlog is growing, not being worked down, and this QA run's own spot-check confirms why.** `report-dataset.md` shows the backlog going from 4 cases (Batch 2) to 7 cases (Batch 3, ~19% of the 36 coded), because WebFetch to ProPublica has returned `EGRESS_BLOCKED` in every research session so far (2026-08-13, 2026-08-14). This QA session independently tried WebFetch against `projects.propublica.org` and `en.wikipedia.org` to spot-check two cited figures (Terra's $614.5M net assets; Hillwood's FY2024 990 numbers) and got the identical `EGRESS_BLOCKED` result on both, so the block is systemic, not session-specific. Standard: QA remit (a), "the primary-verification backlog is honored, not growing unbounded." The standing instruction to retry WebFetch "whenever it's actually working" has not worked across at least three sessions. **Recommendation:** stop retrying WebFetch as the mitigation and pursue the already-identified alternative (`report-dataset.md` line 7: IRS bulk 990 XML index) before coding more cases into the secondary-only pile.

---

## MINOR

6. **`marketing/flagship-report.md` restates a stale coverage count.** It says "~30 of 50 cases coded" (line 60), while `cases/report-dataset.md` — the authoritative live count — is at "36 of 50 coded" as of 2026-08-14. Not contradictory in spirit, just stale. **Fix:** update the figure or point to `report-dataset.md` rather than restating a number that will keep drifting.

7. **Field-name mismatch between template and case files.** `case-template.md` specifies the field `verification_status` with capitalized values (`Provisional`, `Spot-verified`, `Primary-verified`); every actual case file instead uses a lowercase `verification:` field with lowercase values. Harmless in practice since it's applied consistently, but worth normalizing so the template and the files literally match.

---

**Counts:** 1 critical / 4 should-fix / 2 minor.
