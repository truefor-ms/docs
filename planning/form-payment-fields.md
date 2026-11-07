# Form payment fields

**Updated:** 6 November 2026. **Status:** separate future work package, PAY-F. This scope decision is confirmed; provider, timing and detailed payment behavior remain open.

## Scope boundary

This package owns **payment collection inside forms (F36)**, including respondent payment controls, builder configuration and backend processing. It is excluded from the ordinary [respondent](respondent-ui-build-order.md) and [builder](form-builder-ui-build-order.md) component sequences and will be delivered as its own end-to-end package.

**App subscription and billing are not part of this package.** SaaS plans, trials, subscription checkout, invoices, payment methods, cancellation and entitlements remain in the initial implementation process in the first application phase after TrueUI readiness (stage 3 of the [Build path](saas-implementation-plan.md)). Sharing a provider would not merge their domain models or release gates.

F07, a generic amount/currency input, stays in the normal field inventory. Entering an amount does not initiate a payment. Payment-specific totals, charge validation and transaction state belong here.

## Delivery order within PAY-F

| ID | Work | Ownership | Dependency / completion criterion |
| --- | --- | --- | --- |
| PAY-F-01 | Define recipient/merchant model, supported currencies, amount source, payment timing and refund policy | Product + backend | Decide whether payment precedes response acceptance, follows it or uses a separate pending state; no implicit policy |
| PAY-F-02 | Define payment schema, transaction/response association, provider adapter and state contract | Backend + frontend | Requires stable published-form versions and response IDs; server owns amounts and allowed transitions |
| PAY-F-03 | Implement provider session creation, verified events, idempotency, reconciliation and audit records | Backend | Duplicate/out-of-order events and unknown outcomes handled; credentials and raw card data excluded from form answers |
| PAY-F-04 | Build PaymentFieldSettings, AmountRuleSettings, CurrencySettings, PaymentConnectionStatus and schema diagnostics | Frontend using TrueUI | Invalid or disconnected payment configuration blocks publication; test/live configuration explicit |
| PAY-F-05 | Build PaymentSummary, provider-hosted PaymentStep, PaymentPending, PaymentFailure, PaymentRetry and PaymentReceipt | Frontend using TrueUI | Respondent state follows verified backend state, not a redirect URL; cancellation and retry preserve intended response |
| PAY-F-06 | Add payment status to response detail/export and implement refund/support operations | Frontend + backend | Scoped authorization and auditable changes; response status and payment status remain distinct |
| PAY-F-07 | Validate and release the complete package | Frontend + backend + operations | Test success, decline, cancel, timeout, duplicate/reordered events, expired session, refund and provider outage |

Dependencies are the existing form schema/renderer, publication, submission, response management, authorization, secrets and background-job infrastructure. The package can reuse generic TrueUI controls but must not put payment business logic in TrueUI.

## Release boundary

Keep F36 unavailable in the builder palette until configuration, respondent UI, backend validation, event handling, response presentation and operational recovery are ready together. Preview/test mode must not create live charges. Account subscription development and ordinary form creation/submission continue independently while this package is deferred.
