# 仓库与发行规范

简体中文 · [English](README.md) · [项目主页](../../README.zh-CN.md) · [文档](../README.zh-CN.md)

## 分支和标签职责

| 引用 | 职责 | 更新规则 |
| --- | --- | --- |
| `main` | 当前产品文档、发行导航、清单与保全检查 | 审核变更并通过仓库检查，使用普通前向提交 |
| `legacy-v0.0.3` | 基础项目的原始根目录 | 固定指向 `b5f44c111fef3d32b5cdeb3c18d4af40e5c81306` |
| `openketupamk-v*` | 产品发行快照 | 已发布标签固定指向原提交 |
| `openketupamk-runtime-v*` | Runtime 发行快照 | 已发布标签固定指向原提交 |
| `openketupamk-beta` | 历史 Beta | 保留既有指向 |

本次检查时，仅 `main` 作为公开工作分支。标签是固定引用，不是工作分支；历史标签可能显示原发行目录，而非当前 `main` 布局。[标签映射](../../releases/tag-map.json)是保全基准，不为调整页面外观而重指向旧标签。

仓库规则防止删除或强制推送 `main`，并防止更新或删除基础项目、产品、Runtime/Beta 标签命名空间。这些保护不强制所有变更走 PR，也不等于强制外部审核。推送与 PR 均执行自动完整性检查。

## 保全基础项目

`history/Ketupa_v0.0.3/` 保留完整基础项目，Git tree 固定为 `ea29d263d3a6c98b62ef9cb17c326523e5cc383b`。原 111 个文件的路径、模式、字节、作者署名、LICENSE 与 NOTICE 保持原样；历史说明和纠正写在归档旁的指南中，两个来源仓库的提交历史继续保留。

## 发布产品版本

1. 确定版本、支持平台、功能范围、法律许可主体和授权范围。新产品标签采用 `openketupamk-vX.Y.Z`，候选预览可使用 `-rc.N`；Runtime 采用 `openketupamk-runtime-vX.Y.Z`。
2. 构建并验证实际安装包，记录构建输入、组件清单、适用声明/源码、平台兼容性与验收依据。宣称生产适用前应完成[商业交付要求](REVIEW.zh-CN.md)。
3. 在发行清单中记录文件名、大小、SHA-256 和固定标签指向，提供对应中英文说明与准确的直接下载 URL。
4. 在根目录运行 `python3 tools/check_repository.py`。授权文件另行审核发布范围，`licenses/` 仅保存明确指定的公开测试文件。
5. 将附件发布到 GitHub Releases，预览版继续标记为 pre-release。不得静默覆盖已发布附件或移动标签来修正构建，应发布新版本并说明更正。
6. 上传后逐项验证下载 URL 与哈希，更新主页和文档索引。纯文档提交不产生产品版本，也不修改历史标签。

原有 5 个发行组和 15 个附件继续保留。原始发布时间与迁移时间分别记录。发行标签、安装包签名、SHA-256 与法律接受记录证明不同事实，应分别保存依据。

## 法律与运营记录

正式 LICENSE/EULA 文本和修订应可追溯。网站更新不追溯改变已接受的协议或历史已授予权利。商业交付需要核实法律主体、授权依据、实际数据处理告知、支持条款，以及逐版本依赖/源码覆盖。未核实事项不标记为完成。

公开 Issue 接收脱敏产品和文档反馈。权利、私有授权和安全报告使用[私密联系渠道](../../SECURITY.zh-CN.md)，提交变更遵循[贡献说明](../../CONTRIBUTING.zh-CN.md)。

## 架构参考

本次参考 [VS Code](https://github.com/microsoft/vscode)、[PowerToys](https://github.com/microsoft/PowerToys) 与 [Ollama](https://github.com/ollama/ollama) 的产品首页、独立文档、清晰下载、贡献/安全说明和仓库自动化组织方式。其许可、商标、支持承诺及功能声明不转移到本项目。

平台依据：[GitHub 许可说明](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository) · [GitHub 发行与标签](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)。
