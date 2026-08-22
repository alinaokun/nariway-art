# Decision — retire the daily check-in, replace with a weekly advisor + silent trigger-scan (2026-08-22)

**Question.** The daily check-in email was not valuable. Two redesigns (a chief-of-staff digest, then a board-review dashboard) both missed. What structure, if any, makes a recurring internal email genuinely valuable to a solo founder?

**The root diagnosis (why both redesigns failed).** A check-in is a **mirror**: it reports Alina's own internal state back to the person who created it. As the sole operator working in the vault daily, she already knows what she did, what moved, and the numbers (which barely change: 0 paid, 0 situations, 1 discovery call). The only part that ever landed was "today I learned", because it was the one thing *new to her*. Both redesigns kept building better mirrors. Value can only come from what an **outside voice** can add: new thinking, a forcing function, or a decision surfaced at the right moment.

**Advisory panel (2026-08-22).** *Skeptic:* stop building mirrors; a daily self-to-self email may be the wrong artifact. *CFO:* it should exist only if it moves the one number that matters (first paid client); a weekly accountability loop might. *Research:* the only non-redundant thing is a thought she would not generate herself (a disconfirming question, a tension in the evidence). *CMO:* most valuable is turning the research into outward motion, not summarizing the desk. *Founder-Life:* must reduce load and give energy, never feel like homework; short, or silent.

**Decision (Alina).** Build the **"weekly advisor + event-driven"** model. Kill the daily cadence. One routine, two mechanisms:
1. **Daily silent trigger-scan** — most days it does NOTHING; it emails only when a genuine, time-sensitive, action-required trigger fires (a follow-up due/overdue, a decision awaiting her, a belief changed, a market opening within ~3 days, a real CRITICAL). Silence on empty days is the feature.
2. **Monday weekly advisor** ("Nariway Weekly") — short counsel, not a report: (a) last week's named move, did it happen? (the accountability loop, the one thing she cannot do for herself); (b) the challenge (the conversion gap, argument not metrics); (c) this week's ONE client-advancing move; (d) one provocation from her own evidence. The Monday run also maintains the scoreboard internally (it is no longer pasted into any email).

**Why.** Removes the redundant daily mirror; keeps only what an outside voice adds (a push toward the first client + a thought she did not have); matches her solo temperament (short or silent). The accountability loop is powered by [[weekly-brief]]; the deliberation model is [[advisory-panel]].

**Implementation.** Same cloud routine (trig_01JgBkpKKHirinAdDrKmkxZk), renamed, daily cron kept (the daily run is the trigger-scan), Monday branch is the weekly email. Signals (the outside-in morning brief) is untouched and separate.

**Outcome (to fill in later).** Does the weekly advisor actually get read and acted on? Does the accountability loop change behavior? Revisit after ~3-4 weeks.
