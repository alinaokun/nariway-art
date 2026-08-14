# Nariway Design System — the house style (canonical)

*Everything Nariway produces visually, reports, decks, org charts, the website, uses this. The goal is a **modern, sophisticated, authoritative, highly elevated** look, the restraint of a top research institute (WEF, McKinsey Global Institute) with the precision of a contemporary art institution. Authority comes from space, hierarchy, and precision, never from decoration.*

## Hard don'ts (what "elevated" is NOT)
- **No warm cream / beige / yellowish grounds. No brown or terracotta ink or accents.** (This was the earlier mistake, it is the generic AI-design cliché, not sophistication.)
- No textures, drop shadows for drama, heavy rounded corners, gradients-as-decoration, or emoji as section markers.
- No decorative serifs used for warmth. Restraint over ornament.

## Palette (cool, near-monochrome, one accent)
Light: `--bg:#FBFBFC` · `--surface:#FFFFFF` · `--surface-2:#F4F5F7` · `--ink:#0E1116` · `--ink-2:#3B424C` · `--muted:#697180` · `--line:#E6E8EC` · `--line-2:#CED3DB` · `--accent:#1B3A5B` (deep petrol-navy, used sparingly).
Dark: `--bg:#0B0D11` · `--surface:#14171D` · `--surface-2:#0F1218` · `--ink:#EBEEF2` · `--ink-2:#B7BFC9` · `--muted:#8B94A1` · `--line:#222833` · `--line-2:#333B48` · `--accent:#7AA5D6`.
The accent appears only on key numbers, thin rules, cadence/live indicators, and active states. Everything else is monochrome. **The accent is a single token, swap it to re-tone the whole system.**

## Type
Grotesque only: `-apple-system, BlinkMacSystemFont, "Helvetica Neue", Helvetica, Arial, "Segoe UI", system-ui, sans-serif`. Strong scale contrast (a large confident headline against small precise text). **Micro-labels / eyebrows:** uppercase, `letter-spacing:.2em`, ~0.7rem, muted. **Numerals:** always `font-variant-numeric: tabular-nums`. Tight negative letter-spacing on large display sizes.

## Layout
Generous whitespace. **Hairline 1px rules are the primary structural device**, not filled boxes. Near-square corners (2–4px). A clear grid, aligned columns, and a tabular stat row where numbers matter. Cards are white (or `--surface`) with a hairline border and real padding, never a shadow-heavy or textured panel.

## Always
- Theme-aware (light and dark, both designed, via `prefers-color-scheme` + `data-theme` overrides). Light mode is the primary elevated look.
- Self-contained (inline CSS, no external fonts/CDNs), responsive, wide content scrolls in its own container.
- Favicon consistent per artifact.

## Live examples (built to this system)
- [The Digital Workforce](https://claude.ai/code/artifact/477c16e5-0cd8-4558-ba79-adb8ea33b216) (org chart)
- [What Becomes of Great Art Collections](https://claude.ai/code/artifact/6c3dde4f-bfc0-4b43-876c-ede2633907f6) (report visual)

*When Alina wants a different tone, change the `--accent` token first; the rest holds.*
