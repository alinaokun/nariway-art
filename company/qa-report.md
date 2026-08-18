# QA Report — 2026-08-18

**Verdict:** Not clean. 1 new critical — the flagship report manuscript now publishes a Table 1 figure (C10, wealth managers offering art services) as a settled statistic despite the claims-register's own entry flagging it as unconfirmed and possibly backwards. The prior CRITICAL (governance-survival caveat loss) is fixed. The second prior CRITICAL (staccato Substack copy) remains open for a second consecutive audit, still not acted on. Plus 4 should-fix, most of them aging repeat findings on the same three case files, and 2 minor.

---

## CRITICAL

1. **`marketing/what-becomes-of-great-art-collections.md` Table 1 publishes claim C10 as a settled figure, contradicting the claims-register's own caveat on that exact claim.**
   `research/claims-register.md:52-54` (C10) states the ~51%/~25% wealth-manager figure is sourced "via ChatGPT market-sizing review 2026-08-16; **confirm exact figure in the report before citing publicly**," and `company/hygiene-report.md:33` separately flags that the number "may have its trend direction backwards versus its own underlying source." Despite both cautions, `marketing/what-becomes-of-great-art-collections.md:66` — the actual flagship report draft — lists it flat, with no caveat, in Table 1 alongside well-established figures (C1, C8, C9, C3, C12): "~51% | Wealth managers now offering art services, up from ~25% in 2011 | C10." This is the report itself doing the thing the register exists to prevent: an unconfirmed, self-flagged-as-possibly-wrong number reaching publishable copy as if it were settled.
   Standard violated: `company/quality-assurance.md` item 1 (nothing "presented as fact" beyond its source) and the claims-register's own citation discipline. **Fix:** either confirm the figure and trend direction against the actual Deloitte Art & Finance report before Table 1 ships, or pull the row (or mark it `[unconfirmed]`) until then.

2. **Live, published Substack copy in `company/positioning.md` still breaks `voice.md`'s staccato and fragment-stack rules — unresolved for a second consecutive audit.** Same two blocks flagged 2026-08-17, unchanged:
   - Substack About page: "Some collections stay in families for generations. Some become museums or foundations. Some are given or lent to existing institutions. Some travel. Some are divided or sold. Some disappear from public view." (six short parallel sentences, against "No staccato sequences. Never three or more short sentences in a row.")
   - Substack Welcome page: "Does it stay in the family? Become a museum or foundation? Go to an existing institution? Travel? Get divided or sold?" (four subject-less fragments after the first sentence).
   Both HOME.md ("still open, above") and today's queued check-in email ("a QA finding not yet acted on") already acknowledge this is outstanding, so the visibility exists; the copy itself has not moved. Standard violated: `voice.md` craft standards (explicitly "mechanical and non-negotiable") and `ai-tells.md` #2. **Fix:** vary sentence shape or collapse each list into fuller sentences, in `positioning.md` and the live Substack page together, as the file's own mirror rule requires.

---

## SHOULD-FIX

3. **`cases/mcnay.md` still carries the same three invalid controlled-vocabulary values, unresolved for a fifth consecutive audit** — `pathway: house-to-museum` (not in the vocab; should be `found-house-museum`, per `case-template.md`'s own worked example for this case), `verification: in-progress` (not a valid `verification_status`; should be `provisional`), `decision_owner: founder-self` (not in the vocab; should be `collector-alone`). Named explicitly in the 2026-08-16 and 2026-08-17 QA reports and again in yesterday's hygiene report (`company/hygiene-report.md:27`), which additionally notes McNay is still not folded into `report-dataset.md`'s coded 50-case master list — yet `report-dataset.md`'s own Pattern 1 narrative (line 184) cites "McNay's self-perpetuating board" as supporting evidence for the report's central governance-survival claim, while McNay's own file explicitly carries `status: founder-review`, an unread will, and `case-template.md`'s own worked example warns "prose must not outrun research" for this specific case. Pattern 14, the newer counted table, correctly excludes McNay; Pattern 1's older prose does not. **Fix:** sync the frontmatter (values already documented in the file's own template example) and either fold McNay into the numbered dataset or drop it from Pattern 1's supporting-example list until it is.

4. **`cases/neue-galerie.md`'s `decision_owner: founder-self` remains invalid, unresolved for a second consecutive audit.** The 2026-08-17 hygiene sweep (`7021fa9`) corrected this file's `pathway` and `outcome` but left `decision_owner` untouched; `report-dataset.md` #3 already codes this case `collector-alone`. **Fix:** one-line frontmatter edit, value already known.

5. **`cases/moma.md` still carries two values outside `case-template.md`'s controlled vocabulary** — `collection_coherence: absorbed` and `decision_owner: collective-founders-trustees`. Flagged 2026-08-17 as a schema gap rather than a coding error (both describe a real pattern — MoMA's multi-founder, absorbed-collection structure — the vocabulary has no slot for). Still unresolved either way. **Fix:** amend `case-template.md` to add these values, or remap to the nearest existing value with a flagged caveat.

6. **`verification: spot-verified` continues to be applied uniformly across the Primary-verification backlog, now including this run's narrowed items, with no definition in `case-template.md` distinguishing it from `Provisional`.** Confirmed again in `marciano.md`, `jpmorgan-chase-collection.md`, `cam-raleigh.md`, `kreeger-museum.md`, and `pearlman-foundation.md` — all five explicitly note in their own opening paragraph that every quantitative figure is WebSearch-snippet synthesis, `secondary` throughout, not a direct fetch. No individual figure overstates its own confidence (each is honestly tagged inline), so this sits in the same gray zone flagged last audit rather than a fresh violation, but the backlog keeps growing without the tier ever being defined. **Fix:** add a one-line definition of `Spot-verified` to `case-template.md` (e.g., "narrative facts cross-checked across ≥2 independent secondary sources, no direct primary fetch"), or downgrade WebSearch-only cases to `Provisional` until a primary source is pulled.

---

## MINOR

7. **`marketing/website.md` still has em dashes in its "finalized copy" blocks, unresolved for a fifth consecutive audit** (lines 48-49, 55-57: "Nariway — Independent work on…", "The Brief Experiment — A history of…"). Yesterday's hygiene report (`company/hygiene-report.md:35`) flagged genuine ambiguity here — the em-dash-as-label-separator construction is used throughout the vault's own internal formatting, including `voice.md`'s own title — so this may be a false positive on a literal reading of the rule rather than a real voice break. Noting it again without escalating, pending Alina's call on whether the construction is in scope.

8. **`research/research-program.md`** still restates the $992B/5%/$19.84T breakdown (line 38) and the 72%/90%/80% retention figures (line 78) inline rather than linking to `[[claims-register]]` C1/C3/C12. No drift found this run either — the numbers still match — so this remains a standing risk, not an active error.

---

## Resolved since the last audit (noted, no action needed)

- **CRITICAL — governance-survival caveat loss (2026-08-17 finding #1), fixed.** The 88%/77% (13-of-13 vs. 10-of-13) figure now carries its "hand-selected, not a population rate, n=26" caveat everywhere it travels: `HOME.md:32`, `research/learnings-log.md:8`, and today's already-generated check-in email all state it correctly. `marketing/what-becomes-of-great-art-collections.md`'s own "Governance beats endowment" section (§3) does not restate the raw figures at all, only the qualitative pattern, which sidesteps the risk entirely.
- **`marketing/website.md` vs. `company/positioning.md` bio-number drift (2026-08-16/17 finding), resolved.** `website.md:30` now reads "visited hundreds of museums," matching `positioning.md`'s canonical Substack-About language. (Today's queued check-in email still asks Alina to resolve this as an open decision — that email was generated before the fix landed and is now stale; no vault file carries the drift anymore.)

---

**Counts:** 1 critical (new) + 1 critical (carried) / 4 should-fix / 2 minor.
