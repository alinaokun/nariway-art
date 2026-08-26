# QA Report — 2026-08-26

**Verdict:** Not clean. Three of yesterday's four CRITICALs remain unfixed (two now carried across four consecutive audits), one CRITICAL is newly resolved, and two brand-new em-dash breaks were introduced in this run's new case files. The primary-verification backlog kept growing (63 → 67 items). Genuinely good work this run: `terra.md`/`di-rosa.md` were properly re-verified (not just patched), `moma.md`'s vocabulary was corrected, `hedreen`/`jaipur` were migrated to flat frontmatter, and `claims-register.md` C62 was added exactly as last audit's finding #12 requested. But two new public-facing em dashes shipped in the same run that was supposed to be closing that exact category of finding.

---

## CRITICAL

### 1. CARRIED (4th audit) — `export/nariway-public.json` and `content/content.json` still misattribute the $31T figure and blend three non-comparable wealth-transfer totals into one number, live on the public site.
Unchanged verbatim since the first audit: `export/nariway-public.json:5485` and `content/content.json:54` still read `"value": "~$31T+"`, `"source": "wealth-research (Cerulli / UBS / Knight Frank)"`. `claims-register.md` C36 exists specifically to stop this: Deloitte/ArtTactic's ~$31T (C1's input, decade horizon, global) is a different figure from Cerulli's $124T (US-only, through 2048, C8) and UBS's ~$83T (global, 20-25 years); C36 says they "must not be added together, rounded into one another, or cited as convergent evidence for a single figure." Knight Frank doesn't publish a wealth-transfer total at all (only UHNWI population counts, C34). The CMO steward's own 2026-08-26 brief (`marketing/cmo-brief.md`) now independently names this same tile as a second unshipped launch fix, alongside the em-dash issue below, ahead of the Aug 28 GWT launch — the finding has effectively been re-discovered by a second function, which is a sign this needs to actually get fixed, not just re-confirmed.
**Fix:** replace the export/content.json tile with the GWT Block 2/3 figures (already drafted, correctly separated, in `marketing/gwt-content-draft.md`), or at minimum correct the `$31T` tile to cite Deloitte/ArtTactic alone.

### 2. CARRIED (4th audit) — `finance/collection-futures-study.md:28` still presents a fabricated line as a real buyer's words.
*"In the buyer's words, 'I understand my options and I am making this decision on purpose.'"* No buyer said this; H7B (willingness to pay) is explicitly "Untested" per `research-program.md`, and no completed discovery conversation matches this quote in `finance/problem-discovery.md`'s log. This sits inside a section titled "Buyer-backward... hypotheses, to be tested," so the surrounding prose is honest about being hypothetical; the quoted sentence itself is the one place that slips from hypothesis into invented testimony. **Escalation note:** the 2026-08-26 CFO steward brief (`finance/cfo-brief.md:15`) now flags this same line directly and in stronger terms than the audit itself ("a real risk if it's ever shown as-is... should be fixed before the document goes in front of anyone, not treated as a QA backlog item") — two independent functions now agree this is live risk, not a paperwork item, and it is still unfixed four audits later.
**Fix:** reword without quotation marks so it reads as an authored hypothesis of what success looks like, not captured testimony.

### 3. NEW — two newly-added cases ship live public-facing em dashes, the exact defect CRITICAL #4 (below) has flagged for three straight audits.
`cases/bunker-artspace.md:31` (`public_page_eligible: true`, `public_verified: true`): *"...converted a Depression-era Art Deco building in West Palm Beach — once a toy factory, later a wartime armory — into a private exhibition space..."* `cases/petrucci-family-foundation.md:31` (same flags both true): *"...began collecting African American art in 2012 specifically to lend it out — building a 500-plus-work collection with no gallery of its own, circulating instead through partner museums..."* Both are confirmed live in `export/nariway-public.json` (lines 4173 and 3401), not merely drafted. `voice.md`: "No em dashes. Use commas or restructure." Standard violated: `ai-tells.md`/`voice.md` on public-facing copy, same category as the carried #4 below, but these are new instances added *this run*, in files whose sibling this-run edits (`terra.md`, `di-rosa.md`, `moma.md`) show the drafting agent is otherwise capable of clean, careful work — suggesting the em-dash check is not being run against new `public_*` fields at write time, only retrospectively.
**Fix:** rewrite both `public_origin` fields with commas or restructured sentences, then regenerate the export. Given this is now recurring, add an em-dash grep against new `public_*` fields as a pre-commit step for the coding function, not just a QA-audit catch.

### 4. CARRIED (3rd audit) — em dashes in `public_*` export fields remain live in `export/nariway-public.json`, unchanged.
Confirmed still present verbatim in the current export: `bank-of-america-collection.md` ("Broad survey — painting, prints, photography, sculpture"), `ganz-collection.md` ("...for $206.5M — then a record for a single-owner auction."), `crystal-bridges.md`, `klesch-collection-birkbeck.md`, `las-vegas-museum-of-art.md`, `lucas-museum.md`, `cam-raleigh.md`, `brauer-museum-valparaiso.md`. All eight source cases carry `public_page_eligible: true` and `public_verified: true`. Combined with finding #3, this is now **ten** live cases with the same defect, not eight.
**Fix:** rewrite all ten `public_*` fields with commas or restructured sentences, then regenerate the export.

---

## SHOULD-FIX

### 5. CARRIED — the primary-verification backlog keeps growing unbounded: 67 items now, up from 63/57/54/51/47/41/38/35/27 across the audit history, still with no stated policy.
This run added `museum-of-russian-icons` as item 67 while correctly declining to add `bunker-artspace` and `microsoft-art-collection` (both structurally, not just currently, unverifiable — a real, honest distinction). But the underlying finding stands: `quality-assurance.md` names "the primary-verification backlog is honored, not growing unbounded" as its own check, and no file yet states whether the backlog is expected to resolve once WebFetch unblocks, get triaged to a smaller "must-verify" subset, or simply keep growing as the case count grows toward ~100.
**Fix:** state a policy in `research-program.md` or `report-dataset.md` — either the backlog is expected to stay large until WebFetch access changes (and that is not itself a quality problem), or set a cap/triage rule so growth is a decision, not a drift.

### 6. CARRIED — `case-template.md` still contradicts itself on the export gate, and `Spot-verified` remains undefined.
No edits to this file since the finding was first raised. `case-template.md:9` lists `Spot-verified` as an allowed `verification_status` value with no definition anywhere in the file. Line 34 states the export gate is `public_page_eligible` AND `public_verified` (explicitly not the internal `verification` tag), while line 50 still says a case is held from export until `verification: primary-verified` — directly contradicting line 34. No case file carries `primary-verified` (0 of 95), yet cases export today under the line-34 gate.
**Fix:** define `Spot-verified`; delete or rewrite line 50 to match line 34's actual gate.

### 7. CARRIED, still fragmenting — out-of-vocabulary coded values for edge cases and the corporate-origin exception have not converged.
`fisher-landau.md` (`founder_status_at_transition: mixed`), `rubin-museum.md` (`building_type: purpose-acquired-existing`), `rauschenberg-foundation-hq.md` (`primary_friction: funding-optimization`) are unchanged from prior audits, each self-noting its own fallback value in prose but not using it in the coded field. `deutsche-bank-collection.md` and `bank-of-america-collection.md` use `parent-entity-continuity: yes`; `enron-art-collection.md` independently uses `parent-entity-survival` for the same underlying pattern — still two different invented terms. The new `microsoft-art-collection.md` sidesteps the issue by coding `survived_founder: n/a` with no invented term at all, which is at least consistent with the `ubs-art-collection`/`jpmorgan-chase-collection` convention already in use, but `n/a` itself is not in the template's `survived_founder` vocabulary (`yes`·`no`·`not-yet-testable`·`unknown`) — a third variant of the same underlying schema gap, not a fix.
**Fix:** for the individually-flagged cases, use the fallback each file already names in its own prose. For the corporate cases, amend `case-template.md` to add one authorized value for the corporate-continuity pattern (and, ideally, one for `survived_founder: n/a`) before the next corporate case invents a fourth term.

### 8. CARRIED — `marketing/what-becomes-of-great-art-collections.md:225` still cites "(Deloitte, Table 1)" and "(Cerulli, Table 1)" for two figures Table 1 doesn't contain.
Table 1 (line 57) holds $992B, $2.56T→$3.47T, $54T, 72%, 80%, 51%; neither the raw $31T nor $124T appears there (those are the underlying inputs behind C1's $992B and C8's $54T respectively, correctly explained in the surrounding prose). The parenthetical citations are simply wrong pointers.
**Fix:** delete the two "(..., Table 1)" tags.

### 9. CARRIED — `finance/problem-discovery.md:94` still scripts the two-tier paid "Orientation → full study" offer that `collection-futures-study.md` v0.2 explicitly dropped.
*"...the Orientation tier is what gets named first."* `collection-futures-study.md` v0.2 (2026-08-23) states: "This is the trust-builder, and it replaces the paid Orientation tier" / "One tier, not three." `business-model-ledger.md` was updated to the v0.2 structure; `problem-discovery.md`, the file that scripts a live discovery conversation, was not. The CFO steward's 2026-08-26 brief shows a live inbound contact (Fanning) unreplied for a second day — exactly the kind of contact this stale script would be used on.
**Fix:** update `problem-discovery.md:94` to the v0.2 single-tier structure, or drop the parenthetical and link to `collection-futures-study.md` instead.

### 10. CARRIED — `institution-building/institution-building.md:31` still uses the exact "endowment coverage" phrase `claims-register.md` C4 names as the thing not to say about McNay.
*"McNay already fed it (endowment coverage, self-perpetuating board, adaptive-reuse conversion)..."* C4: "Do NOT say: 'McNay has 9.3× endowment coverage' (it's net assets, not endowment)."
**Fix:** replace with "net-assets ratio (upper bound)."

---

## RESOLVED SINCE LAST AUDIT (noted, no action needed)

- **CRITICAL #2 from the last audit** (`terra.md`/`di-rosa.md` stale `public_verified` caveats) — genuinely resolved, not just patched. Both files' public facts were independently re-verified via WebSearch this run (Artforum/Wikipedia for Terra; Artnet News/Press Democrat/SF Chronicle/The Art Newspaper for di Rosa), and the stale "verify first" language now correctly reads as internal-financial-depth-only, matching `case-template.md`'s actual public-export gate (public-fact accuracy, not 990 depth).
- **`cases/moma.md`** — both out-of-vocabulary values (`collection_coherence: absorbed`, `decision_owner: collective-founders-trustees`) corrected to valid template values, with the reasoning documented inline.
- **`cases/hedreen-seattle-university.md` and `cases/jaipur-centre-for-art.md`** — migrated from the deprecated prose "## Public profile" block to flat `public_*` frontmatter, which the export can now actually read.
- **`claims-register.md` C62** — added exactly as last audit's should-fix #12 requested (the "1 in 10" / "31%" Deloitte 2021 estate-planning figures), with an honest note on why a fresh 2026-08-25 search couldn't independently re-derive the original numbers. `gwt-content-draft.md` still cites these inline with "(Deloitte, 2021)" rather than pointing to C62 directly — a minor single-source-of-truth gap, not worth a separate line item, but worth closing before the page ships.
- **`cases/report-dataset.md` Pattern 1's McNay citation** (prior minor #13) — corrected with an explicit note that McNay is deliberately excluded, sourced to this audit.
- **The six newest coded cases** (`museum-of-russian-icons`, `bunker-artspace`, `microsoft-art-collection`, `wolf-kahn-foundation`, `petrucci-family-foundation`, `paz-museum-brumadinho`) show clean sourcing discipline on every quantitative field: `unknown` where genuinely unknown, secondary tags present, contested figures (e.g. Wolf Kahn's two conflicting net-assets snippets) stored as contested rather than picked arbitrarily. The em-dash issue in two of these files (CRITICAL #3) is a voice defect, not a sourcing one.
- **`marketing/linkedin.md` and `marketing/substack.md`** checked against the single-source-of-truth rule: both correctly point to `positioning.md` for live copy rather than keeping their own. No drift found.
- **No settled decision found still marked open.**

---

## MINOR

### 11. CARRIED — the `origin` frontmatter field is still split across multiple values (`corporate`, `private`, `private-individual`) with no definition in `case-template.md`.
**Fix:** pick one value for the private side, normalize, and document it.

### 12. CARRIED — `crm/partners/Dawn Mari La Monica.md:36` still conflates C1 and C8 into a claim neither source makes ("the ~$1T art transfer is happening now, mostly to surviving spouses"), in a file marked CLOSED. Low priority since the file is closed and not live public copy.

---

**Counts:** 4 critical (2 carried, 1 resolved and replaced by 1 new same-category finding) / 5 should-fix (all carried) / 2 minor (both carried).
