# QA Report — 2026-08-29

**Verdict:** Not clean. All three CRITICAL findings from the 2026-08-28 audit remain unfixed, one of them for the fifth consecutive audit and still spreading. The Collections dataset itself continues to show clean sourcing and confidence-tagging discipline in every case coded since the last audit (113 cases now, up from 108; primary-verification backlog narrowed 67 → 60, not growing unbounded).

---

## CRITICAL

### 1. CARRIED (5th audit), still spreading — live public-facing em dashes: 25 instances across 24 case files, two of them new since last audit.
`ai-tells.md` / `voice.md`: "No em dashes. Use commas or restructure," binding on all public-facing copy, which includes every `public_*` frontmatter field (these export verbatim to `export/nariway-public.json` and the live site). A fresh grep of every `public_*` field this run (`grep -rn "—" cases/*.md` filtered to lines beginning `public_`) confirms all 22 files named last audit are still live and unfixed, and finds the defect in two additional files not previously named: `kvareli-foundation.md` and `met-irving-chinese-gift.md` (both coded since the last audit). Total raw occurrences held flat at 25 (one file, `0xcollection.md`, still carries two). This is the fifth consecutive audit to flag this exact defect on the exact same underlying set of files; the fourth audit already predicted that a further recurrence "would indicate the fix instruction itself isn't being read, not just deprioritized," and new cases are still being coded with the same defect rather than the backlog shrinking.
**Fix:** run a single mechanical pass — `grep -rn "—" cases/*.md | grep "^public_"` per file — rewrite every hit with a comma or restructured sentence, regenerate the export, and add this grep as a pre-commit or pre-export check scoped to `public_*` fields. A note in this report has now failed to close this five times running; only an automated gate will.

### 2. CARRIED (3rd audit) — `marketing/what-becomes-of-great-art-collections.md:344` still states the IRS Art Advisory Panel's superseded FY2018 figures as current FY2023 fact, still contradicting the claims-register entry it cites.
The sentence (now at line 344, previously flagged at 314 and 330) is unchanged: *"In FY2023, the most recent year a public tally could be found, the Panel reviewed 251 items across 67 taxpayer cases, an aggregate claimed valuation of $360.9 million, and recommended adjusting **63%** of the items it reviewed, a net adjustment of –$64.6 million (C31)."* `claims-register.md` C31 states plainly that those exact figures (251 items / 67 cases / $360.9M / 63% adjusted / –$64.6M) are the **FY2018** numbers, misattributed; the verified FY2023 figures are **195 items / 37 cases / $795,527,954 claimed / 103 accepted (53%) / 92 adjusted (47%) / –$16,946,454 net**. The manuscript's own `(C31)` citation points to the entry that disproves its sentence.
**Fix:** replace the sentence with C31's verified FY2023 figures.

### 3. CARRIED (7th audit) — `export/nariway-public.json:6604` and `content/content.json:54` still misattribute the wealth-transfer figure to three non-comparable sources blended into one number, live on the public site.
Unchanged verbatim across seven audits: both files still read `"value": "~$31T+"`, `"source": "wealth-research (Cerulli / UBS / Knight Frank)"`. `claims-register.md` C36 exists specifically to bar this: Deloitte/ArtTactic's ~$31T (C1's input, decade, global) is not Cerulli's $124T (US-only, through 2048, C8) or UBS's ~$83T (global, 20-25 years, C36); Knight Frank publishes no wealth-transfer total at all (only UHNWI population counts, C34).
**Fix:** replace the tile with the already-drafted GWT Block 2/3 figures in `marketing/gwt-content-draft.md`, or at minimum attribute `$31T` to Deloitte/ArtTactic alone.

---

## SHOULD-FIX

### 4. CARRIED — `marketing/what-becomes-of-great-art-collections.md:263` still cites "(Deloitte, Table 1)" and "(Cerulli, Table 1)" for two figures Table 1 doesn't contain.
Table 1 (line 57-66) holds $992B, $2.56T→$3.47T, $54T, 72%, 80%, 51%; neither the raw $31T nor $124T appears there.
**Fix:** delete the two "(..., Table 1)" tags.

### 5. CARRIED — `case-template.md` still contradicts itself on the export gate, and `Spot-verified` remains undefined.
Line 9 lists `Spot-verified` as an allowed `verification_status` value with no definition anywhere in the file. Line 34 states the export gate is `public_page_eligible` AND `public_verified` (explicitly not the internal `verification` tag); line 50 still says a case is held from export until `verification: primary-verified`, directly contradicting line 34.
**Fix:** define `Spot-verified`; delete or rewrite line 50 to match line 34.

### 6. Primary-verification backlog narrowed, not growing — good discipline, confirm it continues.
The backlog dropped from 67 to 60 numbered items while the coded dataset grew from 108 to 113 cases. No action needed; noted so the pattern keeps getting checked.

---

## MINOR

### 7. CARRIED — the `origin` frontmatter field is still split across multiple values with no definition in `case-template.md`.
Current usage: `corporate` (35) · `private-individual` (24) · `private` (14) · `artist` (5, not previously named).
**Fix:** pick one value for the private side, normalize, and document all values including `artist` in `case-template.md`.

### 8. CARRIED — corporate-continuity vocabulary still fragmented.
`bank-of-america-collection.md`, `credit-suisse-ubs-collection.md`, `deutsche-bank-collection.md`, `jpmorgan-chase-collection.md`, and `ubs-art-collection.md` use `parent-entity-continuity`; `enron-art-collection.md` and `lehman-brothers-collection.md` use `parent-entity-survival` for the same underlying concept.
**Fix:** adopt one term; add it as an authorized value in `case-template.md`.

### 9. No settled decision found still marked open.
Checked all files in `company/decisions/`: all are explicitly marked decided. No structural issue.

---

**Counts:** 3 critical (0 new, 2 carried unchanged, 1 carried and spreading; all 3 escalating in audit count) / 3 should-fix (1 new confirm-only, 2 carried) / 3 minor (1 detail added, 2 carried).
