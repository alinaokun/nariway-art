# Nariway Intelligence — Product & Knowledge Architecture Specification

**Version:** v0.1 (draft for review) · **Date:** 2026-09-08 · **Author:** drafted with Claude, for Alina Okun
**Status:** Precursor to building the `nariway-intelligence` project. **Do not build until this is ratified.** Companion to the Aug-2026 strategy docs and [[strategic-pivot-2026-08]]. Public Collections on nariway.com are unchanged for now.

> **Note on the Cloudflare section:** the source architecture decision anchors this on the "Pulsar" family-office platform (`nariway-ledger`), which is not present on this machine and could not be inspected. Section 15 proposes a Cloudflare architecture at spec altitude; **reconcile it against Pulsar's actual services and auth before building** so the two platforms share one pattern.

---

## 0. Purpose and the central question

Nariway Intelligence is Nariway's **private professional intelligence and matter-support system** for significant private art-collection transitions. It is not a public product, not a research archive for its own sake, and not the marketing site. It is the working cockpit a fiduciary art-disposition specialist uses to run real matters.

Everything in this spec answers one question:

> **What would Nariway need to know, retrieve, compare, and reason through to support a real collection-transition matter — from the first conversation through execution?**

Design test for every feature: *does it help resolve a real matter, make Nariway demonstrably more competent in the room, or compound institutional learning across matters?* If not, it does not belong in v1.

This system is the engine under the practice defined in [[strategic-pivot-2026-08]]: Nariway sells **control, comparability, documentation, exception management, and reconciliation** of a collection's disposition to estate attorneys and fiduciaries — deliberately **not** art judgment and **not** legal advice. Nariway Intelligence is what makes that service deliverable and repeatable.

---

## 1. What it is — and is not

**It is:**
- A private matter-support system: intake → issue-spotting → research → pathway analysis → specialist coordination → documentation → execution → post-matter learning.
- A private knowledge system: a verified corpus of estate/trust/tax/jurisdiction intelligence, collection-transition precedents, saved sources, and Nariway's own analysis, all retrievable and comparable.
- An institutional-memory system: every matter and every research pass makes the next one faster and better.

**It is not:**
- A publishing platform (that is `nariway-rebuild`).
- A place to *run and grow the company* — CRM, market-evidence, finances, GTM (that is **Nariway Ops**, the likely future role of `nariway-art`).
- A source of legal or tax advice. It produces **reference intelligence and issue spotting**, always flagged as such, to be confirmed by licensed professionals. Nariway coordinates and documents; it does not opine.
- A place to store documents inside GitHub. Code lives in Git; documents and data live in private Cloudflare infrastructure (Section 15).

---

## 2. Relationship to the three environments

| Environment | Repo/host | Owns | Explicitly does not own |
|---|---|---|---|
| **Nariway Ops** (future role of `nariway-art`) | private | company strategy, CRM, market-evidence register, finances, GTM, events, operating rhythm | client matters, deep legal/transition intelligence |
| **Nariway Intelligence** (`nariway-intelligence`, new) | private | the knowledge corpus + matter-support system (this spec) | public presentation; company operations |
| **Public site** (`nariway-rebuild`) | private repo → public site | nariway.com: design, SEO, the deliberately-selected publication layer | any private research, ops, or client data |

**Data flow (target):** Intelligence holds the deep corpus. A **deliberately selected publication layer** is promoted *out* of Intelligence to the public site — the reverse of today's "export the whole corpus" default. Ops references Intelligence read-only where a market conversation needs a fact; it never holds matter data.

---

## 3. Users and access (OPEN DECISION — see §19)

**v1 recommendation: single operator (Alina), internal-only, code-gated**, mirroring Pulsar. This is the simplest correct starting point and matches "only accessible with a code."

The capability list in the source doc ("client-matter support," "specialists and adviser coordination") implies *other people's data* flows through the system, but not necessarily *other people's logins*. Recommendation:
- **v1:** Alina only. Clients/specialists are *data* (parties to a matter), not *users*.
- **Later (flagged, not built):** a narrow, per-matter **share layer** — a read-only or contribute-limited view an attorney or specialist can open for one matter — with hard tenant isolation. This is the single biggest driver of auth and data-model complexity, so it is deferred deliberately and designed-for, not built.

---

## 4. Scope and phasing

The source doc lists ~16 capability areas. Building them all at once is the trap. Proposed phasing:

**Phase 1 — The spine (the minimum that supports one real matter):**
1. **Corpus ingest & source capture** — save an article/paper/case/report; auto-extract metadata; store the file; tag jurisdiction/topic.
2. **Retrieval** — search and semantic ("what do we know about X?") across the corpus, always returning sources.
3. **Matter workspace** — create a matter; capture facts, parties, the collection, and the question.
4. **Issue spotting & tracking** — from matter facts, surface the issues to run down; track each to resolution.
5. **Meeting/matter prep** — assemble a briefing for a specific conversation from matter + corpus.

**Phase 2 — Depth:**
6. Transition-pathway analysis (structured keep/divide/lend/donate/sell/found comparison against precedent).
7. Legal/tax/jurisdiction intelligence library (structured, cited, caveated).
8. Collection-level records and precedent comparison (built on the existing case schema).
9. Claims & source verification (the claims-register discipline, systematized).
10. Specialist/adviser directory and coordination.

**Phase 3 — Compounding & reach:**
11. Cross-matter institutional learning (patterns, checklists that improve with each matter).
12. Matter document generation (control/reconciliation deliverables — the billable artifacts).
13. Selective public-publication promotion pipeline to `nariway-rebuild`.
14. (If ratified) the per-matter external share layer.

Everything past Phase 1 is designed-for but sequenced behind a working spine and real matter use.

---

## 5. Application model

- **A single private web application** (the operator cockpit), not a set of Claude Code conversations. Claude Code builds and maintains it; day-to-day work happens *in the app*.
- **Server-rendered app + API** on Cloudflare (Section 15), with an **AI reasoning layer** invoked through server endpoints (never client-side keys).
- **Core objects the UI is organized around:** Matters, Collections/Entities, Sources, Issues, Claims, Jurisdictions/Legal notes, Pathways, Specialists, and Nariway Analyses.
- **Two primary modes:** *Matter mode* (working a live matter) and *Knowledge mode* (building/searching the corpus). Prep and analysis bridge the two.
- **Everything is cited.** No screen shows a synthesized statement without a path back to its source(s) and a confidence/verification tag.

---

## 6. Information architecture

Top-level spaces:
- **Matters** — the operational heart. Each matter: parties, the collection, the question, facts, issues, research, pathway analysis, specialists, documents, timeline, status.
- **Knowledge** — the corpus, browsable by: Topic, Jurisdiction, Source type, Collection/precedent, Claim, and Pathway.
- **Legal & Jurisdiction** — estate/trust/tax intelligence, organized by jurisdiction and issue (Section 9).
- **Precedents** — collection-transition case studies (Section 10), the private/deep counterpart to the public Collections.
- **Specialists** — advisers/experts by discipline and jurisdiction, with matter history.
- **Prep** — generated briefings for meetings and matter milestones.

Cross-cutting: everything is **taggable and linkable** (jurisdiction, topic, pathway, collection, matter), so a source found for one matter is retrievable for the next. This is the [[fewer-files-preference]] principle enforced by schema instead of discipline: one canonical record per thing, referenced everywhere.

---

## 7. Data model (conceptual)

Relational core (Cloudflare D1), documents in object storage (R2), embeddings for semantic search (Vectorize). Conceptual entities:

- **Source** — id, title, author, publisher, date, url, source_type (article/paper/case/report/statute/ruling/press), jurisdiction(s), topic tags, file_ref (R2), captured_at, capture_note, **verification tier** (see §8), rights/reuse status, publishable flag.
- **Claim** — a discrete factual assertion; canonical statement, the source(s) that support it, verification tier, contested-values field, "resolving source needed," and links to any matter/analysis that relies on it. (Directly systematizes today's [[claims-register]].)
- **Collection / Precedent** — the existing [[case-template]] schema, extended: identity, collector, geography, coherence, the **pathway taxonomy** (retain-family, donate-existing-museum-intact/scattered, long-term-loan, found-standalone/house-museum, found-foundation, university-partnership, intentional-dispersal, merger-into-institution, sell, abandoned-plan, hybrid), founder/governance/outcome fields, timeline, sources. Public vs proprietary depth is a field, not a separate store.
- **Jurisdiction / Legal note** — jurisdiction, topic (situs, probate, trust structures, charitable vehicles, capital-gains/estate/gift tax, cross-border movement, export/cultural-property, consignment/UCC, fractional/entity ownership), the rule in plain terms, citations, last_reviewed, and a hard **"reference, not advice"** flag.
- **Matter** — client/fiduciary, the decedent/collector, the collection, the governing instruments, the question, jurisdiction(s), status (intake → analysis → coordination → execution → closed), engagement tier ($5K review / managed / complex), and a privacy/retention class.
- **Issue** — matter_id, issue statement, category, status (open/researching/resolved/escalated-to-specialist), the sources/claims consulted, the resolution and who owns it.
- **Party / Specialist** — role (attorney, fiduciary, heir, appraiser, insurer, art adviser, auction/dealer, tax adviser), jurisdiction, disciplines, contact, matter history, and a **conflict/independence flag** (Nariway is paid only by the estate/fiduciary — Section 13).
- **Analysis** — Nariway's own synthesis: the question, the reasoning, the claims/precedents relied on, confidence, observed-vs-inferred separation, author, date, and matter or general scope.
- **Pathway analysis** — for a matter: the options considered, feasibility, cost/time, tax/legal consequences, precedent comparison, and the recommendation, framed as **Responsibility → Feasibility → Execution** (the resolved operating thesis in [[estate-transition-synthesis]]).

Every record carries: created/updated, author, verification/confidence, source links, and a privacy class.

---

## 8. Research standards

Carry the vault's existing discipline into the schema so it can't be skipped:
- **Verification tiers** (from [[case-template]]): `Provisional` (single secondary/snippet) · `Spot-verified` (corroborated across two, or a direct read of a secondary) · `Primary-verified` (a directly-read primary instrument — statute, ruling, deed, will, 990 Sch. D). A claim's tier is stored and shown.
- **Observed vs inferred** — never let a read harden into a fact (from the market-learning discipline). Analyses separate the two structurally.
- **No fabrication; sources or "unknown."** Blanks are disallowed; "unknown is a finding." Contested facts store *both* candidate values plus the resolving source needed.
- **Claims register as the single source of truth for numbers** — a figure lives once, is cited, and is referenced, never restated divergently. (This session already caught a real cost of *not* doing this — a corrected figure that hadn't propagated.)
- **QA gate before anything is promoted to the public layer** — the independent-verification stamp that guards the public site today (`public_qa_verified`) becomes a formal state transition in the model.

---

## 9. Legal and jurisdiction intelligence

The reference library that lets Nariway spot issues fast and coordinate the right specialists — **not** give advice.

- **Coverage:** estate & probate, trust structures (revocable/irrevocable, dynasty, CRUT/CLAT, purpose trusts), charitable vehicles (private operating foundations, donor-advised funds, fractional/bargain gifts), transfer/estate/gift tax and capital-gains treatment of art, valuation and appraisal standards (IRS Art Advisory Panel, qualified appraisals), cross-border and situs issues, cultural-property/export rules, consignment and title/UCC, entity and fractional ownership.
- **Organized by jurisdiction first** (US federal + states, starting NY/NJ per GTM; then key international situs jurisdictions as matters demand), then by issue.
- **Every note carries citations, `last_reviewed`, and a bright-line disclaimer:** reference intelligence for issue-spotting and coordination; the licensed professional on the matter owns the legal/tax conclusion. This boundary is a feature, not a hedge — it is exactly Nariway's independent, non-advisory position.
- **Freshness:** law changes; notes have review dates and a re-check workflow. Never assert a rule without its citation and review date.

---

## 10. Case methodology (precedents)

The private, deeper counterpart to the public Collections index.
- Built on the existing [[case-template]] coded header + narrative, extended for matter-relevant dimensions (what triggered the transition, what alternatives were weighed, why the chosen form, where coordination broke down, who owned the decision — H7A).
- **Precedent is for comparison, not decoration:** the value is "a matter like this one went this way, for these reasons, with these frictions." Precedents link to the pathways and issues they illuminate.
- Public vs proprietary is a depth/visibility field on the same record — the public site shows a selected, credibility-grade layer; the deep analysis stays private.

---

## 11. Transition analysis

The reasoning core: given a real collection and situation, structure the disposition decision.
- **Pathway comparison** across the taxonomy, each scored on feasibility, cost, time, tax/legal consequence, reversibility, and durability, with precedent support and confidence.
- **Framed as Responsibility → Feasibility → Execution** — the resolved thesis: sale often has a ready execution path while other outcomes must be *created*; strong governance recurs in the collections that survive their founders, but financial resources alone do not appear sufficient (stated at the corpus's evidence boundary — no invented incidence rates; see [[estate-transition-synthesis]]).
- Output is a documented, comparable analysis — the artifact that embodies Nariway's "control and comparability" value — never a single unshown recommendation.

---

## 12. Matter support

The lifecycle, first conversation → execution:
- **Intake:** capture the collection, parties, governing instruments, the question, jurisdiction(s), and the engagement tier.
- **Issue spotting:** generate the issue list from the facts; track each to resolution or specialist escalation.
- **Research:** pull corpus + legal notes + precedents against the issues; everything cited.
- **Coordination:** the right specialists by discipline/jurisdiction, with independence flags; who owns which decision.
- **Documentation:** the control/reconciliation deliverables that are the billable product (inventory status, options analysis, exception log, decision record).
- **Prep:** a generated briefing for any meeting — what's known, open, and to raise.
- **Close & learn:** what happened, what worked, what to reuse — feeding cross-matter learning.

---

## 13. Privacy and security boundaries

- **Private by construction:** code-gated app, no public registration, all data in private Cloudflare infrastructure.
- **Matter data is the most sensitive tier** — real people, estates, and money. Segregated, access-logged, with an explicit **retention/deletion policy** per matter (hard-delete on request is a supported operation, unlike the vault today).
- **No client/matter data is ever used to train models or sent to any service beyond the reasoning endpoint required to answer**, and never to an unrelated third party. The AI reasoning layer receives only what a given task needs.
- **Independence is enforced in data, not just principle:** specialists/parties carry conflict flags; Nariway takes no commission/referral fee — recorded on the matter.
- **Publication is a deliberate, gated promotion** out of the private corpus to the public site — never an automatic export of the corpus. The default is private; publishing is the exception that passes the QA gate.
- **Legacy public exposure to reconcile:** `nariway-art` is currently a *public* GitHub repo. Under the new architecture the deep corpus must not be public; the migration plan (Section 17) must resolve this, and the public site's current build-time fetch from the public vault must be re-pointed to the deliberate publication layer.

---

## 14. AI behavior

The reasoning layer is a disciplined analyst, not an oracle:
- **Always cite.** Every synthesized statement carries its sources and a verification/confidence tag. No source, no claim.
- **Never fabricate; separate observed from inferred; say "unknown."** Contested facts are shown as contested.
- **Reference, not advice.** Legal/tax output is framed for issue-spotting and coordination, with the licensed-professional boundary explicit.
- **No unstated warmth or certainty** — the relationship-label and evidence-grade disciplines from the vault apply to how the system characterizes parties and findings.
- **Retrieval-grounded** — answers are built from the corpus (RAG over Vectorize + D1), not from model memory; when the corpus is silent, it says so rather than inventing.
- **Auditable** — an analysis records what it read and why it concluded, so it can be checked. Prompts and behavior rules live in the repo (versioned), not buried in the app.

---

## 15. Cloudflare architecture (proposed — reconcile with Pulsar)

At spec altitude; validate implementation with the `cloudflare` / `wrangler` / `workers-best-practices` skills at build time.
- **App + API:** Cloudflare Workers (or Pages + Workers) serving the operator cockpit and server-side API. No secrets client-side.
- **Relational data:** **D1** (SQLite) for the structured model in Section 7 (matters, sources, claims, issues, precedents, legal notes, specialists, analyses).
- **Documents & source files:** **R2** for uploaded PDFs, papers, matter documents; D1 holds metadata + R2 refs.
- **Semantic retrieval:** **Vectorize** for embeddings over the corpus and matter text, enabling "what do we know about X?" RAG.
- **Reasoning:** an **AI Gateway**-fronted model call (Workers AI and/or an external model via the gateway) for synthesis, issue-spotting, and prep, invoked only server-side.
- **Auth / code gate:** **Cloudflare Access** or a Workers-based gate for the single operator now; structured so a future per-matter share layer can bolt on without redesign. Match whatever Pulsar uses.
- **Sessions/config/small state:** **KV**. Coordination/stateful workflows (e.g., long ingest or multi-step analysis) via **Workflows/Queues** or a **Durable Object** if warranted.
- **Migrations, schema, seed, prompts, tests:** in the private GitHub repo. **Data is never committed to Git.**

---

## 16. User experience

- **Fast capture, low friction:** saving a source or a matter fact should take seconds — the whole point of a working cockpit vs. re-running Claude Code conversations.
- **Retrieval-first:** a prominent "ask/search the corpus" that always returns cited results; browse by the IA facets when exploring.
- **Matter as the home for real work:** open a matter and everything (facts, issues, research, prep, docs) is one place.
- **Restraint and clarity over decoration** — a professional instrument, not a dashboard for its own sake; consistent with the quiet Nariway/alinaokun visual language.
- **Mobile-usable for capture and prep** (save a source on the go; pull a briefing before a meeting), full workflows on desktop.
- **Trustworthy surface:** confidence tags, source links, and "unknown" states are visible, not hidden — the UI teaches the discipline.

---

## 17. Migration and inventory of `nariway-art` (LATER — not now)

Per the source doc: do not reorganize, delete, or migrate `nariway-art` without an explicit plan. When the model below is ratified, inventory the existing vault into five categories, then migrate deliberately (design around future needs, not today's folders):
1. **Company operations & strategy** → Nariway Ops
2. **Institutional intelligence & research** → Nariway Intelligence corpus
3. **Public / publishable content** → the publication layer feeding `nariway-rebuild`
4. **Application / infrastructure material** → repos (Ops or Intelligence)
5. **Historical / obsolete** → archive

The public Collections pipeline keeps running unchanged until the publication layer is designed and the swap is planned.

---

## 18. Future expansion

- **Per-matter external share layer** (attorney/specialist read or limited-contribute view), with hard isolation.
- **Selective public publication** promoted from Intelligence precedents to nariway.com (credibility/SEO), replacing today's whole-corpus export default.
- **Cross-matter analytics** — patterns and reusable checklists that improve with each matter (Nariway's compounding moat).
- **Team access** if the practice grows beyond a single operator.
- **Deeper legal-intelligence coverage** by jurisdiction as matters demand.

---

## 19. Open decisions to confirm (these shape the build)

1. **Users:** single-operator internal-only for v1 (recommended), with the external share layer deferred? Or is any client/specialist login needed in v1?
2. **Pulsar reconciliation:** what does `nariway-ledger` actually use (D1? R2? Vectorize? Access vs Workers-auth? which model/gateway)? The spec should match it — please point me to that repo or its stack.
3. **v1 scope:** is the Phase-1 spine (capture · retrieve · matter · issues · prep) the right minimum, or is a specific capability (e.g., legal-intelligence library, pathway analysis) a must-have for the first real matter?
4. **Reasoning model & residency:** any requirement on which model does the reasoning / where data may go, given matter sensitivity?
5. **Ops vs Intelligence split:** confirm `nariway-art` becomes **Nariway Ops** (CRM, market-evidence, finances, GTM), and matter/legal/precedent intelligence moves to `nariway-intelligence`.
6. **`nariway-art` public-repo exposure:** agreed that the deep corpus must go private, and the public site re-points to a deliberate publication layer?

---

## 20. Immediate next steps (spec completion — still not building)

1. You review this draft and answer Section 19.
2. I revise into a **ratified v1.0 spec**, including a concrete D1 schema sketch, the Phase-1 build plan, and the Cloudflare service list reconciled with Pulsar.
3. Only then: create the private `nariway-intelligence` repo and begin Phase 1.

*This document is planning only. No `nariway-art` material has been reorganized, migrated, or deleted, and nothing has been built.*
