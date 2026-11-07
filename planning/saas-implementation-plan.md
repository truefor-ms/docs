# Build path

**Updated:** 7 November 2026. **Status:** agreed direction with proposed implementation stages. No delivery dates or technology choices are implied.

## 1. Set the contracts

Decide the first audience and form journey, frontend/backend stack, hosting and TrueUI distribution. Specify stable field/option IDs, draft revisions, immutable published versions, answer types, API errors, workspace ownership and capabilities. Agree on initial locales, limits and recovery objectives.

**Exit:** documented contracts and valid/invalid fixtures for one form journey. Workspace roles, launch scope and pricing are decisions to make, not already approved specifications.

## 2. Build TrueUI to standalone readiness

Follow the [TrueUI implementation sequence](trueui-implementation.md) for component work packages and cross-surface examples.

**Confirmed sequencing:** TrueUI is the first implementation project. Build the reusable components needed by both Form UI and Form Builder UI in `ui`. Do not start implementation in `frontend` or `backend` until TrueUI passes the readiness gate below. Planning and interface contracts may be documented beforehand; they are not application implementation.

Use the two surface plans as requirements inputs. Build tokens and primitives first, then field controls and feedback, then overlays/navigation, then reusable builder layout and editing interactions. Include advanced reusable controls required by the agreed initial surfaces; a handful of basic inputs is not sufficient readiness.

Demonstrate both surfaces in the standalone TrueUI catalog using fixtures, controlled state and callbacks. Examples should exercise form completion, property-panel editing, option lists, selection/reordering, validation presentation and save/conflict feedback without implementing a product schema engine, real persistence, authentication or billing inside TrueUI.

### TrueUI readiness gate

- Map every reusable requirement for the agreed initial Form UI and Form Builder UI scope to a component, documented composition or explicitly deferred capability. Record deferrals; do not silently narrow the scope to pass the gate.
- Complete component APIs, controlled state/callback contracts, variants and relevant empty/loading/error/disabled/readonly states.
- Verify keyboard navigation, focus, labels/errors, narrow-screen layouts, long content and supported themes/locales in both representative catalog compositions.
- Provide runnable standalone examples and meaningful interaction/regression checks. Product flows are simulated with fixtures; backend acceptance is not claimed.
- Produce a versioned consumable library artifact and verify it in an isolated consumer fixture, without starting the frontend application.
- Record the readiness review, evidence, outstanding limitations and explicit acceptance. Until accepted, both application repositories remain outside implementation scope.

**Exit:** TrueUI independently supports the agreed two-surface scope with documented evidence. Readiness does not mean every future field or payment integration is finished; form payment fields retain their separate package. The readiness review has not yet occurred.

## 3. Begin application foundations and subscriptions

After TrueUI readiness is accepted, establish identity, workspace authorization, migrations, deployment and diagnostic events in the application repositories. Implement app plans, trial, subscription checkout, invoice/payment-method access, changes/cancellation and entitlement rules in this first application phase.

**Exit:** an authorized account owns a workspace; subscription lifecycle works in provider test mode; entitlements and tenant isolation are enforced on the backend. App billing starts early in application development, but does not run in parallel with the initial TrueUI build or wait for form payment fields.

## 4. Complete the first form journey

Develop the [Form UI](respondent-ui-build-order.md) and [Form Builder UI](form-builder-ui-build-order.md) from the same schema contract. Start with text, email, number and choices. Build editing, keyboard reordering, save/conflict recovery, preview, atomic publication, public completion and response list/detail.

**Exit:** create → preview → publish → submit → inspect a persisted response → close collection. Failed saves and submissions preserve values; retries do not duplicate responses; historical answers retain their published schema version. Restore, access checks and abuse controls are required before real-data collection.

## 5. Expand the usable form product

Add common field types in matched batches: control, builder settings, serializer, runtime renderer, client/server validation and response/export formatter. Add files, pages, themes, sharing/embed, invitations, response filters/export, notifications and retention controls.

**Exit:** representative contact, registration, feedback and file-intake forms work end to end. Every enabled field has a complete contract; frontend hiding is never authorization.

## 6. Validate SaaS release readiness

Validate the subscription implementation from stage 3, quota enforcement, upgrades/downgrades/cancellation and recovery from delayed or repeated provider events. Complete account/security settings, support/onboarding, audit access, operational monitoring, backup/restore and deployment rollback.

**Exit:** acceptance evidence covers both the normal journeys and failure/recovery paths. Launch claims match implemented functionality. Specific capacity, availability and data policies are agreed and tested.

## 7. Extend from the retained backlog

Branching, repeaters, matrices, calculations, save/resume, integrations, API/webhooks, automation and advanced response exploration follow their prerequisites. Keep dependencies optional in TrueUI. Specialized capabilities remain planned until their use case and full contract are specified.

**Exit for each addition:** an owner, defined behavior, server enforcement, failure handling and acceptance evidence. Do not equate a working settings screen with a completed capability.

## Separate work package: form payments

[Form payments](form-payment-fields.md) owns payment collection inside forms: builder settings, respondent payment controls, provider events, response association and operational recovery. It is outside the ordinary form-component build sequence. App subscriptions begin in stage 3, after the TrueUI readiness gate. Generic amount entry is not payment collection.

## Ownership

| Area | Owner | Boundary |
| --- | --- | --- |
| Shared presentation and interaction | TrueUI / `ui` | No product endpoints or business decisions |
| Screens, builder and respondent flow | `frontend` | Orchestrates API calls; does not enforce authoritative permissions |
| Validation, access, publication, responses and billing | `backend` | Authoritative persistence and domain rules |
| Specifications and brand sources | `docs` | No runtime application implementation |

## Release checks

- Keyboard, focus, narrow layouts and clear loading/error/empty states.
- Cross-workspace denial, revoked access and authorized file downloads.
- Draft conflicts, schema changes and historical response/export integrity.
- Duplicate submits, timeouts after successful writes and safe reconciliation.
- File validation/scan/retry, safe exports and retention/deletion handling.
- Subscription event replay, quota races and downgrade behavior.
- Deployment rollback, database/file restore and diagnosable failed jobs.

## Start here when implementation begins

1. Define the initial two-surface requirements and library contracts.
2. Implement and validate TrueUI independently using its catalog and fixtures.
3. Record acceptance of the TrueUI readiness gate before starting frontend/backend implementation.
4. Build application identity/workspace and subscriptions, then integrate form rendering and builder editing using the ready library.
5. Connect preview, publication and submission; complete the first product journey before expanding application scope.

Use [Fields](../reference/fields.md) and [Component ownership](../reference/components.md) for detailed planned scope. The surface plans define local work-package order; this document defines the product delivery path.
