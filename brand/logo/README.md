# Trueforms logo: confirmed reference

**Updated:** 5 November 2026. **Scope:** the standalone icon, wordmark, independent dot, and complete horizontal logo.

This README records the established source decisions and the reconstruction results verified so far. It does not define product UI, select a technology stack, or promote proposed usage values into approved brand rules.

![Primary Trueforms B logo](../handoff/v2/assets/svg/trueforms-logo.svg)

## Identity and primary asset

| Subject | Confirmed reference |
| --- | --- |
| Brand name | Trueforms |
| Wordmark | `trueforms`, nine lowercase letters |
| Domain association | `truefor.ms` |
| Primary layout | **B**, with the dot centered within the visible r/m height |
| Alternative layout | **A**, with the dot near the baseline |
| Primary production file | [Original B SVG](../handoff/v2/assets/svg/trueforms-logo.svg) |
| Alternative production file | [Original A SVG](../handoff/v2/assets/svg/trueforms-logo-alt-a.svg) |
| Wordmark source | Nimbus Roman Regular, converted to outlines |
| Dot | The font's actual period outline, separately positioned between r and m |
| Runtime font requirement | None for the outlined SVG |

The dot is not inserted into the word's text advance and is not replaced with a geometric circle. The accessible name remains **Trueforms**. A/B selection uses different placements of the same letter shapes; A includes small dot-X and group-Y differences in addition to its different dot height.

## Colors

The established primary color treatment is fully opaque:

| Element | Color |
| --- | --- |
| Icon | `#16765C` |
| Wordmark | `#183C32` |
| Dot | `#AFBDB0` |
| Reference light surface | `#F8F7F2` |

The logo SVG and its transparent PNG do not include the reference surface. Preview images may include that background. Dot color is explicit, not produced by reducing opacity.

The original package also includes `mono`, `black`, `white`, and inline `currentcolor` derivatives. Its `dark` treatment is a **source proposal**. The newly reconstructed complete logo currently covers **B/color** only; the existence of other original variants does not mean they have all been independently reconstructed.

## Icon geometry

| Measurement or feature | Value |
| --- | --- |
| Structure | Folded document, four text rows, open lower-right corner, detached checkmark |
| Path count | Four: document outline, fold, shared row path, checkmark |
| Centerline document dimensions | `96 × 128` SVG units |
| Painted dimensions | `102.5 × 134.5` SVG units |
| Stroke | `6.5`, round caps and joins, no fill |
| Fold size | `32` units |
| Row lengths | `26, 56, 56, 26` centerline units |
| Vertical row spacing | `20` centerline units |
| Checkmark diagonal runs | `14` and `26` units at 45 degrees; leg ratio `7:13` |

The open corner, four-row pattern, and separation between the checkmark and document are defining features. Stroke scales with the artwork. The icon is a brand mark, not an application success-state indicator.

## Complete-logo geometry and spacing

| Measurement | Value |
| --- | --- |
| Source viewBox | `157.5745 65.0525 619.5523611111112 100.895` |
| Overall aspect ratio | Approximately `6.140565549 : 1` |
| Icon scale inside logo | `0.75` |
| Visible icon dimensions inside logo | `76.875 × 100.875` units |
| Effective icon stroke inside logo | `4.875` units |
| Visible icon-to-wordmark gap | `28.5` units |
| Font size used for outlining | `125.13888888888889` units at `1000` units per em |
| Wordmark local bounds | `1.6268055556, -85.4698611111, 515.7841666667, 1.2513888889` |
| B dot local center | `361.4328472222, -28.7819444444` |
| Dot dimensions | Approximately `13.8904166667 × 13.8904166667` units |

Native font pair kerning is applied first. The following additional spacing is then applied to the natural word, in SVG units:

| Pair | Additional spacing | Cumulative shift of following letter |
| --- | --- | --- |
| t/r | 5.0 | 5.0 |
| r/u | 4.0 | 9.0 |
| u/e | 4.5 | 13.5 |
| e/f | 3.0 | 16.5 |
| f/o | 4.0 | 20.5 |
| o/r | 4.0 | 24.5 |
| r/m | 6.5 | 31.0 |
| m/s | 3.5 | 34.5 |

A single CSS `letter-spacing` value does not reproduce this arrangement. Exact coordinates and A/B deltas remain in the [logo specification](../handoff/v2/specs/trueforms-logo-spec.json).

## Independent reconstruction completed

Both the standalone icon and the primary B/color full logo have been recreated separately from the approved SVG files:

- The icon generator builds its paths from named geometry measurements. The specification's measurement tables and path descriptions were consulted; this is not a claim that the original definitions were never seen.
- The complete-logo generator extracts letter and period outlines from a pinned Nimbus Roman Regular font, applies native AFM kerning and the specified additional spacing, and places the independently generated icon.
- Neither generator reads the approved logo/icon SVG or copies its `d` strings. The original assets were read separately after generation for comparison.
- The recreated SVGs use zero-origin viewBoxes with all coordinates consistently translated. The original files and the recreated files are therefore not byte-identical.
- The standalone reconstruction uses equivalent cubic curves for the specified quadratic turns. The complete logo contains 14 paths: four icon paths, nine letter paths, and one period path. There is no live text or embedded raster image.

The reconstruction is a separate artifact and has **not replaced the approved source masters**.

### Exact font and build inputs

The font is sourced from `ArtifexSoftware/urw-base35-fonts`, pinned to revision `3c0ba3b5687632dfc66526544a4e811fe0ec0cd9`.

| Input | Pinned identity |
| --- | --- |
| `NimbusRoman-Regular.otf` SHA-256 | `fd41669443616a7ae890c42e53a58f47fa24a940fd1e367acaff665cf5b6e9d8` |
| `NimbusRoman-Regular.afm` SHA-256 | `e476212c416039aa9805f20d945e2b3a522be5de15125cb566d257482379ccd9` |
| Python logo-build dependency | `fonttools==4.68.0` |
| Icon-build dependency | Python standard library only |

The font, AFM metrics, and upstream `LICENSE`/`COPYING` files are retained together under `docs/brand/reconstruction-sources/nimbus-roman/`. The logo generator verifies the two input hashes. These are build inputs; the final SVG does not load a font.

### Files and regeneration

All logo materials, reconstruction scripts, inputs, outputs, and evidence belong to this docs repository. The following relative links work locally and in the GitHub repository viewer. The UI repository is reserved for actual UI components.

| Deliverable | Repository location |
| --- | --- |
| Full logo SVG / PNG | [SVG](../recreated/trueforms-logo.svg) · [PNG](../recreated/trueforms-logo.png) |
| Standalone icon SVG / PNG | [SVG](../recreated/trueforms-icon.svg) · [PNG](../recreated/trueforms-icon.png) |
| Build scripts | [Icon](../scripts/recreate-icon.py) · [Complete logo](../scripts/recreate-logo.py) |
| Reconstruction guide | [README](../recreated/README.md) |
| Font provenance and notices | [Source README](../reconstruction-sources/nimbus-roman/README.md) |
| Calculated logo measurements | [Construction report](../recreated/logo-construction.json) |
| Raster comparison evidence | [Icon report](../recreated/verification.json) · [Logo report](../recreated/logo-verification.json) |

Run from the `docs` repository, using your chosen Python environment:

```powershell
python -m pip install -r brand/scripts/requirements-reconstruction.txt
python brand/scripts/recreate-icon.py
python brand/scripts/recreate-logo.py
```

These commands regenerate the SVGs and the logo construction report. They do **not** regenerate PNG previews or raster-comparison reports. Those were produced in a separate verification step; a checked-in one-command raster verification tool has not yet been added.

## What has actually been verified

- The preserved handoff contains 106 files, all compared byte-for-byte with the supplied archive. Its validator passed 192 checks, including 105 manifest entries. See the [handoff review](../../reviews/brand-handoff-v2.md).
- Reconstructed wordmark bounds, overall dimensions, dot size/position, and icon gap agree with the numeric specification within the comparison tolerance of `1e-8` SVG units.
- The recreated icon and logo contain no reused original path strings. Logo SVG checks also confirmed no live text or embedded raster image.
- Raster comparisons used **sharp 0.35.5 / librsvg 2.63.2**, rendering both vectors at density 720 before resizing to the same target dimensions.

Full-logo results:

| Width in pixels | Pixels differing from the reference |
| --- | --- |
| 200 | 4 |
| 240 | **0** |
| 280 | 2 |
| 1200 | 58 |
| 2400 | 148 |

The standalone icon matched exactly at 32 px height in the same comparison process. Other tested icon sizes had small nonzero raster differences. An exact match at one size is not a claim of identical SVG bytes or identical output in every renderer.

Preview images were visually inspected. Browser behavior, physical-device rendering, print, and platform-specific favicon processing were not tested.

## What remains a proposal or an open item

- The source dark-theme palette is still a proposal.
- A 240 px logo width, 200 px trial lower width, 32 px icon height, and the suggested clearspace values are starting recommendations, not universally accepted minimum-size rules.
- Native small-size legibility and real-background usage still need acceptance in their target contexts.
- The independent reconstruction currently covers the standalone color icon and B/color full logo. Independent A and other color-mode builds are not included.
- A reusable one-command raster-rendering/comparison tool remains unfinished.

## Commit and contribution rules

Logo assets, generation scripts, and related documentation follow the [shared contribution rules](../../contributing/README.md):

- Push only as **`formtrue`**; never use `bugrakaan` or another fallback account.
- Use **`Trueforms <352186882+formtrue@users.noreply.github.com>`** as both author and committer for newly authored project commits.
- Use **Conventional Commits** for every new commit message, in English; for example, `docs(logo): record confirmed geometry`.

The shared guide distinguishes commit metadata from GitHub authentication and includes configuration, verification commands, and message examples.

## Reference hierarchy

For established artwork, follow the original source priority: approved B/A source SVGs → exact logo JSON → master document → usage proposals. Reconstruction reports demonstrate what was rebuilt and tested; they do not supersede the source masters.

- [Brand hub and all original materials](../README.md)
- [Master PDF](../handoff/v2/trueforms-logo-master-spec.pdf)
- [Master HTML](../handoff/v2/trueforms-logo-master-spec.html)
- [Exact logo specification](../handoff/v2/specs/trueforms-logo-spec.json)
- [Icon geometry](../handoff/v2/specs/geometry.json)
- [Detailed English brand guidelines](../guidelines.md)
