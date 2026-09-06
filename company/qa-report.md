# QA Report — 2026-09-06 (post commit 2d0c0a9, 49th research run)

**Verdict:** Not clean. All 7 CRITICAL items from the 2026-09-05 audit (`be452f0`) remain open, unfixed in every case checked; two grew wider with content added since (a new em-dash instance in a freshly-coded case's public field, and two new colon-in-prose violations in the manuscript's newest paragraph). One prior SHOULD-FIX item (the duplicated backlog numbering) appears to have been resolved. One genuine new structural gap surfaced this run, present in most of today's new case files: `constraints_documented` values outside the field's own controlled vocabulary.

---

## CRITICAL

### 1. CARRIED, now unresolved across at least five consecutive audits — the "professional-services pivot" contradicts the entire body of work this vault produces daily.
`INDEX.md:3` and `archive/README.md:10-14` both still state Nariway pivoted away from the research/advisory/collector model to "a specialist professional-services firm for estate attorneys and fiduciaries," naming three archived documents as the current source of truth. Meanwhile every research run since, including today's (49th), continues to build exactly the model `archive/README.md` says was retired: `company/positioning.md`, `research/claims-register.md` (94 entries), `cases/report-dataset.md` (166 coded cases), and the manuscript. Unchanged since the last five audits.
**Standard violated:** `[[positioning]]`'s single-source rule; QA remit (e) and (f).
**Fix:** needs Alina's decision, not an editorial one — confirm whether the pivot stands or was abandoned, make `INDEX.md`/`archive/README.md` agree with the model actually being executed, and log the resolution in `company/decisions/`.

### 2. CARRIED — `export/nariway-public.json:8710` still blends three non-comparable wealth-transfer figures into one number.
Still reads `"value": "~$31T+"`, `"source": "wealth-research (Cerulli / UBS / Knight Frank)"` — the exact mixing `claims-register.md` C36 exists to forbid (Deloitte/ArtTactic's ~$31T decade/global figure, Cerulli's $124T US-only/2048 figure, and Knight Frank, which publishes no transfer total at all, attributed as one source to one number).
**Fix:** replace with the Deloitte/ArtTactic-only $31T figure (C1's input); drop Knight Frank from the source line regardless.

### 3. CARRIED and WIDER — em dashes in live `public_*` export fields, now 14+ files, one new today.
Unfixed, verbatim, in the same 13 files flagged in the prior two audits: `cases/art-car-museum.md`, `cases/fresno-metropolitan-museum.md`, `cases/hsbc-art-collection.md`, `cases/lee-kun-hee-collection.md`, `cases/malba-costantini.md`, `cases/monte-dei-paschi-collection.md`, `cases/mowaa.md`, `cases/sakip-sabanci-museum.md`, `cases/schnitzer-family-foundation.md`, `cases/standard-bank-art-collection.md`, `cases/unicredit-art-collection.md`, `cases/yemisi-shyllon-museum-of-art.md`. **New this run:** `cases/instituto-moreira-salles.md:29` — `public_focus: Brazilian cultural heritage — photography, literature, iconography, music, and contemporary art`. The five other new/backfilled cases this run (Gardner, Muzeum Susch, TD Bank, Brant, Hill, Judd, Soloviev) are clean on this specific check.
**Standard violated:** `[[voice]]`/`[[ai-tells]]`, no em dashes, applied to public-facing copy per QA remit (d).
**Fix:** fix all instances in one pass and regenerate the export. A pre-commit grep for em dashes in `public_*` lines would stop the recurring one-new-instance-per-run pattern — this is the third consecutive run to add one on top of an unfixed backlog.

### 4. CARRIED — `cases/kenneth-c-griffin-collection.md` still states a chain of dollar figures as fact with zero sourcing.
Still zero `[source:`/`confidence:` tags in the file (the "Confirmed holdings" list: de Kooning $300M, Pollock $200M, Johns $80M, Basquiat >$100M, Cézanne ~$60M, Richter $46M, the Constitution $43.2M, the Stegosaurus $44.6M), despite `verification: spot-verified`. This run gave the file its first numbered dataset row (`report-dataset.md` #162, backfilled as part of the integrity fix), which makes the unsourced figures more, not less, visible — they're now part of the counted, "coded" corpus.
**Fix:** add `[source: URL; confidence: tier]` to each figure, or downgrade `verification` until it's done.

### 5. CARRIED — "significant" as a prestige adjective for collections is still live in `company/positioning.md`, including its own approved example.
Unchanged at lines 8, 13, 34, 112, and 138 (the codified ✅ example itself).
**Standard violated:** `[[voice]]`'s explicit, non-negotiable craft standard; QA remit (d).
**Fix:** replace with "private art collections" / "collectors" at the live-copy instances and the approved example, then propagate downstream.

### 6. CARRIED and WIDER — the manuscript (`marketing/what-becomes-of-great-art-collections.md`) still carries the em-dash violation flagged in the last two audits, plus two new colon-in-prose violations in today's newest paragraph.
Line 99's em dash (`— see this section's own closing paragraph...`) is unchanged from the last audit (only the case count inside the sentence changed, 155→166). **New this run**, in the Gardner-counter-case paragraph added today (line 127): *"The difference is not scope, this constraint is at least as broad as Barnes's, but enforceability: Gardner's clause names a real, motivated third-party beneficiary..."* — a colon used mid-sentence to introduce an elaborating clause, twice in the same paragraph (also *"...arguably as broad as Barnes's own: no future change to the collection's arrangement..."*). This is the first time an audit has flagged colon-in-prose specifically (the last two audits checked only em dashes here); a spot check of the surrounding sections found this construction recurring well beyond today's addition, suggesting it is a pre-existing, widespread pattern in the manuscript's findings paragraphs, not a one-off. Given the scale, this note is conservative: it names the standard and today's concrete new instances rather than claiming an exhaustive count.
**Standard violated:** `[[voice]]` line 27 ("No colons in prose. Permitted only before dialogue") and `[[ai-tells]]`, both of which explicitly cover "the report."
**Fix:** rewrite the flagged sentences with commas/restructuring; no content change needed. Separately, Toi should decide whether to schedule a dedicated colon-removal pass across the manuscript's existing findings paragraphs, since this run's spot check suggests the issue is larger than the two new instances.

### 7. CARRIED — the LACMA construction-cost contradiction (C38 vs. an unregistered second figure) is still live and unreconciled.
`research/claims-register.md` C38 (unchanged): David Geffen Galleries "opened April 2026," cost "~$724M total." `research/market-intelligence.md:233` (unchanged): "LACMA's ongoing building project has grown from an initial ~$600M estimate to over $750M... with 2026 completion still the target." One says the building already opened at a fixed cost; the other describes an ongoing project targeting 2026 completion. Not touched by this run's tax-and-legal-focused research pass.
**Standard violated:** `claims-register.md`'s single-source/no-drift discipline; QA remit (c).
**Fix:** determine whether this is the same Geffen Galleries project (drop the stale $600-750M framing) or a distinct project (give it its own claims-register entry, clearly distinguished from C38).

---

## SHOULD-FIX

### 8. NEW — `constraints_documented` values fall outside the field's own controlled vocabulary in 23 of 154 coded case files, including 3 of this run's own 6 new/backfilled cases.
`case-template.md:23` defines exactly four permitted values: `yes` · `no` · `partial` · `open`. Across the corpus, 14 files use `n/a` and 9 use `unknown` instead — neither is on the list. This run's own new cases split the same way: `instituto-moreira-salles.md`, `kunsthalle-praha.md`, and `muzeum-susch.md` all code `unknown` (no founding instrument located, could still exist); `td-bank-art-collection.md` and `wesfarmers-art-collection.md` code `n/a` (no individual founder, so no personal constraint is possible). Both uses are internally consistent and semantically distinct from the four permitted values and from each other (a genuine "no constraining instrument exists to look for" is not the same claim as "an instrument may exist but wasn't found," which is not the same as `open`'s specific "living founder, undecided" meaning) — this reads as several independent contributors converging on the same missing values because the template's list is incomplete, not as carelessness.
**Standard violated:** `case-template.md`'s closed-vocabulary rule ("a value outside a list is not permitted without amending this template").
**Fix:** amend `case-template.md` to formally add `n/a` (no founder to impose a constraint) and `unknown` (instrument not located this run) to the `constraints_documented` vocabulary, or map existing `n/a`/`unknown` rows to one of the four existing values if a narrower reading is intended.

### 9. CARRIED — the Fisher/SFMOMA LinkedIn post still collapses the 720+ vs. ~1,100-works distinction.
`marketing/linkedin-posts.md:47-51` unchanged: "more than a thousand works" leads directly into the SFMOMA 100-year-loan sentence, reading as if the whole collection was loaned. `claims-register.md` C53 and `cases/fisher-sfmoma.md` both specify only 720+ of ~1,100 works are the SFMOMA-loaned subset.
**Fix:** state the 720+ figure or drop "more than a thousand" from the lead-in before this post is scheduled.

### 10. CARRIED — `marketing/website.md` still carries the same three undocumented divergences from `positioning.md`.
Unchanged: the file's own "reconcile later" note is still unresolved with no owner or date; the live bio still differs in wording from the canonical Bio with neither marked authoritative; the alinaokun.com "Current" section phrasing still isn't reflected in or flagged against `positioning.md`.
**Fix:** reconcile or explicitly mark each variant as deliberate, the way `linkedin.md`/`substack.md` already do.

### 11. CARRIED — `cases/cultural-museum-of-african-art.md` still states an unsourced superlative as fact.
`public_origin` still reads "one of the largest private African art collections in the US" with no source or attribution for the ranking claim.
**Fix:** attribute it ("press coverage described it as...") or drop "one of the largest."

---

## MINOR

### 12. CARRIED, grown again — the `origin` frontmatter field now spans 7 raw values, still drifting.
Current tally: `private-individual` (46, up from 42) · `corporate` (21, up from 19) · `private` (14) · `private individual` (6) · `individual` (5) · `artist` (5) · `institutional` (3).
**Fix:** consolidate the private-side spelling variants; document `artist` and decide on `institutional` in `case-template.md`.

### 13. CARRIED — corporate-continuity vocabulary still fragmented.
Five files use `parent-entity-continuity`; `enron-art-collection.md` and `lehman-brothers-collection.md` use `parent-entity-survival` for the same concept.
**Fix:** adopt one term, add it to `case-template.md`.

### 14. CARRIED — `primary_friction` schema gap, still self-flagged in the same three files (`benini.md`, `rauschenberg-foundation-hq.md`, `unicredit-art-collection.md`) for the missing "voluntary reallocation/succession-driven reversal from a position of strength" value.
**Fix:** add the missing authorized value to `case-template.md`.

### 15. CARRIED — `company/decisions/2026-08-14-board-membership.md` is still marked open.
Outcome line still reads `_open — shortlist being researched into [[board-opportunities]]._`
**Fix:** move out of `decisions/` until resolved, or mark plainly as in-progress.

### 16. CARRIED, wider — `research/estate-transition-synthesis.md` still cites a stale case count, now further off.
Line 14 still states "141 significant collection transitions," now 25 cases stale against the current 166. Still explicitly internal/not-for-publication and not used for any rate calculation, so still not a standards violation, just a live inconsistency.
**Fix:** update on next touch of the file; no urgency.

---

## Checked, no issue found
- **This run's six new/backfilled cases**, aside from items 3, 4, and 8 above: every other quantitative and governance field carries a source and confidence tag or an explicit `unknown`; no field tagged `primary`/spot-verified beyond what its source supports (Gardner's `net_assets_latest` is correctly held `unknown` rather than upgraded from the low-confidence secondary snippet on file); `net_assets_to_opex_ratio` correctly left uncomputed where no dedicated 990 exists (Muzeum Susch, Kunsthalle Praha — Swiss/no US-990-equivalent regime, honestly named as structural, not a tooling gap).
- **New claims-register entries C93 and C94** (LA wildfires stress test; EU Cultural Goods Import Regulation): both sourced with confidence tags, explicit "do NOT say" scope limits, and correctly distinguished from adjacent entries (C94 from C45/C65/C78's tax-settlement comparators; C93 explicitly declines to attribute the $20-30B all-property wildfire loss figure to art specifically).
- **The manuscript's new findings paragraphs** (Gardner counter-case, Muzeum Susch, TD Bank, EU import regulation): correctly hedged, cite existing claims-register entries rather than restating numbers, and explicitly caveat what is not yet confirmed (e.g. the Gardner paragraph's own admission that this is one case, not a rate).
- **`report-dataset.md`'s primary-verification backlog numbering**: re-checked in full — no duplicate item numbers found. **Appears resolved** since the last audit (see Resolved section below).
- **Dataset-integrity backfill** (Brant, Hill, Judd, Griffin, Soloviev given numbered rows 159-163): transparently logged as a stale-header correction, not silently folded in; case count (166) matches the manuscript and the header's own recount math.

---

## Resolved since the 2026-09-05 audit
- **Prior SHOULD-FIX item 8** (`report-dataset.md`'s primary-verification backlog reusing item numbers 61-67 across two lists): a full recount of the numbered backlog list (currently 1-86) found no duplicates. Marking resolved; will re-check next run in case this was a transient state rather than a deliberate fix.

All 7 prior CRITICAL items remain open (two wider). Three of four prior SHOULD-FIX items remain open unchanged.

---

**Counts:** 7 critical (7 carried, 0 new) / 4 should-fix (3 carried, 1 new) / 5 minor (5 carried, 0 new).
