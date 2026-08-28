# QA Report — 2026-08-28

**Verdict:** Not clean. The em-dash defect on live public copy has gone from a slow-burn recurrence to a full-blown systemic failure (11 → 25 live instances across 22 case files), and two long-standing CRITICALs (the manuscript's C31 self-contradiction, the export's blended $31T figure) are unfixed for a second and sixth audit respectively. Genuinely good news: three archival moves made during the 2026-08-27 business-model pivot retired the fabricated-buyer-quote CRITICAL and two should-fix items outright, because the files carrying them are no longer live or authoritative — noted below, not re-flagged. The Collections dataset itself (108 coded cases, three added since the last audit) continues to show clean sourcing and confidence-tagging discipline.

---

## CRITICAL

### 1. CARRIED, escalated — live public-facing em dashes have more than doubled: 25 instances across 22 case files, not the 11 named last audit.
`ai-tells.md` / `voice.md`: "No em dashes. Use commas or restructure," binding on all public-facing copy, which includes every `public_*` frontmatter field (these export verbatim to `export/nariway-public.json` and the live site). Last audit's 11 named instances (`bank-of-america-collection.md`, `ganz-collection.md`, `crystal-bridges.md`, `klesch-collection-birkbeck.md`, `las-vegas-museum-of-art.md`, `lucas-museum.md`, `cam-raleigh.md`, `brauer-museum-valparaiso.md`, `bunker-artspace.md`, `petrucci-family-foundation.md`, `cookie-factory-denver.md`) are **all still live, unfixed**. A direct grep of every `public_*` field this run finds 14 additional files with the same defect that the prior three audits never named: `0xcollection.md` (×2, `public_size` and `public_pathway_timeline`), `amoca-cardiff.md` (`public_name`), `art-bridges-foundation.md` (`public_origin`), `blaquier-collection.md` (`public_origin`, added this run), `canyon-nyc.md` (`public_focus`), `goodwood-art-foundation.md` (`public_origin`), `heckler-american-folk-art-museum.md` (`public_focus`, added this run), `jaipur-centre-for-art.md` (`public_origin`), `joe-lewis-collection.md` (`public_origin`, added this run), `julia-stoschek-foundation.md` (`public_focus`), `paz-museum-brumadinho.md` (`public_name`), and confirms the total in `export/nariway-public.json` is now 25 raw occurrences, not 11. This is the fourth consecutive audit to flag this exact defect, which the third audit itself predicted: "a fourth recurrence next run would indicate the fix instruction itself isn't being read, not just deprioritized." That has now happened, and the true scope was worse than any prior audit reported, because prior audits sampled recently-touched files rather than grepping the whole `public_*` surface.
**Fix:** run a single mechanical pass — `grep -rn "—" cases/*.md | grep "^\S*:public_"` (or equivalent) — rewrite every hit with a comma or restructured sentence, regenerate the export, and add this exact grep as a pre-commit or pre-export check against `public_*` fields specifically, not general prose. An audit note has now failed to close this four times running; only an automated gate will.

### 2. CARRIED (2nd audit) — `marketing/what-becomes-of-great-art-collections.md:330` still states the IRS Art Advisory Panel's superseded FY2018 figures as current FY2023 fact, still contradicting the claims-register entry it cites.
Flagged new last audit at line 314; the text is unchanged (now at line 330 after intervening edits): *"In FY2023, the most recent year a public tally could be found, the Panel reviewed 251 items across 67 taxpayer cases, an aggregate claimed valuation of $360.9 million, and recommended adjusting **63%** of the items it reviewed, a net adjustment of –$64.6 million (C31)."* `claims-register.md` C31 states plainly: those exact figures are the **FY2018** numbers, misattributed; the real, verified FY2023 figures are **195 items / 37 cases / $795,527,954 claimed / 103 accepted (53%) / 92 adjusted (47%) / –$16,946,454 net**. The manuscript's own `(C31)` citation points to the entry that disproves its sentence. Two full coding runs have touched this file since the finding (this run's commit message says "Manuscript... updated") without correcting it.
**Fix:** replace the sentence with C31's verified FY2023 figures.

### 3. CARRIED (6th audit) — `export/nariway-public.json:6316` and `content/content.json:54` still misattribute the wealth-transfer figure to three non-comparable sources blended into one number, live on the public site.
Unchanged verbatim across six audits: both files still read `"value": "~$31T+"`, `"source": "wealth-research (Cerulli / UBS / Knight Frank)"`. `claims-register.md` C36 exists specifically to bar this: Deloitte/ArtTactic's ~$31T (C1's input, decade, global) is not Cerulli's $124T (US-only, through 2048, C8) or UBS's ~$83T (global, 20-25 years, C36); Knight Frank publishes no wealth-transfer total at all (only UHNWI population counts, C34). The fix has sat drafted in `marketing/gwt-content-draft.md` Block 3 for over two weeks.
**Fix:** replace the tile with the already-drafted GWT Block 2/3 figures, or at minimum attribute `$31T` to Deloitte/ArtTactic alone.

### RESOLVED BY ARCHIVAL (not re-flagged) — the fabricated buyer-quote CRITICAL
Prior audits' CRITICAL #3 (`finance/collection-futures-study.md:28`, an invented quotation attributed to a real buyer) is moot: the file was moved to `archive/finance/collection-futures-study.md` in the 2026-08-27 business-model pivot, and `archive/README.md` explicitly marks everything there "retired... NOT authoritative." It is no longer live copy that could mislead anyone, including Alina, so this audit is not carrying it forward. Confirm no successor document under the new estate-attorney-facing model repeats the same invented-quote pattern; none was found this run.

---

## SHOULD-FIX

### 4. CARRIED — `marketing/what-becomes-of-great-art-collections.md:251` still cites "(Deloitte, Table 1)" and "(Cerulli, Table 1)" for two figures Table 1 doesn't contain.
Table 1 holds $992B, $2.56T→$3.47T, $54T, 72%, 80%, 51%; neither the raw $31T nor $124T appears there. Unchanged since first flagged two audits ago.
**Fix:** delete the two "(..., Table 1)" tags.

### 5. CARRIED — `case-template.md` still contradicts itself on the export gate, and `Spot-verified` remains undefined.
Line 9 lists `Spot-verified` as an allowed `verification_status` value with no definition anywhere in the file. Line 34 states the export gate is `public_page_eligible` AND `public_verified` (explicitly not the internal `verification` tag); line 50 still says a case is held from export until `verification: primary-verified`, directly contradicting line 34. No case file carries `primary-verified`, yet cases export today under line 34's gate.
**Fix:** define `Spot-verified`; delete or rewrite line 50 to match line 34.

### 6. Primary-verification backlog holds flat — good discipline, confirm it continues.
The backlog stayed at 67 numbered items across three more coding runs (101 → 105 → 108 cases). All three of this run's new cases (Heckler, Lewis, Kirk Edward Long) were correctly excluded as structurally, not just currently, unresolvable (gifts absorbed into a larger institution's undisaggregated financials, or a personal holding with no nonprofit filing) rather than added and left to sit. No action needed; noted so the pattern keeps getting checked.

### RESOLVED BY ARCHIVAL (not re-flagged)
- Prior should-fix (`finance/problem-discovery.md:94`, a stale two-tier pricing script) — file archived to `archive/finance/problem-discovery.md`, non-authoritative.
- Prior should-fix (`institution-building/institution-building.md:31`, the "endowment coverage" wording C4 bars) — file archived to `archive/institution-building/institution-building.md`, non-authoritative.

---

## MINOR

### 7. CARRIED — the `origin` frontmatter field is still split across multiple values (`corporate`, `private`, `private-individual`) with no definition in `case-template.md`.
**Fix:** pick one value for the private side, normalize, and document it.

### 8. CARRIED, still fragmenting — out-of-vocabulary coded values for edge cases and the corporate-origin exception have not converged.
`fisher-landau.md`, `rubin-museum.md`, `rauschenberg-foundation-hq.md` each still self-note a fallback value in prose without adopting it in the coded field; `deutsche-bank-collection.md`/`bank-of-america-collection.md` (`parent-entity-continuity`) vs. `enron-art-collection.md` (`parent-entity-survival`) remain two invented terms for the same pattern.
**Fix:** adopt each file's own noted fallback; add one authorized corporate-continuity value to `case-template.md`.

### 9. No settled decision found still marked open.
Checked all five files in `company/decisions/`: all are explicitly marked decided (DECLINE, qualified YES, or a completed redesign with an addendum). No structural issue.

---

**Counts:** 3 critical (0 new, 1 escalated, 2 carried; 1 resolved by archival and not counted) / 3 should-fix (1 new confirm-only, 2 carried; 2 resolved by archival and not counted) / 2 minor (both carried).
