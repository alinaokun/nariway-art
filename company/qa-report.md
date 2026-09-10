# QA Report — 2026-09-10 (post commit c5eef64, 198 coded cases)

**Verdict:** Not clean. All 7 CRITICAL items from the last nine consecutive audits remain open. Two continue to get worse: the em-dash ban on public-facing fields now spans at least 22 case files (up from 18), including two files added this very window that were never previously flagged, and the em dashes have been confirmed propagating into the live `export/nariway-public.json` itself, not just source case files. The manuscript's em-dash count rose again, 93 → 97. The ten new cases coded this window (Afkhami, Agadir, Artizon, Bassam Freiha, Dib Bangkok, Faro Santander, Fondation Zinsou, Hudson's Bay, Jules Strauss, Kawamura, Kirkland, Laura Privatstiftung/Benko, Mathaf, Museum of Photographic Arts, National Gallery/Mellon, Neue Galerie update, Rosenwald, Soane's Museum, UC Irvine/OCMA, Wallace Collection) are otherwise well-sourced and honestly hedged — sourcing discipline (remit item a) continues to hold; voice discipline on public fields (remit item d) does not.

---

## CRITICAL

### 1. CARRIED, ninth+ consecutive audit — the "professional-services pivot" contradiction is unresolved, and the vault keeps building on both sides of it.
`INDEX.md:3` and `archive/README.md:8-14` still state Nariway pivoted to "a specialist professional-services firm for estate attorneys and fiduciaries." `HOME.md:7` (the daily cockpit) still opens with "Nariway is a specialist service used by estate attorneys and fiduciaries to control and document the resolution of significant art collections." Meanwhile this window added real infrastructure for *that* model — `marketing/offer-collection-transition-assessment.md` (a four-offer pricing ladder, entry fee ~$5,000) and `marketing/sample-matter-map.md` — while the research/case-coding engine keeps building the other model: `company/positioning.md` ("research and advisory for private art collections"), `research/claims-register.md` (through C104), `cases/report-dataset.md` (198 coded cases), and the manuscript. Both models are now actively under construction in parallel with no reconciling decision on record.
**Standard violated:** `[[positioning]]`'s single-source rule; QA remit (e) and (f).
**Fix:** needs Alina's decision, not an editorial one — confirm whether the pivot stands, was abandoned, or the two tracks are deliberately parallel (in which case say so explicitly in `HOME.md`/`INDEX.md`), and log the resolution in `company/decisions/`.

### 2. CARRIED — `export/nariway-public.json:11454` still blends three non-comparable wealth-transfer figures into one number.
Still reads `"value": "~$31T+"` with source line `"wealth-research (Cerulli / UBS / Knight Frank)"` — the exact mixing `claims-register.md` C36 (and C100-C101, added this window) exists to forbid: Deloitte/ArtTactic's ~$31T decade/global figure (C1's input), Cerulli's $124T US-only/2048 figure (C8), and Knight Frank's UHNW *population* count (C100, not a transfer total), cited as if they were one source for one number.
**Fix:** replace with the Deloitte/ArtTactic-only $31T figure; drop Knight Frank and Cerulli from the source line.

### 3. CARRIED AND WORSE — em dashes in live `public_*` export fields, now at least 22 files, confirmed propagating into the actual public export JSON.
Confirmed still unfixed in every file named in the last audit (13 original + 5 more: afkhami, agadir, mathaf, rosenwald, soane) — 18 files. **Two more found this pass, added this exact window and never previously flagged:** `cases/wallace-collection-london.md:33` (`public_origin`) and `cases/uc-irvine-langson-ocma.md:31` (`public_origin`) — meaning this is not only carried debt, it is still being produced in brand-new case files each run. A fuller sweep also turned up several long-standing files missed by prior audits: `cases/art-car-museum.md:30`, `cases/botero-donation-banco-de-la-republica.md:37`, `cases/monte-dei-paschi-collection.md:21,34`, `cases/standard-bank-art-collection.md:34`, `cases/unicredit-art-collection.md:24`, `cases/vass-collection-modern-art-gallery.md:23`. **New this pass:** `export/nariway-public.json` itself now carries at least 31 em dashes copied straight from these `public_*` fields (e.g. line 214, Agadir's `origin`; line 693, Monte dei Paschi's `name`) — this is no longer just a case-file hygiene problem, it is live in the artifact the public site actually renders from.
**Standard violated:** `[[voice]]`/`[[ai-tells]]`, no em dashes, applied to public-facing copy per QA remit (d).
**Fix:** fix all flagged files' `public_*` fields in one pass and regenerate the export. This has now been recommended in at least three consecutive audits: a pre-commit grep for em dashes across `public_*` lines (and the export script itself) would stop it recurring every run.

### 4. CARRIED — `cases/kenneth-c-griffin-collection.md` still states a chain of dollar figures with zero inline sourcing.
The "Confirmed holdings" list (de Kooning $300M, Pollock $200M, Johns $80M, Basquiat >$100M, Cézanne ~$60M, Richter $46M) still carries no per-figure `[source: URL; confidence: tier]` tag, only a blanket `public_sources` list at the bottom of the frontmatter. `report-dataset.md` still counts this file as a numbered, coded row.
**Fix:** add a source/confidence tag to each figure, or downgrade `verification` until it's done.

### 5. CARRIED — "significant" as a prestige adjective for collections is still live in `company/positioning.md`, including its own approved example.
Unchanged at lines 8, 13, 34, 112, and the codified ✅ example itself at line 138.
**Standard violated:** `[[voice]]`'s explicit, non-negotiable craft standard; QA remit (d).
**Fix:** replace with "private art collections" / "collectors" at the live-copy instances and the approved example, then propagate downstream.

### 6. CARRIED AND WORSE — the manuscript's em-dash count has grown again, at least the fourth consecutive audit (83 → 86 → 93 → 97).
`marketing/what-becomes-of-great-art-collections.md` now shows 97 em dashes, up from 93 two audits ago, despite 62 lines of edits landing in this file this window. This item has grown on every audit since it was first flagged.
**Standard violated:** `[[voice]]` lines 26-27 (no em dashes, no colons in prose); `[[ai-tells]]`.
**Fix:** a dedicated pass across the whole manuscript is overdue — line-by-line chasing during research runs is demonstrably not working.

### 7. CARRIED — the LACMA construction-cost contradiction (C38 vs. an unregistered second figure) is still live and unreconciled.
`research/claims-register.md` C38 (unchanged): David Geffen Galleries "opened April 2026," cost "~$724M total," a closed, finished project. `research/market-intelligence.md:251` (unchanged): "LACMA's ongoing building project has grown from an initial ~$600M estimate to over $750M... with 2026 completion still the target" — an open, still-in-progress project. Both describe LACMA construction but cannot both be the same project as stated.
**Standard violated:** `claims-register.md`'s single-source/no-drift discipline; QA remit (c).
**Fix:** determine whether this is the same Geffen Galleries project (drop the stale $600-750M framing) or a distinct project (give it its own claims-register entry, clearly distinguished from C38).

---

## SHOULD-FIX

### 8. CARRIED AND DEEPENED — `constraints_documented` values fall outside the field's own controlled vocabulary at real scale.
`case-template.md:23` defines only `yes` · `no` · `partial` · `open`. A full corpus count finds **20 rows using `n/a`, 15 using `unknown`, and 1 using `YES`** (capitalization drift) — 36 rows outside the permitted four values, not a handful of edge cases.
**Fix:** amend `case-template.md` to add `n/a` and `unknown` to the vocabulary (both are clearly needed — cases with no individual founder, or no located instrument), and normalize the one `YES` to `yes`.

### 9. CARRIED — the Fisher/SFMOMA LinkedIn post still collapses the 720+ vs. ~1,100-works distinction.
`marketing/linkedin-posts.md:48,230` unchanged: "more than a thousand works" leads directly into the SFMOMA loan framing, reading as if the whole collection was loaned. `claims-register.md` C53 and `cases/fisher-sfmoma.md` both specify only 720+ of ~1,100 works are the SFMOMA-loaned subset.
**Fix:** state the 720+ figure or drop "more than a thousand" from the lead-in before this post is scheduled.

### 10. CARRIED — `marketing/website.md` still diverges from `positioning.md`'s canonical Bio wording without being marked as a deliberate variant.
"In recent years, research and writing have become a greater focus of my work" (website.md) vs. "Over time, research and writing became an increasingly important part of my work" (positioning.md canonical Bio) — neither file flags the other as authoritative.
**Fix:** reconcile, or explicitly mark the variant as deliberate, the way `linkedin.md`/`substack.md` already do.

### 11. CARRIED — `cases/cultural-museum-of-african-art.md` still states an unsourced superlative as fact.
`public_origin` still reads "one of the largest private African art collections in the US" with no attribution.
**Fix:** attribute it ("press coverage described it as...") or drop "one of the largest."

### 12. NEW — `cases/neue-galerie.md` states an unsourced superlative in the coded header.
Line 51: `durability_signal: strong — the merger absorbs the institution into one of the world's best-capitalized museums...`. Unlike the sample's other corporate/institutional cases added this window (Kawamura, UC Irvine, Hudson's Bay), this file carries no blanket "WebSearch-synthesis, tagged secondary" sourcing footnote and no inline source tag for the superlative itself. Internal coded header, not an exported `public_*` field, so lower severity than items 3/11, but the same failure mode.
**Fix:** attribute the claim (e.g., to the Met's own endowment disclosures) or soften to "a large, well-capitalized museum."

---

## MINOR

### 13. CARRIED, unchanged — the `origin` frontmatter field still spans 7 raw values.
Tally unchanged: `private-individual` (59) · `corporate` (24) · `private` (14) · `individual` (8) · `artist` (7) · `private individual` (6) · `institutional` (3).
**Fix:** consolidate the private-side spelling variants; document `artist` and decide on `institutional` in `case-template.md`.

### 14. CARRIED — corporate-continuity vocabulary still fragmented (`parent-entity-continuity` vs. `parent-entity-survival`).
This window's new corporate case (`hudsons-bay-company-collection.md`) correctly used the more common `parent-entity-continuity` term, so the split isn't worsening, but `report-dataset.md` and the older files (`enron-art-collection.md`, `lehman-brothers-collection.md`) still carry the older `parent-entity-survival` term unreconciled.
**Fix:** adopt one term, add it to `case-template.md`.

### 15. CARRIED, now a third independent instance — `primary_friction` has no authorized value for a case that isn't a funding shortfall but gets coded `funding-gap` anyway.
Kawamura (activist-investor capital-efficiency pressure) and Kirkland → Denver (2021 flood + pandemic closure, explicitly not a described deficit) both flag the same schema gap, each with an honest caveat in the file rather than a silently-forced fit. Handled with good discipline; still a real template gap.
**Fix:** add at least one missing authorized value to `case-template.md`'s `primary_friction` list.

### 16. CARRIED — `company/decisions/2026-08-14-board-membership.md` is still marked open.
Outcome line still reads `_open — shortlist being researched into [[board-opportunities]]._`
**Fix:** move out of `decisions/` until resolved, or mark plainly as in-progress.

---

## Checked, no issue found

- **The ten new/updated case files this window** (Afkhami, Agadir, Artizon, Bassam Freiha, Dib Bangkok, Faro Santander, Fondation Zinsou, Hudson's Bay, Jules Strauss, Kawamura, Kirkland, Laura Privatstiftung/Benko, National Gallery/Mellon, Museum of Photographic Arts, UC Irvine/OCMA, Wallace Collection): every quantitative and governance claim carries an inline `[source: ...]`-style tag or an explicit `unknown`/`not-applicable`/`not-computable`, with reasoning stated rather than assumed. No `net_assets_to_opex_ratio` computed without the required label. No `verification_status` upgraded past what the sourcing supports. Contested figures (e.g. Hudson's Bay's C$4.9M vs C$5.9M hammer price) are flagged as unreconciled, not silently picked. Superlatives are attributed to press coverage rather than stated as fact — except `neue-galerie.md` (item 12, above).
- **New claims-register entries C97-C104:** all correctly sourced, carry explicit "do NOT" guardrails against merging non-comparable figures, and none is asserted above secondary/WebSearch-synthesized confidence. Spot-checked against source framing; no drift found.
- **CRM partner additions this window** (Beth Tractenberg, David Stutzman, David Odo, Kathleen Jameson, Mollie Smith, Philip Hoffman): sourced to named public pages, marked "no contact yet," no fabricated claims.
- **`marketing/offer-collection-transition-assessment.md`:** internal working note, correctly labels its $5,000 fee and pricing ladder as "hypotheses to test," not settled facts — good discipline given H7B is unvalidated (though see item 1 for the model-contradiction this document deepens).

---

**Counts:** 7 critical (7 carried, 2 worse / grown) / 5 should-fix (4 carried, 1 new) / 4 minor (4 carried, 1 with a new supporting instance).
