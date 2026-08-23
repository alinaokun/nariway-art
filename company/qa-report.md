# QA Report — 2026-08-23

**Verdict:** Not clean. Four of last run's five CRITICALs are now genuinely fixed (verified independently, not just trusted from the commit message), but three new CRITICALs surfaced in work committed since, one of them inside the live public export itself. Case-level sourcing discipline is mostly holding across the new India/corporate/bulk-verify batch, with a handful of controlled-vocabulary breaches and two cases where `public_verified: true` was set on admittedly-unresearched stubs.

---

## CRITICAL

### 1. NEW — `export/nariway-public.json:4374-4376` and `content/content.json:54` misattribute the $31T Deloitte figure to Cerulli/UBS/Knight Frank and blend three non-comparable wealth-transfer totals into one number, in the live public export.
The fact tile reads: `{"value": "~$31T+", "label": "Projected global wealth transfer over the coming decade (order of magnitude; sources and window vary)", "source": "wealth-research (Cerulli / UBS / Knight Frank)"}`. Claims-register C36 exists specifically to stop this: Deloitte/ArtTactic's ~$31T (C1's underlying input, a decade horizon) is a different figure from Cerulli's $124T (US-only, through 2048, C8) and UBS's ~$83T (global, 20-25 years); C36 states they "must not be added together, rounded into one another, or cited as convergent evidence for a single figure." This tile takes the $31T number, attributes it to sources that didn't produce it (Knight Frank doesn't even publish a wealth-transfer total, only UHNWI population counts per C34), appends a "+" implying it as a floor toward the larger figures, and hedges with "sources and window vary" instead of separating them. This is the most severe finding in this run because `export/nariway-public.json` is what the live site actually consumes, not a draft.
**Fix:** change the fact to Deloitte/ArtTactic's ~$31T specifically, sourced to Deloitte/ArtTactic and labeled as C1's underlying input. If Cerulli's $124T or UBS's ~$83T are wanted as public facts, add them as separate, correctly-sourced tiles rather than one merged number.

### 2. NEW — `cases/terra.md` and `cases/di-rosa.md` carry `public_verified: true` while each file's own body says the facts are still unverified.
Both files set `public_verified: true` in frontmatter, the accuracy gate case-template.md defines as "the public-facing claims... confirmed against the institution's own site or reputable sources." Neither file contains a single `[source:]` tag. `terra.md`'s own body reads "**Verify first:** dates, the nature of the litigation, and where works ultimately went." `di-rosa.md`'s own body reads "**Verify first:** the 'campus for sale' and deaccessioning claims are provisional, confirm against primary sources before drawing lessons" — yet its `public_status_text` and `public_origin` frontmatter assert the campus-for-sale/deaccessioning narrative as settled fact. Standard violated: case-template.md's public-projection accuracy gate, and quality-assurance.md's sourcing rule (no bare claim presented as fact with no source).
**Fix:** revert `public_verified` to `false` on both files until the verification the files themselves call for is actually done.

### 3. NEW — `finance/collection-futures-study.md:28` presents a fabricated line as a real buyer's words.
Quote: *"In the buyer's words, 'I understand my options and I am making this decision on purpose.'"* No buyer said this. `finance/problem-discovery.md`'s conversation log shows no completed discovery conversation about this offer, and H7B (willingness to pay) is explicitly "Untested" per research-program.md. The sentence sits inside a section labeled as hypotheses to be tested, but the quotation-mark framing ("in the buyer's words") reads as captured testimony, not an authored hypothesis, and risks being cited downstream as if it were evidence a real prospect said this.
**Fix:** reword without quotation marks, e.g. "the ideal outcome, in the buyer's terms, would sound like..." so it can't be mistaken for a real quote.

---

## SHOULD-FIX

### 4. NEW — `finance/problem-discovery.md:92` and `finance/business-model-ledger.md:19` still instruct a tiered paid "Orientation" front door that commit 50cb4cd explicitly killed the same day.
`problem-discovery.md:92`: *"The first paid engagement is now designed in full: [[collection-futures-study]] (a tiered Orientation → full Collection Futures Study)... the Orientation tier is what gets named first."* `business-model-ledger.md:19`: *"Now designed in full: [[collection-futures-study]] (tiered Orientation → full study, the prop for discovery)."* Commit 50cb4cd ("Offer design v0.2") dropped the paid tier in favor of a free scoping conversation; these two files, which double as the actual playbook for running a real discovery conversation, were never updated. Standard violated: single source of truth (quality-assurance.md #4) — both paraphrase `collection-futures-study.md`'s structure instead of linking to it, and the paraphrase is now wrong. This is the one with real-world bite: followed as written, Alina would misstate Nariway's own offer to a live prospect.
**Fix:** update both to the v0.2 structure (free scoping conversation, single-tier study fee named only once a real situation surfaces), or drop the parenthetical description and just link.

### 5. STILL BROKEN (carried) — `marketing/what-becomes-of-great-art-collections.md:173` still cites "Table 1" for two figures Table 1 doesn't contain.
*"...alongside the ~$31T (Deloitte, Table 1) and $124T (Cerulli, Table 1) figures already used here."* Table 1 (lines 59-66) holds $992B, $2.56T→$3.47T, $54T, 72%, 80%, 51% — neither $31T nor $124T. The surrounding prose now correctly explains the C1/C8 mapping, but the wrong parenthetical tags were left standing next to the correction.
**Fix:** delete "(Deloitte, Table 1)" and "(Cerulli, Table 1)"; keep only the correct C1/C8 framing already present nearby.

### 6. STILL BROKEN (carried, now worse) — the primary-verification backlog is still growing unbounded, `Spot-verified` is still undefined, and `case-template.md` now contradicts itself on the export gate.
`report-dataset.md:7`: the backlog is now **51 items**, up from 47/41/38/35/27 across prior runs, with no ceiling or pace. `case-template.md:9` still lists `Spot-verified` as an allowed `verification_status` value with no definition anywhere in the file, even though 69 of 79 case files carry it. New this run: `case-template.md:34` states the export gate is `public_page_eligible` AND `public_verified`, explicitly **not** the internal `verification` tag, while `case-template.md:50` still says a case is "held from the live export until its figures reach `verification: primary-verified`" — directly contradicting its own line 34, and no case file carries `primary-verified` (0 of 79).
**Fix:** define `Spot-verified`; delete or rewrite line 50 to match line 34's actual gate.

### 7. STILL BROKEN (carried) — `marketing/website.md` still asserts the canonical Bio is live with wording that doesn't match, and still instructs overwriting canonical copy.
Line 21 quotes the live bio as *"In recent years, research and writing have become a greater focus of my work"*; `positioning.md:22`'s canonical Bio reads *"Over time, research and writing became an increasingly important part of my work."* Line 16 still reads *"Align positioning to the live copy when convenient"* — but positioning.md's own hero/section capture already matches the live site elsewhere, so following this note would overwrite canonical copy with stale text.
**Fix:** reconcile the Bio wording against the actual live page; delete or narrow line 16's instruction to the one real open item (replacing the third-person site bio with the canonical first-person one, already tracked at positioning.md:39).

### 8. STILL BROKEN (carried) — `market-intelligence.md` regressed: a new passage restates the superseded 65% IRS rate five lines before the correct figure.
Lines 190 and market-intelligence's other original instance are correctly fixed and cite C31 (63%, FY2023). But `market-intelligence.md:232`, added in the 2026-08-23 insurance-domain addendum, reads *"...the IRS Art Advisory Panel's **65% adjustment rate**..."* with no supersession note, contradicting the correct 63% figure at line 237 of the same file.
**Fix:** add the same "superseded, see C31" flag used at line 190.

### 9. STILL BROKEN (carried) — `marketing/substack-notes-queue.md` still ends two Notes on a manufactured conclusion, and `ai-tells.md` incorrectly claims this is fixed.
Line 14 (Rockwell): *"The covers everyone remembers as pure comfort were made by a man in real pain."* Line 41 (Magritte): *"He wanted you to stand in front of a picture and never be sure what it meant."* Both restate the antithesis-kicker pattern `voice.md` bans ("if a closing line explains what the story means, cut it and let the last fact land"). `ai-tells.md:14` says *"already fixed in the Notes"* — that claim is inaccurate for at least Rockwell.
**Fix:** cut both closing sentences, end on the prior concrete fact; correct ai-tells.md's claim once actually fixed.

### 10. NEW — five case files assert coded values outside case-template.md's controlled vocabulary, in some cases naming the invented term explicitly before falling back.
- `cases/fisher-landau.md:45` — `founder_status_at_transition: mixed` (only `living`/`deceased` are allowed; the file itself narrates living-at-2010-gift, deceased-at-2023-auction).
- `cases/rubin-museum.md:44` — `building_type: purpose-acquired-existing`, with the file's own text noting "coded closest to `adapted-other`" — i.e. it names the fallback and then doesn't use it.
- `cases/rauschenberg-foundation-hq.md:41` — `primary_friction: funding-optimization`, same pattern, self-noting the real fallback is `none-documented`.
- `cases/deutsche-bank-collection.md:52`, `cases/bank-of-america-collection.md:39`, `cases/enron-art-collection.md:38` — `founder_status_at_transition: n/a` / `survived_founder: n/a`, with Deutsche Bank additionally inventing `parent-entity-continuity: yes`. This is a pre-existing convention for corporate-origin cases, but case-template.md has never been amended to authorize it, and three more corporate cases landed on it this run.
**Fix:** for the first three, use the coded fallback the file already names in prose. For the corporate cases, either amend case-template.md to add an authorized corporate exception, or code `unknown` rather than an invented term.

### 11. NEW — `cases/hedreen-seattle-university.md` and `cases/jaipur-centre-for-art.md` still use the deprecated prose `## Public profile` body block and set no `public_verified` value, so they're silently excluded from export despite the commit that added them claiming "full public-projection layers."
case-template.md's current schema (added the same window, commit 6f76566) requires flat `public_*` frontmatter, calls the prose-block format "fragile," and `scripts/export_public.py` parses frontmatter only. Neither file sets `public_verified` at all.
**Fix:** migrate both to flat `public_*` frontmatter and set `public_verified` explicitly.

### 12. NEW — eight `public_*` frontmatter fields (export-bound content) contain em dashes, against the standing no-em-dash rule.
`bank-of-america-collection.md:23`, `ganz-collection.md:17`, `crystal-bridges.md:28`, `klesch-collection-birkbeck.md:33`, `las-vegas-museum-of-art.md:26`, `lucas-museum.md:22` (carried from last audit), `cam-raleigh.md:21`, `brauer-museum-valparaiso.md:27`.
**Fix:** rewrite each with a comma or period; en dashes for date/number ranges are fine and not flagged.

### 13. NEW — `institution-building/institution-building.md:31` uses the exact "endowment coverage" phrase claims-register C4 names as the thing not to say about McNay.
Quote: *"McNay already fed it (endowment coverage, self-perpetuating board, adaptive-reuse conversion)..."* C4: *"Do NOT say: 'McNay has 9.3× endowment coverage' (it's net assets, not endowment)."* Every case file checked correctly labels the ratio `[UPPER BOUND]` and disclaims "not endowment coverage" — this is the one place in the vault still using the forbidden phrase.
**Fix:** replace with "net-assets ratio (upper bound)."

### 14. STILL BROKEN (carried) — `crm/partners/Dawn Mari La Monica.md:36` still conflates C1 and C8, and `finance/cfo-brief.md:44` still watches a Table-1/C10 problem that's already fixed elsewhere.
Dawn La Monica line 36: *"the ~$1T art transfer is happening now, mostly to surviving spouses"* — fuses C1's decade-horizon art-and-collectibles figure with C8's US spousal-wealth figure into a claim neither source makes, despite the file being marked CLOSED. cfo-brief.md line 44's watch item describes the C10/Table-1 problem CRITICAL #4 already fixed in the prior audit round, so it's now pointing at a resolved issue.
**Fix:** correct or delete the La Monica line; update or retire the stale cfo-brief watch item.

### 15. NEW — `cases/report-dataset.md:298` states a percentage with a "holds" verdict, under-caveated relative to the file's own no-rates-off-this-set rule.
*"the governance-beats-endowment claim, counted for the first time, holds — 13/13 non-founder-sole cases survived their founder vs. 10/13 founder-sole cases (77%), n=26 testable."* The fuller write-up elsewhere in the same file (Batch 9) carries the required "not a population rate" caveat; this summary bullet doesn't.
**Fix:** either drop the "(77%)" and keep the raw counts, or append the same caveat inline.

---

## MINOR

### 16. CARRIED — `cases/mcnay.md` (`status: founder-review`, outside the numbered dataset) is still cited as a supporting example in `report-dataset.md` Pattern 1 ("McNay's self-perpetuating board").
**Fix:** fold McNay into the numbered dataset once it clears founder-review, or drop it from Pattern 1 until then.

### 17. CARRIED — `cases/moma.md` still carries two out-of-vocabulary values: `collection_coherence: absorbed`, `decision_owner: collective-founders-trustees`.
**Fix:** amend case-template.md to admit these, or remap with a flagged caveat.

### 18. CARRIED — the `origin` frontmatter field is still split three ways: `corporate` (11), `private` (8), `private-individual` (9), still undefined in case-template.md.
**Fix:** pick one value for the private side, normalize, and document the vocabulary.

### 19. LARGELY DEFUSED — `marketing/website.md`'s "(ready to publish)" interim-page section and its "Next step" (swap nariway.com to the interim page) are still literally present, but the file's line-28 blanket historical disclaimer now sits above both, warning a reader not to act on them.
**Fix:** low priority; strike the stale labels next time the file is touched.

### 20. NEW, worth a maintainer's eye — `cases/report-dataset.md` lines 181, 275, 305 describe Corcoran's ratio as "endowment coverage ~0.45x/0.5x." This is drawn from Corcoran's own disclosed endowment line (not its net-assets total), so it isn't the same error as finding #13, but it uses the same forbidden-sounding phrase and is worth confirming it isn't read as a C4-style violation by a future pass.

---

## Clean this run (checked, no findings)

- **CRITICAL #1-4 from the 2026-08-22 report** (hand-selected-sample rates, the transfer-scope-note 2.4x market-size error, the H1 "almost always" overclaim, the C10 "roughly doubled since 2011" restatement) — all four independently reverified as genuinely fixed, with the corrected text now consistent everywhere else those figures appear (Table 1, market-intelligence.md, positioning.md).
- **SHOULD-FIX #6 from the prior report** — `lucas-museum.md`'s `verification` value is now `provisional`, within vocabulary.
- **First paid engagement decision** (`0b0d554`/`50cb4cd`, `collection-futures-study.md`'s open-decisions section) — correctly marked open, explicitly states "H7B unproven, do not quote until discovery," no overclaim of proven demand or a client roster.
- **Every hypothesis restatement checked against research-program.md's H1-H8 status labels** (including the 2026-08-23 cloud-research H1 disconfirmation pass) — none stated more settled than its labeled status.
- **`net_assets_to_opex_ratio` across all 79 case files** — every instance labeled `[UPPER BOUND]`, `not computable`, or explicit `unknown`/`n/a` with a reason.
- **`verification_status` values across all sampled files** — Provisional/Spot-verified/Primary-verified only (the undefined-Spot-verified problem is a documentation gap, not a stray value — see finding 6).
- **report-dataset.md's case count** — 77 numbered entries (1-77, no gaps or duplicates), reconciled correctly against 79 total status-bearing files (77 coded + lucas-museum seed + mcnay founder-review).
- **C1, C6, C10, C23, C31 restated elsewhere in the vault** (positioning.md, pitch-deck.md, market-intelligence.md, the manuscript, content.json, export/nariway-public.json outside finding 1) — consistent with their claims-register canon.
- **company/decisions/** — no settled decision still marked open; the 2026-08-22 daily-check-in decision's open "Outcome (to fill in later)" is legitimate.
- **marketing/linkedin.md and marketing/substack.md** — still hold no local copy of live public text, point to positioning.md throughout.

---

**Counts:** 3 critical (all new) / 12 should-fix (4 carried, 8 new) / 5 minor (4 carried, 1 new note).
