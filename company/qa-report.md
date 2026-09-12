# QA Report — 2026-09-12 (post commit 32643df, 210 coded cases)

**Verdict:** Not clean. All 7 CRITICAL items from the last eleven consecutive audits remain open. One (em dashes in `public_*` export fields) got worse again, two new files this window. One (the manuscript em-dash count) is corrected below: it has not actually been "growing worse" as the last several audits reported — that count was conflating the report body with the manuscript's own internal "Production notes (the workshop, not part of the report)" section. The six new cases this window (`john-g-johnson-collection.md`, `leeum-museum-of-art.md`, `nestle-art-collection.md`, `axa-winterthur-art-collection.md`, `mmca-sri-lanka.md`, `witness-collection-vietnam.md`) are well-sourced, honestly hedged, and correctly withheld from the public export pending the QA gate — sourcing discipline (remit item a) continues to hold across this window; voice discipline on public fields (remit item d) does not, and a new small structural (controlled-vocabulary) gap surfaced in `decision_owner`.

---

## CRITICAL

### 1. CARRIED, eleventh+ consecutive audit — the "professional-services pivot" contradiction is unresolved.
`HOME.md:7` still states Nariway "is a specialist service used by estate attorneys and fiduciaries to control and document the resolution of significant art collections." Meanwhile this window's two research runs (`eaeb0f3`, `32643df`) kept building the other model: six new coded cases (207 → 210), `research/claims-register.md` through C108, and the manuscript, all consistent with `company/positioning.md` ("research and advisory for private art collections"). Both models are still under active, parallel construction with no reconciling decision on record.
**Standard violated:** `[[positioning]]`'s single-source rule; QA remit (e) and (f).
**Fix:** needs Alina's decision, not an editorial one — confirm whether the pivot stands, was abandoned, or the two tracks are deliberately parallel (in which case say so explicitly in `HOME.md`/`INDEX.md`), and log the resolution in `company/decisions/`.

### 2. CARRIED — `export/nariway-public.json:11454` still blends three non-comparable wealth-transfer figures into one number.
Still reads `"value": "~$31T+"` with source line `"wealth-research (Cerulli / UBS / Knight Frank)"` — the exact mixing `claims-register.md` C36 (and C100-C101) exists to forbid: Deloitte/ArtTactic's ~$31T decade/global figure (C1's input), Cerulli's $124T US-only/2048 figure (C8), and Knight Frank's UHNW *population* count (C100, not a transfer total), cited as if they were one source for one number.
**Fix:** replace with the Deloitte/ArtTactic-only $31T figure; drop Knight Frank and Cerulli from the source line.

### 3. CARRIED AND WORSE — em dashes in live `public_*` fields, now at least 26 case files, two more added this exact window.
A fresh corpus-wide scan (`grep` every `public_*` frontmatter line for an em dash) finds 26 files: the files named in prior audits (including `artists-legacy-foundation.md`, `kinosaito.md`, `helen-frankenthaler-foundation.md`) remain unfixed, plus several not previously enumerated by name (`fresno-metropolitan-museum.md`, `instituto-moreira-salles.md`, `lee-kun-hee-collection.md`, `malba-costantini.md`, `mowaa.md`, `sakip-sabanci-museum.md`, `schnitzer-family-foundation.md`, `yemisi-shyllon-museum-of-art.md`), and **two genuinely new this window**: `cases/axa-winterthur-art-collection.md:33` (`public_origin`, "Credit Suisse in 1996, then AXA in 2006 —") and `cases/mmca-sri-lanka.md:27,32` (`public_focus` and `public_origin`). The other four cases coded this window (`john-g-johnson-collection.md`, `leeum-museum-of-art.md`, `nestle-art-collection.md`, `witness-collection-vietnam.md`) are clean, proof the discipline is achievable but still inconsistently applied within the same batch. `export/nariway-public.json` is unaffected this window (all new cases correctly excluded pending the QA gate; the export's own confirmed em-dash count is unchanged at 31 occurrences across existing exported fields).
**Standard violated:** `[[voice]]`/`[[ai-tells]]`, no em dashes, applied to public-facing copy per QA remit (d).
**Fix:** fix all 26 flagged files' `public_*` fields in one pass and regenerate the export. A pre-commit grep for em dashes across `public_*` lines (recommended in at least five consecutive audits now) would stop this recurring — the fact that four of this window's six new cases already passed clean shows the check is trivial when someone remembers to run it before committing.

### 4. CARRIED — `cases/kenneth-c-griffin-collection.md` still states a chain of dollar figures with zero inline sourcing.
The "Confirmed holdings" list (de Kooning $300M, Pollock $200M, Johns $80M, Basquiat >$100M, Cézanne ~$60M, Richter $46M) is prefaced "(each price/year sourced)" but carries no per-figure `[source: URL; confidence: tier]` tag, only a blanket `public_sources` list at the bottom of the frontmatter. `cases/report-dataset.md` still counts this file as a numbered, coded row.
**Fix:** add a source/confidence tag to each figure, or downgrade `verification` until it's done.

### 5. CARRIED — "significant" as a prestige adjective for collections is still live in `company/positioning.md`, including its own approved example.
Unchanged at lines 8, 13, 34, 112, 135, and the codified ✅ example itself at line 138.
**Standard violated:** `[[voice]]`'s explicit, non-negotiable craft standard; QA remit (d).
**Fix:** replace with "private art collections" / "collectors" at the live-copy instances and the approved example, then propagate downstream.

### 6. CORRECTED, still open — the manuscript's actual report-body em-dash count is flat, not "growing worse" as the last five audits claimed; a real, unaddressed count of 59 remains.
`marketing/what-becomes-of-great-art-collections.md` is two documents in one file: the report itself (through `## Appendix. Methodology and sources`, ending before line 617-635 depending on version) and an explicitly internal `## Production notes (the workshop, not part of the report)` section that follows it. Re-counting em dashes **only in the actual report body** (excluding the self-declared-internal Production notes) across this window's two commits gives a flat **59 at every point checked** — `fb8c93c` (the last-audited commit), `eaeb0f3`, `32643df`, and current HEAD all show 59. The two new §3 paragraph blocks added this window are themselves em-dash-free, confirmed by direct diff inspection. The "83 → 86 → 93 → 97 → 99 → 101" growth trend the last several audits reported was almost certainly counting the whole file, including the Production notes changelog (which does grow every run, currently 293 em dashes total there, up from 279 at the last audit) — a section the file's own heading disclaims as not part of the report. **This is a correction to the prior audits' method, not a clean bill of health:** 59 em dashes in the live report body is itself a real, sizable, standing violation of `[[voice]]`'s no-em-dash rule, unaddressed across at least seven consecutive audits regardless of which count is used.
**Standard violated:** `[[voice]]` lines 26-27 (no em dashes, no colons in prose); `[[ai-tells]]`.
**Fix:** a dedicated pass across the report body (lines 1 through the Appendix) is overdue — line-by-line chasing during research runs is demonstrably not working, and new prose additions are staying clean, so the 59 are legacy text needing one cleanup pass. Recommend future audits scope this count to the report body only, and separately track (but not classify as a voice violation) the Production notes section, which is internal working notes rather than public-facing copy.

### 7. CARRIED — the LACMA construction-cost contradiction (C38 vs. an unregistered second figure) is still live and unreconciled.
`research/claims-register.md` C38 (unchanged): David Geffen Galleries "opened April 2026," cost "~$724M total," a closed, finished project. `research/market-intelligence.md:251` (unchanged): "LACMA's ongoing building project has grown from an initial ~$600M estimate to over $750M... with 2026 completion still the target" — an open, still-in-progress project. Both describe LACMA construction but cannot both be the same project as stated.
**Standard violated:** `claims-register.md`'s single-source/no-drift discipline; QA remit (c).
**Fix:** determine whether this is the same Geffen Galleries project (drop the stale $600-750M framing) or a distinct project (give it its own claims-register entry, clearly distinguished from C38).

---

## SHOULD-FIX

### 8. CARRIED, slightly worse with corpus growth — `constraints_documented` values fall outside the field's own controlled vocabulary at real scale.
`case-template.md:23` defines only `yes` · `no` · `partial` · `open`. A full corpus recount finds **21 rows using `n/a`, 16 using `unknown`, and 1 using `YES`** (capitalization drift) — 38 rows outside the permitted four values, up from 36 at the last audit (proportional to corpus growth, no new pattern).
**Fix:** amend `case-template.md` to add `n/a` and `unknown` to the vocabulary, and normalize the one `YES` to `yes`.

### 9. CARRIED — the Fisher/SFMOMA LinkedIn post still collapses the 720+ vs. ~1,100-works distinction.
`marketing/linkedin-posts.md:48,230` unchanged: "more than a thousand works" leads directly into the SFMOMA loan framing, reading as if the whole collection was loaned. `claims-register.md` C53 and `cases/fisher-sfmoma.md` both specify only 720+ of ~1,100 works are the SFMOMA-loaned subset.
**Fix:** state the 720+ figure or drop "more than a thousand" from the lead-in before this post is scheduled.

### 10. CARRIED — `marketing/website.md` still diverges from `positioning.md`'s canonical Bio wording without being marked as a deliberate variant.
`website.md:21`: "In recent years, research and writing have become a greater focus of my work" vs. `positioning.md`'s canonical Bio: "Over time, research and writing became an increasingly important part of my work." Neither file flags the other as authoritative.
**Fix:** reconcile, or explicitly mark the variant as deliberate, the way `linkedin.md`/`substack.md` already do.

### 11. CARRIED — `cases/cultural-museum-of-african-art.md` still states an unsourced superlative as fact.
`public_origin` still reads "one of the largest private African art collections in the US" with no attribution.
**Fix:** attribute it ("press coverage described it as...") or drop "one of the largest."

### 12. CARRIED (third consecutive audit) — `cases/neue-galerie.md` states an unsourced superlative in the coded header.
Line 51, unchanged: `durability_signal: strong — the merger absorbs the institution into one of the world's best-capitalized museums...`. Still no blanket sourcing footnote and no inline source tag for the superlative. Internal coded header, not an exported `public_*` field, so lower severity than items 3/11, but the same failure mode.
**Fix:** attribute the claim (e.g., to the Met's own endowment disclosures) or soften to "a large, well-capitalized museum."

---

## MINOR

### 13. NEW — `decision_owner` carries five rows outside the field's own controlled vocabulary.
`case-template.md`'s `decision_owner` list is exactly thirteen named values (`collector-alone` · `spouse` · `children` · `estate-attorney` · `art-advisor` · `museum-director` · `family-office` · `architect` · `philanthropic-advisor` · `foundation-executive` · `consultant` · `auction-house` · `no-identifiable-person`) with no `unknown`/`n/a` escape hatch. A corpus tally finds one row using **`family`** (`cases/leeum-museum-of-art.md`, coded this window — likely meant as shorthand for `children`/`family-office`, neither of which quite fits a three-generation collector family) and four using **`unknown`** (`cases/di-rosa.md`, `cases/herbert-lust-collection.md`, `cases/souls-grown-deep.md`, `cases/terra.md`, pre-existing, not new this window). The same failure pattern already flagged for `constraints_documented` (item 8).
**Fix:** either add `family` and `unknown` to `case-template.md`'s `decision_owner` vocabulary, or recode the five rows to an existing value.

### 14. CARRIED — the `origin` frontmatter field still spans 8 raw values.
Tally: `private-individual` (60) · `corporate` (27) · `private` (14) · `individual` (8) · `artist` (8) · `private individual` (6) · `artist-estate` (5) · `institutional` (3). Counts grew proportionally with the corpus (210 cases now vs. 204 last audit); no new variant spelling appeared this window.
**Fix:** consolidate the private-side spelling variants; decide whether `artist-estate` is a deliberate new category (distinct from plain `artist`) or drift, and document it in `case-template.md` either way.

### 15. CARRIED — corporate-continuity vocabulary still fragmented (`parent-entity-continuity` vs. `parent-entity-survival`).
The three new corporate-origin cases this window (`nestle-art-collection.md`, `axa-winterthur-art-collection.md`, `leeum-museum-of-art.md`) all have identifiable individual/family founders and correctly use the ordinary `founder_status_at_transition`/`survived_founder` fields rather than the parent-entity recoding convention, so they neither worsen nor resolve the split. The older files (`enron-art-collection.md`, `lehman-brothers-collection.md`) still carry the older `parent-entity-survival` term against six newer files' `parent-entity-continuity`, unreconciled.
**Fix:** adopt one term, add it to `case-template.md`.

### 16. CARRIED — `primary_friction` has no authorized value for a case that isn't a funding shortfall but gets coded `funding-gap` anyway.
No new instance surfaced this window; the two previously-flagged cases (Kawamura, Kirkland) remain the evidence.
**Fix:** add at least one missing authorized value to `case-template.md`'s `primary_friction` list.

### 17. CARRIED — `company/decisions/2026-08-14-board-membership.md` is still marked open.
Outcome line still reads `_open — shortlist being researched into [[board-opportunities]]._`
**Fix:** move out of `decisions/` until resolved, or mark plainly as in-progress.

---

## Checked, no issue found

- **The six new case files this window** (`john-g-johnson-collection.md`, `leeum-museum-of-art.md`, `nestle-art-collection.md`, `axa-winterthur-art-collection.md`, `mmca-sri-lanka.md`, `witness-collection-vietnam.md`): every quantitative and governance claim carries an inline source/confidence tag or an explicit `unknown`; gaps sections are honest and specific (e.g. `mmca-sri-lanka.md` names exactly what wasn't located: object count, current budget, attendance, building-search status). No `verification_status` upgraded past `Spot-verified` without cause.
- **New claims-register entries C107-C108** and their `market-intelligence.md` addenda: correctly sourced to named surveys (wealth-manager/family-office borrower-behavior figures; Hiscox's own "Art and AI Report"), framed as complementary to, not a replacement for, adjacent existing entries.
- **`research/what-we-now-believe.md`'s two new disconfirmation entries** (Rauschenberg trustee litigation; AXA Winterthur insider theft): both properly hedged, state their own scope limits (CHF 1.1M is explicitly flagged as a smaller relative stress than Rauschenberg's $24.6M award, not overgeneralized), and are framed as sharpening rather than reversing the existing governance-durability reading.
- **Export gate discipline:** all six new cases this window are correctly excluded from `export/nariway-public.json` (confirmed still 189 collections) pending the independent QA fact-check pass, exactly as the case-template's export-gate rule requires.
- **WebFetch spot-check attempted:** tried to independently verify the LACMA/C38 source (ArchDaily) named in item 7; blocked by the same `EGRESS_BLOCKED` network restriction the vault's own research runs have logged 60+ consecutive times. Not a finding against the vault — an environment limitation on this audit's own side too.

---

**Counts:** 7 critical (6 carried unchanged in substance, 1 worse [#3], 1 corrected-but-still-open [#6]) / 5 should-fix (5 carried, 0 new) / 5 minor (4 carried, 1 new [#13]).
