# Form UI

**Updated:** 7 November 2026. **Status:** implementation preparation; no runtime components implemented. This surface is the form filled in by a respondent, including embedded forms. It is separate from the [builder UI plan](form-builder-ui-build-order.md).

This sequence translates the existing [field inventory](../reference/fields.md) and [SaaS plan](saas-implementation-plan.md) into dependency-ordered work. Component names are proposed contracts, not selected framework APIs. Deferred capabilities remain in the inventory.

## Ownership and prerequisites

**U = TrueUI:** reusable controls, accessible interaction and visual states. **F = frontend:** schema renderer, respondent session, validation timing, navigation and submission flow. **B = backend dependency:** published schema, authoritative validation, access and durable writes. Backend dependencies are prerequisites, not UI components.

Before RUI-01, agree on stable field/option IDs, versioned field schema, value types, error paths, supported locales, access states and submit/idempotency contract. A renderer should not invent these while being built. Mock fixtures may unblock component work; the first usable milestone still requires a real backend.

## Ordered implementation backlog

Build rows in order unless their dependencies permit parallel work. The initial slice ends at RUI-08. Build complex fields in vertical batches rather than implementing every control before one working submission.

| Order / ID | Components to implement | Owner | Depends on | Completion evidence |
| --- | --- | --- | --- | --- |
| 01 / RUI-01 | Semantic tokens, Text, Heading, Link, Icon, Logo, Stack, Container, Divider, Button, Spinner, Alert | U | Schema/API agreement for consumers | Focus, contrast, pending state, narrow layout and long text examples |
| 02 / RUI-02 | FormField, FieldLabel, FieldDescription, FieldError, FieldGroup, RequiredIndicator, ErrorSummary | U | RUI-01 | IDs associate label/help/error; summary links focus the correct control; required meaning is explicit |
| 03 / RUI-03 | TextInput, Textarea, EmailInput, NumberInput, Select, RadioGroup, Checkbox, CheckboxGroup | U | RUI-02 | Empty/invalid/readonly/disabled; zero/false preserved; keyboard group behavior; field-map F01–F03,F06,F08–F11 |
| 04 / RUI-04 | FormShell, FormHeader, ContentBlock, FieldRenderer, FieldList, UnsupportedFieldState | F using U | RUI-03 + versioned schema | Schema order and stable IDs preserved; unknown type produces recoverable error; safe content rendering |
| 05 / RUI-05 | FormValues controller, ValidationPresenter, SubmissionErrorPanel | F using U | RUI-04 + error contract | Client errors and server field/global errors map correctly; typed values retained; focus moves after failed submit |
| 06 / RUI-06 | SubmitBar, PendingSubmission, RetryAction, SubmissionReceipt, CompletionScreen | F using U | RUI-05 + durable submit API | Success only after acceptance; double click/retry does not duplicate; timeout with unknown outcome reconciles |
| 07 / RUI-07 | FormLoading, UnavailableForm, ClosedForm, ScheduledForm, AccessDenied, ExpiredLink, OfflineNotice | F using U | RUI-04,RUI-06 + access states | Distinct causes and recovery; expired/closed form never silently discards entered values |
| 08 / RUI-08 | PublishedFormRoute, EmbeddedFormShell, ResponsiveFormLayout | F | RUI-04–07 + publication API | Real published form can be completed by keyboard/mobile and reviewed by an authorized owner; embed integration may follow standalone route |
| 09 / RUI-09 | TelephoneInput, URLInput, SearchableSelect, MultiSelect, TagInput, ChoiceCard, NameGroup, AddressGroup | U controls; F domain grouping | RUI-02–05 + option data contracts | Async options handle stale responses and failure; country/name assumptions explicit; F04–F05,F13–F14,F26–F27,F43 |
| 10 / RUI-10 | DateInput, TimeInput, DateTimeInput, DateRangeInput, Rating, OpinionScale, Slider | U; F value adapters | RUI-02–05 + date/value policy | Date versus instant distinguished; bounds/locale handled; unanswered distinct from default; F16–F19,F23–F25 |
| 11 / RUI-11 | FilePicker, Dropzone, UploadQueue, FileItem, UploadProgress, FilePreview, ScanStatus, Cancel/Retry | U presentation; F upload coordinator | RUI-06 + storage/scan/finalization APIs | Invalid/oversize/scanning/rejected states; retry/cancel; authorized file association; F21–F22 |
| 12 / RUI-12 | FormPage, PageTitle, ProgressIndicator, PreviousNextBar, ReviewAnswers | F using U Stepper | RUI-05–06 + page schema | Back preserves input; next validates current page; review links return focus; F47 |
| 13 / RUI-13 | ConditionalField, ConditionalPage, BranchNavigation, DependentChoice | F | RUI-09,RUI-12 + shared rule contract | Hidden-field policy matches server; loops/invalid references blocked; no stranded page/focus; F15 |
| 14 / RUI-14 | PrefillAdapter, HiddenValueAdapter, MaskedInput, InputAffix, CharacterCounter | F adapters; U decorators | RUI-05 + trust/normalization policy | URL/hidden values untrusted; display mask differs from persisted value; F35,F41 |
| 15 / RUI-15 | ResumePrompt, SaveProgressStatus, ResumeLinkState, PartialResponseNotice | F using U | RUI-12–13 + resume/retention APIs | Session/token expiry and cross-device resume handled; partial-data collection explicit |
| 16 / RUI-16 | MatrixField, RankingField, RepeatableGroup, AddRemoveItemBar, CalculatedValue | F compositions; U reusable controls | RUI-13 + advanced schema validators | Keyboard reorder; stable repeated-item IDs; limits/cycles; server recomputes calculations; F31–F34 |
| 17 / RUI-17 | RichTextAnswer, MonthInput, WeekInput, TransferList, LocationInput | U adapters; F contracts | RUI-09–10 + content/provider policies | Restricted content, manual location fallback, accessible alternatives; F20,F28–F29,F42 |
| 18 / RUI-18 | AmountInput, SignatureField, SignatureReview | U amount control; F signature integration | RUI-06 + numeric/signature contracts | Amount entry does not charge money; signature policy established; F07,F30 |
| 19 / RUI-19 | AccessGate, PasswordEntry, VerificationCode, ChallengeAdapter | F flows using U | RUI-07 + authentication/abuse policy | Accessible retries and expiry; backend checks proof; public forms never collect account passwords as ordinary answers; F37–F38,F45 |
| 20 / RUI-20 | LanguageSelector, ThemeBoundary, LongFormNavigation, MediaContent, PrintResponseView | F compositions using U | RUI-08,RUI-12 + locale/theme contracts | Long labels, chosen RTL policy, zoom, captions, theme contrast and separate print checks |

RUI-19 is conditionally pulled forward: if the first release requires a gated form or challenge, it blocks RUI-08. Basic server abuse controls already block public release regardless of whether a challenge widget is used. Similarly, localization and theme acceptance from RUI-20 apply from the first slice for every supported locale/theme; optional selectors/media/print can follow later.

## Shared state contract

Field state: value, error, dirty/touched, enabled/readonly, visible and pending asynchronous work. Form state: loading, ready, validating, submitting, accepted, rejected or unknown outcome. Unknown outcome is not automatically a fresh submission. Keep form access state separate from submission state.

Use the same frontend renderer and field registry for builder preview and published forms. Pass schema, version, resolved theme, locale and explicit preview/live mode. Preview must use an inert submission adapter; live mode requires authorized backend contracts. TrueUI receives props and callbacks rather than knowing a form endpoint or workspace.

## Start-building checklist and first milestone

The first implementation batch is RUI-01–03 with fixtures; the next is RUI-04–07 with a real published schema and response API. Connect RUI-08 after those states work. Do not wait for all 47 families.

The initial milestone passes only when a published form accepts a valid response, shows actionable invalid/server errors without losing values, survives a repeated submission safely, displays closed/unavailable states, and supports keyboard/narrow-screen use. Confirm schema version and stored answers through backend evidence, not a success toast alone. The [builder's first milestone](form-builder-ui-build-order.md#first-milestone-and-integration-order) produces the schema consumed here.
