# 仓库与发行规范 / Repository and release policy

[Home / 项目主页](../../README.md) · [Documentation / 文档](../README.md)

点击语言标题即可在本页切换；另一语言会自动折叠。 / Select a language below; the other section collapses on this page.

<details name="readme-language">
<summary><strong>English</strong></summary>

## Branch and tag roles

| Reference | Role | Update rule |
| --- | --- | --- |
| `main` | Current product documentation, distribution index, manifests, and preservation checks | Review changes and pass repository checks; ordinary forward commits |
| `legacy-v0.0.3` | Original foundational project root | Preserve target `b5f44c111fef3d32b5cdeb3c18d4af40e5c81306` |
| `openketupamk-v*` | Product release snapshots | Published targets remain fixed |
| `openketupamk-runtime-v*` | Runtime release snapshots | Published targets remain fixed |
| `openketupamk-kernel-legacy-v*` | Legacy Linux application/runtime compatibility snapshots | Published targets remain fixed |
| `openketupamk-beta` | Historical Beta | Preserve its existing target |

Only `main` is the published working branch at this review. Tags are fixed references, not working branches. Historical tags may show the original distribution layout rather than today's `main` layout. The [tag map](../../releases/tag-map.json) is the preservation baseline. Do not move old tags to improve their appearance.

Repository rules protect `main` against deletion and force pushes, and the foundation/product/runtime/compatibility/Beta tag namespace against updates and deletion. These safeguards do not require every change to use a pull request or imply a mandatory external review. Automated integrity checks run for pushes and pull requests.

## Preserve the foundation

`history/Ketupa_v0.0.3/` retains the complete foundational project. Its Git tree must remain `ea29d263d3a6c98b62ef9cb17c326523e5cc383b`. The original 111 files, paths, modes, author credits, LICENSE, and NOTICE remain unchanged. Place historical explanation and corrections in the guides beside the archive. Preserve both source repositories' commit ancestry.

## Publish a product version

1. Identify the version, supported platforms, feature scope, legal licensor, and entitlement scope. New product tags use `openketupamk-vX.Y.Z`; preview candidates may use `-rc.N`. Runtime uses `openketupamk-runtime-vX.Y.Z`; legacy Linux compatibility builds use `openketupamk-kernel-legacy-vX.Y.Z`. A compatibility flavour has its own release, assets and test scope.
2. Build and validate the actual installers, recording build inputs, dependency inventory, applicable notices/source, platform compatibility, and acceptance evidence. Complete the [commercial delivery requirements](REVIEW.md) before making production claims.
3. Record filenames, sizes, SHA-256 values, and immutable tag targets in the release manifests. Provide English and Chinese notes on the same page and exact direct-download URLs.
4. Run `python3 tools/check_repository.py` from the repository root. Review entitlement publication separately; only explicitly designated public test files belong under `licenses/`.
5. Publish assets to GitHub Releases. Keep previews marked as pre-releases. Use a new version for functional changes. Never silently replace assets or retarget published tags.
6. Verify every download URL and asset digest after upload. Update the current README and documentation index. A documentation-only commit does not create a product release or change a historical tag.

Public release guides describe downloads, supported systems, features, and how to install. Keep engineering logs and test records in the private maintenance workspace.

## Legal and operational records

Keep operative LICENSE/EULA text and its revision traceable. A new website document does not retroactively change accepted agreements or previously granted historical rights. Commercial delivery needs a verified legal identity, entitlement evidence, actual data-processing disclosures, support terms, and version-specific dependency/source coverage. Do not label unverified items as completed.

Public issues accept sanitized product/documentation reports. Rights, private entitlements, and security reports use the [private contact](../../SECURITY.md).

## Structure references

The organization was reviewed against [VS Code](https://github.com/microsoft/vscode), [PowerToys](https://github.com/microsoft/PowerToys), and [Ollama](https://github.com/ollama/ollama): product-first entry points, distinct documentation, clear downloads, contribution/security guidance, and repository automation. Their licenses, trademarks, support commitments, and feature claims do not transfer to this project.

Platform references: [GitHub licensing](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository) · [GitHub releases and tags](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases).

</details>

<details name="readme-language" open>
<summary><strong>简体中文</strong></summary>

## 分支和标签职责

| 引用 | 职责 | 更新规则 |
| --- | --- | --- |
| `main` | 当前产品文档、发行导航、清单与保全检查 | 审核变更并通过仓库检查，使用普通前向提交 |
| `legacy-v0.0.3` | 基础项目的原始根目录 | 固定指向 `b5f44c111fef3d32b5cdeb3c18d4af40e5c81306` |
| `openketupamk-v*` | 产品发行快照 | 已发布标签固定指向原提交 |
| `openketupamk-runtime-v*` | Runtime 发行快照 | 已发布标签固定指向原提交 |
| `openketupamk-kernel-legacy-v*` | 旧版 Linux 应用/运行环境兼容快照 | 已发布标签固定指向原提交 |
| `openketupamk-beta` | 历史 Beta | 保留既有指向 |

本次检查时，仅 `main` 作为公开工作分支。标签是固定引用，不是工作分支；历史标签可能显示原发行目录，而非当前 `main` 布局。[标签映射](../../releases/tag-map.json)是保全基准，不为调整页面外观而重指向旧标签。

仓库规则防止删除或强制推送 `main`，并防止更新或删除基础项目、产品、Runtime、兼容版及 Beta 标签命名空间。这些保护不强制所有变更走 PR，也不等于强制外部审核。推送与 PR 均执行自动完整性检查。

## 保全基础项目

`history/Ketupa_v0.0.3/` 保留完整基础项目，Git tree 固定为 `ea29d263d3a6c98b62ef9cb17c326523e5cc383b`。原 111 个文件的路径、模式、字节、作者署名、LICENSE 与 NOTICE 保持原样；历史说明和纠正写在归档旁的指南中，两个来源仓库的提交历史继续保留。

## 发布产品版本

1. 确定版本、支持平台、功能范围、法律许可主体和授权范围。新产品标签采用 `openketupamk-vX.Y.Z`，候选预览可使用 `-rc.N`；Runtime 采用 `openketupamk-runtime-vX.Y.Z`，旧版 Linux 兼容构建采用 `openketupamk-kernel-legacy-vX.Y.Z`，独立记录发行组、附件和测试范围。
2. 构建并验证实际安装包，记录构建输入、组件清单、适用声明/源码、平台兼容性与验收依据。宣称生产适用前应完成[商业交付要求](REVIEW.md)。
3. 在发行清单中记录文件名、大小、SHA-256 和固定标签指向，提供同页中英文说明与准确的直接下载 URL。
4. 在根目录运行 `python3 tools/check_repository.py`。授权文件另行审核发布范围，`licenses/` 仅保存明确指定的公开测试文件。
5. 将附件发布到 GitHub Releases，预览版继续标记为 pre-release。功能修改使用新版本。不得静默替换附件或移动已发布标签。
6. 上传后逐项验证下载 URL 与哈希，更新主页和文档索引。纯文档提交不产生产品版本，也不修改历史标签。

公开发行说明提供下载入口、适用系统、功能范围和安装方法。工程日志和测试记录保存在内部维护工作区。

## 法律与运营记录

正式 LICENSE/EULA 文本和修订应可追溯。网站更新不追溯改变已接受的协议或历史已授予权利。商业交付需要核实法律主体、授权依据、实际数据处理告知、支持条款，以及逐版本依赖/源码覆盖。未核实事项不标记为完成。

公开 Issue 接收脱敏产品和文档反馈。权利、私有授权和安全报告使用[私密联系渠道](../../SECURITY.md)。

## 架构参考

本次参考 [VS Code](https://github.com/microsoft/vscode)、[PowerToys](https://github.com/microsoft/PowerToys) 与 [Ollama](https://github.com/ollama/ollama) 的产品首页、独立文档、清晰下载、贡献/安全说明和仓库自动化组织方式。其许可、商标、支持承诺及功能声明不转移到本项目。

平台依据：[GitHub 许可说明](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository) · [GitHub 发行与标签](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)。

</details>
