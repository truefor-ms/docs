# Trueforms workspace

## Project UI skills

Use the relevant project skills in `.agents/skills/` for UI work:

- `building-components`: TrueUI component contracts, composition, states, and documentation. This is a technology-neutral project adaptation, not the upstream Vercel package.
- `web-design-guidelines`: interface implementation reviews.
- `accessibility`: accessibility implementation and evidence-based audits.
- `impeccable`: visual hierarchy, design quality, and refinement within the established brand.
- `better-layout`: grouping, responsive layout, text growth, and RTL.

Load only skills relevant to the task. Their availability does not require running five reviews on every change.

Do not introduce or require Tailwind CSS or TypeScript through a skill. Follow the project's chosen language, styling system, tokens, and component conventions. Upstream snippets are examples, not stack decisions. On updates, inspect instructions and references for new technology requirements before enabling them.

Project requirements and approved brand decisions take precedence over stylistic preferences in skills. Use native HTML behavior where appropriate. Check standards claims against WCAG and WAI-ARIA guidance; distinguish accessibility requirements from aesthetic preferences. Do not add redundant keyboard handlers to native controls or disable useful autocomplete solely to satisfy a generic checklist.

TrueUI must mature independently for both the form interface and form builder before application implementation. Follow the implementation and readiness plans in `docs/planning/`.

## Documentation and Git

Write project documentation in English and follow the documentation repository's own instructions. Use Conventional Commits for every commit. Use the `formtrue` account for pushes, and `Trueforms <352186882+formtrue@users.noreply.github.com>` for author and committer identity.
