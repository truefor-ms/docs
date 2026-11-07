# Trueforms documentation

Trueforms is a form-focused SaaS. This documentation records the confirmed direction and the path to implementation. Runtime implementation has not started here.

## Confirmed decisions

- `ui` contains **TrueUI**, the common UI library.
- `frontend` contains the application and frontend business logic.
- `backend` contains backend operations and authoritative business logic.
- `docs` contains specifications, plans and brand sources.
- Build TrueUI first to standalone readiness for both Form UI and Form Builder UI. Frontend/backend implementation starts only after the readiness gate is accepted.
- App subscriptions and billing start in the first application phase after TrueUI readiness.
- Payment collection inside forms is a separate end-to-end work package.
- Maintained logo documentation starts at **v1.0**. Original supplied materials stay unchanged.
- Documentation is English. Reports and guides are delivered as HTML.

## Implementation path

Start with the [Build path](planning/saas-implementation-plan.md) and the [TrueUI implementation sequence](planning/trueui-implementation.md). After TrueUI readiness is accepted, use the separate [Form UI](planning/respondent-ui-build-order.md) and [Form Builder UI](planning/form-builder-ui-build-order.md) sequences. [Form payments](planning/form-payment-fields.md) has its own delivery boundary.

The [Field reference](reference/fields.md) and [Component ownership](reference/components.md) retain the detailed contracts needed during implementation. They describe planned scope, not shipped features.

## Reference and working rules

- [Logo v1.0](brand/logo/README.md)
- [Original materials](brand/README.md)
- [Contribution rules](contributing/README.md): Conventional Commits, required author/committer identity and pushes only as `formtrue`.
- [Documentation standard](contributing/documentation.md)

## Open decisions

Stack, hosting, initial audience, launch field subset, supported locales, plan/pricing details and operational targets still require explicit decisions. Broad capability inventories do not approve every feature for launch.

## Documentation maintenance

The current docs replace exploratory marketplace research and the superseded pre-plan. Useful field contracts and build sequences remain; original brand materials and verification records are preserved. Open [index.html](index.html) for the documentation interface.
