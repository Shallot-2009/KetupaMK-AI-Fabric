# 仓库迁移记录 / Repository migration record

日期 / Date: 2026-11-18

| Role / 角色 | Original / 原名称 | Final / 最终名称 | GitHub repository ID |
| --- | --- | --- | --- |
| Continuing primary repository / 延续主仓库 | `Shallot-2009/Ketupa_v0.0.3` | `Shallot-2009/KetupaMK-AI-Fabric` | `1005327414` |
| Integrated distribution source / 被整合的发行仓库 | `Shallot-2009/Ketupa-AI-Fabric` | `Shallot-2009/test` | `1424671956` |

## 中文

主仓库通过对原仓库更名实现延续，保留仓库 ID、既有 90 个 star、10 个 fork 关系和 Issues；这些数字是迁移前基线，后续可自然变化。未重建替代仓库，未将另一仓库的 1 个 star 合并计数。旧地址在 GitHub 未被重新占用时依平台规则重定向；当前说明和下载链接全部使用主仓库新地址。

v0.0.3 基准提交 `b5f44c111fef3d32b5cdeb3c18d4af40e5c81306` 的全部 111 个跟踪文件移至 `history/0.0.3/`，按原 Git blob 逐项比对内容，新增 `legacy-v0.0.3` 标签保存原根目录。原 README、LICENSE、NOTICE 和署名保持原字节，包括可能过时的命令与路径；纠正和导航写在归档外的中英文说明中。

发行仓库基准提交为 `67d7ffd815fea925f0fc50ece3cb8dfc53424aae`。两套原有 Git 提交历史通过 merge 保留；原 5 个发行 tag 保持原提交指向。现行根目录整合发行文档、EULA、专有声明、作者批准公开的内测文件及全部第三方材料。仅导航说明、许可范围说明及 Git 文本处理规则作必要更新；原 EULA、专有 LICENSE、第三方材料和内测文件保留字节。

5 个 Release 的 15 个安装包复制至主仓库 Releases；文件名、大小、SHA-256 和预发布状态保留。创建新 Release 的平台时间反映迁移时间，不伪造为历史发布时间；原始发布时间记录在发行清单及各版本说明中。原 README 中 1.0.2 的三个哈希已过时，现行清单改为实际附件的哈希。迁移前说明见 [`provenance/`](provenance/README.md)。安装包不重新打包、不修改签名或内部产品名。

只有主仓库内容、全部安装包及来源记录验证成功后，才将发行源更名为 `test` 并通过普通提交清空其默认分支文件；其原提交历史保留，避免强制改写。原发行 tag 和历史 Git 对象也保留。Release 文件迁入主仓库后，`test` 不再承担分发入口。未对私有开发源码、许可证或 EDA 环境另行扩大公开范围。

Apache-2.0 历史授权、此前 BSD-2-Clause 授权、现行专有产品条款及第三方许可分别适用，详见 [LICENSE.md](../LICENSE.md)。

## English

The original repository is renamed in place, retaining its ID, existing stars, fork relationships, and issues. The pre-migration baseline is 90 stars and 10 forks; these counts may naturally change. No replacement repository is created, and the distribution repository's one star is not combined with the primary count. GitHub redirects old URLs while those names remain unclaimed; current links use the final primary URL.

All 111 tracked files at legacy commit `b5f44c111fef3d32b5cdeb3c18d4af40e5c81306` move to `history/0.0.3/`, validated against their original Git blobs. The `legacy-v0.0.3` tag preserves the original root. Original README, LICENSE, NOTICE, credits, and potentially obsolete commands remain byte for byte; explanatory guidance is kept outside that snapshot.

Distribution baseline: `67d7ffd815fea925f0fc50ece3cb8dfc53424aae`. Both original Git histories are retained through a merge, and all five original release tags keep their commit targets. Distribution documents, the EULA, proprietary notice, author-approved public test license, and complete third-party materials are integrated at the root. Navigation, scope explanations, and Git text handling receive necessary updates; operative legal texts, third-party materials, and the test file retain their bytes.

Five Releases with fifteen installers are copied to the primary repository, preserving filenames, sizes, SHA-256 digests, and pre-release flags. New GitHub release timestamps reflect migration rather than fabricated original publication times; original dates are recorded in the manifest and release notes. The old README's three stale 1.0.2 hashes are corrected against actual assets, and its original bytes are retained in [provenance records](provenance/README.md). Installers are not repacked or internally renamed.

Only after content, all installer files, and provenance are verified is the distribution source renamed to `test` and its default-branch file tree emptied with an ordinary commit. Original commit history, release tags, and Git objects are retained without a force push. After release-file migration, `test` is no longer a distribution entry point. Private development source, licenses, and engineering environments are not additionally published.

Historical Apache-2.0 rights, earlier BSD-2-Clause grants, current proprietary terms, and third-party licenses retain their separate scopes; see [LICENSE.md](../LICENSE.md).
