# TrueUI

**Status:** first implementation workstream. Frontend and backend application implementation starts only after TrueUI reaches standalone readiness for the initial Form UI and Form Builder UI scope.

## Scope

Build in `ui`: reusable presentation, component state, keyboard/focus behavior, tokens and fixture-based examples. Use the [Form UI](respondent-ui-build-order.md) and [Form Builder UI](form-builder-ui-build-order.md) plans as requirements, not as parallel application projects.

TrueUI does not own product schema commands, publication, persistence, authorization or billing. Examples simulate application data and callbacks. Planning those contracts is allowed before the gate; implementing the application repositories is not.

## Implementation order

| Order | Work package | Form UI need | Form Builder need | Completion evidence |
| --- | --- | --- | --- | --- |
| 1 | Token source, theme contract, typography, icons/logo, spacing, layout primitives | Readable form layout | Consistent panels and toolbars | Standalone catalog runs; tokens and supported themes documented |
| 2 | Button, IconButton, Link, FormField, Label, Help, Error, FieldGroup, ErrorSummary | Actions and accessible field feedback | Property editors and schema issue presentation | Keyboard/focus, labeling, errors and pending states verified |
| 3 | Input, Textarea, NumberInput, Select, Checkbox, RadioGroup, Switch and input decorators | Initial answer controls | Label/default/constraint and choice settings | Controlled values and callbacks; empty/invalid/disabled/readonly fixtures |
| 4 | Alert, Toast, Spinner, Progress, EmptyState, Status, Dialog, Menu, Popover, Tooltip | Submit/access/error presentation | Save/conflict/delete and action presentation | Overlay focus and recovery actions demonstrated without backend flows |
| 5 | Tabs, Accordion, responsive PanelLayout, Toolbar, List, Tree and selection primitives | Sections and navigation | Palette, outline and property-panel composition | Long content and narrow-screen navigation work in both sample surfaces |
| 6 | Repeatable option-list presentation, keyboard reorder controls and reusable sortable behavior | Repeated choice/group presentation where required | Option editing and field selection/reorder | Stable item IDs supplied by consumer; add/remove/move callbacks; no drag-only operation |
| 7 | Required advanced controls: combobox/multiselect, dates, upload presentation, rating/range and adapters | Agreed initial extended fields | Corresponding property controls | Each included control has documented value/state contracts and isolated examples |
| 8 | Compose representative form and builder examples | Completion, validation and pending/error states | Palette, selection, property editing, reorder and save/conflict feedback | Both compositions use the same library; fixtures only, no application endpoints |
| 9 | Package, regression coverage and readiness review | Stable consumer contract | Stable consumer contract | Versioned artifact works in an isolated consumer fixture; readiness accepted |

Determine the required initial advanced-control scope before package 7. Record explicit deferrals against the two surface plans; do not treat basic inputs alone as a mature library. Field inventories remain planning references, not a requirement to finish every future integration before accepting the initial scope. Form payment fields retain their [separate package](form-payment-fields.md).

## Readiness evidence

The authoritative [TrueUI readiness gate](saas-implementation-plan.md#trueui-readiness-gate) requires coverage of both surfaces, documented APIs and states, keyboard/accessibility and responsive checks, standalone examples, a consumable artifact and explicit acceptance.

Track each reusable requirement as planned, specified, implemented, verified or accepted, with its example and verification evidence. Mark a composition as simulated when application behavior is provided by fixtures. No readiness acceptance or completed component implementation is claimed by this document.

## After acceptance

Start application foundations and subscriptions, then execute the frontend-owned steps in [Form UI](respondent-ui-build-order.md) and [Form Builder UI](form-builder-ui-build-order.md) against the ready library and backend contracts. Subsequent component additions still belong in TrueUI; application business logic remains in frontend/backend.
