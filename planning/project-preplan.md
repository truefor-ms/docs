# Trueforms project pre-plan

**Updated:** 5 November 2026 · **Status:** planning; repository responsibilities confirmed, implementation choices open · **Basis:** brand handoff v2.0, confirmed project decisions, and repository READMEs.

## 1. Objective and scope

Build a product foundation that can grow while preserving the established brand. Start with versioned brand assets, a small shared UI foundation, and one verifiable product journey. Expand the component library and infrastructure in response to actual usage.

The handoff is a substantial **brand and integration specification**, not a product requirements document. It mentions form and application creation, but does not settle user roles, the data model, pricing, hosting, or launch scope. The product journey below is therefore a proposal. No technology stack, delivery schedule, or capacity commitment is established here.

Documentation, brand preservation, logo reconstruction, and repository responsibility READMEs are in place. TrueUI components and frontend/backend application implementations remain future work. No framework, package identifier, or release process has been selected by this plan.

## 2. Confirmed repository responsibilities

The project uses four separate repositories. Their responsibilities are confirmed; repository count does not imply service count. **TrueUI** is the name of the common UI library maintained in `ui`, not the name of the frontend application or a claim that a package is already published.

| Repository | Confirmed responsibility | Boundary |
| --- | --- | --- |
| `docs` | Product scope, brand originals, reconstruction sources/scripts/outputs, decisions, contract explanations, review records | Not a runtime asset server |
| `ui` / **TrueUI** | Common UI components, reusable presentation and interaction behavior, component tokens/themes, accessibility, and examples | No frontend/backend business logic, application API orchestration, logo source archive, or reconstruction tooling |
| `frontend` | Frontend application code and frontend business logic: pages, navigation, feature state, user journeys, and API orchestration | Consumes TrueUI; does not enforce authoritative backend rules or own logo masters |
| `backend` | Backend operations and backend business logic: authoritative validation, authorization, domain behavior, persistence, integrations, and API contracts | No frontend workflow orchestration, UI presentation, or logo construction |

Dependency direction: the frontend consumes TrueUI components and the backend API contract. TrueUI receives data, state, and callbacks through component APIs; it does not depend on the frontend application or a particular backend service. Frontend business logic coordinates client-side workflows. Backend business logic remains authoritative for permissions and stored data, including requests made outside the normal interface.

Repository entry points: [TrueUI](https://github.com/truefor-ms/ui), [frontend](https://github.com/truefor-ms/frontend), and [backend](https://github.com/truefor-ms/backend). These README boundaries apply to the implementation proposals below.

Sibling directories may be convenient during development, but a release must not require a developer's `../ui` directory. Establish reproducible package or artifact consumption. Consider a monorepo only after recording the actual cost of cross-repository changes and the trade-offs of migration.

## 3. From source artwork to product

Proposed flow: **preserved handoff and reconstruction in docs → validated brand artifacts → frontend consumption through TrueUI components where appropriate → acceptance on actual surfaces**.

1. Keep the original ZIP and complete extracted package accessible through the [brand hub](../brand/README.md), with hashes and provenance.
2. Keep approved artwork, notices, font inputs, reconstruction scripts, and generated logo files in `docs/brand/`. Separate immutable sources from derived outputs. A TrueUI logo-rendering component may consume selected assets; their source ownership stays in docs.
3. Define how applications receive versioned brand artifacts from docs, separately from TrueUI component releases. Record distribution choices in an architecture decision record (ADR).
4. Pin the frontend to known TrueUI and brand artifact versions once distribution is implemented; copy selected public assets to their deployment location during the build. The handoff's `/brand` path is an example, not an existing production endpoint.
5. For a new brand release, record source hashes, derivatives, visible changes, and consumer impact. Retain the previous distribution for rollback.

**Plan proposal:** track the brand source version separately from the TrueUI package version. A component fix may still use brand geometry v2.0. Distinguish compatible fixes, additive assets/APIs, and breaking changes in release notes. Geometry changes must never be presented as silent optimization.

Proposed TrueUI structure, to refine after technology selection:

```text
ui/                   # TrueUI common UI library
  README.md           # Library purpose and responsibility boundaries
  tokens/             # Shared component/theme values
  src/components/     # Reusable UI components, including brand renderers if needed
  examples/           # Isolated component usage and visual review
  scripts/            # Component build and verification
```

This is a proposed structure, not a directory tree created by this documentation task.

## 4. Build TrueUI from a small shared core

TrueUI owns reusable UI behavior, such as keyboard navigation, focus management, selection, and open/closed state. It does not decide product workflows, make feature-specific API calls, or implement frontend/backend business rules. The frontend supplies the application state and handlers; the backend enforces server-side rules.

For example, TrueUI can provide a form field that displays a label and error message. The frontend decides when to show that error and how to coordinate submission; the backend validates the request and applies its business rules. A form-builder screen belongs to the frontend, while reusable controls used by that screen may belong to TrueUI.

| Layer | Contents | Ownership and change rule |
| --- | --- | --- |
| Brand reference | Source colors, font identities, established geometry | Sources and reconstruction stay in docs; consumers trace to a brand version |
| Shared UI tokens and semantic roles | Text, surfaces, control borders, focus, actions, error/success presentation | TrueUI; validate against actual surfaces and interactions |
| Reusable components | Button, input, label, helper text, notification, layout | TrueUI; add reusable APIs as product journeys require them |
| Application composition | Screens, feature state, validation timing, and submission flows | Frontend code and frontend business logic |
| Authoritative operations | Permissions, data integrity, and domain behavior | Backend operations and backend business logic |

The handoff's JSON/CSS are starting references, not a complete shared production system. Prefer one editable source for TrueUI component tokens that generates consumer outputs, with traceable mappings to the brand reference in docs. Keep proposal status visible. Evaluate a product namespace for tokens to avoid generic-name collisions.

Candidate initial components: buttons, links, form fields, labels, help/error presentation, status notifications, text/heading styles, and logo/icon renderers where needed. Add dialogs, tables, date pickers, or reusable drag-and-drop interactions when a real journey requires them. Feature-specific builders and their business decisions remain in the frontend.

Resolve the application's theme preference in one frontend-owned place. TrueUI provides the shared theme presentation and accepts the resolved preference. Supply the same theme to its components and brand renderers. The sample React `mode="auto"` follows the operating system only; it cannot represent a manual application override on its own. If SSR is chosen, verify the initial and hydrated theme remain consistent.

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
| A second interface consumes the same components | Expand TrueUI distribution and consumer compatibility coverage |
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
| 2. Establish TrueUI and brand consumption | Shared components/tokens/catalog in TrueUI; selected brand artifacts supplied from docs | Component API and interaction checks, theme/narrow-screen acceptance, frontend consumer build | TrueUI + brand + frontend |
| 3. Complete the first vertical journey | Frontend code and business logic integrated with backend operations and business logic | Real end-to-end outcome; access boundaries and failure paths verified | Frontend + backend |
| 4. Prepare the first release | Deployment, observability, backup/rollback, platform assets | Target-environment acceptance and recovery exercise recorded | Technical + product |
| 5. Grow from evidence | Features and capacity changes driven by usage | Each addition has a demonstrated need, owner, and acceptance criterion | Product + module owner |

Phase 0 documentation and source preservation are delivered here. This does not accept every handoff proposal or complete application integration.

## 8. Initial actionable backlog

| Priority / ID | Task | Dependencies | Completion evidence |
| --- | --- | --- | --- |
| P0 / TF-001 | Define the initial user and problem | None | One-page product brief; current versus planned capabilities |
| P0 / TF-002 | Select the first journey and exclusions | TF-001 | Start/end, failure cases, and success measurement documented |
| P0 / TF-003 | Select stack and distribution within the confirmed repository boundaries | TF-002 | ADR records implementation choices and the TrueUI consumption method |
| P0 / TF-004 | Define frontend/TrueUI consumption of brand artifacts from docs | TF-003 | Source ownership stays in docs; asset mapping and version consumption validated |
| P0 / TF-005 | Establish TrueUI token source and application theme contract | TF-004 | Consistent outputs; frontend-owned preference; proposal/acceptance status tracked |
| P0 / TF-006 | Build an isolated TrueUI component catalog, including brand usage | TF-004, TF-005 | Reusable APIs and interaction states demonstrated; chosen logo modes/sizes verified |
| P1 / TF-007 | Implement reusable form components in TrueUI | TF-002, TF-005 | Label, help, error, loading, disabled, and focus behavior defined; feature business logic stays in frontend/backend |
| P1 / TF-008 | Define data model and API contract | TF-002, TF-003 | Schema versions, access model, and error shapes illustrated |
| P1 / TF-009 | Compose the first journey in frontend and implement its backend rules | TF-006, TF-007, TF-008 | TrueUI components → frontend business logic → backend operations/business logic → persisted result verified |
| P1 / TF-010 | Complete release and operational acceptance | TF-009 | Target-environment testing, restore, and release rollback recorded |

These IDs are document-local planning references, not tasks created in an external tracker. TF-006 and TF-008 can progress independently once their own dependencies are satisfied.

## 9. Quality gates

| Layer | Verification | Evidence |
| --- | --- | --- |
| Brand source | SHA-256, paths/transforms/viewBox/stroke, A/B and monochrome integrity | Automated report and source version |
| Generated assets | SVG structure, PNG dimensions, font and asset paths | Build artifact inspection |
| TrueUI | Reusable component contracts, interaction states, theme, keyboard, accessible names | Isolated component checks and catalog/browser review record |
| Frontend integration | Component composition, client-side business flows, API orchestration, and actual-size brand readability | Application browser and integration review record |
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
| TrueUI framework, package identifier, and distribution/access | Phase 2 | Library name and ownership are confirmed; implementation and publishing choices remain open |
| Individual versus team/workspace model | Before data modeling | Do not assume multi-tenancy |
| Product language and localization | Before initial screens | English documentation does not select the product language |
| Dark theme and proposed usage sizes | Relevant UI acceptance | Keep source-proposal status until accepted |
| Response retention and deletion | Before real-data collection | Define against the target use case |

The first implementation cycle should make TF-001 through TF-006 concrete. Complete an actual product journey before expanding into a large speculative component library or advanced infrastructure.
