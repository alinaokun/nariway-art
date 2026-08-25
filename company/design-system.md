# Nariway Design System — the house style (canonical)

*Everything Nariway produces visually, the flagship report, decks, org charts, one-pagers, uses this. **Aligned to the live nariway.com brand (2026-08-19), so the site, the report, and every asset read as one identity.** The goal is a **modern, sophisticated, editorial, highly elevated** look, the restraint of a top research institute (WEF, McKinsey Global Institute) with the warmth and literacy of a serious publication. Authority comes from space, hierarchy, typography, and precision, never from decoration. The live site is owned by the separate `nariway-rebuild` project (see [[website]]); this doc mirrors that brand for everything produced here.*

## Hard don'ts (what "elevated" is NOT)
- **No warm cream / beige / yellowish grounds. No brown or terracotta ink or accents.** The brand ground is clean **white**; the ink is a **warm near-black** (a hair of warmth, not brown). Never a cream page or brown text. (Cream/brown was the earlier mistake, the generic AI-design cliché.)
- No textures, drama drop-shadows, heavy rounded corners, gradients-as-decoration, or emoji as section markers.
- **The serif is for editorial headlines only (Newsreader), used with restraint**, never as ornament. No script, slab, or decorative serifs; no serif in body text.

## Palette (warm near-monochrome on white)
Light: `--bg:#FFFFFF` · `--surface:#FFFFFF` · `--surface-2:#F7F6F3` (a barely-warm off-white for panels) · `--ink:#1A1A17` (warm near-black, headings) · `--ink-body:#0A0A0A` · `--ink-2:#3A3A34` · `--muted:#6B6B62` · `--line:#E7E5DF` (warm hairline) · `--line-2:#D4D2CA`.
Dark: `--bg:#141412` · `--surface:#1B1B18` · `--surface-2:#201F1C` · `--ink:#F2F1EC` · `--ink-2:#C7C5BC` · `--muted:#918E84` · `--line:#2A2925` · `--line-2:#3A3833`.
The brand is essentially **monochrome warm**, white ground, warm near-black ink, warm-gray secondaries, hairlines. Color is used almost never; if a single restrained accent is truly needed, keep it quiet and warm-neutral, not a bright hue. Buttons are **text or hairline-outline** (transparent ground, no fill, sharp corners), matching the live site. Keep this one family consistent across the report, decks, and the site.

## Type (the editorial pairing, from the live site)
- **Headlines and display: Newsreader** (an editorial serif), medium weight (~500), large and confident, slight negative letter-spacing at big sizes. This is the brand's voice.
- **Body: Manrope** (a clean geometric sans), comfortable size, ~65-character measure for running text.
- **Eyebrows / micro-labels / UI: Schibsted Grotesk** (or Manrope), uppercase, `letter-spacing:.15em`, ~0.72rem, muted.
- **Numerals:** always `font-variant-numeric: tabular-nums` where figures align.
- Strong scale contrast between a large serif headline and small precise sans text is the primary hierarchy device.
- Fonts: the three are Google Fonts. In Artifacts, load them from Google Fonts (the one allowed external host) with real fallback stacks, Newsreader → Georgia, "Times New Roman", serif; Manrope / Schibsted Grotesk → system-ui, sans-serif. Elsewhere inline as `@font-face` data URIs. Always give every face a genuine fallback.

## Layout
Generous whitespace. **Hairline 1px rules are the primary structural device**, not filled boxes. **Sharp corners (0–2px)**, matching the live site. A clear grid, aligned columns, and a tabular stat row where numbers matter. Cards are white (or `--surface-2`) with a hairline border and real padding, never a shadow-heavy or textured panel.

## Always
- Theme-aware (light and dark, both designed, via `prefers-color-scheme` + `data-theme` overrides). Light mode (white ground) is the primary elevated look.
- Self-contained CSS; the three brand fonts load from Google Fonts (the one host Artifacts allow) or inline as data URIs, always with fallback stacks. Responsive; wide content scrolls in its own container.
- Favicon consistent per artifact.

## Emails (the daily Signals + check-in)
Both daily emails render in this brand with **email-safe** technique (set in their cloud routines, 2026-08-20): every CSS rule INLINE on the elements (mail clients drop `<style>`/`<head>`), a Google Fonts link that degrades gracefully, and brand fonts with strong fallbacks, **Newsreader → Georgia serif** for headlines and masthead, **Manrope / Schibsted Grotesk → system sans** for body. Warm near-black ink on white, warm hairline rules, tabular numerals. Where a client blocks web fonts, the serif fallback keeps the editorial feel, so it reads on-brand everywhere.

**Mobile-first column (required, fixed 2026-08-23 — the emails were unreadable on phones):** the centered content table must be **fluid** — `width="100%"` with an inline `style="max-width:620px"` — and NEVER a fixed `width="620"` / `width:620px`. A fixed pixel width forces a phone's layout viewport to ~620px, so the whole email zooms out and every line is clipped (confirmed: at a 375px viewport the fixed version reports an innerWidth of 620 and scrolls, the fluid version fits at 375 with no overflow). Inline `max-width` is the guarantee: it is fully email-safe (needs no `<style>`, which clients drop) and shrinks to fit any phone. Keep cell side-padding small (~8px) so text is not crowded when the column narrows. A `<style>` media query may progressively tune padding/size on clients that keep `<head>`, but must never be the ONLY thing making the email responsive.

## Knowledge Base pages (the research-publishing register)
A KB entry is *visual research publishing*, enjoyable to read and to scan. Argument headlines carry the thinking, structured objects (matrices, data fields, pathways) carry the proof, prose explains only what neither can show. Specifics for these pages:
- **Section headlines run the full content width**, set in Newsreader, never constrained to a data column. The material beneath them (tables, columns, figures) breaks into its own narrower structure.
- **Vary the treatment; do not repeat one template.** A comparison table, a data field, a staggered pair, and a pathways list should each look different so no two evidence blocks read the same. Two statistics in a row must not sit in identical layouts.
- **Do not use a horizontal rule when hierarchy or whitespace already communicates the transition.** A new headline plus generous space is the transition. Rules should be rare enough that when one appears, it means something (a table's own structure, or the single hairline before Sources where the information type genuinely changes). This is a house rule, not only a KB rule.
- **No standalone precedent inserts.** Collection Index examples belong inside the argument (subordinate to a pathway or a claim), not as a boxed interruption in the reading flow.
- Reading/body type on KB pages follows the *measured live-site tokens* (see [[gwt-vs-production-tokens]]): Schibsted Grotesk 17px/1.7 for reading, Newsreader 500 for headlines and figures. Prototype: [[prototypes/gwt-page|The Great Wealth Transfer and Art]].

## Live examples
- [The Digital Workforce](https://claude.ai/code/artifact/477c16e5-0cd8-4558-ba79-adb8ea33b216) (org chart)
- [What Becomes of Great Art Collections](https://claude.ai/code/artifact/6c3dde4f-bfc0-4b43-876c-ede2633907f6) (report visual)

*Both were built to the earlier cool-navy "Institutional Modern" system; they predate the 2026-08-19 editorial rebrand and should be re-skinned to the palette and type above the next time they are produced. When Alina wants a different tone, adjust within this warm-monochrome family; keep the Newsreader + Manrope pairing as the constant.*
