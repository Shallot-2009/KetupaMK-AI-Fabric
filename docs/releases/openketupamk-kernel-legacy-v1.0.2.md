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
Contact-corrected downloads · 2026-11-19. Original names and tag targets retained; see the [revision record](../../releases/contact-refresh-20261119.json).

| Installer | Bytes |
| --- | --- |
| [ketupa-ai-fabric-kernel-legacy_1.0.2_amd64.deb](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-kernel-legacy-v1.0.2/ketupa-ai-fabric-kernel-legacy_1.0.2_amd64.deb) | 175,131,882 |
| [ketupa-ai-fabric-kernel-legacy-1.0.2-x64.tar.gz](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-kernel-legacy-v1.0.2/ketupa-ai-fabric-kernel-legacy-1.0.2-x64.tar.gz) | 175,318,216 |
| [ketupa-ai-fabric-kernel-legacy-1.0.2-1.x86_64.rpm](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-kernel-legacy-v1.0.2/ketupa-ai-fabric-kernel-legacy-1.0.2-1.x86_64.rpm) | 176,508,163 |
| [ketupa-ai-fabric-kernel-legacy-1.0.2-x64.run](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-kernel-legacy-v1.0.2/ketupa-ai-fabric-kernel-legacy-1.0.2-x64.run) | 175,319,169 |
<!-- current-assets:end -->

All four files deliver the same signed application/runtime environment in alternative formats. Choose one. They are separate from the [standard Windows/Linux 1.0.2 distribution](openketupamk-v1.0.2.md) and the historical Runtime 1.0.0 distribution.

## System baseline

| Item | Recorded requirement or evidence |
| --- | --- |
| CPU / userspace | Linux x86_64 (amd64), glibc 2.28 or later; not ARM64, 32-bit, or musl/Alpine |
| Build userspace | CentOS Linux 8.1.1911; an EL8-compatible ABI baseline |
| Maximum required symbol versions | GLIBC 2.28 · GLIBCXX 3.4.25 · CXXABI 1.3.11 |
| Rocky / RHEL family | Rocky Linux 8+ / RHEL-compatible systems are the intended targets; RPM is the native package format |
| Debian / Ubuntu family | Ubuntu 20.04 DEB install/reinstall/removal is recorded in the supplied acceptance results; other versions require their own checks |
| Host dependencies | glibc, libstdc++, libgcc, libgomp, libxcrypt and zlib as appropriate; the package manager resolves its declared dependencies |
| OpenSSL / Python | No fixed system OpenSSL 1.1/3 SONAME dependency in the compatibility report; private Python runtime is bundled |
| Kernel support | No independently established minimum kernel version; userspace tests share the host kernel |

The inspected DEB declares `libc6 (>= 2.28), libstdc++6, libcrypt1, zlib1g, libgomp1`. Runtime bundling does not make system prerequisites optional. RPM/DEB dependency resolution may require configured repositories or locally supplied packages even though the application runtime is bundled.

## Installation and replacement

See the [four-format installation guide](../installation/README.md#legacy-linux-en) for exact commands. Stop active jobs and the affected license service before replacing an installation. Keep project workspaces and entitlement state outside the application prefix and preserve their records.

The compatibility DEB uses package name `ketupa-ai-fabric`, version `1.0.2`, and the usual `/opt/ketupa-ai-fabric` prefix. A package manager can therefore replace a standard build at the same version; it is not a second independent package. Do not mix formats or standard/compatibility payloads in one prefix. For a separate TAR/RUN installation, choose a separate prefix and command name and explicitly configure its service/entitlement ownership. `--replace` is an intentional replacement option, not a default recommendation.

## Recorded acceptance and limits

The supplied acceptance records dated **2026-11-17** report:

- ABI and dynamic-loader checks for **791 ELF files**; maximum symbol versions are listed above.
- **22 passed** EL8.1 TAR/RUN/RPM tests, **6 passed** DEB structure tests, and **8 passed** Ubuntu 20.04 DEB install/reinstall/removal tests.
- Signature verification for **9,351 payload files** in those prior records. Signatures were not independently reverified during this publication task.

These were isolated userspace tests using bubblewrap and the host kernel. Native Rocky hardware/kernel installation, actual vendor EDA integration, licensed modeling/solving and engineering signoff were not established. No claim of support for every older Linux kernel follows from these tests. During publication, the four installer sizes and SHA-256 digests were independently checked against the supplied metadata; installers were not executed. [Sanitized evidence summary](../../releases/kernel-legacy-v1.0.2-acceptance.json).

## SHA-256

Download [SHA256SUMS](https://raw.githubusercontent.com/Shallot-2009/KetupaMK-AI-Fabric/main/SHA256SUMS) beside your selected installer, then run `sha256sum --ignore-missing -c SHA256SUMS`.

```text
ba520b8ca83e55520dee86be51eb058972692c73391e25efe332c1574a9093c3  ketupa-ai-fabric-kernel-legacy_1.0.2_amd64.deb
82598b072f679e1321ccf38f9524e7db30ca39973183ad7a44d3412663e2ccff  ketupa-ai-fabric-kernel-legacy-1.0.2-x64.tar.gz
d19942305b4ece379e1eab7e9d2d452e30c90a61eaaa7d104b539f3b1c0040f0  ketupa-ai-fabric-kernel-legacy-1.0.2-1.x86_64.rpm
4f287fb78e79ba7edc04356c2cfb20e7dcdaf0fa2020cb5782fc4f2881bd58ff  ketupa-ai-fabric-kernel-legacy-1.0.2-x64.run
```

## Terms, included documentation and provenance

The TAR payload contains `docs/Linux_Kernel_Legacy.md`, the other product guides, `dependency-inventory.json`, `MANIFEST.json`, `package-manifest.json` and signature material, plus `notices/` and dependency license files. Some bundled general guides describe older/standard builds; use this release page and the current installation guide to choose this flavour. The current contact-corrected packages are synchronized from audited development releases; earlier publication records remain historical evidence.

This compatibility group was first published here on 2026-11-18. The current contact-corrected four packages were synchronized on 2026-11-19 and total **702,277,430 bytes**; see the [revision record](../../releases/contact-refresh-20261119.json). Earlier acceptance records describe their dated builds and are not a new installation test of these files. The original release tag targets and complete [v0.0.3 foundation](../../history/README.md) remain preserved.

[EULA](../../EULA.md#english) · [License scope](../../LICENSE.md) · [Third-party coverage](../../third-party/README.md) · [Test entitlement scope](../../licenses/README.md). A valid version/module-scoped KetupaMK entitlement and separately licensed, compatible EDA tools are required. Existing public LIC downloads do not themselves prove compatibility or grant additional rights.

</details>

<details name="readme-language" open>
<summary><strong>简体中文</strong></summary>

**预发布 · Linux x86_64 / amd64 · 应用与运行环境安装包**

标签：[`openketupamk-kernel-legacy-v1.0.2`](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/tree/openketupamk-kernel-legacy-v1.0.2) · [GitHub Release](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/tag/openketupamk-kernel-legacy-v1.0.2) · [全部标签](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/tags)

这是面向较旧 Linux 用户空间的 1.0.2 兼容发行组，包括 Rocky/RHEL 8 和 Ubuntu 20.04。它保留 1.0.2 应用范围，降低二进制 ABI 依赖基线，安装 KetupaMK 及其私有运行环境；不会安装或替换 Linux 操作系统、内核或宿主 glibc。文件名中的 `kernel-legacy` 表示兼容构建类型，不是回退到历史业务版本。

## 选择一种格式下载


<!-- current-assets:start -->
联系方式修正版 · 2026-11-19。保留原文件名与标签指向，见[修订记录](../../releases/contact-refresh-20261119.json)。

| 安装包 | 字节数 |
| --- | --- |
| [ketupa-ai-fabric-kernel-legacy_1.0.2_amd64.deb](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-kernel-legacy-v1.0.2/ketupa-ai-fabric-kernel-legacy_1.0.2_amd64.deb) | 175,131,882 |
| [ketupa-ai-fabric-kernel-legacy-1.0.2-x64.tar.gz](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-kernel-legacy-v1.0.2/ketupa-ai-fabric-kernel-legacy-1.0.2-x64.tar.gz) | 175,318,216 |
| [ketupa-ai-fabric-kernel-legacy-1.0.2-1.x86_64.rpm](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-kernel-legacy-v1.0.2/ketupa-ai-fabric-kernel-legacy-1.0.2-1.x86_64.rpm) | 176,508,163 |
| [ketupa-ai-fabric-kernel-legacy-1.0.2-x64.run](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-kernel-legacy-v1.0.2/ketupa-ai-fabric-kernel-legacy-1.0.2-x64.run) | 175,319,169 |
<!-- current-assets:end -->

四个文件以不同格式交付同一套签名应用与运行环境，任选一种。它们与[标准 Windows/Linux 1.0.2](openketupamk-v1.0.2.md)、历史 Runtime 1.0.0 分开发行。

## 系统基线

| 项目 | 已记录要求或依据 |
| --- | --- |
| CPU 与用户空间 | Linux x86_64（amd64），glibc 2.28 或以上；不适用于 ARM64、32 位或 musl/Alpine |
| 构建用户空间 | CentOS Linux 8.1.1911，采用 EL8 兼容 ABI 基线 |
| 最高所需符号版本 | GLIBC 2.28 · GLIBCXX 3.4.25 · CXXABI 1.3.11 |
| Rocky / RHEL 系列 | 目标为 Rocky Linux 8+ / RHEL 兼容系统，优先使用原生 RPM 格式 |
| Debian / Ubuntu 系列 | 提供的验收记录包含 Ubuntu 20.04 DEB 安装、同版本重装和卸载；其他版本需各自核验 |
| 宿主依赖 | 按平台准备 glibc、libstdc++、libgcc、libgomp、libxcrypt、zlib 等，具体以包管理器声明为准 |
| OpenSSL / Python | 兼容报告未要求固定的系统 OpenSSL 1.1/3 SONAME；随包提供私有 Python 运行环境 |
| 内核范围 | 未独立确定最低 Linux 内核版本；隔离用户空间测试共用宿主内核 |

实际检查的 DEB 依赖为 `libc6 (>= 2.28), libstdc++6, libcrypt1, zlib1g, libgomp1`。随包提供运行环境不等于免除系统基础库要求。RPM/DEB 解析依赖时仍可能需要配置软件源或准备离线系统依赖包。

## 安装与替换

准确命令见[四种格式安装说明](../installation/README.md#legacy-linux-zh)。替换前先停止使用该目录的任务及受影响的许可服务，工作区与授权状态独立于应用安装目录保存，并保留其记录。

兼容 DEB 的包名仍为 `ketupa-ai-fabric`，版本为 `1.0.2`，默认使用 `/opt/ketupa-ai-fabric`。包管理器可能在相同版本号下替换标准构建，不能把它当成第二套独立包。不要在同一前缀混装不同格式或标准/兼容载荷。TAR/RUN 如需独立安装，应分别指定目录和命令名，并明确服务与授权归属。`--replace` 用于有意替换，不应默认使用。

## 已有验收及边界

维护者提供的 **2026-11-17** 验收记录记载：

- **791 个 ELF** 的 ABI 与动态加载器检查，最高所需符号版本见上表。
- EL8.1 TAR/RUN/RPM 测试 **22 项通过**，DEB 结构测试 **6 项通过**，Ubuntu 20.04 DEB 安装、同版本重装和卸载测试 **8 项通过**。
- 此前记录包含 **9,351 个载荷文件**的签名验证；本次发布未独立重做密码学签名验证。

以上使用 bubblewrap 隔离用户空间，共用宿主内核，未建立 Rocky 真机内核/硬件安装、实际厂商 EDA 联调、有授权建模/求解或工程签核的通过依据，不能据此承诺支持所有旧 Linux 内核。本次发布独立核对了四个原始安装包的大小与 SHA-256，未执行安装器。详见[脱敏验收摘要](../../releases/kernel-legacy-v1.0.2-acceptance.json)。

## SHA-256

将 [SHA256SUMS](https://raw.githubusercontent.com/Shallot-2009/KetupaMK-AI-Fabric/main/SHA256SUMS) 与所选安装包下载到同一目录，运行 `sha256sum --ignore-missing -c SHA256SUMS`。

```text
ba520b8ca83e55520dee86be51eb058972692c73391e25efe332c1574a9093c3  ketupa-ai-fabric-kernel-legacy_1.0.2_amd64.deb
82598b072f679e1321ccf38f9524e7db30ca39973183ad7a44d3412663e2ccff  ketupa-ai-fabric-kernel-legacy-1.0.2-x64.tar.gz
d19942305b4ece379e1eab7e9d2d452e30c90a61eaaa7d104b539f3b1c0040f0  ketupa-ai-fabric-kernel-legacy-1.0.2-1.x86_64.rpm
4f287fb78e79ba7edc04356c2cfb20e7dcdaf0fa2020cb5782fc4f2881bd58ff  ketupa-ai-fabric-kernel-legacy-1.0.2-x64.run
```

## 条款、包内文档与来源

TAR 载荷包含 `docs/Linux_Kernel_Legacy.md`、其他产品指南、`dependency-inventory.json`、`MANIFEST.json`、`package-manifest.json` 及签名材料，以及 `notices/` 和依赖许可文件。部分通用包内指南描述旧版或标准构建；本兼容版的选包与安装以本页和当前安装指南为入口。当前联系方式修正版从已核对的开发发布目录同步；此前发布记录作为历史依据保留。

本兼容发行组于 2026-11-18 首次纳入本仓库。当前四个联系方式修正版于 2026-11-19 同步，共 **702,277,430 字节**，详见[修订记录](../../releases/contact-refresh-20261119.json)。此前验收对应其注明日期的构建，不代表此次文件已重新执行安装测试。原发行标签指向与完整的 [v0.0.3 基础项目](../../history/README.md)继续保留。

[EULA](../../EULA.md#中文) · [许可范围](../../LICENSE.md) · [第三方覆盖范围](../../third-party/README.md) · [测试授权范围](../../licenses/README.md)。实际运行需要适用版本/模块的有效 KetupaMK 授权，以及另行获准使用且兼容的 EDA 工具；现有公开 LIC 下载本身不证明适用，也不会扩大权利。

</details>
