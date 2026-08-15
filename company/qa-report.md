# QA Report — 2026-08-15

**Verdict:** No critical findings this run. Sourcing discipline across the 24 rows in `report-dataset.md` and the newest case files (Fondation Beyeler, Vogel Collection, De la Cruz Collection, JPMorgan Chase, Enron, Deutsche Bank, Benini, Yuz Museum) remains genuinely strong: every figure carries a source and confidence tag or an honest `unknown`, every net-assets ratio is labeled UPPER BOUND, hypotheses stay hedged ("not a rate," "one case," "flagged, not confirmed"), and public-facing profile copy in `positioning.md` is voice-clean. The problems are the same structural ones flagged in the 2026-08-14 report, and most are still open: five pilot-era case files were never synced to the locked `case-template.md` vocabulary and still contradict `report-dataset.md`'s own coding of the same cases, `flagship-report.md`'s case-count is now more stale than before, and the primary-verification backlog keeps growing while the recommended alternative to WebFetch has not been tried.

---

## CRITICAL

None this run.

---

## SHOULD-FIX

1. **Four pilot-era case files still contradict `report-dataset.md`'s authoritative coding of the same cases, unchanged since the 2026-08-14 audit — and one contradiction was missed last time.** Standard: `case-template.md`'s binding rule that controlled-vocabulary fields come only from the fixed lists, and `Cases.base`'s Pipeline/Board views render these exact frontmatter fields, so an invalid value silently miscodes the pathway/outcome/decision-owner charts the flagship report depends on.
   - `cases/terra.md`: `pathway: museum-dissolved` (not a `pathway` value) and `outcome: collapsed` (not an `outcome_category` value); `decision_owner: unknown` (not a valid H7A value — the vocab's gap value is `no-identifiable-person`). `report-dataset.md` #7 codes this same case `pathway: found-standalone-museum`, `outcome: closed-dispersed`, `decision: foundation-executive`. **Fix:** correct all three fields.
   - `cases/di-rosa.md`: `pathway: museum+park` (invalid; should be `found-art-park`) and `decision_owner: unknown` (invalid; `report-dataset.md` #9 codes `decision foundation-executive`). **Fix:** correct both.
   - `cases/mcnay.md`: `pathway: house-to-museum` (invalid; should be `found-house-museum`), `verification: in-progress` (not a template value; should be `provisional` per the worked example in `case-template.md`), and `decision_owner: founder-self` (invalid; the template's own McNay worked example codes `decision_owner: collector-alone`). **Fix:** correct all three.
   - `cases/souls-grown-deep.md`: `decision_owner: unknown` (invalid; `report-dataset.md` #1 codes `decision foundation-executive`). **Fix:** correct.
   - **New this run:** `cases/neue-galerie.md`'s `verification` field was fixed since the last audit (now `spot-verified`, matching `report-dataset.md`), but `decision_owner: founder-self` was not caught last time and is the same invalid value flagged in `mcnay.md` — `report-dataset.md` #3 codes this case `decision collector-alone`. **Fix:** correct.
   The correct values already exist in `report-dataset.md` / `case-template.md` for all five cases; this remains a one-time sync pass, not new research. Recommend prioritizing this before the 50-case set locks and any chart is drawn from it.

2. **`marketing/flagship-report.md`'s case-count is more stale than at the last audit, not less.** It still reads "~30 of 50 cases coded" (line 60), unchanged since 2026-08-14, while `report-dataset.md` — the authoritative live count — has moved from 36 to **44 of 50** in the same window (three coding batches: Kreeger/Michener/Lehman, Enron/Deutsche Bank/Benini/Yuz, Beyeler/Vogel/De la Cruz/JPMorgan). The gap has grown from 6 cases to 14. Standard: single source of truth (QA remit e) — a working page should point to the canonical count rather than restate a number that visibly keeps drifting; `HOME.md` already does this correctly (states "44 of 50," matching `report-dataset.md`, each time it's updated). **Fix:** replace the hardcoded figure with a link to `[[report-dataset]]`, or update it and note it will need refreshing each batch — the former is more durable given how often the source moves.

3. **The primary-verification backlog keeps growing, and the fix recommended at the last audit still hasn't been tried.** `report-dataset.md`'s own accounting shows the backlog now at 15 of 44 coded cases (≈34%), up from 7 of 36 (≈19%) at the last audit. This is the fifth consecutive research run (2026-08-13 through 2026-08-15, three runs today) to hit `EGRESS_BLOCKED` on every domain tried, including a non-aggregator third-party PDF host tested specifically to route around the block. This QA session independently hit the identical `EGRESS_BLOCKED` result fetching `alinaokun.com`, confirming the block is still session/environment-wide, not domain-specific. Standard: QA remit (a), "the primary-verification backlog is honored, not growing unbounded." The 2026-08-14 report recommended pursuing the already-identified alternative (IRS bulk 990 XML index, noted in `report-dataset.md` itself) instead of continuing to retry WebFetch; the retries have continued every run since, and the alternative has not been attempted. **Recommendation:** stop retrying WebFetch as the mitigation and actually start the IRS bulk-XML pass, even a manual one-case test, before coding further cases into the backlog.

4. **The alinaokun.com public-copy voice check flagged at the last audit is still unresolved, in either direction.** `marketing/website.md`'s "finalized copy, 2026-08-13" block for the Projects and Writing sections still contains em dashes ("Nariway — Independent work on...", "The Brief Experiment — A history of...", four instances total, lines 48 and 55–57), which fails the `voice.md`/`ai-tells.md` em-dash ban for public-facing copy (QA remit d). The subsequent "LIVE revised, confirmed 2026-08-14" note explicitly says the punctuation on the actual live page was never checked ("Could not verify exact About-text punctuation from a paraphrase, worth a quick self-check"). This QA session tried to spot-check the live page directly and hit the same `EGRESS_BLOCKED` result as finding 3, so it remains unverified whether the live site is clean or not. **Fix:** either confirm (screenshot or copy-paste from the live CMS) that the actual published text differs from this draft and is clean, or rewrite the vault draft without em dashes and push that text live — the open question shouldn't carry into a third audit cycle.

---

## MINOR

5. **`flagship-report.md` paraphrases the claims-register's transfer figure instead of linking it.** Line 6 and line 20 both say "the ~$1T wave" / "the ~$1T" where `claims-register.md` C1's canonical figure is **$992B**, sourced and captioned "do NOT... paraphrase." $992B rounds defensibly to "~$1T," so this isn't a contradiction, but it's exactly the paraphrase pattern the register exists to prevent. **Fix:** cite the precise $992B or link `[[claims-register]] C1` instead of restating a rounded version.

6. **Field-name mismatch between template and case files persists.** `case-template.md` specifies `verification_status` with capitalized values; every case file still uses a lowercase `verification:` field with lowercase values. Harmless (applied consistently across all ~30 case files checked), flagged at the last audit too, not re-flagged as urgent — worth a single normalization pass whenever the vocabulary sync (finding 1) is done, since the same files are already being touched.

---

**Counts:** 0 critical / 4 should-fix / 2 minor.
