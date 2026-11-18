# Repository and release policy

[简体中文](README.zh-CN.md) · English · [Home](../../README.md) · [Documentation](../README.md)

## Branch and tag roles

| Reference | Role | Update rule |
| --- | --- | --- |
| `main` | Current product documentation, distribution index, manifests, and preservation checks | Review changes and pass repository checks; ordinary forward commits |
| `legacy-v0.0.3` | Original foundational project root | Preserve target `b5f44c111fef3d32b5cdeb3c18d4af40e5c81306` |
| `openketupamk-v*` | Product release snapshots | Published targets remain fixed |
| `openketupamk-runtime-v*` | Runtime release snapshots | Published targets remain fixed |
| `openketupamk-beta` | Historical Beta | Preserve its existing target |

Only `main` is the published working branch at this review. Tags are fixed references, not working branches. Historical tags may show the original distribution layout rather than today's `main` layout. The [tag map](../../releases/tag-map.json) is the preservation baseline. Do not move old tags to improve their appearance.

Repository rules protect `main` against deletion and force pushes, and the foundation/product/runtime/Beta tag namespace against updates and deletion. These safeguards do not require every change to use a pull request or imply a mandatory external review. Automated integrity checks run for pushes and pull requests.

## Preserve the foundation

`history/Ketupa_v0.0.3/` retains the complete foundational project. Its Git tree must remain `ea29d263d3a6c98b62ef9cb17c326523e5cc383b`. The original 111 files, paths, modes, author credits, LICENSE, and NOTICE remain unchanged. Place historical explanation and corrections in the guides beside the archive. Preserve both source repositories' commit ancestry.

## Publish a product version

1. Identify the version, supported platforms, feature scope, legal licensor, and entitlement scope. New product tags use `openketupamk-vX.Y.Z`; preview candidates may use `-rc.N`. Runtime uses `openketupamk-runtime-vX.Y.Z`.
2. Build and validate the actual installers, recording build inputs, dependency inventory, applicable notices/source, platform compatibility, and acceptance evidence. Complete the [commercial delivery requirements](REVIEW.md) before making production claims.
3. Record filenames, sizes, SHA-256 values, and immutable tag targets in the release manifests. Provide corresponding English and Chinese notes and exact direct-download URLs.
4. Run `python3 tools/check_repository.py` from the repository root. Review entitlement publication separately; only explicitly designated public test files belong under `licenses/`.
5. Publish assets to GitHub Releases. Keep previews marked as pre-releases. Never overwrite an already published asset or retarget its tag to silently correct a build; publish a new version and describe the correction.
6. Verify every download URL and asset digest after upload. Update the current README and documentation index. A documentation-only commit does not create a product release or change a historical tag.

The original five release groups and their fifteen assets remain preserved. Original publication times are recorded separately from migration timestamps. A release tag, installer signature, SHA-256 digest, and legal acceptance record establish different facts; keep their evidence separate.

## Legal and operational records

Keep operative LICENSE/EULA text and its revision traceable. A new website document does not retroactively change accepted agreements or previously granted historical rights. Commercial delivery needs a verified legal identity, entitlement evidence, actual data-processing disclosures, support terms, and version-specific dependency/source coverage. Do not label unverified items as completed.

Public issues accept sanitized product/documentation reports. Rights, private entitlements, and security reports use the [private contact](../../SECURITY.md). Contributed changes follow the [contribution guide](../../CONTRIBUTING.md).

## Structure references

The organization was reviewed against [VS Code](https://github.com/microsoft/vscode), [PowerToys](https://github.com/microsoft/PowerToys), and [Ollama](https://github.com/ollama/ollama): product-first entry points, distinct documentation, clear downloads, contribution/security guidance, and repository automation. Their licenses, trademarks, support commitments, and feature claims do not transfer to this project.

Platform references: [GitHub licensing](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository) · [GitHub releases and tags](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases).
