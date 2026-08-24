# QA Report — 2026-08-24

**Verdict:** Not clean. All three CRITICALs from the last audit remain unfixed, and one MINOR-adjacent finding is escalated to CRITICAL this run because the vault's own export now confirms it reached the live public site, not just a draft file. One genuine fix landed (the Substack Notes closings). Case-level sourcing discipline across the three newest batches (Julia Stoschek, Art Bridges, AMOCA Cardiff) remains strong, and the new GWT (Great Wealth Transfer) content-architecture work in progress shows real rigor — it is, in effect, the correct design for fixing CRITICAL #1 below, just not yet applied to the live export.

---

## CRITICAL

### 1. CARRIED, unfixed — `export/nariway-public.json` and `content/content.json` still misattribute the $31T figure and blend three non-comparable wealth-transfer totals into one number, live on the public site.
The fact tile (`export/nariway-public.json:4729-4731`, `content/content.json:54`) still reads `"value": "~$31T+"`, `"source": "wealth-research (Cerulli / UBS / Knight Frank)"`. `research/claims-register.md` C36 exists specifically to stop this: Deloitte/ArtTactic's ~$31T (C1's input, decade horizon) is a different figure from Cerulli's $124T (US-only, through 2048, C8) and UBS's ~$83T (global, 20-25 years); C36 says they "must not be added together, rounded into one another, or cited as convergent evidence for a single figure." Knight Frank doesn't publish a wealth-transfer total at all (only UHNWI population counts, C34). Unchanged since the last audit.
**Note (mitigating, not a fix):** `marketing/kb-gwt-content-architecture.md`, drafted this run, designs this exact fact correctly — DP1 ($992B, cited to Deloitte alone) and DP2 (the three-estimate comparison table, explicitly "must NOT be summed") are built to C36's discipline and are marked "for review," not yet live. The correct design exists; it just hasn't replaced the bad tile in the actual export.
**Fix:** replace the export/content.json tile with DP1/DP2 as designed in the new architecture doc, or at minimum correct the $31T tile to cite Deloitte/ArtTactic alone.

### 2. CARRIED, unfixed — `cases/terra.md` and `cases/di-rosa.md` still carry `public_verified: true` while each file's own body says the facts are unverified.
`terra.md`: "**Verify first:** dates, the nature of the litigation, and where works ultimately went." `di-rosa.md`: "**Verify first:** the 'campus for sale' and deaccessioning claims are provisional, confirm against primary sources before drawing lessons." Both still set `public_verified: true` in frontmatter. Standard violated: `case-template.md`'s public-projection accuracy gate; `quality-assurance.md`'s sourcing rule.
**Fix:** revert `public_verified` to `false` on both until the verification each file itself calls for is done.

### 3. CARRIED, unfixed — `finance/collection-futures-study.md:28` still presents a fabricated line as a real buyer's words.
*"In the buyer's words, 'I understand my options and I am making this decision on purpose.'"* No buyer said this — H7B (willingness to pay) is explicitly "Untested" per `research-program.md`, and no completed discovery conversation about this offer exists in `finance/problem-discovery.md`'s log. Unchanged since the last audit.
**Fix:** reword without quotation marks so it reads as an authored hypothesis, not captured testimony.

### 4. ESCALATED from should-fix/minor — em dashes in `public_*` fields are confirmed live in `export/nariway-public.json`, a direct breach of `voice.md`/`ai-tells.md` in public-facing copy.
The last audit flagged 8 case files with em dashes in export-bound `public_*` frontmatter as a should-fix. This run confirms the mechanism actually fires: `export/nariway-public.json` contains the em dashes verbatim, e.g. line 420 `"focus": "Broad survey — painting, prints, photography, sculpture"` (Bank of America Collection), line 991 `"origin": "...Bentonville, Arkansas — a purpose-built Moshe Safdie complex..."` (Crystal Bridges), line 3842 `"currentState": "Sold at Christie's, New York, in 1997 for $206.5M — then a record for a single-owner auction."` (Ganz Collection), plus Lucas Museum and CAM Raleigh's `focus` fields. All eight source cases carry `public_page_eligible: true` AND `public_verified: true`, so this is not a hypothetical export, it is the actual live public payload. `voice.md`: "No em dashes. Use commas or restructure." This is exactly the category the vault's own quality-assurance.md names as critical: "a voice break in live public copy."
**Fix:** rewrite all eight `public_*` fields (`bank-of-america-collection.md`, `ganz-collection.md`, `crystal-bridges.md`, `klesch-collection-birkbeck.md`, `las-vegas-museum-of-art.md`, `lucas-museum.md`, `cam-raleigh.md`, `brauer-museum-valparaiso.md`) with commas or restructured sentences, then regenerate the export.

---

## SHOULD-FIX

### 5. CARRIED, unchanged — the primary-verification backlog keeps growing unbounded (57 items now, up from 51/47/41/38/35/27), and `case-template.md` still contradicts itself on the export gate.
`case-template.md:9` still lists `Spot-verified` as an allowed `verification_status` value with no definition anywhere in the file. `case-template.md:34` states the export gate is `public_page_eligible` AND `public_verified` — explicitly not the internal `verification` tag — while line 50 still says a case is "held from the live export until its figures reach `verification: primary-verified`," directly contradicting line 34 (no case file carries `primary-verified`; 0 of 83).
**Fix:** define `Spot-verified`; delete or rewrite line 50 to match line 34's actual gate.

### 6. CARRIED and worse — out-of-vocabulary coded values keep spreading, now with three mutually inconsistent invented terms for the same corporate-origin exception.
`fisher-landau.md:45` (`founder_status_at_transition: mixed`), `rubin-museum.md:44` (`building_type: purpose-acquired-existing`, self-noting the real fallback is `adapted-other`), `rauschenberg-foundation-hq.md:41` (`primary_friction: funding-optimization`, self-noting the fallback is `none-documented`) are all unchanged from the last audit. New this run: `enron-art-collection.md:38` recodes `survived_founder` as **`parent-entity-survival`** — a third distinct invented term, different from `deutsche-bank-collection.md` and `bank-of-america-collection.md`'s own `parent-entity-continuity`. The corporate-origin convention is not converging on one authorized value, it is fragmenting further with each new corporate case.
**Fix:** for the first three, use the fallback each file already names in its own prose. For the corporate cases, amend `case-template.md` to add one authorized value for this pattern before the next corporate case invents a fourth term.

### 7. CARRIED, unchanged — `cases/hedreen-seattle-university.md` and `cases/jaipur-centre-for-art.md` still use the deprecated prose `## Public profile` block and set no `public_verified` value, silently excluding them from export.
`case-template.md`'s schema requires flat `public_*` frontmatter and calls the prose-block format "fragile"; `scripts/export_public.py` parses frontmatter only.
**Fix:** migrate both to flat `public_*` frontmatter and set `public_verified` explicitly.

### 8. CARRIED, unchanged — `marketing/website.md` still quotes the live Bio with wording that doesn't match the canonical text, and still instructs overwriting canonical copy.
`website.md:21` quotes: *"In recent years, research and writing have become a greater focus of my work."* `positioning.md`'s canonical Bio reads: *"Over time, research and writing became an increasingly important part of my work."* `website.md`'s line "Align positioning to the live copy when convenient" still stands, which would overwrite the canonical text with this mismatched quote if followed literally.
**Fix:** reconcile the Bio wording against the actual live page; narrow the instruction to the one real open item already tracked (`positioning.md:39`, the third-person site bio still needing the canonical first-person swap).

### 9. CARRIED, unchanged — `research/market-intelligence.md:232` still restates the superseded 65% IRS Art Advisory Panel rate with no supersession flag, in a passage added after the correct 63%/C31 figure was already established elsewhere in the same file.
Line 232: *"...the IRS Art Advisory Panel's 65% adjustment rate)..."* with no "superseded, see C31" note, while lines 190, 237, and 283 of the same file all correctly cite 63%/C31.
**Fix:** add the same "superseded, see [[claims-register]] C31" flag used at line 190.

### 10. CARRIED, unchanged — `marketing/what-becomes-of-great-art-collections.md`'s C36 discussion still cites "(Deloitte, Table 1)" and "(Cerulli, Table 1)" for two figures Table 1 doesn't contain.
*"...alongside the ~$31T (Deloitte, Table 1) and $124T (Cerulli, Table 1) figures already used here."* Table 1 holds $992B, $2.56T→$3.47T, $54T, 72%, 80%, 51% — neither raw $31T nor $124T appears there (those are the underlying inputs behind C1's $992B and C8's $54T respectively). The surrounding C36 discussion is otherwise correctly built.
**Fix:** delete the two wrong parenthetical tags; the correct C1/C8 framing already stated nearby doesn't need them.

### 11. CARRIED, unchanged — `crm/partners/Dawn Mari La Monica.md:36` still conflates C1 and C8 into a claim neither source makes.
*"the ~$1T art transfer is happening now, mostly to surviving spouses"* fuses C1's decade-horizon art-and-collectibles figure with C8's US spousal-wealth figure, in a file marked CLOSED.
**Fix:** correct or delete the line.

### 12. CARRIED, unchanged — `finance/problem-discovery.md:92` still instructs the old tiered paid "Orientation" front door that the offer redesign (v0.2) dropped.
*"...the Orientation tier is what gets named first."* `finance/business-model-ledger.md:19` was correctly updated this run to the v0.2 structure (free scoping conversation, single priced engagement named only once a real situation surfaces) — but `problem-discovery.md`, the file that actually scripts a live discovery conversation, was not. This is the one with real-world bite: followed as written, Alina would misstate Nariway's own offer to a live prospect.
**Fix:** update `problem-discovery.md:92` to the v0.2 structure, or drop the parenthetical and link to `collection-futures-study.md` instead.

### 13. CARRIED, unchanged — `institution-building/institution-building.md:31` still uses the exact "endowment coverage" phrase `claims-register.md` C4 names as the thing not to say about McNay.
*"McNay already fed it (endowment coverage, self-perpetuating board, adaptive-reuse conversion)..."* C4: "Do NOT say: 'McNay has 9.3× endowment coverage' (it's net assets, not endowment)."
**Fix:** replace with "net-assets ratio (upper bound)."

---

## MINOR

### 14. CARRIED — `cases/report-dataset.md` Pattern 1's original prose still cites McNay ("McNay's self-perpetuating board") as supporting evidence, while `cases/mcnay.md` remains `status: founder-review`, outside the numbered dataset. The newer, fully-tabulated Pattern 14 (the file's own designated authoritative version) correctly excludes McNay already.
**Fix:** fold McNay into the numbered dataset once its research clears the bar, or strike it from Pattern 1's prose list until then.

### 15. CARRIED — `cases/moma.md` still carries two out-of-vocabulary values: `collection_coherence: absorbed`, `decision_owner: collective-founders-trustees`.
**Fix:** amend `case-template.md` to admit these, or remap with a flagged caveat.

### 16. CARRIED, growing — the `origin` frontmatter field is now split three ways across the case set (`corporate`: 11, `private`: 14, `private-individual`: 9), still undefined anywhere in `case-template.md`.
**Fix:** pick one value for the private side, normalize, and document it.

### 17. CARRIED — `marketing/website.md`'s "(ready to publish)" interim-page section and its "Next step" instruction are still literally present, though the file's own historical disclaimer sits above both.
**Fix:** low priority; strike the stale labels next time the file is touched.

### 18. CARRIED — `cases/report-dataset.md` (Corcoran, "endowment coverage fell below ~0.5x") uses the same forbidden-sounding phrase as finding #13, but is drawn from Corcoran's own disclosed endowment line rather than a net-assets total, so it isn't the same error. Worth a maintainer's eye, not a fix.

---

## Resolved since the last audit (noted, no action needed)

- **`marketing/substack-notes-queue.md`'s Rockwell and Magritte Notes are now genuinely fixed** — both closings were cut and now end on a concrete fact, matching `voice.md`'s no-manufactured-conclusion rule. The file's own note documents the fix landing 2026-08-24 in direct response to the last audit's finding, and `ai-tells.md`'s "already fixed in the Notes" claim is now accurate.
- **`finance/business-model-ledger.md`'s Collection Futures Study entry is now correctly updated to the v0.2 offer** (free scoping conversation, single priced engagement, "do not sell" discipline stated explicitly) — only its sibling file (`problem-discovery.md`, finding #12 above) still needs the same update.
- **The three newest case files** (`julia-stoschek-foundation.md`, `art-bridges-foundation.md`, `amoca-cardiff.md`) show clean sourcing: every quantitative field carries a source/confidence tag or explicit `unknown`, and each names a distinct, specific re-fetch target in the backlog rather than a vague placeholder.
- **`marketing/kb-gwt-content-architecture.md`** (new this run, "for review") independently reasons through the exact C1/C36 discipline CRITICAL #1 needs — a genuinely well-built draft, just not yet applied to the live export.
- **No settled decision found still marked open**, and no new claims-register drift found beyond the items already carried above.
- **`finance/cfo-brief.md`'s older C10/Table-1 "watch" entries (2026-08-19, 2026-08-20)** are dated rolling-journal entries from when that issue was genuinely open, not live stale watch items — correctly left as historical record now that C10 is fixed. Retracting the prior audit's characterization of this as a should-fix.

---

**Counts:** 4 critical (3 carried unfixed, 1 escalated from should-fix) / 9 should-fix (all carried) / 5 minor (all carried).
