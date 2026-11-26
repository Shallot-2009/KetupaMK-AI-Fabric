# 安装与核验 / Installation and verification

[Home / 项目主页](../../README.md) · [Documentation / 文档](../README.md)

点击语言标题即可在本页切换；另一语言会自动折叠。 / Select a language below; the other section collapses on this page.

<details name="readme-language">
<summary><strong>English</strong></summary>

## Select and download

Use the [download table](../../README.md#downloads-en) to select a version and platform. Click a format link to download the actual installer. Standard Linux TAR.GZ/DEB and compatibility Linux RPM/DEB/RUN/TAR.GZ are alternative formats within their respective distributions. Runtime 1.0.0 is a separate distribution; 1.0.2, 1.0.1, and Beta retain their pre-release status.

Use the checksums from the selected release guide. [Download and verification index](../releases/README.md)

## Verify the download

For 1.0.3, use the checksums on the [1.0.3 download guide](../releases/openketupamk-v1.0.3.md).

On Linux, with the downloaded installer and checksum list in the same directory:

```bash
sha256sum --ignore-missing -c SHA256SUMS
```

In Windows PowerShell:

```powershell
Get-FileHash -Algorithm SHA256 .\your-selected-installer.exe
```

Replace the example with the exact filename and compare the result with its entry in SHA256SUMS. A matching digest establishes file consistency, not code-signing identity or functional acceptance.

## Windows x64

Run the selected EXE and follow its installer. Review the [EULA](../../EULA.md#english) and configure the external tools and entitlement required by that version. Select the existing installation directory when updating the same product.

## Linux x64 / amd64

- DEB: on a compatible Debian/Ubuntu system, use the exact filename with `sudo apt install ./your-selected-package.deb`; review the dependencies before installation.
- TAR.GZ: extract with `tar -xzf your-selected-package.tar.gz`, then follow the instructions included in that package. Internal paths and launchers may differ by version.

The standard 1.0.3 Linux package requires x86_64 and glibc 2.34 or later. For a same-version replacement, use `sudo apt install --reinstall ./your-selected-package.deb` or run the TAR installer with the existing prefix and `--replace`. Stop tasks and the relevant license service before replacement, then restart the service and check the installed version:

```bash
ketupa --version
ketupa license status
ketupa license-service status
```

<a id="legacy-linux-en"></a>

## Legacy Linux 1.0.2: Rocky / RHEL 8 and Ubuntu 20.04

Use the [compatibility release](../releases/openketupamk-kernel-legacy-v1.0.2.md), tag `openketupamk-kernel-legacy-v1.0.2`. All four formats target **Linux x86_64 with glibc 2.28 or later**. They install the application and bundled runtime, not a Linux kernel. Choose one format:

| Format | Recommended selection | Installation after SHA-256 verification |
| --- | --- | --- |
| RPM | Rocky / RHEL-compatible 8+ | `sudo dnf install ./ketupa-ai-fabric-kernel-legacy-1.0.2-1.x86_64.rpm` |
| DEB | Ubuntu 20.04 / compatible Debian | `sudo apt install ./ketupa-ai-fabric-kernel-legacy_1.0.2_amd64.deb` |
| RUN | Self-extracting installer, bundled TAR payload | Commands below |
| TAR.GZ | Inspect/extract before installation; explicit prefix | Commands below |

For RUN, first check the embedded archive, then install into a dedicated prefix:

```bash
sh ketupa-ai-fabric-kernel-legacy-1.0.2-x64.run --check
sudo sh ketupa-ai-fabric-kernel-legacy-1.0.2-x64.run --prefix /opt/ketupa-ai-fabric-kernel-legacy-1.0.2 --command ketupa-legacy
```

For TAR.GZ:

```bash
tar -xzf ketupa-ai-fabric-kernel-legacy-1.0.2-x64.tar.gz
cd ketupa-ai-fabric-kernel-legacy-1.0.2-x64
sudo ./ketupa-setup --prefix /opt/ketupa-ai-fabric-kernel-legacy-1.0.2 --command ketupa-legacy
```

The RPM/DEB default application prefix is `/opt/ketupa-ai-fabric`. The compatibility DEB still identifies as `ketupa-ai-fabric` version `1.0.2`; a same-version installation can replace the standard build. Review package-manager actions before continuing. Use the package manager for packages it owns; never unpack TAR/RUN over an RPM/DEB-owned directory. TAR/RUN support `--replace` for an intentional replacement after stopping affected jobs/services. A separate prefix and command name avoid file collisions but do not create independent entitlement or service state automatically.

Host system libraries remain prerequisites. The DEB declares `libc6 (>= 2.28), libstdc++6, libcrypt1, zlib1g, libgomp1`; RPM resolves its own declared dependencies. Fully offline hosts must have those dependencies available locally. Do not replace the host glibc to install this application.

After a dedicated-prefix installation, check the exact installed executable before configuring a compatible entitlement or external EDA tools:

```bash
/opt/ketupa-ai-fabric-kernel-legacy-1.0.2/ketupa --version
/opt/ketupa-ai-fabric-kernel-legacy-1.0.2/ketupa license status
/opt/ketupa-ai-fabric-kernel-legacy-1.0.2/ketupa license-service status
```

For RPM/DEB, substitute `/opt/ketupa-ai-fabric/ketupa`. Preserve workspaces, service configuration, entitlement files and consumption/time records when upgrading or removing an installation; do not reset or roll them back. Use the installed format's maintenance instructions for removal.

The supplied acceptance records cover isolated EL8.1 TAR/RUN/RPM and Ubuntu 20.04 DEB operations. They share the host kernel and do not establish a minimum kernel version, native Rocky hardware support or successful EDA solving. See the [release evidence and limitations](../releases/openketupamk-kernel-legacy-v1.0.2.md).

## Entitlements and engineering environment

The [public test LIC files](../../licenses/README.md) are supplied unchanged. Use the entitlement-import or configuration workflow documented by your installed version. Their actual signed restrictions govern use; copying a file does not activate or renew it.

Prepare the compatible Ansys/Cadence or other tools, vendor licenses, layouts, stackups/XML, connector models, and project data required by the selected workflow. [Product scope](../product/README.md) describes the published boundaries. External commercial tools are not licensed by a KetupaMK download.

GitHub Source code ZIP/TAR files and a Git clone are repository snapshots. The foundational [v0.0.3 project](../../history/README.md) has its own historical dependencies, which should not be applied to the current proprietary product.

## Report a problem

Include the product version, operating system, package filename, checksum result, minimal steps, and sanitized error text in an issue. Send private entitlements, sensitive logs, or security findings through the [private reporting channel](../../SECURITY.md).

</details>

<details name="readme-language" open>
<summary><strong>简体中文</strong></summary>

## 选择并下载

在[下载表](../../README.zh-CN.md#downloads-zh)中选择版本和平台，点击格式链接直接下载安装包。标准 Linux 的 TAR.GZ/DEB 与兼容 Linux 的 RPM/DEB/RUN/TAR.GZ 分别在各自发行组内任选一种。Runtime 1.0.0 为独立发行组；1.0.2、1.0.1 与 Beta 保留预发布状态。

使用所选发行说明提供的校验值。[下载与校验索引](../releases/README.md)

## 校验下载

1.0.3 安装包的校验值见 [1.0.3 下载说明](../releases/openketupamk-v1.0.3.md)。

Linux 下，在安装包与校验清单所在目录执行：

```bash
sha256sum --ignore-missing -c SHA256SUMS
```

Windows PowerShell：

```powershell
Get-FileHash -Algorithm SHA256 .\your-selected-installer.exe
```

把示例替换为真实文件名，与 SHA256SUMS 中对应行比较。哈希一致说明文件一致，不等于验证代码签名身份或功能验收。

## Windows x64

运行所选 EXE 并遵循安装器说明。阅读 [EULA](../../EULA.md#中文)，配置该版本要求的外部工具与授权。更新同一产品时选择原安装目录。

## Linux x64 / amd64

- DEB：在兼容的 Debian/Ubuntu 系统中，使用实际文件名执行 `sudo apt install ./your-selected-package.deb`，安装前检查依赖变化。
- TAR.GZ：使用 `tar -xzf your-selected-package.tar.gz` 解压，按包内说明操作；不同版本的内部路径和启动方式可能不同。

标准 Linux 1.0.3 要求 x86_64 和 glibc 2.34 或以上。同版本覆盖时，DEB 使用 `sudo apt install --reinstall ./your-selected-package.deb`，TAR 使用原安装目录并指定 `--replace`。替换前结束正在运行的任务并停止相关授权服务，完成后重新启动服务并检查安装版本：

```bash
ketupa --version
ketupa license status
ketupa license-service status
```

<a id="legacy-linux-zh"></a>

## 旧版 Linux 兼容环境 1.0.2：Rocky / RHEL 8 与 Ubuntu 20.04

选择[兼容发行组](../releases/openketupamk-kernel-legacy-v1.0.2.md)，标签为 `openketupamk-kernel-legacy-v1.0.2`。四种格式均面向 **Linux x86_64、glibc 2.28 或以上**，安装应用与随包运行环境，不安装 Linux 内核。任选一种：

| 格式 | 建议使用场景 | 核对 SHA-256 后安装 |
| --- | --- | --- |
| RPM | Rocky / RHEL 兼容 8+ | `sudo dnf install ./ketupa-ai-fabric-kernel-legacy-1.0.2-1.x86_64.rpm` |
| DEB | Ubuntu 20.04 / 兼容 Debian | `sudo apt install ./ketupa-ai-fabric-kernel-legacy_1.0.2_amd64.deb` |
| RUN | 自解压安装，内嵌 TAR 载荷 | 见下方命令 |
| TAR.GZ | 先查看、解压再安装，明确指定前缀 | 见下方命令 |

RUN 先检查内嵌归档，再安装到独立目录：

```bash
sh ketupa-ai-fabric-kernel-legacy-1.0.2-x64.run --check
sudo sh ketupa-ai-fabric-kernel-legacy-1.0.2-x64.run --prefix /opt/ketupa-ai-fabric-kernel-legacy-1.0.2 --command ketupa-legacy
```

TAR.GZ：

```bash
tar -xzf ketupa-ai-fabric-kernel-legacy-1.0.2-x64.tar.gz
cd ketupa-ai-fabric-kernel-legacy-1.0.2-x64
sudo ./ketupa-setup --prefix /opt/ketupa-ai-fabric-kernel-legacy-1.0.2 --command ketupa-legacy
```

RPM/DEB 默认应用目录为 `/opt/ketupa-ai-fabric`。兼容 DEB 的包名仍是 `ketupa-ai-fabric`、版本仍是 `1.0.2`，同版本安装可能替换标准构建，继续前先检查包管理器计划。包管理器负责的目录应继续由其维护，不要将 TAR/RUN 解压覆盖到 RPM/DEB 安装目录。TAR/RUN 的 `--replace` 用于停止相关任务/服务后的有意替换。独立目录和命令名可以避免文件冲突，但不会自动隔离授权和服务状态。

宿主仍须具备基础系统库。DEB 声明 `libc6 (>= 2.28), libstdc++6, libcrypt1, zlib1g, libgomp1`，RPM 依其自身声明解析。全离线主机应事先在本地准备这些依赖，不要为安装应用替换宿主 glibc。

独立目录安装后，先检查准确的已安装入口，再配置适用授权及外部 EDA 工具：

```bash
/opt/ketupa-ai-fabric-kernel-legacy-1.0.2/ketupa --version
/opt/ketupa-ai-fabric-kernel-legacy-1.0.2/ketupa license status
/opt/ketupa-ai-fabric-kernel-legacy-1.0.2/ketupa license-service status
```

RPM/DEB 安装则替换为 `/opt/ketupa-ai-fabric/ketupa`。升级或卸载时保留工作区、服务配置、授权文件及消耗/时间记录，不重置或回滚。卸载应使用所选格式自身的维护说明。

提供的验收记录覆盖隔离 EL8.1 TAR/RUN/RPM 与 Ubuntu 20.04 DEB 操作，共用宿主内核，不能据此确定最低内核版本、Rocky 真机硬件支持或 EDA 求解成功。详见[发行验收依据与限制](../releases/openketupamk-kernel-legacy-v1.0.2.md)。

## 授权与工程环境

[公开测试 LIC](../../licenses/README.md) 保持原始内容。请使用所安装版本记载的许可证导入或配置流程；实际签名限制决定使用范围，复制文件不等于激活或续期。

按工作流准备兼容的 Ansys/Cadence 等工具、厂商许可、版图、层叠/XML、连接器模型和工程数据。已发布范围见[产品说明](../product/README.md)。下载 KetupaMK 不会取得外部商业工具的授权。

GitHub Source code ZIP/TAR 和 Git clone 取得的是仓库快照。[v0.0.3 基础项目](../../history/README.md)有独立的历史依赖记录，不应直接应用于现行专有产品。

## 问题反馈

公开 Issue 请提供产品版本、操作系统、安装包文件名、哈希结果、最小复现步骤和脱敏错误信息。私有授权、敏感日志及安全问题使用[私密报告渠道](../../SECURITY.md)。

</details>
