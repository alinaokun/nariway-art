# QA Report — 2026-09-09 (post commit 5e0571d, 192 coded cases)

**Verdict:** Not clean. All 7 CRITICAL items from the 2026-09-08 audit (`ce1470b`) remain open and unfixed. Two of them got worse this window: the em-dash ban on public-facing case fields was breached in 5 of the 7 new case files added since the last audit (13 → 18 files), and the manuscript's em-dash count rose again (86 → 93). The seven new cases coded this window (Museum of Photographic Arts, Kirkland Museum, Soane's Museum, Rosenwald Collection, Mathaf, Afkhami Foundation, Agadir Museum) are otherwise well-sourced, properly hedged, and honest about gaps — the sourcing discipline (item d in the remit) is holding; the voice discipline (item c... item (d) in the remit) is not.

---

## CRITICAL

### 1. CARRIED, eight consecutive audits — the "professional-services pivot" contradiction is unresolved, and now restated in `HOME.md` itself.
`INDEX.md:3` and `archive/README.md:8-14` still state Nariway pivoted to "a specialist professional-services firm for estate attorneys and fiduciaries," naming three archived documents as current. `HOME.md:5` (the daily cockpit, refreshed every morning) still opens with the identical line: "Nariway is a specialist service used by estate attorneys and fiduciaries to control and document the resolution of significant art collections." Every research and case-coding run since, including this window's two research commits (182→188→192 coded cases), continues to build the other model: `company/positioning.md` ("research and advisory for private art collections," "for collectors and families"), `research/claims-register.md` (102 entries through C102), `cases/report-dataset.md`, and the manuscript.
**Standard violated:** `[[positioning]]`'s single-source rule; QA remit (e) and (f).
**Fix:** needs Alina's decision, not an editorial one — confirm whether the pivot stands or was abandoned, make `HOME.md`/`INDEX.md`/`archive/README.md` agree with the model actually being executed, and log the resolution in `company/decisions/`.

### 2. CARRIED — `export/nariway-public.json:11237` still blends three non-comparable wealth-transfer figures into one number.
Still reads `"value": "~$31T+"` with source line `"wealth-research (Cerulli / UBS / Knight Frank)"` — the exact mixing `claims-register.md` C36 (and now C100-C101, this window's own new Knight Frank/UBS entries) exists to forbid: Deloitte/ArtTactic's ~$31T decade/global figure (C1's input), Cerulli's $124T US-only/2048 figure (C8), and Knight Frank, which publishes a UHNW population count (C100), not a transfer total, cited as if it were one source for one number.
**Fix:** replace with the Deloitte/ArtTactic-only $31T figure; drop Knight Frank from the source line regardless.

### 3. CARRIED AND WORSE — em dashes in live `public_*` export fields, now 18 files, five of them new this window.
Confirmed still unfixed, verbatim, in the 13 files named in every prior audit: `cases/art-car-museum.md`, `cases/fresno-metropolitan-museum.md`, `cases/hsbc-art-collection.md`, `cases/lee-kun-hee-collection.md`, `cases/malba-costantini.md`, `cases/monte-dei-paschi-collection.md`, `cases/mowaa.md`, `cases/sakip-sabanci-museum.md`, `cases/schnitzer-family-foundation.md`, `cases/standard-bank-art-collection.md`, `cases/unicredit-art-collection.md`, `cases/yemisi-shyllon-museum-of-art.md`, `cases/instituto-moreira-salles.md`. New this window, in `public_*` fields of cases added since the last audit: `cases/afkhami-foundation-iii-museum.md:20` (`public_name`), `cases/agadir-museum-of-art.md:30` (`public_origin`), `cases/mathaf-arab-museum-modern-art.md:27` (`public_size`), `cases/rosenwald-collection-nga-loc.md:23,25` (`public_structure`, `public_size`), `cases/soane-museum.md:19,33` (`public_status_text`, `public_origin`). This is the pattern actively reproducing itself in new content, not just carried debt — the same failure mode already flagged for the manuscript (item 6) is now also true here.
**Standard violated:** `[[voice]]`/`[[ai-tells]]`, no em dashes, applied to public-facing copy per QA remit (d).
**Fix:** fix all 18 files' `public_*` fields in one pass and regenerate the export. A pre-commit grep for em dashes across `public_*` lines, or a step in the case-coding routine that checks new `public_*` fields against `[[ai-tells]]` before the file is saved, would stop this recurring every research run.

### 4. CARRIED — `cases/kenneth-c-griffin-collection.md` still states a chain of dollar figures with zero inline sourcing.
The "Confirmed holdings" list (de Kooning $300M, Pollock $200M, Johns $80M, Basquiat >$100M, Cézanne ~$60M, Richter $46M, the Constitution $43.2M, the Stegosaurus $44.6M) still carries no per-figure `[source: URL; confidence: tier]` tag, only a prose parenthetical naming the deal/year and a blanket `public_sources` list at the bottom of the frontmatter. `report-dataset.md` still counts this file as a numbered, coded row.
**Fix:** add a source/confidence tag to each figure, or downgrade `verification` until it's done.

### 5. CARRIED — "significant" as a prestige adjective for collections is still live in `company/positioning.md`, including its own approved example.
Unchanged at lines 8, 13, 34, 112, and the codified ✅ example itself at line 138.
**Standard violated:** `[[voice]]`'s explicit, non-negotiable craft standard; QA remit (d).
**Fix:** replace with "private art collections" / "collectors" at the live-copy instances and the approved example, then propagate downstream.

### 6. CARRIED AND WORSE — the manuscript's em-dash count has grown again, third consecutive audit (83 → 86 → 93).
`marketing/what-becomes-of-great-art-collections.md` now shows 93 em dashes (up from 86 at the last audit). This has grown every window since the item was first flagged, despite being named explicitly each time as a needed dedicated pass.
**Standard violated:** `[[voice]]` lines 26-27 (no em dashes, no colons in prose); `[[ai-tells]]`.
**Fix:** a dedicated pass across the whole manuscript is overdue — the line-by-line chase during research runs is not working, and the count is now net-positive on new content three audits running.

### 7. CARRIED — the LACMA construction-cost contradiction (C38 vs. an unregistered second figure) is still live and unreconciled.
`research/claims-register.md` C38 (unchanged): David Geffen Galleries "opened April 2026," cost "~$724M total," a closed, finished project. `research/market-intelligence.md:242` (unchanged): "LACMA's ongoing building project has grown from an initial ~$600M estimate to over $750M... with 2026 completion still the target" — an open, still-in-progress project. Both describe LACMA construction but cannot both be the same project as stated.
**Standard violated:** `claims-register.md`'s single-source/no-drift discipline; QA remit (c).
**Fix:** determine whether this is the same Geffen Galleries project (drop the stale $600-750M framing) or a distinct project (give it its own claims-register entry, clearly distinguished from C38).

---

## SHOULD-FIX

### 8. CARRIED — `constraints_documented` values still fall outside the field's own controlled vocabulary.
`case-template.md:23` still defines only `yes` · `no` · `partial` · `open`; the corpus still uses `n/a` and `unknown` for cases with no individual founder or no located instrument (confirmed again this run, e.g. `mathaf-arab-museum-modern-art.md`, `rosenwald-collection-nga-loc.md`, `agadir-museum-of-art.md` all correctly need a value the vocabulary doesn't have), unamended since first flagged.
**Fix:** amend `case-template.md` to add `n/a` and `unknown` to the vocabulary, or remap existing rows to the four permitted values.

### 9. CARRIED — the Fisher/SFMOMA LinkedIn post still collapses the 720+ vs. ~1,100-works distinction.
`marketing/linkedin-posts.md:48` and `:230` unchanged: "more than a thousand works" leads directly into (or stands beside) the SFMOMA hundred-year-loan framing, reading as if the whole collection was loaned. `claims-register.md` C53 and `cases/fisher-sfmoma.md` both specify only 720+ of ~1,100 works are the SFMOMA-loaned subset.
**Fix:** state the 720+ figure or drop "more than a thousand" from the lead-in before this post is scheduled.

### 10. CARRIED — `marketing/website.md` still diverges from `positioning.md`'s canonical copy without being marked as a deliberate variant.
The live-site bio wording ("In recent years, research and writing have become a greater focus of my work") still differs from the canonical Bio's wording ("Over time, research and writing became an increasingly important part of my work") with neither file flagging the other as authoritative.
**Fix:** reconcile, or explicitly mark the variant as deliberate, the way `linkedin.md`/`substack.md` already do.

### 11. CARRIED — `cases/cultural-museum-of-african-art.md` still states an unsourced superlative as fact.
`public_origin` still reads "one of the largest private African art collections in the US" with no attribution for the ranking claim.
**Fix:** attribute it ("press coverage described it as...") or drop "one of the largest."

---

## MINOR

### 12. CARRIED, unchanged this window — the `origin` frontmatter field still spans 7 raw values.
Tally unchanged from the last audit: `private-individual` (59) · `corporate` (23) · `private` (14) · `individual` (8) · `artist` (7) · `private individual` (6) · `institutional` (3). None of this window's 7 new cases introduced a new variant.
**Fix:** consolidate the private-side spelling variants; document `artist` and decide on `institutional` in `case-template.md`.

### 13. CARRIED — corporate-continuity vocabulary still fragmented (`parent-entity-continuity` vs. `parent-entity-survival`).
**Fix:** adopt one term, add it to `case-template.md`.

### 14. CARRIED, and now three distinct mechanisms hitting the same gap — `primary_friction` has no authorized value for a case that isn't a funding shortfall but gets coded `funding-gap` anyway.
Kawamura (activist-investor capital-efficiency pressure), Rauschenberg (voluntary real-estate optimization from strength), and now this window's Kirkland Museum → Denver (a 2021 flood plus pandemic closure, explicitly not a described operating deficit) all flag the same schema gap independently, each with an honest caveat in the file rather than a silently-forced fit.
**Fix:** add at least one missing authorized value to `case-template.md`'s `primary_friction` list (e.g. a physical/external-shock value and a strategic-reallocation value, distinct from `funding-gap`).

### 15. CARRIED — `company/decisions/2026-08-14-board-membership.md` is still marked open.
Outcome line still reads `_open — shortlist being researched into [[board-opportunities]]._`
**Fix:** move out of `decisions/` until resolved, or mark plainly as in-progress.

---

## Checked, no issue found

- **The seven new cases this window** (`museum-of-photographic-arts-sdma.md`, `kirkland-museum-denver.md`, `soane-museum.md`, `rosenwald-collection-nga-loc.md`, `mathaf-arab-museum-modern-art.md`, `afkhami-foundation-iii-museum.md`, `agadir-museum-of-art.md`): every quantitative and governance claim carries an inline `[source: ...]`-style tag or an explicit `unknown`/`not-applicable`, with the reasoning for each stated rather than assumed. Ambiguous fields (Mathaf's insider governance overlap, Rosenwald's `not-applicable` vs. `unknown` financial fields, MOPA's founder-less coding) are flagged plainly rather than forced into a misleading value. None over-claims a pattern off this sample.
- **New claims-register entries C99-C102:** all four correctly sourced, carry explicit "do NOT" guardrails against merging non-comparable figures (C100 vs. C9; C102 vs. C85), and none is asserted as more than secondary/WebSearch-synthesized confidence.
- **The Part D disconfirmation entries this window** (HBC vs. MOWAA carried from last window; Soane vs. Gardner; Rosenwald vs. the Botero/Elliott/Mellon chain): correctly framed as sharpening or testing an existing hypothesis, not as new settled findings.
- **CRM (Ian Silverstein) and events-radar updates:** internal working notes, not public copy — sourced where they cite outside facts (event dates, venues), and honest about relationship status ("early, so not yet warm, but real, not inferred").

---

**Counts:** 7 critical (7 carried, 2 worse / grown) / 4 should-fix (4 carried) / 4 minor (4 carried, 1 with new supporting instances).
