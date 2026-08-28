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
- **State:** ENABLED (disabled then RE-ENABLED 2026-08-27 at Alina's direction — she wants Collections research to continue, with the accuracy checks)
- **Trigger / cadence:** cron `0 9,21 * * *` — twice daily (9a/9p UTC)
- **Purpose:** grew the case dataset to primary-source depth, advanced the ecosystem research, kept the living manuscript and the evidence base current ("the moat")
- **Reads:** `cases/`, `research/`, `marketing/what-becomes-of-great-art-collections.md`
- **Writes:** `cases/`, `research/market-intelligence.md`, `research/claims-register.md`, `research/what-we-now-believe.md`, the manuscript, **`export/nariway-public.json`**
- **Side effects:** git push; runs `scripts/export_public.py` → the export change **trips `deploy-site` → live-site deploy**; WebSearch/WebFetch
- **Dependents:** the live-site Collections data was refreshed by this routine
- **Last successful run:** 2026-08-27 ~21:08 UTC
- **Business justification (current):** Alina values the Collections library and wants it built out with the established quality checks. KEPT ON. Its old-model extras (the flagship "report/manuscript" and the H1–H8 evidence-base framing) can be trimmed to pure Collections + accuracy later if she wants; behavior unchanged for now.
- **Replacement:** none (kept)

### 2. signals ("Nariway Signals daily")
- **ID:** `trig_01LocFBpJweadpmXK5J5Wy3Y`
- **State:** ENABLED (disabled then RE-ENABLED 2026-08-27 at Alina's direction — she likes the daily brief)
- **Repoint 2026-08-27:** added a fifth "Law & Estates" beat (estate-attorney + art legal/tax news) via `research/nariway-signals.md`; the art-collections coverage she likes is unchanged.
- **Trigger / cadence:** cron `0 11 * * *` — daily ~7a ET
- **Purpose:** daily editorial art-world morning brief, emailed
- **Reads:** `research/nariway-signals.md`, `crm/`, `marketing/`
- **Writes:** `research/nariway-signals.md`, **`.mail/outbox/signals.json`**
- **Side effects:** **emails Alina** (via `email-sender` Action → Resend); WebSearch
- **Dependents:** email pipeline
- **Last successful run:** 2026-08-27 11:21 UTC
- **Business justification (current):** Alina reads it daily and values knowing what is happening with art collections worldwide. KEPT ON, now also carrying estate-attorney/art legal news for the new audience.
- **Replacement:** none (kept)

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
- **State:** ENABLED (disabled then RE-ENABLED + REPOINTED 2026-08-27 at Alina's direction — she wants HOME kept current, but with only the relevant information)
- **Trigger / cadence:** cron `30 10 * * *` — daily ~6:30a ET
- **Purpose (repointed):** keep `HOME.md` lean and current for the new business — refresh the date, the upcoming events (EPC meetings in Bergen/Westchester/NYC/Palm Beach, previews, conferences), and the open follow-ups. Leaves the human-written "This week" section alone. Explicitly instructed never to reintroduce old-model content.
- **Reads:** `HOME.md`, `marketing/events/events-radar.md`, `marketing/to-see.md`, `crm/partners/`
- **Writes:** `HOME.md` only. **No email.**
- **Business justification (current):** a lean daily cockpit Alina reads, kept current from live event and CRM data.
- **Replacement:** none (kept, repointed)

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

**Verdicts (updated 2026-08-27 per Alina):**
- **quality-assurance — KEEP.** Alina wants the established accuracy checks on the Collections research to continue. Left running.
- **network-research — KEEP, repointed.** Now prioritizes Estate Planning Council events in Bergen County NJ, Westchester, NYC, and Palm Beach, plus other worthwhile conferences, via `marketing/events/events-radar.md` (updated 2026-08-27). Still running.
- **cfo-steward — OFF (disabled 2026-08-28).** Self-disabled via `update_trigger` on its own scheduled run, same mechanism cmo-steward used the same day. `trig_014KCjwMrTLo85e1sKudTUof` no longer fires. This was the last cfo-steward run; see its final entry in `finance/cfo-brief.md`.
- **cmo-steward — OFF (disabled 2026-08-28).** Self-disabled via `update_trigger` on its own scheduled run, once it was confirmed that only a routine's own bound session can flip its `enabled` flag. `trig_01G6v8M8PYcokUiXRtxfb1TJ` no longer fires. This was the last cmo-steward run; see its final entry in `marketing/cmo-brief.md`.
- **site-health — KEEP (Alina's decision 2026-08-27).** Left running.
- **vault-hygiene — KEEP (Alina's decision 2026-08-27).** Left running.

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

- **2026-08-27 (morning)** — Zero-based operating reset begun. Killed the runaway PR #1 loop. Disabled cloud routines 1–5 (dataset-research, signals, weekly-advisor, HOME-refresh, Artobiography docket).
- **2026-08-27 (correction, Alina's direction)** — Alina had not read the aggressive "default OFF" directive before it was posted and disagrees with parts of it. RE-ENABLED **signals** (now also carrying a Law & Estates beat) and **dataset-research** (Collections research continues with QA). Confirmed **quality-assurance** stays on (accuracy checks) and **network-research** stays on, repointed to Estate Planning Council events in Bergen County NJ / Westchester / NYC / Palm Beach plus other worthwhile conferences. Still disabled: PR loop, weekly-advisor, HOME-refresh, Artobiography docket. Still running pending Alina's call: cfo-steward, cmo-steward, site-health, vault-hygiene.
- **2026-08-27 (routine decisions)** — Alina: turn off **cfo-steward** and **cmo-steward**; keep **site-health** and **vault-hygiene**; bring back **HOME-refresh** but with only the relevant information. HOME.md rewritten lean (old-model clutter removed) and HOME-refresh RE-ENABLED + REPOINTED to maintain only the date, upcoming events, and open follow-ups. cfo-steward and cmo-steward still awaiting their trigger IDs to disable (browser unavailable).
- **2026-08-28** — cmo-steward self-disabled on its own scheduled run (see above); this was its last run, no more old-model marketing entries land on autopilot. cfo-steward self-disabled the same day on its own scheduled run; no more old-model CFO entries land on autopilot either. Both pending disables from the 2026-08-27 reset are now complete.
