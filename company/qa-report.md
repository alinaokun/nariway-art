# QA Report — 2026-09-05 (post commit f7e544d, 47th research run)

**Verdict:** Not clean, and getting worse, not better. All 7 CRITICAL and 4 SHOULD-FIX items from the 2026-09-04 audit (`5c633de`) remain open, byte-for-byte unfixed in every case checked. Two of them grew wider with content added since: the em-dash defect in public-facing frontmatter picked up a new instance (`fresno-metropolitan-museum.md`, coded today), and the manuscript's live prose picked up two more em-dash violations (in §3 and §4.3, both added by today's and yesterday's research runs, not the exempt changelog). The four newly-coded cases this run (DePaul, Zeitz MOCAA, Fondation Louis Vuitton, Fresno Met) are themselves clean on sourcing and controlled vocabulary. No item from the prior report was resolved.

---

## CRITICAL

### 1. CARRIED, now unresolved across at least four consecutive audits — the "professional-services pivot" contradicts the entire body of work this vault produces daily.
`INDEX.md:3`'s migration banner (dated 2026-08-27) and `archive/README.md:5-14` both state Nariway pivoted away from the research/advisory/collector model to "a specialist professional-services firm for estate attorneys and fiduciaries," and both name three archived documents plus a memory file as the current source of truth. `marketing/linkedin-posts.md:3` still cites the archived `Nariway_Company_Positioning_and_Operating_Brief_Aug_30_2026.md`. Meanwhile, every research run since (dozens of commits, through today) has continued to build exactly the model archive/README.md says was retired: `company/positioning.md` (actively maintained, last substantive dated language 2026-08-19/20, describes "research and advisory for private art collections," an HBR classification, a public bio), `research/claims-register.md` (92 entries, most recent dated today), `cases/report-dataset.md` (155 coded cases), and the manuscript, none of which shows any sign of the stated pivot. Either the pivot was reversed without updating `INDEX.md`/`archive/README.md`, or two incompatible operating models are both being maintained as "current" at once. This is the single most consequential inconsistency in the vault: it means a session or person landing on `INDEX.md` first is told to disregard the very files (`positioning.md`, `claims-register.md`, `report-dataset.md`) every other standard this audit checks treats as canonical.
**Standard violated:** `[[positioning]]`'s single-source rule; QA remit (e) and (f).
**Fix:** this needs Alina's decision, not an editorial one — confirm whether the pivot stands or was abandoned; whichever it is, make `INDEX.md` and `archive/README.md` agree with the model actually being executed, and log the resolution in `company/decisions/`.

### 2. CARRIED — `export/nariway-public.json:8710` and `content/content.json:54` still blend three non-comparable wealth-transfer figures into one number.
Both still read `"value": "~$31T+"`, `"source": "wealth-research (Cerulli / UBS / Knight Frank)"` — the exact mixing `claims-register.md` C36 exists to forbid (Deloitte/ArtTactic's ~$31T decade/global figure, Cerulli's $124T US-only/2048 figure, and Knight Frank, which publishes no transfer total at all, attributed as one source to one number). `content.json` now adds a `"verify": true` flag and a "sources and window vary" caveat, a partial softening, but the underlying figure and the false joint attribution are unchanged.
**Fix:** replace with the Deloitte/ArtTactic-only $31T figure (C1's input), or the already-drafted GWT figures in `marketing/gwt-content-draft.md`; drop Knight Frank from the source line regardless, since it has no transfer-total figure to contribute.

### 3. CARRIED and WIDER — em dashes in live `public_*` export fields, now 16+ instances across 13 files, one new today.
Still unfixed, verbatim: `cases/art-car-museum.md:29`, `cases/hsbc-art-collection.md:35`, `cases/lee-kun-hee-collection.md:35-36`, `cases/malba-costantini.md:21`, `cases/monte-dei-paschi-collection.md:21,33,34`, `cases/mowaa.md:28,32`, `cases/sakip-sabanci-museum.md:34`, `cases/schnitzer-family-foundation.md:35`, `cases/standard-bank-art-collection.md:34`, `cases/unicredit-art-collection.md:24`, `cases/yemisi-shyllon-museum-of-art.md:32`. **New this run:** `cases/fresno-metropolitan-museum.md:30` (`public_period: N/A — a general survey collection...`), coded today in commit `45c0d29`. The three other new cases this run (`depaul-art-museum.md`, `zeitz-mocaa.md`, `fondation-louis-vuitton.md`) are clean.
**Standard violated:** `[[voice]]`/`[[ai-tells]]`, no em dashes, applied to public-facing copy per QA remit (d).
**Fix:** fix all instances in one pass and regenerate the export. A pre-commit grep for em dashes in `public_*` lines would stop this recurring case by case — this is the second consecutive run to add a fresh instance on top of an unfixed backlog.

### 4. CARRIED — `cases/kenneth-c-griffin-collection.md` still states a chain of dollar figures as fact with zero sourcing.
Still zero `[source:`/`confidence:` tags in the entire file (confirmed again this run: `grep -c` returns 0); the "Confirmed holdings" list (de Kooning $300M, Pollock $200M, Johns $80M, Basquiat >$100M, Cézanne ~$60M, Richter $46M, the Constitution $43.2M, the Stegosaurus $44.6M) remains untagged despite `verification: spot-verified` in frontmatter.
**Fix:** add `[source: URL; confidence: tier]` to each figure, or downgrade `verification` until it's done.

### 5. CARRIED — "significant" as a prestige adjective for collections is still live in `company/positioning.md`, including its own approved example.
Unchanged at lines 8 (live vision paragraph), 13, 34 (live Contact copy), 112 (live LinkedIn bio), and 138 (✅ codified as an approved usage example).
**Standard violated:** `[[voice]]`'s explicit, "non-negotiable" craft standard; QA remit (d).
**Fix:** replace "significant" with "private art collections" / "private collections" at the live-copy instances and the approved example, then propagate to nariway.com and LinkedIn.

### 6. CARRIED and WIDER — the manuscript (`marketing/what-becomes-of-great-art-collections.md`) still carries the em-dash/colon violations flagged last run, plus two new ones added by the two most recent research runs, inside the live reading draft (§3, §4.3 — not the exempt changelog below line 529).
The six sentences flagged 2026-09-04 (§3, Corcoran/PMA/AAM section) remain unfixed verbatim. **New this run:** line 99 (§3's dataset-size footnote, added `2b79fb8`/`45c0d29`): *"...no rates are published off a non-random sample — see this section's own closing paragraph..."*; line 388 (§4.3 Box 3, added `2b79fb8`): *"...its first disclosed secured borrowing (C91) — a reminder that 'platform risk'..."*.
**Standard violated:** `[[voice]]`/`[[ai-tells]]` — no em dashes, no colons in prose.
**Fix:** rewrite with commas/restructuring; no content change needed.

### 7. CARRIED — the LACMA construction-cost contradiction (C38 vs. an unregistered second figure) is still live and unreconciled.
`research/claims-register.md` C38 (unchanged): LACMA's David Geffen Galleries "opened April 2026," cost "~$724M total." `research/market-intelligence.md:226` (unchanged): "LACMA's ongoing building project has grown from an initial ~$600M estimate to over $750M... with 2026 completion still the target." One says the building already opened at a fixed cost; the other says a LACMA project is still under construction targeting 2026. Not folded into the manuscript this run (the two new institutional-economics additions this run — C88, C89 — don't touch it), but the underlying contradiction between the two research files is unchanged.
**Standard violated:** `claims-register.md`'s single-source/no-drift discipline; QA remit (c).
**Fix:** determine whether this is the same Geffen Galleries project (drop the stale $600-750M framing) or a distinct LACMA project (give it its own claims-register entry, clearly distinguished from C38).

---

## SHOULD-FIX

### 8. CARRIED — `cases/report-dataset.md`'s primary-verification backlog still reuses numbers 61-67 across two separate lists.
Unchanged since last audit; the running-count prose was never reconciled against the duplication.
**Fix:** renumber the backlog list sequentially in one pass; consider deriving the count programmatically.

### 9. CARRIED — the Fisher/SFMOMA LinkedIn post still collapses the 720+ vs. ~1,100-works distinction.
`marketing/linkedin-posts.md:47-51` unchanged: "more than a thousand works" leads directly into the SFMOMA 100-year-loan sentence, reading as if the whole collection was loaned. `claims-register.md` C53 and `cases/fisher-sfmoma.md` both specify only 720+ of ~1,100 works are the SFMOMA-loaned subset.
**Fix:** state the 720+ figure or drop "more than a thousand" from the lead-in before this post is scheduled.

### 10. CARRIED — `marketing/website.md` still carries the same three undocumented divergences from `positioning.md`.
Unchanged: the file's own "reconcile later" note (line 16) is still unresolved with no owner or date; the reported live bio still differs in wording from the canonical Bio with neither marked authoritative; the alinaokun.com "Current" section phrasing still isn't reflected in or flagged against `positioning.md`.
**Fix:** reconcile or explicitly mark each variant as deliberate, the way `linkedin.md`/`substack.md` already do.

### 11. CARRIED — `cases/cultural-museum-of-african-art.md` still states an unsourced superlative as fact.
`public_origin:35` still reads "one of the largest private African art collections in the US" with no source or attribution for the ranking claim.
**Standard violated:** `[[voice]]`'s evidence-discipline principle.
**Fix:** attribute it ("press coverage described it as...") or drop "one of the largest."

---

## MINOR

### 12. CARRIED, grown again — the `origin` frontmatter field now spans 7 raw values, still drifting.
Current tally: `private-individual` (42) · `corporate` (19) · `private` (14) · `private individual` (6, up from 3) · `individual` (5) · `artist` (5) · `institutional` (3, up from 1 — two of this run's new cases, `depaul-art-museum.md` and `fresno-metropolitan-museum.md`, used it).
**Fix:** consolidate the private-side spelling variants; document `artist` and decide on `institutional` in `case-template.md`.

### 13. CARRIED — corporate-continuity vocabulary still fragmented.
`bank-of-america-collection.md`, `credit-suisse-ubs-collection.md`, `deutsche-bank-collection.md`, `jpmorgan-chase-collection.md`, `ubs-art-collection.md` use `parent-entity-continuity`; `enron-art-collection.md` and `lehman-brothers-collection.md` use `parent-entity-survival` for the same concept.
**Fix:** adopt one term, add it to `case-template.md`.

### 14. CARRIED — `primary_friction` schema gap, still self-flagged in the same three files.
`cases/benini.md` (coded `unknown`, a different issue — no cause found, correctly coded), `cases/rauschenberg-foundation-hq.md`, and `cases/unicredit-art-collection.md` still independently flag the same missing controlled-vocabulary value for "voluntary reallocation/succession-driven reversal from a position of strength," not forced into an ill-fitting label in any of the three.
**Fix:** add the missing authorized value to `case-template.md`.

### 15. CARRIED — `company/decisions/2026-08-14-board-membership.md` is still marked open.
Outcome line still reads `_open — shortlist being researched into [[board-opportunities]]._`
**Fix:** move out of `decisions/` until resolved, or mark plainly as in-progress.

### 16. CARRIED, wider — `research/estate-transition-synthesis.md` still cites a stale case count, now further off.
Line 14 still states "141 significant collection transitions," now 14 cases stale against the current 155. Still explicitly internal/not-for-publication and not used for any rate calculation, so still not a standards violation, just a live inconsistency.
**Fix:** update on next touch of the file; no urgency.

---

## Checked, no issue found
- **This run's four new cases** (`depaul-art-museum.md`, `zeitz-mocaa.md`, `fondation-louis-vuitton.md`, `fresno-metropolitan-museum.md`, aside from the one em-dash instance in #3): every quantitative and governance field carries a source and confidence tag or an explicit `unknown`; `net_assets_to_opex_ratio` correctly marked `not computable` where no dedicated balance sheet exists (DePaul) rather than guessed; no field tagged `primary`/`primary-verified` on secondary-sourced facts; controlled-vocabulary fields all use authorized values.
- **`report-dataset.md` diff (Batch 47):** case count recount (151→155) is transparent and matches the manuscript and `research-program.md`; framing ("no rates published off it") retained.
- **Claims-register addition C92:** correctly distinguished from the already-canonical C23/C24 (the file's own process note describes catching and correcting a near-duplicate before publishing); sourced with a confidence tag.
- **`what-we-now-believe.md`'s new disconfirmation entries (Zeitz MOCAA governance-under-strain test, Fresno Met H6/H8 replication):** correctly hedged, explicit unknowns sections, no overgeneralization from a single case.
- **`cases/candidate-universe.md` diff:** appropriately hedged as a pre-coding leads table.

---

## Resolved since the 2026-09-04 audit
None. All 7 critical and 4 should-fix items from the prior report remain open; two grew wider with new content.

---

**Counts:** 7 critical (7 carried, 0 new) / 4 should-fix (4 carried, 0 new) / 5 minor (5 carried, 0 new).
