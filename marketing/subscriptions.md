# Subscriptions — triage of the newsletters Alina pays to read

A capability run by [[nariway-signals|Signals]] (and Toi on demand). Alina subscribes to dense, comprehensive newsletters that are excellent but overwhelming. This function reads an issue she forwards or points to, applies the Nariway filter below, and returns a one-screen brief so nothing relevant is missed and nothing irrelevant takes her time. Relevant events land in [[events-radar|events.base]], relevant people in the [[prospects]] or [[partners]] CRM.

## Why it works this way
There is no live connection to Alina's inbox, and these are paywalled, so an agent cannot auto-read them on a schedule. It does not need to. The cadence is monthly, so the flow is simple, she forwards or pastes the issue, or opens it in her logged-in browser and I read it there. Five minutes of her attention a month.

## The subscriptions
- **What's Up in NY This Month?** (Substack, paid). Comprehensive monthly guide to New York culture and events. Excellent but firehose-scale, hence this filter.
- *(add others here as they come up)*

## The Nariway filter (what counts as relevant)
Keep only what serves one of Nariway's real jobs. Everything else is discarded.

**Attend or act on**
- Exhibitions, openings, galas, panels, and talks where the people Nariway needs actually gather, especially the two channels the network is thin in ([[warm-network]]), **trusts and estates attorneys** and **museum directors, curators, and development heads**, plus collectors, family offices, and art advisors.
- Talks or lectures Alina could attend or eventually give that build her authority on the future of private collections.
- Major art-market moments in the calendar, the New York auction weeks, art fairs (Armory, Frieze New York, TEFAF New York, Independent), and significant museum openings.

**Radar (know it, file it, no action needed)**
- Any exhibition or story about a significant private collection, a collector-founded museum or foundation, a major gift or bequest, a deaccession, or a collection entering public life. These are editorial fodder for [[format-v0.1|Artobiography]] and case leads.
- Named people who match a prospect, partner, or warm-network target.
- Institutions or programs worth tracking over time.

**Skip (collapse to nothing)**
- Restaurants, bars, nightlife, food, shopping, tourism, family and kids, most theater, music, film, and dance unless it is philanthropy-, collection-, or collector-adjacent.

## What Alina gets back
One screen, three buckets.
1. **Act on** — a short list, each with date, place, and cost, ready to drop into events.base.
2. **Radar** — one line each, filed to the right register with a link.
3. **Skip** — a single line confirming the rest was scanned and set aside, so she can trust nothing was lost.

No emojis, clickable links, dates and costs concrete. Governed by the same sourcing discipline as [[nariway-signals]].

## How to hand off an issue, or any email
Two ways, same result.
- **Forward and forget (the standing setup):** forward any email to `alinaokun+claude@gmail.com`, or apply the Gmail label "Claude." A Gmail filter labels it, and each morning a local script (`C:\Users\alina\.nariway\gmail_fetch.py`, run as the first step of the daily Signals task) pulls everything labeled "Claude" via IMAP into `OneDrive\Documents\0 - Nariway\Inbox for Claude`. The run then reads each one, decides what needs action, reports it in the daily email, files anything relevant, and moves the file to Processed. This is the default path for anything that can wait until morning.
- **Right now:** forward or paste the email into a chat, or open it in the logged-in browser and say the word. The brief comes back the same session. Use this for anything urgent.

There is no live inbox connector here, so nothing reads Alina's mailbox continuously. The IMAP pull uses an app password she stores locally at `C:\Users\alina\.nariway\gmail_imap.txt` (never in chat, never in git), the same pattern as the Resend key. Only emails she labels "Claude" are ever read.
