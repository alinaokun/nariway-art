# QA Report — 2026-09-11 (post commit fb8c93c, 204 coded cases)

**Verdict:** Not clean. All 7 CRITICAL items from the last ten consecutive audits remain open, and two continue to get worse: the manuscript's em-dash count rose again (97 → 99), and the public-facing em-dash ban now spans at least 21 case files with `public_*` em dashes confirmed, after three more were added this exact window (`artists-legacy-foundation.md`, `kinosaito.md`, `helen-frankenthaler-foundation.md`) — while three sibling cases coded the same run (`roy-lichtenstein-foundation.md`, `nancy-graves-foundation.md`, `resnick-passlof-foundation.md`) got it right, so the discipline is inconsistent within the same batch, not universally absent. The three new cases and this window's claims-register/market-intelligence additions (C106) are otherwise well-sourced, honestly hedged, and correctly withheld from the public export pending the independent QA gate — sourcing discipline (remit item a) continues to hold; voice discipline on public fields (remit item d) does not.

---

## CRITICAL

### 1. CARRIED, tenth+ consecutive audit — the "professional-services pivot" contradiction is unresolved, and the vault keeps building on both sides of it.
`INDEX.md:3`, `HOME.md:7`, and `archive/README.md:8-14` still state Nariway pivoted to "a specialist service used by estate attorneys and fiduciaries to control and document the resolution of significant art collections." Meanwhile this window's research runs (`fb8c93c`, `381a0c3`) kept building out the *other* model: three new coded cases, `research/claims-register.md` (through C106), `cases/report-dataset.md` (204 coded cases), and the manuscript, all consistent with `company/positioning.md` ("research and advisory for private art collections"). Both models are still under active, parallel construction with no reconciling decision on record.
**Standard violated:** `[[positioning]]`'s single-source rule; QA remit (e) and (f).
**Fix:** needs Alina's decision, not an editorial one — confirm whether the pivot stands, was abandoned, or the two tracks are deliberately parallel (in which case say so explicitly in `HOME.md`/`INDEX.md`), and log the resolution in `company/decisions/`.

### 2. CARRIED — `export/nariway-public.json:11454` still blends three non-comparable wealth-transfer figures into one number.
Still reads `"value": "~$31T+"` with source line `"wealth-research (Cerulli / UBS / Knight Frank)"` — the exact mixing `claims-register.md` C36 (and C100-C101) exists to forbid: Deloitte/ArtTactic's ~$31T decade/global figure (C1's input), Cerulli's $124T US-only/2048 figure (C8), and Knight Frank's UHNW *population* count (C100, not a transfer total), cited as if they were one source for one number.
**Fix:** replace with the Deloitte/ArtTactic-only $31T figure; drop Knight Frank and Cerulli from the source line.

### 3. CARRIED AND WORSE — em dashes in live `public_*` export fields, now at least 21 files, three added this exact window.
Every file named in the last audit remains unfixed (23 files: the original 13 + afkhami, agadir, mathaf, rosenwald, soane + wallace-collection-london, uc-irvine-langson-ocma + art-car-museum, botero-donation-banco-de-la-republica, monte-dei-paschi-collection, standard-bank-art-collection, unicredit-art-collection, vass-collection-modern-art-gallery). **Three more found this pass, all added this exact window (`fb8c93c`):** `cases/artists-legacy-foundation.md:33` (`public_origin`, two em dashes bracketing an artist-name aside), `cases/kinosaito.md:34` (`public_origin`), `cases/helen-frankenthaler-foundation.md:32` (`public_origin`). Notably, the three *sibling* cases coded in the same and prior run (`roy-lichtenstein-foundation.md`, `nancy-graves-foundation.md`, `resnick-passlof-foundation.md`) carry no em dashes in their public fields — proof the discipline is achievable, just inconsistently applied. The live `export/nariway-public.json` itself still carries em dashes copied straight from these fields (35 confirmed by an exhaustive scan of all string values, e.g. `origin` and `name` fields); the three newest cases are correctly excluded from this export pending the QA gate, so the export count did not grow this window, but the underlying source files did.
**Standard violated:** `[[voice]]`/`[[ai-tells]]`, no em dashes, applied to public-facing copy per QA remit (d).
**Fix:** fix all flagged files' `public_*` fields in one pass and regenerate the export. Recommended in at least four consecutive audits now: a pre-commit grep for em dashes across `public_*` lines (and the export script itself) would stop it recurring every run — the fact that half of this window's new cases already passed clean shows the check is easy to apply when someone remembers to.

### 4. CARRIED — `cases/kenneth-c-griffin-collection.md` still states a chain of dollar figures with zero inline sourcing.
The "Confirmed holdings" list (de Kooning $300M, Pollock $200M, Johns $80M, Basquiat >$100M, Cézanne ~$60M, Richter $46M) still carries no per-figure `[source: URL; confidence: tier]` tag, only a blanket `public_sources` list at the bottom of the frontmatter. `report-dataset.md` still counts this file as a numbered, coded row.
**Fix:** add a source/confidence tag to each figure, or downgrade `verification` until it's done.

### 5. CARRIED — "significant" as a prestige adjective for collections is still live in `company/positioning.md`, including its own approved example.
Unchanged at lines 8, 13, 34, 112, and the codified ✅ example itself at line 138.
**Standard violated:** `[[voice]]`'s explicit, non-negotiable craft standard; QA remit (d).
**Fix:** replace with "private art collections" / "collectors" at the live-copy instances and the approved example, then propagate downstream.

### 6. CARRIED AND WORSE — the manuscript's em-dash count has grown again, at least the fifth consecutive audit (83 → 86 → 93 → 97 → 99).
`marketing/what-becomes-of-great-art-collections.md` now shows 99 em dashes, up from 97 two audits ago. The two new paragraphs added this window (§3's single-controlled-foundation finding, §4.5's worsening-survey-trend finding) are themselves clean of em dashes on inspection, so the growth is coming from elsewhere in the file (prior edits, changelog prose) rather than the newest additions — but the total keeps climbing regardless.
**Standard violated:** `[[voice]]` lines 26-27 (no em dashes, no colons in prose); `[[ai-tells]]`.
**Fix:** a dedicated pass across the whole manuscript is overdue — line-by-line chasing during research runs is demonstrably not working.

### 7. CARRIED — the LACMA construction-cost contradiction (C38 vs. an unregistered second figure) is still live and unreconciled.
`research/claims-register.md` C38 (unchanged): David Geffen Galleries "opened April 2026," cost "~$724M total," a closed, finished project. `research/market-intelligence.md:251` (unchanged): "LACMA's ongoing building project has grown from an initial ~$600M estimate to over $750M... with 2026 completion still the target" — an open, still-in-progress project. Both describe LACMA construction but cannot both be the same project as stated.
**Standard violated:** `claims-register.md`'s single-source/no-drift discipline; QA remit (c).
**Fix:** determine whether this is the same Geffen Galleries project (drop the stale $600-750M framing) or a distinct project (give it its own claims-register entry, clearly distinguished from C38).

---

## SHOULD-FIX

### 8. CARRIED — `constraints_documented` values fall outside the field's own controlled vocabulary at real scale.
`case-template.md:23` defines only `yes` · `no` · `partial` · `open`. A full corpus recount finds **20 rows using `n/a`, 15 using `unknown`, and 1 using `YES`** (capitalization drift) — 36 rows outside the permitted four values, unchanged from the last audit.
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

### 12. CARRIED (second consecutive audit) — `cases/neue-galerie.md` states an unsourced superlative in the coded header.
Line 51, unchanged: `durability_signal: strong — the merger absorbs the institution into one of the world's best-capitalized museums...`. Still no blanket sourcing footnote and no inline source tag for the superlative. Internal coded header, not an exported `public_*` field, so lower severity than items 3/11, but the same failure mode, now confirmed persisting rather than a one-off.
**Fix:** attribute the claim (e.g., to the Met's own endowment disclosures) or soften to "a large, well-capitalized museum."

---

## MINOR

### 13. CARRIED AND WORSE — the `origin` frontmatter field now spans 8 raw values, not 7.
Tally: `private-individual` (59) · `corporate` (24) · `private` (14) · `individual` (8) · `artist` (8) · `private individual` (6) · `institutional` (3) · **`artist-estate` (5, new)**. All five files using the new `artist-estate` spelling were coded in the last two research runs (`helen-frankenthaler-foundation.md`, `kinosaito.md`, `nancy-graves-foundation.md`, `resnick-passlof-foundation.md`, `roy-lichtenstein-foundation.md`) — a genuinely new, previously-untallied variant, not more instances of an existing one.
**Fix:** consolidate the private-side spelling variants; decide whether `artist-estate` is a deliberate new category (distinct from plain `artist`) or drift, and document it in `case-template.md` either way.

### 14. CARRIED — corporate-continuity vocabulary still fragmented (`parent-entity-continuity` vs. `parent-entity-survival`).
No new corporate cases this window, so the split neither worsened nor improved; `report-dataset.md` and the older files (`enron-art-collection.md`, `lehman-brothers-collection.md`) still carry the older `parent-entity-survival` term unreconciled.
**Fix:** adopt one term, add it to `case-template.md`.

### 15. CARRIED — `primary_friction` has no authorized value for a case that isn't a funding shortfall but gets coded `funding-gap` anyway.
No new instance surfaced this window; the two previously-flagged cases (Kawamura, Kirkland) remain the evidence.
**Fix:** add at least one missing authorized value to `case-template.md`'s `primary_friction` list.

### 16. CARRIED — `company/decisions/2026-08-14-board-membership.md` is still marked open.
Outcome line still reads `_open — shortlist being researched into [[board-opportunities]]._`
**Fix:** move out of `decisions/` until resolved, or mark plainly as in-progress.

---

## Checked, no issue found

- **The three new case files this window** (`artists-legacy-foundation.md`, `kinosaito.md`, `roy-lichtenstein-foundation.md`): every quantitative and governance claim carries an inline source/confidence tag or an explicit `unknown`/`not-computable`. All three `net_assets_to_opex_ratio` values are correctly labeled `[UPPER BOUND, secondary-sourced]`. No `verification_status` upgraded past `Spot-verified` without cause. Consistent with the last several audits' finding on sourcing discipline (remit a).
- **New claims-register entry C106** and its `market-intelligence.md` addendum: correctly sourced to AAM's own named survey report, carries an explicit "do NOT treat as a population rate" guardrail, and is distinguished from the related point-in-time figures (C57, C88) it extends rather than duplicates.
- **`research/what-we-now-believe.md`'s new disconfirmation entry** (Roy Lichtenstein Foundation, testing sole/spousal-control durability): properly hedged, states its own unknowns and next test, does not overstate the finding as a reversal of the existing H6/H8 reading.
- **Export gate discipline:** all three new cases this window are correctly excluded from `export/nariway-public.json` (still 189 collections) pending the independent QA fact-check pass, exactly as the case-template's export-gate rule requires.

---

**Counts:** 7 critical (7 carried, 2 worse / grown) / 5 should-fix (5 carried, 0 new) / 4 minor (4 carried, 1 worse with a genuinely new sub-instance).
