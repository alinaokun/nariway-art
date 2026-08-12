---
type: case
sample: report
title: Carl & Marilynn Thoma Art Foundation
pathway: long-term-loan
status: coded
priority: medium
founder_status: living
geography: Chicago, IL / Santa Fe, NM, USA
outcome: thriving
verification: spot-verified
---

# Carl & Marilynn Thoma Art Foundation — collection built to lend

*Coded to [[case-template]]. Report-grade, sourced. A living-founder foundation whose thesis is circulation: a large museum-loan program plus two small viewing spaces, rather than a founder museum. Gap-honest: an entity-name ambiguity around the 990-PF net-assets figure is flagged below and left `unknown` pending resolution.*

## Coded header
- `pathway`: **long-term-loan** (museum-loan program is the dominant public-access mechanism) · `secondary_pathways`: [**found-foundation**; two exhibition spaces — Art House, Santa Fe; Orange Door, Chicago] · `pathway_is_branched`: **yes**
- `founder_status_at_transition`: **living** (Foundation formed 2014; Carl & Marilynn Thoma living) [source: https://en.wikipedia.org/wiki/Carl_%26_Marilynn_Thoma_Art_Foundation; confidence: secondary] · `founder_still_living_now`: **living** (both, as of 2026) [confidence: inferred — no death recorded]
- `survived_founder`: **not-yet-testable** (both founders living)
- `outcome_category`: **thriving** (active loan program + two public-facing spaces) · `durability_signal`: **moderate** (durability untested against succession)
- `governance_control_at_founding`: **founder-sole / family-controlled** (private foundation of Carl & Marilynn Thoma) [source: https://projects.propublica.org/nonprofits/organizations/465446388; confidence: primary]
- `building_type`: **adapted-other** (Art House on Canyon Road, Santa Fe; Orange Door warehouse, Chicago, by appointment) · `collection_coherence`: **broad-survey** (four distinct areas) [source: https://thomafoundation.org/about/who-we-are/; confidence: secondary] · `coherence_drifted`: n/a (multi-thesis by design)
- `decision_owner`: **collector-alone** (Carl & Marilynn Thoma) · `primary_friction`: **none-documented** · `constraints_documented`: **partial**

**Key terms (loan model + collection), sourced:**
- **Collection size:** "over 1500 works," collecting begun **1975** [source: https://en.wikipedia.org/wiki/Carl_%26_Marilynn_Thoma_Art_Foundation; confidence: secondary]; Foundation also states a "1,700+ work collection" [source: https://thomafoundation.org/about/who-we-are/; confidence: secondary] — figures differ by vintage; range ~1,500–1,700, coded `unknown` for a single point value
- **Collection areas:** Art of the Spanish Americas (Spanish Colonial); Digital & Media/Electronic Art; Japanese Bamboo; Post-war Painting & Sculpture (color field / hard-edge abstraction) [source: https://thomafoundation.org/about/who-we-are/; confidence: secondary]
- **Museum Loan Program:** "loaned over 1,400 artworks from its collection to more than 250 exhibitions worldwide" [source: https://thomafoundation.org/about/what-we-do/; confidence: secondary — Foundation self-published; corroborate against loan schedule]
- **Two exhibition spaces:** Art House (Santa Fe) and Orange Door (Chicago), opened 2014 [source: https://en.wikipedia.org/wiki/Carl_%26_Marilynn_Thoma_Art_Foundation; confidence: secondary]

**Quantitative fields (990-PF, FY2024, EIN 46-5446388 — "Carl and Marilynn Thoma Art Foundation," Santa Fe NM):**
- `net_assets_latest`: **$1,213,338,107** (FMV of assets, end of year) [source: https://projects.propublica.org/nonprofits/organizations/465446388; confidence: primary — but see entity-ambiguity gap below; coded **unknown** for the report until the filer identity is confirmed]
- `total_expenses_latest`: **$48,370,008** [source: same; confidence: primary]
- `total_revenue_latest`: **$151,403,860** [source: same; confidence: primary]
- `net_assets_to_opex_ratio`: **≈25x [UPPER BOUND]** (net assets embed the collection's carried value; not a spendable endowment — [[claims-register]] C4) · `true_endowment_usd`: **unknown** · `endowment_to_opex_ratio`: **not computable**
- `institution_open_year`: 2014 · `collecting_start_year`: 1975 [secondary] · `fte_headcount`: **unknown**
- Historical anchor: Wikipedia cites asset value **US$79M (2015)**; the ~$1.2B FY2024 figure implies large subsequent funding by Carl Thoma (private-equity founder) — flagged for verification [source: https://en.wikipedia.org/wiki/Carl_%26_Marilynn_Thoma_Art_Foundation; confidence: secondary]

## Narrative
Carl and Marilynn Thoma began collecting in 1975 and in 2014 formed the Carl & Marilynn Thoma Art Foundation to steward and circulate the collection rather than concentrate it in a founder museum. The collection spans four deliberately distinct areas — Art of the Spanish Americas, Digital and Electronic Art, Japanese Bamboo, and post-war color-field and hard-edge painting and sculpture — variously reported at "over 1500 works" and "1,700+." Public access runs primarily through a Museum Loan Program that the Foundation says has "loaned over 1,400 artworks... to more than 250 exhibitions worldwide," supplemented by two small viewing spaces opened in 2014: Art House on Canyon Road in Santa Fe and the Orange Door warehouse in Chicago (by appointment). The Foundation is notably a leader in collecting and lending digital/media art, a category most museums under-hold. On the 990-PF (EIN 46-5446388) the Santa Fe art foundation reports very large net assets, but the figure sits above a $79M 2015 asset value cited by Wikipedia and near a same-sized general Thoma grantmaking entity, so the number is held as `unknown` for the report until the filer identity and the collection's carrying basis are confirmed. Both founders are living, so durability past succession is not yet testable; the coded outcome reflects present activity, not proven permanence.

## Primary sources to obtain
The Foundation's 990-PF full filing (EIN 46-5446388) to confirm it is the collection-holding art foundation and to read the collection's carried value; disambiguation from the separate "Carl & Marilynn Thoma Foundation" (Chicago, EIN 36-3486549); a dated, itemized loan tally behind the "1,400 works / 250 exhibitions" claim; the governing instrument and any succession/keep-together provisions; a reconciled single collection-size figure (1,500 vs 1,700+).

## Gaps / contradictions
- **Entity ambiguity:** at least two Thoma vehicles exist — "Carl and Marilynn Thoma Art Foundation" (Santa Fe, EIN 46-5446388) and "Carl & Marilynn Thoma Foundation" (Chicago, EIN 36-3486549). The $1.2B net-assets figure is attributed here to 46-5446388 but must be confirmed as the collection holder; coded `unknown` for the report pending that check.
- **Asset-value jump:** $79M (2015, Wikipedia) → ~$1.2B (FY2024, ProPublica) is large; requires verification that both refer to the same entity and reflect real funding rather than collection revaluation.
- Collection size reported inconsistently (1,500 vs 1,700+) — `unknown` single value.
- Loan-program figures are Foundation-self-published (secondary); corroborate against museum-side loan credits.
