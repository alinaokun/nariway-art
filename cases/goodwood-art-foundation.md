---
type: case
sample: report
title: Goodwood Art Foundation
pathway: found-foundation
status: coded
priority: medium
founder_status: living
geography: Goodwood Estate, West Sussex, England, UK
outcome: emerging
verification: spot-verified
decision_owner: collector-alone
interview_status: not-contacted
hypotheses: [H4, H5, H6]
origin: private
public_page_eligible: true
public_verified: true
public_depth: expanded
public_status_text: "Opened May 2025 on the Goodwood Estate; a new non-collecting contemporary-art foundation, separate from the family's centuries-old private collection."
public_name: Goodwood Art Foundation
public_founder: Charles Gordon-Lennox, 11th Duke of Richmond
public_location: Goodwood Estate, near Chichester, West Sussex, England
public_founded: 2025
public_structure: UK non-profit foundation (charitable status unconfirmed)
public_access: Open to the public, seasonal/ticketed on the estate
public_size: 70-acre woodland site; no permanent collection (commissioned/rotating exhibitions)
public_focus: Contemporary art, environment, and education
public_movements: Contemporary sculpture and site-specific installation
public_period: 2025–present
public_media: sculpture; site-specific installation; land art
public_selected_artists: Rachel Whiteread
public_pathway_timeline: 2025|build-institution|found-foundation|Goodwood Art Foundation opens on 70 acres of the estate with an inaugural Rachel Whiteread exhibition
public_origin: The Dukes of Richmond have held a private Old Master collection (Canaletto, Reynolds, Romney, Stubbs, Van Dyck) at Goodwood for over 300 years. In 2025 the 11th Duke launched a separate, new non-profit foundation on the estate's woodland, not a display of the family's own historic holdings, but a public contemporary-art and education venue with no permanent collection of its own.
public_sources: The Art Newspaper; Sotheby's; Apollo Magazine; Historic Houses
hero_image_status: no_usable_image
living_collector: true
last_reviewed: 2026-08
---

# Goodwood Art Foundation

*Coded to [[case-template]]. WebFetch re-tested this run against a fresh domain (www.goodwood.com) and re-confirmed `EGRESS_BLOCKED` — the twenty-second consecutive confirmation, following the ProPublica re-test logged this run. All facts below are WebSearch-snippet synthesis of art-trade press (The Art Newspaper, Apollo Magazine, Sotheby's, Historic Houses), tagged `secondary`. Chosen from [[candidate-universe]] §"Signals cycle 1" specifically because it tests a structurally distinct shape this sample had not yet coded: a landed aristocratic estate spinning off a brand-new, NON-COLLECTING public foundation, while its centuries-old private family collection stays exactly where it always was — untouched, unpledged, and not the subject of the public venue at all.*

One-line: Charles Gordon-Lennox, 11th Duke of Richmond, opened the Goodwood Art Foundation in May 2025 on 70 acres of his family's 300-year-old West Sussex estate — a new contemporary-art and education charity built around rotating commissions (inaugural artist Rachel Whiteread) rather than around the family's own historic collection of Canaletto, Reynolds, Romney, Stubbs, and Van Dyck, which remains privately held and undisplayed at the venue.

## Why in the sample

Every other `found-foundation` case in this dataset (Chinati, Dia, Fondation Cartier, Fondazione Prada) puts the founder's *own collection* on public view. Goodwood inverts that: the family's inherited Old Master holdings stay private and off-site from the new foundation, while the public venue commissions and exhibits *other* artists' contemporary work with no permanent collection of its own — closer to a kunsthalle than a museum. This is a genuinely distinct sub-form: a landed estate using its land, name, and capital to found a public-facing institution that is deliberately NOT a vehicle for the family's own art. It also tests H6 (does founder resources/community fit predict form) from an angle the sample has not captured — multi-generational agricultural/sporting estate wealth (Goodwood is also home to horse racing and motorsport events) diversifying into contemporary-art philanthropy, rather than a single-collection or single-fortune founder.

## Coded header (dataset row)

`case_id`: (report) · `collection_name`: Goodwood Art Foundation · `founder_name`: Charles Gordon-Lennox, 11th Duke of Richmond · `geography`: Goodwood Estate, near Chichester, West Sussex, England, UK · `verification_status`: **Spot-verified** (founding, opening date, location, inaugural exhibition, and the three-pillar mission cross-verified across ≥4 independent trade-press sources; no primary charity-registration or financial document located)

- `pathway`: **found-foundation** (a new, dedicated non-profit entity, distinct from the family's private holdings) [confidence: secondary] · `secondary_pathways`: [retain-family] (the Dukes' own Old Master collection continues to be privately held at Goodwood, entirely separate from the new foundation) · `pathway_is_branched`: **yes**
- `founder_status_at_transition`: **living** · `founder_still_living_now`: **living** · `survived_founder`: **not-yet-testable** (opened 2025, founder living, no succession event to test)
- `outcome_category`: **emerging** (opened May 2025, little more than a year of operating history) · `durability_signal`: **indeterminate**
- `governance_control_at_founding`: **founder-sole** (no independent board membership located via search; described in every source as the Duke of Richmond's own initiative) [confidence: secondary — a formal board may exist and simply not surface in press coverage]
- `building_type`: **purpose-built** (new woodland pavilions/exhibition structures on previously undeveloped estate land; landscape design by Dan Pearson Studio) [source: Dan Pearson Studio; confidence: secondary]
- `collection_coherence`: **n/a** — the foundation holds no permanent collection; it commissions and hosts rotating exhibitions. This itself is a taxonomy-relevant fact: `collection_coherence` as currently defined assumes an object collection exists, which does not fit a pure kunsthalle model (flagged for [[case-template]] below).
- `decision_owner`: **collector-alone** (the Duke of Richmond, per every source; no advisor, curator, or family-office role credited as the initiating decision-maker)
- `primary_friction`: **none-documented**
- `constraints_documented`: **open** (living founder, no governing instrument located)

**Governance sub-fields:**
- `board_type`: **unknown** — no board roster located via search this run
- `succession_locked_before_founder_death`: **unknown**
- `founder_control_mechanism`: reported as the Duke of Richmond's personal initiative on his own family's land; the Goodwood Estate itself (racing, motorsport, farming, hospitality) remains a separate, much larger family commercial enterprise the Foundation sits alongside, not inside
- `donor_intent_instrument`: **unknown** — no founding charter, trust deed, or charity-registration filing located this run
- `endowment_governance`: **unknown** — no financial disclosure located; UK charitable status (and therefore any Charity Commission filing) is unconfirmed, not merely unpulled

**Quantitative fields:**
- `collecting_start_year`: **n/a** (no permanent collection is being built) · `transition_year`: **n/a** · `institution_open_year`: **2025** (opened May/June 2025 — sources give both months) [source: The Art Newspaper, 2025-06-04; Historic Houses; confidence: secondary] · `legal_recognition_year`: **unknown**
- `collection_size_at_founding` / `collection_size_current`: **n/a** (kunsthalle model, not a permanent-collection institution)
- `founding_endowment_usd` / `net_assets_latest` / `total_expenses_latest` / `net_assets_to_opex_ratio` / `true_endowment_usd`: **unknown** — UK charitable status unconfirmed this run; if registered, Charity Commission accounts would be the resolving source, not a US 990 (a jurisdiction this sample has not yet coded a UK-charity-regime case for)
- `earned_revenue_latest` / `annual_attendance` / `fte_headcount`: **unknown**
- Site size: **70 acres** of the wider Goodwood Estate [source: Historic Houses, Artlyst; confidence: secondary]

## Narrative (sourced)

Charles Gordon-Lennox, 11th Duke of Richmond, opened the Goodwood Art Foundation in May 2025 as a new non-profit contemporary-art and education venue on 70 acres of the Goodwood Estate in West Sussex — land his family has held and developed for more than 350 years into horse racing, motorsport, and organic farming enterprises, alongside a private art collection spanning Canaletto, Reynolds, Romney, Stubbs, and Van Dyck [source: The Art Newspaper, 2025-06-04; Sussex Express; confidence: secondary]. The Foundation is organized around three stated pillars — Art, Environment, and Education — and opened with a headline exhibition devoted to Rachel Whiteread, the first woman to win the Turner Prize, sited in a woodland setting landscaped by Dan Pearson Studio [source: Apollo Magazine; Dan Pearson Studio; confidence: secondary].

The structurally distinctive feature, for this dataset, is what the Foundation is *not*: it is not a display vehicle for the family's own three-centuries-deep Old Master holdings, which by every account found this run remain privately held at Goodwood House itself, off the new public site. Instead the Foundation operates on a rotating-commission, no-permanent-collection model — closer to a Kunsthalle (a German-tradition exhibition space with no standing collection) than to any other `found-foundation` case in this sample, all of which (Chinati, Dia, Fondation Cartier) center on a founder's or foundation's own permanent holdings. Whether this separation is deliberate estate-planning (keeping the historic collection's tax/inheritance treatment untouched by public charitable use) or simply reflects an initial curatorial choice is not established by any source found this run.

## Primary sources to obtain

1. UK Charity Commission register search for "Goodwood Art Foundation" — not attempted this run (WebFetch blocked); would resolve legal structure, trustee roster, and (once filed) annual accounts.
2. goodwoodartfoundation.org fetched directly, for the Foundation's own mission statement, governance page, and any stated funding commitment from the Goodwood Estate or the Richmond family.
3. Goodwood Estate's own consolidated accounts or press materials for any disclosed capital cost of the 70-acre site's development (woodland pavilions, Dan Pearson landscaping).
4. A primary interview or estate press release naming the Foundation's actual board members and director, none of whom were confirmed by name in this run's search results.

## Gaps / contradictions

- **Opening month contested**: sources give both "May 2025" (Sussex Express, direct quote context) and the Art Newspaper's own dateline of 2025-06-04 describing the opening as recent news — coded here as May/June 2025, not resolved to a single date.
- **Legal/charitable status unconfirmed** — every source describes the Foundation as "non-profit," but no UK Charity Commission registration number was located via search snippet this run; this is the sample's first UK-jurisdiction case where even the *existence* of a charitable registration, not just its filed accounts, is unverified.
- **Taxonomy-coverage note**: `collection_coherence` and the quantitative `collection_size_*` fields assume the coded institution holds a permanent object collection. A pure rotating-exhibition kunsthalle (no permanent collection, holding = 0 by design) is a case shape [[case-template]] does not yet have a clean field for — flagged in [[report-dataset]] patterns this run alongside the Klesch case's `retain-family + university-partnership` note, as a second instance this run of the schema meeting a genuinely new institutional form.
- **Founder's own collection deliberately out of scope of the coded institution** — unlike every other estate/family case in this sample, the Old Master holdings that would normally anchor the case are not part of what became public; only the new foundation is coded here.
