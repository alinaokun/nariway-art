# The Guide — knowledge-domain map (the thinking exercise, 2026-08-22)

> Before designing pages or freezing nav labels, map the KNOWLEDGE DOMAIN itself and let the structure emerge — the same method that produced the collection data model and the pathway taxonomy. The question is not "what pages should we build" but: **if Nariway were to become the most useful serious reference on private art collections, what would someone need to be able to learn there?** Derived from the vault's existing structures (the [[research-program]] ecosystem agenda, the [[decision-map]] lifecycle, [[field-definition]], the [[what-becomes-of-great-art-collections|report]] Part 4), not invented.

## The architecture simplification (agreed direction, 2026-08-22)
Collapse Decisions / Topics / Findings / Flagship Report / Market Research into ONE body of knowledge. They were never different *types* of information — they were internal filing categories leaking to the reader. The public nav becomes **three**, each answering one reader question:
- **Collections** — *what have others actually done?* (the evidence; live)
- **[Guide]** — *what should I understand?* (this body of knowledge)
- **Conversations** — *what do people who work with collections know?* (firsthand)

Decisions, Findings, and the flagship report do not disappear — they become *ways of organizing and entering* the Guide, not separate products. The website itself becomes the flagship research; a periodic "State of Private Collections" is an *output* from it, never a permanent container to feed.

**Naming (open; label renders from a lookup, so it never blocks the build):** "Research" is accurate but reads academic/inward. Recommended, in order: **Guide** / **The Guide** (answers "what should I understand," unpretentious) · **Field Guide** (most elegant — pairs with Collections as the specimens and Conversations as the field's voices) · **The Field** (most ambitious, most abstract). Placeholder below: **the Guide**.

## The domain, grouped into four areas (the emergent structure)
Each area lists the subjects it covers and the vault assets that already feed it (so this is derivation, not invention). Every subject is an *entry* in the Guide whose depth follows the evidence — no container is built empty.

### A. The Landscape — *the scale and shape of the field* (houses the macro anchor)
Scale of private art wealth · the Great Wealth Transfer and art · art within UHNW wealth · collector demographics · geographic patterns · the private-museum landscape (how many, where, opening/closing rates) · the economics of private museums.
*Feeds from:* [[market-intelligence]] macro + institutional-economics; [[claims-register]]; the report's transfer spine. **The non-negotiable v1 macro anchor ("The Great Wealth Transfer and Art") lives here.**

### B. Holding a Collection — *the collection as a held asset*
Ownership structures and entities · valuation and appraisal · insurance · storage and conservation · documentation and provenance · the cost of keeping art · art finance and lending.
*Feeds from:* the ecosystem agenda (cost-of-keeping, insurance, valuation/appraisal, art finance); [[case-template]] governance fields.

### C. Passing It On — *transition and succession*
Estate planning · tax and legal structures · heirs and family dynamics · governance design · keeping a collection together vs dividing it · the founder-death stress test.
*Feeds from:* the ecosystem agenda (tax & legal); [[decision-map]] (Structure→Sustain); the Evidence Base H1/H6/H8; the Erskine and Asher Conversations. **The non-negotiable v1 first Topic ("Estate Planning and Art Collections") lives here.**

### D. Into Public Life — *bringing a collection into public view (where the pathways live)*
The spectrum of sharing (ownership ≠ access) · the pathways: build an institution · partner with an institution (loan / university / lending) · give to an institution · disperse deliberately · sell · keep in the family. Each with its comparison and its example collections. Also: museum gifts and acceptance policies · long-term loans · foundations · public-access models.
*Feeds from:* [[field-definition]]'s central tension and public-life dimensions; the [[decision-map]] forms; the pathway families + the audited grammar; the report's pathway work.

**Where "Decisions" goes:** it dissolves into Area D. "Partner with an institution" is not a special page *type* — it is a substantial Guide entry within *Into Public Life*, containing the ways-it-has-been-done, the example collections (Anderson, Fisher, Broad…), and the factual comparison table. The decision *framework* remains core IP; it just stops being a nav tab. (Suspicion confirmed: "Decisions" does not survive as a top-level category.)

**Cross-cutting, not its own area — the professional ecosystem:** who does what (appraiser, estate attorney, tax adviser, insurer, conservator, art adviser, family office, auction house, museum). Appears factually within the relevant entries (e.g. the "professional roles" block in the Estate Planning entry), plus perhaps one small reference entry. Facts, not a sales pitch.

## How the existing pieces map (nothing is lost)
| Old container | New home |
|---|---|
| Topics (estate planning, wealth transfer, insurance, valuation…) | Guide entries across A–D |
| Decisions / pathway pages | entries within **D. Into Public Life** |
| Flagship Report | the Guide *is* the flagship; a periodic "State of" is an output |
| Market Research | **A. The Landscape** |
| Findings | appear inside the relevant entry first; earn a dedicated note only when substantial |

## What to confirm before freezing (open)
- The exact area count and labels (four is the emergent shape; test it against the full subject list before locking).
- The section name (Guide / Field Guide / The Field).
- Whether the professional ecosystem is purely cross-cutting or also one small standalone entry.
- The export contract currently carries separate `decisions` and `topics` arrays; when this settles, they may consolidate into Guide entries — no change needed now (the site is deploying Collections first).

**Discipline note:** this is a thinking exercise, not a build order. No Guide pages are built until the structure is confirmed and the content exists (the killed-Histories / killed-Reference-chapter rule). Entries appear because a subject deserves treatment and the evidence supports it, never to fill an outline.
