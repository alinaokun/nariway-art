# QA Report — 2026-08-31

**Verdict:** Not clean. Three CRITICAL items: two carried (the positioning-brief conflict, now a second audit unresolved and still spreading into new files; the blended-source $31T figure live on the export, now a ninth audit unchanged) and one new (today's batch of new cases reintroduced the em-dash defect a mechanical pass fixed and verified clean two audits ago). The dataset itself keeps growing cleanly — 124 coded cases, up from 121, primary-verification backlog flat at 75 rather than growing, manuscript and claims-register entries for the three new cases are well-sourced and honestly hedge open gaps.

---

## CRITICAL

### 1. CARRIED (2nd audit) — Two documents still both claim to be Nariway's canonical positioning, and the conflict is spreading rather than narrowing.
`Nariway_Company_Positioning_and_Operating_Brief_Aug_30_2026.md` still opens with **"Status: Current source of truth for the Nariway company / operations / agents Claude Code project,"** defines Nariway as a **"founder-led art estate consulting practice,"** gives Alina's title as **"Alina Okun, CPA, Founder and Art Estate Consultant"** (explicitly: "Do not use CGMA"), and frames estate attorneys/fiduciaries/trustees/families as the people Nariway works *with* directly. `company/positioning.md` — the vault's own canonical file per its header ("Website, LinkedIn, and any public copy reference THIS") and [[quality-assurance]]'s rule — states the opposite on every point: strategic advisory, "not an art advisor/dealer," bio with no CPA credential, and attorneys/wealth managers explicitly named "referral / relationship channels — **NOT customers**."

This is no longer a two-file problem. `INDEX.md` line 3 now carries a standing migration banner: *"Nariway pivoted to a professional-services firm for estate attorneys and fiduciaries. The current source of truth is [[Nariway_Business_Strategy_and_Operating_Plan_Aug_2026]], [[Nariway_Company_Positioning_and_Operating_Brief_Aug_30_2026]]..."* — declaring the conflicting brief authoritative over `company/positioning.md` at the vault's own front door, not just leaving it unresolved. And the citation pattern already flagged for `marketing/linkedin-strategy-brief.md` (since fixed) has resurfaced in a newer file: `marketing/linkedin-posts.md:3` reads *"the company positioning is `Nariway_Company_Positioning_and_Operating_Brief_Aug_30_2026.md`"* — a file created after the conflict was first flagged, still citing the wrong source.
**Standard violated:** [[positioning]]'s single-source rule; QA remit (e) single source of truth; (c) claims/positioning consistency.
**Fix:** unchanged from the prior audit — this is Alina's call, not a mechanical one. Whichever document governs, update `company/positioning.md` itself with the outcome and repoint every file (now including `marketing/linkedin-posts.md` and `INDEX.md`'s own banner) to cite `[[positioning]]` rather than a second copy.

### 2. CARRIED (9th audit) — `export/nariway-public.json:7275` and `content/content.json:54` still misattribute the wealth-transfer figure to three non-comparable sources blended into one number, live on the public site.
Unchanged verbatim across nine audits: both files still read `"value": "~$31T+"`, `"source": "wealth-research (Cerulli / UBS / Knight Frank)"`. `claims-register.md` C36 exists specifically to bar this: Deloitte/ArtTactic's ~$31T (C1's input, decade, global) is not Cerulli's $124T (US-only, through 2048, C8) or UBS's ~$83T (global, 20-25 years, per the June 2026 Global Next Generation Report); Knight Frank publishes no wealth-transfer total at all (only UHNWI population counts, C34). Blending three differently-scoped figures under one attribution is exactly the error C36 was written to stop.
**Fix:** replace the tile with the already-drafted GWT figures in `marketing/gwt-content-draft.md`, or at minimum attribute `$31T` to Deloitte/ArtTactic alone.

### 3. NEW — Today's two newest cases reintroduce live public-facing em dashes, undoing the fix verified clean across the whole dataset two audits ago.
The 2026-08-29 audit closed a five-consecutive-audit finding (25 em dashes across 24 files) with a mechanical pass, and the 2026-08-30 audit confirmed a fresh grep of every `public_*` field found zero. That is no longer true. `cases/lee-kun-hee-collection.md` (`public_page_eligible: true`, `public_verified: true` — i.e. exported) carries two em dashes in `public_origin` ("...one of the largest private art collections ever assembled — built up across his and his father's generations — alongside...") and one more in `public_pathway_timeline`'s 2021 event text ("...23,181 works — ~1,500 to MMCA..."). Both are confirmed live in `export/nariway-public.json`'s `collections[].origin` and `.classification.pathwayTimeline[].event` fields for `lee-kun-hee-collection`, not just in the source frontmatter. A third, milder instance sits in `cases/unicredit-art-collection.md`'s `public_location` field (a parenthetical em dash). No other case in the dataset carries this defect — it is confined to today's two new cases, not a broader regression.
**Standard violated:** [[voice]] / [[ai-tells]], no em dashes in prose, applied to public-facing copy per QA remit (d); the same standard the 2026-08-29 fix pass already established for exactly this field type.
**Fix:** replace both em dashes in `lee-kun-hee-collection.md`'s `public_origin` and the one in its `public_pathway_timeline` event with commas or a restructured sentence; fix the `unicredit-art-collection.md` `public_location` em dash the same way; regenerate the export.

---

## SHOULD-FIX

### 4. CARRIED — The Fisher/SFMOMA LinkedIn post, now labeled "finalized" and "fact-checked," still collapses the 720+ vs ~1,100-works scope distinction flagged last audit.
`marketing/linkedin-posts.md`'s "Finalized posts (fact-checked, 2026-08-30)" section states the post is the "current voice and standard" for Fisher specifically. The post text is unchanged on this point: *"By the end they had more than a thousand works... in 2009, they made a deal with the San Francisco Museum of Modern Art. The museum would show the collection for 100 years."* As written, "the collection" reads back to the just-stated "more than a thousand works" figure. `claims-register.md` C53 and `cases/fisher-sfmoma.md` are both explicit that only **720+ of the ~1,100 total works** are the SFMOMA-loaned subset — the two scopes must stay labeled separately. Being marked "fact-checked" did not catch this; it is the same conflation the prior audit flagged, still live in a post now one step closer to publication.
**Fix:** before this post is scheduled, either state the loan figure as 720+ works or drop "more than a thousand" from the sentence that leads into the loan.

---

## MINOR

### 5. CARRIED — the `origin` frontmatter field is still split across multiple values with no definition in `case-template.md`.
Current usage: `private-individual` (27) · `private` (14) · `corporate` (14) · `artist` (4, including today's new `hilma-af-klint-foundation`, still undocumented).
**Fix:** pick one value for the private side, normalize, and document all values including `artist` in `case-template.md`.

### 6. CARRIED — corporate-continuity vocabulary still fragmented.
`bank-of-america-collection.md`, `credit-suisse-ubs-collection.md`, `deutsche-bank-collection.md`, `jpmorgan-chase-collection.md`, and `ubs-art-collection.md` use `parent-entity-continuity`; `enron-art-collection.md` and `lehman-brothers-collection.md` use `parent-entity-survival` for the same underlying concept.
**Fix:** adopt one term; add it as an authorized value in `case-template.md`.

---

## Checked, no issue found
- **Primary-verification backlog**: flat at 75 numbered items this run (three new cases added zero — none files a US 990 of any kind), against a dataset that grew from 121 to 124. No longer outpacing case-count growth as it briefly did two audits ago; no action needed.
- **New case sourcing** (`lee-kun-hee-collection.md`, `unicredit-art-collection.md`, `hilma-af-klint-foundation.md`): every quantitative and governance claim carries a source and confidence tag or an explicit `unknown`; no bare numbers presented as fact. `hilma-af-klint-foundation.md` also correctly carries forward its own correction to `claims-register.md` C47 (the settlement resolves litigation, not confirmed to resolve the underlying Zwirner deal) — C47 itself already reflects the revision.
- **Over-claiming**: the manuscript's findings section still explicitly disclaims rate/percentage claims off the hand-selected case set, and this run's two new manuscript paragraphs (Lee Kun-hee, UniCredit) are appropriately hedged ("a genuine, if narrow, counter-example," "a reminder," no overstated pattern language).
- **Decisions folder**: no settled decision found still marked open; the one `_open_` line (2026-08-14 board membership) is honestly about an in-progress shortlist search, not an unrecorded decision, unchanged from the prior audit's finding.

---

## Resolved since the 2026-08-30 audit
- The five drafted LinkedIn posts' "manufactured conclusion" closing lines (SHOULD-FIX #4 last audit): fixed. All five finalized posts now end on a concrete fact or image, not a stated moral.

---

**Counts:** 3 critical (2 carried, 1 new) / 1 should-fix (carried) / 2 minor (both carried) — against 1 item resolved since the last audit.
