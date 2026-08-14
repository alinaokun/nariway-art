#!/usr/bin/env python3
"""Send queued Nariway emails via Resend.

Reads email jobs from .mail/outbox/*.json (each: {from, to, subject, html}) and
POSTs them to the Resend API using the RESEND_API_KEY GitHub Actions secret.

On a push, it sends only the outbox files that CHANGED in the latest commit, so a
check-in push never resends the Signals digest and vice versa. On a manual
workflow_dispatch, it sends whatever is currently in the outbox (for testing).
"""
import json
import os
import subprocess
import sys
import urllib.request
from urllib.error import HTTPError

OUTBOX = ".mail/outbox"


def changed_outbox_files():
    try:
        out = subprocess.check_output(
            ["git", "diff", "--name-only", "HEAD~1", "HEAD"], text=True
        )
        return [ln.strip() for ln in out.splitlines() if ln.strip()]
    except Exception as e:  # first commit, shallow clone, etc.
        print(f"git diff unavailable ({e}); will consider all outbox files.")
        return None


def all_outbox_files():
    if not os.path.isdir(OUTBOX):
        return []
    return [os.path.join(OUTBOX, f) for f in os.listdir(OUTBOX)]


def main():
    key = os.environ.get("RESEND_API_KEY")
    if key:
        key = key.strip()  # a trailing newline in the secret corrupts the auth header
    if not key:
        print("No RESEND_API_KEY secret is set; nothing sent.")
        return 0
    print(f"Key present: length {len(key)}, prefix {key[:3]}...")

    event = os.environ.get("GITHUB_EVENT_NAME", "")
    if event == "workflow_dispatch":
        targets = all_outbox_files()
    else:
        changed = changed_outbox_files()
        if changed is None:
            targets = all_outbox_files()
        else:
            targets = [
                f for f in changed
                if f.startswith(OUTBOX + "/") and f.endswith(".json")
            ]

    targets = [f for f in targets if f.endswith(".json") and os.path.exists(f)]
    if not targets:
        print("No queued emails to send.")
        return 0

    sent = 0
    for f in targets:
        try:
            msg = json.load(open(f, encoding="utf-8"))
            payload = json.dumps({
                "from": msg["from"],
                "to": msg["to"],
                "subject": msg["subject"],
                "html": msg["html"],
            }).encode("utf-8")
            req = urllib.request.Request(
                "https://api.resend.com/emails",
                data=payload,
                headers={
                    "Authorization": f"Bearer {key}",
                    "Content-Type": "application/json",
                },
            )
            resp = urllib.request.urlopen(req, timeout=30)
            print(f"Sent {f}: HTTP {resp.status}")
            sent += 1
        except HTTPError as e:
            body = e.read().decode(errors="replace")
            print(f"FAILED to send {f}: HTTP {e.code} - {body}")
        except Exception as e:
            # Never fail the whole job on one bad send; report and continue.
            print(f"FAILED to send {f}: {e}")

    print(f"Done. {sent} email(s) sent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
