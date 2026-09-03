---
type: case
sample: report
title: Canyon
origin: private-individual
pathway: found-standalone-museum
status: coded
priority: medium
founder_status: living
geography: New York, NY
outcome: emerging
verification: secondary
public_page_eligible: true
public_verified: true
public_qa_verified: 2026-09-03
public_depth: record
public_status_text: "Under construction; opening on New York's Lower East Side, 2027."
public_name: Canyon
public_founder: Robert Rosenkranz
public_location: New York, NY
public_founded: 2027
public_structure: Purpose-built standalone venue (legal structure not yet publicly documented)
public_access: Opening to the public, 2027
public_size: 40,000 sq ft
public_focus: Durational art, video, sound, and performance
public_period: Contemporary (as documented, 2026)
public_media: video; sound; performance
public_pathway_timeline: 2027|build-institution|found-standalone-museum|Venue opens on the Lower East Side, Manhattan
public_origin: Robert Rosenkranz, a collector who has long shown time-based work inside his own home, is funding a purpose-built public venue for video, sound, and performance art in Manhattan, led by former MASS MoCA director Joe Thompson.
public_sources: canyon.org; The Art Newspaper; Artnet
hero_image_status: no_usable_image
living_collector: true
last_reviewed: 2026-09
---
# Canyon — the sample's first case built around a medium, not an object collection, and a genuine taxonomy test for `collection_coherence`

**New case, 2026-08-24 (twenty-fourth run), chosen for thesis diversity: every other standalone-museum case in the sample organizes around collected objects (paintings, sculpture, decorative arts); Canyon organizes around durational, largely non-collectible art forms (video, sound, performance) instead.** WebFetch re-tested this run against projects.propublica.org — `EGRESS_BLOCKED` again (see [[report-dataset]]); no EIN or 990 was located via WebSearch (the venue has not yet opened and may not yet be separately registered, or is registered under a name not surfaced by search), so financials are `unknown` for a currently-structural reason, not just an unpulled filing. Figures below are press-sourced (The Art Newspaper, Artnet, Artforum, Canyon's own site), tagged `secondary`.

## Coded header
- `pathway`: **found-standalone-museum** [source: canyon.org/about ; confidence: primary] · `secondary_pathways`: [] · `pathway_is_branched`: no
- `founder_status_at_transition`: **living** (Robert Rosenkranz) · `founder_still_living_now`: **living** · `survived_founder`: **not-yet-testable** (pre-opening)
- `outcome_category`: **emerging** (opening reported as 2027; initial 2026 announcements were revised later to 2027 — see Gaps) · `durability_signal`: **indeterminate**
- `governance_control_at_founding`: **founder-sole** (Rosenkranz is the sole named funder; Joe Thompson, ex-MASS MoCA director, leads operations, but no independent board was located via WebSearch) [confidence: secondary — absence of evidence, not confirmed absence]
- `building_type`: **adapted-other** (a 40,000 sq ft disused space inside the Essex Crossing mixed-use complex, Lower East Side, converted for gallery/performance use) · `collection_coherence`: **tight-single-thesis, but a taxonomy-boundary case** — like [[onera]], Canyon holds **no owned object collection at all**; its "coherence" is a medium commitment (durational/time-based work) rather than a set of acquired objects. Coded `tight-single-thesis` for the strength of the curatorial thesis, flagged as the sample's second medium-not-object taxonomy case after Onera · `coherence_drifted`: no
- `decision_owner`: **collector-alone** · `primary_friction`: **none-documented**
- `constraints_documented`: **open** (living founder, no instrument located)

**Governance sub-fields:** `board_type`: **unknown** (no independent board located) · `succession_locked_before_founder_death`: **unknown** · `founder_control_mechanism`: **informal** (sole funder + hired director) · `donor_intent_instrument`: **unknown** · `endowment_governance`: **unknown**

**Quantitative fields:**
- `collecting_start_year`: **n/a** (no owned collection) · `transition_year`: **n/a** · `institution_open_year`: **2027** [secondary — see Gaps for the 2026→2027 date revision] · `legal_recognition_year`: **unknown**
- `collection_size_at_founding` / `collection_size_current`: **n/a** (a programming venue, not a collecting institution — like Onera, this sits outside the schema's object-count fields by design, not by omission)
- `founding_endowment_usd` / `net_assets_latest` / `total_expenses_latest` / `true_endowment_usd`: **unknown — no EIN located** · `net_assets_to_opex_ratio` / `endowment_to_opex_ratio`: **not computable**
- `earned_revenue_latest` / `annual_attendance` / `fte_headcount`: **unknown**

## Narrative
Canyon is worth coding now, before it opens, specifically because it breaks the pattern every other standalone-museum case in this sample shares: a founder assembling and then housing an **object collection**. Rosenkranz's commitment is instead to a **medium** — video, sound, and performance work that by nature resists both permanent display and, often, individual ownership in the way a painting or sculpture can be owned. Positioned explicitly by its founding team as a hybrid of museum, performing-arts venue, and "third place" (evening hours, hospitality, long-partner relationships with Electronic Arts Intermix, Rhizome, and the Archive of Contemporary Music), it is closer in spirit to Onera's no-collection foundation model than to any of the sample's built-museum cases, giving the dataset a second data point on how the `collection_coherence` field should handle an institution organized around a curatorial thesis rather than an inventory.

The venue's own announced opening date moved from "2026" in its earliest June 2025 press coverage to "2027" in later reporting, an ordinary pre-opening slip rather than a distress signal, but worth tracking as this dataset's newest live opening-date case alongside [[muzej-lah]] and [[amoca-cardiff]]. No governance structure beyond "founder funds, hired director operates" was locatable via WebSearch; whether an independent board exists is genuinely unknown rather than confirmed founder-sole, and is the case's single highest-value re-fetch target once WebFetch unblocks or the venue's own site publishes governance information after opening.

## Primary sources to obtain
Canyon's own IRS filing once an EIN can be located (not found this run under "Canyon" or "Canyon NYC" in WebSearch-surfaced aggregators); a primary account of its legal structure (board vs. founder-sole); a confirmed opening date once construction is closer to complete; the founding gift amount, not yet disclosed in any source found.

## Gaps / contradictions
- **Opening date has moved once already** (2026 → 2027 across different press cycles) — coded conservatively as 2027, the most recent sourcing, but not confirmed as final.
- **No EIN or financial filing located** — genuinely unknown whether this is a standalone 501(c)(3), a project of an existing foundation, or a for-profit LLC funding a public program; this is a structural gap in what WebSearch can surface pre-opening, not a WebFetch failure.
- **Governance is coded `founder-sole` on an absence of evidence** (no board found), which is the weakest form of this field's evidence and should be revisited once the venue opens and publishes more about itself.
