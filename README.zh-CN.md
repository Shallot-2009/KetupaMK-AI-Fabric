# KetupaMK-AI-Fabric

简体中文 · [English](README.md) · [项目历史](history/README.md) · [版本下载](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases)

本仓库延续 Ketupa 项目：原 **Ketupa_v0.0.3** 项目整体归档于 [`history/Ketupa_v0.0.3/`](history/Ketupa_v0.0.3/)，完整保留其源码、文档、资源及工程文件；现行 **KetupaMK** 安装包、运行环境发行版、授权资料和必要第三方源码统一在此维护。

本仓库由原 `Shallot-2009/Ketupa_v0.0.3` 直接更名为 `KetupaMK-AI-Fabric`，保留原仓库身份、star、fork 关系和既有 Issues；原 `Ketupa-AI-Fabric` 发行仓库内容已整合至此。后者的 1 个 star 不会转入或叠加到本仓库。详见[迁移记录](docs/MIGRATION.md)。

## 下载安装包

共 **5 个发行组、15 个安装包**。Runtime 1.0.0 与普通 1.0.0 为独立发行组。安装包保留原始文件名和字节，包括历史上的 `OpenKetupa`、`Ketupa-AI-Fabric` 命名；下表保留来源 Release 的正式/预发布标记。

| Version / 版本 | Status / 状态 | Windows x64 | Linux x64 | Linux amd64 |
| --- | --- | --- | --- | --- |
| [KetupaMK 1.0.2](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/tag/openketupamk-v1.0.2) | Pre-release / 预发布 | [EXE](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.2/openketupa-ai-fabric-1.0.2-Windows-x64-Setup.exe) | [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.2/openketupa-ai-fabric-linux-1.0.2-x64.tar.gz) | [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.2/openketupa-ai-fabric-linux_1.0.2_amd64.deb) |
| [KetupaMK 1.0.1](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/tag/openketupamk-v1.0.1) | Pre-release / 预发布 | [EXE](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.1/Ketupa-AI-Fabric-1.0.1-Windows-x64-Setup.exe) | [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.1/ketupa-ai-fabric-linux-1.0.1-x64.tar.gz) | [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.1/ketupa-ai-fabric-linux_1.0.1_amd64.deb) |
| [KetupaMK 1.0.0](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/tag/openketupamk-v1.0.0) | Release / 正式发布 | [EXE](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.0/openketupa-1.0.0-Windows-x64-Setup.exe) | [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.0/openketupa-1.0.0-Linux-x64.tar.gz) | [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.0/openketupa-1.0.0-linux-amd64.deb) |
| [KetupaMK Runtime 1.0.0](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/tag/openketupamk-runtime-v1.0.0) | Release / 正式发布 | [EXE](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-runtime-v1.0.0/ketupa-runtime-1.0.0-Windows-x64-Setup.exe) | [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-runtime-v1.0.0/ketupa-runtime-1.0.0-Linux-x64.tar.gz) | [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-runtime-v1.0.0/ketupa-runtime-installer_1.0.0_amd64.deb) |
| [KetupaMK Beta](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/tag/openketupamk-beta) | Pre-release / 预发布 | [EXE](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-beta/openketupa-Beta-Windows-x64-Setup.exe) | [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-beta/openketupa-Beta-linux-x64.tar.gz) | [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-beta/openketupa-Beta-linux-amd64.deb) |

Linux 的 TAR.GZ 和 DEB 二选一，无需重复安装。安装包位于本仓库的 Releases，不在 Git 工作目录重复存放。GitHub 自动生成的 Source code ZIP/TAR 是仓库资料快照，不是产品安装包。

使用 [SHA256SUMS](SHA256SUMS) 核验下载文件。[发行清单](releases/manifest.json)记录原始发布时间、准确文件名、字节数、SHA-256 和现行下载地址。原发行仓库 README 的三个 1.0.2 校验值已过时，现已按实际附件修正；迁移前的 README 作为[来源记录](docs/provenance/Ketupa-AI-Fabric-README.before-migration.md)原样保留。

## 安装与工程环境

请参阅[中文安装说明](docs/INSTALLATION.zh-CN.md)、[English installation guide](docs/INSTALLATION.en.md)及所选版本的说明。1.0.2 仍为**预发布版**；其公开功能说明包括受许可证控制的 CIR 工作流入口、AI 预处理与集成资料、Windows Launcher、Linux CLI 和仅导入的 GDS Interposer 流程，具体范围与限制见 [1.0.2 发行说明](docs/releases/openketupamk-v1.0.2.md)。

安装包提供该版本打包的软件与运行环境，不提供 Ansys、Cadence、MATLAB、Polar 等第三方商业授权。实际工程仍需兼容的外部 EDA 工具、经批准的输入数据及适用的 KetupaMK 许可证。本次仓库迁移验证资料保留和下载一致性，不代表完成实际安装、物理仿真验收或工程签核。

已有、经作者公开的[内测许可证](licenses/README.md#internal-test)保留原始字节，说明统一汇入许可证目录。其签名范围、版本适用性和有效期仍以原文件为准；迁移不会续期或扩大授权。

维护者公开的[离线测试 LIC](licenses/README.md#offline-test)现已同步；两类文件的入口与范围见[许可证目录](licenses/README.md)。

## 项目起源与历史归档

Ketupa v0.0.3 是本项目的起源。原始 README 记载初始发行日期为 **2025 年 8 月 14 日**，作者署名为 **Asenjo.HB.L.**，研究内容涉及 HFSS 贴片天线、传输线、测量相关性、MATLAB/CNN 探索、LLM 交互及桌面自动化。这些属于历史描述，不构成当前产品的验收声明。保留的 Git 历史起于 **2025 年 6 月 20 日**；Git 首次提交日期与 README 记载的发行日期分别描述不同事件。

归档保留原提交 `b5f44c111fef3d32b5cdeb3c18d4af40e5c81306` 的全部 **111 个跟踪文件**，包括原始内容、版权声明、许可、NOTICE 和工程资料。[`legacy-v0.0.3` 标签](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/tree/legacy-v0.0.3)保留历史根目录结构；两个来源仓库的原始提交历史均通过整合 merge 保留。

请先阅读[历史归档指南](history/README.md)。原有安装命令、路径和依赖名称可能已经过时，归档不暗中改写这些历史记录。时间线与来源清单见 [ORIGIN.md](history/ORIGIN.md)。

## 许可范围

| 资料范围 | 适用条款 |
| --- | --- |
| `history/Ketupa_v0.0.3/` 中原作者有权许可的 v0.0.3 源代码 | [归档 Apache-2.0 LICENSE](history/Ketupa_v0.0.3/LICENSE) 与[原始 NOTICE](history/Ketupa_v0.0.3/NOTICE)；此前 BSD-2-Clause 副本保留原有授权 |
| 现行第一方专有产品与产品资料 | [LICENSE.txt](LICENSE.txt)、[EULA.md](EULA.md)及适用的有效书面协议 |
| 第三方组件、许可与源码归档 | 各自独立许可，见 [third-party/README.md](third-party/README.md) |
| 历史归档内的第三方工程文件、文档、数据及生成资料 | 保留各自独立适用的权利；项目源码许可不自动覆盖它们 |

详见中英文[许可边界说明](LICENSE.md)与 [NOTICE](NOTICE)。公开可下载及历史开源授权不意味着现行专有产品开源；现行专有条款也不追溯撤销 v0.0.3 与第三方材料已合法授予的权利。原文件名中的 `OpenKetupa` 是历史产品标识，不构成开源授权。

## 作者与联系

当前公开署名：**Asenjo HB**；v0.0.3 原有署名 **Asenjo.HB.L.** 保留在历史归档中。

邮箱：[asenjoaupa@gmail.com](mailto:asenjoaupa@gmail.com) · [3405802009@qq.com](mailto:3405802009@qq.com)
GitHub：[Shallot-2009](https://github.com/Shallot-2009/) · [asen-tech.com](https://asen-tech.com)
