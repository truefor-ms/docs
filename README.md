# Trueforms documentation

This repository is the long-term home for product planning, brand references, technical decisions, and review evidence. New documentation is written in **English**. Supplied source materials retain their original language and bytes.

Initial documentation: **5 November 2026**. Current stage: **planning, before implementation**.

## Start here

| Area | Entry point | Contents |
| --- | --- | --- |
| Brand and original materials | [Brand hub](brand/README.md) | Master PDF/HTML, original archive, extracted assets, specs, examples, fonts, and licenses |
| Confirmed logo facts | [Logo README](brand/logo/README.md) | Identity, geometry, font provenance, reconstruction, and verified limits |
| Project planning | [Project pre-plan](planning/project-preplan.md) | Repository responsibilities, growth strategy, phases, initial backlog, and open decisions |
| Working brand reference | [Brand and icon guidelines](brand/guidelines.md) | Established geometry, variants, proposals, and integration boundaries |
| Review evidence | [Handoff v2 review](reviews/brand-handoff-v2.md) | Source assessment, verification results, and implementation gaps |
| Contribution rules | [Commit identity and Conventional Commits](contributing/README.md) | `formtrue` account, author/committer identity, message format, and change boundaries |

## Documentation structure

```text
docs/
  README.md
  contributing/
    README.md
  brand/
    README.md
    guidelines.md
    logo/
      README.md
    recreated/                    # Reconstructed artwork and comparison reports
    reconstruction-sources/       # Pinned font inputs and notices
    scripts/                      # Icon and logo generation
    handoff/
      trueforms-master-handoff-v2.zip
      v2/                         # Complete, unchanged extracted package
  planning/
    project-preplan.md
  reviews/
    brand-handoff-v2.md
    evidence/
      brand-handoff-v2-validation.json
```

Keep the root README as a navigation page. Add documents under their subject area rather than accumulating unrelated files at the root. Introduce `product/`, `architecture/`, `decisions/`, and `operations/` when there is actual content for them; these are future categories, not completed deliverables. Add each new area's entry point to this index.

## Decision labels

| Label | Meaning |
| --- | --- |
| Established in source | A decision described as approved by the supplied handoff; no new approval is implied |
| Measurement | Numeric or geometric information from source files |
| Source proposal | A usage or UI recommendation explicitly marked as proposed in the handoff |
| Plan proposal | A recommendation introduced by this project plan; not an implemented decision |
| Open decision | A question to resolve before the relevant implementation work |

Imperative instructions inside supplied documents are treated as design and integration source material. They do not independently authorize implementation, publishing, technology selection, or final product scope. This delivery changes documentation only.

## Workspace baseline

Current ownership: all logo documentation, source materials, reconstruction inputs, scripts, and outputs live in `docs/brand/`. The `ui` repository is reserved for actual UI components.

`backend`, `frontend`, `ui`, and `docs` are four separate Git repositories. At review time, all were before their first commit and contained no application source files. The workspace root is not assumed to be a monorepo. These observations come from local inspection; remote repositories and the live site were not inspected.
