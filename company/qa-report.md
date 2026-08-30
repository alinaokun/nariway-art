# QA Report — 2026-08-30

**Verdict:** Not clean. Four of the six findings carried from the 2026-08-29 audit are now fixed (see Resolved, below) — the dataset's own hygiene is holding up well (116 coded cases, up from 113; backlog growth is individually justified, not unbounded). But one CRITICAL item is carried an eighth straight audit, and this run surfaces a new, more serious CRITICAL: a same-day company brief that redefines what Nariway *is* now sits uncrossed against the canonical positioning file, and new marketing collateral has already started citing the wrong one.

---

## CRITICAL

### 1. NEW — Two documents both claim to be Nariway's canonical positioning, and they contradict each other.
`Nariway_Company_Positioning_and_Operating_Brief_Aug_30_2026.md` (vault root, added today by Alina directly) opens: **"Status: Current source of truth for the Nariway company / operations / agents Claude Code project."** It defines Nariway as a **"founder-led art estate consulting practice,"** gives Alina's title as **"Alina Okun, CPA, Founder and Art Estate Consultant"** (explicitly: "Do not use CGMA"), and frames the audience as "estate attorneys, fiduciaries, trustees, families, and other professional advisors when a significant art collection becomes part of an estate."

`company/positioning.md` — the vault's actual canonical positioning file per [[quality-assurance]] and its own header ("Website, LinkedIn, and any public copy reference THIS") — states the opposite on every one of those points: Nariway is **"strategic advisory / consulting — not an arts org... not an art advisor/dealer"**; the canonical bio gives no CPA credential and a different title ("Alina Okun, Founder"); the audience is framed as primarily B2C (the collector directly), with fiduciary/attorney channels named explicitly as **"referral / relationship channels — NOT customers."**

This is not a stale-doc problem, it is a live one: `marketing/linkedin-strategy-brief.md:3` already reads *"the company positioning is `Nariway_Company_Positioning_and_Operating_Brief_Aug_30_2026.md`"* — new marketing work has started pointing at the new file instead of `[[positioning]]`, the single source of truth [[quality-assurance]] and [[positioning]] itself both require. If this is a deliberate pivot, positioning.md is now the stale one; if it is not yet decided, it should not be described as "current source of truth."
**Standard violated:** [[positioning]]'s single-source rule; QA remit (e) single source of truth; (c) claims/positioning consistency.
**Fix:** Alina resolves which document governs (or how they reconcile — e.g., the root brief as the *services* layer beneath the existing public *identity* layer). Whichever way it resolves, update `company/positioning.md` itself with the outcome, and repoint `marketing/linkedin-strategy-brief.md` (and anything else already citing the root file) to `[[positioning]]` rather than a second copy.

### 2. CARRIED (8th audit) — `export/nariway-public.json:6963` and `content/content.json:54` still misattribute the wealth-transfer figure to three non-comparable sources blended into one number, live on the public site.
Unchanged verbatim across eight audits: both files still read `"value": "~$31T+"`, `"source": "wealth-research (Cerulli / UBS / Knight Frank)"`. `claims-register.md` C36 exists specifically to bar this: Deloitte/ArtTactic's ~$31T (C1's input, decade, global) is not Cerulli's $124T (US-only, through 2048, C8) or UBS's ~$83T (global, 20-25 years, C36); Knight Frank publishes no wealth-transfer total at all (only UHNWI population counts, C34).
**Fix:** replace the tile with the already-drafted GWT Block 2/3 figures in `marketing/gwt-content-draft.md`, or at minimum attribute `$31T` to Deloitte/ArtTactic alone.

---

## SHOULD-FIX

### 3. NEW — `marketing/linkedin-posts.md` post 5 (Fisher/SFMOMA) collapses a scope distinction the vault itself is careful about, before it reaches Alina.
The draft says: *"more than a thousand works by artists including Warhol, Richter, Serra, and Ellsworth Kelly... in 2009 they placed **the collection** on loan to the San Francisco Museum of Modern Art for 100 years."* As written, a reader takes the whole 1,000+-work collection to be on loan. But `cases/fisher-sfmoma.md` and `claims-register.md` C53 both flag this exact conflation as the thing to avoid: only **720+ of the ~1,100 works** are the SFMOMA-loaned subset; the case file lists "the 720-on-loan vs ~1,100-total reconciliation" as an open gap, not a settled fact to publish over.
**Fix:** before this post is scheduled, either state the loan figure as 720+ works, or drop the "more than a thousand" total from the loan sentence.

### 4. NEW — All five drafted LinkedIn posts end on a stated-meaning "moral" line, the exact pattern the file's own governing voice rules forbid.
`marketing/linkedin-posts.md` line 6 says voice is governed by [[voice]] and [[ai-tells]], "specifically the Substack Notes register." That register's own rule: *"End on a concrete fact or image, never a manufactured conclusion... If a closing line explains what the story means, cut it and let the last fact land."* [[ai-tells]] names the same pattern directly: *"The ending that repeats the post."* Every one of the five drafted posts closes this way instead of on a fact:
- Post 1: "What a collection becomes after its collector stops building it is the part I pay attention to."
- Post 2: "The direction the money takes is the thing worth watching."
- Post 3: "The clearest reading of a corporate collection is often a reading of the company behind it."
- Post 4: "A private collection becomes a public institution the moment someone decides its next owner should be everyone. Trumbull made that decision for himself, in advance, and built the room to enforce it."
- Post 5: "Ownership is one question. Who will look after the work for the next century is a different one, and the Fishers answered the second."

This is a 5-for-5 pattern, not an isolated slip, and it is exactly the "no stating beliefs directly, let the scene carry them" rule in [[voice]].
**Fix:** cut the closing interpretive sentence from each post; end on the last concrete fact instead (post 5, for instance, reads cleanly ending at "...shortly before Doris Fisher died at 94").

### 5. Primary-verification backlog grew from 60 (2026-08-29 baseline) to 73 items over the last three research runs, faster than the case count grew (113 → 116).
Every addition is individually justified with a real, located EIN, and structural gaps (aggregator-only financials, foreign-jurisdiction disclosure gaps, gifts absorbed into a larger institution's undisaggregated finances) continue to be correctly excluded from the numbered list rather than inflating it — the same discipline noted as good practice last audit. No action needed yet, but flagging because this is the first run-window where the backlog grew faster than the dataset; worth a narrowing-focused run if the trend continues.

---

## MINOR

### 6. CARRIED — the `origin` frontmatter field is still split across multiple values with no definition in `case-template.md`.
Current usage: `private-individual` (25) · `private` (14) · `corporate` (12) · `artist` (3, still not documented).
**Fix:** pick one value for the private side, normalize, and document all values including `artist` in `case-template.md`.

### 7. CARRIED — corporate-continuity vocabulary still fragmented.
`bank-of-america-collection.md`, `credit-suisse-ubs-collection.md`, `deutsche-bank-collection.md`, `jpmorgan-chase-collection.md`, and `ubs-art-collection.md` use `parent-entity-continuity`; `enron-art-collection.md` and `lehman-brothers-collection.md` use `parent-entity-survival` for the same underlying concept.
**Fix:** adopt one term; add it as an authorized value in `case-template.md`.

### 8. No settled decision found still marked open.
Checked all files in `company/decisions/`. The board-membership decision (2026-08-14) is itself resolved ("a qualified YES, to the right board only"); its outcome line is honestly marked `_open_` because the specific board search is genuinely still in progress, not because a decision is unrecorded. No structural issue.

---

## Resolved since the 2026-08-29 audit (confirmed this run, no longer flagged)
- **Live public-facing em dashes** (5 consecutive prior audits, 25 instances across 24 files): fixed. A fresh grep of every `public_*` frontmatter field across all of `cases/*.md` found zero em dashes.
- **Manuscript FY2018/FY2023 IRS Art Advisory Panel mix-up** (3 consecutive prior audits): fixed. `marketing/what-becomes-of-great-art-collections.md:358` now states the verified FY2023 figures (195 items / 37 cases / $795,527,954 / 47% adjusted / –$16,946,454), matching claims-register C31.
- **Table 1 mis-citation**: fixed. The two "(..., Table 1)" tags citing figures Table 1 doesn't contain are gone.
- **`case-template.md` export-gate self-contradiction + undefined `Spot-verified`**: fixed. `Spot-verified` is now defined at line 9; line 50 now matches line 34's export-gate statement instead of contradicting it.

---

**Counts:** 2 critical (1 new, 1 carried an 8th audit) / 3 should-fix (2 new, 1 confirm-only) / 3 minor (all carried, unchanged) — against 4 items resolved since the last audit.
