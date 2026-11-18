# 安装与核验 / Installation and verification

[Home / 项目主页](../../README.md) · [Documentation / 文档](../README.md)

点击语言标题即可在本页切换；另一语言会自动折叠。 / Select a language below; the other section collapses on this page.

<details name="readme-language">
<summary><strong>English</strong></summary>

## Select and download

Use the [download table](../../README.md#downloads-en) to select a version and platform. Click EXE, TAR.GZ, or DEB to download the actual installer. Linux TAR.GZ and DEB are alternatives. Runtime 1.0.0 is a separate distribution; 1.0.2, 1.0.1, and Beta retain their pre-release status.

Download [SHA256SUMS](https://raw.githubusercontent.com/Shallot-2009/KetupaMK-AI-Fabric/main/SHA256SUMS) into the installer directory. Exact names, sizes, and digests are recorded in the [release manifest](../../releases/manifest.json).

## Verify the download

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

Run the selected EXE and follow its installer. Review the [EULA](../../EULA.md#english) and configure the external tools and entitlement required by that version. Version 1.0.2 provides a Windows Launcher. A repository rename does not rename installed products or rebuild historical installers.

## Linux x64 / amd64

- DEB: on a compatible Debian/Ubuntu system, use the exact filename with `sudo apt install ./your-selected-package.deb`; review the dependencies before installation.
- TAR.GZ: extract with `tar -xzf your-selected-package.tar.gz`, then follow the instructions included in that package. Internal paths and launchers may differ by version.

Version 1.0.2 is a CLI distribution on Linux. On an installed and configured system, the documented read-only checks are:

```bash
ketupa --version
ketupa license status
ketupa license-service status
```

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

在[下载表](../../README.zh-CN.md#downloads-zh)中选择版本和平台，点击 EXE、TAR.GZ 或 DEB 直接下载安装包。Linux 的 TAR.GZ 与 DEB 二选一。Runtime 1.0.0 为独立发行组；1.0.2、1.0.1 与 Beta 保留预发布状态。

将 [SHA256SUMS](https://raw.githubusercontent.com/Shallot-2009/KetupaMK-AI-Fabric/main/SHA256SUMS) 下载到安装包所在目录。准确文件名、大小和哈希见[发行清单](../../releases/manifest.json)。

## 校验下载

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

运行所选 EXE 并遵循安装器说明。阅读 [EULA](../../EULA.md#中文)，配置该版本要求的外部工具与授权。1.0.2 提供 Windows Launcher。仓库更名不会重命名已安装产品，也不会重新构建历史安装包。

## Linux x64 / amd64

- DEB：在兼容的 Debian/Ubuntu 系统中，使用实际文件名执行 `sudo apt install ./your-selected-package.deb`，安装前检查依赖变化。
- TAR.GZ：使用 `tar -xzf your-selected-package.tar.gz` 解压，按包内说明操作；不同版本的内部路径和启动方式可能不同。

1.0.2 在 Linux 上提供 CLI。系统完成安装与配置后，可使用该版本记载的只读检查命令：

```bash
ketupa --version
ketupa license status
ketupa license-service status
```

## 授权与工程环境

[公开测试 LIC](../../licenses/README.md) 保持原始内容。请使用所安装版本记载的许可证导入或配置流程；实际签名限制决定使用范围，复制文件不等于激活或续期。

按工作流准备兼容的 Ansys/Cadence 等工具、厂商许可、版图、层叠/XML、连接器模型和工程数据。已发布范围见[产品说明](../product/README.md)。下载 KetupaMK 不会取得外部商业工具的授权。

GitHub Source code ZIP/TAR 和 Git clone 取得的是仓库快照。[v0.0.3 基础项目](../../history/README.md)有独立的历史依赖记录，不应直接应用于现行专有产品。

## 问题反馈

公开 Issue 请提供产品版本、操作系统、安装包文件名、哈希结果、最小复现步骤和脱敏错误信息。私有授权、敏感日志及安全问题使用[私密报告渠道](../../SECURITY.md)。

</details>
