# QA Report — 2026-08-19

**Verdict:** Not clean, but narrowing. Both prior CRITICALs remain open for a third consecutive audit — the flagship report still publishes claim C10 as settled fact despite the claims-register's own caveat, and the live Substack copy in `positioning.md` still breaks `voice.md`'s staccato rule. Several previously-flagged should-fix items were genuinely fixed this run (McNay's and Neue Galerie's frontmatter vocabulary). The four new case files added this run (UBS, Fondazione Prada, Muzej Lah, Reader's Digest) are exemplary sourcing discipline — every quantitative field carries a source and confidence tag, contested figures are flagged as contested, gaps are marked `unknown` rather than guessed. No new critical issues found.

---

## CRITICAL

1. **`marketing/what-becomes-of-great-art-collections.md` still publishes claim C10 as a settled figure — open for a third consecutive audit, and the report now builds a causal claim on top of it.**
   `research/claims-register.md:52-54` (C10) states the source is "via ChatGPT market-sizing review 2026-08-16; **confirm exact figure in the report before citing publicly**," and separately warns the trend direction may be backwards versus the underlying source (`company/hygiene-report.md:23,30` carries the same open flag). Despite this, Table 1 (line 66) still lists it flat, no caveat: "~51% | Wealth managers now offering art services, up from ~25% in 2011 | C10." Worse, the prose beneath the table (line 68) now draws an inference from it: "The surrounding financial industry has noticed, which is why art services inside wealth management have roughly doubled since 2011." An unconfirmed, self-flagged-as-possibly-wrong number is not only presented as fact, it is now the premise of a causal statement in the report's own preface chapter.
   Standard violated: `company/quality-assurance.md` item 1 (nothing "presented as fact" beyond its source); the claims-register's own citation discipline. **Fix:** confirm the figure and trend direction against the actual Deloitte Art & Finance report before Table 1 or the causal sentence ships, or pull both until then, or mark the row `[unconfirmed]` and soften "which is why... have roughly doubled" to something the source can actually support.

2. **Live, published Substack copy in `company/positioning.md` still breaks `voice.md`'s staccato and fragment-stack rules — open for a third consecutive audit, unchanged.**
   - Substack About page (line 51): "Some collections stay in families for generations. Some become museums or foundations. Some are given or lent to existing institutions. Some travel. Some are divided or sold. Some disappear from public view." (six short parallel sentences, against "No staccato sequences. Never three or more short sentences in a row.")
   - Substack Welcome page (line 81): "Does it stay in the family? Become a museum or foundation? Go to an existing institution? Travel? Get divided or sold?" (four subject-less fragments after the first sentence).
   Both are live, published pages, and both HOME.md and prior check-in emails already acknowledge this is outstanding — the visibility exists, the copy has not moved in three audits.
   Standard violated: `voice.md` craft standards (explicitly "mechanical and non-negotiable") and `ai-tells.md` #2. **Fix:** vary sentence shape or collapse each list into fuller sentences, in `positioning.md` and the live Substack page together, per the file's own mirror rule.

---

## SHOULD-FIX

3. **`cases/mcnay.md` still isn't folded into `report-dataset.md`'s numbered master synthesis, while its narrative is cited as supporting evidence — open for a sixth consecutive audit, though the field-level errors are now fixed.** This run's frontmatter is now valid (`pathway: found-house-museum`, `verification: provisional`, `decision_owner: collector-alone` — all three prior invalid values corrected). But `report-dataset.md`'s Pattern 1 prose (line 228) still cites "McNay's self-perpetuating board" as supporting evidence for the report's central governance-survival claim, while McNay's own file still carries `status: founder-review` with an unread will, and `case-template.md`'s own worked example for this exact case warns "prose must not outrun research." Pattern 14 (the newer, fully-counted table) correctly excludes McNay; Pattern 1's older prose does not. **Fix:** fold McNay into the numbered 1-54 dataset once its research is complete enough, or drop it from Pattern 1's supporting-example list until then.

4. **`cases/moma.md` still carries two values outside `case-template.md`'s controlled vocabulary** — `collection_coherence: absorbed` and `decision_owner: collective-founders-trustees` — unresolved for a third consecutive audit. This is a schema gap, not a coding error: both values describe a real pattern (MoMA's multi-founder, absorbed-collection structure) the vocabulary has no slot for. **Fix:** amend `case-template.md` to add these values, or remap to the nearest existing value with a flagged caveat.

5. **`verification: spot-verified` is now applied to 40+ cases including all four added this run (UBS, Fondazione Prada, Muzej Lah, Reader's Digest), with `case-template.md` still not defining what distinguishes it from `Provisional`.** Each new file is honest inline about being WebSearch-snippet synthesis, `secondary` throughout, no direct primary fetch — so no individual figure overstates its own confidence, and this stays in the same gray zone flagged across four prior audits rather than a fresh violation. But the backlog keeps growing unbounded while the tier stays undefined, which is exactly the condition `company/quality-assurance.md` asks this audit to watch for. **Fix:** add a one-line definition of `Spot-verified` to `case-template.md` (e.g., "narrative facts cross-checked across ≥2 independent secondary sources, no direct primary fetch"), or downgrade WebSearch-only cases to `Provisional` until a primary source is pulled.

---

## MINOR

6. **`marketing/website.md` still has em dashes in its "finalized copy" blocks** (e.g. "Nariway — Independent work on…", "The Brief Experiment — A history of…"), unresolved for a sixth consecutive audit. Still likely a false positive on a literal reading of the rule — the em-dash-as-label-separator construction is used throughout the vault's own internal formatting, including `voice.md`'s own title — so this is noted without escalating, pending Alina's call on whether the construction is in scope.

7. **`research/research-program.md` still restates the $992B/5%/$19.84T breakdown (line 38) and the 72%/90%/80% retention figures (line 78) inline rather than linking to `[[claims-register]]` C1/C3/C12.** No drift found this run — every number still matches its claims-register entry — so this remains a standing risk rather than an active error.

---

## Resolved since the last audit (noted, no action needed)

- **`cases/mcnay.md`'s three invalid controlled-vocabulary values, fixed.** `pathway`, `verification`, and `decision_owner` now all match the values `case-template.md`'s own worked example already specified. (The dataset-inclusion question, item 3 above, is separate and remains open.)
- **`cases/neue-galerie.md`'s `decision_owner: founder-self`, fixed.** Now reads `collector-alone`, matching `report-dataset.md` #3's already-coded value.
- **Website/positioning public-copy reconciliation is proceeding cleanly.** `company/positioning.md` was updated this run to mirror the live nariway.com redesign (hero, intro, Conversations, advisory, Contact, About, founder bio), matching `marketing/website.md`'s own capture of the same live site. Both files independently defer to the live site as authoritative rather than to each other, so no single-source-of-truth violation, though it is worth watching that the two mirrors stay in sync as the site keeps changing.
- **The four new case files this run** (`ubs-art-collection.md`, `fondazione-prada.md`, `muzej-lah.md`, `readers-digest-wallace-collection.md`) show no sourcing violations: every quantitative field carries a `[source: ...; confidence: ...]` tag or an explicit `unknown`, contested figures (UBS collection size, Muzej Lah's two start-year clocks, Reader's Digest's sale-lot count) are presented as contested rather than resolved, and no net-assets-to-opex ratio appears unlabeled.
- **No new claims-register drift found.** Spot-checked the newly added claims (C21-C27, covering art-loan terms, insurance, and the 2026 tax law) against their citations in `marketing/what-becomes-of-great-art-collections.md` §4.3-4.5 — all match, all carry `Ref` tags, and C27 (the insurance-market-size literature) is correctly cited as a finding-about-unreliability rather than as a number.
- **`marketing/linkedin.md` and `marketing/substack.md` correctly point to `positioning.md`** for their live bios rather than keeping their own copy, per the single-source-of-truth rule.

---

**Counts:** 2 critical (both carried, 3rd audit) / 3 should-fix / 2 minor.
