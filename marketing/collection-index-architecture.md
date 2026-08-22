# Collection Index — data model + IA (the pre-build package, 2026-08-22)

> The last conceptual step before ChatGPT's design brief. Built from the vault's OWN coded vocabulary, not invented: the lifecycle from [[decision-map]], the pathways + coded fields from [[case-template]], the measurement layer from [[field-definition]]. Companion to the concept note [[collection-index]]. Purpose: give the brief a real information architecture so Claude Code builds against a spec, not a guess.

---

## PART 1 — THE TAXONOMY (three layers, two of them navigable)

The mistake to avoid is a single tree. A private collection has **two orthogonal structures** plus a **measurement overlay**. All three already exist in the vault in different files; the Index unifies them.

### Axis A — THE LIFECYCLE (chapters) — the reference-work spine ("The Field" + "The Guide")
Derived from [[decision-map]]'s lifecycle (Suitability → Compare forms ⇄ Viability → Select → Structure → Build → Operate → Sustain) and reconciled with ChatGPT's eight draft chapters. Eight chapters, each hosting macro evidence at the top and explanation below (the Stanford *Finding → Chapter → Evidence → Explanation → Sources* hierarchy):

1. **The Collection** — how collections form, coherence, distinctiveness, provenance, documentation, inventory. *(field-definition's unit; coded field `collection_coherence`.)*
2. **Value & Significance** — appraisal, market value vs cultural / historical / personal significance, changing taste. *(the value-vs-significance question; Mark Winter + Eirini intel.)*
3. **Ownership & Structure** — entities, title, trusts, foundations, private operating foundations, fractional interests. *(decision-map "Structure"; the POF note; coded `governance_control_at_founding`.)*
4. **Stewardship & Cost** — conservation, storage, insurance, collection management, the carrying cost of keeping art. *(decision-map "Build/Operate"; claims C13/C14/C15.)*
5. **Public Life** — the spectrum of sharing: loans, exhibitions, university partnerships, traveling, digital, access periods. *(field-definition's central tension "how many ways can privately owned art be shared?"; the public-life dimensions below.)*
6. **Succession & Transition** — heirs, estate planning, governance design, family dynamics, the founder-death stress test. *(decision-map "Sustain"; H1/H6/H8; Erskine's "founder's disease" and "Common Goal".)*
7. **Giving** — museum gifts (intact vs scattered), foundations, charitable structures, donor-intent restrictions. *(H2 the receiving end; Barnes's deed constraints.)*
8. **Sale & Dispersal** — auction, private sale, deaccession, intentional dispersal, fragmentation. *(Cisneros, de la Cruz, Vogel.)*

*The decision-map's front gate ("what could this become?" = Suitability + Compare-forms) is not a ninth chapter; it is the DECISION moment that Axis B serves.*

### Axis B — THE PATHWAYS (destinations) — the "Collections" decision navigation (the COMMERCIAL spine)
This is the case-template `pathway` controlled vocabulary exactly (all 73 cases are already coded in it, so this mapping is mechanical). The 16 coded values group into **six reader-facing decision families** — the view a prospect actually uses ("I'm weighing X"):

| Decision family (public) | Coded `pathway` values it contains |
|---|---|
| **Keep it in the family** | `retain-family` |
| **Build an institution** | `found-standalone-museum` · `found-house-museum` · `found-art-park` · `found-foundation` |
| **Partner with an institution** | `university-partnership` · `long-term-loan` · `merger-into-institution` |
| **Give to museums** | `donate-existing-museum-intact` · `donate-existing-museum-scattered` |
| **Disperse deliberately** | `intentional-dispersal` · `traveling-program` |
| **Sell** | `sell-auction` · `sell-private` |
| *(cross-cutting realities)* | `abandoned-plan` · `hybrid` · `pathway_is_branched` (most real cases are a PORTFOLIO of pathways, not one choice) |

**Each pathway page = the proof-of-work unit:** the decision a prospect is weighing → the cases that took it → the relevant Finding → the relevant Conversation. This is the revenue-relevant navigation; it must be first-class, not buried under the chapters.

### Axis C — THE MEASUREMENT OVERLAY (analytic, not navigation) — powers Findings
Not a menu the reader browses; the scoring that makes the Field chapters evidence-based. Two parts, both already in the vault:
- **The public-life dimensions** ([[field-definition]]): ownership · custody · visibility · physical access · scholarship · education/teaching · geographic reach · number reached. A collection scores high on some, near-zero on others (Vogel: high ownership, low visibility; Fisher: private ownership, high visibility).
- **The coded analytic fields** ([[case-template]]): `outcome_category`, `durability_signal`, `survived_founder`, `collection_coherence`, `decision_owner` (H7A). These stay INTERNAL as analysis; the public sees factual translations (see the vocabulary rule in Part 3).

### How the axes relate (the one-line model)
**A case sits on a pathway (Axis B) and illustrates several chapters (Axis A); the overlay (Axis C) is how we compare cases and write Findings.** A prospect enters by pathway; a researcher enters by chapter; a journalist enters by finding — and all three land on the same underlying case records. That convergence is the thing competitors can't cheaply reproduce.

---

## PART 2 — THE 10-CASE TWO-LENS DRAFTS
Ten deliberately different real cases, each drafted as it would appear PUBLICLY, then read through the Editorial lens (what a reader learns) and the Commercial lens (what decision it proves expertise in), with the template strain noted. Public status language uses factual translation, never the internal `outcome_category` label. Fields that are unknown simply disappear (no "N/A").

### 1. The Barnes Foundation — RICH (artist + governance)
**Public Index Record.** *Merion → Philadelphia, PA · Founder: Albert C. Barnes · Focus: Impressionist, Post-Impressionist, early Modern, hung in fixed pedagogical ensembles · Selected artists: Renoir (181), Cézanne (69), Matisse (59), Picasso (46) · Pathway: built an institution (educational foundation, 1922) · Status: operating in Philadelphia since 2012; relocated from Merion by court order under cy pres · Key dates: 1922 chartered, 1925 Merion opened, 1951 founder died, 2012 Parkway opened, 2023 loans permitted · Why it matters: the canonical case that a documented, aggressive donor-intent instrument is not self-enforcing — a court can rewrite it for viability.*
- **Editorial:** the limits of control from beyond the grave; how "keep it exactly as I built it" collides with money.
- **Commercial:** proves expertise in *donor-intent restrictions and governance design* — the collector who wants to lock terms forever. Pathway: **Build an institution**; chapters: Ownership, Succession, Giving.
- **Strain:** none — this is the model deep history. Anchors the "restrictions can preserve intent yet create fragility" finding.

### 2. The Broad — RICH (governance/finance), artist-poor
**Public Index Record.** *Los Angeles, CA · Founders: Eli & Edythe Broad · Focus: postwar & contemporary, 2,000+ works, ~200 artists · Pathway: partner with an institution (lending library), later also built one · Status: active; lending library since 1984, free museum since 2015; continued after Eli Broad's death (2021) · Why it matters: the clearest case of choosing dispersed access through loans rather than a single monument — then building one anyway.*
- **Editorial:** you don't have to choose one path; access-by-lending vs the monument.
- **Commercial:** proves expertise in *long-term loan / lending-library models* and branched strategies. Pathway: **Partner with an institution**; chapters: Public Life, Stewardship.
- **Strain:** artist-poor (no named artists public). Tests whether the schema survives with an empty "selected artists" field — it must, gracefully. The *focus* + *scale* fields carry the record instead.

### 3. Anderson Collection at Stanford — MODERATE (artist-rich, governance-poor)
**Public Index Record.** *Stanford, CA · Founders: Harry & Mary Margaret Anderson (family) · Focus: 20th-c. American art, AbEx through Bay Area Figurative · Selected artists: Pollock, de Kooning, Kline, Still, Guston · Pathway: partner with an institution (university) · Status: at Stanford University since 2014 (purpose-built building) · Why it matters: a major collection placed with a university through a purpose-built partnership rather than a standalone family museum.*
- **Editorial:** the university as a home for a collection; a gift with its own building.
- **Commercial:** proves expertise in *university partnerships* — the collector weighing a university gift (Leslie Anderson Conversation attaches here). Pathway: **Partner with an institution**; chapters: Public Life, Giving, Succession.
- **Strain:** collection-level finances are structurally unavailable (a Stanford department, no 990). The record works on artists + story; the deep history omits the finance section without looking incomplete. Also: "university-partnership" hides **two sub-models** (a standalone-shaped gift vs an absorbed collection) — the pathway taxonomy may need a sub-tag.

### 4. Colección Patricia Phelps de Cisneros — MODERATE (governance ok, artist-poor, no financials)
**Public Index Record.** *Caracas, Venezuela / New York · Founder: Patricia Phelps de Cisneros · Focus: Latin American modern & contemporary, geometric-abstraction core (tight thesis) · Pathway: disperse deliberately (permanent gifts to existing institutions) · Recipients: MoMA, Reina Sofía, Blanton (UT Austin), MAMBA, MALI, Bronx Museum · Status: distributed through major gifts (2016, 2018); no founder museum · Why it matters: a wager that embedding Latin American art inside canonical institutions does more lasting cultural work than a single founder building.*
- **Editorial:** dispersal as a deliberate strategy, not a failure; durability without a building.
- **Commercial:** proves expertise in *intentional dispersal + institutional gifts* and endowed research. Pathway: **Disperse deliberately / Give to museums**; chapters: Giving, Public Life, Value.
- **Strain:** no named artists, no financials (non-US, no 990). "Selected recipients" substitutes for "selected artists" — a good sign the schema should allow *recipients* as a field for dispersal cases.

### 5. De la Cruz Collection — MODERATE (artist + auction-rich, governance-poor)
**Public Index Record.** *Miami, FL · Founders: Rosa (d. 2024) & Carlos de la Cruz · Focus: contemporary, depth in Ana Mendieta and Félix González-Torres · Pathway: sell (auction), after a 15-year private museum · Status: museum closed 2024 after the founder's death; collection consigned to auction; building sold to ICA Miami · Key dates: museum opened 2009, founder died Feb 2024, first sale May 2024 · Why it matters: the fastest, cleanest closure in the record — founder died first without warning, the surviving spouse closed and sold within the year, no locked succession, no institutional intermediary.*
- **Editorial:** what happens when there is no plan and the founder dies first; a museum that lasted only as long as its founder.
- **Commercial:** proves expertise in *succession failure and the no-plan default* (the exact risk Nariway sells against). Pathway: **Sell**; chapters: Succession, Sale & Dispersal.
- **Strain:** a LIVING founder (Carlos) is central. Handle via public-by-choice + factual sourcing only (the auction and building sale are public record); no private family circumstances. Good test of the living-collector rule on a sensitive, recent case.

### 6. Corcoran Gallery of Art — THIN (a stub)
**Public Index Record.** *Washington, DC · One of the oldest US private-collection museums (founded 1869) · Pathway: gave to museums (scattered) via court order · Status: dissolved by court order (cy pres) in 2014; 19,493 objects distributed to the National Gallery and 22 DC institutions; school and building to George Washington University · Why it matters: survived its founder for ~126 years, then dissolved on a funding gap — good governance did not prevent institutional death, only a slower kind.*
- **Editorial:** money, not the founder's death, is the long-run killer; 126 years is not forever.
- **Commercial:** proves expertise in *long-run financial durability and dissolution* (the H6/H8 finding). Pathway: **Give to museums**; chapters: Stewardship & Cost, Succession.
- **Strain:** THE hard test — coherence, decision-owner, governance fields are absent in the case file (it's a stub pointing to the dataset). **Verdict: this is an Index Record ONLY, not yet a Collection History.** It proves the two-level model is necessary: a genuinely important case with thin public detail still earns a factual record, without being forced into a deep narrative it can't support. Fill `collection focus` / `selected artists` before any deep history.

### 7. Credit Suisse Art Collection → UBS — MODERATE (some artists, governance-poor)
**Public Index Record.** *Zürich, Switzerland · Origin: corporate (no individual founder) · Focus: broad survey with a Swiss-artist core · Selected artists: Hodler, Vallotton (Credit Suisse); Basquiat, Lichtenstein, Freud (UBS) · Pathway: hybrid (absorbed into the acquirer) · Status: absorbed into the UBS Art Collection following the 2023 UBS–Credit Suisse merger; integration ongoing · Why it matters: the intermediate corporate case between bankruptcy liquidation and voluntary retreat — a distressed-but-not-bankrupt parent whose collection was absorbed wholesale.*
- **Editorial:** what happens to a corporate collection when the company itself disappears.
- **Commercial:** proves expertise in *corporate collections and institutional absorption* — a distinct client type. Pathway: **Partner/merger (hybrid)**; chapters: Ownership, Sale & Dispersal.
- **Strain:** the `decision_owner` vocabulary has no clean value for a corporate/M&A actor (closest: `no-identifiable-person`; operational lead named). Corporate cases stress the person-centric schema — may need a corporate `origin` branch. `founder` fields disappear gracefully.

### 8. The Chinati Foundation — RICH (artist + governance + finance)
**Public Index Record.** *Marfa, TX · Founder: Donald Judd (the artist himself) · Focus: permanent large-scale installation, site + architecture + object as one inseparable work · Selected artists: Judd, Dan Flavin, John Chamberlain, Oldenburg/van Bruggen, Kabakov (~14 artists) · Pathway: built an institution (art park) · Status: operating in Marfa since 1986; continued ~30+ years past the founder's 1994 death · Why it matters: the purest "site is the artwork" thesis, the anti-white-cube — and a founder hard-coding permanence that has held.*
- **Editorial:** when the place IS the collection; an artist designing his own permanence.
- **Commercial:** proves expertise in *artist-founded, site-specific institutions and durable permanence*. Pathway: **Build an institution**; chapters: The Collection, Public Life, Succession.
- **Strain:** none — the fullest record. Anchors H4 (distinctiveness as the product) and H8 (permanence by design).

### 9. Almaty Museum of Arts (ALMA) — THIN-to-MODERATE (governance-intent-rich, finance-poor)
**Public Index Record.** *Almaty, Kazakhstan · Founder: Nurlan Smagulov · Focus: Kazakh/Central Asian contemporary (700+ works) bridged to international blue-chip · Selected artists: Serra, Kiefer, Bill Viola, Kusama · Pathway: built an institution (standalone museum) · Status: opened September 2025; founder-controlled at opening with a publicly stated plan to move toward mixed governance and an endowment · Why it matters: a rare case where a governance transition is announced as a plan AT founding, rather than inferred after the fact.*
- **Editorial:** a new region's first private contemporary museum; planning to give away control on purpose.
- **Commercial:** proves expertise in *governance-transition design and founder-to-institution handoff* (the "beat founder's disease before it starts" move). Pathway: **Build an institution**; chapters: Ownership, Succession.
- **Strain:** LIVING founder + EMERGING (opened 2025, no track record) + no disclosure regime (finance unknown). Status must read "emerging," not an outcome. Tests the living + emerging + thin combination — the record holds on story + intent; no deep history yet.

### 10. Lucas Museum of Narrative Art — EMERGING (living founders)
**Public Index Record.** *Los Angeles, CA · Founders: George Lucas & Mellody Hobson · Focus: "narrative art" — illustration, comic art, film, photography, fine art (40,000+ works) · Selected artists: Norman Rockwell, N.C. Wyeth, Jack Kirby, Frida Kahlo, Jacob Lawrence · Pathway: built an institution (standalone museum) · Status: opening September 22, 2026 · Why it matters: the biggest live test of whether a mega-collection can become a mega-museum without losing the specificity of what the founders actually collected.*
- **Editorial:** inventing a field ("narrative art") rather than collecting a canon; specificity at mega-scale.
- **Commercial:** proves expertise in *mega-collection institutionalization and thesis-driven collecting*. Pathway: **Build an institution**; chapters: The Collection, Value, Succession.
- **Strain:** LIVING founders + EMERGING + a still-unverified endowment. Status "opening 2026," not an outcome; press-sourced figures flagged. A clean, fully public-by-choice living case (they are opening a public museum) — the model living-founder Index entry.

---

## ARCHITECTURE LOCKED + PROTOTYPE PLAN (2026-08-22, Alina)
Enough architecture. Locked: **Axis A** = the 8 lifecycle chapters (The Collection · Value & Significance · Ownership & Structure · Stewardship & Cost · Public Life · Succession & Transition · Giving · Sale & Dispersal); **Axis B** = the 6 reader-facing decision families (Keep it in the family · Build an institution · Partner with an institution · Give to an institution · Disperse deliberately · Sell); **Axis C** = invisible analysis (the coded overlay that powers Findings). Refinements: records are **editorial, not database-like** (consistent identity fields, then whatever makes the collection worth knowing; unknowns disappear); **"Why it matters" is elevated** (the field only Nariway supplies). **Principle: controlled data vocabulary is STABLE; website labels are FLEXIBLE** (store `pathway` codes, render display labels from a lookup, so "Give to museums" → "Give to an institution" is never a recode). **Label change adopted:** "Give to an institution" (museum / university / other cultural institution). **A 4th user to design FOR but not build now: the referral partner who enters by PROBLEM** ("my kids don't want it", "I want it to stay together", "we inherited this and don't know where to begin") — the content model must be able to carry future "Questions collectors face" pages that route problem → pathway/chapter/case/Conversation; this is the likely bridge to the advisory business. Do NOT build the platform; build **4 prototype pages** then critique: (1) moderate Collection Record, (2) rich Collection History [Barnes/Chinati], (3) Pathway page [Partner with an institution], (4) Reference chapter [Succession & Transition]. Inside the existing brand, real content, no new identity, no elaborate interaction.

**Prototype 1 BUILT + REVISED 2026-08-22** → the Collection Record at three evidence levels (Cisneros / Barnes / Corcoran): https://claude.ai/code/artifact/585e590c-0271-43d9-9752-b4cf43cd2fc8 . Real implementation lands in the `nariway-rebuild` website project; this is the visual prototype.

**Record schema/treatment — FINAL after the v1→v3 critique (LOCK for the production brief):**
- The Index Record is **restrained and factual, NOT interpretive.** It answers only: what is this collection, where did it come from, what happened to it. Order: pathway eyebrow → name → founder · location → **Origin** (short, factual account; flexes with evidence) → a quiet **Key facts** strip (Focus · Selected artists/Recipients · Scale if meaningful · Current state) → **timeline** → **Sources + Last reviewed**.
- **The interpretive standfirst is REMOVED (reverses the v2 lock).** The record does not carry a thesis under the title. Moving "Why it matters" to the top was an overcorrection; those lines had a manufactured "not X, but Y" AI cadence and made the page read like content marketing. The record needs no editorial thesis to stand.
- **`origin` is in the schema, but the prose is RESTRAINED reference tone** — no rhetorical contrasts, no moral framing, no lines written to sound quotable, no museum-catalogue voice. Confidence through specificity, not authorial performance.
- Public evidence-richness badges (thin/moderate/rich) are INTERNAL ONLY. Public rigor signals = Sources, Last reviewed, and (when needed) "public information is limited."
- `Current state` (short) replaces `Status`; the longer story lives in the timeline.
- No-image state = first-class intentional variant (never a gray placeholder). Timeline grammar confirmed (variable length).

**THE EDITORIAL GRAMMAR (the big discovery — where interpretation lives, by product level). Keeps Nariway from "constantly announcing profound conclusions," and separates fact from analysis so the reader can trust the records (the antidote to the Private Museum Research objectivity problem):**
| Product | Voice | Interpretation |
|---|---|---|
| **Index Record** | factual, concise, restrained | minimal / none |
| **Collection History** | narrative + **context** | **careful** interpretation that EMERGES from the facts, never a case built to prove a Nariway hypothesis (revised 2026-08-22) |
| **Pathway page** | comparative | what several cases reveal about ONE choice |
| **Finding** | analytical | what the accumulated evidence suggests |
| **Conversation** | first-person | the guest's perspective |
| **Reference chapter** | synthesis | evidence + expert + economics + practical explanation |
- **METHOD RULE: the case supplies evidence; the synthesis happens ABOVE the case.** Cisneros's dispersal is interpreted on the "Disperse deliberately" pathway page; Barnes on findings about donor restrictions/governance; Corcoran on findings about long-term financial durability. The record just supplies the facts.
- **STANDING RULE (still holds, applied at the interpretation levels): public interpretation is a separate writing pass, never a paste of the internal finding.**

**Origin-prose calibration (three tones, discovered across v1→v3).** Too-interpretive/AI ("a chosen legacy, not a failure to keep it whole") and too-dry ("began collecting in the 1970s. Over time the collection developed...") both fail. The target is **factual with enough human detail and specificity that the reader wants to keep going.** The writing formula for Origins: **how it began → what the collection became → what the collector did with it** (not every record supports all three, which is fine). **The current prototype Origin copy is PLACEHOLDER/reference-grade, not the final editorial standard** — each record gets an individual Origin writing pass at publication, based on its evidence. **Confirmed: no "Why it matters" field on the record at all** (the page is calmer and more authoritative without it).

**Prototype 1: STRUCTURALLY SOLVED (2026-08-22).** Move on.

**THE GOVERNING PRINCIPLE (discovered building Prototype 2, applies everywhere): Nariway does not need to sound clever.** The subject is already interesting; authority comes from connecting what others have not, documenting it carefully, and explaining it clearly. That is far harder for AI-generated competitors to imitate than a distinctive voice. Manufactured "not X, but Y" theses, quotable pull-lines, and lesson-announcing section titles ("What X shows") are BANNED across all page types.

**Collection History corrections (from the P2 critique, LOCK):**
- **Write the case FAITHFULLY first; compare cases ONE LEVEL UP.** Comparative moves (e.g. Chinati vs Barnes on preserving intent) belong on Pathway/Finding pages, NOT inside a History. Putting the comparison inside the case turns it into evidence built for a predetermined conclusion, and it is a confirmation-bias trap as the corpus grows.
- A History answers: what happened · why the collector made these choices · how the collection developed · what changed after the founder · what worked · what was hard · where it is now. Interpretation emerges; it does not organize.
- **Deepen the after-the-founder story** (the real Nariway subject and the thing a reader does not already know): who took responsibility, financial condition, governance, crises, estate/foundation conflict, financing, expansion-vs-fidelity, conservation-vs-permanence, how much changed. End with a factual **"[Collection] today"**, not a lesson; a restrained close, no bow.
- **Length: ~1,800–2,500 words** when the evidence warrants (a History is earned by knowing enough to tell the larger life).
- **Claim-level sourcing** (quiet numbered notes/superscripts), not one compressed source line, since journalists/academics/lawyers/clients will check.
- **Image standards differ BY PAGE TYPE:** Record = image optional (no-image is a first-class state); **History = a legitimate image is strongly preferred, and "a licensed image exists" becomes a selection criterion for the 5–6 launch Histories.**
- Cross-link block stays, but **remove "What the cases suggest"** from it (don't make every page deliver a conclusion); reframe as a quiet "Explore the research" (Pathway · Related topics · Related collections · Related chapters).

**Prototype 2 BUILT + REVISED 2026-08-22** → Chinati Foundation Collection History: https://claude.ai/code/artifact/93cea7ab-3c45-4b80-8d3e-36f4c5dba26d . Page-type visual grammar confirmed; rewritten as faithful biography with the deepened after-Judd account, "Chinati today" close, claim-level notes, and an image slot. Specifics flagged verify-to-grade.

Original build note: **Prototype 2 = the Chinati Foundation Collection History** (chosen over Barnes deliberately: Barnes is too easy to turn into courtroom drama; Chinati tests the harder, more representative breadth — the relationship among a collector/artist, the works, a place, an institutional model, and what happens after the founder). Then 3 (Pathway "Partner with an institution" — comparative), then 4 (Reference chapter "Succession & Transition" — synthesis).

## PART 3 — WHAT THE EXERCISE PROVED (the template verdict for the brief)

1. **The two-level model (Index Record vs Collection History) is validated and necessary.** Corcoran and Almaty prove it: important cases with thin public detail earn a factual Index Record without being forced into a deep narrative they can't support. Deep histories are earned by evidence, not importance.
2. **The internal→public vocabulary split is essential and must be enforced in the schema.** `outcome_category` values (`dissolved`, `closed-dispersed`, `pivoted`, `distressed`) must NEVER render publicly. Every public status is a factual sentence ("dissolved by court order in 2014"; "absorbed into the UBS collection"; "opening September 2026"). Store the analytic label internal-only; store a separate `public_status_text` field.
3. **Both axes are real and both must be built.** Pathways (Axis B) are the commercial navigation; chapters (Axis A) are the reference work. Do not collapse them. Every case carries `pathway` (already coded) AND maps to 2–4 chapters.
4. **Fields must disappear gracefully — no "N/A" graveyard.** Broad (no artists), Cisneros (no artists/financials), Corcoran (no coherence/governance), corporate cases (no founder). The schema must render a clean record from whatever subset is known.
5. **Two schema additions the cases forced:**
   - a **`recipients`** field for dispersal/gift cases (Cisneros lists recipients where others list artists);
   - a **corporate `origin` branch** — the person-centric `founder`/`decision_owner` fields need a corporate path (Credit Suisse/UBS has no individual founder; `decision_owner` had no clean value).
6. **`university-partnership` hides two sub-models** (standalone-shaped gift vs absorbed collection) — add a sub-tag before the pathway pages are written.
7. **Living + emerging cases need explicit handling** (Lucas, Almaty, de la Cruz's living spouse): status reads "emerging/opening," never an outcome; grounded only in public-by-choice, documented, non-sensitive facts; `living_collector` and `public_depth` fields gate what renders.
8. **The data-richness reality (plan the launch around it):** of a diverse 10, only ~2 are RICH enough for a top-tier deep history immediately (Chinati, Barnes; Broad if artist-agnostic). That confirms the earlier call — launch with the full shallow index + **5–6** superb deep histories drawn from the RICH set, not 12–15.
