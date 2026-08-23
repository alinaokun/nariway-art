---
type: case
sample: report
title: Onera Foundation
pathway: found-house-museum
status: coded
priority: low
founder_status: living
geography: New Canaan, CT, USA
outcome: emerging
verification: provisional
public_page_eligible: true
public_verified: true
public_depth: record
public_status_text: "Opened its public exhibition venue in New Canaan in October 2025."
public_name: Onera Foundation
public_founder: David B. Peterson
public_location: New Canaan, Connecticut
public_founded: 2018
public_structure: Architectural-preservation foundation with a public exhibition venue
public_access: Open to the public (Tuesday–Saturday)
public_focus: Historic American architecture and its intersection with art
public_pathway_timeline: 2018|build-institution|found-foundation|Onera Foundation established; acquires the 1836 Maxwell Perkins House ;; 2025|build-institution|found-house-museum|Opens the restored house as a public exhibition venue
public_origin: David B. Peterson founded the Onera Foundation in 2018 to advance the preservation of historic American architecture. It restored the landmarked 1836 Maxwell Perkins House in New Canaan and opened it to the public as an exhibition venue in October 2025.
public_sources: onerafoundation.org; The Art Newspaper; The Architect's Newspaper
hero_image_status: no_usable_image
living_collector: true
last_reviewed: 2026-08
---

# Onera Foundation

One-line: David B. Peterson's Onera Foundation (founded 2018) is an architectural-preservation advocacy nonprofit, not a traditional art-collection museum; it acquired the landmarked 1836 Maxwell Perkins House in New Canaan, CT in 2018 and in October 2025 opened it as a public gallery for architecture-and-art exhibitions, alongside funding the Onera Prize at Columbia — with essentially no public financials.

**Why in the sample:** an **edge case** that stresses the taxonomy — the "collection" is a historic building plus rotating loan exhibitions rather than an owned art collection, and it is a founder-sole preservation foundation. It marks the boundary between an art institution and an advocacy platform, and it is the note where almost every quantitative field is legitimately `unknown`.

## Coded header

**Identity.** `case_id`: onera · `collection_name`: Onera Foundation (Maxwell Perkins House venue) · `founder_name`: David B. Peterson · `geography`: New Canaan, CT, USA · `verification_status`: **Provisional**

**Controlled-vocabulary fields:**
- `pathway`: **found-house-museum** (opened a public exhibition venue in an adapted historic residence) · `secondary_pathways`: [found-foundation] (primary identity is an advocacy/grantmaking foundation; the Onera Prize predates the venue) · `pathway_is_branched`: **yes** [source: https://www.theartnewspaper.com/2025/10/01/new-onera-foundation-venue-in-connecticut | secondary]
- `founder_status_at_transition`: **living** · `founder_still_living_now`: **living** · `survived_founder`: **not-yet-testable** (founder living; venue opened 2025)
- `outcome_category`: **emerging** (public venue opened Oct 2025) · `durability_signal`: **indeterminate** [source: https://www.theartnewspaper.com/2025/10/01/new-onera-foundation-venue-in-connecticut | secondary]
- `governance_control_at_founding`: **founder-sole** (David B. Peterson, founder and president; Laurence Lafforgue appointed executive director) [source: https://www.onerafoundation.org/about | secondary]
- `building_type`: **adapted-residence** (landmarked 1836 Greek Revival Maxwell Perkins House, 63 Park Street) [source: https://www.archpaper.com/2025/10/onera-foundation-architectural-preservation-new-canaan-connecticut/ | secondary]
- `collection_coherence`: **tight-single-thesis** (historic American architecture / preservation) · `coherence_drifted`: **no** — **caveat**: the field fits awkwardly; Onera presents invited-artist and architecture exhibitions rather than displaying an owned art collection [source: https://www.theartnewspaper.com/2025/10/01/new-onera-foundation-venue-in-connecticut | secondary]
- `decision_owner`: **collector-alone** (David B. Peterson) [source: https://www.onerafoundation.org/about | secondary]
- `primary_friction`: **none-documented**
- `constraints_documented`: **open** (founder living; institution one year old; no governing instrument documented)

**Quantitative fields** (USD):
- `collecting_start_year`: **n/a** (not a conventional collecting story; foundation founded 2018) [source: https://www.archpaper.com/2025/10/onera-foundation-architectural-preservation-new-canaan-connecticut/ | secondary]
- `transition_year` / `legal_recognition_year` (foundation founded): **2018** [source: https://www.archpaper.com/2025/10/onera-foundation-architectural-preservation-new-canaan-connecticut/ | secondary] — exact IRS ruling year **unknown** (see below)
- `institution_open_year` (public venue): **2025** (opened 1 Oct 2025) [source: https://www.theartnewspaper.com/2025/10/01/new-onera-foundation-venue-in-connecticut | primary]
- `building_acquired_year`: **2018** (Maxwell Perkins House) [source: https://www.theartnewspaper.com/2025/10/01/new-onera-foundation-venue-in-connecticut | secondary]
- `collection_size_at_founding` / `collection_size_current`: **n/a** (no owned art collection; venue shows loans/commissions; the "asset" is the historic building + garden) [source: https://www.onerafoundation.org/about | secondary]
- `founding_endowment_usd`: **unknown** — resolve via IRS filings / CT or NY charity registration
- `net_assets_latest`: **unknown** — **not located on ProPublica Nonprofit Explorer** under "Onera Foundation" (likely files Form 990-N e-postcard, or is registered under a different legal name); resolve via IRS Tax Exempt Organization Search (TEOS) for EIN, then 990/990-N, plus CT Attorney General charity registration [source: https://projects.propublica.org/nonprofits/api/v2/search.json?q=Onera | unknown]
- `total_expenses_latest`: **unknown** (same resolving source)
- `total_revenue_latest`: **unknown**
- `true_endowment_usd`: **unknown**
- `endowment_to_opex_ratio` / `net_assets_to_opex_ratio`: **not computable** (no financials located)
- `earned_revenue_latest`: **unknown**
- `annual_attendance`: **unknown** (venue <1 year old)
- `fte_headcount`: **unknown** (founder-president + one executive director named; count unverified) [source: https://www.onerafoundation.org/about | inferred]
- Real-asset fact (not a coded metric): owns the 1836 Maxwell Perkins House and grounds, incl. a modernist garden by Richard Bergmann documented in the Smithsonian's Archives of American Gardens; acquisition price **unknown** [source: https://www.onerafoundation.org/about | secondary]

## Narrative

The Onera Foundation, founded in 2018 by David B. Peterson — a Columbia-trained historic-preservation specialist and author — is fundamentally an advocacy and education nonprofit devoted to preserving historic American architecture, not an art-collection institution [source: https://www.archpaper.com/2025/10/onera-foundation-architectural-preservation-new-canaan-connecticut/ | secondary]. For years its main visible output was the Onera Prize, funding research at Columbia's Graduate School of Architecture, Planning and Preservation [source: https://www.theartnewspaper.com/2025/10/01/new-onera-foundation-venue-in-connecticut | secondary]. In 2018 the foundation acquired the landmarked 1836 Greek Revival Maxwell Perkins House at 63 Park Street in New Canaan — once home to the legendary Scribner's editor — and, after restoration, opened it to the public as an exhibition venue on 1 October 2025 [source: https://www.theartnewspaper.com/2025/10/01/new-onera-foundation-venue-in-connecticut | primary]. The venue presents architecture-and-art exhibitions and public programs rather than a permanent collection of owned artworks, which makes it a hybrid: the "collection" is effectively the building and its documented modernist garden [source: https://www.onerafoundation.org/about | secondary]. Governance is founder-sole — Peterson is founder and president, with Laurence Lafforgue recently named executive director [source: https://www.onerafoundation.org/about | secondary]. The foundation's financials are essentially opaque: no filing surfaces on ProPublica's Nonprofit Explorer under its name, suggesting it either files a Form 990-N e-postcard (below the full-disclosure threshold) or is registered under a different legal name [source: https://projects.propublica.org/nonprofits/api/v2/search.json?q=Onera | unknown]. As a result nearly every quantitative field here is a genuine `unknown` with a named resolving source, and the case is coded `emerging` with an `indeterminate` durability signal. It is included precisely as a taxonomy stress-test: a founder-sole preservation platform that adopted a house-museum form one year ago.

## Primary sources to obtain
- IRS Tax Exempt Organization Search (TEOS) — confirm EIN, 501(c)(3) status, ruling year, and filing type (990 vs 990-N)
- The Form 990 (or 990-N) itself, once the EIN is known — revenue, expenses, net assets, officer compensation
- Connecticut Attorney General / Dept. of Consumer Protection charity registration — financials and governance
- New Canaan land records — the 2018 Maxwell Perkins House acquisition price and any preservation easement
- Onera Foundation governing documents / bylaws — board composition, succession, mission scope (advocacy vs museum)

## Gaps / contradictions
- **No public financials located** — the single biggest gap; the org does not surface on ProPublica, so revenue, expenses, net assets, endowment and staffing are all `unknown` pending an EIN lookup.
- **Taxonomy fit is contested** — is this an art institution at all, or a preservation-advocacy foundation with a house venue? Coded `found-house-museum` primary + `found-foundation` secondary, but reasonable coders could invert those.
- **"Collection" fields are n/a, not unknown** — there is no owned art collection; do not let the venue be charted as if it holds a collection of a given size/value.
- **IRS ruling year unverified** — "founded 2018" is press-sourced; the legal recognition year needs TEOS confirmation.
- **Building acquisition price unknown** — the house is the principal asset; its cost/current value is unrecorded here.
