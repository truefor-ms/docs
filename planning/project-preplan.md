# Trueforms project pre-plan

**Date:** 5 November 2026 · **Status:** draft, before implementation · **Basis:** brand handoff v2.0 and local repository inspection.

## 1. Objective and scope

Build a product foundation that can grow while preserving the established brand. Start with versioned brand assets, a small shared UI foundation, and one verifiable product journey. Expand the component library and infrastructure in response to actual usage.

The handoff is a substantial **brand and integration specification**, not a product requirements document. It mentions form and application creation, but does not settle user roles, the data model, pricing, hosting, or launch scope. The product journey below is therefore a proposal. No technology stack, delivery schedule, or capacity commitment is established here.

This delivery covers documentation and source preservation. Application development, repository restructuring, package publication, and deployment remain future work.

## 2. Starting point and repository responsibilities

The initial workspace inspection found four separate Git repositories, each before its first commit. Repository count does not imply service count. The confirmed ownership boundary is that logo materials and reconstruction tooling stay in `docs`, while `ui` contains actual UI components.

| Repository | Proposed responsibility | Boundary |
| --- | --- | --- |
| `docs` | Product scope, brand originals, reconstruction sources/scripts/outputs, decisions, contract explanations, review records | Not a runtime asset server |
| `ui` | Actual shared accessible UI components, their tokens, and component examples | No logo source archive or reconstruction tooling; no backend business rules |
| `frontend` | Pages, navigation, application theme, feature journeys, API consumption | No redrawn logo or independently maintained copies of shared tokens |
| `backend` | Authorization, domain rules, persistence, API implementation and contract | No brand geometry or visual theme logic |

Dependency direction: frontend consumes a versioned UI distribution and the backend API contract. UI does not depend on frontend. Backend can run independently. Documentation records the relationships between releases.

Sibling directories may be convenient during development, but a release must not require a developer's `../ui` directory. Establish reproducible package or artifact consumption. Consider a monorepo only after recording the actual cost of cross-repository changes and the trade-offs of migration.

## 3. From source artwork to product

Proposed flow: **preserved handoff and reconstruction in docs → validated brand artifacts → frontend consumption through UI components → acceptance on actual surfaces**.

1. Keep the original ZIP and complete extracted package accessible through the [brand hub](../brand/README.md), with hashes and provenance.
2. Keep approved artwork, notices, font inputs, reconstruction scripts, and generated logo files in `docs/brand/`. Separate immutable sources from derived outputs. UI components consume the selected assets without taking ownership of their reconstruction sources.
3. Define how applications receive versioned brand artifacts from docs, separately from UI component releases. Record distribution choices in an architecture decision record (ADR).
4. Pin the frontend to known UI and brand artifact versions; copy selected public assets to their deployment location during the build. The handoff's `/brand` path is an example, not an existing production endpoint.
5. For a new brand release, record source hashes, derivatives, visible changes, and consumer impact. Retain the previous distribution for rollback.

**Plan proposal:** track the brand source version separately from the UI package version. A component fix may still use brand geometry v2.0. Distinguish compatible fixes, additive assets/APIs, and breaking changes in release notes. Geometry changes must never be presented as silent optimization.

Proposed UI structure, to refine after technology selection:

```text
ui/
  tokens/             # Values used by UI components
  src/brand/          # Actual logo/icon components consuming brand assets
  src/components/     # Components required by real product journeys
  examples/           # Developer and visual review catalog
  scripts/            # Component build and verification
```

This is a proposed structure, not a directory tree created by this documentation task.

## 4. Grow the design system from a small core

| Layer | Contents | Change rule |
| --- | --- | --- |
| Brand primitives | Source colors, font identities, established geometry | Trace to a brand source version |
| Semantic roles | Text, surfaces, control borders, focus, actions, error/success | Validate against actual surfaces and interactions |
| Component values | Button, input, label, helper text, notification, layout | Add as required by the first journey |

The handoff's JSON/CSS are starting references, not a complete shared production system. Prefer one editable token source that generates CSS and other consumer outputs. Keep proposal status visible. Evaluate a product namespace for tokens to avoid generic-name collisions.

Initial components: logo, standalone icon, text/heading styles, links, buttons, form fields, labels, help/error text, and status notifications. Add dialogs, tables, date pickers, and drag-and-drop builders when a real journey requires them.

Resolve theme preference in one frontend-owned place. Distinguish user preference from system preference and supply the same resolved theme to UI and brand components. The sample React `mode="auto"` follows the operating system only; it cannot represent a manual application override on its own. If SSR is chosen, verify the initial and hydrated theme remain consistent.

The first implementation can start with light mode. If the dark proposal is accepted, validate it on actual screens. Supporting monochrome brand assets does not automatically require a user-facing monochrome application theme.

## 5. Define the first product scope

Write the first product brief around one user, one problem, and one end-to-end outcome. Landing-page copy from the handoff is not a substitute for this decision.

**Candidate first journey, if the product direction is confirmed:** create a form draft → add a limited set of field types → preview → publish → submit a response → let an authorized user view it.

If selected, resolve these data boundaries early:

- Separate an editable draft from a published form version; retain the schema version associated with each response.
- Separate form definitions, response data, and presentation/theme settings.
- Enforce identity and permissions on the backend; hidden UI controls are not authorization.
- Define field types, validation rules, and API error shapes in an explicit shared contract.
- Decide whether the first audience is individuals or teams/workspaces before introducing tenancy into the model.

Uploads, payments, conditional logic, integrations, automations, custom domains, and a general application builder are not implicitly part of the first release. Scope each against user value and ongoing maintenance cost.

## 6. Implementation and growth strategy

**Plan proposal:** begin with one backend application with explicit module boundaries. Keep form definitions, publishing, and response processing distinct inside it. Evaluate independent services only when measurements or team ownership justify them. Do not preselect queues, search engines, or multi-region infrastructure without a demonstrated requirement.

Record data migrations, compatibility windows, and consumer versions with API/data changes. Keep the machine-readable API contract alongside the backend release; docs should link to and explain it rather than maintaining a divergent copy.

| Observed need | Change to evaluate |
| --- | --- |
| A second interface consumes the same components | Expand UI distribution and consumer compatibility coverage |
| Assets are repeatedly copied by hand | Centralize build/package distribution |
| Notifications or external calls delay user requests | Introduce background work with defined retry behavior |
| Measured queries become slow | Inspect queries/indexes first; add caching or a separate read model if justified |
| Teams need independent releases or modules need different scaling | Evaluate extracting the relevant service |
| Schema edits affect historical responses | Apply schema versioning and migration rules; establish the foundation in the first journey |

Before collecting real data, establish configuration/secrets handling, server-side validation, access boundaries, abuse limits, backups, and a restore exercise. Logs should support diagnosis without recording complete form responses by default. Define retention/deletion requirements against the actual users and data collected.

Initial measurements may include journey completion, submission failure rate, API latency, failed background jobs, and user drop-off. Establish baselines before claiming success thresholds or capacity.

## 7. Phases and exit criteria

Order reflects dependencies, not a delivery-time estimate. Owners below are roles, not assigned individuals.

| Phase | Deliverables | Exit criteria | Suggested owner |
| --- | --- | --- | --- |
| 0. Preserve the foundation | Source archive, extracted materials, brand reference, review, pre-plan | Source integrity verified; established decisions separated from proposals | Documentation + brand |
| 1. Define product and technical foundations | First user/journey, MVP exclusions, stack and distribution ADRs | One written journey and success measure; dependencies identified | Product + technical lead |
| 2. Establish brand and UI core | Versioned assets, tokens, logo/icon adapters, small catalog | Geometry checks, theme/narrow-screen acceptance, consumer build | Brand/UI + frontend |
| 3. Complete the first vertical journey | Frontend, API, and persistence for the selected journey | Real end-to-end outcome; access boundaries and failure paths verified | Frontend + backend |
| 4. Prepare the first release | Deployment, observability, backup/rollback, platform assets | Target-environment acceptance and recovery exercise recorded | Technical + product |
| 5. Grow from evidence | Features and capacity changes driven by usage | Each addition has a demonstrated need, owner, and acceptance criterion | Product + module owner |

Phase 0 documentation and source preservation are delivered here. This does not accept every handoff proposal or complete application integration.

## 8. Initial actionable backlog

| Priority / ID | Task | Dependencies | Completion evidence |
| --- | --- | --- | --- |
| P0 / TF-001 | Define the initial user and problem | None | One-page product brief; current versus planned capabilities |
| P0 / TF-002 | Select the first journey and exclusions | TF-001 | Start/end, failure cases, and success measurement documented |
| P0 / TF-003 | Decide stack, distribution, and repository boundaries | TF-002 | ADR with ownership and consumption method |
| P0 / TF-004 | Define UI/application consumption of brand artifacts from docs | TF-003 | Source ownership stays in docs; asset mapping and version consumption validated |
| P0 / TF-005 | Establish token source and theme contract | TF-004 | Consistent generated outputs; proposal/acceptance status tracked |
| P0 / TF-006 | Build logo/icon usage catalog | TF-004, TF-005 | B/A, modes, actual small sizes, manual theme behavior verified |
| P1 / TF-007 | Implement first form components and state roles | TF-002, TF-005 | Label, help, error, loading, disabled, and focus behavior defined |
| P1 / TF-008 | Define data model and API contract | TF-002, TF-003 | Schema versions, access model, and error shapes illustrated |
| P1 / TF-009 | Complete the first end-to-end journey | TF-006, TF-007, TF-008 | UI → API → persistence → user outcome verified |
| P1 / TF-010 | Complete release and operational acceptance | TF-009 | Target-environment testing, restore, and release rollback recorded |

These IDs are document-local planning references, not tasks created in an external tracker. TF-006 and TF-008 can progress independently once their own dependencies are satisfied.

## 9. Quality gates

| Layer | Verification | Evidence |
| --- | --- | --- |
| Brand source | SHA-256, paths/transforms/viewBox/stroke, A/B and monochrome integrity | Automated report and source version |
| Generated assets | SVG structure, PNG dimensions, font and asset paths | Build artifact inspection |
| UI | Actual-size readability, surfaces, theme, keyboard, accessible names | Catalog and browser review record |
| Product | Selected journey, empty/loading/error states, access boundaries | Meaningful integration and end-to-end tests |
| Release | Deployment paths, caching, target environment, rollback | Release acceptance record |

Suggested brand matrix: A/B × color/dark/mono/black/white, plus inline currentColor. Inspect horizontal logos at 200/240/280 px, icons at 24/32 px, and favicons at 16/32 px in actual contexts. Treat 160 px logos as stress cases. Start viewport checks at 320 px and at least one wide-screen size; finalize browser/platform coverage in the product decisions.

PWA installation, email clients, print, and animation require separate acceptance only when those surfaces are in scope. Passing source validation is distinct from passing browser, device, or product-journey testing.

## 10. Decisions and documentation maintenance

Record substantial decisions under `decisions/NNNN-short-title.md` when needed. Each ADR should include context, options, decision, rationale, consequences, status, date, and source version. Suggested statuses: `proposed`, `accepted`, `superseded`. Preserve superseded decisions and link to replacements.

Update documentation with the change that alters behavior. Brand changes involve the brand owner; API changes involve backend and consumer owners; scope changes involve the product owner. One person may hold several roles in a small team.

| Open decision | Needed by | Interim position |
| --- | --- | --- |
| Initial audience and product scope | Phase 1 | Do not infer a complete product from brand materials |
| First release: marketing/demo or functioning form product? | Phase 1 | Do not turn proposed landing copy into availability claims |
| Frontend/backend stack and hosting | Before scaffolding | The TSX sample does not mandate React |
| UI package distribution/access | Phase 2 | Target reproducible, versioned consumption |
| Individual versus team/workspace model | Before data modeling | Do not assume multi-tenancy |
| Product language and localization | Before initial screens | English documentation does not select the product language |
| Dark theme and proposed usage sizes | Relevant UI acceptance | Keep source-proposal status until accepted |
| Response retention and deletion | Before real-data collection | Define against the target use case |

The first implementation cycle should make TF-001 through TF-006 concrete. Complete an actual product journey before expanding into a large speculative component library or advanced infrastructure.
