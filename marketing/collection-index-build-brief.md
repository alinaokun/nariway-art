# Nariway Collection Index — Production Brief (build spec, 2026-08-22)

> The single specification the **`nariway-rebuild`** website project builds from. It assembles everything settled across five prototypes, the 73-case taxonomy audit, and the standards. Concept and design rationale live in [[collection-index]] and [[collection-index-architecture]]; this file is the buildable instruction. Prototyping is complete. No further prototypes.

## 0. What the product is
**A documented map of the decisions private art collections face, built from what collectors and institutions have actually done.** Not a report, not a downloadable PDF, not a textbook, not a directory. A continuously-maintained, web-native research platform. The unit is **the collection as an entity with a life history**: Nariway studies the collection **longitudinally**, rather than primarily the collector, the artwork, the transaction, or the institution (the units the rest of the field is organized around — collectors at Larry's List, artworks at Collect24, institutions at Art Privée).

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
Stable coded layer = [[case-template]] (`pathway`/`outcome`/governance/coherence/decision_owner/quantitative fields, each with `_source`/`_confidence`). Public page renders a subset. Add now (retrofitting later across 100+ cases is painful): `origin` (narrative), the composition fields as genuinely structured data (focus/movements/period/media/selected-artists/recipients), `pathway` as an ordered event timeline (multi-path), `living_collector`, `public_page_eligible`, `public_verified` (the export accuracy gate), `public_depth`, `last_reviewed`, `public_status_text` (the factual public translation of the internal `outcome_category`), and the image-rights block (`hero_image_status` public; `image_source`/`image_rights`/`image_credit`/`image_caption`/`image_verified_date` internal). Let the dataset teach which further composition fields recur before adding them.

## 6. Sourcing, images, access
- **Source hierarchy** (from [[flagship-report]] Standards): primary/official → institutional research → professional standards bodies → academic → quality journalism. **Stricter for Topics** (tax/legal/insurance/macro): a fact like "$15M exemption" cites IRS/Treasury, never a blog. Numbers link to [[claims-register]]. Claim-level sourcing (quiet numbered notes).
- **Images:** never scrape-and-display; publicly visible ≠ reusable. Hierarchy: licensed/press → open-access (Met/NGA/Getty/Wikimedia, verified) → PD portrait → institution/setting → no image. Never stock. Never imply an image is "of" a collection when it only illustrates. **By page type:** Collection = optional; Topic/deep pages strongly prefer a legitimate image (image availability can be a selection criterion for featured depth).
- **Access:** radically open at launch — no email wall, no lead magnet. Add a "Know something we should update?" input channel (a research funnel). A registered "research" layer is deferred until users ask for it; do not build it now.

## 7. v1 scope (ruthless) and what's OUT
**The non-negotiable v1 spine: Collections + Decisions + one macro anchor.** Together they tell the whole story without dozens of pages: *here is the scale of the transition happening now* (the macro anchor) · *here are actual collections that have faced it* (Collections) · *here are the choices they made* (Decisions) · *here is some of the professional knowledge to evaluate those choices* (the first deep Topic). That is a stronger authority position than a database alone or a set of educational articles.

**v1 = the architecture capable of becoming the whole thing, populated enough to prove it works:**
- The full **shallow Collection index** (all public-qualified collections as records) — the breadth signal.
- A handful of **deep Collection pages** done well (from the evidence-rich set) — not all cases deep.
- **Decision pages only where the corpus supports a useful comparison** (Partner with an institution is proven; others as cases allow).
- **The macro anchor — The Great Wealth Transfer and Art (NON-NEGOTIABLE, not "Topic breadth").** Its job differs from a professional Topic: it establishes *why this field matters now*, connecting private collections to the larger transition in private wealth, inheritance, succession, and generational change. Do not treat it as optional decoration.
- **Estate Planning — the first deep professional Topic (in v1).** Demonstrates subject-matter depth. Any Topics beyond these two are optional breadth.
- **Methodology page** (inclusion criteria, definitions, verification, public-by-choice, living-collector handling — methodology is part of the authority).
- **Conversations** (already live) wired in.
- The **cross-link architecture** connecting Collections ↔ Decisions ↔ Topics ↔ Conversations.
- Image-rights handling in the data model. Simple filtering only if genuinely useful; no elaborate interactive visualization.
**Commercial priority if anything is cut:** the Decision/pathway pages, the rich Collection pages, AND the macro anchor + first deep Topic are all load-bearing (the pathway/collection pages are the proof-of-work a referred prospect checks; the macro anchor is why-now, the first Topic is depth). Cut only *additional* Topic breadth before any of those — the macro anchor is NOT Topic breadth.
**OUT / deferred:** the annual PDF report; a Reference-chapter textbook; a premium/registered layer; Findings as a standalone content type; any page a container-first instinct wants but the evidence doesn't yet fill.

## 8. Open items to resolve during the build (not blockers)
- **Verify every figure to grade** before publication — especially Topic tax numbers (the 2026 $15M exemption rests on 2025 legislation) and prototype case figures (Fisher work count, loan terms, form counts).
- **Apply the audit's taxonomy refinements to the corpus**, then freeze the Partner axis value lists.
- The pathway grammar and composition field set are working hypotheses; let the full corpus finalize them.

## 9. How the two repos reconcile (`nariway-art` ↔ `nariway-rebuild`)
**The vault is the database. `nariway-rebuild` is the presentation layer. The website consumes the data; it never re-authors it.** Hand-copying case data into the site repo is the silent-omission/drift failure this whole project has fought — forbidden. The only edited copy of any collection is in the vault.

**Mechanism — a public-projection export.** A script in `nariway-art` reads the coded case files and emits one file, **`export/nariway-public.json`**, committed to the vault. `nariway-rebuild` pulls that single file at build time (not a submodule of the whole vault) and renders it. Research reaches the site by re-running the export, never by copying.

**The gate (publishable ≠ coded):** a case exports only if `public_page_eligible: true` AND `public_verified: true` (the public-facing claims — founder, dates, location, structure, composition/artists, pathway/status — confirmed against the institution's own site or reputable sources). **This is NOT the internal `verification` financial-depth tag.** The public page shows facts, not 990 financials, so public export depends on public-fact accuracy — which is confirmable via WebSearch and institution sites (never egress-blocked) — not on primary 990 pulls (which the cloud WebFetch block prevents). A case can be `public_verified: true` while its internal `verification` is still `secondary`. `status: coded` alone is not enough. This decoupling is what keeps the cloud agent's partly-unverified financial work off the site while NOT holding the whole site hostage to the 990 egress block.

**Privacy (non-negotiable):** the projection emits ONLY public fields. Everything internal — the analytic `outcome_category`, sourcing-tier flags, verify-to-grade notes, prospect info, the private corpus — is stripped by construction. **Never make `nariway-rebuild` a submodule of the vault**; a public deploy would carry private material. It pulls only the projected JSON, which contains nothing private.

**What lives where:** structured collection data → vault, exported (mandatory, or it drifts). Design tokens/templates/CSS → `nariway-rebuild` (the vault holds only the spec, [[design-system]]). All numbers → [[claims-register]] is the single source. **Adopted defaults (reversible):** Topic and Findings prose are authored in the vault (as markdown, versioned with the research, numbers tied to claims-register) and exported like everything else; the export commits into the vault and the site pulls it.

**Population is automated (2026-08-22):** the twice-daily **dataset-research routine** now populates the public-projection fields on every case it codes AND backfills 1–2 already-coded cases per run (launch set first: Cisneros, Fisher, Anderson, Broad, de la Cruz), using the proof set (Chinati/Barnes/Corcoran/Lucas) as the format exemplar. So the corpus fills in its public fields over time without hand-work; the export gate is `public_verified` (public-fact accuracy, confirmable via WebSearch), which is separate from and NOT blocked by the internal 990 `verification` egress problem.

**Prerequisite:** the export only works once the vault frontmatter carries the §5 fields (`public_page_eligible`, `public_depth`, `public_status_text`, composition fields, image-rights block, pathway-as-timeline). Build that data model in the vault BEFORE `nariway-rebuild` wires in real data.

**Steady-state workflow:** research happens in the vault (Alina + cloud agent) → a case is marked public-eligible and its figures verified → run the export → the site rebuilds from the new JSON. Additive, auditable, no drift.

**Auto-deploy (wired 2026-08-24).** The rebuild step is now automatic. `.github/workflows/deploy-site.yml` fires on any push to `main` that changes `export/nariway-public.json` (which the cloud research routine regenerates each run), validates the JSON is non-empty, then POSTs the `nariway-rebuild` host's **deploy hook** (stored as the repo secret `SITE_DEPLOY_HOOK`) to trigger a rebuild that re-pulls the latest export. So a newly verified collection reaches the live site within one build cycle, no manual step. One-time setup the workflow file documents: create the deploy hook in the host (Vercel/Netlify/Cloudflare Pages) and add it as `SITE_DEPLOY_HOOK`. Until the secret is set the workflow runs and safely skips.

**Two content origins (this is how the four content types get into the export):**
- **Collections are GENERATED** from `cases/*.md` (the flat `public_*` frontmatter), automatically, by the export script.
- **Decisions, Topics, and Conversations are AUTHORED** editorial content — they are not per-collection data, so they live in one vault source file, **`content/content.json`**, authored in the vault and **merged** into the export by `scripts/export_public.py`. Prototype content (the Partner-with-an-institution decision, the Estate Planning + Great Wealth Transfer topics, the Conversations index) is ported there. `nariway-rebuild` NEVER authors these in its own repo — it consumes them from the export, same rule as collections. (Correction to an earlier draft: the authored source is `content/content.json`, a SOURCE file; `export/nariway-public.json` is the generated OUTPUT. Do not conflate them.) Figures in `content/content.json` carry a `verify: true` flag until confirmed to grade per §8.

### The export contract (v1)
The projection `nariway-rebuild` consumes. Field names are the contract; add fields as the data model grows, never remove silently.

```json
{
  "generated": "2026-08-22",                     // stamped at export time
  "taxonomy": {
    "pathwayFamilies": [
      { "id": "build-institution",  "label": "Build an institution",     "hasPublicPage": true  },
      { "id": "partner-institution","label": "Partner with an institution","hasPublicPage": true  },
      { "id": "give-institution",   "label": "Give to an institution",    "hasPublicPage": false },
      { "id": "disperse",           "label": "Disperse deliberately",     "hasPublicPage": false },
      { "id": "sell",               "label": "Sell",                      "hasPublicPage": false },
      { "id": "keep-family",        "label": "Keep it in the family",     "hasPublicPage": false }
    ],
    "partnerAxes": {
      "ownership": ["gift","long-term-loan","partial","co-ownership","staged","contested"],
      "partner":   ["museum","university","foundation","archive-library","network","government"],
      "publicModel":["dedicated-galleries","integrated","rotating","lending-program"]
    }
  },
  "collections": [
    {
      "slug": "chinati",
      "name": "The Chinati Foundation",
      "founder": "Donald Judd",
      "location": "Marfa, Texas",
      "profile": {
        "founded": 1986, "collectingBegan": null,
        "structure": "Independent nonprofit foundation",
        "publicAccess": "Open by tour; annual October open house",
        "currentState": "Open, ~340 acres",       // public_status_text — factual, NOT the internal outcome label
        "size": "~13 artists, permanent installations"
      },
      "composition": {                            // structured data, not display copy; omit any unknown key
        "focus": "Minimalism and related postwar and contemporary art",
        "movements": ["Minimalism"],
        "period": "1960s onward",
        "media": ["sculpture","installation","light"],
        "selectedArtists": ["Donald Judd","Dan Flavin","John Chamberlain","Ilya Kabakov","Roni Horn","Claes Oldenburg & Coosje van Bruggen","Richard Long"],
        "recipients": []                          // present only for dispersal/gift cases
      },
      "classification": {                         // Nariway's IP; rendered in its own block, separate from fact
        "pathwayTimeline": [
          { "year": 1986, "familyId": "build-institution", "codedPathway": "found-art-park", "event": "Chinati Foundation opens" }
        ]
      },
      "origin": "Donald Judd grew dissatisfied in the 1970s with…",   // restrained reference prose
      "sections": [                               // appear ONLY where evidence warrants; not mandatory
        { "heading": "The place", "body": "…", "refs": [1] },
        { "heading": "After the founder", "body": "…", "refs": [1,4] }
      ],
      "timeline": [ { "year": 1979, "event": "Acquires Fort D.A. Russell with Dia support" } ],
      "image": { "status": "no_usable_image", "url": null, "credit": null, "caption": null },
      "sources": [ { "n": 1, "text": "The Chinati Foundation (chinati.org)", "url": null } ],
      "lastReviewed": "2026-08",
      "related": { "pathways": ["build-institution"], "topics": ["succession-transition"], "conversations": [], "collections": ["storm-king","menil"] }
    }
  ],
  "decisions": [                                  // pathway pages — only families with hasPublicPage:true AND enough cases
    {
      "slug": "partner-institution",
      "label": "Partner with an institution",
      "framing": "A collector does not have to found a new institution to keep a collection together and publicly accessible.",
      "relevantWhen": ["…"],
      "axes": { "ownership": ["gift","long-term-loan"], "partner": ["museum","university"], "publicModel": ["dedicated-galleries"] },
      "cases": [ { "slug": "anderson-collection-stanford", "ownership": "gift", "partner": "university", "publicModel": "dedicated-galleries", "works": 121, "opened": 2014 } ],
      "comparison": { "dimensions": ["Ownership","Duration","Control retained","Public access","Kept together","Collector-funded infrastructure","Post-founder arrangement"], "rows": [ { "case": "anderson-collection-stanford", "values": ["…"] } ] },
      "questions": ["Who owns the works?","Does the collection have to remain together?"],
      "sources": [], "lastReviewed": "2026-08"
    }
  ],
  "topics": [
    { "slug": "estate-planning", "title": "Estate Planning and Art Collections", "kind": "professional-depth",
      "facts": [ { "value": "$15M", "label": "Federal estate & gift tax exemption per individual (2026)", "source": "IRS / Treasury", "effectiveDate": "2026", "lastVerified": null } ],
      "sections": [ { "heading": "What makes art different", "body": "…" } ],
      "sources": [], "lastReviewed": "2026-08" },
    { "slug": "great-wealth-transfer", "title": "The Great Wealth Transfer and Art", "kind": "macro-anchor", "facts": [], "sections": [], "sources": [], "lastReviewed": null }
  ],
  "conversations": [
    { "slug": "matthew-erskine", "title": "Not every collection can stay whole", "guest": "Matthew Erskine", "url": "https://nariway.com/conversations/matthew-erskine", "relatedTopics": ["estate-planning","succession-transition"], "relatedPathways": ["build-institution"] }
  ]
}
```

**Export script — RUNNABLE, at `nariway-art/scripts/export_public.py`** (dependency-free; reads the flat `public_*` frontmatter; gate = `public_page_eligible AND public_verified`; emits `export/nariway-public.json`; privacy-checked — no internal fields present). First export generated 2026-08-22 with the verified proof set (Chinati, Barnes, Corcoran, Lucas); it grows automatically as the cloud agent backfills `public_verified` cases. Logic sketch:
```python
# Reads cases/*.md, projects the PUBLIC subset to export/nariway-public.json.
# Contract: only public_page_eligible AND public_verified cases; only public fields; internal fields stripped.
import glob, json, re, datetime  # NOTE: pass the date in; the cloud env forbids Date.now()-style calls in some tools

PUBLIC_PROFILE = ["founded","collectingBegan","structure","publicAccess","currentState","size"]
PUBLIC_COMPOSITION = ["focus","movements","period","media","selectedArtists","recipients"]
# fields deliberately NEVER exported: outcome_category, durability_signal, verification, *_confidence,
# decision_owner, secondary-sourcing notes, prospect/CRM data, anything under the private corpus.

def parse_frontmatter(md):  # minimal YAML-ish frontmatter reader
    m = re.match(r"^---\n(.*?)\n---\n", md, re.S)
    return m.group(1) if m else ""

def is_publishable(fm):
    return "public_page_eligible: true" in fm and "public_verified: true" in fm  # gate: eligible AND public-facts confirmed (NOT the internal 990/verification tag)

def project(path):
    fm = parse_frontmatter(open(path, encoding="utf-8").read())
    if not is_publishable(fm):
        return None
    # ... map the PUBLIC fields into the export-contract shape above (profile, composition,
    #     classification.pathwayTimeline, origin, sections, timeline, image, sources, related);
    #     public_status_text -> profile.currentState; NEVER copy internal fields.
    return {"slug": path.split("/")[-1].replace(".md",""), "...": "..."}

def main(today):
    collections = [c for c in (project(p) for p in glob.glob("cases/*.md")) if c]
    out = {"generated": today, "taxonomy": {}, "collections": collections,
           "decisions": [], "topics": [], "conversations": []}
    json.dump(out, open("export/nariway-public.json","w",encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"exported {len(collections)} public collections")

# main(today="2026-08-22")  # pass the date explicitly
```
The gate condition, the field allow-list, and the "NEVER exported" list above are the load-bearing parts — they are what make the private/public boundary enforced by code rather than by discipline.

## 10. Reference set (what the builder reads)
Design: [[design-system]] (Newsreader/Manrope/Schibsted, white + warm near-black, hairlines, sharp corners, both themes). Data & standards: [[report-dataset]], [[case-template]], [[claims-register]], [[what-we-now-believe]]. Field/decision logic: [[field-definition]], [[decision-map]]. Voice: [[voice]], [[ai-tells]]. The full design rationale and the taxonomy audit: [[collection-index]], [[collection-index-architecture]]. Conversations: [[conversations-series]].
