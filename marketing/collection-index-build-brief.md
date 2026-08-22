# Nariway Collection Index — Production Brief (build spec, 2026-08-22)

> The single specification the **`nariway-rebuild`** website project builds from. It assembles everything settled across five prototypes, the 73-case taxonomy audit, and the standards. Concept and design rationale live in [[collection-index]] and [[collection-index-architecture]]; this file is the buildable instruction. Prototyping is complete. No further prototypes.

## 0. What the product is
**A documented map of the decisions private art collections face, built from what collectors and institutions have actually done.** Not a report, not a downloadable PDF, not a textbook, not a directory. A continuously-maintained, web-native research platform. The unit is **the collection as an entity with a life history** (longitudinal) — the white space no one owns (Larry's List maps museums, Art Privée institutions, Collect24 artworks).

Multiple doors, one research ecosystem: a collector enters at "my children don't want the art," an attorney at "examples of long-term museum loans," a journalist at "current wealth-transfer data," a family-office adviser at "appraisal/tax/insurance/succession." All reach the same underlying research.

## 1. Governing principles (apply to every page)
1. **Nariway does not need to sound clever.** Authority comes from connecting what others have not and documenting it carefully. Banned everywhere: manufactured "not X, but Y" theses, quotable pull-lines written to impress, lesson-announcing section titles ("What X shows"). This is what AI competitors cannot easily imitate.
2. **Facts vs interpretation are separated by LAYER.** A collection page reports; interpretation lives above it (Decisions compare, Findings conclude). The case supplies evidence; synthesis happens one level up. Write cases faithfully first, compare later — a confirmation-bias safeguard.
3. **Internal research schema ≠ public page schema.** The corpus classifies in far more detail than the site exposes (e.g. `founder_status`, analytic `outcome_category`, `retain-and-steward` are internal-only).
4. **Don't build a container before there is content worthy of it** (the killed-Histories / killed-Reference-chapter lesson). Sections, Decision pages, Topics, and Findings appear only when evidence supports them.
5. **Public by choice.** The Index covers collections that have entered the public record deliberately; it never uncovers collections owners kept private. Public copy is grounded only in documented public information. A client's private information never appears without separate explicit permission.
6. **Verify-to-grade.** Every figure carries a source; time-sensitive numbers also carry an effective date and a last-verified date. Unknown is a first-class value, never filled with plausible prose.

## 2. Public architecture (five layers + the private corpus)
- **Collections — verified PRECEDENT.** One canonical page per collection; depth expands with evidence.
- **Decisions — verified COMPARISON.** What forms a collector can choose among; public pages only when the corpus has enough cases to compare usefully.
- **Topics — CONTEXT.** External data + professional/legal/tax frameworks (wealth transfer, estate planning, tax, valuation, insurance, appraisal, conservation, philanthropy, lending, family governance, jurisdictions). Macro lives here, at higher altitude, not a separate silo.
- **Conversations — EXPERTISE.** Firsthand practitioner perspective (already live on nariway.com).
- **Findings — earned CONCLUSIONS.** Not a required publishing format; a finding appears inside the page where it belongs first, and earns its own URL only when important enough to cite independently.
- Underneath: the **private research corpus** ([[report-dataset]], [[what-we-now-believe]]), more detailed than the public site.

Each layer checks the others: a Topic (tax rule) explains why a Collection took its path; a Collection shows what a Decision looks like in practice; a Conversation reveals what documents miss; enough Collections → original data → Findings → which improve Decisions and Topics. That loop is the research engine, and it is the commercial asset (a prospect sees the expertise before ever speaking with Alina).

## 3. Taxonomy (final)
**Pathway families (public Decisions):** Build an institution · Partner with an institution · Give to an institution · Disperse deliberately · Sell · (Keep it in the family — in the model, but **no public page yet**, n=0 in the corpus, a flagged research gap). **Not a public family:** corporate active-stewardship = internal `retain-and-steward` (subtypes family/corporate/foundation/other); revisit later.
- **Pathway is a TIMELINE of events, not one label.** A case appears under every pathway it touches, anchored to dated events (Fisher: "planned museum → long-term loan"). ~1 in 4 cases are multi-path.
- **`traveling-program` → Partner** when title is retained; reserve Disperse for actual title transfer.
- **Donation to multiple institutions** classified by DOCUMENTED intent (single recipient set = Give; deliberate wide scattering = Disperse). If intent is not publicly documented, leave hybrid/uncertain — never infer.
- **"Partner with an institution" resolves along three independent axes:** Ownership arrangement (gift · long-term loan · partial · co-ownership/shared-title · staged/phased · contested/reverted) · Institutional partner (museum · university · foundation · archive/library · network/consortium · government/state) · Public model (dedicated galleries · integrated · rotating · lending program; combinations allowed). Freeze the value lists only after the full audit refinements are applied to the corpus.
- The coded `pathway`/`outcome` controlled vocabulary in [[case-template]] is the stable data layer; public display labels render from a lookup ("Give to museums" → "Give to an institution" is a display change, never a recode).

## 4. Page-type specifications
Visual reference prototypes (Nariway editorial brand, built to [[design-system]]):
- Collection page: https://claude.ai/code/artifact/ee4d283c-7a51-402d-beeb-c8f049a149ac
- Pathway/Decision page: https://claude.ai/code/artifact/aef32828-dce5-4cdb-a489-7dadddd1b197
- Topic page: https://claude.ai/code/artifact/9f853c63-93b1-4b1c-9fb0-ffdefaad43e7

### 4a. Collection page
Two layers on one URL. **(1) Collection Profile — the structured hero (retrieval)**, art-catalogue style (quiet columns, hairlines, not a dashboard), structured data is the visual lead: a **facts** block (reported facts only: founder · founded/collecting-began · location · structure · public access · current state · size) and a weighted **"The collection" / Composition** block (focus · movements/genres · period · media · **selected artists** given prominence · recipients for dispersal cases). **(2) The expanded record (understanding):** an **Origin** narrative (restrained reference tone; formula = how it began → what it became → what the collector did; flexes shorter for thin cases) then factual sections that EXPLAIN the profile, appearing only where evidence warrants (The place · Structure & governance · After the founder · Public life · Stewardship & cost · Turning points · Current state), then a **timeline**, then **Sources + Last reviewed**.
- **Nariway classification** in its own quiet block (the pathway/-s as a timeline), visually separate from reported fact — this is IP, not fact.
- No interpretive standfirst. No `founder_status` in public display. Unknown fields disappear (no "N/A"). Image optional — the no-image state is a first-class, intentional design state, never a gray placeholder.

### 4b. Decision (Pathway) page
Organized from the collector's decision, built as **structured comparison, not an essay**: a one-line factual framing → **When collectors have chosen this route** (descriptive circumstances, not advice) → **The choices within** (the grammar axes) → **The cases** (structured entries positioned on the axes) → **What differs** (a side-by-side COMPARISON TABLE — the hero — strictly factual, comparable columns; use "Collector-funded infrastructure" not "capital required"; "Post-founder arrangement" stated as fact or "governed by documented terms," never predicted for a living collector) → **Questions this decision raises** (usable by a collector/attorney/adviser in a live conversation). **No "what the cases show" summary** — conclusions wait for Findings on a larger sample.

### 4c. Topic page
Structured reference, not an essay; depth is evidence-dependent. Structure: a short intro → a **sourced-facts hero** (5–6 facts spanning law + economics + collector behavior + corpus) → what-makes-this-different → the decisions it forces → the framework (sourced figures; document the rules and STOP — never "you may be better off…", that is advice) → jurisdiction only where warranted → questions to work through → **professional roles** (factual descriptions of appraiser/attorney/tax adviser/insurer/art adviser — NO Nariway sales pitch in reference copy) → related material → sources. A Topic draws on three evidence kinds (external data · rules/frameworks · Nariway corpus — the third is the differentiator, used only when the corpus supports it). **Facts, not advice.** Disclaimer: one quiet line near the bottom + a site-wide footer/legal page, never a prominent top box.

### 4d. Conversations
Firsthand practitioner perspective. Already live (Hall Rockefeller, Adam Szymanski, Matthew Erskine). Each attaches to the Collections/Decisions/Topics it bears on. Format per [[conversations-series]].

### 4e. Findings
Earned cross-case conclusions. Appear inside the relevant page first; graduate to a standalone Finding URL only when cite-worthy. Never manufactured to fill a section.

## 5. Data model (the collection record)
Stable coded layer = [[case-template]] (`pathway`/`outcome`/governance/coherence/decision_owner/quantitative fields, each with `_source`/`_confidence`). Public page renders a subset. Add now (retrofitting later across 100+ cases is painful): `origin` (narrative), the composition fields as genuinely structured data (focus/movements/period/media/selected-artists/recipients), `pathway` as an ordered event timeline (multi-path), `living_collector`, `public_page_eligible`, `public_depth`, `last_reviewed`, `public_status_text` (the factual public translation of the internal `outcome_category`), and the image-rights block (`hero_image_status` public; `image_source`/`image_rights`/`image_credit`/`image_caption`/`image_verified_date` internal). Let the dataset teach which further composition fields recur before adding them.

## 6. Sourcing, images, access
- **Source hierarchy** (from [[flagship-report]] Standards): primary/official → institutional research → professional standards bodies → academic → quality journalism. **Stricter for Topics** (tax/legal/insurance/macro): a fact like "$15M exemption" cites IRS/Treasury, never a blog. Numbers link to [[claims-register]]. Claim-level sourcing (quiet numbered notes).
- **Images:** never scrape-and-display; publicly visible ≠ reusable. Hierarchy: licensed/press → open-access (Met/NGA/Getty/Wikimedia, verified) → PD portrait → institution/setting → no image. Never stock. Never imply an image is "of" a collection when it only illustrates. **By page type:** Collection = optional; Topic/deep pages strongly prefer a legitimate image (image availability can be a selection criterion for featured depth).
- **Access:** radically open at launch — no email wall, no lead magnet. Add a "Know something we should update?" input channel (a research funnel). A registered "research" layer is deferred until users ask for it; do not build it now.

## 7. v1 scope (ruthless) and what's OUT
**v1 = the architecture capable of becoming the whole thing, populated enough to prove it works:**
- The full **shallow Collection index** (all public-qualified collections as records) — the breadth signal.
- A handful of **deep Collection pages** done well (from the evidence-rich set) — not all cases deep.
- **Decision pages only where the corpus supports a useful comparison** (Partner with an institution is proven; others as cases allow).
- **2–3 Topics** (Estate Planning; The Great Wealth Transfer and Art; one more) — not the full list.
- **Methodology page** (inclusion criteria, definitions, verification, public-by-choice, living-collector handling — methodology is part of the authority).
- **Conversations** (already live) wired in.
- The **cross-link architecture** connecting Collections ↔ Decisions ↔ Topics ↔ Conversations.
- Image-rights handling in the data model. Simple filtering only if genuinely useful; no elaborate interactive visualization.
**Commercial priority if anything is cut:** the Decision/pathway pages and the rich Collection pages are load-bearing (the proof-of-work a referred prospect checks); cut Topics breadth before cutting those.
**OUT / deferred:** the annual PDF report; a Reference-chapter textbook; a premium/registered layer; Findings as a standalone content type; any page a container-first instinct wants but the evidence doesn't yet fill.

## 8. Open items to resolve during the build (not blockers)
- **Verify every figure to grade** before publication — especially Topic tax numbers (the 2026 $15M exemption rests on 2025 legislation) and prototype case figures (Fisher work count, loan terms, form counts).
- **Apply the audit's taxonomy refinements to the corpus**, then freeze the Partner axis value lists.
- The pathway grammar and composition field set are working hypotheses; let the full corpus finalize them.

## 9. Reference set (what the builder reads)
Design: [[design-system]] (Newsreader/Manrope/Schibsted, white + warm near-black, hairlines, sharp corners, both themes). Data & standards: [[report-dataset]], [[case-template]], [[claims-register]], [[what-we-now-believe]]. Field/decision logic: [[field-definition]], [[decision-map]]. Voice: [[voice]], [[ai-tells]]. The full design rationale and the taxonomy audit: [[collection-index]], [[collection-index-architecture]]. Conversations: [[conversations-series]].
