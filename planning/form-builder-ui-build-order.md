# Form Builder UI

**Updated:** 7 November 2026. **Status:** implementation preparation; proposed component names and contracts. This surface creates, configures, previews and publishes forms. The [respondent UI plan](respondent-ui-build-order.md) covers filling them in. Account, billing and response management remain in the [application map](../reference/components.md).

The sequence uses the existing [field inventory](../reference/fields.md) and [SaaS delivery stages](saas-implementation-plan.md). It is a dependency plan, not a framework selection. All field capabilities remain accounted for, including later extensions.

## TrueUI-first execution rule

Start with the [TrueUI implementation sequence](trueui-implementation.md). This surface plan supplies requirements for that initial standalone library build. Implement its reusable U components and fixture-based catalog compositions first. F-owned product components and B-owned backend services begin only after the [TrueUI readiness gate](saas-implementation-plan.md#trueui-readiness-gate) is accepted. Mixed-ownership rows are split at that boundary: reusable presentation now, domain integration later. The row numbers below describe dependencies within this surface, not permission to bypass the global gate.


## Ownership and shared foundations

**U = TrueUI:** inputs, overlays, layout, selection and reusable interaction. **F = frontend:** builder canvas, field registry, property editors, schema commands, history, rules, preview and publication orchestration. **B = backend dependency:** draft persistence, concurrency, authoritative schema checks and immutable publication.

Reuse respondent RUI-01–03 foundations rather than creating builder-only versions of Button, Input or FormField. A builder settings control is not automatically a public field type: for example, a label editor uses TextInput while editing the definition of a DateField. Domain-specific components below belong to frontend even when they compose TrueUI controls.

Before BUI-01, agree on field/option IDs, draft revision and published version contracts, safe content representation, option deletion behavior and server validation errors. Define selection independently from keyboard focus. Select an initial keyboard-first reorder strategy; drag-and-drop is an enhancement, not the starting dependency.

## Ordered implementation backlog

| Order / ID | Components to implement | Owner | Depends on | Completion evidence |
| --- | --- | --- | --- | --- |
| 01 / BUI-01 | BuilderShell, BuilderHeader, MainToolbar, PanelLayout, EmptyCanvas | F using U layout/button/text | RUI-01 and workspace access contract | Open a draft, show title and editable/readonly access; panels usable on narrow screens |
| 02 / BUI-02 | BuilderDocument controller, Selection controller, SchemaCommand dispatcher, FieldRegistry | F, mostly nonvisual | Schema contract | Stable IDs; add/update/remove/move commands produce valid predictable changes; selection survives reorder |
| 03 / BUI-03 | FieldPalette, FieldTypeItem, PaletteSearch, AddFieldAction | F using U list/search/menu | BUI-02 + basic field definitions | Add each initial type using keyboard; disabled/not-yet-supported types are explained |
| 04 / BUI-04 | CanvasFieldList, CanvasFieldFrame, SelectionOutline, FieldActions, MoveUpDown, Duplicate/Delete | F using U buttons/menus/dialog | BUI-02–03 | Add/select/duplicate/delete/reorder; focus goes to a predictable neighbor; copied IDs regenerated |
| 05 / BUI-05 | PropertiesPanel, LabelEditor, DescriptionEditor, RequiredToggle, DefaultValueEditor, PlaceholderEditor | F using U RUI-02–03 | BUI-04 | Edits update schema/preview; invalid property drafts do not silently corrupt document |
| 06 / BUI-06 | OptionListEditor, OptionRow, AddRemoveOption, OptionMoveControls, SelectionBounds | F using U | BUI-05 + option-ID contract | Choice types support stable IDs; reorder/rename distinct from deletion; duplicate option IDs rejected |
| 07 / BUI-07 | ValidationSettings, LengthBounds, NumericBounds, ErrorMessageEditor, SchemaIssueList | F using U | BUI-05–06 + shared validation rules | Contradictory constraints and invalid defaults identified; issue link selects correct field/property |
| 08 / BUI-08 | SaveStatus, UnsavedChangesNotice, SaveRetry, ConflictResolutionPanel, LeaveEditorDialog | F using U | BUI-02 + revision/save API | Saved/saving/failed/conflict distinct; old async save cannot overwrite newer draft; offline work retained |
| 09 / BUI-09 | UndoRedoToolbar, CommandHistory, RestoreSelection | F using U | BUI-02, BUI-08 | Add/edit/delete/reorder reversible; compound edits grouped; save and undo semantics documented |
| 10 / BUI-10 | PreviewPanel/Route, ViewportSelector, PreviewModeBanner, ResetPreviewAnswers | F using U | BUI-07 + RUI-04–07 | Actual respondent renderer consumes current draft; preview cannot write real responses |
| 11 / BUI-11 | PublishChecklist, PublishDialog, PublishStatus, PublicLinkPanel, CopyLinkAction | F using U | BUI-08,BUI-10 + publish API | Unresolved schema errors block publication; atomic publish returns version/link; failure preserves draft |
| 12 / BUI-12 | PageOutline, SectionEditor, PageBreakItem, PageActions, CompletionContentEditor | F using U tree/list | BUI-04–07 + RUI-12 | Move between pages safely; deleting a page handles contained fields explicitly; order matches runtime |
| 13 / BUI-13 | TypeSpecificSettings: date, telephone, address, rating, scale, file, choice card | F using U advanced controls | BUI-05–07 + corresponding RUI-09–11 | Type config, runtime value contract, backend validator and response formatter all agree |
| 14 / BUI-14 | ThemePanel, ColorControl, TypographyControl, SpacingControl, Logo/ImagePicker, ThemePreview | F using U | BUI-10 + theme/asset contract | Theme changes independent from answer schema; contrast/focus preserved; draft/published styling explicit |
| 15 / BUI-15 | DragHandle, DropIndicator, SortableCanvas, DragOverlay, AutoScroll | U generic interaction; F schema commands | BUI-04,BUI-09,BUI-12 | Same commands as move buttons; touch/keyboard alternatives; invalid/nested drops rejected |
| 16 / BUI-16 | LogicRuleList, ConditionGroupEditor, FieldReferencePicker, OperatorSelect, RuleValueEditor, ActionEditor, LogicIssueList | F using U | BUI-07,BUI-12–13 + RUI-13/server rule engine | Type-aware operators; missing references/cycles blocked; preview and server evaluate consistently |
| 17 / BUI-17 | MatrixSettings, RankingSettings, RepeaterSettings, CalculationEditor, DependencyViewer | F using U | BUI-16 + RUI-16 | Stable nested IDs, limits and dependency diagnostics; deletion of referenced fields is explicit |
| 18 / BUI-18 | PublishHistory, DraftVsPublishedSummary, VersionDetails, RollbackConfirmation, RestoreDraft | F using U timeline/dialog/diff | BUI-11 + version history APIs | Restore creates explicit revision; prior responses remain linked to original published schema |
| 19 / BUI-19 | FormAccessSettings, ScheduleSettings, LimitsSettings, ResumeSettings, NotificationSettings | F using U | BUI-11 + corresponding backend/runtime capabilities | Settings enforced by server; schedules show timezone; draft versus immediately active changes clear |
| 20 / BUI-20 | SharePanel, EmbedConfigurator, EmbedPreview, QRExport, DomainSettings | F using U | BUI-11 + embed/domain APIs | Correct version/access state; safe embed output; domain verification before activation |
| 21 / BUI-21 | TemplateBrowser, TemplatePreview, ImportSchema, ImportIssueSummary, ExportSchema | F using U cards/dialog/upload | BUI-07–10 + schema compatibility | Imports validated before replacing work; new IDs and unsupported types handled; recoverable failure |
| 22 / BUI-22 | LanguageManager, TranslationEditor, MissingTranslationSummary, LocalePreview | F using U | BUI-10,BUI-12 + locale schema | Stable field IDs across languages; missing translations visible; runtime fallback explicit |
| 23 / BUI-23 | ConnectorSettings, WebhookEditor, PrefillMapping, Calculation/CodeSettings, IntegrationTestResult | F using U; B secrets/jobs | BUI-11,BUI-16 + integration APIs | Secret masking, safe validation, test/live separation and scoped access |
| 24 / BUI-24 | AdvancedFieldSettings: signature, location, rich text, transfer, month/week | F using U adapters | Corresponding runtime fields and backend services | Full seven-deliverable field contract; no palette item enabled based on settings UI alone |
| 25 / BUI-25 | CollaboratorPresence, FieldLock/ConflictNotice, CommentThread, ActivityPanel | F using U; B coordination | BUI-08–09 + collaboration protocol | Concurrent changes do not silently overwrite; reconnect and revoked access handled |

Read-only/permission handling belongs in BUI-01 and every later mutation, not only collaboration. Leave warnings and save failures are required before real editing in BUI-08. Basic publishing issue feedback belongs in BUI-11; richer version diff can wait until BUI-18. Language support for the selected initial locale is foundational; multi-language management is BUI-22.

## Type registry and feature completeness

Every enabled field type provides: palette metadata, schema defaults, property editor, schema serializer, runtime renderer, client validation adapter, backend validator, and response/export formatter. These are deliverables across repositories, not eight exports from TrueUI. New field introduction should include a test fixture that exercises all representations.

## First milestone and integration order

1. Agree on surface requirements and contracts, then build all required shared U components and representative fixture-based compositions in TrueUI. Record acceptance of the standalone readiness gate before application work.
2. Build RUI-04–07 against a small fixed schema while BUI-01–07 builds the editor for that same schema. These application tracks can proceed independently only after TrueUI readiness is accepted and their contracts exist.
3. Add BUI-08–09 persistence/history. Add BUI-10 using the existing respondent renderer.
4. Connect BUI-11 to atomic publication; RUI-08 loads that published version. Complete create → preview → publish → submit → inspect stored response.
5. Expand in matched batches: field control + builder settings + server validation + response display/export. Multi-page settings cannot ship before multi-page runtime; upload settings cannot ship before upload storage/validation.

Initial builder acceptance: create a form with text, email, number and choices; edit labels/options/constraints; reorder by keyboard; undo; reload saved work; recover a failed save; preview; publish; copy a working link. A second editor must see a conflict rather than silently overwrite. Invalid schema blocks publication with field-specific explanations.

## Shared and surface-specific components

| Build once in TrueUI | Respondent frontend | Builder frontend |
| --- | --- | --- |
| Tokens, layout, text, icons, buttons, fields, input controls, alerts | PublishedFormRoute, FieldRenderer, respondent values, validation/submission coordinator | BuilderShell, schema commands, palette, canvas and properties |
| Dialog, menu, tabs, popover, tooltip, toast, progress | Access/closed/receipt states, page and branch navigation | Save/conflict handling, undo/redo, schema issues and publish workflow |
| Generic sortable/selection controls, tree, editor/upload adapters | Specialized answer compositions | Field configuration, rule editors, version history and integration settings |

A canvas preview may wrap the same field renderer in a selection frame, but must not accidentally edit respondent answers when selecting a field. Interactive preview runs as a separate explicit mode. Keep selection overlays and editing affordances out of published markup.

## Verification before enabling a package

Record keyboard/focus behavior, narrow-screen panel navigation, long labels, invalid settings, undo/redo, autosave race/conflict, permission loss and schema compatibility. Verify that fields disabled in the registry cannot be introduced through imports or API requests. Test deleting referenced fields/options/pages and opening an older draft after a registry update. Use frontend examples for app compositions and the TrueUI catalog for reusable components; neither substitutes for end-to-end backend evidence.

See the [SaaS plan](saas-implementation-plan.md) for surrounding account, response, billing and operational requirements. Those remain required product work but are not mislabeled as builder controls.
