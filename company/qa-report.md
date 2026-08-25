# QA Report — 2026-08-25

**Verdict:** Not clean, and no ground gained since yesterday. All four CRITICALs from the last audit remain unfixed (three of them now carried across three or more consecutive audits), and the primary-verification backlog kept growing (57 → 63 items). New research work since the last audit (three new coded cases, a claims-register addition, an institutional-economics deepening pass, the GWT page content draft) is clean and well-disciplined — sourced, confidence-tagged, and consistent with the register. The unfixed problems are all inherited, not new.

---

## CRITICAL

### 1. CARRIED (3rd audit) — `export/nariway-public.json` and `content/content.json` still misattribute the $31T figure and blend three non-comparable wealth-transfer totals into one number, live on the public site.
The fact tile (`export/nariway-public.json:4999`, `content/content.json:54`) still reads `"value": "~$31T+"`, `"source": "wealth-research (Cerulli / UBS / Knight Frank)"`. `claims-register.md` C36 exists specifically to stop this: Deloitte/ArtTactic's ~$31T (C1's input, decade horizon, global) is a different figure from Cerulli's $124T (US-only, through 2048, C8) and UBS's ~$83T (global, 20-25 years); C36 says they "must not be added together, rounded into one another, or cited as convergent evidence for a single figure." Knight Frank doesn't publish a wealth-transfer total at all (only UHNWI population counts, C34). Unchanged for the third straight audit.
**Note (the fix now exists, just not applied):** `marketing/gwt-content-draft.md` Block 3, finalized this run, is the correct design — a comparison table with all three figures held separate, explicitly labeled as covering different geographies/scopes/timeframes and "cannot be added together or compared directly," matching C36 exactly. The GWT page is targeting an Aug 28 launch per the CMO/CFO briefs. Whoever ships it should also retire the old `~$31T+` tile in `export/nariway-public.json`/`content/content.json` at the same time, or this critical simply outlives the page that was meant to fix it.
**Fix:** replace the export/content.json tile with the GWT Block 2/3 figures as drafted, or at minimum correct the `$31T` tile to cite Deloitte/ArtTactic alone.

### 2. CARRIED (3rd audit) — `cases/terra.md` and `cases/di-rosa.md` still carry `public_verified: true` while each file's own body says the facts are unverified.
`terra.md`: "**Verify first:** dates, the nature of the litigation, and where works ultimately went." `di-rosa.md`: "**Verify first:** the 'campus for sale' and deaccessioning claims are provisional, confirm against primary sources before drawing lessons." Both still set `public_verified: true` in frontmatter, and both still export live. Standard violated: `case-template.md`'s public-projection accuracy gate (`public_verified` = "the public-facing claims... are confirmed"); `quality-assurance.md`'s sourcing rule.
**Fix:** revert `public_verified` to `false` on both until the verification each file itself calls for is done.

### 3. CARRIED (3rd audit) — `finance/collection-futures-study.md:28` still presents a fabricated line as a real buyer's words.
*"In the buyer's words, 'I understand my options and I am making this decision on purpose.'"* No buyer said this. H7B (willingness to pay) is explicitly "Untested" per `research-program.md`, and no completed discovery conversation about this offer exists in `finance/problem-discovery.md`'s log (the log still shows one completed conversation, Dawn, and this quote does not match her logged material). This sits inside a section titled "Buyer-backward... hypotheses, to be tested," so the surrounding prose is honest about being hypothetical — the quoted sentence itself is the one place that slips from hypothesis into invented testimony.
**Fix:** reword without quotation marks so it reads as an authored hypothesis of what success looks like, not captured testimony.

### 4. CARRIED (2nd audit) — em dashes in `public_*` export fields remain live in `export/nariway-public.json`, a direct breach of `voice.md`/`ai-tells.md` in public-facing copy.
Confirmed still present verbatim in the current export, unchanged since escalated last audit: `bank-of-america-collection.md` ("Broad survey — painting, prints, photography, sculpture"), `ganz-collection.md` ("...for $206.5M — then a record for a single-owner auction."), `crystal-bridges.md` ("...in Bentonville, Arkansas — a purpose-built Moshe Safdie complex..."), `klesch-collection-birkbeck.md`, `las-vegas-museum-of-art.md`, `lucas-museum.md`, `cam-raleigh.md`, `brauer-museum-valparaiso.md`. All eight source cases carry `public_page_eligible: true` and `public_verified: true`, so this is live payload, not a hypothetical export. `voice.md`: "No em dashes. Use commas or restructure."
**Fix:** rewrite all eight `public_*` fields with commas or restructured sentences, then regenerate the export.

---

## SHOULD-FIX

### 5. CARRIED — the primary-verification backlog keeps growing unbounded: 63 items now, up from 57/54/51/47/41/38/35/27 across the audit history, with no stated plan to shrink it.
Every research batch adds new secondary-only cases to the backlog faster than any are resolved (the count has only ever gone up). `quality-assurance.md` names "the primary-verification backlog is honored, not growing unbounded" as its own check. The block itself is honestly maintained (each item names a distinct re-fetch target, and the growth is transparently logged as blocked by this session's WebFetch egress restriction, now confirmed across 25+ consecutive research runs), so this is a structural/tooling problem, not a discipline one — but "structural" doesn't mean "not worth a decision." No file states whether the backlog is expected to resolve once WebFetch unblocks, get triaged down to a smaller "must-verify" subset, or simply keep growing as the case count grows toward ~100.
**Fix:** either state explicitly (in `research-program.md` or `report-dataset.md`) that the backlog is expected to stay large until WebFetch access changes and is not itself a quality problem, or set a policy (e.g., cap new secondary-only cases once the backlog passes some threshold) so growth is a decision, not a drift.

### 6. CARRIED — `case-template.md` still contradicts itself on the export gate, and `Spot-verified` remains undefined.
`case-template.md:9` still lists `Spot-verified` as an allowed `verification_status` value with no definition anywhere in the file. `case-template.md:34` states the export gate is `public_page_eligible` AND `public_verified` (explicitly not the internal `verification` tag), while line 50 still says a case is "held from the live export until its figures reach `verification: primary-verified`," directly contradicting line 34 — no case file carries `primary-verified` (confirmed 0 of 89), yet cases export today under the line-34 gate.
**Fix:** define `Spot-verified`; delete or rewrite line 50 to match line 34's actual gate.

### 7. CARRIED, still fragmenting — out-of-vocabulary coded values for the corporate-origin exception have not converged; a new run added a third distinct invented term.
`fisher-landau.md` (`founder_status_at_transition: mixed`), `rubin-museum.md` (`building_type: purpose-acquired-existing`, self-noting the fallback is `adapted-other`), `rauschenberg-foundation-hq.md` (`primary_friction: funding-optimization`, self-noting the fallback is `none-documented`) are all unchanged from prior audits. `deutsche-bank-collection.md` and `bank-of-america-collection.md` both use `parent-entity-continuity: yes`; `enron-art-collection.md` independently uses `parent-entity-survival` for the same underlying pattern — still two different invented terms for the same corporate-origin exception, not one.
**Fix:** for the first three, use the fallback each file already names in its own prose. For the corporate cases, amend `case-template.md` to add one authorized value for this pattern before the next corporate case invents a fourth term.

### 8. CARRIED — `cases/hedreen-seattle-university.md` and `cases/jaipur-centre-for-art.md` still use the deprecated prose `## Public profile` block instead of flat `public_*` frontmatter, silently excluding them from export.
`case-template.md`'s schema requires flat frontmatter and calls the prose-block format "fragile"; the export parses frontmatter only.
**Fix:** migrate both to flat `public_*` frontmatter and set `public_verified` explicitly.

### 9. CARRIED — `marketing/what-becomes-of-great-art-collections.md:209` still cites "(Deloitte, Table 1)" and "(Cerulli, Table 1)" for two figures Table 1 doesn't contain.
Table 1 (line 57) holds $992B, $2.56T→$3.47T, $54T, 72%, 80%, 51% — neither the raw $31T nor $124T appears there (those are the underlying inputs behind C1's $992B and C8's $54T respectively, correctly explained in the surrounding prose). The parenthetical citations are simply wrong pointers.
**Fix:** delete the two "(..., Table 1)" tags; the correct C1/C8 framing already stated nearby doesn't need them.

### 10. CARRIED — `finance/problem-discovery.md:94` still scripts the two-tier paid "Orientation → full study" offer that `collection-futures-study.md` v0.2 explicitly dropped.
*"...the Orientation tier is what gets named first."* `collection-futures-study.md` itself (v0.2, 2026-08-23) states plainly: "This is the trust-builder, and it replaces the paid Orientation tier" and "One tier, not three." `business-model-ledger.md` was updated to the v0.2 structure, but `problem-discovery.md`, the file that scripts what to actually say in a live discovery conversation, was not. This is the one with real-world bite: followed as written today, Alina would misstate Nariway's own offer to a live prospect (Colleen Fanning, per the 2026-08-25 CFO steward note, is exactly the kind of live contact this script would be used on).
**Fix:** update `problem-discovery.md:94` to the v0.2 single-tier structure (free scoping conversation → one priced engagement), or drop the parenthetical and link to `collection-futures-study.md` instead.

### 11. CARRIED — `institution-building/institution-building.md:31` still uses the exact "endowment coverage" phrase `claims-register.md` C4 names as the thing not to say about McNay.
*"McNay already fed it (endowment coverage, self-perpetuating board, adaptive-reuse conversion)..."* C4: "Do NOT say: 'McNay has 9.3× endowment coverage' (it's net assets, not endowment)."
**Fix:** replace with "net-assets ratio (upper bound)."

### 12. NEW — `marketing/gwt-content-draft.md` Block 6 cites two figures ("just over one in ten," "about 31%," both Deloitte 2021) that are not in `claims-register.md`.
The register's own convention states: "Add a claim here the first time a number matters enough to be repeated." These two figures are about to anchor a page block ("Keeping is not deciding") on a page targeting an Aug 28 public launch, but they exist only inline in the draft, not as a citable register entry the way every other figure on the same page (C1, C3, C8, C12, C36) already is. This is not a sourcing failure in the narrow sense — the draft does cite "(Deloitte, 2021)" and lists the report in Block 11's sources — but it is a single-source-of-truth gap: if this number needs correcting later, there is no register entry for downstream files to point to, and the exact mechanism the register exists to prevent (a stat drifting because it was copied instead of linked) is live for this pair the moment the page ships.
**Fix:** add a claims-register entry (next available C-number) for the "1 in 10 have a written plan" / "31% of intenders have discussed or arranged care" pair before or at launch, sourced to the Deloitte Art & Finance Report 2021, then have the GWT block reference it.

---

## MINOR

### 13. CARRIED — `cases/report-dataset.md` Pattern 1's original prose still cites McNay ("McNay's self-perpetuating board") as supporting evidence, while `cases/mcnay.md` remains `status: founder-review`, outside the numbered dataset. The newer, fully-tabulated Pattern 14 already excludes McNay correctly.
**Fix:** fold McNay into the numbered dataset once its research clears the bar, or strike it from Pattern 1's prose list until then.

### 14. CARRIED — `cases/moma.md` still carries two out-of-vocabulary values: `collection_coherence: absorbed`, `decision_owner: collective-founders-trustees`.
**Fix:** amend `case-template.md` to admit these, or remap with a flagged caveat.

### 15. CARRIED — the `origin` frontmatter field is still split across multiple values (`corporate`, `private`, `private-individual`) with no definition in `case-template.md`.
**Fix:** pick one value for the private side, normalize, and document it.

### 16. CARRIED — `crm/partners/Dawn Mari La Monica.md:36` still conflates C1 and C8 into a claim neither source makes ("the ~$1T art transfer is happening now, mostly to surviving spouses"), in a file marked CLOSED. Low priority since the file is closed and not live public copy.

---

## Resolved since the last audit (noted, no action needed)

- **The three newest coded cases** (`wolfsonian-fiu.md`, `pier24-photography.md`, `hall-art-foundation.md`) show clean sourcing: every quantitative field carries a source/confidence tag or explicit `unknown`, ratios are correctly labeled where computable, and each names a distinct re-fetch target in the backlog rather than a vague placeholder.
- **New claims-register entry C57** (foundation policy risk / anti-DEI executive-order scope) is properly sourced, carries an honest confidence tag, and correctly flags the underlying IMLS-elimination legal status as unresolved rather than settled — good discipline on a live, contested fact.
- **`marketing/gwt-content-draft.md`** (new this run) is the strongest evidence yet that the design fix for CRITICAL #1 is understood: its Block 3 table holds the three wealth-transfer estimates separate and correctly labeled, matching C36 exactly, and its evidence-discipline notes (bottom of file) show real rigor about what each figure can and cannot support.
- **The old superseded-65%-IRS-rate issue** flagged in a prior audit is now handled correctly everywhere it recurs in `research/market-intelligence.md` (each mention carries or clearly defers to the "superseded, see C31" framing).
- **No settled decision found still marked open**, and no other new claims-register drift found beyond items already carried above.

---

**Counts:** 4 critical (3 carried unfixed, 1 carried unfixed from last run's escalation) / 8 should-fix (7 carried, 1 new) / 4 minor (all carried).
