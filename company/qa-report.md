# QA Report — 2026-09-01

**Verdict:** Not clean. Three CRITICAL items, all carried from the last audit and none resolved: the positioning-brief conflict (now spreading, not narrowing), the blended-source $31T figure live on the export (10th audit unchanged), and the public-facing em-dash defect (unfixed since being flagged last audit, and now present in a further new case). The dataset itself keeps growing cleanly — 129 coded cases, up from 124, primary-verification backlog flat at 75, sourcing and hedging on the five new cases are sound.

---

## CRITICAL

### 1. CARRIED (3rd audit) — Two documents still both claim to be Nariway's canonical positioning, and the conflict has hardened rather than resolved.
`Nariway_Company_Positioning_and_Operating_Brief_Aug_30_2026.md` still opens "Status: Current source of truth for the Nariway company / operations / agents Claude Code project," defines Nariway as a "founder-led art estate consulting practice," and gives Alina's title as "Alina Okun, CPA, Founder and Art Estate Consultant." `company/positioning.md` — the vault's own canonical file per its own header ("Website, LinkedIn, and any public copy reference THIS") and [[quality-assurance]]'s rule — still states the opposite on every point: strategic advisory, "not an art advisor/dealer," no CPA in the bio, attorneys/wealth managers explicitly "referral / relationship channels — NOT customers." `INDEX.md` line 3 still carries the standing migration banner naming the conflicting brief authoritative over `company/positioning.md`. No decision file in `company/decisions/` records this pivot as settled (the folder's five files are unrelated: email delivery, Opal summit, Sotheby's course, board membership, retiring the daily check-in). `marketing/linkedin-posts.md:3` still cites the second brief as "the company positioning" rather than `[[positioning]]`. Meanwhile every live public-facing copy source checked this run — `company/positioning.md`, `marketing/substack.md`, `marketing/linkedin.md`, `marketing/website.md` — is internally consistent with itself and with the research/advisory positioning, not the estate-consulting brief. So the vault is not drifting at the edges; it is carrying two irreconcilable definitions of the company at its center, and the newer one is winning by default (INDEX's banner) without ever having been written into `positioning.md` itself or logged as a decision.
**Standard violated:** [[positioning]]'s single-source rule; QA remit (e) single source of truth; (c) claims/positioning consistency.
**Fix:** unchanged — this is Alina's call, not a mechanical one. Whichever document governs, update `company/positioning.md` itself with the outcome, log it in `company/decisions/`, and repoint every file that still cites the second brief (including `marketing/linkedin-posts.md` and `INDEX.md`'s own banner) to `[[positioning]]`.

### 2. CARRIED (10th audit) — `export/nariway-public.json:7659` and `content/content.json:54` still misattribute the wealth-transfer figure to three non-comparable sources blended into one number, live on the public site.
Unchanged verbatim across ten audits: both files still read `"value": "~$31T+"`, `"source": "wealth-research (Cerulli / UBS / Knight Frank)"`. `claims-register.md` C36 exists specifically to bar this: Deloitte/ArtTactic's ~$31T (C1's input, decade, global) is not Cerulli's $124T (US-only, through 2048, C8) or UBS's ~$83T (global, 20-25 years); Knight Frank publishes no wealth-transfer total at all (only UHNWI population counts, C34). Blending three differently-scoped figures under one attribution is exactly the error C36 was written to stop.
**Fix:** replace the tile with the already-drafted GWT figures in `marketing/gwt-content-draft.md`, or at minimum attribute `$31T` to Deloitte/ArtTactic alone.

### 3. CARRIED (2nd audit) and spreading — the em-dash fix the last audit called for was never made, and a further new case now carries the same defect.
Last audit flagged three live em dashes in exported `public_*` fields (`lee-kun-hee-collection.md`'s `public_origin` ×2 and `public_pathway_timeline`, `unicredit-art-collection.md`'s `public_location`) and asked for them to be replaced before the export regenerates. None was fixed: `cases/lee-kun-hee-collection.md:34-35` and `cases/unicredit-art-collection.md:23` all still carry the identical em dashes verbatim, unchanged since the prior audit. New this run: `cases/hsbc-art-collection.md:34` (`public_page_eligible: true`, exported) adds a fourth instance in `public_origin` ("...into a collection of more than 4,000 works spanning a century of the bank's expansion — from its Far East origins through the 1992 acquisition of Midland Bank..."). No other case in the new batch (fondation-pierre-berge-yves-saint-laurent, easton-foundation) carries this defect, so it is not a broad regression, but the fix from last audit simply did not happen, and the defect gained a new instance instead of shrinking.
**Standard violated:** [[voice]] / [[ai-tells]], no em dashes in prose, applied to public-facing copy per QA remit (d).
**Fix:** replace all four em dashes (2× `lee-kun-hee-collection.md` `public_origin`, 1× its `public_pathway_timeline` event, 1× `unicredit-art-collection.md` `public_location`, 1× `hsbc-art-collection.md` `public_origin`) with commas or restructured sentences; regenerate the export; then re-grep `^public_` fields in `cases/*.md` for `—` on the next audit to confirm this actually closes this time.

---

## SHOULD-FIX

### 4. CARRIED (2nd audit) — The Fisher/SFMOMA LinkedIn post, still labeled "finalized" and "fact-checked," still collapses the 720+ vs ~1,100-works scope distinction.
`marketing/linkedin-posts.md:44-58`, in the section still headed "Finalized posts (fact-checked, 2026-08-30)," is unchanged from the prior audit: "By the end they had more than a thousand works..." (line 48) leads directly into "...in 2009, they made a deal with the San Francisco Museum of Modern Art. The museum would show the collection for 100 years" (line 52), so "the collection" reads back to the just-stated thousand-plus figure. `claims-register.md`'s Fisher/SFMOMA entry and `cases/fisher-sfmoma.md` are both explicit that only **720+ of the ~1,100 total works** are the SFMOMA-loaned subset, and that the two scopes must stay labeled separately. Being marked "fact-checked" a second time did not catch this.
**Fix:** before this post is scheduled, either state the loan figure as 720+ works or drop "more than a thousand" from the sentence that leads into the loan.

---

## MINOR

### 5. CARRIED, and worse — the `origin` frontmatter field now spans five values, still undocumented in `case-template.md`.
Current usage: `private-individual` (27) · `corporate` (16) · `private` (14) · `artist` (4) · `individual` (3, new this run — `charles-dee-mitchell-collection.md`, `easton-foundation.md`, `fondation-pierre-berge-yves-saint-laurent.md`). Three new cases this run introduced a fifth distinct value for what appears to be the same private-individual concept, rather than reusing an existing one.
**Fix:** pick one value for the private side, normalize across all five variants, and document all authorized values (including `artist`) in `case-template.md`.

### 6. CARRIED — corporate-continuity vocabulary still fragmented.
`bank-of-america-collection.md`, `credit-suisse-ubs-collection.md`, `deutsche-bank-collection.md`, `jpmorgan-chase-collection.md`, and `ubs-art-collection.md` use `parent-entity-continuity`; `enron-art-collection.md` and `lehman-brothers-collection.md` use `parent-entity-survival` for the same underlying concept.
**Fix:** adopt one term; add it as an authorized value in `case-template.md`.

### 7. NEW — two `primary_friction` values fall outside the controlled vocabulary `case-template.md` defines.
`cases/benini.md` codes `primary_friction`: **unknown**, and `cases/rauschenberg-foundation-hq.md` codes `primary_friction`: **funding-optimization**. Neither appears in the template's authorized list (funding-gap · family-disagreement · museum-rejection · zoning · community-opposition · tax · governance-conflict · collection-incoherence · storage · conservation · staffing · founder-control · poor-attendance · succession-failure · advisor-fragmentation · construction-overrun · legal-challenge · gift-refused · none-documented). Both files predate this audit window; not a new-case regression, a pre-existing drift surfaced by this run's full vocabulary sweep.
**Fix:** recode `benini.md` to `none-documented` if no friction is actually documented (the template has no `unknown` state for this field), or add `unknown` to the controlled list if the distinction from `none-documented` is intentional; recode `rauschenberg-foundation-hq.md` to the closest authorized value or add `funding-optimization` to the list if it names a real, distinct mechanism.

---

## Checked, no issue found
- **Primary-verification backlog**: flat at 75 numbered items this run (129 coded cases, up from 124; five new cases added zero — none files a directly-fetched US 990). Growing in line with, not faster than, case-count growth.
- **New case sourcing** (`hsbc-art-collection.md`, `fondation-pierre-berge-yves-saint-laurent.md`, `easton-foundation.md`): every quantitative and governance claim carries a source and confidence tag or an explicit `unknown`; net-assets-to-opex ratios on all six new-since-last-audit cases that use the field (`american-visionary-art-museum`, `easton-foundation`, `mint-museum`, `oliver-ranch-foundation`, `price-sculpture-forest`, `reynolda-house`) are correctly labeled UPPER BOUND.
- **Over-claiming**: `marketing/what-becomes-of-great-art-collections.md`'s new findings this run (Souls Grown Deep curated-placement mechanism, Jaipur Centre for Art, the London Old Masters/scholarship case, the Storm King counter-example) are all appropriately hedged ("not yet answerable from a single case," "not yet a pattern with more than one instance"); no rate or percentage claim runs off the hand-selected case set as fact.
- **Claims consistency**: spot-checked the $992B figure (C1) across `positioning.md`, `marketing/what-becomes-of-great-art-collections.md`, and the `marketing/gwt-*` files — consistent wording and attribution everywhere it's used outside the two files already flagged under CRITICAL #2.
- **Single source of truth**: `marketing/substack.md` and `marketing/linkedin.md` both correctly point to `[[positioning]]` for live profile copy rather than keeping their own; `marketing/website.md` is explicitly marked historical/interim below its live-site summary, not duplicated live copy.
- **Decisions folder**: no settled decision found still marked open.

---

## Resolved since the 2026-08-31 audit
None. All three prior CRITICAL items and the one SHOULD-FIX item are still open; nothing on the carried list closed this run.

---

**Counts:** 3 critical (all carried) / 1 should-fix (carried) / 3 minor (2 carried, 1 new) — 0 items resolved since the last audit.
