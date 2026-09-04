# QA Report — 2026-09-04

**Verdict:** Not clean. The three long-carried CRITICAL items are all still open in some form — one (the positioning single-source-of-truth conflict) changed shape this run when Alina archived the conflicting brief herself, but the vault's own pointers to it were not updated, so the contradiction persists rather than resolving. Two new CRITICAL items surface this run: an unsourced case file and a banned word live in canonical public copy. The dataset itself keeps growing cleanly (141 coded cases, up from 138; sourcing and hedging discipline on 17 of 18 new cases is sound; no drift found in any recurring canonical number checked against claims-register.md).

---

## CRITICAL

### 1. CARRIED, changed shape — the positioning single-source-of-truth conflict is not resolved, it is now self-contradictory.
In the most recent commit (`08caf7e`, authored by Alina, "vault backup: 2026-09-03 12:33:34"), all three documents from the August estate-consulting pivot — `Nariway_Business_Strategy_and_Operating_Plan_Aug_2026.md`, `Nariway_Company_Positioning_and_Operating_Brief_Aug_30_2026.md`, and `Nariway_Website_Strategy_and_Build_Brief_Aug_2026.md` — were moved into `archive/`, a pure rename with no content change. But nothing that points to them was updated to match:
- `INDEX.md:3`'s migration banner (still dated 2026-08-27) still names all three, by wikilink, as "the current source of truth."
- `archive/README.md` — the very folder these files now live in — separately lists the same three files as "the current source of truth," directly contradicting its own opening line two paragraphs above: "Everything in this `archive/` folder is retired... It does NOT describe how Nariway works today."
- `marketing/linkedin-posts.md:3` still cites `Nariway_Company_Positioning_and_Operating_Brief_Aug_30_2026.md` (now archived) as "the company positioning," instead of `[[positioning]]`.
- No file in `company/decisions/` (still five files, none related) records this move as a settled reversal, so there is no way to tell from the vault whether Alina meant to reverse the pivot or was simply tidying files.
Whatever the intent, right now the vault's own entry point (`INDEX.md`) and its own archive folder both instruct a reader to treat retired files as current, while `company/positioning.md` (unchanged, internally consistent, and the file this QA process is instructed to audit against) states the opposite research/advisory model.
**Standard violated:** `[[positioning]]`'s single-source rule; QA remit (e) single source of truth; (f) structural integrity.
**Fix:** this is Alina's call, not a mechanical one — confirm whether the pivot is reversed. If so, update `INDEX.md`'s banner and `archive/README.md`'s "current source of truth" list to point at `company/positioning.md` instead, repoint `marketing/linkedin-posts.md:3` to `[[positioning]]`, and log the reversal in `company/decisions/`. If not, explain why the operating-model documents were archived while the banners still cite them.

### 2. CARRIED (12th audit) — `export/nariway-public.json:8426` and `content/content.json:54` still misattribute the wealth-transfer figure to three non-comparable sources blended into one number, live on the public site.
Unchanged verbatim across twelve audits: both files still read `"value": "~$31T+"`, `"source": "wealth-research (Cerulli / UBS / Knight Frank)"`. `claims-register.md` C36 exists specifically to bar this: Deloitte/ArtTactic's ~$31T (C1's input, decade, global) is not Cerulli's $124T (US-only, through 2048, C8) or UBS's ~$83T (global, 20-25 years); Knight Frank publishes no wealth-transfer total at all (only UHNWI population counts, C34).
**Fix:** replace the tile with the already-drafted GWT figures in `marketing/gwt-content-draft.md`, or at minimum attribute `$31T` to Deloitte/ArtTactic alone.

### 3. CARRIED (5th audit), unchanged — the em-dash fix called for four times now was never made.
All 12 previously-flagged em dashes in live `public_*` export fields are still present, verbatim, unfixed:
- `cases/lee-kun-hee-collection.md` `public_pathway_timeline` and `public_origin` (×2)
- `cases/unicredit-art-collection.md` `public_location`
- `cases/hsbc-art-collection.md` `public_origin`
- `cases/malba-costantini.md` `public_name`
- `cases/monte-dei-paschi-collection.md` `public_name`, `public_pathway_timeline`, `public_origin`
- `cases/schnitzer-family-foundation.md` `public_origin`
- `cases/standard-bank-art-collection.md` `public_pathway_timeline`
- `cases/yemisi-shyllon-museum-of-art.md` `public_origin`
The one piece of good news: the defect did not spread further this run — the three newest cases (`gochman-family-collection.md`, `warehouse-wieland.md`, `museum-macan.md`) and `kenneth-c-griffin-collection.md` are all clean of em dashes in their public fields, so the standing fix instruction appears to be holding at the point of new coding even though the backlog itself has not been touched in five audits.
**Standard violated:** `[[voice]]` / `[[ai-tells]]`, no em dashes in prose, applied to public-facing copy per QA remit (d).
**Fix:** replace all 12 em dashes with commas or restructured sentences; regenerate the export.

### 4. NEW — `cases/kenneth-c-griffin-collection.md` states a chain of specific dollar figures as fact with zero inline sourcing, unlike every other case file checked.
The file contains zero instances of `[source:` or `confidence:` anywhere — unique among the 18 new/recently-touched case files reviewed this run. Its "Notes and cautions (verification)" section is explicitly labeled "**Confirmed holdings** (each price/year sourced)" and then lists de Kooning *Interchange* ($300M, 2015), Pollock *Number 17A* ($200M, 2015), Jasper Johns *False Start* ($80M, 2006), Basquiat *Boy and Dog in a Johnnypump* (>$100M, 2020), Cézanne (~$60M), Richter ($46M), a first-printing US Constitution ($43.2M), and a Stegosaurus fossil ($44.6M) — none carrying a source or confidence tag. Frontmatter claims `verification: spot-verified`, but no individual figure is tied to a specific source/confidence tier the way the rest of the corpus does it (contrast `cases/broad.md`, which tags every claim, including narrative color, with `[source: URL; confidence: tier]`, or the companion file `cases/griffin-leonardo-loan-met.md`, which does the same for the same collector's 2026 Leonardo loan).
**Standard violated:** `[[case-template]]`'s binding sourcing rule; QA remit (a) sourcing — "any bare number presented as fact with no source."
**Fix:** add `[source: URL; confidence: tier]` to each price/date claim in the Notes section, matching the pattern used elsewhere in the corpus (most of these figures are widely reported and should be easy to source quickly).

### 5. NEW — the banned prestige-adjective "significant" is live in canonical public copy, in `company/positioning.md` itself.
`company/voice.md` states explicitly: *"No prestige adjectives for collections. Do not use 'significant' or 'serious' as a default qualifier."* Yet `company/positioning.md` — the file this whole standard is meant to protect — uses it twice in blocks marked as live, canonical copy:
- Line 34, the live nariway.com Contact copy: *"Our advisory work is for collectors and families making long-term decisions about **significant** private art collections."*
- Line 112, the live LinkedIn bio: *"I founded Nariway to focus on those decisions, the future of **significant** private collections..."*
- Line 138 compounds it: the same phrase from line 34 is listed as a **✅ approved example** in positioning.md's own "language line" guidance, meaning the violation is currently codified as correct usage, not just an overlooked instance.
`marketing/website.md` and `marketing/linkedin.md` both correctly mirror positioning.md rather than keeping independent copy, so the defect propagates through the single-source-of-truth mechanism instead of being contained by it.
**Standard violated:** `[[voice]]` craft standard (explicit, mechanical, "non-negotiable" per voice.md's own closing line); QA remit (d) voice on public-facing copy.
**Fix:** in `positioning.md`, replace "significant private art collections" / "significant private collections" with "private art collections" / "private collections" in both live blocks and in the ✅ example at line 138, then propagate to the live nariway.com and LinkedIn pages.

---

## SHOULD-FIX

### 6. `cases/report-dataset.md`'s primary-verification backlog has duplicate item numbers and an unreconciled running count.
The numbered backlog list assigns `61. gochman-family-collection`, `62. warehouse-wieland`, `63. museum-macan` (Batch 43, 2026-09-03) — but those same numbers (`61. wolfsonian-fiu`, `62. pier24-photography`, `63. hall-art-foundation`) were already used by an earlier batch. As a result the file's own prose is internally inconsistent: one passage states the backlog at "79 numbered items," while the note for the newest batch says it "grows from 60 to 63 items." Each new case is still individually logged with a specific re-fetch target (the backlog is not being silently ignored), but the aggregate count can't be trusted without a dedup/renumbering pass.
**Fix:** renumber the backlog list sequentially and reconcile the prose count against the corrected total.

### 7. CARRIED (4th audit) — the Fisher/SFMOMA LinkedIn post still collapses the 720+ vs ~1,100-works scope distinction.
`marketing/linkedin-posts.md:44-58` is unchanged: "By the end they had more than a thousand works..." leads directly into "...in 2009, they made a deal with the San Francisco Museum of Modern Art. The museum would show the collection for 100 years," so "the collection" reads back to the just-stated thousand-plus figure. `claims-register.md`'s Fisher/SFMOMA entry (C53) and `cases/fisher-sfmoma.md` are both explicit that only **720+ of the ~1,100 total works** are the SFMOMA-loaned subset.
**Fix:** before this post is scheduled, either state the loan figure as 720+ works or drop "more than a thousand" from the sentence that leads into the loan.

### 8. `marketing/website.md` carries several undocumented, unreconciled divergences from `positioning.md`'s canonical text.
Three separate gaps in the same file: (a) `website.md` itself notes, unresolved and with no owner or date, that "the live hero/section copy differs from the canonical public copy in `[[positioning]]`... align positioning to the live copy when convenient" — an acknowledged but unfixed drift risk; (b) the reported live bio sentence ("In recent years, research and writing have become a greater focus of my work") differs in wording from positioning.md's canonical Bio ("Over time, research and writing became an increasingly important part of my work") without either being marked as the authoritative version; (c) the alinaokun.com "Current" section phrasing ("Research and advisory work on the decisions that shape the long-term future of private art collections") does not appear in positioning.md at all and isn't flagged as a deliberate variant.
**Standard violated:** QA remit (e) single source of truth.
**Fix:** reconcile website.md's copy against positioning.md (update whichever is stale) and mark any deliberate per-channel variant explicitly as such, the way `marketing/linkedin.md` and `marketing/substack.md` already do.

---

## MINOR

### 9. CARRIED — the `origin` frontmatter field still spans five undocumented values.
Current usage, unchanged in shape from the last audit: `private-individual` (36) · `corporate` (18) · `private` (14) · `individual` (5) · `artist` (4).
**Fix:** consolidate the private-side variants and document all authorized values, including `artist`, in `case-template.md`.

### 10. CARRIED — corporate-continuity vocabulary still fragmented.
`bank-of-america-collection.md`, `credit-suisse-ubs-collection.md`, `deutsche-bank-collection.md`, `jpmorgan-chase-collection.md`, and `ubs-art-collection.md` use `parent-entity-continuity`; `enron-art-collection.md` and `lehman-brothers-collection.md` use `parent-entity-survival` for the same concept.
**Fix:** adopt one term; add it as an authorized value in `case-template.md`.

### 11. CARRIED — `primary_friction` schema gap, now self-flagged in three files.
`cases/benini.md` (`unknown`, not an authorized value), `cases/rauschenberg-foundation-hq.md`, and `cases/unicredit-art-collection.md` all independently flag the same missing controlled-vocabulary value for "voluntary reallocation from a position of strength" (as distinct from `funding-gap` or `founder-control`).
**Fix:** recode `benini.md` to `none-documented` if no friction is actually documented, or add `unknown` to the controlled list if the distinction is intentional; add an authorized value for the reallocation-from-strength shape the other two cases hit.

### 12. `company/decisions/2026-08-14-board-membership.md` is still marked open.
Its Outcome line reads *"_open — shortlist being researched into [[board-opportunities]]._"* A file living in the `decisions/` folder that has not actually decided anything is a minor structural mismatch (distinct from `2026-08-22-retire-daily-checkin.md`, which is resolved with a normal future review note).
**Fix:** move it out of `decisions/` until resolved, or note plainly that it tracks an in-progress decision rather than a settled one.

---

## Checked, no issue found
- **New case sourcing** (17 of 18 files: gochman-family-collection, museum-macan, warehouse-wieland, bonovitz-collection, joy-of-giving-something, mennello-museum, malba-costantini, monte-dei-paschi-collection, schnitzer-family-foundation, barjeel-art-foundation, standard-bank-art-collection, yemisi-shyllon-museum-of-art, easton-foundation, fondation-pierre-berge-yves-saint-laurent, hsbc-art-collection, charles-dee-mitchell-collection, uob-art-collection): every quantitative and governance claim carries a source and confidence tag or an explicit `unknown`; `verification_status` tags honestly match actual sourcing depth. `kenneth-c-griffin-collection.md` is the sole exception (CRITICAL #4).
- **UPPER BOUND labeling**: every computed `net_assets_to_opex_ratio` found, in new cases and across the corpus, correctly carries the label; cases correctly marked `not computable` rather than forced (e.g. `art-bridges-foundation.md`) are handled properly.
- **Claims-register drift**: no drift found for the $992B transfer figure, the McNay 9.3x/6.4x ratios, or the estate-tax-exemption figure anywhere outside claims-register.md; report-dataset.md and case-template.md's own worked example match C4 exactly.
- **Over-claiming**: `research/what-we-now-believe.md` (six new entries this window) remains rigorously hedged — every finding is framed as sharpening, narrowing, or complicating a belief, never as settled, with explicit "next test" and "unknowns" sections on each entry. No rate or percentage in `report-dataset.md` or the manuscript runs off the hand-selected case set as if representative without a stated denominator.
- **Primary-verification backlog**: actively tracked and growing in proportion to case count (numbering issue aside, see SHOULD-FIX #6).
- **Single source of truth (working pages)**: `marketing/linkedin.md` and `marketing/substack.md` correctly hold no independent copy and point to `[[positioning]]`; only `marketing/website.md` (SHOULD-FIX #8) and the INDEX/archive pointers (CRITICAL #1) have gaps.
- **Decisions folder**: four of five files are properly resolved (see MINOR #12 for the exception).

---

## Resolved since the 2026-09-02 audit
None outright. CRITICAL #1 changed shape (a human action was taken — the conflicting brief was archived — but the vault's pointers were not updated to match, so the underlying contradiction persists). CRITICAL #2 and #3 (the previous audit's items 2 and 3) are unchanged, confirmed by direct re-check this run. SHOULD-FIX #7 (Fisher/SFMOMA) is also unchanged, confirmed by direct re-check this run.

---

**Counts:** 5 critical (3 carried in some form, 2 new) / 3 should-fix (1 carried, 2 new) / 4 minor (3 carried, 1 new).
