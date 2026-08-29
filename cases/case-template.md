# Case Template — the report-grade standard

Every case study produces two things: a **coded header** (controlled-vocabulary and quantitative fields that aggregate into the [[flagship-report]]'s charts) and a **narrative packet** (the depth and founder-learning the [[case-study-protocol]] requires). The coded header is the dataset; the narrative is the reading. **Binding rule: the coded header is a compression of the narrative's verified content, never an upgrade of it.** No coded value may assert more confidence than its narrative source. A chart may be built only from cells tagged `primary` or `secondary`, and every chart caption must state how many cases were `unknown` for that field. This is the [[claims-register]] discipline generalized to all cases.

Born from the fresh-eyes review of [[mcnay-packet]] (2026-08). Controlled vocabularies below are the *allowed values*; a value outside a list is not permitted without amending this template, so the vocabulary stays stable across all ~80 rows.

## Coded header (the dataset row)

**Identity.** `case_id` · `collection_name` · `founder_name` · `geography_city/region/country` · `verification_status` [`Provisional` (WebSearch-snippet synthesis only) · `Spot-verified` (at least one figure independently corroborated across two sources, or a direct fetch of a secondary source) · `Primary-verified` (financials sourced to a directly-fetched primary document — a 990 Schedule D, deed, will, or founding instrument)].

**Controlled-vocabulary fields (these make the charts):**
- **`pathway`** (dominant disposition form): `retain-family` · `sell-auction` · `sell-private` · `donate-existing-museum-intact` · `donate-existing-museum-scattered` · `long-term-loan` · `found-standalone-museum` · `found-house-museum` · `found-foundation` · `found-art-park` · `university-partnership` · `traveling-program` · `intentional-dispersal` · `merger-into-institution` · `abandoned-plan` · `hybrid`. Plus `secondary_pathways` (array) and `pathway_is_branched` (bool), because dispositions are a portfolio, not one choice.
- **`founder_status_at_transition`**: `living` · `deceased` (exactly two values — the headline chart pivots on it).
- **`founder_still_living_now`**: `living` · `deceased` · `n/a`.
- **`survived_founder`**: `yes` · `no` · `not-yet-testable` · `unknown`. **The single most important field.** Rule: `yes` iff the institution kept operating in substantially its founded form for at least one director succession (or ~5 years) after the founder's death.
- **`outcome_category`** (mutually exclusive, each with a one-line decision rule): `thriving` · `stable` · `distressed` · `closed-dispersed` · `dissolved` · `merged` · `pivoted` · `founder-open` · `emerging`. (Replaces free-text adjectives like "thriving/durable".)
- **`durability_signal`** (ordinal that survives missing data): `strong` · `moderate` · `weak` · `failed` · `indeterminate`.
- **`governance_control_at_founding`**: `independent-board` · `family-controlled` · `mixed` · `founder-sole` · `parent-institution`.
- **`building_type`**: `purpose-built` · `adapted-residence` · `adapted-other` · `existing-institution` · `no-building`.
- **`collection_coherence`**: `tight-single-thesis` · `coherent-multi` · `broad-survey`, plus `coherence_drifted` (bool).
- **`decision_owner`** (H7A): `collector-alone` · `spouse` · `children` · `estate-attorney` · `art-advisor` · `museum-director` · `family-office` · `architect` · `philanthropic-advisor` · `foundation-executive` · `consultant` · `auction-house` · `no-identifiable-person`.
- **`primary_friction`** (single dominant, from protocol §K list): funding-gap · family-disagreement · museum-rejection · zoning · community-opposition · tax · governance-conflict · collection-incoherence · storage · conservation · staffing · founder-control · poor-attendance · succession-failure · advisor-fragmentation · construction-overrun · legal-challenge · gift-refused · none-documented.
- **`constraints_documented`**: `yes` · `no` · `partial` · `open` (living founder, genuinely undecided — distinct from `unknown`). Guards H8 against reading "no constraints found" as "founder imposed none" (absence of evidence is not evidence of absence).

**Quantitative fields** — each carries a companion `_source` and `_confidence` (`primary` · `secondary` · `inferred` · `unknown`): `collecting_start_year` · `transition_year` · `institution_open_year` · `legal_recognition_year` (primary) · `collection_size_at_founding` · `collection_size_current` · `founding_endowment_usd` (primary) · `net_assets_latest` (primary) · `total_expenses_latest` (primary) · `true_endowment_usd` (primary, 990 Sch. D) · `endowment_to_opex_ratio` (derived) · `net_assets_to_opex_ratio` (derived, label UPPER BOUND) · `earned_revenue_latest` · `annual_attendance` · `fte_headcount`.

**The durability metric, stated once.** Charts run on `endowment_to_opex_ratio` where the true endowment is known; fall back to `net_assets_to_opex_ratio` (flagged upper bound) where not; fall back to the ordinal `durability_signal` where neither. Never mix an upper-bound net-assets ratio and a true-endowment ratio in one series without labeling (claims-register C4, generalized).

## Public projection layer (the export schema — added 2026-08-22)
Distinct from the coded header above, which is the INTERNAL research schema. These fields are what the public site renders, projected by the export ([[collection-index-build-brief]] §9). **A blank/absent public field simply does not render; unknown is never filled with prose.** Internal fields (`outcome_category`, `durability_signal`, `verification`, `decision_owner`, `_confidence` tags, sourcing notes) are NEVER exported.

**Frontmatter flags (the export gate + render controls):**
- `public_page_eligible`: `true` / `false` — the curatorial/ethics gate (public-by-choice, documented, non-sensitive).
- `public_verified`: `true` / `false` — the ACCURACY gate. The public-facing claims (founder, dates, location, structure, composition/artists, pathway/status) are confirmed against the institution's own site or reputable sources. **The live export requires `public_page_eligible` AND `public_verified` — NOT the internal `verification` financial-depth tag.** The public page shows facts, not 990 financials, so public export depends on public-fact accuracy (confirmable via WebSearch, which is never egress-blocked), not on primary 990 pulls. A case can be `public_verified: true` while its internal `verification` is still `secondary`/`spot-verified`. `status: coded` alone is not enough. When a public fact can't be confirmed or sources conflict (e.g. a contested object count), soften or omit it rather than publish it — do not let one unconfirmable figure hold back an otherwise-verified page.
- `public_depth`: `record` (structured profile only) / `expanded` (profile + factual sections). Depth follows evidence, never a quota.
- `public_status_text`: a SHORT factual sentence, the public translation of the internal `outcome_category` (which never renders). e.g. `pivoted` → "Operating in Philadelphia since 2012."; `dissolved` → "Dissolved, 2014."
- `hero_image_status`: `cleared` / `open_access` / `permission_required` / `no_usable_image`. (Internal-only, never exported: `image_source`, `image_rights`, `image_credit`, `image_caption`, `image_verified_date`.)
- `living_collector`: `true` / `false` — gates sensitive handling; when true, artist/period fields are dated/softened and no post-founder outcome is predicted.
- `last_reviewed`: `YYYY-MM`.

**Structured public fields — ALL in FRONTMATTER (flat `key: value`, the machine contract the export reads; single source of truth; dependency-free, so no YAML library is needed).** Lists use `; ` as the delimiter; omit any field that is unknown (never a false-complete list). This is a STRICT format contract — keep it exact so the export parses reliably across ~100 agent-maintained files.
- Identity/profile: `public_name` · `public_founder` · `public_location` · `public_founded` (year) / `public_collecting_began` · `public_structure` · `public_access` · `public_size`
- Composition: `public_focus` · `public_movements` (`; `-list) · `public_period` · `public_media` (`; `-list) · `public_selected_artists` (`; `-list) · `public_recipients` (`; `-list; dispersal/gift cases)
- `public_pathway_timeline` (the multi-path model): events as `year|family|coded_pathway|event`, multiple events separated by ` ;; `. A case appears under every family its timeline touches.
- `public_origin`: one or two short, restrained, factual sentences (how it began → what it became → what the collector did); placeholder-grade until a publication writing pass.
- `public_sources`: `; `-list of short source labels.

**Why flat frontmatter (not a prose body block, not nested YAML):** the export must parse reliably across ~100 agent-maintained files. Flat `key: value` is the format an agent gets right every time and a parser reads without a YAML dependency. The richer factual prose SECTIONS (brief §4a: The place, After the founder, etc.) stay in the normal case body and are a LATER export iteration; v1 exports profile + composition + timeline + origin + status + image + sources.

*Populating these does not re-verify the coded header. The export gate is `public_page_eligible` AND `public_verified` (line 34 above) — NOT the internal `verification` financial-depth tag; a case can export while its internal `verification` is still `Provisional` or `Spot-verified`.*

## Gaps are a first-class value (not an exception)
- Every quantitative field has an explicit `unknown` state; a **blank is never allowed** (blanks hide gaps; `unknown` counts them). "Unknown is a finding."
- Contested fields store **both candidate values plus the resolving source needed**, and stay `unknown` until a primary source decides. So the report can say "N of ~80 cases have a verified founding endowment" — the gap becomes a statistic, which for a report on how collections fare is itself a differentiator.
- Systematically-unavailable fields, expected `unknown` for many cases: founding endowment $ (probate/trust docs), true endowment vs net assets (990 Sch. D for US 501(c)(3); easier for 990-PF; often unavailable intl/university), attendance (self-reported, treat secondary), founder constraints (locked in unread instruments).

## Narrative sections (kept, disciplined)
Close to the protocol's A–L: 1) Pathway spine (with branch-check) · 2) The collector (intent quote's provenance rated) · 3) The collection (coherence + cultural-opportunity, scored separately from viability) · 4) The transition (trigger, alternatives, why this form) · 5) Institutional design · 6) Money (always the net-assets-vs-endowment caveat + upper-bound label) · 7) Governance, succession & founder constraints (H8; what the founder gave up) · 8) Outcome & durability (behind the coded values) · 9) Advisors & network map · 10) Friction (leads, not conclusions) · 11) Decision owner & coordinator (H7A) · 12) Evidence & confidence (primaries to obtain, gaps-and-contradictions list).

## Charts this enables
- **Survive-the-founder:** among `founder_status_at_transition = deceased` AND `pathway ∈ found-*`, share with `survived_founder = yes`.
- **Outcomes by pathway** · **Durability by governance** (independent-board vs family) · **Distinctiveness vs value** (durability by coherence, H4) · **Who owns the decision** (decision_owner distribution, H7A) · **Data-availability** (count of `unknown` per field — honesty as a differentiator).

---

## Worked example — McNay coded header (from the packet's verified content)
`case_id`: 1 · `collection_name`: McNay Art Museum · `founder_name`: Marion Koogler McNay · `geography`: San Antonio, TX, USA · `verification_status`: **Provisional**
- `pathway`: **found-house-museum** · `secondary_pathways`: [] · `pathway_is_branched`: no
- `founder_status_at_transition`: **deceased** · `founder_still_living_now`: deceased · `survived_founder`: **yes** (75 yrs, one full board handoff)
- `outcome_category`: **thriving** · `durability_signal`: **strong**
- `governance_control_at_founding`: **independent-board** (self-perpetuating; no family/municipal appointment)
- `building_type`: **adapted-residence** · `collection_coherence`: **coherent-multi** · `coherence_drifted`: yes
- `decision_owner`: **collector-alone** (pre-mortem, via will) · `primary_friction`: **none-documented** (house conversion kept in narrative; no verified cost overrun)
- `constraints_documented`: **no** (the will is unread — excludes McNay from the H8 constraint chart; not "imposed none")
- `net_assets_latest`: $100,080,025 [primary, 990 FY2025] · `total_expenses_latest`: $10,805,899 [primary] · `net_assets_to_opex_ratio`: **9.3x [UPPER BOUND]** · `true_endowment_usd`: **unknown** (Sch. D unpulled) · `endowment_to_opex_ratio`: **not computable yet**
- `collection_size_at_founding`: **unknown** (contested 200 vs 700) · `collection_size_current`: ~20,000–22,000 [secondary] · `annual_attendance`: **unknown** (contested 100k vs 200k) · `fte_headcount`: **unknown** (990 Part I line 5 unpulled) · `institution_open_year`: 1954 · `legal_recognition_year`: 1951 [IRS]

### McNay fix-list to reach report grade
**Mechanical (no interview needed):** pull 990 Schedule D → `true_endowment_usd` + real ratio; pull FTE (990 Part I line 5); resolve the FY2011 $3.2M revenue anomaly; get a 2nd source for the 2022 Sarah Fox controversy before coding any distress; test the "first modern-art museum in Texas" superlative vs CAMH 1948 / Dallas / Fort Worth; confirm live admission price.
**Archive/interview (blocking for a *published* row):** obtain the will + Bexar County probate file (1950) → founding endowment, deaccession/keep-together/display constraints (H8), whether contested; resolve collection-size (200 vs 700) from the estate inventory; resolve attendance from an authoritative figure; settle minor contested facts (death date, house completion year).
**Framing (prose must not outrun research):** stop letting "two-thirds of her wealth," "largest single gift in the city's history," "~75% of the house altered," "six feet of earth excavated" read as established figures — keep them as tagged reported color, none feeding a coded field; treat the Leeper "severe standards of quality" line as secondary interpretation, like the uncited Wikipedia quote.
