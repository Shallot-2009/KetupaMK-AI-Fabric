# KetupaMK-AI-Fabric

[English](README.md) · [简体中文](README.zh-CN.md) · [文档](docs/README.md) · [版本](docs/releases/README.md) · [标签](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/tags)

KetupaMK 是面向**模拟 IC、信道算法、先进封装、Interposer 中介层，以及信号完整性与电源完整性（SI/PI）**的 CIR 工程自动化平台，连接 PCB/封装/互连工作流、Touchstone 信道分析与 AI 辅助输入准备，提供 Windows 和 Linux 发行环境。

按需查看[技术方向](docs/product/DOMAINS.md)、[产品功能](docs/product/README.md)或[项目结构导航](docs/PROJECT_MAP.md)。CIR 配置全局变量，include 模块描述具体工程，兼容的 EDA 工具负责执行相应工程任务。

本仓库是 KetupaMK 的公开发行与文档仓库。现行产品的专有核心源码单独维护；Windows/Linux 安装包、运行环境发行版、测试授权文件和第三方材料在此发布。

**项目起源与基础：[Ketupa_v0.0.3](history/Ketupa_v0.0.3/)。** 原项目整体保留，是本项目演进的基础：111 个跟踪文件、原始目录结构、作者署名、LICENSE、NOTICE 及工程资料均原样归档。原 Git 提交历史与 [`legacy-v0.0.3` 标签](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/tree/legacy-v0.0.3)继续保留。详见[项目起源记录](history/ORIGIN.md)。

项目始于 **2023 年**，维护者确认 **2024 年 5—6 月**已有早期项目提交。当前仓库可核对的最早 Git 留存日期为 2025-06-20，不能将其当作项目起点。完整时间线与来源标注见[项目沿革](history/ORIGIN.md)。

## 主要功能

| 领域 | 1.0.2 已发布的功能范围 |
| --- | --- |
| CIR 工作流管理 | 统一入口、工程 include、工程队列与网络 worker，组织既有 PKG、PCB 和 Merge 工作流 |
| 封装与互连配置 | bump、solderball、芯片朝向、端口阻抗、混合单位扫频及可追溯输出命名 |
| DDR 报告 | `.tap` 读取 Touchstone、显式端口映射与规范，向 Excel 输出 S21 延迟和相对 skew |
| AI 集成 | 网络清单、分类映射、Excel 预处理，以及可选的 Skill/Agent/MCP 接入 |
| 操作接口 | Windows Launcher、Linux CLI，以及带鉴权的本地 HTTPS 接口和前端 SDK |
| GDS Interposer | 导入辅助；当前公开范围不包含求解或电气签核 |

涉及外部工程工具的工作流需要兼容的 EDA 软件、厂商许可、获准使用的工程输入，以及适用版本的 KetupaMK 授权。各功能的版本范围见[产品说明](docs/product/README.md)。

<a id="downloads"></a>
<a id="downloads-zh"></a>

## 下载安装包

**当前预览版 KetupaMK 1.0.3** — [Windows EXE](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.3/Ketupa-AI-Fabric-1.0.3-Windows-x64-Setup.exe) · [Linux TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.3/ketupa-ai-fabric-linux-1.0.3-x64.tar.gz) · [Linux DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.3/ketupa-ai-fabric-linux_1.0.3_amd64.deb)

Windows 选择 EXE。Linux 在 DEB 和 TAR.GZ 中任选一种。Rocky/RHEL 8 和 Ubuntu 20.04 可选下方的旧版 Linux 兼容环境。[1.0.3 下载与安装](docs/releases/openketupamk-v1.0.3.md)

| 发行版本 | 状态 | Windows x64 | Linux x64 | Linux amd64 |
| --- | --- | --- | --- | --- |
| [KetupaMK 1.0.2](docs/releases/openketupamk-v1.0.2.md) | 预发布 | [EXE](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.2/openketupa-ai-fabric-1.0.2-Windows-x64-Setup.exe) | [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.2/openketupa-ai-fabric-linux-1.0.2-x64.tar.gz) | [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.2/openketupa-ai-fabric-linux_1.0.2_amd64.deb) |
| [KetupaMK 1.0.1](docs/releases/openketupamk-v1.0.1.md) | 预发布 | [EXE](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.1/Ketupa-AI-Fabric-1.0.1-Windows-x64-Setup.exe) | [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.1/ketupa-ai-fabric-linux-1.0.1-x64.tar.gz) | [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.1/ketupa-ai-fabric-linux_1.0.1_amd64.deb) |
| [KetupaMK 1.0.0](docs/releases/openketupamk-v1.0.0.md) | 历史正式发行 | [EXE](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.0/openketupa-1.0.0-Windows-x64-Setup.exe) | [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.0/openketupa-1.0.0-Linux-x64.tar.gz) | [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.0/openketupa-1.0.0-linux-amd64.deb) |
| [Runtime 1.0.0](docs/releases/openketupamk-runtime-v1.0.0.md) | 历史正式发行 | [EXE](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-runtime-v1.0.0/ketupa-runtime-1.0.0-Windows-x64-Setup.exe) | [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-runtime-v1.0.0/ketupa-runtime-1.0.0-Linux-x64.tar.gz) | [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-runtime-v1.0.0/ketupa-runtime-installer_1.0.0_amd64.deb) |
| [Beta](docs/releases/openketupamk-beta.md) | 预发布 | [EXE](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-beta/openketupa-Beta-Windows-x64-Setup.exe) | [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-beta/openketupa-Beta-linux-x64.tar.gz) | [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-beta/openketupa-Beta-linux-amd64.deb) |

<a id="legacy-linux"></a>

### 旧版 Linux 兼容环境 · 1.0.2

适用于 Rocky/RHEL 8、Ubuntu 20.04 等较旧用户空间，要求 **x86_64、glibc ≥ 2.28**。四种格式任选一种，均为 Linux 应用与运行环境安装包。

| 目标平台 / 安装方式 | 直接下载 |
| --- | --- |
| Rocky / RHEL 8 | [RPM](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-kernel-legacy-v1.0.2/ketupa-ai-fabric-kernel-legacy-1.0.2-1.x86_64.rpm) |
| Ubuntu 20.04 / Debian | [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-kernel-legacy-v1.0.2/ketupa-ai-fabric-kernel-legacy_1.0.2_amd64.deb) |
| 自解压安装 | [RUN](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-kernel-legacy-v1.0.2/ketupa-ai-fabric-kernel-legacy-1.0.2-x64.run) |
| 独立目录安装 | [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-kernel-legacy-v1.0.2/ketupa-ai-fabric-kernel-legacy-1.0.2-x64.tar.gz) |

[兼容版说明与验证范围](docs/releases/openketupamk-kernel-legacy-v1.0.2.md) · [Release](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/tag/openketupamk-kernel-legacy-v1.0.2) · [标签页](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/tags)

每个安装目录使用一种格式。运行工程前，请确认目标系统依赖和 EDA 工具兼容性。

[安装说明](docs/installation/README.md) · [下载 SHA256SUMS](https://raw.githubusercontent.com/Shallot-2009/KetupaMK-AI-Fabric/main/SHA256SUMS) · [发行说明](docs/releases/README.md)

Runtime 1.0.0 为独立发行组。请在发行附件中选择适合系统的安装包。


<!-- legacy-mirrors:start -->
同一套旧版 Linux 兼容安装包也保留在主 1.0.2 发布页：[DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.2/openketupa-ai-fabric-kernel-legacy_1.0.2_amd64.deb) · [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.2/openketupa-ai-fabric-kernel-legacy-1.0.2-x64.tar.gz) · [RPM](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.2/openketupa-ai-fabric-kernel-legacy-1.0.2-1.x86_64.rpm) · [RUN](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.2/openketupa-ai-fabric-kernel-legacy-1.0.2-x64.run)
<!-- legacy-mirrors:end -->

<a id="licenses"></a>
<a id="licenses-zh"></a>

## 测试授权与软件条款

下列链接打开对应 GitHub 文件页，在页面点击 **Download raw file** 保存 `.lic`。

1. [离线测试](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/blob/main/licenses/openketupamk-offline-test-12w.lic)
2. [内部测试](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/blob/main/licenses/openketupamk-internal-test-12w.lic)

[选用与激活步骤](licenses/README.md)。

`.lic` 是软件使用授权文件，与著作权许可文件含义不同。适用版本、模块、设备和有效期依原文件及软件验证执行；下载不会续期，也不直接授予商用权利。

| 资料范围 | 适用条款 |
| --- | --- |
| v0.0.3 原作者有权许可的历史源码 | [归档 Apache-2.0 LICENSE](history/Ketupa_v0.0.3/LICENSE) 与 [NOTICE](history/Ketupa_v0.0.3/NOTICE)；此前 BSD-2-Clause 授权继续保留 |
| 现行专有产品 | [LICENSE.txt](LICENSE.txt)、[EULA.md](EULA.md#中文)及适用的有效书面协议 |
| 第三方组件及工程资料 | 各自的条款、声明与源码提供义务，见[第三方材料](third-party/README.md) |

详见[许可范围](LICENSE.md)与[商业交付检查](docs/governance/REVIEW.md)。本仓库没有一份覆盖全部资料的统一开源许可。

## 仓库结构

```text
KetupaMK-AI-Fabric/
├── docs/          产品、安装、发行说明、维护规范与来源记录
├── history/       Ketupa_v0.0.3 基础项目、起源记录和保全清单
├── licenses/      公开测试 LIC、使用说明与校验值
├── releases/      安装包清单与固定标签映射
├── third-party/   第三方声明与对应源码归档
├── tools/         仓库完整性检查
└── .github/       自动检查与问题模板
```

`main` 维护当前文档与发行导航。标签固定历史快照：`legacy-v0.0.3` 保存原项目，`openketupamk-v*` 对应产品发行，`openketupamk-runtime-v*` 对应 Runtime，`openketupamk-kernel-legacy-v*` 对应旧版 Linux 兼容环境。标签是固定引用，不是分支。详见[分支与发行规范](docs/governance/README.md)。

## 文档与联系

[文档索引](docs/README.md) · [基础项目归档](history/README.md) · [迁移记录](docs/MIGRATION.md) · [安全报告](SECURITY.md)

当前公开作者署名为 **Asenjo HB**；基础项目的原始署名 **Asenjo.HB.L.** 完整保留。本仓库由原 GitHub 仓库延续更名，保留仓库身份、star、fork 关系及 Issues。

授权、权利与私密安全报告联系：[asenjoaupa@gmail.com](mailto:asenjoaupa@gmail.com) · [3405802009@qq.com](mailto:3405802009@qq.com)。公开 Issue 用于可复现的产品和文档问题；提交前请移除客户资料和私有授权文件。
