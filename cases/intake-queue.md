# Collection intake queue

*How Alina adds collections she finds herself (Instagram, travel, reading, word of mouth) without going through the research agent, with a quality gate so weak or off-territory entries never dilute Nariway. This file is both the instructions and the list. Add liberally to **Pending**; the gate decides what becomes a case. See the export contract in [[collection-index-build-brief]] and the Signals filter in [[nariway-signals]].*

## The one idea that removes the worry: adding ≠ publishing
There are two tiers, and they are separated by a gate:
- **Tier 1 — tracked (internal).** A name in this queue or a row in [[candidate-universe]]. Costs nothing to add, invisible to the public.
- **Tier 2 — published (public).** A `cases/*.md` file that clears the export gate (`public_page_eligible: true` AND `public_verified: true`) and appears on the live Collection Index.

Only Tier 2 affects Nariway's perceived quality, and the gate is automatic — an entry cannot reach the site until its public facts are verified and it is judged worth showing. **So you can be generous at intake and strict at publish.** A dubious Instagram find can be logged, held, or rejected without ever touching the public product.

## How you add one (fast, from anywhere)
Drop a line under **Pending** with whatever you have. Thirty seconds while scrolling is enough:
`- Name — @ig_handle or url — one line on why it caught your eye`
Obsidian mobile or the GitHub app both work, so this can happen on your phone. You do not research it; you just capture it. Processing (below) does the vetting.

## How it gets processed (you stay in the loop)
Paste a batch of Pending names into a Claude Code session and ask to "vet the intake queue." For each, the open web (not Instagram) is searched to confirm it is real and relevant, the gate below is applied, and a verdict is proposed with its reason. You approve. To start, keep this interactive rather than automated, so you see the reasoning on the borderline calls, which are exactly the ones you flagged. Once the gate proves out, it can become a routine.

**Instagram is a discovery surface, not a verification surface.** IG accounts are found there; legitimacy is confirmed on the open web (an official site, foundation registration, press, a real physical space). A collection that exists *only* as an Instagram account with no other footprint fails the evidence gate by definition — that absence is itself the signal.

## The quality gate (four tests, then a verdict)
A candidate must clear all four to become a published case. Any test it fails routes it to Hold or Reject.

1. **Real.** Independent public evidence that it exists as a collection or collector-founded institution — an official site, a foundation record, press coverage, a physical space. Not just a well-photographed feed.
2. **In territory.** It is a *significant private art collection or collector-founded institution whose future and public life is the story.* NOT a commercial gallery, a dealer, an art fair, an artist's own studio account, a fully government/public museum, or a personal art-appreciation account. (Nariway studies what becomes of collections, not the market that trades art.)
3. **Distinctive enough to belong.** It clears the Signals bar: a living founder + a distinctive or overlooked collection + a real public act, OR a genuinely novel form (non-building, shared-campus, archive, hospitality, and so on). Down-weight generic blue-chip vanity spaces and thin, aspirational, or purely promotional accounts. The test from Conversations applies: if we have to talk ourselves into why it belongs, it does not.
4. **Documentable.** There is enough verifiable public information to build at least a useful record. If the only source is the IG feed, it is not yet documentable.

### Verdicts
- **Add** — clears all four. Create `cases/<slug>.md`, populate the `public_*` fields that public sources verify, and set `public_verified: true` only where the facts confirm. If real and in-territory but thin, add the case with `public_verified: false` so it stays internal until verified.
- **Hold** — genuinely interesting but fails test 1 or 4 today (not enough evidence yet), or is borderline on 3. Log it in [[candidate-universe]] with a one-line note on what would move it to Add. Not published.
- **Reject** — fails test 2 (out of territory) or is clearly not legitimate or would dilute the corpus. Record it in the **Rejected** log below with a one-line reason, so we do not re-litigate it later.

---

## Pending (awaiting vetting)
*Add candidates here. Name — handle/url — why it caught your eye.*

- 

## Vetted — Added
*(date · name · slug · verified? · one line)*

## Vetted — Held
*(date · name · what would move it to Add)*

## Rejected
*(date · name · one-line reason — so it is not reconsidered)*
