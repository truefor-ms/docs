# Field reference

Planned field contracts. No runtime implementation is implied.

The [TrueUI readiness gate](../planning/saas-implementation-plan.md#trueui-readiness-gate) governs execution: implement the reusable scope required by both initial surfaces in TrueUI before starting frontend/backend application work. Phase labels below describe capability priority, not parallel application implementation.

## Common field contract

Every answer-bearing field has a stable ID, type and type version, label, description, required flag, constraints, default policy, option IDs where relevant, and presentation settings separated from stored values. Labels are editable; IDs are not derived from labels. Preserve the published schema version with each response. Unknown types must fail publication safely and render a recoverable incompatibility state, not disappear.

TrueUI owns label/help/error association, keyboard/focus behavior, visual states and value callbacks. The frontend owns draft values, dirty/touched state, conditional visibility and submission orchestration. The backend owns schema validation, authoritative answer validation, normalization, authorization and persistence. A readonly or hidden control cannot establish trust.

Empty, omitted and explicit false/zero are distinct. Define empty-string normalization per type; do not coerce every empty field to zero. All fields need editable, focused, invalid, disabled and readonly behavior where meaningful, with long labels, help, server errors and narrow layouts. Group fields use a group label and per-option accessible names. Passwords are account controls, not a default public survey field.

## Field inventory and priority

Stages follow the [Build path](../planning/saas-implementation-plan.md).

| ID | Field / family | Expected use / phase | Stored value and essential behavior |
| --- | --- | --- | --- |
| F01 | Short text | Frequent / first journey | String; length bounds, Unicode, whitespace policy; no silent truncation |
| F02 | Long text / autosize textarea | Frequent / first journey | String with line breaks; counter; resizing must preserve focus |
| F03 | Email | Frequent / first journey | String; syntactic check is not ownership verification; explicit single/multiple policy |
| F04 | Telephone | Frequent / product expansion | String plus country context if supplied; preserve leading + and zeros; extension policy |
| F05 | URL | Common / product expansion | String; accepted schemes; safe rendering as a link; never fetch arbitrary destinations implicitly |
| F06 | Integer / decimal / stepper | Frequent / first journey | Canonical numeric representation; min/max/step, locale parsing; reject nonfinite values |
| F07 | Currency / amount | Common / numeric-control batch | Decimal amount plus currency; explicit precision and rounding; not floating-point billing arithmetic |
| F08 | Single select | Frequent / first journey | Stable option ID or null; placeholder is not an answer; removed-option history |
| F09 | Radio group / yes-no | Frequent / first journey | One option ID; no accidental default; keyboard group behavior |
| F10 | Checkbox / acknowledgement | Frequent / first journey | Boolean; unchecked differs from unanswered where required; immutable wording/version for consent records |
| F11 | Checkbox group | Frequent / first journey | Option-ID array; min/max selections; deterministic output order |
| F12 | Switch | Frequent in settings / foundation | Boolean; explain immediate versus deferred save; use explicit choices when respondent intent is ambiguous |
| F13 | Searchable select / combobox | Common / product expansion | ID plus display label; empty/loading/failure; stale async results ignored; keyboard navigation |
| F14 | Multi-select / tags | Common / product expansion | ID array or free-text array, explicitly different modes; duplicates, paste limits and removal |
| F15 | Cascading / dependent choice | Common / advanced features | Parent and child IDs; invalidate stale child when parent changes; server validates relation |
| F16 | Date | Frequent / product expansion | Calendar date without timezone conversion; bounds and manual entry |
| F17 | Time | Common / product expansion | Local time; precision and optional zone context; not automatically an instant |
| F18 | Date-time | Common / product expansion | Instant plus zone when scheduling; ambiguous/nonexistent local time handling |
| F19 | Date / time range | Common / product expansion | Start/end with inclusive-boundary policy; ordering and timezone semantics |
| F20 | Month / week | Occasional / advanced features | Year-month or week-year/week; explicit calendar convention |
| F21 | File upload / dropzone | Frequent / product expansion | File references, not arbitrary client URLs; per-file and total limits, progress, cancel/retry, scan status |
| F22 | Image upload / crop | Common / product expansion then advanced features crop | File reference and transform metadata; image decoding, orientation, accessible filename and original preservation policy |
| F23 | Rating / stars | Common / product expansion | Bounded integer or specified increments; explicit unanswered state; text alternative |
| F24 | Opinion scale / NPS | Common / product expansion | Integer with configured endpoints; store question version; scoring belongs to product analytics |
| F25 | Slider / range | Common / product expansion | Number or pair; keyboard increments and exact-entry alternative; distinguish untouched from chosen default |
| F26 | Name group | Common / product expansion | Structured optional parts; support single names and non-Western order |
| F27 | Address / country / region | Common / product expansion | Structured strings and country code; country-dependent labels; manual entry if lookup fails |
| F28 | Location / map coordinate | Occasional / extensions | Coordinates plus precision and optional address; manual fallback; permission failure state |
| F29 | Rich text answer / content editor | Occasional / advanced features | Restricted structured content; sanitized rendering and pasted content; attachment limits |
| F30 | Signature | Optional / extensions | Asset or typed-name record plus timestamp/context; legal meaning is a separate product decision |
| F31 | Matrix / Likert | Common surveys / advanced features | Row-ID to option-ID map; mobile stacked layout, per-row errors, missing-versus-skipped |
| F32 | Ranking / sortable choices | Occasional / advanced features | Ordered option IDs; keyboard move buttons, uniqueness, partial-ranking policy |
| F33 | Repeatable / nested group | Common / advanced features | Array of objects with stable item IDs; add/remove/reorder, nesting and item limits |
| F34 | Calculated / read-only result | Common / advanced features | Typed server-recomputed value; dependency graph, cycles, rounding and division errors |
| F35 | Hidden / prefilled value | Common / product expansion | Typed untrusted input; signed trusted context separately; URL values excluded from authorization |
| F36 | Payment collection | Separate [Form payment fields work package](../planning/form-payment-fields.md) | Payment-specific respondent controls, builder settings and backend flow are delivered together; not part of the ordinary field sequence |
| F37 | Password / reveal / strength | Account / foundation | Ephemeral secret input; password-manager support; no response-data or analytics logging |
| F38 | OTP / verification code | Account / foundation or release readiness | Ephemeral code; paste/autofill, resend cooldown and server expiry/attempt limits |
| F39 | Search | App / first journey | Query string; debounce/cancel and URL state as appropriate; not a response field by default |
| F40 | Color picker | Builder / product expansion | Canonical color; alpha policy, text entry and contrast feedback |
| F41 | Masked / formatted input | Cross-cutting / product expansion | Separate display mask from raw value; allow paste/edit; format is not validation |
| F42 | Dual-list selection / transfer | Optional / extensions | Selected ID set; search both lists, keyboard transfer and stable order policy |
| F43 | Card / picture choice | Common / product expansion | Option ID(s); image alternative text; selection independent of image loading |
| F44 | Code / JSON editor | Integration settings / advanced features | Text plus parse diagnostics; no execution of untrusted expressions |
| F45 | Challenge / anti-abuse widget | Runtime / first journey policy, adapter as needed | Short-lived proof validated server-side; expiry/retry and accessible alternative |
| F46 | Content block / heading / paragraph / media | Builder / first journey | No answer value; sanitized content, alt text/captions, safe embeds |
| F47 | Section / page break / completion block | Builder / first journey then product expansion pages | Structure IDs; progress/navigation; completion only after durable acceptance |

## Field decorators and layout variants

Preserve these as independently specified variants, not extra domain field types: leading/trailing icon or text, attached action, prefix/suffix units, floating versus static label, sizes/density, rounded/border styles, inline versus stacked choices, option groups, clear button, counters, autosize, masked display, copy action, strength feedback, disabled options, readonly display, vertical/horizontal forms, responsive grids, sticky actions, numbered/icon step navigation, inline editing, nested groups, and input groups.
Color variants must communicate state with text/semantics as well as color. A floating label is presentation, not a separate validation contract. Avoid multiplying exports for visual differences that can be expressed as a documented variant.

## Builder and respondent parity

Each enabled field needs seven deliverables: builder palette entry, property editor, schema serializer, respondent renderer, client validation adapter, server validator, and response/export formatter. Preview must use the published renderer with a draft schema, not a separate mock. Publication checks field compatibility, unique IDs, options, constraints and logic before changing the active version atomically.

Conditional fields need explicit policy: when hidden, exclude from submission and required checks by default; whether to retain a temporary draft answer for undo must not alter the submitted payload. The server evaluates the same published rules. Multi-page back navigation preserves valid input; hidden pages cannot strand focus or create a loop.

## Acceptance matrix

| Dimension | Required evidence |
| --- | --- |
| Input | Empty, valid, boundary, malformed, pasted, Unicode, very long values; false and zero preserved |
| Accessibility | Labels, group names, error associations, keyboard-only completion, focus restoration, screen-reader announcement; no drag-only operations |
| Submission | Server field errors mapped by stable ID; values retained; duplicate retry handled; stale schema response recoverable |
| Async | Out-of-order search, disconnected upload, expired session, aborted requests; no late result overwrites newer input |
| Versioning | Rename/delete/reorder options and fields after responses exist; historical display/export remain meaningful |
| Responsive / locale | Narrow viewport, zoom, long translations, RTL decision, dates/numbers and timezone boundaries |
| Data handling | Escaped display, safe CSV export, file authorization, no secret logging, backend rejects tampered hidden values |

## Open decisions

Audience, launch fields, locales, phone/address policy and maximum form size remain open. Enable a field only after its builder, renderer, validation and response contracts are ready.
