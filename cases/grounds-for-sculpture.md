---
type: case
sample: report
title: Grounds For Sculpture
pathway: found-art-park
status: coded
priority: high
founder_status: living
geography: Hamilton, NJ
outcome: thriving
verification: spot-verified
decision_owner: collector-alone
interview_status: not-contacted
hypotheses: [H3, H4, H8]
public_page_eligible: true
public_verified: true
public_qa_verified: 2026-09-03
public_depth: expanded
public_status_text: "Open in Hamilton, New Jersey since 1992."
public_name: Grounds For Sculpture
public_founder: J. Seward Johnson
public_location: Hamilton, New Jersey
public_founded: 1992
public_structure: Independent nonprofit
public_access: Open to the public
public_size: 42 acres; 300+ outdoor sculptures
public_focus: Contemporary sculpture
public_period: 20th–21st century
public_media: sculpture
public_selected_artists: J. Seward Johnson; George Segal; Kiki Smith; Magdalena Abakanowicz; Beverly Pepper; Anthony Caro; Clement Meadmore; Boaz Vaadia
public_pathway_timeline: 1992|build-institution|found-art-park|Grounds For Sculpture opens on the former New Jersey State Fairgrounds ;; 2000|build-institution|found-foundation|Converted to an independent nonprofit with its own board, two decades before the founder's death ;; 2020|||J. Seward Johnson dies
public_origin: J. Seward Johnson, a Johnson & Johnson heir and figurative sculptor, opened Grounds For Sculpture on the former New Jersey State Fairgrounds in 1992 to make contemporary sculpture accessible to a general public. In 2000 he converted it into an independent nonprofit with its own board, twenty years before his death.
public_sources: groundsforsculpture.org; Wikipedia; VisitNJ
hero_image_status: no_usable_image
living_collector: false
last_reviewed: 2026-09
---

# Grounds For Sculpture

One-line: Johnson & Johnson heir and sculptor Seward Johnson built Grounds For Sculpture on the former New Jersey State Fairgrounds (opened 1992), spun it into an independent nonprofit in 2000, and it now shows 270+ contemporary sculptures on 42 landscaped acres — thriving six years past his 2020 death.

**Why in the sample:** an artist-founder with dynastic wealth who deliberately handed his park to an *independent board* while living — a governance choice most founder-parks avoid. Tests H8 (giving up founder control on purpose) and H4 (accessibility, not market value, as the stated thesis).

## Coded header (dataset row)

`case_id`: (report) · `collection_name`: Grounds For Sculpture · `founder_name`: J. Seward Johnson (John Seward Johnson II, 1930–2020) · `geography`: Hamilton, NJ, USA · `verification_status`: **Spot-verified**

- `pathway`: **found-art-park** · `secondary_pathways`: [found-foundation] · `pathway_is_branched`: no
- `founder_status_at_transition`: **living** (Johnson founded 1992 and stood up the independent nonprofit in 2000, all before his death) · `founder_still_living_now`: **deceased** (d. 10 Mar 2020) · `survived_founder`: **yes** (6 yrs and still operating in founded form; the independent board predated his death by 20 yrs) [secondary: [groundsforsculpture.org/about](https://www.groundsforsculpture.org/about/); [Wikipedia](https://en.wikipedia.org/wiki/Grounds_For_Sculpture)]
- `outcome_category`: **thriving** · `durability_signal`: **strong**
- `governance_control_at_founding`: **founder-sole** at 1992 origin, deliberately converted to **independent-board** in 2000 · `building_type`: **adapted-other** (former NJ State Fairgrounds; six indoor galleries) + landscape
- `collection_coherence`: **coherent-multi** (contemporary sculpture, heavy on Johnson's own figurative bronzes plus 700+ exhibited artists) · `coherence_drifted`: no
- `decision_owner`: **collector-alone** (Johnson conceived, funded and sited it) · `primary_friction`: **none-documented** (desk-level)
- `constraints_documented`: **partial** (the 2000 conversion to an independent public nonprofit is documented; founding gift instruments/endowment terms not pulled)

**Quantitative fields** — Form 990 via ProPublica (EIN **22-3694371**; 501(c)(3); IRS ruling **May 2000**). Landing: https://projects.propublica.org/nonprofits/organizations/223694371
- `institution_open_year`: **1992** (public opening) · `legal_recognition_year`: **2000** [primary, IRS ruling via ProPublica] — note the 8-yr gap between opening and independent-nonprofit status
- `net_assets_latest`: **$65,723,240** [primary, 990 FY2024 (Dec)] · `total_expenses_latest`: **$8,958,442** [primary, 990 FY2024] · `total_revenue_latest`: $11,772,078 [primary]; total assets $67,895,902
- `net_assets_to_opex_ratio`: **≈7.3x [UPPER BOUND]** (net assets include the 42-acre site, buildings and installed works; not a true endowment) · `true_endowment_usd`: **unknown** (990 Schedule D unpulled) · `endowment_to_opex_ratio`: **not computable yet**
- Prior years [primary, 990 JSON]: FY2023 net assets $58,714,069 / opex $9,023,015; FY2022 $54,850,580 / $9,308,429 (note: FY2022 revenue $27.2M included ~$22.7M in gifts/grants — a bequest/campaign spike, not operating income); FY2021 $39,741,904 / $7,265,186
- `collection_size`: **270–300+ outdoor sculptures**; **700+ artists** exhibited over time [secondary: [Wikipedia](https://en.wikipedia.org/wiki/Grounds_For_Sculpture) states "over 270"; [groundsforsculpture.org](https://www.groundsforsculpture.org/about/) states "over 300"] — reconcile against official checklist
- `acreage`: **42 acres** [secondary: [groundsforsculpture.org](https://www.groundsforsculpture.org/about/); [Wikipedia](https://en.wikipedia.org/wiki/Grounds_For_Sculpture)]
- `annual_attendance`: **unknown** (no authoritative figure verified) · `fte_headcount`: **unknown** (990 Part I line 5 unpulled) · `founding_endowment_usd`: **unknown**

## Narrative (sourced)

Seward Johnson — a Johnson & Johnson heir who became a prolific figurative sculptor — conceived a public sculpture park in 1984 and opened Grounds For Sculpture on the former New Jersey State Fairgrounds in Hamilton in 1992, an outgrowth of his adjacent Johnson Atelier casting operation [secondary: [groundsforsculpture.org/about](https://www.groundsforsculpture.org/about/)]. The stated thesis is accessibility rather than market value: making contemporary sculpture comfortable for a general public, which places it near the public-benefit end of H4 [secondary]. The governance move that distinguishes this case is deliberate: in July 2000 Johnson converted the park into an independent public nonprofit with its own board, ceding founder-sole control 20 years before his death — an H8 case of a founder giving up control on purpose while alive [primary, IRS ruling date; secondary, [Wikipedia](https://en.wikipedia.org/wiki/Grounds_For_Sculpture)]. Johnson died on 10 March 2020, and the institution has continued in substantially its founded form under that pre-existing board, a clean `survived_founder = yes` [secondary]. Financially it is healthy and growing: FY2024 net assets of $65.72M against $8.96M of expenses give a net-assets-to-opex cushion near 7.3x, with net assets having climbed from ~$39.7M in FY2021 partly on a large FY2022 gift/bequest spike (~$22.7M) [primary, [990 via ProPublica](https://projects.propublica.org/nonprofits/organizations/223694371)]. That 7.3x figure is an **upper bound** — it folds in the 42-acre site, six galleries and installed works, and the true endowment (Schedule D) has not been pulled.

## Primary sources to obtain

1. The 2000 conversion documents and any founding gift/endowment instrument from Johnson or The Sculpture Foundation → governance terms and whether display/deaccession constraints were imposed (H8).
2. Form 990 **Schedule D** (FY2024 PDF) → true endowment vs. the net-assets upper bound; and the FY2022 990 to confirm the ~$22.7M gift.
3. Official collection checklist → reconcile the 270 vs. 300+ sculpture count and current acreage.
4. The relationship map between GFS, the Johnson Atelier, and The Sculpture Foundation (which entity holds what) → decision-owner and asset control.
5. Authoritative annual attendance and FTE headcount (990 Part I line 5).

## Gaps / contradictions

- Sculpture count contested: **270+** (Wikipedia) vs **300+** (official site) — resolve to the checklist.
- The 8-year gap between the 1992 public opening and 2000 nonprofit ruling means pre-2000 governance/ownership (Johnson personally vs. an entity) is unverified.
- FY2022's $27.2M revenue is a one-time gift/bequest spike, not operating income — do not read it as recurring.
- True endowment vs. net assets unresolved; 7.3x is an upper bound.
- Attendance and FTE not verified; founding endowment amount unknown.
