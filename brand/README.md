# Brand hub

The original Trueforms materials are active working references. Start with the master document, use the supplied assets, and consult the English guidelines for implementation planning.

## Master documents and working references

| Resource | Purpose |
| --- | --- |
| [Original master PDF](handoff/v2/trueforms-logo-master-spec.pdf) | Complete 32-page brand specification and handoff |
| [Original master HTML](handoff/v2/trueforms-logo-master-spec.html) | Offline document with embedded visual examples and logo laboratory |
| [English brand and icon guidelines](guidelines.md) | Practical reference, decision status, and integration constraints |
| [Handoff review](../reviews/brand-handoff-v2.md) | Findings, verification evidence, and outstanding application checks |
| [Project pre-plan](../planning/project-preplan.md) | How the brand foundation connects to the growing product |

## Original production materials

| Material | Direct access |
| --- | --- |
| Primary B logo | [SVG](handoff/v2/assets/svg/trueforms-logo.svg) |
| Alternative A logo | [SVG](handoff/v2/assets/svg/trueforms-logo-alt-a.svg) |
| Standalone icon | [Color SVG](handoff/v2/assets/svg/trueforms-icon-color.svg) |
| Approved avatar | [4096 px PNG](handoff/v2/source-reference/approved-avatar-4096.png) |
| SVG / PNG families | [SVG directory](handoff/v2/assets/svg/) · [PNG directory](handoff/v2/assets/png/) |
| Unchanged source references | [Source directory](handoff/v2/source-reference/) |
| Exact logo specification | [Logo JSON](handoff/v2/specs/trueforms-logo-spec.json) |
| Icon geometry | [Geometry JSON](handoff/v2/specs/geometry.json) |
| Colors and theme examples | [Token JSON](handoff/v2/tokens/trueforms.tokens.json) · [CSS](handoff/v2/tokens/trueforms.css) |
| Browser laboratory | [System theme](handoff/v2/examples/index.html) · [Light](handoff/v2/examples/light.html) · [Dark](handoff/v2/examples/dark.html) · [Monochrome](handoff/v2/examples/monochrome.html) |
| React integration example | [TrueformsBrand.tsx](handoff/v2/examples/TrueformsBrand.tsx) |
| Fonts and notices | [Fonts](handoff/v2/assets/fonts/) · [Licenses](handoff/v2/licenses/) |
| Original handoff text | [Instructions](handoff/v2/HANDOFF-INSTRUCTIONS.txt) · [Package README](handoff/v2/README.txt) |
| Integrity and validation | [Manifest](handoff/v2/MANIFEST.sha256) · [Validator](handoff/v2/scripts/validate-assets.py) |
| Original archive | [Download ZIP](handoff/trueforms-master-handoff-v2.zip) |

The entire extracted package is available under [handoff/v2](handoff/v2/), including figures, provenance, reports, platform examples, and rendering scripts. Its original relative structure is preserved, so local HTML examples retain their asset paths. Browser interaction still needs application-level verification.

## Preservation and use

- Source: `D:/Downloads/trueforms-master-handoff-v2.zip`, supplied by the user.
- Package version/date: **2.0 / 5 November 2026**.
- ZIP size: **5,904,790 bytes**.
- ZIP SHA-256: `f4e5cec1925db29b122d15cb95677220c77712ed747756e8f648cf2d77a07b55`.
- Extracted content: **106 files**, with **105 entries** covered by the supplied manifest; the manifest does not hash itself.
- The original Turkish text is retained. English summaries and review evidence live outside the preserved package.

Do not edit the preserved v2 package in place. Future source deliveries belong in their own version directory with provenance and review notes. Implementation-specific changes belong in the relevant application/UI repository. The version directory supports traceability while this hub keeps the materials directly accessible.

To rerun the inspected validator from the `docs` repository, using Python 3:

```powershell
python -X utf8 .\brand\handoff\v2\scripts\validate-assets.py
```

Keep generated reports outside `handoff/v2/`: the validator reads every JSON file in its package tree. The current review result is stored in [review evidence](../reviews/evidence/brand-handoff-v2-validation.json).
