# 版本与下载 / Releases and downloads

[Home / 项目主页](../../README.md) · [Documentation / 文档](../README.md)

点击语言标题即可在本页切换；另一语言会自动折叠。 / Select a language below; the other section collapses on this page.

<details name="readme-language">
<summary><strong>English</strong></summary>

Select a distribution below. **1.0.2 is the current preview**, not a promoted production release. The original pre-release flags are retained.

| Distribution | Status | Windows x64 | Linux x64 | Linux amd64 |
| --- | --- | --- | --- | --- |
| [KetupaMK 1.0.2](openketupamk-v1.0.2.md) | Pre-release | [EXE](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.2/openketupa-ai-fabric-1.0.2-Windows-x64-Setup.exe) | [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.2/openketupa-ai-fabric-linux-1.0.2-x64.tar.gz) | [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.2/openketupa-ai-fabric-linux_1.0.2_amd64.deb) |
| [KetupaMK 1.0.1](openketupamk-v1.0.1.md) | Pre-release | [EXE](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.1/Ketupa-AI-Fabric-1.0.1-Windows-x64-Setup.exe) | [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.1/ketupa-ai-fabric-linux-1.0.1-x64.tar.gz) | [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.1/ketupa-ai-fabric-linux_1.0.1_amd64.deb) |
| [KetupaMK 1.0.0](openketupamk-v1.0.0.md) | Historical release | [EXE](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.0/openketupa-1.0.0-Windows-x64-Setup.exe) | [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.0/openketupa-1.0.0-Linux-x64.tar.gz) | [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.0/openketupa-1.0.0-linux-amd64.deb) |
| [Runtime 1.0.0](openketupamk-runtime-v1.0.0.md) | Historical release | [EXE](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-runtime-v1.0.0/ketupa-runtime-1.0.0-Windows-x64-Setup.exe) | [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-runtime-v1.0.0/ketupa-runtime-1.0.0-Linux-x64.tar.gz) | [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-runtime-v1.0.0/ketupa-runtime-installer_1.0.0_amd64.deb) |
| [Beta](openketupamk-beta.md) | Pre-release | [EXE](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-beta/openketupa-Beta-Windows-x64-Setup.exe) | [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-beta/openketupa-Beta-linux-x64.tar.gz) | [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-beta/openketupa-Beta-linux-amd64.deb) |

<a id="legacy-linux-en"></a>

### Legacy Linux environments · 1.0.2

For older userspaces such as Rocky/RHEL 8 and Ubuntu 20.04: **x86_64, glibc ≥ 2.28**. Choose one of four Linux application/runtime installer formats.

| Target / installation method | Direct download |
| --- | --- |
| Rocky / RHEL 8 | [RPM](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-kernel-legacy-v1.0.2/ketupa-ai-fabric-kernel-legacy-1.0.2-1.x86_64.rpm) |
| Ubuntu 20.04 / Debian | [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-kernel-legacy-v1.0.2/ketupa-ai-fabric-kernel-legacy_1.0.2_amd64.deb) |
| Self-extracting installation | [RUN](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-kernel-legacy-v1.0.2/ketupa-ai-fabric-kernel-legacy-1.0.2-x64.run) |
| Dedicated-prefix installation | [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-kernel-legacy-v1.0.2/ketupa-ai-fabric-kernel-legacy-1.0.2-x64.tar.gz) |

[Compatibility notes and tested scope](openketupamk-kernel-legacy-v1.0.2.md) · [Release](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/tag/openketupamk-kernel-legacy-v1.0.2) · [Tags](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/tags)

This distribution remains a pre-release. Recorded acceptance covers isolated EL8.1 and Ubuntu 20.04 userspaces, not native Rocky kernels or EDA solving. Keep compatibility and standard payloads out of the same installation prefix.

There are six public release groups with nineteen installer assets. Runtime 1.0.0 and product 1.0.0 are separate distributions. Names and installer bytes are preserved. Download an installer for your platform, then follow the [installation guide](../installation/README.md) and verify [SHA256SUMS](../../SHA256SUMS).

| Reference | Meaning |
| --- | --- |
| `main` | Current documentation, download links, and preservation records |
| `openketupamk-v*` | Product release snapshots |
| `openketupamk-runtime-v*` | Runtime snapshots |
| `openketupamk-kernel-legacy-v*` | Legacy Linux application/runtime compatibility snapshots |
| `openketupamk-beta` | Preserved historical Beta snapshot |
| `legacy-v0.0.3` | Foundational project in its original root layout |

[Browse GitHub tags](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/tags) · [Browse releases](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases). The [tag map](../../releases/tag-map.json) records exact commits. Several historical distribution tags share a documentation commit; their separate installer assets remain distinct. Existing tags keep their original targets, even when the current `main` layout differs. [Publishing policy](../governance/README.md).

GitHub-generated Source code archives contain the tagged repository snapshot, not protected product installers. Original publication times are retained in the [release manifest](../../releases/manifest.json); GitHub's migrated-release timestamps describe the later migration.

</details>

<details name="readme-language" open>
<summary><strong>简体中文</strong></summary>

在下表选择发行组。**1.0.2 是当前预览版**，未被提升为生产正式版；原有预发布标记继续保留。

| 发行版本 | 状态 | Windows x64 | Linux x64 | Linux amd64 |
| --- | --- | --- | --- | --- |
| [KetupaMK 1.0.2](openketupamk-v1.0.2.md) | 预发布 | [EXE](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.2/openketupa-ai-fabric-1.0.2-Windows-x64-Setup.exe) | [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.2/openketupa-ai-fabric-linux-1.0.2-x64.tar.gz) | [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.2/openketupa-ai-fabric-linux_1.0.2_amd64.deb) |
| [KetupaMK 1.0.1](openketupamk-v1.0.1.md) | 预发布 | [EXE](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.1/Ketupa-AI-Fabric-1.0.1-Windows-x64-Setup.exe) | [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.1/ketupa-ai-fabric-linux-1.0.1-x64.tar.gz) | [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.1/ketupa-ai-fabric-linux_1.0.1_amd64.deb) |
| [KetupaMK 1.0.0](openketupamk-v1.0.0.md) | 历史正式发行 | [EXE](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.0/openketupa-1.0.0-Windows-x64-Setup.exe) | [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.0/openketupa-1.0.0-Linux-x64.tar.gz) | [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.0/openketupa-1.0.0-linux-amd64.deb) |
| [Runtime 1.0.0](openketupamk-runtime-v1.0.0.md) | 历史正式发行 | [EXE](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-runtime-v1.0.0/ketupa-runtime-1.0.0-Windows-x64-Setup.exe) | [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-runtime-v1.0.0/ketupa-runtime-1.0.0-Linux-x64.tar.gz) | [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-runtime-v1.0.0/ketupa-runtime-installer_1.0.0_amd64.deb) |
| [Beta](openketupamk-beta.md) | 预发布 | [EXE](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-beta/openketupa-Beta-Windows-x64-Setup.exe) | [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-beta/openketupa-Beta-linux-x64.tar.gz) | [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-beta/openketupa-Beta-linux-amd64.deb) |

<a id="legacy-linux-zh"></a>

### 旧版 Linux 兼容环境 · 1.0.2

适用于 Rocky/RHEL 8、Ubuntu 20.04 等较旧用户空间，要求 **x86_64、glibc ≥ 2.28**。四种格式任选一种，均为 Linux 应用与运行环境安装包。

| 目标平台 / 安装方式 | 直接下载 |
| --- | --- |
| Rocky / RHEL 8 | [RPM](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-kernel-legacy-v1.0.2/ketupa-ai-fabric-kernel-legacy-1.0.2-1.x86_64.rpm) |
| Ubuntu 20.04 / Debian | [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-kernel-legacy-v1.0.2/ketupa-ai-fabric-kernel-legacy_1.0.2_amd64.deb) |
| 自解压安装 | [RUN](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-kernel-legacy-v1.0.2/ketupa-ai-fabric-kernel-legacy-1.0.2-x64.run) |
| 独立目录安装 | [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-kernel-legacy-v1.0.2/ketupa-ai-fabric-kernel-legacy-1.0.2-x64.tar.gz) |

[兼容版说明与验证范围](openketupamk-kernel-legacy-v1.0.2.md) · [Release](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/tag/openketupamk-kernel-legacy-v1.0.2) · [标签页](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/tags)

本组保持预发布状态。已有验收为 EL8.1 与 Ubuntu 20.04 隔离用户空间测试，未覆盖 Rocky 真机内核或 EDA 求解。兼容构建与标准构建不要混装到同一目录。

当前有 6 个公开发行组、19 个安装包。Runtime 1.0.0 与产品 1.0.0 为独立发行组，安装包名称和字节保持原样。选择适合平台的安装包后，参阅[安装说明](../installation/README.md)，并用 [SHA256SUMS](../../SHA256SUMS) 核对。

| 引用 | 含义 |
| --- | --- |
| `main` | 当前文档、下载导航与保全记录 |
| `openketupamk-v*` | 产品发行快照 |
| `openketupamk-runtime-v*` | Runtime 快照 |
| `openketupamk-kernel-legacy-v*` | 旧版 Linux 应用与运行环境兼容快照 |
| `openketupamk-beta` | 保留的历史 Beta 快照 |
| `legacy-v0.0.3` | 保留原始根目录布局的基础项目 |

[GitHub 标签页](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/tags) · [Releases 页](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases)。[标签映射](../../releases/tag-map.json)记录准确提交。部分历史发行标签共用一个文档提交，其安装包附件仍为不同发行组。既有标签继续指向原提交，不因当前 `main` 目录变化而重新指向。详见[发布规范](../governance/README.md)。

GitHub 自动生成的 Source code 归档包含标签对应的仓库快照，不包含受保护的产品安装器。[发行清单](../../releases/manifest.json)记录原始发布时间；GitHub 上迁移后的发布时间反映后续迁移。

</details>
