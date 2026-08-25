# GWT prototype vs. production tokens — measured comparison (2026-08-25)

> Actual computed CSS read live from nariway.com (homepage, `/collections` index, and a Collection page, `/collections/almaty-museum-of-arts`), versus the current GWT prototype. Purpose: the Knowledge Base must inherit the site's typographic DNA and spatial scale, not a new system. **No redesign made here — this is the evidence for the next decision.**

## The two facts that explain most of the mismatch
1. **The reading font on content pages is Schibsted Grotesk 17px, not Manrope.** The `<body>` default is Manrope 16px, but every content page renders prose in **Schibsted Grotesk 17px / lh 1.7**. The prototype uses Manrope for body — a real DNA mismatch.
2. **The dek/intro is Schibsted Grotesk 19px (sans), not a large serif.** The homepage lede is `Schibsted Grotesk 19px / 30.4`. The prototype's standfirst is a 23–31px serif — that is why it reads "much too large."

## Comparison table

| Element | Production (nariway.com, measured) | GWT prototype (current) |
|---|---|---|
| **Content / max width** | Collection page outer wrap **1240px** (pad 64); Index wrap **900px** (pad 52); **reading text measure ~620–675px** (collection body 623px, homepage lede 673px, index lead 540px) | field **800px**; reading measure **528px** (33rem) |
| **Page title** | Newsreader **500** · **37.6px** collection / 45.6 index / 56 home · lh ~1.05–1.1 | Newsreader 500 · clamp **35–51px** · lh 1.05 |
| **Section heading** | Newsreader **500** · **23.2px** · lh **29px (1.25)** | none as such; "argument statement" Newsreader 400 · 23–31px · lh 1.32 |
| **Body** | **Schibsted Grotesk 400 · 17px · lh 28.9 (1.7)** (desktop); ~17.6/24.6 mobile · measure ~620px | **Manrope 400 · 16–18px · lh 1.66** · measure 528px |
| **Dek / intro** | **Schibsted Grotesk 400 · 19px · lh 30.4 (1.6)** (homepage lede) | Newsreader **serif** · **23–31px** (standfirst) |
| **Small labels / meta** | Schibsted Grotesk **600 · 11.5px uppercase** (labels); 13px (source) | 0.82rem (**13px**), uppercase eyebrow |
| **Paragraph spacing** | ~**19px** (lede) up to ~38px block gaps | 20px (1.25rem) |
| **Major section spacing** | **~90px desktop / ~61px mobile** (`.cc-sec` margin-top 89.6 / 60.8) | variable, invented: turn 46–84px, peak 76–136px, bigspace 58–104px |
| **Horizontal padding (desktop / tablet / mobile)** | **64px / 38px / 24px** (collection wrap); 52px desktop (index) | **40px / ~30px / 22px** (clamp 22–40) |
| **Fonts in use** | Newsreader (headings) · Schibsted Grotesk (body, dek, labels) · Manrope (body default only) | Newsreader (title + argument statements) · Manrope (body) · Schibsted (labels) |
| **Largest display element** | Homepage h1 **56px** (no giant stat anywhere) | **$992B up to 96px** |

## Diagnosis, mapped to the stated assessment
- **"Too narrow."** Confirmed: reading measure 528px vs production ~620–675px; padding 40px vs 64px. Widen both.
- **"Body too small."** Confirmed and worse than "small" — it is the **wrong font** (Manrope 16–18px vs Schibsted Grotesk 17px/1.7). Switch body to Schibsted Grotesk 17px/1.7.
- **"Standfirst much too large."** Confirmed: 23–31px serif vs the site's 19px Schibsted Grotesk sans dek. Roughly halve it and change the font.
- **"$992B oversized / too loud."** Confirmed: up to 96px vs the site's largest element at 56px. It must not exceed the title scale.
- **"Spacing arbitrary."** Confirmed: the prototype invents three section-gap clamps; the site uses one consistent rhythm (section ~90px desktop / ~61px mobile, paragraph ~19px). Adopt the site's tokens.
- **"Margin annotations too small and force a narrow column."** Remove the concept in the next version; precedents go inline.

## The tokens the next version must inherit (not reinterpret)
- Body: **Schibsted Grotesk 17px / lh 1.7**, reading measure **~640–680px**.
- Dek: **Schibsted Grotesk 19px / lh 1.6** (sans, not serif).
- Title: **Newsreader 500 ~38–46px** (collection/index scale), lh ~1.1.
- Section markers / argument statements: **Newsreader 500 ~23px**, lh 1.25 (the site's h2 scale) — not 31px.
- Labels/meta: **Schibsted Grotesk 600 ~11.5px uppercase**.
- Paragraph spacing **~19px**; major section spacing **~90px** (desktop), **~61px** (mobile).
- Horizontal padding **64 / 38 / 24** (desktop / tablet / mobile).
- $992B: keep it a number, but no larger than the title scale (~46–56px), never the loudest thing on the page.

*Measured 2026-08-25 from live nariway.com. For review before the next GWT prototype. The KB keeps its own editorial composition, but on this shared DNA.*
