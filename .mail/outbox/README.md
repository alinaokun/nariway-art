# .mail/outbox

Email jobs queued by the Nariway cloud agents, sent by the GitHub Action in
`.github/workflows/nariway-daily-email.yml`.

Each `*.json` file is one email: `{ "from": ..., "to": [...], "subject": ..., "html": ... }`.
The daily check-in writes `checkin.json`; Signals writes `signals.json`. The agents
overwrite these each run; the Action sends whatever changed in the triggering push.
The Resend key lives only as a GitHub Actions secret (`RESEND_API_KEY`), never in this repo.
