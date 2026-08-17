# QA Report — 2026-08-17

**Verdict:** Not clean. 2 critical findings — the dataset's central governance-survival number loses its "not a population rate" caveat once it leaves `report-dataset.md`, and two live, published Substack pages break the mechanical staccato/fragment-stack rule in `voice.md`. Plus 4 should-fix and 3 minor, several of them aging repeat findings (frontmatter drift, an em-dash violation, a drifted bio fact) now unresolved for a third or fourth consecutive audit despite being named explicitly each time.

---

## CRITICAL

1. **The 88%/77% governance-survival figure loses its "hand-selected, not a population rate" caveat outside `report-dataset.md`.**
   `cases/report-dataset.md:85` (Pattern 14) is properly hedged: "not a population rate — the sample is deliberately picked for pathway/outcome variance, not randomly drawn, and n=26 is small." But the same number is restated flat, with no caveat, in three places that are about to reach Alina or already frame it as settled:
   - `research/learnings-log.md:7` — "The report's central claim finally has a real number behind it: 13 of 13 non-founder-sole institutions survived their founder, versus 10 of 13 founder-sole ones (77%)."
   - `HOME.md:52` — same figures, same framing, no caveat.
   - `.mail/outbox/checkin.json` (today's queued check-in email, unsent) — repeats the exact learnings-log sentence verbatim under "Today I learned," which is what Alina will read.
   Standard violated: `company/quality-assurance.md` item 2 / this audit's remit (b) — "No rates or percentages published off the hand-selected case set." **Fix:** add one clause to the learnings-log entry, HOME.md, and the check-in draft before it sends — e.g. "(n=26, hand-selected for variation, not a population rate)" — so the caveat travels with the number everywhere it's repeated, per `claims-register.md`'s own convention.

2. **Live, published Substack copy in `company/positioning.md` breaks `voice.md`'s staccato and fragment-stack rules.** Both blocks are explicitly marked LIVE ("mirror of the live page… do not edit for style without changing Substack too"), so these are published, not draft:
   - Substack About page: "Some collections stay in families for generations. Some become museums or foundations. Some are given or lent to existing institutions. Some travel. Some are divided or sold. Some disappear from public view." — six short parallel sentences in a row, against `voice.md`'s explicit "No staccato sequences. Never three or more short sentences in a row."
   - Substack Welcome page: "Does it stay in the family? Become a museum or foundation? Go to an existing institution? Travel? Get divided or sold?" — only the first is a complete sentence; the next four are subject-less fragments, matching `ai-tells.md` tell #2 ("Two short bits stuck together… pick one") stacked five deep.
   Standard violated: `voice.md` craft standards (explicitly "mechanical and non-negotiable") and `ai-tells.md`. **Fix:** vary sentence shape or collapse each list into one or two fuller sentences in both `positioning.md` and the live Substack page, keeping them as a matched pair.

---

## SHOULD-FIX

3. **`cases/mcnay.md` still carries three invalid controlled-vocabulary values, unresolved for a fourth consecutive audit** — `pathway: house-to-museum` (not in the vocab; should be `found-house-museum`, per `case-template.md`'s own worked example for this exact case), `verification: in-progress` (not a valid `verification_status`; should be `provisional`), `decision_owner: founder-self` (not in the vocab; should be `collector-alone`). This file was named explicitly in the 2026-08-16 QA report and again implied by the 2026-08-17 hygiene commit `7021fa9` ("sync 5 case files… drift open 3+ audits"), but that commit's diff shows it touched `di-rosa.md`, `neue-galerie.md`, `pearlman-foundation.md`, `souls-grown-deep.md`, and `terra.md` — not `mcnay.md`. **Fix:** apply the same sync to `mcnay.md`; the correct values are already documented in the file's own template worked example.

4. **`cases/neue-galerie.md`'s `decision_owner: founder-self` remains invalid after last run's partial fix.** Commit `7021fa9` corrected this file's `pathway` and `outcome` fields but left `decision_owner: founder-self` untouched; `report-dataset.md` #3 already codes this case `collector-alone`. **Fix:** one-line frontmatter edit, value already known.

5. **`cases/moma.md` introduces two new values outside the controlled vocabulary: `collection_coherence: absorbed` and `decision_owner: collective-founders-trustees`.** Neither is in `case-template.md`'s lists, and `case-template.md` states "a value outside a list is not permitted without amending this template." Both describe real patterns the vocabulary doesn't yet have a slot for (a multi-founder decision structure; a collection absorbed into a much larger whole rather than kept coherent) — this is a schema gap, not a coding error, but it risks silently breaking any `Cases.base` view grouped on these fields until resolved. **Fix:** either amend `case-template.md` to add these values (they're likely to recur — MoMA-style multi-founder, absorbed-collection cases aren't unique in the set) or remap to the nearest existing value with a flagged caveat.

6. **`verification: spot-verified` is applied uniformly to all ~21 cases in the Primary-verification backlog, where every quantitative field is tagged `secondary`/"WebSearch-surfaced, not directly fetched."** Confirmed directly in `rubin-museum.md`, `moma.md`, `cam-raleigh.md`, `rauschenberg-foundation-hq.md`, `pearlman-foundation.md`, `kreeger-museum.md`, and `credit-suisse-ubs-collection.md` — same pattern across the full backlog. `case-template.md` never defines what distinguishes `Spot-verified` from `Provisional`, so this may be an intentional convention rather than a slip, and no individual figure overstates its own confidence (each is honestly tagged `secondary` inline, and `case-template.md` explicitly allows charts to run on `secondary`-tagged cells). But as written, "Spot-verified" and "Provisional" currently carry no practical distinction for these files, which sits close to `company/quality-assurance.md`'s structural-integrity rule that "nothing is marked verified that is only secondary-sourced." **Fix:** add a one-line definition of `Spot-verified` to `case-template.md` (e.g. "narrative facts cross-checked across ≥2 independent secondary sources, no direct primary fetch") so the tier means something specific, or downgrade WebSearch-only cases to `Provisional` until a primary source is pulled.

---

## MINOR

7. **`marketing/website.md` still carries independently-drifted bio copy instead of pointing to `positioning.md`, unresolved for a fourth consecutive audit** — "visited more than 100 museums" (website.md) vs. "visited hundreds of museums" (positioning.md, canonical). This is already surfaced directly to Alina in today's queued check-in email as a one-line decision she needs to make, so no new escalation is needed here — noting only that the underlying file still lacks the "edit only in positioning.md" pointer that `linkedin.md` and `substack.md` already carry, so the fix should include that pointer once the number is settled, not just the number.

8. **`marketing/website.md` still has em dashes in its "finalized copy" blocks, unresolved for a fourth consecutive audit** (lines 48–49, 55–57: "Nariway — Independent work on…", "The Brief Experiment — A history of…", etc.), against `voice.md`'s em-dash ban. The file's own note says the live page's actual punctuation was never independently verified against this draft.

9. **`research/research-program.md`** restates the $992B/5%/$19.84T breakdown (line 38) and the 72%/90%/80% retention figures (line 78) inline rather than linking to `[[claims-register]]` C1/C3/C12 — no drift found (the numbers still match), but this predates the register's "link, don't paraphrase" convention and is a standing drift risk.

---

## Resolved since the last audit (noted, no action needed)
- `marketing/flagship-report.md`'s stale "~30 of 50" case count and "~$1T" paraphrase (both flagged 2026-08-16) no longer appear — the file was restructured and the report's live content moved to `marketing/what-becomes-of-great-art-collections.md`.
- All four Notes in `marketing/substack-notes-queue.md` now end on a concrete fact or image (fixed 2026-08-17, per the file's own note), resolving last audit's finding #6.
- `company/decisions/` has no stale entries — the one "open" decision (board membership) is genuinely still open, consistent with the active shortlist in `marketing/board-opportunities.md`.

---

**Counts:** 2 critical / 4 should-fix / 3 minor.
