---
type: proposal
title: "Proposal — a new pathway family for shared-campus / collective legacy?"
status: open — awaiting Alina's decision
opened: 2026-08-23
trigger: Art Omi Pavilions (Chatham, NY), filed in [[candidate-universe]] 2026-08-23
decision_owner: Alina
---

# Proposal: does the shared-campus model warrant a NEW pathway family?

**One-line ask:** Art Omi Pavilions doesn't fit any of the six current pathway
families. Should we add a seventh — a **shared-campus / collective-legacy**
family — or is it a variant we can classify inside what exists? This is a
taxonomy change that touches the whole site, so it's presented for your
decision, not made unilaterally.

## What triggered this
The 2026-08-23 Signals surfaced **Art Omi Pavilions**: a 190-acre site in
Chatham, NY where 12–18 collectors and artists each design and control their own
legacy pavilion (with an architect of their choosing) on shared land and
infrastructure. Susan and Michael Hort are among the first collector
participants. Phase One opens June 2027.
Sources: [Art Omi Pavilions](https://artomipavilions.org/) ·
[archpaper](https://www.archpaper.com/2024/07/art-omi-debuts-new-architect-and-artist-designed-pavilions-in-chatham-new-york/).

The structural novelty: it is **neither a single-founder museum nor a
dispersal**. Each participant keeps control of their own structure and curatorial
voice, but shares land, infrastructure, and (presumably) some stewardship — a
*multi-collector* answer to the single-founder-museum model this brief tracks.

## The six families it has to fit into
From `export/nariway-public.json` → `taxonomy.pathwayFamilies`:

| id | label |
|---|---|
| build-institution | Build an institution |
| partner-institution | Partner with an institution |
| give-institution | Give to an institution |
| disperse | Disperse deliberately |
| sell | Sell |
| keep-family | Keep it in the family |

## Why it doesn't cleanly fit any of them
- **build-institution** — closest, but assumes *one* founder building *their*
  institution. Art Omi's whole point is that no single participant builds or
  controls the whole; each builds a part inside a shared frame. Filing it here
  erases the collective/shared-infrastructure fact that is the entire reason it's
  interesting.
- **partner-institution** — a participant does partner with Art Omi (the host
  nonprofit) for land and infrastructure. But "partner" in our taxonomy means a
  collector hands ownership/custody of the *collection* to an institution (gift,
  long-term loan, co-ownership). Here the collector retains their pavilion and
  control; Art Omi is a landlord/steward of the campus, not the recipient of the
  art. A stretch that loses the distinctive feature.
- **give-institution / disperse / sell / keep-family** — none apply: nothing is
  given away, scattered, sold, or kept privately in the family.

So the model sits *between* build and partner, and the feature that makes it
worth studying — **shared land/infrastructure + retained individual control,
across many collectors** — is precisely what every existing family flattens.

## What's genuinely new vs. what we've already seen
The pavilions-in-a-landscape *form* is not new to the universe — Inhotim, Paz's
second museum, Storm King, Dia:Beacon all use it. What's new is the **ownership
and control architecture**: multiple independent legacies co-located under shared
stewardship, each self-governed. That's the axis no current family encodes.

Adjacent-but-different existing cases (so we don't over-claim novelty):
- **Dia Art Foundation** [[dia-art-foundation]] — one foundation stewarding many
  artists' work permanently; but it's a *single* steward's collection, not many
  collectors each controlling their own structure.
- **co-ownership gifts** (Daskalopoulos [[daskalopoulos]]) — shared *ownership of
  works* between institutions; not shared *campus with retained individual
  control*.
- **Powder Mountain / Goodwood** (Signals cycle 1) — single-owner land opened to
  art; not multi-collector.
None of these is the Art Omi structure. It appears to be a category of one *so
far*.

## The cost of a taxonomy change (why this is your call)
Adding a family is not a local edit. Per [[case-template]] and the
[[collection-index-build-brief]], a new `pathwayFamilies` id ripples to:
1. **`export/nariway-public.json` → `taxonomy.pathwayFamilies`** — the source list.
2. **Decision pages** — each family with `hasPublicPage: true` renders a page;
   we'd decide whether this one is public-facing or internal-only (like
   `give-institution`, `disperse`, `sell`, `keep-family`, which are
   `hasPublicPage: false`).
3. **The Collection template's classification layer** — `public_pathway_timeline`
   events reference a `family`; a new family becomes a valid value every case can
   point to, and "a case appears under every family its timeline touches."
4. **The coded header vocabulary** ([[case-template]]) — `pathway`'s controlled
   list has no shared-campus value; the template says a value outside the list
   "is not permitted without amending this template." So a new family likely also
   needs a new coded `pathway` term (e.g. `shared-campus-pavilion`).
5. **The rebuild site** consumes the export, so the list change is what actually
   surfaces publicly — governed by the data boundary (vault authors data; site
   renders it).

## Three options

**Option A — Add a seventh family: `shared-campus` (label e.g. "Share a campus"
or "Collective legacy").**
- *For:* honestly encodes a structure the other six can't; gives the report a
  forward-looking category as more of these appear (the single-founder-museum
  economics are exactly what pushes collectors toward shared infrastructure — this
  may be an emerging pattern, not a one-off); strong distinctiveness/north-star
  fit.
- *Against:* a category of one today; adds a public/decision surface we'd maintain
  on a single provisional, not-yet-open (June 2027) case; risks looking like we
  invented a family to fit one press release.
- *Guardrail if chosen:* set `hasPublicPage: false` until there are ≥2–3 verified
  cases, so it exists in the data model without a thin public page.

**Option B — Keep six families; classify Art Omi as `build-institution` with a
`hybrid`/secondary tag and a modifier note.**
- *For:* no site-wide change; uses the existing `pathway_is_branched` /
  `secondary_pathways` machinery and the `hybrid` coded value the template already
  allows; low maintenance for a single provisional case.
- *Against:* buries the one genuinely new thing; if the pattern grows we
  re-do this later anyway.

**Option C — Hold. Log it as a flagged candidate (done), open a "watch" for a
second instance, and revisit the family question when a 2nd shared-campus case
appears.**
- *For:* most disciplined — taxonomy earns a new family from a pattern, not a
  single case; costs nothing now; the candidate row + this memo preserve the
  reasoning.
- *Against:* if the pattern is real and accelerating, we're slightly behind the
  story.

## My recommendation
**Option C now, pre-committing to Option A on a second verified case.** The
structure is real and unencodable in the current six, but one provisional,
unopened case is thin ground to add a permanent, site-wide public category to.
Holding costs nothing — the candidate row and this memo capture the full
reasoning, so if/when a second shared-campus legacy surfaces (or Art Omi's Phase
One opens in June 2027 with the ownership/stewardship terms documented), promoting
to a new `shared-campus` family is a fast, well-argued move rather than a
speculative one. If you'd rather lead the story than follow it, Option A with the
`hasPublicPage: false` guardrail is the aggressive-but-safe version.

**Whatever you decide, the Art Omi case file stays deferred until then** —
seeding it requires a coded `pathway`/`familyId`, which is this decision.

## If you approve a new family — the mechanical checklist
1. Add the id to `export/nariway-public.json` → `taxonomy.pathwayFamilies`
   (`hasPublicPage` per your call).
2. Add the coded `pathway` value + any `secondary_pathways` term to
   [[case-template]]'s controlled vocabulary (the template forbids out-of-list
   values, so amend it explicitly).
3. Seed `cases/art-omi-pavilions.md` with `familyId` / `pathway` set, verified
   public facts only, sources per the Signals sourcing rule.
4. Confirm the rebuild site's Decision-page and Collection-template rendering
   handle the new family (data boundary: vault change flows to the site via the
   export).

---
*Decision:* ______________  *(Alina)*  ·  *Date:* __________
