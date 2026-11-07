# Component ownership

Planned shared components and application responsibilities.

## Reusable component families

This reference retains reusable foundations and form-SaaS compositions. Unrelated example applications and decorative extensions are omitted. The build stages are dependency phases, not dates. A listed composition does not automatically require a separate package export.

| ID | Family and variants | First use / phase | Boundary and required states |
| --- | --- | --- | --- |
| C01 | Tokens, typography, spacing, color, elevation, borders, density, motion, focus | All / foundation | TrueUI; semantic roles, contrast and reduced motion; frontend resolves theme |
| C02 | Text, heading, link, icon, logo, separator, list | All / foundation | TrueUI; semantic markup, truncation alternatives, decorative versus named icons |
| C03 | Button, icon button, button group, split button | All / foundation | TrueUI; pending, disabled, destructive, keyboard and repeat activation |
| C04 | Field wrapper, label, help, error, required indicator, group, error summary | Forms / foundation | TrueUI presentation; frontend validation timing; backend authority |
| C05 | Basic and advanced controls F01–F47 | Forms / foundation–extensions | See [field contract](fields.md); domain renderers live in frontend |
| C06 | Stack, grid, container, responsive columns, divider, surface/card/panel | All / foundation | TrueUI; no product-specific data fetching |
| C07 | App shell, sidebar, header, footer, top navigation, compact/horizontal layouts | Admin / foundation | TrueUI slots; frontend route and permission state |
| C08 | Page header, breadcrumbs, toolbar, action bar, sticky actions | Admin / first journey | TrueUI composition; frontend titles/actions; narrow-layout overflow |
| C09 | Menu, dropdown, context menu, nested navigation | Admin / first journey | TrueUI; keyboard roving, escape, focus return, viewport collision |
| C10 | Dialog, confirmation, alert dialog, drawer/offcanvas | Edit/delete / first journey | TrueUI focus containment; frontend intent, dirty-state and delete workflow |
| C11 | Tooltip, popover, hover card | Help / first journey | TrueUI; keyboard/touch access; essential instructions available without hover |
| C12 | Tabs/pills, accordion, collapse/disclosure | Settings / first journey | TrueUI; selection and expansion semantics, lazy content state |
| C13 | Alert/banner, toast/snackbar, inline status | Save/failure / foundation | TrueUI; persistent errors not toast-only, announcement and action support |
| C14 | Spinner, skeleton, progress, overlay/blocking state | Async / foundation–product expansion | TrueUI; measurable versus indeterminate; cancel/retry supplied by app |
| C15 | Empty state, no results, error panel, offline and permission state | All / first journey | TrueUI presentation; app distinguishes causes and recovery |
| C16 | Badge, chip, tag, status dot, ribbon | Lists / first journey | TrueUI; text meaning, removable keyboard action, no color-only status |
| C17 | Avatar/group, image/thumbnail, media object, file tile | Team/assets / product expansion | TrueUI; image failure, initials, alt text and loading |
| C18 | Semantic table, responsive table, row actions | Responses / first journey | TrueUI; headers, empty/loading/error, narrow-screen reading |
| C19 | DataTable: sort, filter, search, pagination, selection, bulk actions | Responses / product expansion | TrueUI controlled state; backend query authorization; explicit all-page selection semantics |
| C20 | Column visibility/order/resize/pinning, expandable rows, virtualized grid, inline edit | Large datasets / advanced features | Optional TrueUI composition; stable row IDs; keyboard access and server conflicts |
| C21 | Pagination/pager, page-size control, load-more | Lists / first journey | TrueUI; counts unknown/known, reset on filter, stable query state |
| C22 | Filter bar, filter chips, date range, saved-view presentation | Responses / product expansion | TrueUI widgets; frontend query model; backend saves views and filters |
| C23 | Global search / command palette / shortcuts | Admin / advanced features | TrueUI search shell; app result routing and authorization |
| C24 | Stepper, wizard, progress navigation | Onboarding/forms / product expansion | TrueUI; frontend progression rules, back/skip/invalid steps |
| C25 | Sortable list, drag handle, drop target, transfer, tree view | Builder / first journey basic move, advanced features advanced | TrueUI generic interaction; keyboard move alternative; app schema/permissions |
| C26 | Timeline/activity feed, audit event presentation | History / product expansion | TrueUI; backend immutable event facts and visibility |
| C27 | Chart adapters, legends, metrics, sparklines, gauges, heatmaps | Analytics / release readiness–advanced features | Optional TrueUI; frontend metric definitions; accessible tabular alternative |
| C29 | Rich text, code editor, syntax highlighting, diff | Content/integrations / advanced features | Optional adapters; restricted content and app validation |
| C30 | Upload queue, preview, image crop, file browser | Files / product expansion–advanced features | TrueUI presentation; backend storage, scan and signed access |
| C33 | Tour, onboarding checklist, contextual help, feedback prompt | Activation / release readiness | Reusable presentation; frontend completion and eligibility |
| C34 | Scroll area, sticky regions, scroll-to-top, scrollspy, resizable/split panels | Builder/layout / product expansion–advanced features | TrueUI where reusable; preserve native input and zoom behavior |
| C36 | Notification list, inbox item, unread indicator | SaaS / release readiness | TrueUI presentation; frontend preferences; backend delivery/read state |

## Application compositions and domain ownership

| ID | Composition / feature | Reusable parts | Frontend and backend responsibilities | Phase |
| --- | --- | --- | --- | --- |
| A01 | Marketing, pricing, FAQ, help, status and contact | C02, C06, C12 | Accurate public availability, plan content, support routing | release readiness |
| A02 | Signup, verification, login, logout, reset, MFA, session list | C03–C05, C13 | Identity lifecycle, session revocation, recovery and throttling | foundation then release readiness MFA |
| A03 | Onboarding, workspace switch/create, invitations | C07, C24 | Tenant membership, invite expiry/revocation, owner transfer | foundation–release readiness |
| A04 | Form library: list/grid, search, folders/tags, duplicate/archive/trash | C08–C10, C18–C22 | Authorized queries, lifecycle and restore/retention | first journey–product expansion |
| A05 | Form builder: palette, canvas, outline, properties, rules | C04–C06, C25, C34 | Schema state, undo/redo, autosave, conflict resolution, validation | first journey–advanced features |
| A06 | Preview, theme, publication/version history, share/embed | C10, C24, C26 | Atomic publish, stable public URL, access rules, embed configuration | first journey–product expansion |
| A07 | Respondent flow: welcome, questions, pages, review, submit, receipt | F01–F47, C13–C15 | Public renderer, conditional logic, durable submit, close/expiry and retry | first journey–advanced features |
| A08 | Response inbox/detail, attachments, notes, tags, export, deletion | C18–C22, C26, C30 | Version-aware answers, access checks, safe export, retention | first journey–product expansion |
| A09 | Form analytics, drop-off, completion, sources, trends | C27 | Defined event/metric contracts, bot exclusion and aggregation | release readiness–advanced features |
| A10 | Workspace/member/role administration and audit | C18, C10, C26 | Backend capability checks and object scope; revoke active access | product expansion–release readiness |
| A11 | Subscription, plan/usage, upgrade, payment method, invoices, cancellation | C06, C13, C19 | App billing starts with foundations; distinct from form payment fields | foundation implementation; release readiness release validation |
| A12 | Profile, preferences, security, localization, data controls | C04, C12 | Account/workspace settings ownership and export/deletion flows | product expansion–release readiness |
| A13 | API keys, webhooks, integrations, delivery logs and retry | C19, C29 | Scopes/secrets, outbound delivery queue, idempotency and revocation | advanced features |
| A14 | Automation/rules, approvals, assignments, notification examples | C25, C26, C29 | Versioned execution, retry/dead-letter, authorization and history | advanced features |
| A15 | Platform operator console, abuse cases, support tooling | C18, C22, C26 | Separate staff permissions, audited access, operational controls | release readiness |

## Shared acceptance contract

Every implemented family needs examples for ordinary, empty, pending, failed, denied, disabled and overflow states where applicable. Document controlled/uncontrolled state, callback payloads, focus behavior, keyboard contract and localization boundaries. Test nested overlays, long content, zoom, reduced motion, theme contrast and mobile touch. A published API includes supported variants and intentional exclusions; visual resemblance to a theme is not an acceptance criterion.

No reusable component may fetch a Trueforms endpoint, infer a subscription plan, authorize a user or persist a form. Domain compositions stay in frontend; backend remains authoritative. Heavy adapters load independently so a text field does not import charts or editors. Library choices require license, maintenance, accessibility, size and integration review; evaluate dependencies against product requirements.
