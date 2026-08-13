# Vault Hygiene — the librarian sweep (on-call subagent)

Not a standing function (see [[executive-model]]) — a recurring **subagent** Toi runs to keep the vault clean, current, and legible, so noise and stale information never accumulate to slow Alina down. It complements the one-time [[vault-review]] audit by making hygiene a standing loop rather than an occasional cleanup.

**Standing principle (Alina's stated preference): fewer files.** Bias toward consolidation. Before anyone creates a new note, extend an existing home instead; only create a new page when a topic genuinely has no home. Fewer, canonical pages beat many overlapping ones, because every extra file is a place for stale or contradictory content to hide.

## What it watches for
- **Stale information** — dates, statuses, or facts that no longer match reality (e.g. a HOME date left behind, a "pending" that is now decided, a "waiting on X" that already happened).
- **Redundancy** — the same fact stated in two places (violates the single-source-of-truth convention), duplicate notes, superseded drafts.
- **Canonical-copy drift (a known recurring offender)** — a working page (e.g. [[linkedin]], [[substack]], [[website]]) holding its own copy of something that is canonical elsewhere, most often the public profile copy in [[positioning]] or a number in [[claims-register]]. When Alina updates the live copy, the canonical page changes but a working page can keep a stale version, so two pages disagree. Fix: the working page points to the canonical home, it never keeps its own copy. Flag any working page that still carries live copy instead of a pointer.
- **Noise and clutter** — retired practices still lying around (like the old `debriefs/` folder), empty or orphaned files, dead ends.
- **Broken structure** — broken `[[wikilinks]]`, notes missing frontmatter the bases need, files in the wrong folder, decisions left open in `company/decisions/` that are actually settled.
- **A stale map** — a new note that is not yet listed in [[index|INDEX]], or an INDEX line pointing at a moved or renamed file. Keeping the INDEX current is part of the sweep, since it and HOME are the two files Alina navigates from.

## What it does, and the boundary (important)
- **Safe fixes, autonomously:** repair broken wikilinks, move clearly-superseded or retired material to `archive/`, correct obviously-stale dates or statuses, remove unambiguous duplicates. Everything is a git commit Alina can see and revert.
- **Propose, do not force:** anything requiring judgment, merging two notes, deleting content, restructuring a folder, changing meaning, is **flagged for Alina**, not done silently. It writes findings to a short hygiene note and surfaces the important ones in the daily check-in.
- **Never** delete a person's data, a decision record, or primary research without asking. When unsure, flag rather than act.

## How it runs
A periodic **cloud routine** (`Nariway vault hygiene`) scans the whole vault a few times a week, on Anthropic's servers, whether the laptop is on or off, and commits its safe fixes plus a findings list. The daily check-in relays anything needing Alina. This is the always-on cleanup crew she asked for. Run by Toi.
