# QA Report — 2026-09-08 (post commit b7bc184, 185 coded cases)

**Verdict:** Not clean. All 7 CRITICAL items from the 2026-09-07 audit (`993894d`) remain open, unfixed, verified individually against current file content. Two items resolved since the last audit (the 8-case coded-header gap; manuscript/dataset case-count staleness). No new critical issues surfaced in the intervening research runs (two "Cloud research" commits, 182→185 coded cases) — the three newest cases and the two new claims-register entries (C97, C98) are properly sourced, hedged, and disciplined.

---

## CRITICAL

### 1. CARRIED, seven consecutive audits — the "professional-services pivot" contradiction is unresolved.
`INDEX.md:3` and `archive/README.md:8-14` still state Nariway pivoted to "a specialist professional-services firm for estate attorneys and fiduciaries," naming three archived documents as current. Every research run since, including this window's two research commits, continues to build the model `archive/README.md` calls retired: `company/positioning.md`, `research/claims-register.md` (now 98 entries through C98), `cases/report-dataset.md` (185 coded cases), and the manuscript.
**Standard violated:** `[[positioning]]`'s single-source rule; QA remit (e) and (f).
**Fix:** needs Alina's decision, not an editorial one — confirm whether the pivot stands or was abandoned, make `INDEX.md`/`archive/README.md` agree with the model actually being executed, and log the resolution in `company/decisions/`.

### 2. CARRIED — `export/nariway-public.json:10833` still blends three non-comparable wealth-transfer figures into one number.
Still reads `"value": "~$31T+"` with source line attributing it to `"wealth-research (Cerulli / UBS / Knight Frank)"` — the exact mixing `claims-register.md` C36 exists to forbid (Deloitte/ArtTactic's ~$31T decade/global figure, Cerulli's $124T US-only/2048 figure, and Knight Frank, which publishes no transfer total at all, cited as one source for one number).
**Fix:** replace with the Deloitte/ArtTactic-only $31T figure (C1's input); drop Knight Frank from the source line regardless.

### 3. CARRIED — em dashes in live `public_*` export fields, same 13 files.
Confirmed still unfixed, verbatim, in: `cases/art-car-museum.md`, `cases/fresno-metropolitan-museum.md`, `cases/hsbc-art-collection.md`, `cases/lee-kun-hee-collection.md`, `cases/malba-costantini.md`, `cases/monte-dei-paschi-collection.md`, `cases/mowaa.md`, `cases/sakip-sabanci-museum.md`, `cases/schnitzer-family-foundation.md`, `cases/standard-bank-art-collection.md`, `cases/unicredit-art-collection.md`, `cases/yemisi-shyllon-museum-of-art.md`, `cases/instituto-moreira-salles.md`. No new instance introduced in this window's `public_*` fields specifically (the three new cases this window — Hudson's Bay, Kawamura, UC Irvine/OCMA — are clean in their public frontmatter).
**Standard violated:** `[[voice]]`/`[[ai-tells]]`, no em dashes, applied to public-facing copy per QA remit (d).
**Fix:** fix the 13 files' `public_*` fields in one pass and regenerate the export. A pre-commit grep for em dashes across `public_*` lines would catch the pattern before it ships again.

### 4. CARRIED — `cases/kenneth-c-griffin-collection.md` still states a chain of dollar figures with zero inline sourcing.
The "Confirmed holdings" list (de Kooning $300M, Pollock $200M, Johns $80M, Basquiat >$100M, Cézanne ~$60M, Richter $46M, the Constitution $43.2M, the Stegosaurus $44.6M) still carries no per-figure `[source: URL; confidence: tier]` tag, only a prose parenthetical naming the deal/year and a blanket `public_sources` list at the bottom of the frontmatter. `report-dataset.md` still counts this file as a numbered, coded row.
**Fix:** add a source/confidence tag to each figure, or downgrade `verification` until it's done.

### 5. CARRIED — "significant" as a prestige adjective for collections is still live in `company/positioning.md`, including its own approved example.
Unchanged at lines 8, 13, 34, 112, and the codified ✅ example itself at line 138.
**Standard violated:** `[[voice]]`'s explicit, non-negotiable craft standard; QA remit (d).
**Fix:** replace with "private art collections" / "collectors" at the live-copy instances and the approved example, then propagate downstream.

### 6. CARRIED and worse — the manuscript's em-dash and colon-in-prose count has grown again, and this window added a fresh instance in new findings prose, not just changelog text.
The em-dash count in `marketing/what-becomes-of-great-art-collections.md` rose from 83 (last audit) to **86**. Most of the growth is in changelog entries, but one is in newly added, publicly-readable findings prose from this window's own research run: "Some major art valuers are reportedly shutting down their own smaller lending operations in response — an early sign the art-secured lending market is stratifying into two tiers" (the new §4.3 paragraph on C98). The same paragraph also opens with a colon in prose ("The mechanism behind the divergence: the wider art market itself contracted..."), a second, distinct `[[voice]]` violation (line 27, "no colons in prose"). This is the manuscript actively re-introducing the pattern the standing item exists to stop, not merely carrying old debt.
**Standard violated:** `[[voice]]` lines 26-27 (no em dashes, no colons in prose); `[[ai-tells]]`.
**Fix:** this needs a dedicated pass across the manuscript, not a line-by-line chase during each research run — and research runs adding new findings paragraphs should self-check against `[[ai-tells]]` before folding prose into this file, since the gap is now growing net-positive on new content, not just carried debt.

### 7. CARRIED — the LACMA construction-cost contradiction (C38 vs. an unregistered second figure) is still live and unreconciled.
`research/claims-register.md` C38 (unchanged): David Geffen Galleries "opened April 2026," cost "~$724M total," a closed, finished project. `research/market-intelligence.md:233` (unchanged): "LACMA's ongoing building project has grown from an initial ~$600M estimate to over $750M... with 2026 completion still the target" — an open, still-in-progress project. Both describe LACMA construction but cannot both be the same project as stated.
**Standard violated:** `claims-register.md`'s single-source/no-drift discipline; QA remit (c).
**Fix:** determine whether this is the same Geffen Galleries project (drop the stale $600-750M framing) or a distinct project (give it its own claims-register entry, clearly distinguished from C38).

---

## SHOULD-FIX

### 8. CARRIED — `constraints_documented` values still fall outside the field's own controlled vocabulary.
`case-template.md:23` still defines only `yes` · `no` · `partial` · `open`; the corpus (checked across all coded files this run: 201 `no`, 60 `open`, 29 `partial`, 20 `n/a`, 17 `yes`, 17 `unknown`) still uses `n/a` and `unknown` for cases with no individual founder or no located instrument, values not on the list, unamended since flagged.
**Fix:** amend `case-template.md` to add `n/a` and `unknown` to the vocabulary, or remap existing rows to the four permitted values.

### 9. CARRIED — the Fisher/SFMOMA LinkedIn post still collapses the 720+ vs. ~1,100-works distinction.
`marketing/linkedin-posts.md:48` and `:230` unchanged: "more than a thousand works" leads directly into (or stands beside) the SFMOMA hundred-year-loan framing, reading as if the whole collection was loaned. `claims-register.md` C53 and `cases/fisher-sfmoma.md` both specify only 720+ of ~1,100 works are the SFMOMA-loaned subset.
**Fix:** state the 720+ figure or drop "more than a thousand" from the lead-in before this post is scheduled.

### 10. CARRIED — `marketing/website.md` still diverges from `positioning.md`'s canonical copy without being marked as a deliberate variant.
The live-site bio wording ("In recent years, research and writing have become a greater focus of my work," line 21) still differs from the canonical Bio's wording ("Over time, research and writing became an increasingly important part of my work") with neither file flagging the other as authoritative.
**Fix:** reconcile or explicitly mark the variant as deliberate, the way `linkedin.md`/`substack.md` already do.

### 11. CARRIED — `cases/cultural-museum-of-african-art.md` still states an unsourced superlative as fact.
`public_origin` still reads "one of the largest private African art collections in the US" with no attribution for the ranking claim.
**Fix:** attribute it ("press coverage described it as...") or drop "one of the largest."

---

## MINOR

### 12. CARRIED, grown again — the `origin` frontmatter field now spans 7 raw values, drifting further.
Current tally: `private-individual` (59, up from 55) · `corporate` (23, up from 21) · `private` (14) · `individual` (8) · `artist` (7) · `private individual` (6) · `institutional` (3).
**Fix:** consolidate the private-side spelling variants; document `artist` and decide on `institutional` in `case-template.md`.

### 13. CARRIED — corporate-continuity vocabulary still fragmented (`parent-entity-continuity` vs. `parent-entity-survival`).
**Fix:** adopt one term, add it to `case-template.md`.

### 14. CARRIED — `primary_friction` schema gap, still missing an authorized value for "activist-investor capital-efficiency pressure," now a second time (Kawamura Memorial DIC Museum this window recoded it as `funding-gap` with an explicit note that "the closest existing vocabulary value... undersells the mechanism," the same workaround flagged in a prior case).
**Fix:** add the missing authorized value to `case-template.md`.

### 15. CARRIED — `company/decisions/2026-08-14-board-membership.md` is still marked open.
Outcome line still reads `_open — shortlist being researched into [[board-opportunities]]._`
**Fix:** move out of `decisions/` until resolved, or mark plainly as in-progress.

---

## Checked, no issue found

- **The three new cases this window** (`hudsons-bay-company-collection.md`, `kawamura-memorial-dic-museum.md`, `uc-irvine-langson-ocma.md`): every quantitative and governance claim carries an inline `[source: URL; confidence: tier]` tag; unusual/ambiguous fields (e.g. `survived_founder: n/a` for corporate cases, HBC's schema-coverage gap for `decision_owner`) are explicitly flagged and reasoned through rather than forced into a misleading value.
- **The 8-case coded-header gap from the last two audits is resolved.** `mark-rothko-foundation.md`, `richman-collection-african-art-high.md`, `shaheen-collection-high-museum.md`, `stein-collection-high-museum.md`, `t-marshall-hahn-collection.md`, and `tanoto-art-foundation.md` all now carry `survived_founder`, `durability_signal`, `governance_control_at_founding`, `building_type`, `collection_coherence`, and `primary_friction`, added and dated with an explicit note tying the fix to the QA finding that surfaced it. `report-dataset.md`'s header count (185) matches a fresh `grep -l "^status: coded" cases/*.md` recount exactly, and the manuscript's case count (185) now matches both.
- **New claims-register entries C97 (museum-merger cluster) and C98 (art-finance margin-call mechanism):** both correctly sourced to named outlets, carry an explicit "do NOT" mis-citation guardrail, and neither overstates a hand-selected sample into a rate or population claim.
- **The Part D disconfirmation entries** (HBC vs. MOWAA; the Mellon/Congress and Artizon/Ishibashi cases against the founder-succession-collapse pattern): correctly framed as sharpening or testing an existing hypothesis, not as new settled findings.

---

## Resolved since the last audit

- **Item 8 (2026-09-07 audit): 8 cases missing controlled-vocabulary coded-header fields.** Fixed directly in each file, dated and cross-referenced to the QA finding.
- **Item 17 (2026-09-07 audit): case-count staleness in the manuscript vs. dataset header.** Both now read 185 and agree with the actual file count.

---

**Counts:** 7 critical (7 carried, 0 new) / 4 should-fix (4 carried, 0 new) / 4 minor (4 carried, 0 new).
