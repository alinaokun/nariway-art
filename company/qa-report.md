# QA Report — 2026-08-21

**Verdict:** Not clean, but narrow and stable. Both CRITICALs carry over unchanged for a **fifth consecutive audit** — the flagship report still draws the forbidden "risen since 2011" reading from C10 in one sentence, and the live Substack copy mirrored in `positioning.md` still breaks the staccato rule. Three new case files this run (Museum Berggruen, Inhotim, Anderson Collection Stanford) show clean, disciplined sourcing, including a correctly-applied binding-rule catch (Inhotim: founder's personal/corporate debt kept separate from the institution's own unknown financials). One prior should-fix (`marketing/linkedin.md`'s stale headline note) is now resolved.

---

## CRITICAL

1. **`marketing/what-becomes-of-great-art-collections.md` line 68 still asserts the forbidden C10 reading in prose — open for a fifth consecutive audit, text unchanged since first flagged.** Table 1 correctly caveats claim C10 ("~51% | ... up long-run from ~25% (2011), but down from 63% (2023)"), but the prose directly beneath it still reads: "The surrounding financial industry has noticed, which is why art services inside wealth management have roughly doubled since 2011." `research/claims-register.md` C10's own do-not-say line forbids exactly this: "wealth-manager art-service adoption has risen steadily since 2011 — the most recent two-year window (2023-2025) moved the other way." Standard violated: claims-register C10; `quality-assurance.md` item 2 (no drift between restatements of the same figure). **Fix:** rewrite the line-68 sentence to match the correctly-framed retreat language already used elsewhere in the same document (e.g., line 180): "...the surrounding financial industry has noticed, even as actual service delivery has recently pulled back."

2. **Live, published Substack copy mirrored in `company/positioning.md` still breaks `voice.md`'s staccato/fragment-stack rules — open for a fifth consecutive audit, text unchanged since first flagged.**
   - Substack About page (line 61): "Some collections stay in families for generations. Some become museums or foundations. Some are given or lent to existing institutions. Some travel. Some are divided or sold. Some disappear from public view." — six short parallel sentences, against "No staccato sequences. Never three or more short sentences in a row."
   - Substack Welcome page (line 91): "Does it stay in the family? Become a museum or foundation? Go to an existing institution? Travel? Get divided or sold?" — four subject-less fragments in a row.
   Both are explicitly marked in the file as mirrors of live, published pages. Standard violated: `voice.md` craft standards (called "mechanical and non-negotiable" in the same file) and `ai-tells.md` #2. **Fix:** vary sentence shape or collapse each list into fuller sentences, on the live Substack page and in `positioning.md` together, per the file's own mirror rule.

---

## SHOULD-FIX

3. **The Primary-verification backlog in `cases/report-dataset.md` keeps growing every run with no ceiling or resolution plan — open for a sixth consecutive audit.** Now 41 items (up from 38, 35, 27 across the last several runs), driven by WebFetch staying `EGRESS_BLOCKED` for 17 consecutive research runs — an independently reconfirmed, real tooling constraint (this audit's own WebFetch call to the Sid Richardson ProPublica filing also returned `EGRESS_BLOCKED`). No individual case overstates its confidence tier; every new figure is still tagged correctly. But `quality-assurance.md` item 1 asks this audit to watch that the backlog isn't growing unbounded, and by design it is, every run. **Fix:** as previously suggested, add a one-line definition of `Spot-verified` to `case-template.md` (still missing — the template lists it as an allowed `verification_status` value but never defines what distinguishes it from `Provisional`), and/or set an explicit pace at which future runs prioritize primary-source upgrades over new cases if WebFetch stays blocked past some threshold (e.g., 20 runs).

4. **`cases/mcnay.md` still isn't folded into `report-dataset.md`'s numbered master synthesis, while its narrative is cited as supporting evidence — open for an eighth consecutive audit.** `report-dataset.md` Pattern 1 still cites "McNay's self-perpetuating board" as a survivor supporting the report's central governance-survival claim, while `cases/mcnay.md` still carries `status: founder-review`, the only case with this status, and remains absent from the numbered case list. **Fix:** fold McNay into the numbered dataset once its research clears founder-review, or drop it from Pattern 1's supporting-example list until then.

5. **`cases/moma.md` still carries two values outside `case-template.md`'s controlled vocabulary — `collection_coherence: absorbed` and `decision_owner: collective-founders-trustees` — unresolved for a fifth consecutive audit.** Both describe a real pattern (MoMA's multi-founder, absorbed-collection structure) the vocabulary has no slot for; a schema gap, not a coding error. **Fix:** amend `case-template.md` to add these values, or remap to the nearest existing value with a flagged caveat.

---

## MINOR

6. **`marketing/website.md` line 16 carries a standing, undated "reconciliation to do later" note** stating the live site's hero/section copy "differs from the canonical public copy in [[positioning]]," with no specific divergent line named and no target date, deferred as "not now" / "when convenient." `positioning.md`'s own mirror of the live site (captured the same day, 2026-08-19) appears to match what `website.md` describes (hero, homepage intro, $992B framing, Conversations, About). Since no concrete drifted line could be located this run, this stays minor rather than escalating to a single-source-of-truth violation, but an open-ended "will diverge, fix later" note on the file that's supposed to be the single source of truth for public copy is worth closing out or making concrete. **Fix:** either name the specific line(s) that actually differ, or remove the note if the two are in fact in sync.

7. **`marketing/website.md`'s "finalized copy" blocks still have em dashes, unresolved for an eighth consecutive audit.** Consistent with prior audits, likely a false positive (label-separator usage, not mid-sentence prose); noted without escalating, pending Alina's call on scope.

---

## Resolved since the last audit

- **`marketing/linkedin.md`'s stale headline note (prior should-fix #3) is fixed.** The "Current state" section no longer restates a copy of the headline; it now correctly points to `positioning.md` as the sole source, with no drifted text left behind.
- **Three new case files this run** (`museum-berggruen.md`, `inhotim.md`, `anderson-collection-stanford.md`) show no sourcing violations: every quantitative field is explicit `unknown` with a stated structural reason, no net-assets-to-opex ratio appears unlabeled, and Inhotim's file explicitly and correctly separates the founder's personal/corporate debt figures from the institution's own (unknown) financials per the case-template's binding rule.
- **No new claims-register drift found** elsewhere spot-checked this run (C1/$992B consistent across `positioning.md`, `website.md`, and the manuscript; the manuscript's "Outlook" predictions are correctly labeled candidate/unscored, not settled findings; all case-frontmatter controlled-vocabulary fields — `pathway`, `outcome`, `verification`, `founder_status` — checked in bulk across all ~68 case files and found within the allowed vocabulary, aside from the pre-existing `moma.md` exception in item 5).
- **`company/decisions/2026-08-14-board-membership.md`'s open status is legitimate**, not a stale marking — no board has yet been selected in `marketing/board-opportunities.md`.

---

**Counts:** 2 critical (both carried, 5th audit) / 3 should-fix (1 resolved, 2 carried) / 2 minor (1 new, 1 carried).
