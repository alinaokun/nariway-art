# QA Report — 2026-09-02

**Verdict:** Not clean. The same three CRITICAL items carry forward unresolved, and one of them — the em-dash defect in exported public copy — has gotten materially worse, tripling from 4 to 12 live instances and now present in 5 of the 6 cases coded since the last audit. The dataset itself keeps growing cleanly: 135 coded cases, up from 129, sourcing and hedging discipline on all six new cases is sound, and the primary-verification backlog is flat in proportion (77/135 ≈ 57%, versus 75/129 ≈ 58%).

---

## CRITICAL

### 1. CARRIED (4th audit) — Two documents still both claim to be Nariway's canonical positioning; still unresolved.
`Nariway_Company_Positioning_and_Operating_Brief_Aug_30_2026.md` still opens "Status: Current source of truth," defines Nariway as a "founder-led art estate consulting practice," and gives Alina's title as "Alina Okun, CPA, Founder and Art Estate Consultant" (lines 15-16, 58, 193, 980). `company/positioning.md` — the vault's own canonical file by its own header and by [[quality-assurance]]'s rule — still states the opposite: strategic advisory, "not an art advisor/dealer," no CPA in the bio, attorneys/wealth managers explicitly "referral / relationship channels — NOT customers." `INDEX.md` line 3 still carries the migration banner naming the conflicting brief authoritative. No file in `company/decisions/` (still five files, all unrelated: email delivery, Opal summit, Sotheby's course, board membership, retiring the daily check-in) records this pivot as settled. `marketing/linkedin-posts.md:3` still cites the second brief as "the company positioning" instead of `[[positioning]]`. Every live public-facing copy source checked this run (`company/positioning.md`, `marketing/substack.md`, `marketing/linkedin.md`, `marketing/website.md`) remains internally consistent with the research/advisory positioning, not the estate-consulting brief — so the vault is still carrying two irreconcilable definitions of the company at its center, unresolved for a fourth consecutive audit.
**Standard violated:** [[positioning]]'s single-source rule; QA remit (e) single source of truth; (c) claims/positioning consistency.
**Fix:** unchanged — this is Alina's call, not a mechanical one. Whichever document governs, update `company/positioning.md` itself with the outcome, log it in `company/decisions/`, and repoint every file that still cites the second brief (including `marketing/linkedin-posts.md` and `INDEX.md`'s own banner) to `[[positioning]]`.

### 2. CARRIED (11th audit) — `export/nariway-public.json:8040-8042` and `content/content.json:54` still misattribute the wealth-transfer figure to three non-comparable sources blended into one number, live on the public site.
Unchanged verbatim across eleven audits: both files still read `"value": "~$31T+"`, `"source": "wealth-research (Cerulli / UBS / Knight Frank)"`. `claims-register.md` C36 exists specifically to bar this: Deloitte/ArtTactic's ~$31T (C1's input, decade, global) is not Cerulli's $124T (US-only, through 2048, C8) or UBS's ~$83T (global, 20-25 years); Knight Frank publishes no wealth-transfer total at all (only UHNWI population counts, C34). Blending three differently-scoped figures under one attribution is exactly the error C36 was written to stop.
**Fix:** replace the tile with the already-drafted GWT figures in `marketing/gwt-content-draft.md`, or at minimum attribute `$31T` to Deloitte/ArtTactic alone.

### 3. CARRIED (3rd→4th audit) and worse — the em-dash fix called for twice now was never made, and the defect has spread to most of the newest batch of cases.
Last audit flagged four live em dashes in exported `public_*` fields: `cases/lee-kun-hee-collection.md` `public_origin` (×2) and `public_pathway_timeline`, `cases/unicredit-art-collection.md` `public_location`, and `cases/hsbc-art-collection.md` `public_origin`. **None of the five was fixed** — all still carry the identical em dashes verbatim. Worse, five of the six cases coded across the two research runs since the last audit add **eight new instances**:
- `cases/malba-costantini.md:20` `public_name` — "MALBA — Museo de Arte Latinoamericano de Buenos Aires"
- `cases/monte-dei-paschi-collection.md:20` `public_name` — "Banca Monte dei Paschi di Siena — Historical Art Collection"
- `cases/monte-dei-paschi-collection.md:32` `public_pathway_timeline` — "...taking a 68% stake — the art collection is not liquidated"
- `cases/monte-dei-paschi-collection.md:33` `public_origin` — "...and the collection — still centered on the Sienese School — has remained..."
- `cases/schnitzer-family-foundation.md:34` `public_origin` — "...as a circulating lending library — placing works with museums..."
- `cases/standard-bank-art-collection.md:33` `public_pathway_timeline` — "...Robert Stewart — the collection's earliest recorded work"
- `cases/yemisi-shyllon-museum-of-art.md:31` `public_origin` — "...to establish the Yemisi Shyllon Museum of Art — the first privately funded art museum..."

That is **12 live em dashes across 8 case files, exported to the public site**, up from 4 across 3 files last audit — the defect has more than tripled and is now the default, not the exception, in newly-coded `public_origin`/`public_pathway_timeline`/`public_name` text (only `barjeel-art-foundation.md`, the sixth new case, is clean). The research/coding process is generating this defect faster than the standing fix instruction is closing it.
**Standard violated:** [[voice]] / [[ai-tells]], no em dashes in prose, applied to public-facing copy per QA remit (d) — these fields populate the live `nariway-public.json` export per `case-template.md`'s public-projection-layer contract.
**Fix:** replace all 12 em dashes with commas or restructured sentences (title fields like `public_name` can drop the appositive or use a comma: "MALBA, Museo de Arte Latinoamericano de Buenos Aires"); regenerate the export; then add an em-dash check to the case-coding step itself, not just the audit, since a post-hoc catch has now failed twice in a row while the underlying process keeps producing more instances than it fixes.

---

## SHOULD-FIX

### 4. CARRIED (3rd audit) — The Fisher/SFMOMA LinkedIn post, still labeled "finalized" and "fact-checked," still collapses the 720+ vs ~1,100-works scope distinction.
`marketing/linkedin-posts.md:44-58` is unchanged from the prior two audits: "By the end they had more than a thousand works..." (line 48) leads directly into "...in 2009, they made a deal with the San Francisco Museum of Modern Art. The museum would show the collection for 100 years" (line 52), so "the collection" reads back to the just-stated thousand-plus figure. `claims-register.md`'s Fisher/SFMOMA entry (C53) and `cases/fisher-sfmoma.md` are both explicit that only **720+ of the ~1,100 total works** are the SFMOMA-loaned subset, and the two scopes must stay labeled separately.
**Fix:** before this post is scheduled, either state the loan figure as 720+ works or drop "more than a thousand" from the sentence that leads into the loan.

---

## MINOR

### 5. CARRIED, worse — the `origin` frontmatter field now spans five values, still undocumented in `case-template.md`.
Current usage: `private-individual` (29) · `corporate` (18) · `private` (14) · `individual` (5, up from 3 — `schnitzer-family-foundation.md` is a new instance of the same drift) · `artist` (4). No new case this run introduced a sixth value, but the pre-existing fragmentation was not consolidated either.
**Fix:** pick one value for the private side, normalize across all five variants, and document all authorized values (including `artist`) in `case-template.md`.

### 6. CARRIED — corporate-continuity vocabulary still fragmented.
`bank-of-america-collection.md`, `credit-suisse-ubs-collection.md`, `deutsche-bank-collection.md`, `jpmorgan-chase-collection.md`, and `ubs-art-collection.md` use `parent-entity-continuity`; `enron-art-collection.md` and `lehman-brothers-collection.md` use `parent-entity-survival` for the same underlying concept.
**Fix:** adopt one term; add it as an authorized value in `case-template.md`.

### 7. CARRIED — `primary_friction` schema gap keeps recurring, now flagged a third time by the research process itself.
`cases/benini.md` (`unknown`, not an authorized value) and `cases/rauschenberg-foundation-hq.md` (`funding-optimization`, not an authorized value) are unchanged since the last audit. `cases/unicredit-art-collection.md` (coded 2026-08-31, before the last audit but not previously called out here) independently flags the identical gap — a "voluntary, non-distress reallocation" shape with no clean fit in the controlled list — for a third distinct case. This is now a self-identified, recurring template gap, not an isolated coding error.
**Fix:** recode `benini.md` to `none-documented` if no friction is actually documented (the template has no `unknown` state for this field), or add `unknown` to the controlled list if the distinction from `none-documented` is intentional; add an authorized value (e.g. `voluntary-optimization` or similar) for the reallocation-from-strength shape `rauschenberg-foundation-hq.md` and `unicredit-art-collection.md` both independently hit, rather than leaving each case to flag it individually.

---

## Checked, no issue found
- **New case sourcing** (`barjeel-art-foundation.md`, `standard-bank-art-collection.md`, `yemisi-shyllon-museum-of-art.md`, `monte-dei-paschi-collection.md`, `schnitzer-family-foundation.md`, `malba-costantini.md`): every quantitative and governance claim carries a source and confidence tag or an explicit `unknown`; no bare numbers presented as fact. `verification_status` tags (`Provisional`/`Spot-verified`) match their actual sourcing depth per the template's definitions.
- **Primary-verification backlog**: 77 numbered items across 135 coded cases (≈57%), essentially flat against 75/129 (≈58%) last audit — growing in line with, not faster than, case-count growth.
- **Over-claiming**: this run's new manuscript findings (the Monte dei Paschi/Lehman disconfirmation pairing, the Schnitzer/MALBA pathway additions, the Louvre/Lloyd's insurance-ceiling pairing) are all appropriately hedged ("a real, narrowing disconfirmation," "not yet resolvable," "two well-documented cases, not a rate"); no rate or percentage claim runs off the hand-selected case set as fact.
- **Claims consistency**: the two new claims-register entries this window (C82 Louvre heist, C83 Willis/Circle Asia facility) match their citations in `marketing/what-becomes-of-great-art-collections.md` §4.4 exactly; no drift found.
- **Single source of truth**: `marketing/substack.md` and `marketing/linkedin.md` continue to point to `[[positioning]]` rather than keeping their own copy.
- **Decisions folder**: no settled decision found still marked open.

---

## Resolved since the 2026-09-01 audit
None. All three CRITICAL items and the one SHOULD-FIX item are still open; nothing on the carried list closed this run, and CRITICAL #3 regressed.

---

**Counts:** 3 critical (all carried, 1 worse) / 1 should-fix (carried) / 3 minor (carried) — 0 items resolved since the last audit.
