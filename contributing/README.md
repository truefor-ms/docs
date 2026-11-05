# Contribution and commit rules

These project rules apply to new work in the Trueforms `docs`, `ui`, `frontend`, and `backend` repositories, including logo assets, reconstruction scripts, and documentation.

## GitHub account and commit identity

Use **`formtrue`** for every Trueforms push. **Never push through `bugrakaan`**, and do not fall back to another account if authentication or repository access fails. Resolve access for `formtrue` before retrying.

For newly authored project commits, use this identity for both the author and committer:

| Field | Required value |
| --- | --- |
| GitHub account used to push | `formtrue` |
| Git author name | `Trueforms` |
| Git committer name | `Trueforms` |
| Author and committer email | `352186882+formtrue@users.noreply.github.com` |

Commit identity and push authentication are separate. Correct author/committer metadata does not establish which GitHub account authenticates the push. Check both. Preserve original attribution when importing third-party history rather than rewriting its authors to the project identity.

Configure identity inside each relevant repository, using local settings so unrelated projects retain their own accounts:

```powershell
git config --local user.name "Trueforms"
git config --local user.email "352186882+formtrue@users.noreply.github.com"
git config --local credential.https://github.com.username formtrue
```

Verify the effective identity before committing; environment overrides can differ from repository configuration:

```powershell
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Before pushing, confirm that the remote is the intended Trueforms repository and that the credential helper or SSH identity used by **Git** authenticates as `formtrue`. If using GitHub CLI authentication, check its account too:

```powershell
gh api user --jq .login
git remote -v
```

The CLI account check alone is not proof of Git's account if a different credential helper is configured. Never print tokens or embed them in remote URLs, documentation, or commit messages.

## Conventional Commits

Every new commit message must follow [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/). The subject uses a type, an optional scope, and a short description:

```text
type(scope): description
```

Trueforms conventions: use English, lowercase types, a short relevant scope when useful, and a concrete action-oriented description. Do not use subjects such as `update`, `changes`, or `final` without a meaningful type and description.

| Type | Use in this project |
| --- | --- |
| `docs` | Documentation and reference updates |
| `feat` | New functionality or a new supported capability |
| `fix` | Corrections to existing behavior or output |
| `refactor` | Internal restructuring without changing behavior |
| `perf` | Performance improvements |
| `test` | Verification/test additions or corrections |
| `build` | Dependencies, packaging, or build tooling |
| `ci` | CI configuration and workflow changes |
| `chore` | Maintenance that does not fit a more precise type |
| `style` | Code formatting only; not a blanket label for visual design changes |
| `revert` | Reverting a prior change; identify the reverted commit in the body |

Examples for this workspace:

```text
docs(logo): record confirmed geometry and reconstruction results
docs(contributing): define commit identity and message rules
feat(brand): add reproducible logo generation
fix(logo): correct period alignment in the primary layout
build(brand): pin font outline tooling
```

Indicate a breaking change with `!` before the colon or a `BREAKING CHANGE:` footer. Explain the consumer impact and migration when relevant. For example:

```text
feat(brand)!: rename public logo asset paths

BREAKING CHANGE: Consumers must replace the previous asset paths with the documented names.
```

Bodies and footers are optional when the subject fully explains a small change. Apply the same message rules to amended commits, squash commits, and any merge commits created for the project; do not rely on an automatically generated title without reviewing it.

## Change boundaries and verification

- Stage only files belonging to the requested change and preserve unrelated work.
- Inspect the staged diff before committing. Keep independent changes in separate commits where practical.
- Keep original handoff files unchanged; new artwork and reconstruction code live separately.
- Run checks appropriate to the change and report their actual scope. A file-level or same-renderer comparison is not a browser/device acceptance test.
- Use English for newly authored documentation. Preserve the language and bytes of original supplied materials.
- Creating or editing files does not by itself request a commit or push. Perform those actions when requested as part of the task.

Before publishing a new commit, inspect its recorded identity and message:

```powershell
git log -1 --format="Author: %an <%ae>%nCommitter: %cn <%ce>%nSubject: %s"
```

These are documented rules. This change does not install a commit hook or CI enforcement and does not configure credentials in other repositories.
