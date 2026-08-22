# QA Report — 2026-08-22

**Verdict:** Not clean. Two CRITICALs carry over for a sixth audit, and three new ones surfaced in work committed since the last run, including the first outright breach of the "no rates off the hand-selected set" rule and a canonical-number contradiction inside the vault's own $992B scope note. Case-level sourcing discipline remains strong (the three new Batch 19 cases and every net-assets-to-opex ratio in the vault are clean), and the new public-projection layer is well-built; the damage is concentrated in the flagship manuscript's prose and in two research files.

---

## CRITICAL

### 1. NEW — `marketing/what-becomes-of-great-art-collections.md` line 133 publishes rates off the hand-selected case set, which the dataset's own standing rule forbids.
The manuscript states: *"found built-institution pathways succeeding **92% of the time** (23 of 25 cases with a settled outcome), statistically indistinguishable from lighter models' **90%** (9 of 10)."*

`company/quality-assurance.md` item 2 and `cases/report-dataset.md`'s own header both state the rule absolutely. The dataset header's closing sentence reads: *"Hand-selected set for variation, not a random sample; **no rates are published off it**."* The same header (line 7) then states the 92%/90% rates itself, so the file contradicts its own rule internally.

Two further problems compound it. **"Statistically indistinguishable"** is an inferential claim with no test behind it, and a deliberately variation-selected sample of n=25 and n=10 cannot support one in principle. And the underlying counts were computed at 67 coded cases; the set is now 73, and the 25/10 denominators were never recomputed, so the manuscript's "across the coded dataset" no longer describes the dataset.

The paragraph does carry a survivorship-bias caveat, but the standard bars publishing the rate, not publishing an uncaveated rate. `research/what-we-now-believe.md` handles the same finding correctly as internal evidence tracking, with confidence, caveats and a flip condition; that treatment is fine and should stay.

**Fix:** in the manuscript, state raw counts and drop both percentages and the statistical-equivalence language, e.g. *"only two of the twenty-five built institutions with a settled outcome have failed, against one of ten lighter models."* Remove the rates from `report-dataset.md`'s header for the same reason. Keep the full treatment in `what-we-now-believe.md`.

### 2. NEW — `research/transfer-scope-note.md` line 10 contradicts claims-register C6, misstating the art market's size by roughly 2.4x.
The line reads: *"Global art *auction* turnover is only ~$60B/yr."* C6's canonical figure is *"Global art market sales ≈ **$59.6B in 2025** (~$34.8B dealers, ~$24.8B auction)."* The ~$60B figure is the **whole market**, dealers included; auction alone is ~$24.8B. The italicised *auction* makes this a deliberate scoping, not a typo.

This matters more than a stray number. `transfer-scope-note.md` is the file `claims-register` cites as the source for C1, C2 and C3, and this sentence is the load-bearing comparison behind the report's central "the $992B is transfer, not a sale wave" argument. Standard violated: claims-register C6, and the register's own convention that a canonical number is never independently restated.

**Fix:** *"Global art market sales are only ~$59.6B/yr in total, of which auction is ~$24.8B (see [[claims-register]] C6)."*

### 3. NEW — `marketing/what-becomes-of-great-art-collections.md` line 21 states a hypothesis as a settled key finding.
Key finding 1 ends: *"The decision is **almost always** unmanaged, not planned."*

No source in the vault supports that frequency. `research/transfer-scope-note.md` line 21 explicitly says *"Retained **and** unmanaged" is a **hypothesis to investigate**, not a finding."* `research/research-program.md` rates H1 *"Initial evidence against / restate"* and gives the defensible wording as *"the transition is **typically** unmanaged."* Standard violated: `quality-assurance.md` item 2 (patterns stated no more strongly than the evidence supports; hypotheses labeled provisional).

**Fix:** replace "almost always" with "typically", matching H1's own restated wording. One word.

### 4. CARRIED (sixth consecutive audit, text unchanged) — `marketing/what-becomes-of-great-art-collections.md` line 68 asserts the exact C10 reading the register forbids.
*"The surrounding financial industry has noticed, which is why art services inside wealth management have roughly doubled since 2011."* C10's do-not-say line: *"wealth-manager art-service adoption has risen steadily since 2011 — the most recent two-year window (2023-2025) moved the other way."* The "which is why" adds a causal frame on top, and the same file states the figure correctly twice elsewhere (line 66's Table 1 and line 210's *"has, if anything, recently retreated, from 63% of firms in 2023 to 51% in 2025"*), so this is one file carrying three restatements, one of them forbidden.

**Fix:** adopt the line-210 framing, e.g. *"The surrounding financial industry has noticed, even as its actual delivery of art services recently pulled back (C10)."*

### 5. CARRIED (sixth consecutive audit, text unchanged) — live, published Substack copy mirrored in `company/positioning.md` breaks the staccato and fragment-stack rules.
- Line 61 (Substack About, marked *LIVE as published 2026-08-16*): *"Some collections stay in families for generations. Some become museums or foundations. Some are given or lent to existing institutions. Some travel. Some are divided or sold. Some disappear from public view."* Six short parallel sentences, against `voice.md`'s *"Never three or more short sentences in a row."*
- Line 91 (Substack Welcome, same marking): *"Does it stay in the family? Become a museum or foundation? Go to an existing institution? Travel? Get divided or sold?"* Four subject-less fragments in a row, against `ai-tells.md` #2.

Both blocks are explicitly labelled mirrors of live pages, so this is the only finding in this report sitting on copy the public can read today. Standards violated: `voice.md` craft standards, which that file calls *"mechanical and non-negotiable"*.

**Fix:** vary sentence shape or collapse each list into fuller sentences, on the live Substack pages and in `positioning.md` together, per the file's own mirror rule.

---

## SHOULD-FIX

### 6. NEW — `cases/lucas-museum.md` carries `verification: press-sourced`, a value outside the controlled vocabulary, in a field the Cases base renders as a column.
`case-template.md` line 9 permits exactly three values: `Provisional` · `Spot-verified` · `Primary-verified`. `cases/Cases.base` lists `verification` in its Pipeline table order, so a stray value shows up as its own column value in the base. The export gate in `collection-index-build-brief.md` is an allow-list (`verification: primary-verified`), so this fails safe and will not leak, but the vocabulary is still breached.

**Fix:** recode to `provisional` (the file's own body already says *"figures below are press-sourced, verify before asserting"*), or amend `case-template.md` to admit `press-sourced` as a fourth value.

### 7. NEW — the superseded 65% IRS Art Advisory Panel rate is still stated as current in two research files, contradicting C31 and, in one case, contradicting the same file 69 lines later.
C31 fixes the current figure at **63% of items adjusted (157 of 251), FY2023**, with an **18% aggregate decrease**, and instructs *"cite C31 going forward."*
- `research/market-intelligence.md` line 190 still calls 2012 *"the most recent year for which a public tally could be found"* and reports **65%** with a mean adjustment of **+18%** — both the vintage claim and the direction are wrong, and line 259 of the same file already records that C31 supersedes it. Line 225 then restates *"65% of audited appraisals adjusted"* as a live recommendation for report §4.4, with no dated flag at all.
- `research/learnings-log.md` line 10 states *"the IRS Art Advisory Panel's 65% appraisal-adjustment rate"* with no vintage and no superseded marker, so it reads as current.

**Fix:** add a superseded-by-C31 banner to market-intelligence #8's Panel paragraph and keep 65%/2012 only as a labelled longer-run reference point; correct the "+18%" direction; re-point line 225 and learnings-log line 10 to C31's 63% (FY2023).

### 8. NEW — `marketing/what-becomes-of-great-art-collections.md` line 161 cites Table 1 for two figures Table 1 does not contain.
The C36 guardrail paragraph, the one place the report warns against conflating non-comparable transfer totals, reads *"alongside the ~$31T (Deloitte, Table 1) and $124T (Cerulli, Table 1) figures already used here."* Table 1 (lines 59-66) contains $992B, $2.56T→$3.47T, $54T, 72%, 80% and 51%. Neither $31T nor $124T appears in Table 1 or anywhere else in the manuscript, so "already used here" is also false. The C36 substance is stated correctly; only the cross-reference is broken.

**Fix:** change the parentheticals to "(Deloitte, C1's underlying input)" and "(Cerulli, C8)", and drop "already used here" or add both figures to Table 1.

### 9. CARRIED (seventh consecutive audit) — the primary-verification backlog reached 47 items and still has no ceiling, pace, or resolution plan, and `Spot-verified` is still undefined.
The backlog in `cases/report-dataset.md` now runs to item 47, up from 41, 38, 35 and 27 across recent runs. **This audit independently re-tested WebFetch** against `projects.propublica.org` and got `EGRESS_BLOCKED`, the twentieth consecutive confirmation and the first from outside the research agent's own session, so the constraint is real and not agent negligence. No individual case overstates its confidence tier, and every new figure is still correctly tagged `secondary`.

Two things still need deciding. `case-template.md` lists `Spot-verified` as an allowed value but never defines what distinguishes it from `Provisional` — flagged for a seventh audit, and now load-bearing, because 65 of 75 cases carry it while their own files describe them as WebSearch-snippet synthesis. Separately, the export gate requires `verification: primary-verified`, and **no case in the vault carries that value**, so the public export as currently specified would emit zero collections, including all four proof-set cases marked `public_page_eligible: true`.

**Fix:** define `Spot-verified` in `case-template.md`; and either set an explicit pace at which runs prioritise primary upgrades over new cases if WebFetch stays blocked past a threshold, or widen the export gate to the "non-numeric/structural figures" carve-out `case-template.md` already contemplates.

### 10. NEW — `marketing/website.md` line 21 asserts the canonical Bio is live while recording different live wording.
The line says the canonical first-person bio *"is now live here"*, then records the live wording as *"In recent years, research and writing have become a greater focus of my work."* The canonical Bio at `company/positioning.md` line 22 reads *"Over time, research and writing became an increasingly important part of my work."* Same sentence, two texts, captured by direct scrape 2026-08-19. The vault claims a match that does not exist. Standard violated: `quality-assurance.md` item 4 (single source of truth).

**Fix:** reconcile against the live page, correct whichever side is wrong, and reduce website.md line 21 to a pointer carrying no quoted wording.

### 11. ESCALATED from minor — `marketing/website.md` line 16's reconciliation note is not merely stale, it now instructs an action that would destroy canonical copy.
The note reads: *"the live hero/section copy differs from the canonical public copy in [[positioning]]... Align positioning to the live copy when convenient."* That no longer holds. `positioning.md` lines 29-37 are already a 2026-08-19 mirror of the live site, and website.md's own hero capture matches it word for word. The one divergence that does remain runs the opposite way: `positioning.md` line 39 records that the live third-person founder bio should be **replaced with** the canonical first-person Bio. Following this note would overwrite the canonical Bio with the very text positioning has scheduled for removal.

**Fix:** delete the note, or replace it with a pointer to the single open item already tracked at `positioning.md` line 39.

### 12. NEW — `marketing/substack-notes-queue.md` line 14 ends on a manufactured conclusion, in a file that claims all four closings were already fixed.
Note 1 (Norman Rockwell) closes: *"The covers everyone remembers as pure comfort were made by a man in real pain."* The line adds no new fact; it restates the opening juxtaposition and explains what the story means, in the comfort-versus-pain antithesis shape. `voice.md`'s Notes rule: *"End on a concrete fact or image, never a manufactured conclusion... If a closing line explains what the story means, cut it and let the last fact land."* Line 7 of the same file states *"Fixed 2026-08-17 (QA finding #6): all four closings rewritten... Ready to post as drafted"*, so this one was missed and is queued to publish as-is.

**Fix:** cut the sentence and let beat two end on *"He spent his life battling a darkness he was painting his way out of"*, or substitute a concrete fact.

### 13. CARRIED (ninth consecutive audit) — `cases/mcnay.md` is cited as supporting evidence in `report-dataset.md` Pattern 1 while still sitting outside the numbered dataset at `status: founder-review`.
Pattern 1 cites *"McNay's self-perpetuating board"* among the survivors supporting the central governance-survival claim, while `cases/mcnay.md` remains the only case at `status: founder-review` and is absent from the numbered case list, even after this run's Batch 19 integrity reconciliation folded in three other stragglers.

**Fix:** fold McNay into the numbered dataset once its research clears founder-review, or drop it from Pattern 1's supporting-example list until then.

### 14. CARRIED (sixth consecutive audit) — `cases/moma.md` carries two values outside the controlled vocabulary.
`collection_coherence: absorbed` and `decision_owner: collective-founders-trustees`. Both describe a real pattern MoMA's multi-founder, absorbed-collection structure exhibits and the vocabulary has no slot for; a schema gap, not a coding error.

**Fix:** amend `case-template.md` to admit these values, or remap to the nearest existing value with a flagged caveat.

---

## MINOR

### 15. The `origin` frontmatter field has drifted into two values for one concept, and is defined nowhere.
Across the case files: `origin: corporate` (11), `origin: private-individual` (9), `origin: private` (6). The last two appear to mean the same thing, and the split is not chronological (the newest Batch 19 cases use `private-individual`, several Batch 16-17 cases use `private`). `case-template.md` never defines an `origin` vocabulary at all; only `research/research-program.md` uses the term, in prose. `origin` is not a `Cases.base` column, so nothing renders wrong today, but the corporate sub-population is described as *"a separate, tagged sub-population"* and the tagging cannot be relied on while the private side has two spellings. **Fix:** pick one value, normalise, and add the vocabulary to `case-template.md`.

### 16. Two nits in the new public-projection layer, both in export-bound content.
`cases/lucas-museum.md`'s public `focus` field contains an em dash (*"narrative art — illustration, comic art..."*), against the standing no-em-dash rule; the structural `·` and `—` separators in the pathway-timeline rows are fine, since those are field delimiters rather than prose. Separately, `cases/chinati.md`'s *"Why in the sample"* paragraph, which cites H4 and H8 by name, sits **inside** the `## Public profile` block that `case-template.md` designates as the export's body source; internal hypothesis rationale should sit below it. Neither can leak today, because the export gate holds both files back. **Fix:** comma or restructure the Lucas focus line; move the Chinati paragraph out of the public block.

### 17. `marketing/website.md`'s archived copy blocks carry stale action labels and em dashes.
The `alinaokun.com` "finalized copy" block uses six em dashes as name/description separators (carried, ninth audit; likely benign label usage, still unresolved as a scope question). More usefully: the nariway.com block is still headed *"(ready to publish)"* and the file's closing "Next step" still says *"Swap nariway.com to the interim page above within a few days"*, though line 5 records the site as fully rebuilt and live since 2026-08-19. Only the line-28 historical banner prevents someone acting on superseded instructions. **Fix:** strike the stale labels and the superseded Next step block.

### 18. Two stale cross-references worth a sweep.
`finance/cfo-brief.md` line 44 flags Table 1 for citing C10 *"as settled"* and says the register calls the trend direction possibly backwards; neither is true any more (Table 1 now carries the corrected framing, and C10 states the decline as fact), and the real open C10 breach is line 68, so the watch item points at the wrong line. `crm/partners/Dawn Mari La Monica.md` line 36 fuses C1 and C8 into *"the ~$1T art transfer is happening now, mostly to surviving spouses"* — that imports a regional split C1 forbids and collapses the decade horizon; the file is marked CLOSED, but the line is written as a phrase to say aloud.

### 19. `marketing/substack-notes-queue.md` line 41 (Magritte) may have the same closing problem as finding 12, at lower confidence.
*"He wanted you to stand in front of a picture and never be sure what it meant."* Neither a concrete fact nor an image, and it restates beat two. Dismissible if read as a fact about the artist's intent. Noted rather than asserted.

### 20. `origin/main` was force-updated, dropping 51 commits from the remote's reachable history.
This audit's fetch reported `+ eda9297...efe16b6 main -> origin/main (forced update)`. The 51 commits on the superseded line are no longer ancestors of `main`. **No content was lost** — a tree diff shows no deleted files and only small in-file line replacements, and the current history carries the same work at a later stage (the superseded tip was *"Matthew Erskine CONFIRMED"*; current `main` contains *"Matthew Erskine Conversation PUBLISHED"*). Flagged only because `git log` is no longer a complete audit trail of what changed and when, which is the mechanism this audit and `vault-hygiene` both rely on. No action needed on content.

---

## Clean this run (checked, no findings)

- **The three new Batch 19 cases** (`ganz-collection`, `rennie-collection`, `kohler-art-preserve`) show disciplined sourcing throughout: every quantitative field carries a `[source: ...; confidence]` tag or an explicit `unknown`/`n/a` with a stated structural reason, and each file names its own schema strain rather than coding through it (Ganz's "financial success and institutional failure are simultaneously true" vocabulary gap; Kohler's museum-director-as-founder edge case, explicitly flagged for `case-template` review rather than resolved unilaterally).
- **Every `net_assets_to_opex_ratio` in the vault** is either labelled UPPER BOUND, marked not computable, or explicitly `unknown`/`n/a` with a reason. No unlabelled ratio found anywhere.
- **C1, C2, C3, C4, C8 and C31's manuscript restatement** are consistent everywhere they appear; the $992B figure matches canon across `positioning.md`, `website.md`, `pitch-deck.md` and the manuscript, no "6% ⇒ donation is rare" restatement survives anywhere, retention and unmanagedness are kept separate outside the one instance at finding 3, and 9.3x appears only with its UPPER BOUND label and never as endowment coverage.
- **Case frontmatter controlled vocabularies** (`pathway`, `outcome`, `founder_status`, `status`) checked in bulk across all case files and found within the allowed vocabulary, aside from the two exceptions at findings 6 and 14.
- **`marketing/linkedin.md`** is the model for single-source discipline: it holds no local copy and points to `positioning.md` throughout. `marketing/substack.md` mirrors the canonical headline and description exactly, correctly labelled.
- **`company/decisions/`** contains no settled decision still marked open; the 2026-08-14 board-membership decision's open status remains legitimate, as no board has been selected.

---

**Counts:** 5 critical (2 carried, 3 new) / 9 should-fix (3 carried, 1 escalated, 5 new) / 6 minor.
