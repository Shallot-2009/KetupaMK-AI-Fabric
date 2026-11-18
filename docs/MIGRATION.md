# Repository migration record

[简体中文](MIGRATION.zh-CN.md) · English · [Home](../README.md) · [Documentation](README.md)

Date: 2026-11-18

| Role / 角色 | Original / 原名称 | Final / 最终名称 | GitHub repository ID |
| --- | --- | --- | --- |
| Continuing primary repository / 延续主仓库 | `Shallot-2009/Ketupa_v0.0.3` | `Shallot-2009/KetupaMK-AI-Fabric` | `1005327414` |
| Integrated distribution source / 被整合的发行仓库 | `Shallot-2009/Ketupa-AI-Fabric` | `Shallot-2009/test` | `1424671956` |

The original repository is renamed in place, retaining its ID, existing stars, fork relationships, and issues. The pre-migration baseline is 90 stars and 10 forks; these counts may naturally change. No replacement repository is created, and the distribution repository's one star is not combined with the primary count. GitHub redirects old URLs while those names remain unclaimed; current links use the final primary URL.

All 111 tracked files at legacy commit `b5f44c111fef3d32b5cdeb3c18d4af40e5c81306` move to `history/Ketupa_v0.0.3/`, validated against their original Git blobs. The `legacy-v0.0.3` tag preserves the original root. Original README, LICENSE, NOTICE, credits, and potentially obsolete commands remain byte for byte; explanatory guidance is kept outside that snapshot.

The original project is archived as a whole, preserving its complete relative directory structure and every tracked file. On 2026-11-18, the initial archive directory `history/0.0.3/` was renamed to `history/Ketupa_v0.0.3/`, with navigation, the archive manifest, and Git byte-preservation rules updated accordingly. Archive contents, file modes, original commit history, and the `legacy-v0.0.3` tag remain unchanged.

Distribution baseline: `67d7ffd815fea925f0fc50ece3cb8dfc53424aae`. Both original Git histories are retained through a merge, and all five original release tags keep their commit targets. Distribution documents, the EULA, proprietary notice, author-approved public test license, and complete third-party materials are integrated at the root. Navigation, scope explanations, and Git text handling receive necessary updates; operative legal texts, third-party materials, and the test file retain their bytes.

Five Releases with fifteen installers are copied to the primary repository, preserving filenames, sizes, SHA-256 digests, and pre-release flags. New GitHub release timestamps reflect migration rather than fabricated original publication times; original dates are recorded in the manifest and release notes. The old README's three stale 1.0.2 hashes are corrected against actual assets, and its original bytes are retained in [provenance records](provenance/README.md). Installers are not repacked or internally renamed.

Only after content, all installer files, and provenance are verified is the distribution source renamed to `test` and its default-branch file tree emptied with an ordinary commit. Original commit history, release tags, and Git objects are retained without a force push. After release-file migration, `test` is no longer a distribution entry point. Private development source, licenses, and engineering environments are not additionally published.

After the distribution source is renamed to `test` and its Releases are removed, its former installer download deep links do not redirect across repository identities to the primary repository. Update them to the new URLs in the homepage and manifest. This differs from the original historical repository's in-place rename redirect.

Historical Apache-2.0 rights, earlier BSD-2-Clause grants, current proprietary terms, and third-party licenses retain their separate scopes; see [LICENSE.md](../LICENSE.md).
