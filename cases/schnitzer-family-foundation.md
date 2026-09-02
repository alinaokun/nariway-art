---
type: case
sample: report
title: Jordan Schnitzer Family Foundation
origin: individual
pathway: traveling-program
status: coded
priority: medium
founder_status: living
geography: Portland, OR, USA
outcome: founder-open
verification: spot-verified
decision_owner: collector-alone
interview_status: not-contacted
hypotheses: [H3, H5, H7A]
public_page_eligible: true
public_verified: true
public_depth: expanded
public_status_text: "Active lending program based in Portland, OR; founder living."
public_name: Jordan Schnitzer Family Foundation
public_founder: Jordan D. Schnitzer
public_location: Portland, Oregon, USA
public_founded: 1997
public_structure: Private operating foundation (nonprofit, 501(c)(3))
public_access: No public gallery of its own; works circulate on free loan to partner museums nationwide
public_size: 22,000+ works
public_focus: Prints and multiples by major and emerging contemporary artists
public_movements: Contemporary printmaking
public_period: mid-20th century to present
public_media: prints; multiples
public_selected_artists: Judy Chicago; Chuck Close; Kara Walker; Ed Ruscha; Roy Lichtenstein
living_collector: true
public_pathway_timeline: 1997|found-foundation|found-foundation|Jordan Schnitzer establishes the Jordan Schnitzer Family Foundation ;; 1997-2026|traveling-program|traveling-program|Foundation lends prints free of charge to museums; over 160 exhibitions organized at 120+ venues
public_origin: Portland real-estate developer Jordan Schnitzer built a collection of over 22,000 prints and multiples and, rather than founding a museum, structured his foundation as a circulating lending library — placing works with museums that lack their own blue-chip holdings, at no cost beyond shipping and insurance.
public_sources: Jordan Schnitzer Family Foundation (jordanschnitzer.org); Artnet News; Cause IQ
hero_image_status: no_usable_image
last_reviewed: 2026-09
---

# Jordan Schnitzer Family Foundation

One-line: Portland developer Jordan Schnitzer built a 22,000+-work print collection and, instead of founding a museum, runs it as a free-lending circulating program — 160+ exhibitions placed at 120+ museums since 1997 — a living, non-museum answer to "what becomes of a large collection" that this dataset had not yet coded.

**Why in the sample:** the sample's clearest *traveling-program* pathway with a still-living, still-active founder (joining [[kinsey]], [[bank-of-america-collection]], and [[petrucci-family-foundation]] as the only other `traveling-program`-coded cases, and the only one built by an individual rather than a bank or an existing foundation partnership). Directly tests H5 (filling a gap — regional museums without their own print holdings) and H3 (a standalone museum is not the only, or even the modal, "serious collector" outcome) with a real, well-documented counter-example to the founder-museum default.

## Coded header
- `pathway`: **traveling-program** (the foundation's core activity is circulating the collection on loan, not housing it) [source: [Lending Program — Jordan Schnitzer Family Foundation](https://jordanschnitzer.org/lending-program); confidence: secondary] · `secondary_pathways`: [found-foundation] · `pathway_is_branched`: yes (the loan program operates through a formally incorporated private foundation)
- `founder_status_at_transition`: **living** · `founder_still_living_now`: **living** · `survived_founder`: **not-yet-testable**
- `outcome_category`: **founder-open** (actively growing; founder still directing acquisitions and lending) · `durability_signal`: **strong** (28 years of continuous operation, growing asset base, no evidence of distress)
- `governance_control_at_founding`: **founder-sole** [inferred — no evidence found of an independent board exercising control distinct from Schnitzer's direction]
- `building_type`: **no-building** (the foundation holds no public gallery; the collection lives in storage and circulates) · `collection_coherence`: **coherent-multi** (prints/multiples across many artists and decades, unified by medium rather than a single thesis) · `coherence_drifted`: no
- `decision_owner`: **collector-alone** · `primary_friction`: **none-documented**
- `constraints_documented`: **open** (living founder; no succession or post-founder plan located in this run's sources — a genuinely open question, distinct from `unknown`)

**Quantitative fields:**
- `collecting_start_year`: **unknown exact year** (Schnitzer's personal collecting predates the 1997 foundation) · `transition_year`: **1997** (foundation established) [secondary] · `institution_open_year`: **n/a** (no physical venue) · `legal_recognition_year`: **1997** [secondary, EIN 93-1236637]
- `collection_size_current`: **22,000+ works** [source: [Artnet News, "Inside 'Prince of Prints' Jordan Schnitzer's Sprawling Collection"](https://news.artnet.com/art-world/jordan-schnitzer-portland-2764270); confidence: secondary]
- `net_assets_latest`: **$76,944,091** (2024, per aggregator citation of the foundation's Form 990) [source: Instrumentl 990 Report / Cause IQ, both citing IRS Form 990 filings; confidence: secondary — WebFetch to ProPublica (EIN 93-1236637) blocked this run, added to Primary-verification backlog] · `total_expenses_latest`: **unknown** · `net_assets_to_opex_ratio`: **not computable** · `true_endowment_usd`: **unknown** (Schedule D unpulled)
- **Growth trajectory**: total assets grew from **$22.2M (2019) to $76.9M (2024)**, a 246% increase over five years [source: Instrumentl 990 aggregation; confidence: secondary] — the only case in this sample with a multi-year asset-growth series available pre-primary-verification, worth flagging for the report's "which models are still growing, not just surviving" framing
- `annual_attendance`: **n/a** (no single venue; attendance accrues to the 120+ host museums, not trackable at the foundation level) · `fte_headcount`: **unknown**
- **Program scale**: over **160 exhibitions** organized, placed at more than **120 museums** since inception [source: [About — Jordan Schnitzer Family Foundation](https://jordanschnitzer.org/about); confidence: secondary]

## Narrative
Jordan Schnitzer, a Portland, Oregon real-estate developer, built one of the largest privately held print collections in the United States — more than 22,000 works spanning major postwar and contemporary artists (Judy Chicago, Chuck Close, Kara Walker, Ed Ruscha, Roy Lichtenstein among the names cited) alongside deliberate support for emerging artists. Rather than building a museum to house it — the default pathway this dataset otherwise codes most often for a collection of this scale — Schnitzer structured his 1997 foundation around circulation: works are lent free of charge (beyond shipping and insurance) to museums that request them, with foundation staff handling curatorial coordination, artist relationships, and publications. The result, per the foundation's own account, is over 160 organized exhibitions placed at more than 120 venues, disproportionately regional museums that could not otherwise mount a blue-chip print show.

The model is instructive for H5 (gap-filling): prints and multiples are, as the source material notes, a more affordable and portable category than paintings or sculpture, which lets Schnitzer's foundation reach institutions systematically excluded from single-object blockbuster loans — smaller university and regional museums rather than the largest metropolitan institutions. It is also a clean test of H3: a collection this size, with obvious financial capacity to found a standalone museum (Schnitzer's family name already appears on the Jordan Schnitzer Museum of Art at the University of Oregon, a *separate*, earlier-named gift, not this foundation's own venue), instead chose the lighter, non-building traveling-program pathway — evidence that "found a museum" is a choice among several viable large-collection pathways, not the inevitable one.

Because Schnitzer is living and the foundation's public materials describe no succession plan, `survived_founder` is coded `not-yet-testable` and `constraints_documented` as `open` rather than `unknown` — the template's distinction for a genuinely undecided living-founder case. The foundation's own Form 990 asset growth (a secondary-sourced $22.2M→$76.9M five-year trajectory) is the most concrete financial trend line available in this sample without a primary pull, and is flagged for upgrade once WebFetch access to ProPublica's Nonprofit Explorer (EIN 93-1236637) resumes.

## Gaps / contradictions
- **No succession plan documented.** What happens to the collection and lending program after Schnitzer is the single largest open question for this case — genuinely unknown, not merely unresearched, per the sources available this run.
- **Financial figures are aggregator-cited, not primary-pulled.** All net-asset figures trace to Instrumentl/Cause IQ's citation of Form 990 data, not a direct ProPublica or IRS.gov fetch (blocked, `EGRESS_BLOCKED`, this run). Primary source to obtain: ProPublica Nonprofit Explorer, EIN 93-1236637, for Schedule D (true endowment vs. net assets), Part I FTE headcount, and total expenses.
- **Collecting-start year not isolated.** Sources describe Schnitzer's personal collecting as predating the 1997 foundation but do not cite a specific start year.
