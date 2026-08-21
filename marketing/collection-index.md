# The Nariway Collection Index — knowledge infrastructure (direction taking shape, 2026-08-21)

> **Status: direction, not locked decisions.** Captures where the report/cases strategy is heading after a deep Alina + external-review session. Supersedes the "downloadable PDF report" idea entirely. Consistent with [[flagship-report]]'s "the research is the product" reframe — this is *how the corpus becomes public*.

## The core reframe
The flagship **report is not the asset; the research CORPUS is.** The report was one product of it; the corpus can generate several. So the "report" **dissolves into a continuously-maintained, web-native research platform**, the **Nariway Collection Index** — *tracking what happens to significant private art collections over time.* No PDF, no email-gated lead magnet, no annual freeze.

**This is not a pivot.** It is the public form of what the vault already believes: [[field-definition]] already frames the project as *the larger life of a collection over time*, and Artobiography is *the biography of collections*. The Index is the **biographical model of collections** made public (born → develops → acquires identity → founder ages → ownership changes → remains intact / migrates / institutionalizes / fragments / recombines / dies as a collection / influences after death).

## The distinctive unit = the white space
Nariway's unit of analysis is **the collection as an entity with a life history** (longitudinal). Nobody owns this:
- Larry's List → *collectors* / *private museums* (4,000+ collector profiles; Private Art Museum Report, 166 museums 2016, updated w/ Univ. Amsterdam to **446 museums, 2023**). Deliberately EXCLUDES deceased collectors, corporate collections, and non-museum outcomes — exactly Nariway's territory.
- Art Privée → *private institutions* (a directory).
- Collect24 (Global Art Registry) → *artworks*.
- Museum databases → *objects*.
- **Nariway → the collection's trajectory and destination.** Not "who owns art?" or "where can I visit?" but **"what became of the collection?"** Fundamentally longitudinal.

## The four (→ five) connected assets
| Asset | Role |
|---|---|
| **Collection Corpus** | the underlying proprietary evidence (the coded [[report-dataset]] + [[candidate-universe]]) — the moat |
| **Findings / Research Briefs** | the synthesis and the datable *publishing moments* (replaces the annual report) |
| **Collection Index (Atlas)** | public exploration — the individual histories, pathways, evidence layer |
| **[[conversations-series|Conversations]]** | primary perspectives that challenge and explain the evidence |
| **Collector Study** (later) | original demand-side data on what today's collectors are actually planning ([[problem-discovery]]) — the one thing the case corpus cannot tell us |

## Access model (radically open at launch)
Three eventual layers, but **open first** — the scarce resource is authority and citations, not email addresses:
1. **Public Index** — ~100–250 words per collection, selected structured fields, timeline, outcome, sources, related findings. Completely open. Journalists cite it, professors link it, lawyers send a case to a client, museum people argue with it, collectors find themselves in it.
2. **Research Record** (registered/free account, eventually) — deeper case analysis, governance, financial structure, succession detail, full sources, confidence, research notes. The value exchange is *"explore the evidence,"* NOT *"give me your email to read page 27."*
3. **Internal Nariway Intelligence** (never public) — hypothesis coding, unpublished interview intelligence, advisory implications, prospect info, sensitive observations. **Publish the insight, not the machinery that produces it.**
- **Input channel:** a *"Know something we should update?"* invitation (borrowed from the Univ. Amsterdam private-museum research) — how a database becomes a networked knowledge resource and a research-input funnel.
- **Publish the case NARRATIVE + selected fields; retain the full research RECORD internally.** Do not dump the Obsidian dataset online (that turns months of proprietary coding into a free spreadsheet).

## Publishing rhythm (no annual PDF, but keep the events)
Living platform PLUS periodic, datable, citable **Research Briefs / Special Studies / Data Stories / a short annual web "What changed in private collections in 20XX."** Each brief is a media moment ("Index reaches 100 histories, five findings"; "founder death is not the primary cause of private-museum failure"; "corporate collections added"). Findings are **living essays that can change** ("last updated March 2027"), which is more honest than a stale PDF.

## GUARDRAILS (the friction that keeps this from becoming enrichment) — Claude Code, 2026-08-21
The Index is the best idea and therefore **the most dangerous** — it collides head-on with the risk the [[what-we-now-believe|Evidence Base]] names and the [[scoreboard|check-in dashboard]] exists to police (*building > operating*). A three-tier platform with filters, per-collection pages, interactive pathway viz, and a methodology doc is potentially **months** of the most thrilling deferral yet. So:
1. **Scope and SEQUENCE against the commercial goal.** The test is the [[problem-discovery]] signal ladder, not citation counts. Build the *minimum* that creates authority; gate the platform build behind evidence it earns attention.
2. **DECOUPLE thinking from building.** (a) Lock the intellectual architecture + data model NOW (cheap, sharpens everything). (b) Ship a MINIMAL radically-open v1 (~15–25 exemplary collection pages + pathways framing + 3–4 findings), NOT the full platform. (c) Gate filters / registered research layer / live viz behind v1 actually earning citations/inbound. **Two weeks, not two months, before the first public thing exists.**
3. **Living collectors are a GATING risk, not a footnote.** Publicly coding a living collector's collection "distressed"/"dispersed" is a reputational and legal liability (and some are future clients). Collides with the "no private family circumstances" guardrail in [[research-program]]. Decide BEFORE launch: living collectors get lighter treatment, opt-out, or exclusion from public outcome-coding.
4. **"Continuously maintained" is a public PROMISE** = ongoing verification labor, and a visibly stale "living" index is worse than an honestly-dated report. Only claim "living" for the slice actually maintainable. (The existing `verification` field + a new `last_reviewed` supports this.)
5. **Keep at least one datable, citable publication moment.** "Always live" must not mean "nothing ever launches."
6. **Time-box the methodology work** so methodology-first does not itself become the deferral.

## Methodology-as-authority (the Larry's List lesson)
Before building public anything, draft **Collection Index Methodology v1.0** — and treat it as *part of the authority*, not housekeeping. Open questions to resolve: what qualifies as a "collection" and as "significant"? Corporate collections? Already-fully-dispersed collections? Historical (1850)? Royal? Artist estates? Dealer collections? Decorative arts? Unnamed collections? Precise definitions of thriving / stable / distressed / pivoted / dissolved / dispersed / emerging. Review cadence and what counts as "verified." What to do when sources disagree. **How to handle living collectors and sensitive information** (see guardrail 3). Larry's List *revised* its definition rather than pretending the old one held — do the same.

## The concrete next step (sequenced)
1. **Intellectual architecture + data model** (do first, it's cheap thinking). Take 8–10 deliberately different real cases from the coded set (Barnes vs Broad vs Cisneros vs de la Cruz vs Corcoran vs a corporate dispersal vs Souls Grown Deep) and ask *what should a public reader LEARN from each* — not what fields happen to exist in Obsidian. That defines the **public unit of knowledge**. Then map: which [[case-template]] fields are public vs internal-record; which **longitudinal fields to add now** (`last_reviewed`, `living_collector` flag, `change_log`) because retrofitting 100 cases later is painful.
2. **Study 5–6 serious web research publications** (not "interactive report inspiration") for navigation, progressive disclosure, case exploration, dataviz, citations, methodology, public-vs-registered access, report↔evidence linking. Confirmed exemplars: **State of AI** (report-as-website + predictions database w/ public hit-rate + Compute Index), **Stanford AI Index** (glance→read→investigate; open findings + data; widely cited). Find 4 more from think tanks / journalism / wealth research / museum data projects.
3. **Nariway Research Architecture v1** — page structures + rough wireframes for `/research`, `/collections`, `/collections/{slug}`, `/findings`, `/methodology` — the precise brief Claude Code (the website project) builds from. **Only after 1–2.**

## Reference models (studied)
- **State of AI** (stateof.ai) — the report-is-a-website model; predictions as a permanent searchable product with a public hit-rate; Compute Index as a separate interactive data product. The closest philosophical precedent.
- **Stanford AI Index** — executive findings open to all, chapter pages for depth, underlying public data; three depths *glance → read → investigate*; explicitly built for journalists/policymakers/researchers, hence widely cited.
- **Larry's List Private Art Museum Report** (2016; Univ. Amsterdam update 2023, privatemuseumresearch.org) — precedent for mapping the territory AND for methodological seriousness; their exclusions are Nariway's white space.
- Feel is **research journal × museum publication × data product**, NOT a corporate annual report with animations.
