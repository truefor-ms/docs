# Brand and icon guidelines

Date: **5 November 2026**. Source: **Master Spec + Complete Handoff 2.0**.

This English reference supports implementation planning; it does not replace the exact artwork. Package paths below are relative to [the preserved source package](handoff/v2/). For direct access to original documents and assets, use the [brand hub](README.md).

## 1. Source precedence

The master document specifies this order:

1. `source-reference/approved-b.svg` and `approved-a.svg`.
2. `specs/trueforms-logo-spec.json`.
3. The master PDF/HTML explanation.
4. Usage proposals.

For the standalone icon, also preserve `source-reference/approved-icon.svg` and `specs/geometry.json`. For the avatar, preserve `source-reference/approved-avatar-4096.png`. Record inconsistencies for review without silently changing the source.

Legacy references to **Linux Libertine logo typesetting**, a **72.1935 u icon-to-wordmark gap**, or a **687.515 u viewBox width** do not describe the current logo and must not be carried into new implementation work.

## 2. Identity established in source

| Subject | Reference |
| --- | --- |
| Brand name / accessible image name | Trueforms |
| Wordmark text | `trueforms`; domain association `truefor.ms` |
| Primary layout | B: dot centered vertically within the visible r/m height |
| Alternative layout | A: dot near the baseline |
| Primary asset | `assets/svg/trueforms-logo.svg`, an exact B/color source copy |
| Alternative asset | `assets/svg/trueforms-logo-alt-a.svg`, an exact A/color source copy |
| Wordmark | Outlined Nimbus Roman Regular artwork, not live text |
| Dot | Independent period outline between r and m, not a replacement circle or typed punctuation |
| Icon | Folded document, four rows, open lower-right corner, detached checkmark |

The logo does not load a font. Retyping the wordmark, approximating its spacing with CSS, or moving the dot manually changes the artwork. Select the supplied A/B files: their differences include small horizontal and group-vertical offsets as well as the dot's vertical position.

## 3. Geometry to preserve

| Measurement | Value |
| --- | --- |
| Icon paths | 4: document outline, fold, shared four-row path, checkmark |
| Stroke / cap / join | `6.5` / `round` / `round`; `fill="none"` |
| Standalone icon viewBox | `14.75 12.75 102.5 134.5` |
| Standalone icon transform | `translate(4 4)` |
| Horizontal logo viewBox | `157.5745 65.0525 619.5523611111112 100.895` |
| Horizontal aspect ratio | Approximately `6.140565549 : 1` |
| Icon-to-wordmark gap | `28.5 u` |
| Icon transform inside logo | `translate(149.522 58.5) scale(.75)` |
| Effective stroke inside logo | `4.875 u` |
| Row pattern | Short / long / long / short; centers separated by `20 u` |

`u` means SVG user units, not CSS pixels. Do not reset the viewBox origin without transforming the paths consistently. Preserve proportional scaling, including stroke scaling; do not add `non-scaling-stroke`. Supply clearspace through the outer container. Coordinate rounding, path merging, or stroke expansion requires a separately tracked derivative and comparison against the source.

## 4. Color modes

| Mode | Icon | Wordmark | Dot | Status / use |
| --- | --- | --- | --- | --- |
| `color` | `#16765C` | `#183C32` | `#AFBDB0` | Established in source; reference surface `#F8F7F2` |
| `dark` | `#E8EFE5` | `#F8F7F2` | `#657B70` | Source proposal; measured on `#183C32` |
| `mono` | `#183C32` | `#183C32` | `#183C32` | Single-color derivative |
| `black` | `#000000` | `#000000` | `#000000` | Single-color derivative |
| `white` | `#FFFFFF` | `#FFFFFF` | `#FFFFFF` | Single-color derivative |
| `currentcolor` | `currentColor` | `currentColor` | `currentColor` | CSS color through inline SVG only |

All parts remain fully opaque. Do not derive the dot color with opacity. `dark` and `white` are distinct variants. An external SVG loaded through `<img>` does not inherit the parent's CSS `color`. Logo and standalone icon assets are transparent; avatar and favicon assets include backgrounds.

## 5. Source proposals, pending product acceptance

| Starting proposal | Value | Acceptance needed |
| --- | --- | --- |
| Horizontal logo width | 240 px; 240–280 px in the header | Actual header and mobile layout |
| Trial lower width | 200 px | Serif and dot readability; not a proven minimum |
| Logo clearspace | 26 u on every side | About 10.07 px at 240 px logo width |
| Icon height | 32 px; trial at 24 px | Stroke and detached-checkmark readability |
| Icon clearspace | 13 u on every side | About 3.09 px at 32 px icon height |
| Spacing scale | 4, 8, 12, 16, 24, 32, 48, 64, 96 px | Actual content and component needs |
| Radius | Controls 10 px; cards 20 px | Product design review |
| Dark theme | Supplied semantic-role proposal | Visual and interaction review on actual surfaces |

The 160 px logo sample is an inspection case. A supplied 16 px favicon is not proof of accepted micro-size readability. A redesigned micro icon must be a separate derivative rather than a silent master replacement.

## 6. Typography, tokens, and accessible use

UI fonts are **Rubik 400/700** and **Linux Libertine Display** for display headings. Neither replaces the outlined logo. Rubik 500/600 files are absent. Preserve the supplied `licenses/` notices with font distribution; this is source preservation, not a new licensing assessment.

The supplied `specs/contrast-report.json` reports **1.82:1** for the dot on the light surface, **2.67:1** for the dot on the dark surface, **4.20:1** for muted text on sage, and **1.34:1** for the decorative line on white. These figures do not establish whole-product accessibility. Keep the dot out of functional text/state roles and do not use the decorative line as a control's only distinguishing boundary.

Success, error, warning, and information roles still need product design. The brand checkmark is not confirmation that a form was submitted. Plan persistent labels, associated help/error text, visible keyboard focus, and state communication that does not depend on color alone.

A standalone logo uses the accessible name `Trueforms`. If its home-link container already supplies the accessible name, keep the nested image decorative. Avoid duplicate inline SVG IDs when artwork is repeated.

## 7. Surface-specific assets

| Surface | Starting asset | Additional verification |
| --- | --- | --- |
| Web header/footer | B SVG in a suitable mode | Ratio, manual theme, narrow viewport, focus |
| Compact brand area | Standalone SVG icon | Contextual meaning and readability |
| Profile/avatar | Approved 4096 px PNG or suitable smaller export | Platform square/circle crop |
| Favicon | SVG, ICO, 16/32/48 px PNG | Real browser tab and cache behavior |
| Email | 1200/2400 px-wide PNG | Absolute delivery URL and client dark mode |
| PWA, if selected | 192/512 px app icons with `purpose="any"` | Installation and platform checks; no maskable derivative supplied |
| Print, embossing, motion | Separate derivative work | Production proof or motion acceptance |

On the avatar's 1024-unit square, the visible icon height is 640 with 192-unit top/bottom margins and a `#E8EFE5` background. Do not squeeze the horizontal wordmark into a square. Vertical lockups, taglines, maskable icons, and animation are not completed assets in this delivery.

Sources: master PDF pages 3–24 and 26–28; `specs/trueforms-logo-spec.json`, `specs/geometry.json`, `specs/contrast-report.json`, `tokens/`, and `licenses/`.
