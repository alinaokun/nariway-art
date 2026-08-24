---
type: case
sample: report
title: AMOCA — Artistic Museum of Contemporary Art
pathway: found-standalone-museum
status: coded
priority: medium
founder_status: living
geography: Cardiff, Wales, UK
outcome: emerging
verification: spot-verified
decision_owner: collector-alone
interview_status: not-contacted
hypotheses: [H5, H6]
origin: private
public_page_eligible: true
public_verified: true
public_depth: expanded
public_status_text: "Registered as a UK charity in August 2025; running pop-up exhibitions ahead of a planned permanent home in central Cardiff, expected in 2026."
public_name: AMOCA — Artistic Museum of Contemporary Art
public_founder: Anders Hedlund
public_location: Cardiff, Wales, UK
public_founded: 2025
public_structure: Registered UK charity (Charity Commission no. 1214619), not-for-profit
public_access: Pop-up exhibitions pre-opening; permanent public museum planned 2026
public_size: ~1,000 works from the founder's private collection, plus other exhibiting artists
public_focus: Contemporary art, minorities and subcultures, Welsh artists
public_movements: Contemporary art (broad, cross-medium)
public_period: contemporary
public_media: (medium breakdown not itemized in sources this run)
public_pathway_timeline: 2025|build-institution|found-standalone-museum|AMOCA registers as a UK charity and holds its first pop-up exhibition at Cardiff's Temple of Peace ;; 2026|build-institution|found-standalone-museum|Permanent museum home planned to open in central Cardiff (exact date not yet announced)
public_origin: Cardiff-based, Swedish-born entrepreneur Anders Hedlund founded AMOCA to give Wales its first dedicated contemporary art museum, planning to show roughly 1,000 works from his own private collection alongside other artists, with a stated focus on minorities, subcultures, and platforming Welsh talent.
public_sources: Museums Association; Time Out; Welsh Centre for International Affairs; UK Charity Commission register
hero_image_status: no_usable_image
living_collector: true
last_reviewed: 2026-08
---

# AMOCA — Artistic Museum of Contemporary Art

*Coded to [[case-template]]. WebFetch re-tested this run (projects.propublica.org) and re-confirmed `EGRESS_BLOCKED` — the twenty-third consecutive confirmation; amoca.wales itself was not attempted this run. Coded from WebSearch-snippet synthesis of Museums Association, Time Out, the Welsh Centre for International Affairs, and — notably — a direct WebSearch hit on the UK Charity Commission's own public register (charity number 1214619, registered 20 August 2025), which is a genuine primary-registry confirmation obtained without a blocked fetch, distinguishing this case from [[goodwood-art-foundation]], whose UK charitable status remains entirely unconfirmed. Chosen from [[candidate-universe]] §"Signals cycle 1" as a small, overlooked, pre-opening international case: Wales' first dedicated contemporary art museum, a genuinely new civic institution rather than a mega-gift to an existing one.*

One-line: Cardiff-based, Swedish-born entrepreneur Anders Hedlund (founder of IG Design Group) registered AMOCA as a UK charity in August 2025 to give Wales its first dedicated contemporary art museum, running pop-up exhibitions ahead of a planned central-Cardiff permanent home slated for 2026, built around roughly 1,000 works from his own collection alongside other artists with an explicit focus on minorities, subcultures, and Welsh talent.

## Why in the sample

Most standalone-museum cases in this dataset are either well-established (Barnes, MoMA, Menil) or mid-construction with a fixed opening date (Lucas Museum, Muzej Lah). AMOCA is earlier-stage than either — charity-registered but still pop-up-only, with no confirmed permanent site or opening date — making it the sample's clearest test of a `found-standalone-museum` case caught at the *very* beginning of its pathway, before `outcome_category` can be more than `emerging`. It is also a genuine UK regional-gap case (Wales had no dedicated contemporary museum before this), a small/overlooked geography this sample under-represents relative to London/New York/California, and — via the located Charity Commission registration — the sample's first UK case where charitable status is directly confirmed against the government's own public register rather than inferred from press characterization, a useful contrast to [[goodwood-art-foundation]]'s unconfirmed status.

## Coded header (dataset row)

`case_id`: (report) · `collection_name`: AMOCA (Artistic Museum of Contemporary Art) · `founder_name`: Anders Hedlund · `geography`: Cardiff, Wales, UK · `verification_status`: **Spot-verified** (founding, charity registration date/number, founder identity, and collection focus cross-verified across ≥4 independent sources including the UK Charity Commission's own register; permanent site and opening date unconfirmed by any source)

- `pathway`: **found-standalone-museum** (new-build/civic museum plan; currently pop-up-stage) [confidence: secondary] · `secondary_pathways`: [] · `pathway_is_branched`: no
- `founder_status_at_transition`: **living** · `founder_still_living_now`: **living** · `survived_founder`: **not-yet-testable**
- `outcome_category`: **emerging** (charity registered Aug 2025; pop-up exhibitions only; permanent museum not yet open) · `durability_signal`: **indeterminate**
- `governance_control_at_founding`: **founder-sole** [confidence: secondary — UK charity law requires a trustee board, but no trustee roster beyond Hedlund was located via search this run; the Charity Commission's own governing-document page was surfaced but not fetched]
- `building_type`: **no-building** (pop-up/touring exhibitions only as of this run) → planned **purpose-built or adapted-other** once the permanent Cardiff site is secured
- `collection_coherence`: **coherent-multi** (contemporary art broadly, cross-medium, with an explicit minorities/subcultures/Welsh-artist thesis giving it more focus than a pure encyclopedic survey)
- `decision_owner`: **collector-alone** (every source attributes the initiative to Hedlund personally)
- `primary_friction`: **none-documented** (no permanent site secured yet, but no source frames this as friction rather than normal pre-opening sequencing)
- `constraints_documented`: **open** (living founder, no governing instrument located beyond the Charity Commission's registration record, which was not fetched)

**Governance sub-fields:** `board_type`: **unknown** (a UK charity trustee board legally exists but its membership was not located this run) · `succession_locked_before_founder_death`: **unknown** · `founder_control_mechanism`: founder-initiated and founder-funded per every source; Hedlund is also described as the museum's co-founder alongside the institution itself, implying at least one other founding party not named in sources found · `donor_intent_instrument`: **unknown** · `endowment_governance`: **unknown** — charity registered but no annual accounts yet due/filed at this early stage

**Quantitative fields:** `collecting_start_year`: **unknown** · `institution_open_year`: **2025** (charity registration; pop-up launch) — permanent museum opening **2026, exact date unannounced** [source: Museums Association; Time Out; confidence: secondary] · `legal_recognition_year`: **2025-08-20** (UK Charity Commission registration date, charity no. 1214619) [source: UK Charity Commission register; confidence: secondary — surfaced via WebSearch, not directly fetched, but the register itself is a primary government source] · `collection_size_current`: **~1,000 works** (from Hedlund's private collection, to be exhibited alongside other artists) [source: iAsk/News summary of press coverage; confidence: secondary] · `founding_endowment_usd` / `net_assets_latest` / `total_expenses_latest` / `true_endowment_usd` / `fte_headcount` / `annual_attendance`: **unknown** (too early-stage for any UK Charity Commission annual return to exist yet)

## Narrative (sourced)

Anders Hedlund, a Cardiff-based, Swedish-born entrepreneur best known for founding the global company IG Design Group, launched AMOCA as Wales' first dedicated contemporary art museum project, aiming to exhibit roughly 1,000 works from his own private collection alongside temporary and touring exhibitions, with a stated focus on increasing public access to contemporary art, spotlighting minorities and subcultures, and specifically platforming Welsh artists [source: iAsk News summary; Time Out, 2025; confidence: secondary]. The project pre-launched with a pop-up exhibition at Cardiff's historic Temple of Peace (Marble Hall) on June 4, 2025, ran further pop-up programming through the year, and was formally registered as a charity with the UK Charity Commission on August 20, 2025 (charity number 1214619) [source: Welsh Centre for International Affairs; UK Charity Commission register; confidence: secondary]. As of this run, no permanent building has been confirmed — press coverage describes only that "plans are underway to secure a permanent building in Cardiff" for a 2026 opening, with the charity's registered address (a private address in Lisvane, Cardiff) evidently administrative rather than the museum's future public site [source: Museums Association, "Museum openings not to miss in 2026"; confidence: secondary].

This is the earliest-stage `found-standalone-museum` case in the sample: the founder, funding intent, and now legal charitable status are all confirmed, but the actual public-facing institution — building, opening date, board, and any financial disclosure — does not yet exist to code. It is included now, rather than deferred, on the same logic as [[muzej-lah]] and [[lucas-museum]]'s pre-opening seeding: a real, sourced, registered case is more valuable to the dataset caught early (revisitable as it develops) than skipped until it is fully resolved.

## Primary sources to obtain

1. amoca.wales fetched directly, for the museum's own account of its founding, mission, and any published governance/trustee information.
2. The UK Charity Commission's own governing-document and trustee filings for charity number 1214619 (both pages were surfaced by search this run but not fetched), to establish the actual trustee board beyond Hedlund and resolve `board_type` and `governance_control_at_founding` from `secondary` to `primary`.
3. A confirmed permanent-site announcement and opening date once published — both remain `unknown` in every source located this run.
4. AMOCA's or Hedlund's own materials for a reconciled, itemized collection count and medium breakdown, currently sourced only to a single secondary summary's "~1,000 works" figure.

## Gaps / contradictions

- **No permanent site or opening date confirmed** — every 2026-dated source describes the permanent museum as still pending, the central fact this case cannot yet resolve.
- **Trustee board membership unlocated** — UK charity law requires trustees distinct from the founder, but none beyond Hedlund is named in any source found this run, so `governance_control_at_founding` is coded `founder-sole` on an absence of evidence, the same caveat [[case-template]]'s worked McNay example flags for `constraints_documented`.
- **Collection size (~1,000 works) sourced to a single secondary summary**, not independently corroborated across multiple outlets the way most other coded figures in this sample are.
