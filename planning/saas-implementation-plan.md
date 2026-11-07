# Build path

**Updated:** 7 November 2026. **Status:** agreed direction with proposed implementation stages. No delivery dates or technology choices are implied.

## 1. Set the contracts

Decide the first audience and form journey, frontend/backend stack, hosting and TrueUI distribution. Specify stable field/option IDs, draft revisions, immutable published versions, answer types, API errors, workspace ownership and capabilities. Agree on initial locales, limits and recovery objectives.

**Exit:** documented contracts and valid/invalid fixtures for one form journey. Workspace roles, launch scope and pricing are decisions to make, not already approved specifications.

## 2. Build the shared foundation and subscriptions

Build TrueUI tokens, typography, layout, buttons, field wrappers and basic controls. Establish identity, workspace authorization, migrations, deployment and diagnostic events. Implement app plans, trial, subscription checkout, payment-method/invoice access, changes/cancellation and entitlement rules in this initial phase.

**Exit:** an authorized account owns a workspace; subscription lifecycle works in provider test mode; entitlements and tenant isolation are enforced on the backend. App billing does not wait for form payment fields.

## 3. Complete the first form journey

Develop the [Form UI](respondent-ui-build-order.md) and [Form Builder UI](form-builder-ui-build-order.md) from the same schema contract. Start with text, email, number and choices. Build editing, keyboard reordering, save/conflict recovery, preview, atomic publication, public completion and response list/detail.

**Exit:** create → preview → publish → submit → inspect a persisted response → close collection. Failed saves and submissions preserve values; retries do not duplicate responses; historical answers retain their published schema version. Restore, access checks and abuse controls are required before real-data collection.

## 4. Expand the usable form product

Add common field types in matched batches: control, builder settings, serializer, runtime renderer, client/server validation and response/export formatter. Add files, pages, themes, sharing/embed, invitations, response filters/export, notifications and retention controls.

**Exit:** representative contact, registration, feedback and file-intake forms work end to end. Every enabled field has a complete contract; frontend hiding is never authorization.

## 5. Validate SaaS release readiness

Validate the subscription implementation from stage 2, quota enforcement, upgrades/downgrades/cancellation and recovery from delayed or repeated provider events. Complete account/security settings, support/onboarding, audit access, operational monitoring, backup/restore and deployment rollback.

**Exit:** acceptance evidence covers both the normal journeys and failure/recovery paths. Launch claims match implemented functionality. Specific capacity, availability and data policies are agreed and tested.

## 6. Extend from the retained backlog

Branching, repeaters, matrices, calculations, save/resume, integrations, API/webhooks, automation and advanced response exploration follow their prerequisites. Keep dependencies optional in TrueUI. Specialized capabilities remain planned until their use case and full contract are specified.

**Exit for each addition:** an owner, defined behavior, server enforcement, failure handling and acceptance evidence. Do not equate a working settings screen with a completed capability.

## Separate work package: form payments

[Form payments](form-payment-fields.md) owns payment collection inside forms: builder settings, respondent payment controls, provider events, response association and operational recovery. It is outside the ordinary form-component build sequence. App subscriptions remain in stage 2. Generic amount entry is not payment collection.

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

1. Resolve stage 1 decisions and schema/API fixtures.
2. Build shared TrueUI controls once, alongside identity/workspace and subscription foundations.
3. Develop form rendering and builder editing in parallel against the same contract.
4. Connect preview, publication and submission; demonstrate the complete first journey before expanding fields.

Use [Fields](../reference/fields.md) and [Component ownership](../reference/components.md) for detailed planned scope. The surface plans define local work-package order; this document defines the product delivery path.
