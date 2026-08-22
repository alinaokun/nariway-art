---
type: case
sample: report
title: The Barnes Foundation
pathway: found-foundation
status: coded
priority: high
founder_status: deceased
geography: Merion / Philadelphia, PA
outcome: pivoted
verification: spot-verified
public_page_eligible: true
public_verified: true
public_depth: expanded
public_status_text: "Operating in Philadelphia since 2012; relocated from Merion by court order."
hero_image_status: no_usable_image
living_collector: false
last_reviewed: 2026-08
---
# The Barnes Foundation — the canonical donor-intent / cy pres relocation case

*Coded to [[case-template]]. Report-grade, sourced. The spine here is the **litigation and cy pres record**, not self-history; Barnes's own account and the film *The Art of the Steal* are color only. This is the reference case for what happens when a founder's deed-of-trust constraints collide with institutional viability.*

## Public profile
*(export layer, per [[case-template]]; figures verify-to-grade before live export)*
- **Public facts:** founded **1922** · Merion → Philadelphia, PA · educational foundation · open to the public · 4,000+ objects, 900+ paintings
- **Composition:** focus *Impressionist, Post-Impressionist, and early Modern painting, hung in fixed ensembles* · movements *Impressionism · Post-Impressionism · early Modernism* · period *late 19th–early 20th century* · media *painting* · selected_artists *Renoir (179) · Cézanne (69) · Matisse (59) · Picasso (46)* · recipients *(none)* — *Renoir/Cézanne counts confirmed against barnesfoundation.org, 2026-08 (corrected from 181 to the site's stated 179)*
- **Pathway timeline:** 1922 — *Build an institution* (`found-foundation`) — chartered as an educational foundation, Merion · 2012 — *Build an institution* (`found-standalone-museum`) — relocated to Philadelphia by court order under cy pres
- **Origin:** Albert C. Barnes assembled his collection in the early twentieth century, building deep holdings in Impressionist, Post-Impressionist, and early Modern painting. In 1922 he chartered the Barnes Foundation as an educational institution and installed the works in fixed ensembles of his own arrangement in a purpose-built gallery in Merion. His trust set strict terms after his death, restricting whether the works could be moved or loaned, how they were hung, and who could see them.

## Coded header
- `pathway`: **found-foundation** (chartered 1922 as an educational foundation, not a public museum) · `secondary_pathways`: [**found-standalone-museum** — de facto since the 2012 Parkway relocation] · `pathway_is_branched`: **yes**
- `founder_status_at_transition`: **living** (Albert C. Barnes chartered and endowed the Foundation Dec 4, 1922; the Merion gallery opened 1925 — all during his life) [secondary — barnesfoundation.org / Wikipedia] · `founder_still_living_now`: **deceased** (d. 1951-07-24, car accident near Phoenixville, PA) [secondary — Britannica; PA Center for the Book]
- `survived_founder`: **yes** — operated in substantially its founded Merion form for ~60 years after Barnes's death (1951→2012), through multiple trustee succession, before the cy pres relocation [secondary — Wikipedia timeline]
- `outcome_category`: **pivoted** — the institution thrives financially and by attendance today, but only after a court overrode the founding intent, converting a restricted-access educational foundation in Merion into a public museum on the Benjamin Franklin Parkway. Thriving-as-museum is *not* the same as surviving-as-founded. · `durability_signal`: **strong** (as currently operating) — but the durability came *through* breaking the deed, so the signal is about the institution, not the intent.
- `governance_control_at_founding`: **founder-sole** — Barnes controlled during life; his indenture then vested trustee-appointment power in **Lincoln University** (a historically Black university) after his death [secondary — PA Center for the Book; Wikipedia]
- `building_type`: **purpose-built** (both the Paul Cret Merion gallery, dedicated 1925, and the Tod Williams Billie Tsien Parkway building, opened 2012, were purpose-built) [primary — barnesfoundation.org]
- `collection_coherence`: **coherent-multi** — Impressionist/Post-Impressionist/early Modern paintings hung as fixed pedagogical "ensembles" alongside African sculpture, antiquities, and wrought-iron metalwork · `coherence_drifted`: **no** (the ensemble arrangement was replicated wall-for-wall in the new building)
- `decision_owner`: **foundation-executive** — the relocation was driven by the Foundation's trustees and major funders (Pew, Lenfest, Annenberg foundations), not the founder [secondary — Wikipedia; press]. *(Original 1922 founding decision owner: collector-alone.)*
- `primary_friction`: **funding-gap** — the cy pres petition rested on the argument that the Foundation was financially non-viable at Merion under the indenture's restrictions [secondary]. Also present: **legal-challenge** ("Friends of the Barnes" appeals 2004–2011) and **founder-control** (the indenture itself as the binding constraint).
- `constraints_documented`: **yes** — the **Indenture of Trust** is a documented, litigated instrument. Key deed-of-trust constraints:
  - *No move / no sale / no loan:* after Barnes's death "no picture belonging to the collection shall ever be loaned, sold or otherwise disposed of" except a picture in "actual decay" [primary — quoted in barnesfoundation.org press release on loan permission]
  - *Fixed salon-style hanging:* the wall ensembles frozen "in exactly the places they are" [secondary — Wikipedia]
  - *Limited public access:* admission originally limited to ~two days/week; an education institution, not a public museum; free access intended for "plain people... who make their livelihood by daily toil" [secondary/primary]
  - *No color reproductions, no touring* [secondary]
- **The cy pres move (what broke vs held):** BROKEN — the absolute no-move-from-Merion term (overridden by Montgomery County Orphans' Court, Judge Stanley R. Ott, Dec 2004); the 5-trustee board cap (expanded to 15, diluting Lincoln's control); restricted access; and later the no-loan term (Orphans' Court granted temporary-loan permission, 2023). PRESERVED (as a court condition) — the salon-style ensemble arrangement, reproduced in the 2012 building. [secondary — Wikipedia; primary — barnesfoundation.org loan release]

### Quantitative fields (each sourced; unknowns explicit)
- `legal_recognition_year`: **1922** (chartered by the Commonwealth of PA, Dec 4) [secondary — Wikipedia] · `institution_open_year (Merion)`: **1925** [primary — barnesfoundation.org] · `institution_open_year (Parkway)`: **2012** (opened May 18–19) [primary — barnesfoundation.org]
- `collection_size_current`: **4,000+ objects; 900+ paintings** [primary/secondary — barnesfoundation.org]. Named groups: **Renoir 179** (largest single group in the world; barnesfoundation.org states 179 as of 2026-08, corrected from a prior 181), **Cézanne 69** (largest single group), **Matisse 59**, **Picasso 46** [primary — barnesfoundation.org]
- `collection_value`: **unknown** — press cites ~$20–30B (often "$25B") but there is **no official appraisal**; do not code as fact [secondary/inferred — Center for Art Law]
- `net_assets_latest`: **$245,027,793** (FY ending June 2025) [primary — IRS Form 990, EIN 23-6000149, via ProPublica] · `total_expenses_latest`: **$30,073,540** (FY June 2025) [primary] · `net_assets_to_opex_ratio`: **~8.1x [UPPER BOUND]** (net assets include the buildings; true endowment is smaller and unpulled)
- `total_revenue_latest`: **$33,749,714** (FY June 2025) [primary — ProPublica]
- `founding_endowment_usd`: **unknown** — Barnes left an endowment under conservative investment restrictions later cited in the viability argument, but the dollar figure at his 1951 death is not in consulted sources [unknown — resolve via the Orphans' Court cy pres record / probate] 
- `true_endowment_usd`: **unknown** (990 Schedule D unpulled) · `endowment_to_opex_ratio`: **not computable yet**
- `annual_attendance`: **217,000 (2012); 305,000 (2013)** [secondary — Philadelphia Inquirer]; recent-year figure **unknown** (attendance is not an IRS field)
- `fte_headcount`: **unknown** (990 Part I line 5 unpulled)
- `founder wealth source`: Argyrol, a silver-protein antiseptic (A.C. Barnes Company), sold ~1929 before the crash [secondary — Britannica]

## Narrative
Dr. Albert C. Barnes made his fortune from the antiseptic Argyrol and, shaped by John Dewey's educational philosophy, assembled one of the world's great concentrations of Impressionist, Post-Impressionist, and early Modern painting — 181 Renoirs, 69 Cézannes, 59 Matisses — which he chartered in 1922 as an educational *foundation*, not a museum, and hung in fixed pedagogical ensembles in a purpose-built Merion gallery (Paul Cret, 1925). His Indenture of Trust locked the collection down: no work could ever be moved, sold, or loaned; the wall arrangements were frozen; public access was deliberately limited; and after his 1951 death, trustee-appointment power passed to Lincoln University. For decades the Foundation operated in exactly that founded form, but by the early 2000s its trustees argued it was financially non-viable in Merion under those restrictions, and petitioned the Montgomery County Orphans' Court to move the collection to Philadelphia. Judge Stanley Ott, applying cy pres, declined an immediate move in early 2004 but granted the relocation in December 2004, also approving expansion of the board from 5 to 15 trustees — diluting Lincoln's control. Appeals by "Friends of the Barnes" (including a 2011 bid citing the film *The Art of the Steal*) failed, and the new Tod Williams Billie Tsien building opened on the Benjamin Franklin Parkway in 2012, replicating Barnes's ensembles wall-for-wall as a court condition. The institution is now robust — FY2025 net assets of ~$245M against ~$30M expenses, with 200,000–300,000 annual visitors in its early Parkway years — but that durability was purchased by overriding nearly every access and location constraint the founder wrote, which is why this case is coded **pivoted**, not simply thriving. In 2023 the Orphans' Court went further, permitting temporary loans, another deviation from the deed. The Barnes is the canonical demonstration that a documented, aggressive donor-intent instrument is not self-enforcing: a court can rewrite it in the name of viability.

## Primary sources to obtain
- The **Indenture of Trust** (full text) and its amendments — for the exact, verbatim deed constraints (move/sale/loan, hanging, access) rather than press paraphrase.
- The **Montgomery County Orphans' Court opinions** *In re Barnes Foundation* (Ott, 2004 preliminary + December 2004 grant; 2011 denial of reopening; 2023 loan permission) — to upgrade the litigation record from secondary to primary and to resolve the Dec 13 vs Dec 15 2004 date discrepancy.
- The Barnes Foundation **Form 990 full filing PDF/XML** (EIN 23-6000149) — Schedule D for `true_endowment_usd`; Part I line 5 for FTE; Part VIII for earned-revenue detail.
- **Probate / trust records** for Barnes's 1951 estate → founding endowment dollar figure and its investment restrictions.
- Official **Board of Trustees roster** → current exact trustee count and Lincoln University's residual role.

## Gaps / contradictions
- **Collection valuation** ($20B / $25B / $30B) is press estimate only — no official appraisal; must not feed a coded field.
- **December 2004 ruling date** cited as Dec 13 vs Dec 15 across sources; the court opinion resolves it.
- **Founding endowment dollar figure** at Barnes's death: unknown from consulted sources.
- **Current trustee count** and **recent-year attendance**: unknown; resolving sources named above.
- **`net_assets_to_opex_ratio` (~8.1x) is an UPPER BOUND** per [[claims-register]] C4 — net assets include real property; true endowment (Schedule D) unpulled and smaller.
- Much of the governance/timeline detail rests on secondary sources (Wikipedia, press); the Orphans' Court docket is the primary record that would confirm it.
