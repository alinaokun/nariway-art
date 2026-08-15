# Decision — how to send the daily Signals digest

[[it|IT]] recommendation, 2026-08-12. Status, decided. Resend has been live for the daily digest since 2026-08-14.

## The job
Send one email a day, the Signals digest, to alina@nariway.com. About thirty emails a month, to your own inbox. That is the whole requirement.

## Your stack
Google Workspace mailbox, so receiving is already done. Cloudflare DNS. A Resend account you already have. A daily local scheduled task that produces the digest.

## The options, plainly

| Option | What it takes | Pros | Cons |
|---|---|---|---|
| **Resend** (you have it) | The task calls the Resend API with a key you hold. Optional later, verify nariway.com with two or three Cloudflare DNS records for pristine inbox delivery. | Account already exists. One API call. Built for exactly this. Best deliverability. Near-zero setup. Free at your volume, forever. | One third-party vendor, though you already use it. |
| **Cloudflare Email** (Worker) | Write and deploy a small Worker with wrangler. The task calls it with a secret. | Stays on Cloudflare, infrastructure you already control. No new vendor. | More setup, and a running Worker to maintain. Cloudflare's outbound sending is newer than Resend. More moving parts for a one-email job. |

## Recommendation, custom to Nariway
**Use Resend.** Three reasons specific to you, not generic.
- You already have the account, so there is nothing new to set up.
- The job is trivial, one email a day to yourself, so building and maintaining a Worker buys nothing you need.
- Resend is purpose-built for transactional email and has the better deliverability, so the digest lands in your inbox rather than in Promotions.

The instinct to keep everything on Cloudflare is reasonable, and for something bigger it might win. For a single daily email it is the wrong optimization. You would be running a Worker to do what Resend does in one line.

## Does the advisory panel need to weigh in
No. This is small and fully reversible, you can switch senders in an afternoon, and the cost is zero either way. It does not warrant the panel. The CFO's only note is that both are free at your volume. This is the kind of decision the IT function should simply recommend and you should simply make.

## What happens next
You keep your Resend key on your side. I wire the morning task to call Resend and send the digest to alina@nariway.com. Start with no DNS changes so it works tomorrow, then add the nariway.com verification later for cleaner placement. I will give you the exact records when you want them.
