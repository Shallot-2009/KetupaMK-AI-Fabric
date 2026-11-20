# KetupaMK 1.0.2 · 旧版 Linux 兼容环境 / Legacy Linux environment

[Home / 项目主页](../../README.md) · [Documentation / 文档](../README.md)

点击语言标题即可在本页切换；另一语言会自动折叠。 / Select a language below; the other section collapses on this page.

<details name="readme-language">
<summary><strong>English</strong></summary>

**Pre-release · Linux x86_64 / amd64 · application and runtime environment**

Tag: [`openketupamk-kernel-legacy-v1.0.2`](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/tree/openketupamk-kernel-legacy-v1.0.2) · [GitHub Release](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/tag/openketupamk-kernel-legacy-v1.0.2) · [All tags](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/tags)

This is the 1.0.2 compatibility distribution for older Linux userspaces, including Rocky/RHEL 8 and Ubuntu 20.04. It retains the 1.0.2 application scope while lowering the binary ABI baseline. It installs KetupaMK and its private runtime; it does not install or replace the Linux operating system, kernel, or host glibc. The `kernel-legacy` filename identifies this compatibility flavour, not a different historical application version.

## Download one format


<!-- current-assets:start -->
Rocky Linux 8.10 rebuild · 2026-11-20. Original filenames and tag targets retained; see the [new revision record](../../releases/legacy-rocky8-20261120.json) and [prior contact revision](../../releases/contact-refresh-20261119.json).

| Installer | Bytes |
| --- | --- |
| [ketupa-ai-fabric-kernel-legacy_1.0.2_amd64.deb](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-kernel-legacy-v1.0.2/ketupa-ai-fabric-kernel-legacy_1.0.2_amd64.deb) | 176,315,356 |
| [ketupa-ai-fabric-kernel-legacy-1.0.2-x64.tar.gz](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-kernel-legacy-v1.0.2/ketupa-ai-fabric-kernel-legacy-1.0.2-x64.tar.gz) | 175,341,549 |
| [ketupa-ai-fabric-kernel-legacy-1.0.2-1.x86_64.rpm](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-kernel-legacy-v1.0.2/ketupa-ai-fabric-kernel-legacy-1.0.2-1.x86_64.rpm) | 176,280,667 |
| [ketupa-ai-fabric-kernel-legacy-1.0.2-x64.run](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-kernel-legacy-v1.0.2/ketupa-ai-fabric-kernel-legacy-1.0.2-x64.run) | 175,342,502 |
<!-- current-assets:end -->

All four files deliver the same signed application/runtime environment in alternative formats. Choose one.

| System or need | Recommended format |
| --- | --- |
| Rocky/RHEL/AlmaLinux 8+ | RPM |
| Ubuntu 20.04 / Debian family, glibc 2.28+ | DEB; verify on the target host |
| Separate installation prefix | RUN; run --check first |
| Manual/offline extraction | TAR.GZ |

They are separate from the [standard Windows/Linux 1.0.2 distribution](openketupamk-v1.0.2.md) and the historical Runtime 1.0.0 distribution.

## System baseline

| Item | Recorded requirement or evidence |
| --- | --- |
| CPU / userspace | Linux x86_64 (amd64), glibc 2.28 or later; not ARM64, 32-bit, or musl/Alpine |
| Build userspace | Rocky Linux 8.10, GCC 8.5, glibc 2.28 |
| Recorded maximum required GLIBC symbol | GLIBC 2.28; other symbols require a separate audit for this build |
| Rocky / RHEL family | Rocky Linux 8+ / RHEL-compatible systems are the intended targets; RPM is the native package format |
| Debian / Ubuntu family | DEB format is available for glibc 2.28+; fresh target-host installation of this exact rebuild remains unverified |
| Host dependencies | glibc, libstdc++, libgcc, libgomp, libxcrypt and zlib as appropriate; the package manager resolves its declared dependencies |
| Python/runtime | Private Python runtime is bundled; target-host system dependencies still apply |
| Kernel support | No independently established minimum kernel version; userspace tests share the host kernel |

The inspected DEB declares `libc6 (>= 2.28), libstdc++6, libcrypt1, zlib1g, libgomp1`. Runtime bundling does not make system prerequisites optional. RPM/DEB dependency resolution may require configured repositories or locally supplied packages even though the application runtime is bundled.

## Installation and replacement

See the [four-format installation guide](../installation/README.md#legacy-linux-en) for exact commands. Stop active jobs and the affected license service before replacing an installation. Keep project workspaces and entitlement state outside the application prefix and preserve their records.

The compatibility DEB uses package name `ketupa-ai-fabric`, version `1.0.2`, and the usual `/opt/ketupa-ai-fabric` prefix. A package manager can therefore replace a standard build at the same version; it is not a second independent package. Do not mix formats or standard/compatibility payloads in one prefix. For a separate TAR/RUN installation, choose a separate prefix and command name and explicitly configure its service/entitlement ownership. `--replace` is an intentional replacement option, not a default recommendation.

## Recorded acceptance and limits

The 2026-11-20 Rocky Linux 8.10 build record reports 528 compiled native modules, a maximum required GLIBC symbol version of 2.28, verification of 9,354 signed payload files, RUN --check, RPM/DEB structure checks, and a RUN replacement install that preserved the valid license service. Full modeling on AEDT 2026R1, no-toggle acceptance on AEDT 2025R2, Mode 1 solving, fresh-system RPM/DEB installation, and physical signoff remain unverified for these exact files. The older 2026-11-17 acceptance belongs to the previous build. See the [current sanitized acceptance summary](../../releases/legacy-rocky8-20261120-acceptance.json) and [historical acceptance summary](../../releases/kernel-legacy-v1.0.2-acceptance.json).

## SHA-256

Download [SHA256SUMS](https://raw.githubusercontent.com/Shallot-2009/KetupaMK-AI-Fabric/main/SHA256SUMS) beside your selected installer, then run `sha256sum --ignore-missing -c SHA256SUMS`.

```text
e0ecf61d1544d5aacaaf8ea14e34eb54914b55bed9cf5be84867e17d0da98bdc  ketupa-ai-fabric-kernel-legacy_1.0.2_amd64.deb
de0c8d083e6a3568b07bca81ba4ceafa3bd58d943949a740968c6c134cb96511  ketupa-ai-fabric-kernel-legacy-1.0.2-x64.tar.gz
4c69b3dcb13fe9c7162d321adc50bcb30731e71cc78b6027e4e687bc6d8d91af  ketupa-ai-fabric-kernel-legacy-1.0.2-1.x86_64.rpm
c4c8d178cda9fb3156b2c122312e753c9f2215fc4a8211d0d7aeec53a7486adc  ketupa-ai-fabric-kernel-legacy-1.0.2-x64.run
```

## Terms, included documentation and provenance

The TAR payload contains `docs/Linux_Kernel_Legacy.md`, the other product guides, `dependency-inventory.json`, `MANIFEST.json`, `package-manifest.json` and signature material, plus `notices/` and dependency license files. Some bundled general guides describe older/standard builds; use this release page and the current installation guide to choose this flavour. The current Rocky 8.10 packages match the recorded rebuild checksums; earlier publication records remain historical evidence.

This compatibility group was first published here on 2026-11-18. The current four packages were rebuilt on Rocky Linux 8.10 and synchronized on 2026-11-20; see the [current revision](../../releases/legacy-rocky8-20261120.json). Earlier release and acceptance records remain historical evidence. The original release tag targets and complete [v0.0.3 foundation](../../history/README.md) remain preserved.

[EULA](../../EULA.md#english) · [License scope](../../LICENSE.md) · [Third-party coverage](../../third-party/README.md) · [Test entitlement scope](../../licenses/README.md). A valid version/module-scoped KetupaMK entitlement and separately licensed, compatible EDA tools are required. Existing public LIC downloads do not themselves prove compatibility or grant additional rights.

</details>

<details name="readme-language" open>
<summary><strong>简体中文</strong></summary>

**预发布 · Linux x86_64 / amd64 · 应用与运行环境安装包**

标签：[`openketupamk-kernel-legacy-v1.0.2`](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/tree/openketupamk-kernel-legacy-v1.0.2) · [GitHub Release](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/tag/openketupamk-kernel-legacy-v1.0.2) · [全部标签](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/tags)

这是面向较旧 Linux 用户空间的 1.0.2 兼容发行组，包括 Rocky/RHEL 8 和 Ubuntu 20.04。它保留 1.0.2 应用范围，降低二进制 ABI 依赖基线，安装 KetupaMK 及其私有运行环境；不会安装或替换 Linux 操作系统、内核或宿主 glibc。文件名中的 `kernel-legacy` 表示兼容构建类型，不是回退到历史业务版本。

## 选择一种格式下载


<!-- current-assets:start -->
Rocky Linux 8.10 重编译版 · 2026-11-20。保留原文件名与标签指向，见[本次修订记录](../../releases/legacy-rocky8-20261120.json)及[此前联系方式修订](../../releases/contact-refresh-20261119.json)。

| 安装包 | 字节数 |
| --- | --- |
| [ketupa-ai-fabric-kernel-legacy_1.0.2_amd64.deb](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-kernel-legacy-v1.0.2/ketupa-ai-fabric-kernel-legacy_1.0.2_amd64.deb) | 176,315,356 |
| [ketupa-ai-fabric-kernel-legacy-1.0.2-x64.tar.gz](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-kernel-legacy-v1.0.2/ketupa-ai-fabric-kernel-legacy-1.0.2-x64.tar.gz) | 175,341,549 |
| [ketupa-ai-fabric-kernel-legacy-1.0.2-1.x86_64.rpm](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-kernel-legacy-v1.0.2/ketupa-ai-fabric-kernel-legacy-1.0.2-1.x86_64.rpm) | 176,280,667 |
| [ketupa-ai-fabric-kernel-legacy-1.0.2-x64.run](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-kernel-legacy-v1.0.2/ketupa-ai-fabric-kernel-legacy-1.0.2-x64.run) | 175,342,502 |
<!-- current-assets:end -->

四个文件以不同格式交付同一套签名应用与运行环境，任选一种。

| 系统或需求 | 推荐格式 |
| --- | --- |
| Rocky/RHEL/AlmaLinux 8+ | RPM |
| Ubuntu 20.04 / Debian 系，glibc 2.28+ | DEB；需在目标机验证 |
| 独立安装目录 | RUN，先执行 --check |
| 手动或离线解压 | TAR.GZ |

它们与[标准 Windows/Linux 1.0.2](openketupamk-v1.0.2.md)、历史 Runtime 1.0.0 分开发行。

## 系统基线

| 项目 | 已记录要求或依据 |
| --- | --- |
| CPU 与用户空间 | Linux x86_64（amd64），glibc 2.28 或以上；不适用于 ARM64、32 位或 musl/Alpine |
| 构建用户空间 | Rocky Linux 8.10、GCC 8.5、glibc 2.28 |
| 已记录最高所需 GLIBC 符号 | GLIBC 2.28；此构建的其他符号版本需另行审计 |
| Rocky / RHEL 系列 | 目标为 Rocky Linux 8+ / RHEL 兼容系统，优先使用原生 RPM 格式 |
| Debian / Ubuntu 系列 | 提供 glibc 2.28+ 适用的 DEB 格式；此重编译包在全新目标机上的安装尚未验证 |
| 宿主依赖 | 按平台准备 glibc、libstdc++、libgcc、libgomp、libxcrypt、zlib 等，具体以包管理器声明为准 |
| Python/运行环境 | 随包提供私有 Python 运行环境；目标机仍需满足系统依赖 |
| 内核范围 | 未独立确定最低 Linux 内核版本；隔离用户空间测试共用宿主内核 |

实际检查的 DEB 依赖为 `libc6 (>= 2.28), libstdc++6, libcrypt1, zlib1g, libgomp1`。随包提供运行环境不等于免除系统基础库要求。RPM/DEB 解析依赖时仍可能需要配置软件源或准备离线系统依赖包。

## 安装与替换

准确命令见[四种格式安装说明](../installation/README.md#legacy-linux-zh)。替换前先停止使用该目录的任务及受影响的许可服务，工作区与授权状态独立于应用安装目录保存，并保留其记录。

兼容 DEB 的包名仍为 `ketupa-ai-fabric`，版本为 `1.0.2`，默认使用 `/opt/ketupa-ai-fabric`。包管理器可能在相同版本号下替换标准构建，不能把它当成第二套独立包。不要在同一前缀混装不同格式或标准/兼容载荷。TAR/RUN 如需独立安装，应分别指定目录和命令名，并明确服务与授权归属。`--replace` 用于有意替换，不应默认使用。

## 已有验收及边界

2026-11-20 的 Rocky Linux 8.10 构建记录包括：528 个原生模块编译成功、最高所需 GLIBC 符号版本 2.28、9,354 个签名载荷文件校验、RUN --check、RPM/DEB 结构检查，以及保留有效许可服务的 RUN 覆盖安装。此四包的 AEDT 2026R1 完整建模、AEDT 2025R2 无临时开关验收、Mode 1 求解、全新系统 RPM/DEB 安装和物理签核仍未验证。此前 2026-11-17 的验收属于旧构建。参见[当前脱敏验收摘要](../../releases/legacy-rocky8-20261120-acceptance.json)和[历史验收摘要](../../releases/kernel-legacy-v1.0.2-acceptance.json)。

## SHA-256

将 [SHA256SUMS](https://raw.githubusercontent.com/Shallot-2009/KetupaMK-AI-Fabric/main/SHA256SUMS) 与所选安装包下载到同一目录，运行 `sha256sum --ignore-missing -c SHA256SUMS`。

```text
e0ecf61d1544d5aacaaf8ea14e34eb54914b55bed9cf5be84867e17d0da98bdc  ketupa-ai-fabric-kernel-legacy_1.0.2_amd64.deb
de0c8d083e6a3568b07bca81ba4ceafa3bd58d943949a740968c6c134cb96511  ketupa-ai-fabric-kernel-legacy-1.0.2-x64.tar.gz
4c69b3dcb13fe9c7162d321adc50bcb30731e71cc78b6027e4e687bc6d8d91af  ketupa-ai-fabric-kernel-legacy-1.0.2-1.x86_64.rpm
c4c8d178cda9fb3156b2c122312e753c9f2215fc4a8211d0d7aeec53a7486adc  ketupa-ai-fabric-kernel-legacy-1.0.2-x64.run
```

## 条款、包内文档与来源

TAR 载荷包含 `docs/Linux_Kernel_Legacy.md`、其他产品指南、`dependency-inventory.json`、`MANIFEST.json`、`package-manifest.json` 及签名材料，以及 `notices/` 和依赖许可文件。部分通用包内指南描述旧版或标准构建；本兼容版的选包与安装以本页和当前安装指南为入口。当前 Rocky 8.10 重编译包与已记录的校验值一致；此前发布记录作为历史依据保留。

本兼容发行组于 2026-11-18 首次纳入本仓库。当前四包在 Rocky Linux 8.10 上重编译，于 2026-11-20 同步，见[本次修订记录](../../releases/legacy-rocky8-20261120.json)。此前发布及验收记录作为历史依据保留；原发行标签指向与完整的 [v0.0.3 基础项目](../../history/README.md)继续保留。

[EULA](../../EULA.md#中文) · [许可范围](../../LICENSE.md) · [第三方覆盖范围](../../third-party/README.md) · [测试授权范围](../../licenses/README.md)。实际运行需要适用版本/模块的有效 KetupaMK 授权，以及另行获准使用且兼容的 EDA 工具；现有公开 LIC 下载本身不证明适用，也不会扩大权利。

</details>
