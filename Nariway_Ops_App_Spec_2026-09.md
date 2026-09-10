# Nariway Ops — v1 App Spec (the private operations cockpit)

**Version:** v0.1 draft · **Date:** 2026-09-10 · For the new private project `nariway-ops`.
**Status:** scoped small on purpose. Companion to [[strategic-pivot-2026-08]] and the three-environment architecture. **Built like Pulsar Family Office** (private, code-gated, non-indexable), on `ops.nariway.com`.

> **The whole point of v1 is to be small.** It is a clean surface over what already exists in the vault, built to make Alina *act* on the outward work, not a system to maintain. If a feature does not help her see a decision or take an external action, it is not in v1. Timebox it to a Pulsar-weekend.

*(Note: like the Intelligence spec, this is a private business document and `nariway-art` is currently a public repo, so it is left uncommitted. Seed the new `nariway-ops` project with it, or say the word to commit.)*

---

## 0. Purpose
A private cockpit that answers, at a glance: *what is my situation, and what should I do next to move Nariway forward?* It replaces reading messy Obsidian markdown with an intuitive, cohesive view of operations decisions and status. **Success = it causes an outward action** (a follow-up, a booking, a register entry) that Alina would otherwise have missed. It is a place to act, not a place to admire.

## 1. What it is / is not
- **Is:** the operations layer — *run the company*. Movement, people, market-evidence, the events pipeline, the offer, open decisions, the weekly brief.
- **Is not:** matter or client data, or legal/tax/transition knowledge (that is `nariway-intelligence`). Not public content (that is `nariway-rebuild`). Not a full CRM, analytics suite, or multi-user tool.

## 2. Architecture (the Pulsar pattern)
- **New private Claude Code project `nariway-ops`**, private GitHub repo (code only).
- **Cloudflare-hosted, code-gated, non-indexable, on `ops.nariway.com`.** Match Pulsar's exact auth (Cloudflare Access or the same gate Pulsar uses) so there is one pattern across your private apps.
- **Data on Cloudflare** (D1 for structured state the app writes; KV for config/session; R2 if a document ever needs storing). GitHub holds code, not data.

## 3. Data source — read the vault, do not replace it (yet)
v1 consumes a **curated Ops export** from `nariway-art`, the same non-destructive pattern the public site uses: a small script emits `nariway-ops.json` **grouped by the departments in Section 4**, so the app's structure — how you think about the company — is what you see, not the vault's file layout. The vault stays the source of truth; the `nariway-art → Ops` migration comes later, **not in v1** (per the three-environment rule: do not restructure the vault now). The department-to-source-file mapping is in Section 4.

## 4. Information architecture — organized by department, not by file
**The core design principle, and the whole reason to build this:** you should always know which *department* something lives in without searching. The structure mirrors how you think about the company (a corporate intranet), not how the vault's files happen to be arranged. **Search is the safety net, not the primary way to find things** — the win is that you rarely need it.

**Top-level navigation = Nariway's functions.** Each is a clean page surfacing its key items; every item has one obvious home. The source files each department reads from are noted in brackets.

1. **Home / Today** — the action dashboard: the 3 highest-value external actions this week, follow-ups due, the next room, and the **market-evidence register count** front and center (the leading indicator, currently zero).
2. **Strategy** — positioning and the pivot, the thesis, the four-offer model, strategic decisions, and the market intelligence that informs them. [[strategic-pivot-2026-08]], [[positioning]], [[market-intelligence]]
3. **Business Development & Events** — the outward engine and the rooms in one place: the movement log + working list, the market-evidence register + discovery questions, the network and per-person files, the Weekly Operator Brief, and the events pipeline (the November campaign, registered rooms, pre-event briefs). [[market-entry-sept-2026]], [[market-learning]], [[warm-network]], `crm/partners/`, [[events-radar]]
4. **Marketing & Content** — the offer one-pager, the sample matter map, Signals, LinkedIn, the Conversations/Artobiography work, and a link out to the public site. [[offer-collection-transition-assessment]], [[sample-matter-map]], `marketing/`
5. **Finance & Legal** — the revenue model and scenarios, the pricing ladder, capital, and entity/tax (Pulsar Innovation LLC), plus trademark, engagement letters, conflicts, and E&O. Keep both boundaries visible: not a CPA and not a lawyer, route to the professionals. `finance/`, `company/legal.md`
6. **Operations** — the operating rhythm and cadence, the open-decisions log, the routines (Signals, scheduled tasks), and the status of the three apps, with the link across to **Nariway Intelligence** (whose matters and corpus live there, not here). `company/`

**Global search** sits above the departments: one box, over every item's title and body, so anything is one query away when the structure is not enough.

## 5. Interactions (light)
- **Read-first.** v1 is mostly a clean read over the export, organized by department.
- **Global search** across all items (title + body) — the safety net when the department structure is not enough.
- **Quick-capture (v1.1):** add a movement line, a register note, or a decision from the app in seconds, written to the Cloudflare store (synced back to the vault later if wanted).
- Nothing heavier: no automation, no email, no multi-user.

## 6. What v1 deliberately leaves out (guardrails against scope creep)
- No matter/client data (that is Intelligence).
- No accounting or finances beyond a simple plan/decisions view.
- No analytics or charts for their own sake.
- No public/marketing content.
- No automation beyond rendering the operator brief.
- No multi-user or roles — single operator, like Pulsar.

## 7. The discipline / success test
- **Timebox v1 to a Pulsar-weekend.** If it is taking weeks, it has become the trap (building instead of selling).
- **Success:** within its first two weeks it causes at least one outward action Alina would otherwise have missed.
- **Failure mode to avoid:** polishing the cockpit instead of securing the first paid assessment. The cockpit exists to *push* the commercial work.

## 8. Build sequence
- **v1:** read-only cockpit over the Ops export (Today, Register, Events, People, Offer, Decisions, Brief), Cloudflare + code gate.
- **v1.1:** quick-capture write-back.
- **Later:** migrate the vault's Ops content into the app's own store; richer decision and finance views; whatever repeated use proves it needs, not before.

## 9. Open decisions to confirm
1. **Auth:** match Pulsar's exact gate (Cloudflare Access vs. a Workers code gate)?
2. **Export vs. live fetch:** v1 reads a committed `nariway-ops.json` (simplest), or fetches the vault live like the public site's raw-URL pattern? Recommend the export pattern.
3. **Source of truth:** the vault stays canonical through v1 (recommended), migration deferred?
4. **Subdomain:** `ops.nariway.com` — **confirmed (2026-09-10).**
5. **Departments:** the six in Section 4 (confirmed 2026-09-10: BizDev + Events merged; Finance + Legal merged; Knowledge dropped). Any further renaming or splitting before build?

---

*This is planning only. Nothing built, and no `nariway-art` content reorganized or migrated.*
