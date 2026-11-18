# KetupaMK-AI-Fabric

简体中文 · [English](README.md) · [文档](docs/README.zh-CN.md)

KetupaMK 面向 PCB、封装与互连建模，使用 CIR 配置文件组织工程输入、调用兼容的 EDA 工具并归集可追溯结果。1.0.2 同时提供 DDR Touchstone 延迟与偏斜报告，以及 AI 辅助的网络数据准备功能。

本仓库是 KetupaMK 的公开发行与文档仓库。现行产品的专有核心源码单独维护；Windows/Linux 安装包、运行环境发行版、测试授权文件和第三方材料在此发布。

**项目起源与基础：[Ketupa_v0.0.3](history/Ketupa_v0.0.3/)。** 原项目整体保留，是本项目演进的基础：111 个跟踪文件、原始目录结构、作者署名、LICENSE、NOTICE 及工程资料均原样归档。原 Git 提交历史与 [`legacy-v0.0.3` 标签](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/tree/legacy-v0.0.3)继续保留。详见[项目起源记录](history/ORIGIN.zh-CN.md)。

## 主要功能

| 领域 | 1.0.2 已发布的功能范围 |
| --- | --- |
| CIR 工作流管理 | 统一入口、工程 include、工程队列与网络 worker，组织既有 PKG、PCB 和 Merge 工作流 |
| 封装与互连配置 | bump、solderball、芯片朝向、端口阻抗、混合单位扫频及可追溯输出命名 |
| DDR 报告 | `.tap` 读取 Touchstone、显式端口映射与规范，向 Excel 输出 S21 延迟和相对 skew |
| AI 集成 | 网络清单、分类映射、Excel 预处理，以及可选的 Skill/Agent/MCP 接入 |
| 操作接口 | Windows Launcher、Linux CLI，以及带鉴权的本地 HTTPS 接口和前端 SDK |
| GDS Interposer | 导入辅助；当前公开范围不包含求解或电气签核 |

涉及外部工程工具的工作流需要兼容的 EDA 软件、厂商许可、获准使用的工程输入，以及适用版本的 KetupaMK 授权。各功能的版本范围见[产品说明](docs/product/README.zh-CN.md)。

<a id="downloads"></a>

## 下载安装包

**当前预览版：KetupaMK 1.0.2** — [Windows EXE](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.2/openketupa-ai-fabric-1.0.2-Windows-x64-Setup.exe) · [Linux TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.2/openketupa-ai-fabric-linux-1.0.2-x64.tar.gz) · [Linux DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.2/openketupa-ai-fabric-linux_1.0.2_amd64.deb)

点击上述链接直接下载安装包。Linux 的 TAR.GZ 与 DEB 二选一。1.0.2 仍为预发布版，请按实际工作流选择版本并验证。

| 发行版本 | 状态 | Windows x64 | Linux x64 | Linux amd64 |
| --- | --- | --- | --- | --- |
| [KetupaMK 1.0.2](docs/releases/openketupamk-v1.0.2.zh-CN.md) | 预发布 | [EXE](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.2/openketupa-ai-fabric-1.0.2-Windows-x64-Setup.exe) | [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.2/openketupa-ai-fabric-linux-1.0.2-x64.tar.gz) | [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.2/openketupa-ai-fabric-linux_1.0.2_amd64.deb) |
| [KetupaMK 1.0.1](docs/releases/openketupamk-v1.0.1.zh-CN.md) | 预发布 | [EXE](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.1/Ketupa-AI-Fabric-1.0.1-Windows-x64-Setup.exe) | [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.1/ketupa-ai-fabric-linux-1.0.1-x64.tar.gz) | [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.1/ketupa-ai-fabric-linux_1.0.1_amd64.deb) |
| [KetupaMK 1.0.0](docs/releases/openketupamk-v1.0.0.zh-CN.md) | 历史正式发行 | [EXE](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.0/openketupa-1.0.0-Windows-x64-Setup.exe) | [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.0/openketupa-1.0.0-Linux-x64.tar.gz) | [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.0/openketupa-1.0.0-linux-amd64.deb) |
| [Runtime 1.0.0](docs/releases/openketupamk-runtime-v1.0.0.zh-CN.md) | 历史正式发行 | [EXE](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-runtime-v1.0.0/ketupa-runtime-1.0.0-Windows-x64-Setup.exe) | [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-runtime-v1.0.0/ketupa-runtime-1.0.0-Linux-x64.tar.gz) | [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-runtime-v1.0.0/ketupa-runtime-installer_1.0.0_amd64.deb) |
| [Beta](docs/releases/openketupamk-beta.zh-CN.md) | 预发布 | [EXE](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-beta/openketupa-Beta-Windows-x64-Setup.exe) | [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-beta/openketupa-Beta-linux-x64.tar.gz) | [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-beta/openketupa-Beta-linux-amd64.deb) |

[安装说明](docs/installation/README.zh-CN.md) · [下载 SHA256SUMS](https://raw.githubusercontent.com/Shallot-2009/KetupaMK-AI-Fabric/main/SHA256SUMS) · [发行说明](docs/releases/README.zh-CN.md)

Runtime 1.0.0 是独立发行组。安装包保留原始名称、字节与发行状态。GitHub 自动生成的 **Source code** ZIP/TAR 是仓库快照；产品安装包为上表中的 EXE、DEB 和 TAR.GZ 附件。

<a id="licenses"></a>

## 测试授权与软件条款

维护者公开的测试文件：[离线测试 LIC](https://raw.githubusercontent.com/Shallot-2009/KetupaMK-AI-Fabric/main/licenses/Ketupa-ketupamk_offline_test_12w-20261116-232329-233.lic) · [内测 LIC](https://raw.githubusercontent.com/Shallot-2009/KetupaMK-AI-Fabric/main/licenses/openketupamk-internal-test-12w.lic) · [使用说明与校验值](licenses/README.zh-CN.md)。

`.lic` 是软件使用授权文件，与著作权许可文件含义不同。适用版本、模块、设备和有效期依原文件及软件验证执行；下载不会续期，也不直接授予商用权利。

| 资料范围 | 适用条款 |
| --- | --- |
| v0.0.3 原作者有权许可的历史源码 | [归档 Apache-2.0 LICENSE](history/Ketupa_v0.0.3/LICENSE) 与 [NOTICE](history/Ketupa_v0.0.3/NOTICE)；此前 BSD-2-Clause 授权继续保留 |
| 现行专有产品 | [LICENSE.txt](LICENSE.txt)、[EULA.md](EULA.md#中文)及适用的有效书面协议 |
| 第三方组件及工程资料 | 各自的条款、声明与源码提供义务，见[第三方材料](third-party/README.zh-CN.md) |

详见[许可范围](LICENSE.zh-CN.md)与[商业交付检查](docs/governance/REVIEW.zh-CN.md)。本仓库没有一份覆盖全部资料的统一开源许可。

## 仓库结构

```text
KetupaMK-AI-Fabric/
├── docs/          产品、安装、发行说明、维护规范与来源记录
├── history/       Ketupa_v0.0.3 基础项目、起源记录和保全清单
├── licenses/      公开测试 LIC、使用说明与校验值
├── releases/      安装包清单与固定标签映射
├── third-party/   第三方声明与对应源码归档
├── tools/         仓库完整性检查
└── .github/       自动检查与贡献模板
```

`main` 维护当前文档与发行导航。标签固定历史快照：`legacy-v0.0.3` 保存原项目，`openketupamk-v*` 对应产品发行，`openketupamk-runtime-v*` 对应 Runtime。标签是固定引用，不是分支。详见[分支与发行规范](docs/governance/README.zh-CN.md)。

## 文档与联系

[文档索引](docs/README.zh-CN.md) · [基础项目归档](history/README.zh-CN.md) · [迁移记录](docs/MIGRATION.zh-CN.md) · [贡献说明](CONTRIBUTING.zh-CN.md) · [安全报告](SECURITY.zh-CN.md)

当前公开作者署名为 **Asenjo HB**；基础项目的原始署名 **Asenjo.HB.L.** 完整保留。本仓库由原 GitHub 仓库延续更名，保留仓库身份、star、fork 关系及 Issues。

授权、权利与私密安全报告联系：[asenjoaupa@gmail.com](mailto:asenjoaupa@gmail.com) · [3405802009@qq.com](mailto:3405802009@qq.com)。公开 Issue 用于可复现的产品和文档问题；提交前请移除客户资料和私有授权文件。
