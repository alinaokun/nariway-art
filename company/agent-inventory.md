# Agent & Automation Registry (authoritative)

*The single source of truth for every automated process touching Nariway: cloud routines, GitHub Actions, local scheduled tasks, and pipelines. Created 2026-08-27 during the zero-based operating reset ([[strategic-pivot-2026-08]]). Supersedes the automation lists in [[it]] and [[executive-model]], which were stale and disagreed with each other.*

## Governing rule (permanent)

> **No automated routine may exist unless it is documented in this registry.** If a routine is running and not listed here, that is a defect: either add it with full justification or disable it. Every new routine is added here at creation, with its business justification, before it is enabled.

## Operating principle (from the 2026-08-27 reset)

> **Automation follows proven work. It does not precede it.** Nariway defaults to OFF. A recurring or event-driven process is created only after a real business activity has demonstrated, through actual work done by hand at least a few times, that the process is worth automating. The technology should make Nariway extraordinarily capable when work exists, not manufacture work when nothing needs doing.

---

## A. Cloud routines (Anthropic CCR, laptop-independent)

All run model `claude-sonnet-5`, environment `env_01218VC3YNVJmMDtm4pvhGJk`, with a git checkout of `github.com/alinaokun/nariway-art`, and carry two MCP connectors (Google Drive, Claude Code Remote). Push to `main` unless noted.

### 1. dataset-research ("Cloud research")
- **ID:** `trig_01E3pZ2fYZCu9hhjuWnKdRDt`
- **State:** DISABLED 2026-08-27 (was enabled)
- **Trigger / cadence:** cron `0 9,21 * * *` — twice daily (9a/9p UTC)
- **Purpose:** grew the case dataset to primary-source depth, advanced the ecosystem research, kept the living manuscript and the evidence base current ("the moat")
- **Reads:** `cases/`, `research/`, `marketing/what-becomes-of-great-art-collections.md`
- **Writes:** `cases/`, `research/market-intelligence.md`, `research/claims-register.md`, `research/what-we-now-believe.md`, the manuscript, **`export/nariway-public.json`**
- **Side effects:** git push; runs `scripts/export_public.py` → the export change **trips `deploy-site` → live-site deploy**; WebSearch/WebFetch
- **Dependents:** the live-site Collections data was refreshed by this routine
- **Last successful run:** 2026-08-27 ~21:08 UTC
- **Original justification:** a proprietary research moat was the product (research/advisory model)
- **Retired because:** Collections is now a secondary asset, not the moat. Cases added intentionally, by hand, when useful. No recurring production.
- **Replacement:** none

### 2. signals ("Nariway Signals daily")
- **ID:** `trig_01LocFBpJweadpmXK5J5Wy3Y`
- **State:** DISABLED 2026-08-27 (was enabled)
- **Trigger / cadence:** cron `0 11 * * *` — daily ~7a ET
- **Purpose:** daily editorial art-world morning brief, emailed
- **Reads:** `research/nariway-signals.md`, `crm/`, `marketing/`
- **Writes:** `research/nariway-signals.md`, **`.mail/outbox/signals.json`**
- **Side effects:** **emails Alina** (via `email-sender` Action → Resend); WebSearch
- **Dependents:** email pipeline
- **Last successful run:** 2026-08-27 11:21 UTC
- **Original justification:** stay current on the collection-futures world (research model)
- **Retired because:** a daily art-world brief is useful information, not a necessary operation, and does not bring a client or advance a matter
- **Replacement:** none yet. A tightly scoped weekly "Professional Watch" (T&E, fiduciary, art-estate, competitors, NAEPC) may be reintroduced later, only if active client-getting work shows it helps.

### 3. weekly-advisor + trigger-scan
- **ID:** `trig_01JgBkpKKHirinAdDrKmkxZk`
- **State:** DISABLED 2026-08-27 (was enabled)
- **Trigger / cadence:** cron `30 11 * * *` — daily silent scan + Monday email
- **Purpose:** silent daily trigger alerts + a Monday advisor email; maintained the scoreboard
- **Reads:** HOME, `company/weekly-brief.md`, `company/scoreboard.md`, `crm/partners/`, `company/decisions/`, `research/what-we-now-believe.md`, etc.
- **Writes:** `company/weekly-brief.md`, `company/scoreboard.md`, `HOME.md` (Mon/trigger), **`.mail/outbox/checkin.json`**
- **Side effects:** emails Alina on Mondays and trigger days
- **Last successful run:** 2026-08-27 11:43 UTC
- **Original justification:** an outside advisor voice + accountability loop for the solo founder
- **Retired because:** the weekly founder review is a 20-minute document Alina does herself, not an autonomous cloud routine
- **Replacement:** a manual `Founder Review` document (Phase 2), not automated

### 4. HOME daily refresh
- **ID:** `trig_01MAW5468LcAExrAGQ2MCP5Y`
- **State:** DISABLED 2026-08-27 (was enabled)
- **Trigger / cadence:** cron `30 10 * * *` — daily ~6:30a ET
- **Purpose:** kept `HOME.md` date + "your move" current on silent days
- **Reads:** `HOME.md`, `company/weekly-brief.md`, `company/scoreboard.md`
- **Writes:** `HOME.md` only. **No email.**
- **Dependents:** reads the advisor's `weekly-brief.md`
- **Last successful run:** 2026-08-27 10:37 UTC
- **Original justification:** keep the dashboard fresh under the old daily-check-in model
- **Retired because:** HOME as a daily auto-refreshed dashboard belongs to the old model; the founder review replaces it
- **Replacement:** none

### 5. Artobiography weekly docket
- **ID:** `trig_01TAVXaSwci5XMzoBhtxZQ9g`
- **State:** DISABLED 2026-08-27 (was enabled)
- **Trigger / cadence:** cron `0 11 * * 4` — Thursdays
- **Purpose:** weekly 12-item editorial research menu for the Artobiography newsletter, emailed
- **Reads:** `artobiography/`, `research/nariway-signals.md`, `cases/`
- **Writes:** `artobiography/dockets/<date>.md`, **`.mail/outbox/docket.json`**
- **Side effects:** emails Alina on Thursdays; WebSearch
- **Last successful run:** 2026-08-27 11:29 UTC
- **Original justification:** feed the Artobiography publication (audience/reach model)
- **Retired because:** Artobiography is removed from Nariway operations. The property is preserved separately and carries no recurring Nariway resources.
- **Replacement:** none

### 6. PR #1 check-in (runaway)
- **ID:** `trig_01TtUhD2Zm55UwjEz4ozWcy6` (plus ~20 hourly run-once siblings, already fired/disabled)
- **State:** DISABLED 2026-08-27 (was enabled; was re-arming itself hourly)
- **Trigger / cadence:** self-re-arming hourly one-shots
- **Purpose:** babysat PR #1 on `nariway-rebuild` (legal-review branch)
- **Writes:** the nariway-rebuild PR
- **Retired because:** runaway loop; the repo it watched is being replaced by the new build
- **Replacement:** none

### 7–12. PENDING ID RETRIEVAL (to be disabled once IDs are supplied)

These six run and commit to the vault daily/near-daily but their trigger IDs are not recorded, and the routine-list API returns only the most recent 20 entries (all the now-dead PR loop) with no working pagination. IDs must be read from **claude.ai/code/routines**. All are slated to DISABLE in the same pass.

| # | Routine | Cadence (from git) | Writes | Emails? | Last run (git) |
|---|---|---|---|---|---|
| 7 | **cfo-steward** | daily ~noon ET | `finance/cfo-brief.md`, ledgers | no | 2026-08-27 16:04 |
| 8 | **cmo-steward** | daily ~11a ET | CMO brief / `marketing/` | no | 2026-08-27 15:08 |
| 9 | **quality-assurance** ("QA audit") | daily ~4p ET | `company/qa-report.md` | no | 2026-08-27 20:13 |
| 10 | **network-research** | ~Mon/Thu | `crm/`, `marketing/events/` | no | 2026-08-27 13:29 |
| 11 | **site-health** | ~Mon/Thu | `company/site-health.md` | no | 2026-08-27 14:12 |
| 12 | **vault-hygiene** | M/W/F ~4a ET | `INDEX.md`, `company/hygiene-report.md`, fixes | no | 2026-08-26 08:16 |

**Verdicts (all):** retire the recurring schedule. QA → event-gated checklists (pre-publish, pre-client-issue, pre-Collections-publish). CFO → a monthly checklist Alina runs. Network research → event-driven prep before a specific meeting or event. Site-health → paused until the new site launches. Vault-hygiene → manual/occasional. No replacement routines created until proven necessary.

---

## B. Infrastructure (kept)

### email-sender (`.github/workflows/nariway-daily-email.yml`)
- **State:** KEPT, now DORMANT (nothing writes to `.mail/outbox/` while the emailing routines are off)
- **Trigger:** GitHub Action on push to `.mail/outbox/**`
- **Purpose:** holds the Resend key (`RESEND_API_KEY` secret) and sends queued email jobs
- **Justification:** the email pipeline itself is sound; if a real business email workflow returns (e.g. a scoped weekly watch), it uses this. Harmless while dormant.

### deploy-site (`.github/workflows/deploy-site.yml`)
- **State:** KEPT
- **Trigger:** GitHub Action on push changing `export/nariway-public.json`
- **Purpose:** POSTs the Cloudflare deploy hook (`SITE_DEPLOY_HOOK` secret) so the live site tracks the export
- **Note:** now fires only on a deliberate export change (dataset-research no longer auto-regenerates it)

### vault backup
- **State:** KEPT
- **Trigger:** Obsidian Git plugin, local laptop, near-real-time auto-commit/push
- **Purpose:** offsite backup of the vault to GitHub
- **Note:** backs up `nariway-art` only. `nariway-rebuild` has substantial uncommitted work that this does NOT cover.

---

## C. Retired local scheduled tasks (already off)

- **nariway-signals-daily** — local scheduled task, DISABLED 2026-08-14 (superseded by the cloud Signals routine, now also off)
- **nariway-daily-checkin** — local scheduled task, DISABLED 2026-08-14 (superseded, now retired)

---

## Reset log

- **2026-08-27** — Zero-based operating reset begun. Killed the runaway PR #1 loop. Disabled cloud routines 1–5 (dataset-research, signals, weekly-advisor, HOME-refresh, Artobiography docket). Routines 7–12 pending ID retrieval, then disable. Target end-state: no autonomous business activity, only backup + the two dormant/on-change Actions. Automation re-introduced only when real work proves a specific process worth it.
