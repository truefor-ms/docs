---
name: building-components
description: Design and implement TrueUI component contracts, composition, state handling, semantic styling, and usage documentation in the project's existing technology stack.
metadata:
  variant: trueforms-stack-neutral
---

# Building TrueUI components

This is a locally authored, technology-neutral adaptation of the component architecture scope proposed by [Vercel components.build](https://github.com/vercel/components.build/tree/main/skills/building-components). It does not include or activate the upstream TypeScript, Tailwind, registry, or framework recipes.

## Scope and constraints

Use for reusable TrueUI components and their consumer examples. Follow `docs/planning/trueui-implementation.md` and the form and builder plans before choosing the next component. Existing brand decisions, component contracts, language, and styling conventions govern implementation. Do not require Tailwind CSS, TypeScript, a particular framework, or a new dependency to follow this skill.

## Component contract

Before implementation, identify the consumer task, semantic element, public inputs and events, state ownership, and composition boundaries. Keep reusable presentation and interaction in TrueUI; keep application business logic in its owning application. Prefer native controls when they satisfy the contract.

Expose the states the component actually needs, including focus, disabled, invalid, pending, empty, or read-only where applicable. Specify default values, value changes, validation messaging, and reset behavior for form controls. Avoid public options that merely encode an application's one-off layout.

Use semantic design tokens and the project's established styling mechanism. Keep visual appearance separate from behavior so form and builder surfaces can compose the same primitives. Reuse existing components before introducing parallel implementations.

## Accessibility and interaction

Implement accessible names, descriptions, keyboard navigation, and focus behavior appropriate to the component. Consult the relevant [WAI-ARIA Authoring Practices pattern](https://www.w3.org/WAI/ARIA/apg/patterns/) for custom widgets; preserve native behavior rather than duplicating it. Provide non-drag alternatives to drag operations.

## Verification and documentation

Document the public API in the existing language, with examples and explicit state behavior. Use JSDoc if that fits the codebase; do not introduce a type system for documentation.

Verify meaningful behavior such as value propagation, keyboard operation, focus return, error association, and reset. Inspect rendered components at supported widths and with long labels. Distinguish source checks from browser and assistive-technology verification. Use consumer fixtures for form and builder compositions before declaring TrueUI readiness; a passing build alone does not establish maturity.
