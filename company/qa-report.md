# QA Report — 2026-09-07 (post commit dbd16b1, 179 coded cases)

**Verdict:** Not clean. All 7 CRITICAL items from the 2026-09-06 audit (`1feee5d`) remain open, unfixed, verified individually against current file content. One genuinely new structural gap surfaced this run: 8 cases added today (7 High Museum harvest cases plus Tanoto Art Foundation) are marked `status: coded` / `verification: spot-verified` but carry none of `case-template.md`'s controlled-vocabulary coded-header fields, including `survived_founder`, the field the template itself calls "the single most important." Today's other commits (the Silverstein/H9 addition, the law-firm market-intelligence entry) are clean and properly disciplined.

---

## CRITICAL

### 1. CARRIED, six consecutive audits — the "professional-services pivot" contradiction is unresolved.
`INDEX.md:3` and `archive/README.md:8-14` still state Nariway pivoted to "a specialist professional-services firm for estate attorneys and fiduciaries," naming three archived documents as current. Every research run since, including today's five commits, continues to build the model `archive/README.md` calls retired: `company/positioning.md`, `research/claims-register.md` (now 97 entries through C45+ and beyond), `cases/report-dataset.md` (179 coded cases), and the manuscript.
**Standard violated:** `[[positioning]]`'s single-source rule; QA remit (e) and (f).
**Fix:** needs Alina's decision, not an editorial one — confirm whether the pivot stands or was abandoned, make `INDEX.md`/`archive/README.md` agree with the model actually being executed, and log the resolution in `company/decisions/`.

### 2. CARRIED — `export/nariway-public.json:10833` still blends three non-comparable wealth-transfer figures into one number.
Still reads `"value": "~$31T+"` with source line attributing it to `"wealth-research (Cerulli / UBS / Knight Frank)"` — the exact mixing `claims-register.md` C36 exists to forbid (Deloitte/ArtTactic's ~$31T decade/global figure, Cerulli's $124T US-only/2048 figure, and Knight Frank, which publishes no transfer total at all, cited as one source for one number).
**Fix:** replace with the Deloitte/ArtTactic-only $31T figure (C1's input); drop Knight Frank from the source line regardless.

### 3. CARRIED — em dashes in live `public_*` export fields, same 13 files, no new instance in today's public_* fields specifically.
Confirmed still unfixed, verbatim, in: `cases/art-car-museum.md`, `cases/fresno-metropolitan-museum.md`, `cases/hsbc-art-collection.md`, `cases/lee-kun-hee-collection.md`, `cases/malba-costantini.md`, `cases/monte-dei-paschi-collection.md`, `cases/mowaa.md`, `cases/sakip-sabanci-museum.md`, `cases/schnitzer-family-foundation.md`, `cases/standard-bank-art-collection.md`, `cases/unicredit-art-collection.md`, `cases/yemisi-shyllon-museum-of-art.md`, `cases/instituto-moreira-salles.md`. Today's 8 new cases (Bunnen, Crawford, Rothko Foundation, Richman, Shaheen, Stein, Hahn, Tanoto) are clean in their `public_*` frontmatter, but 4 of them introduce the same em-dash pattern in the internal narrative's "One-line" summary instead (`cases/bunnen-collection-high-museum.md:46`, `cases/mark-rothko-foundation.md:46,48`, `cases/stein-collection-high-museum.md:46`, `cases/t-marshall-hahn-collection.md:46`) — narrative prose is not the exported layer, so not counted toward this item, but it is the same recurring habit landing one level up the file each time it gets fixed at the export layer.
**Standard violated:** `[[voice]]`/`[[ai-tells]]`, no em dashes, applied to public-facing copy per QA remit (d).
**Fix:** fix the 13 files' `public_*` fields in one pass and regenerate the export. A pre-commit grep for em dashes across the whole case file (not just `public_*` lines) would catch the pattern wherever it lands next.

### 4. CARRIED — `cases/kenneth-c-griffin-collection.md` still states a chain of dollar figures with zero inline sourcing.
The "Confirmed holdings" list (de Kooning $300M, Pollock $200M, Johns $80M, Basquiat >$100M, Cézanne ~$60M, Richter $46M, the Constitution $43.2M, the Stegosaurus $44.6M) still carries no per-figure `[source: URL; confidence: tier]` tag, only a blanket `public_sources` list at the bottom of the frontmatter. `report-dataset.md` still counts this file as a numbered, coded row (item 162+ per the 2026-09-06 integrity backfill).
**Fix:** add a source/confidence tag to each figure, or downgrade `verification` until it's done.

### 5. CARRIED — "significant" as a prestige adjective for collections is still live in `company/positioning.md`, including its own approved example.
Unchanged at lines 8, 13, 34, 112, and the codified ✅ example itself at line 138.
**Standard violated:** `[[voice]]`'s explicit, non-negotiable craft standard; QA remit (d).
**Fix:** replace with "private art collections" / "collectors" at the live-copy instances and the approved example, then propagate downstream.

### 6. CARRIED and now measured at true scale — the manuscript's em-dash and colon-in-prose violations are far more widespread than prior audits' spot checks suggested.
Line 99's em dash (case count now 168, still stale against the true 179 — see item 17 below) is unchanged. A full scan this run found **83 separate lines** in `marketing/what-becomes-of-great-art-collections.md` containing an em dash, not the one or two instances prior audits named — this is the flagship report manuscript, governed by `[[voice]]`'s "no em dashes" rule same as any public copy, per QA remit (d) and `ai-tells.md`'s explicit inclusion of "the report." Prior audits' conservative, spot-check-only framing understated the scope; this is a structural pattern across the manuscript's findings paragraphs, not a handful of stray instances.
**Standard violated:** `[[voice]]` lines 26-27 (no em dashes, no colons in prose); `[[ai-tells]]`.
**Fix:** this now needs a dedicated pass across the manuscript, not a line-by-line chase during each research run. Recommend Toi schedule one before the next public-facing use of this document, since fixing one instance per run while the count grows net-positive will never close the gap.

### 7. CARRIED — the LACMA construction-cost contradiction (C38 vs. an unregistered second figure) is still live and unreconciled.
`research/claims-register.md` C38 (unchanged): David Geffen Galleries "opened April 2026," cost "~$724M total," a closed, finished project. `research/market-intelligence.md:233` (unchanged): "LACMA's ongoing building project has grown from an initial ~$600M estimate to over $750M... with 2026 completion still the target" — an open, still-in-progress project. Both describe LACMA construction but cannot both be the same project as stated.
**Standard violated:** `claims-register.md`'s single-source/no-drift discipline; QA remit (c).
**Fix:** determine whether this is the same Geffen Galleries project (drop the stale $600-750M framing) or a distinct project (give it its own claims-register entry, clearly distinguished from C38).

---

## SHOULD-FIX

### 8. NEW — 8 cases added today are `status: coded` but carry none of `case-template.md`'s controlled-vocabulary coded-header fields, anywhere.
`cases/bunnen-collection-high-museum.md`, `crawford-collection-decorative-arts-high.md`, `mark-rothko-foundation.md`, `richman-collection-african-art-high.md`, `shaheen-collection-high-museum.md`, `stein-collection-high-museum.md`, `t-marshall-hahn-collection.md`, and `tanoto-art-foundation.md` each carry only the lightweight frontmatter (`pathway`, `founder_status`, `outcome`, `decision_owner`) plus the public-projection layer. None has `survived_founder` (Tanoto is the one exception, coded `not-yet-testable`), `durability_signal`, `governance_control_at_founding`, `building_type`, `collection_coherence`, or `primary_friction` anywhere in the file, and `cases/report-dataset.md` has not yet been updated to include these 8 as numbered rows (its header still reads 171, stale by 8), so the values do not exist in the vault's master synthesis either. This differs from the vault's older no-"Coded header"-section files (e.g. `corcoran-gallery.md`, `terra.md`), whose coded values live instead in `report-dataset.md`'s own numbered-row prose — that fallback does not apply here because these 8 rows do not exist there yet. `survived_founder` in particular is directly codeable for the 7 founder-deceased High Museum cases (each gift demonstrably outlived its founder inside a still-operating museum) and its total absence, rather than an explicit `unknown`, is exactly what `case-template.md`'s "a blank is never allowed" rule exists to prevent.
**Standard violated:** `case-template.md`'s binding rule (coded header is the compression of verified narrative content) and its "blank is never allowed" gaps-are-first-class-value rule.
**Fix:** either add the missing fields (at minimum `survived_founder`) to each of the 8 files, or add their rows to `report-dataset.md`'s numbered synthesis with the fields recorded there, before treating them as fully `coded`.

### 9. CARRIED — `constraints_documented` values still fall outside the field's own controlled vocabulary.
`case-template.md:23` still defines only `yes` · `no` · `partial` · `open`; the corpus still uses `n/a` and `unknown` for cases with no individual founder or no located instrument, values not on the list, unamended since flagged.
**Fix:** amend `case-template.md` to add `n/a` and `unknown` to the vocabulary, or remap existing rows to the four permitted values.

### 10. CARRIED — the Fisher/SFMOMA LinkedIn post still collapses the 720+ vs. ~1,100-works distinction.
`marketing/linkedin-posts.md:48` unchanged: "more than a thousand works" leads directly into the SFMOMA hundred-year-loan sentence, reading as if the whole collection was loaned. `claims-register.md` C53 and `cases/fisher-sfmoma.md` both specify only 720+ of ~1,100 works are the SFMOMA-loaned subset.
**Fix:** state the 720+ figure or drop "more than a thousand" from the lead-in before this post is scheduled.

### 11. CARRIED — `marketing/website.md` still diverges from `positioning.md`'s canonical copy without being marked as a deliberate variant.
The live-site bio wording ("In recent years, research and writing have become a greater focus of my work," line 21) still differs from the canonical Bio's wording ("Over time, research and writing became an increasingly important part of my work") with neither file flagging the other as authoritative; the "Current" section's descriptor phrasing (line 23) still isn't reconciled against or flagged from `positioning.md`'s own language-line guidance.
**Fix:** reconcile or explicitly mark each variant as deliberate, the way `linkedin.md`/`substack.md` already do.

### 12. CARRIED — `cases/cultural-museum-of-african-art.md` still states an unsourced superlative as fact.
`public_origin` still reads "one of the largest private African art collections in the US" with no attribution for the ranking claim.
**Fix:** attribute it ("press coverage described it as...") or drop "one of the largest."

---

## MINOR

### 13. CARRIED, grown again — the `origin` frontmatter field now spans 7 raw values, drifting further.
Current tally: `private-individual` (55, up from 46) · `corporate` (21) · `private` (14) · `individual` (8, up from 5) · `artist` (7, up from 5) · `private individual` (6) · `institutional` (3).
**Fix:** consolidate the private-side spelling variants; document `artist` and decide on `institutional` in `case-template.md`.

### 14. CARRIED — corporate-continuity vocabulary still fragmented (`parent-entity-continuity` vs. `parent-entity-survival`).
**Fix:** adopt one term, add it to `case-template.md`.

### 15. CARRIED — `primary_friction` schema gap, still missing the "voluntary reallocation/succession-driven reversal from a position of strength" value.
**Fix:** add the missing authorized value to `case-template.md`.

### 16. CARRIED — `company/decisions/2026-08-14-board-membership.md` is still marked open.
Outcome line still reads `_open — shortlist being researched into [[board-opportunities]]._`
**Fix:** move out of `decisions/` until resolved, or mark plainly as in-progress.

### 17. CARRIED, wider — case-count staleness in the manuscript and dataset header has grown to an 11-case gap.
The manuscript (`marketing/what-becomes-of-great-art-collections.md:99`) still states "currently 168," and `cases/report-dataset.md`'s own header states 171; the true coded count (`grep -l "^status: coded" cases/*.md`) is now **179**. Neither figure feeds a rate calculation, so this stays MINOR, but the gap is now wider than the last audit noted for a related file (`research/estate-transition-synthesis.md`, also still stale, unchanged).
**Fix:** update on next touch of each file; no urgency, but worth folding into whichever run next revises the manuscript's §3 opening paragraph.

---

## Checked, no issue found
- **Today's Silverstein/H9 addition** (`crm/partners/Ian Silverstein.md`, `research/market-intelligence.md`, `research/research-program.md`): correctly hedged throughout — explicitly labeled "a targeting insight, not a claims-register number," H9 marked "untested... NOT a reason to reposition," and the candidate-universe discipline honored (no corpus rows added without a documented transition).
- **The law-firm collector-demographic entry** (`research/market-intelligence.md:~555-569`): properly sourced to a named essay and author, flags the source as "a survey essay, not data," and its radar-triage section correctly withholds any collection from the corpus without a documented transition story.
- **Today's 8 new cases' `public_*` frontmatter and sourcing**: aside from items 3 and 8 above, every public-facing fact carries a source in the file's blanket `public_sources`/footer citation, consistent with the corpus's established convention for gift-type cases; no figure asserts more confidence than its source (Tanoto correctly holds `net_assets_latest`-type fields absent entirely rather than guessed, and explicitly separates the reported "$868M" site-sale figure from any build-cost claim in its own narrative note).
- **`museum-harvest.md` procedure**: confirms these harvest-sourced cases were intended to "pass the standard research and QA-verification gate before it publishes" — the gate named there is the same one item 8 above finds incompletely applied, not a separate, lighter-weight standard authorizing the gap.

---

## Resolved since the last audit
None. All items carried from the 2026-09-06 audit remain open.

---

**Counts:** 7 critical (7 carried, 0 new) / 5 should-fix (4 carried, 1 new) / 5 minor (5 carried, 0 new).
