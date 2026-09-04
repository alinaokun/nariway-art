# QA Report — 2026-09-04 (second run today, post commit 34e4693)

**Verdict:** Not clean. All 12 items from this morning's audit (commit `50085ef`) are still open, unchanged in substance — nothing was fixed between that run and this one. Two of those items grew in scope because new content landed in between (three new cases in `7f53b15`, one human edit in `34e4693`). This run also found two new CRITICAL items in that same new content: a live voice violation in the manuscript's public-facing prose, and an unreconciled contradiction between a new LACMA cost/status claim and the vault's own existing canonical figure (C38). The good news: the new cases' *coded* data (sourcing, confidence tags, controlled vocabulary) is clean, and `research/estate-transition-synthesis.md`'s human-authored tightening pass did exactly what its commit message claimed, with no new over-claims introduced.

---

## CRITICAL

### 1. CARRIED (unchanged) — the positioning single-source-of-truth conflict is still unresolved and self-contradictory.
`INDEX.md:3`'s migration banner (dated 2026-08-27) still names three archived documents as "the current source of truth." `archive/README.md` still lists the same three files under its own "current source of truth" heading, two paragraphs below its own disclaimer that archived files "do NOT describe how Nariway works today." `marketing/linkedin-posts.md:3` still cites the archived `Nariway_Company_Positioning_and_Operating_Brief_Aug_30_2026.md` instead of `[[positioning]]`. `company/decisions/` still holds the same five files, none recording this move as a settled reversal.
**Standard violated:** `[[positioning]]`'s single-source rule; QA remit (e), (f).
**Fix:** unchanged from this morning — confirm with Alina whether the pivot is reversed; if so, repoint `INDEX.md`, `archive/README.md`, and `marketing/linkedin-posts.md:3` to `[[positioning]]` and log the reversal in `company/decisions/`.

### 2. CARRIED (unchanged) — `export/nariway-public.json:8426` and `content/content.json:54` still blend three non-comparable wealth-transfer sources into one figure.
Both files still read `"value": "~$31T+"`, `"source": "wealth-research (Cerulli / UBS / Knight Frank)"`, the exact mixing `claims-register.md` C36 exists to prevent (Deloitte/ArtTactic ~$31T decade/global ≠ Cerulli $124T US-only/2048 ≠ Knight Frank, which publishes no transfer total at all).
**Fix:** unchanged — replace with the Deloitte/ArtTactic-only $31T figure (C1's input) or the already-drafted GWT figures in `marketing/gwt-content-draft.md`.

### 3. CARRIED, and wider than last measured — the em-dash fix in live `public_*` export fields still hasn't happened, and this run found it in three more files the prior audit's spot check missed.
All 12 previously-flagged em dashes remain, verbatim, unfixed (`cases/lee-kun-hee-collection.md`, `cases/unicredit-art-collection.md`, `cases/hsbc-art-collection.md`, `cases/malba-costantini.md`, `cases/monte-dei-paschi-collection.md` ×3, `cases/schnitzer-family-foundation.md`, `cases/standard-bank-art-collection.md`, `cases/yemisi-shyllon-museum-of-art.md`). This run additionally found the same defect in three files never checked before:
- `cases/art-car-museum.md:29` (new today, commit `7f53b15`): `public_focus: "Art cars" — vehicles transformed into artworks — and the broader Houston Art Car movement...` — two em dashes.
- `cases/mowaa.md:28,32` (added 2026-09-03, commit `df498c7`, predates this morning's audit — a miss, not a new regression): `public_size` and `public_origin` each carry one em dash.
- `cases/sakip-sabanci-museum.md:34` (same commit `df498c7`, same-day miss): one em dash in `public_origin`.
`cases/zabludowicz-collection.md` and `cases/cultural-museum-of-african-art.md` (also new today) are clean, so the defect is not universal in new coding, just not being caught consistently.
**Standard violated:** `[[voice]]`/`[[ai-tells]]`, no em dashes, applied to public-facing copy per QA remit (d).
**Fix:** fix all 15 now-identified instances in one pass and regenerate the export; consider a pre-commit grep for em dashes in `public_*` fields so this stops recurring case by case.

### 4. CARRIED (unchanged) — `cases/kenneth-c-griffin-collection.md` still states a chain of dollar figures as fact with zero sourcing.
Still zero `[source:`/`confidence:` tags anywhere in the file; the "Confirmed holdings" list (de Kooning $300M, Pollock $200M, Johns $80M, Basquiat >$100M, Cézanne ~$60M, Richter $46M, the Constitution $43.2M, the Stegosaurus $44.6M) remains untagged despite `verification: spot-verified` in frontmatter, unlike every comparable case file in the corpus.
**Fix:** unchanged — add `[source: URL; confidence: tier]` to each figure.

### 5. CARRIED (unchanged, and wider than previously flagged) — "significant" as a prestige adjective for collections is still live in `company/positioning.md` itself, including its own approved example.
Confirmed unchanged at lines 34 (live Contact copy), 112 (live LinkedIn bio), and 138 (✅ approved example, meaning the violation is codified as correct usage). Also present, not previously flagged, at line 8 (the live vision paragraph: "a **significant** collection reaches the question of what becomes of it") and line 13 (internal framing, lower priority but same word).
**Standard violated:** `[[voice]]`'s explicit, "non-negotiable" craft standard; QA remit (d).
**Fix:** replace "significant" with "private art collections" / "private collections" at all four live-copy instances (lines 8, 34, 112, 138) and propagate to nariway.com and LinkedIn.

### 6. NEW — the manuscript itself (`marketing/what-becomes-of-great-art-collections.md`) carries multiple fresh em-dash and mid-sentence-colon violations, added today, inside the live reading draft (not the working-notes section below the changelog line).
From the diff added in commit `7f53b15` (§3, the Corcoran/PMA/AAM section):
- *"...gave up a dedicated public building — a Himalayan-art museum, a contemporary-art center selling its warehouse, an artist foundation divesting its headquarters, a bank's Berlin exhibition space — carried some real funding or lease pressure..."* (two em dashes)
- *"A different, smaller-scale, and previously uncoded shape: nearly five decades spent quietly acquiring..."* (mid-sentence colon)
- *"...had neither: no dedicated foundation, no written succession instructions..."* (mid-sentence colon)
- *"Its collection did not vanish, though: the founders' children funded a new, dedicated home..."* (mid-sentence colon)
- *"...shows the deficit widening, not narrowing, in the turnaround's first year: roughly $10M on a $76.5M FY2026 budget, on top of $5.4M the year before (C89) — not a verdict..."* (colon + em dash)
- *"...puts a figure on what is driving the deficits above: labor costs up 20%... alongside the funding-cut figures already on file — 34% of respondents lost a federal grant..."* (colon + em dash)
**Standard violated:** `[[voice]]`/`[[ai-tells]]` — no em dashes, no colons in prose (only before dialogue); this document is explicitly in scope (marketing copy, public-facing reading material).
**Fix:** rewrite each flagged sentence with commas, periods, or restructuring; no content change needed, only punctuation.

### 7. NEW — an unreconciled contradiction between a new LACMA capital-cost claim and the vault's own existing canonical figure, C38, both now live in the manuscript and `market-intelligence.md`.
`research/claims-register.md` C38 (unchanged, existing entry): LACMA's David Geffen Galleries **"opened April 2026"**, cost **"~$724M total."** New text added today in `research/market-intelligence.md:226` and folded into the manuscript (`marketing/what-becomes-of-great-art-collections.md:486`) states: *"one major West Coast museum's building project has grown from an initial ~$600M budget to over $750M... with 2026 completion still the target but further delay 'remain[ing] possible.'"* The manuscript doesn't name the museum, but `market-intelligence.md`'s fuller version does: LACMA. One canonical entry says LACMA's flagship gallery already opened at $724M; the new, unregistered figure says a LACMA project is still under construction, targeting 2026, at $600M-$750M+. These describe either the same project inconsistently or two different LACMA projects conflated as one without saying so — either way it is exactly the drift `claims-register.md` exists to prevent, and it is now published in the live manuscript, not just internal research notes.
**Standard violated:** `research/claims-register.md`'s single-source/no-drift discipline; QA remit (c).
**Fix:** determine whether this is the same Geffen Galleries project (in which case the $600M→$750M+/still-under-construction framing is stale or wrong and should be dropped) or a distinct LACMA capital project (in which case it needs its own claims-register entry, clearly distinguished from C38, before it stays in the manuscript).

---

## SHOULD-FIX

### 8. CARRIED, wider than before — `cases/report-dataset.md`'s primary-verification backlog numbering collision has grown from 3 to 7 duplicate numbers.
The "recent batches" list (Batches 43-45, added since the last audit) reuses `61`-`67` a second time against an older backlog list that already used those same numbers for `wolfsonian-fiu`, `pier24-photography`, `hall-art-foundation`, `wolf-kahn-foundation`, `petrucci-family-foundation`, `paz-museum-brumadinho`, and `museum-of-russian-icons`. The running-count prose was last updated at Batch 43 and was never touched for Batches 44 or 45, so it is now stale on top of already being wrong.
**Fix:** renumber the backlog list sequentially in one pass and reconcile the prose count against the corrected total; consider deriving the count programmatically rather than hand-tracking it, since it keeps drifting batch to batch.

### 9. CARRIED (unchanged) — the Fisher/SFMOMA LinkedIn post still collapses the 720+ vs ~1,100-works distinction.
`marketing/linkedin-posts.md:47-51` is byte-identical to what the last audit quoted: "more than a thousand works" leads directly into the SFMOMA 100-year loan sentence, reading as if the whole collection was loaned. `claims-register.md` C53 and `cases/fisher-sfmoma.md` both specify only 720+ of ~1,100 works are the SFMOMA-loaned subset.
**Fix:** unchanged — state the 720+ figure or drop "more than a thousand" from the lead-in sentence before this post is scheduled.

### 10. CARRIED (unchanged) — `marketing/website.md` still carries three undocumented divergences from `positioning.md`.
(a) The file's own note that live hero/section copy differs from `[[positioning]]` is still unresolved, no owner or date. (b) The reported live bio sentence still differs in wording from positioning.md's canonical Bio with neither marked authoritative. (c) The alinaokun.com "Current" section phrasing still doesn't appear in positioning.md and isn't flagged as a deliberate variant.
**Fix:** unchanged — reconcile or explicitly mark each variant as deliberate, the way `linkedin.md` and `substack.md` already do.

### 11. NEW — `cases/cultural-museum-of-african-art.md` states an unsourced superlative as fact.
The body's summary line calls it "one of the largest private African art collections in the US." The Gaps section sources the $10M valuation and object count, but nothing sources or attributes this ranking claim against comparable collections.
**Standard violated:** `[[voice]]`'s evidence-discipline principle ("do not upgrade a careful finding into a stronger claim"); adjacent to QA remit (b).
**Fix:** attribute it ("press coverage described it as...") or drop "one of the largest" if no source actually ranks it.

---

## MINOR

### 12. CARRIED, grown — the `origin` frontmatter field now spans 7 raw values, up from 5.
Prior tally: `private-individual` (36) · `corporate` (18) · `private` (14) · `individual` (5) · `artist` (4). Today's three new cases introduced two more spellings never seen before: `private individual` (space, not hyphen — used by all three new cases from commit `7f53b15`) and `institutional` (used by `mowaa.md`, added yesterday). Current: `private-individual` (38) · `corporate` (18) · `private` (14) · `individual` (5) · `artist` (4) · `private individual` (3) · `institutional` (1).
**Fix:** consolidate the private-side variants to one spelling and document all authorized values, including `artist` and a decision on `institutional`, in `case-template.md`.

### 13. CARRIED (unchanged) — corporate-continuity vocabulary still fragmented.
`bank-of-america-collection.md`, `credit-suisse-ubs-collection.md`, `deutsche-bank-collection.md`, `jpmorgan-chase-collection.md`, `ubs-art-collection.md` use `parent-entity-continuity`; `enron-art-collection.md` and `lehman-brothers-collection.md` use `parent-entity-survival` for the same concept.
**Fix:** unchanged — adopt one term, add it to `case-template.md`.

### 14. CARRIED (unchanged) — `primary_friction` schema gap, self-flagged in three files.
`cases/benini.md` (`unknown`, not an authorized value), `cases/rauschenberg-foundation-hq.md`, and `cases/unicredit-art-collection.md` still independently flag the same missing controlled-vocabulary value for "voluntary reallocation from a position of strength."
**Fix:** unchanged — recode `benini.md` or add the missing authorized value.

### 15. CARRIED (unchanged) — `company/decisions/2026-08-14-board-membership.md` is still marked open.
Outcome line still reads `_open — shortlist being researched into [[board-opportunities]]._`
**Fix:** unchanged — move out of `decisions/` until resolved, or mark plainly as in-progress.

### 16. NEW, minor — `research/estate-transition-synthesis.md` cites a stale case count, though the document is internal and the count isn't load-bearing.
Line 14 states "141 significant collection transitions," already stale relative to `report-dataset.md`'s count at the time this file was edited (144 the prior day, 148 as of a commit 17 minutes earlier the same day). This document is explicitly marked internal working draft, not for publication, and doesn't use the count for any rate calculation, so it is not a standards violation, only a live inconsistency worth a routine sync.
**Fix:** update the count on next touch of the file; no urgency.

---

## Checked, no issue found
- **New case sourcing** (`zabludowicz-collection.md`, `art-car-museum.md`, `cultural-museum-of-african-art.md`): every quantitative and governance field carries a source and confidence tag or an explicit `unknown`; no field is tagged `primary`/`primary-verified` on secondary-sourced facts; no `net_assets_to_opex_ratio` computed for any of the three, so no UPPER BOUND labeling issue arises; controlled-vocabulary fields all use authorized values from `case-template.md` (aside from the `origin` field drift noted in MINOR #12).
- **`report-dataset.md` diff (Batch 45):** explicitly retains "not conclusions... no rates published off it" framing; new rows cite sources and confidence consistently; the 145→148 header recount is transparently explained.
- **Claims-register additions C88/C89:** figures match `market-intelligence.md`'s corresponding addendum exactly, in wording and value, both correctly tagged `secondary`, with an explicit "do not conflate with C57" disambiguation.
- **`what-we-now-believe.md`'s new disconfirmation entry (Zabludowicz, 26th pass):** carefully hedged throughout ("a real, if modest, disconfirmation," "narrows rather than reverses"), with explicit *Unknowns* and *Next test* sections; correctly avoids generalizing beyond the single tested case.
- **`research/estate-transition-synthesis.md` (human edit, commit `34e4693`):** both requested claim-boundary fixes from the commit message are correctly applied (governance "predicts" → "recurs"; the "defaulted to sale" line fully removed, confirmed by direct grep). The new Part 3 model is consistently hedged as candidate/provisional throughout ("hypotheses, not answers," each candidate model paired with an explicit "Oversimplifies" line). This file is explicitly internal, so its own use of em dashes is not a voice violation.
- **`cases/candidate-universe.md` diff:** appropriately hedged as a pre-coding leads table, not subject to full coded-header sourcing discipline.

---

## Resolved since the 2026-09-04 morning audit
None. All 12 prior findings remain open, two (em-dash spread, origin-field drift) wider than before. Two new CRITICAL items surfaced in content added since that audit.

---

**Counts:** 7 critical (5 carried, 2 new) / 4 should-fix (3 carried, 1 new) / 5 minor (4 carried, 1 new).
