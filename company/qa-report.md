# QA Report — 2026-08-27

**Verdict:** Not clean. One new CRITICAL (a live canonical-number contradiction in the manuscript itself), the two longest-standing CRITICALs are unfixed for a **fifth** straight audit, and the em-dash defect this audit's own history has tracked for four audits gained an eleventh live instance rather than closing. Genuinely good news this run: the primary-verification backlog held flat at 67 across two full coding runs (98 → 101 cases) instead of growing, which resolves last audit's should-fix #5.

---

## CRITICAL

### 1. NEW — `marketing/what-becomes-of-great-art-collections.md:314` states the IRS Art Advisory Panel's superseded, incorrect FY2018 figures as current FY2023 fact, contradicting the very claims-register entry it cites.
The manuscript reads: *"In FY2023, the most recent year a public tally could be found, the Panel reviewed 251 items across 67 taxpayer cases, an aggregate claimed valuation of $360.9 million, and recommended adjusting **63%** of the items it reviewed, a net adjustment of –$64.6 million (C31)."* But `claims-register.md` C31 was corrected on 2026-08-24: those exact figures (251 items / 67 cases / $360.9M / 63% / –$64.6M) are explicitly flagged there as a **year misattribution** — they are the FY2018 numbers, not FY2023's. C31's real, verified FY2023 figures are **195 items across 37 taxpayer cases, $795,527,954 claimed, 103 items (53%) accepted, 92 items (47%) adjusted, net adjustment –$16,946,454**. The manuscript's own citation `(C31)` points to the entry that disproves its own sentence. This is a live claims-register/manuscript drift on a number the report treats as a settled, citable fact, not a working note. (For orientation: the file's changelog further down, at the 2026-08-20 entry, correctly describes the "63%, superseding the older ~65%/2012 figure" — that changelog line predates the 2026-08-24 correction and documents history accurately; it is only the manuscript body at line 314 that is wrong and current.)
**Fix:** replace line 314 with C31's real FY2023 figures (195 items / 37 cases / $795.5M claimed / 47% adjusted / –$16.9M net).

### 2. CARRIED (5th audit) — `export/nariway-public.json:5843` and `content/content.json:54` still misattribute the wealth-transfer figure to three non-comparable sources blended into one number, live on the public site.
Unchanged verbatim across five audits: both files still read `"value": "~$31T+"`, `"source": "wealth-research (Cerulli / UBS / Knight Frank)"`. `claims-register.md` C36 exists specifically to stop this: Deloitte/ArtTactic's ~$31T (C1's input, decade horizon, global) is a different figure from Cerulli's $124T (US-only, through 2048, C8) and UBS's ~$83T (global, 20-25 years); C36 says they "must not be added together, rounded into one another, or cited as convergent evidence for a single figure." Knight Frank doesn't publish a wealth-transfer total at all (only UHNWI population counts, C34). The fix has sat fully drafted in `marketing/gwt-content-draft.md` Block 3 for over a week, and the GWT page targeting this exact figure launches tomorrow (Aug 28) per the CMO steward's own brief.
**Fix:** replace the export/content.json tile with the GWT Block 2/3 figures (already drafted, correctly separated), or at minimum correct the `$31T` tile to cite Deloitte/ArtTactic alone.

### 3. CARRIED (5th audit) — `finance/collection-futures-study.md:28` still presents a fabricated line as a real buyer's words.
*"In the buyer's words, 'I understand my options and I am making this decision on purpose.'"* No buyer said this; H7B (willingness to pay) is explicitly "Untested" per `research-program.md`, and no completed discovery conversation matches this quote in `finance/problem-discovery.md`'s log. The surrounding section is honestly framed as hypothesis ("Buyer-backward... hypotheses, to be tested"); the quoted sentence is the one place that slips from hypothesis into invented testimony. This is now flagged independently by both the CFO steward brief (`finance/cfo-brief.md`, 2026-08-27: "This is the exact document that would go in front of Fanning's collector if that call happens... should be fixed today") and this audit, across four consecutive prior QA runs plus today's.
**Fix:** reword without quotation marks so it reads as an authored hypothesis of what success looks like, not captured testimony. This is a one-sentence edit with no dependency on any other unresolved question.

### 4. CARRIED, and worse — live public-facing em dashes now number **eleven**, up from ten last audit, with a third consecutive run adding a fresh instance instead of closing the category.
Confirmed still live in `export/nariway-public.json`: the eight cases named in the prior two audits (`bank-of-america-collection.md`, `ganz-collection.md`, `crystal-bridges.md`, `klesch-collection-birkbeck.md`, `las-vegas-museum-of-art.md`, `lucas-museum.md`, `cam-raleigh.md`, `brauer-museum-valparaiso.md`), plus last audit's two new instances (`bunker-artspace.md`, `petrucci-family-foundation.md`), plus a new one this run: `cases/cookie-factory-denver.md:23`, in the `public_structure` frontmatter field itself (`public_page_eligible: true`, `public_verified: true`): *"Privately owned and privately funded; deliberately not a 501(c)(3) nonprofit — no board, no fundraising, no donor competition."* `voice.md`: "No em dashes. Use commas or restructure," binding on public-facing copy per `ai-tells.md`. This is the third straight run in which brand-new coded cases ship a fresh public-field em dash despite two prior audits calling for exactly this defect to stop recurring, confirming the earlier audit's diagnosis: the em-dash check is not running against new `public_*` fields at write time, only caught retrospectively.
**Fix:** rewrite all eleven `public_*` fields with commas or restructured sentences, then regenerate the export. Given three consecutive recurrences, this now needs a mechanical pre-commit grep against new `public_*` fields, not another audit note — a fourth recurrence next run would indicate the fix instruction itself isn't being read, not just deprioritized.

---

## SHOULD-FIX

### 5. RESOLVED, noted — the primary-verification backlog held flat at 67 across two coding runs (98 → 101 cases), addressing last audit's should-fix.
Both `stieglitz-collection-fisk-crystal-bridges`/`rachofsky-warehouse-dallas`/`societe-generale-collection` (98-run) and `cookie-factory-denver`/`powder-art-foundation`/`ashbery-collection-flow-chart` (101-run) were correctly excluded from the backlog as structurally, not just currently, unverifiable, rather than added and left to sit. This is real triage discipline, not just luck; worth confirming it holds as coding continues toward 100+.

### 6. CARRIED — `marketing/what-becomes-of-great-art-collections.md:237` still cites "(Deloitte, Table 1)" and "(Cerulli, Table 1)" for two figures Table 1 doesn't contain.
Table 1 (line 57) holds $992B, $2.56T→$3.47T, $54T, 72%, 80%, 51%; neither the raw $31T nor $124T appears there (those are the underlying inputs behind C1's $992B and C8's $54T respectively, correctly explained in the surrounding prose). The parenthetical citations are simply wrong pointers. Unchanged since first flagged.
**Fix:** delete the two "(..., Table 1)" tags.

### 7. CARRIED — `case-template.md` still contradicts itself on the export gate, and `Spot-verified` remains undefined.
`case-template.md:9` lists `Spot-verified` as an allowed `verification_status` value with no definition anywhere in the file. Line 34 states the export gate is `public_page_eligible` AND `public_verified` (explicitly not the internal `verification` tag), while line 50 still says a case is held from export until `verification: primary-verified` — directly contradicting line 34. No case file carries `primary-verified`, yet cases export today under the line-34 gate.
**Fix:** define `Spot-verified`; delete or rewrite line 50 to match line 34's actual gate.

### 8. CARRIED — `finance/problem-discovery.md:94` still scripts the two-tier paid "Orientation → full study" offer that `collection-futures-study.md` v0.2 explicitly dropped.
`collection-futures-study.md` v0.2 states: "This is the trust-builder, and it replaces the paid Orientation tier" / "One tier, not three." `problem-discovery.md`, the file that scripts a live discovery conversation, was not updated to match. Colleen Fanning's inbound (per the CFO steward's 2026-08-27 brief, unreplied a third calendar day as of this run) is exactly the kind of contact this stale script would be used on.
**Fix:** update `problem-discovery.md:94` to the v0.2 single-tier structure, or drop the parenthetical and link to `collection-futures-study.md` instead.

### 9. CARRIED — `institution-building/institution-building.md:31` still uses the exact "endowment coverage" phrase `claims-register.md` C4 names as the thing not to say about McNay.
*"McNay already fed it (endowment coverage, self-perpetuating board, adaptive-reuse conversion)..."* C4: "Do NOT say: 'McNay has 9.3× endowment coverage' (it's net assets, not endowment)."
**Fix:** replace with "net-assets ratio (upper bound)."

---

## RESOLVED SINCE LAST AUDIT (noted, no action needed)

- **Primary-verification backlog growth** (should-fix #5 last audit) — held flat at 67 across two runs; see #5 above.
- **The two newest three-case batches' sourcing discipline** — `stieglitz-collection-fisk-crystal-bridges`, `rachofsky-warehouse-dallas`, `societe-generale-collection`, `cookie-factory-denver`, `powder-art-foundation`, `ashbery-collection-flow-chart` all show clean confidence tagging (`secondary`/`unknown`/`n/a` correctly distinguished, contested facts like Petrucci's founding year stored as contested rather than picked). The em-dash issue in `cookie-factory-denver.md` (CRITICAL #4) is a voice defect, not a sourcing one.
- **No settled decision found still marked open** — checked `company/decisions/`; the one file present (`2026-08-12-opal-summit.md`) is correctly marked "decided — DECLINE (final, 2026-08-13)".
- **`marketing/linkedin.md`, `marketing/substack.md`, `marketing/website.md`** re-checked against single-source-of-truth: all three correctly point to `positioning.md` for live public copy rather than keeping their own. No drift, no live em dashes or voice breaks found in current public-facing text.

---

## MINOR

### 10. CARRIED — the `origin` frontmatter field is still split across multiple values (`corporate`, `private`, `private-individual`) with no definition in `case-template.md`.
**Fix:** pick one value for the private side, normalize, and document it.

### 11. CARRIED, still fragmenting — out-of-vocabulary coded values for edge cases and the corporate-origin exception have not converged.
`fisher-landau.md` (`founder_status_at_transition: mixed`), `rubin-museum.md` (`building_type: purpose-acquired-existing`), `rauschenberg-foundation-hq.md` (`primary_friction: funding-optimization`) remain unchanged, each self-noting its own fallback value in prose but not using it in the coded field. `deutsche-bank-collection.md`/`bank-of-america-collection.md` (`parent-entity-continuity: yes`) vs. `enron-art-collection.md` (`parent-entity-survival`) remain two different invented terms for the same pattern.
**Fix:** for the individually-flagged cases, use the fallback each file already names in its own prose. For the corporate cases, amend `case-template.md` to add one authorized value before another corporate case invents a fourth term.

### 12. CARRIED — `crm/partners/Dawn Mari La Monica.md:36` still conflates C1 and C8 into a claim neither source makes, in a file marked CLOSED. Low priority since the file is closed and not live public copy.

---

**Counts:** 4 critical (1 new, 3 carried) / 5 should-fix (1 resolved and listed above, 4 carried) / 3 minor (all carried).
