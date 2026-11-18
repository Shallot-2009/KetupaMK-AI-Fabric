# 安装与运行环境

[English](INSTALLATION.en.md) · [下载入口](../README.zh-CN.md#下载安装包)

## 选择发行版本

按需求选择 5 个发行组之一。普通 1.0.0 与 Runtime 1.0.0 是不同发行组，不能仅按文件名互相替代。1.0.2、1.0.1 和 Beta 保留原有预发布状态。每个发行组提供一个 Windows x64 EXE，以及 Linux 的两种可选安装格式。[发行清单](../releases/manifest.json)记录准确文件名、字节数、校验值和地址。

下载对应平台的文件后，与 [SHA256SUMS](../SHA256SUMS) 比对。Linux 可将校验清单下载到安装包所在目录，然后运行：

```bash
sha256sum --ignore-missing -c SHA256SUMS
```

Windows PowerShell 中计算所选安装包的哈希，再与清单的对应行核对：

```powershell
Get-FileHash -Algorithm SHA256 .\your-selected-installer.exe
```

将示例文件名替换为实际下载文件名。哈希比对验证文件与迁移版本一致，不等同于全部依赖可信、实际运行成功或工程验收。

## Windows x64

运行所选 EXE 并按安装器说明操作。1.0.2 发行说明提供 Windows Launcher；请按该版本要求配置外部工程工具及适用的 KetupaMK 许可证。GitHub 仓库更名不会重命名或重新构建已安装产品。

## Linux x64 / amd64

以下二选一：

- DEB：在兼容的 Debian/Ubuntu 系统中，使用实际本地文件名执行 `sudo apt install ./your-selected-package.deb`，并核对将安装的依赖变化。
- TAR.GZ：使用实际文件名执行 `tar -xzf your-selected-package.tar.gz`，阅读包内安装说明，再使用该版本文档记载的启动方式；不同版本不推定具有相同内部目录。

1.0.2 的 Linux 发行形式为 CLI，不包含 Windows Launcher。正确安装并配置 1.0.2 后，可使用 `ketupa --version`、`ketupa license status` 和 `ketupa license-service status` 进行只读检查；CIR 功能范围见 [1.0.2 发行说明](releases/openketupamk-v1.0.2.md)。

## 运行环境、厂商工具与输入

既有安装包、Runtime 发行组及已发布的第三方源码/许可资料，均统一在本仓库及其 Releases。未额外公开私有第一方开发环境或核心源码。打包运行环境不表示附带外部商业 EDA 授权，也不保证与未指定的厂商版本兼容。

请为所选工作流准备兼容的 Ansys/Cadence 等工具、相应厂商许可、经批准的工程输入文件和适用版本的 KetupaMK 许可证。现有[内测许可证](../licenses/internal-test/README.md)仅原样保留，不续期；有效期与模块范围依原签名文件。

v0.0.3 源码具有独立的历史依赖记录，见[归档指南](../history/README.md)；不要把它的旧 requirements 文件直接应用于现行专有产品。

本次迁移核验历史文件保留、许可文本保留、Release 附件大小与 SHA-256 及仓库链接，不执行安装器、激活授权、运行 EDA 建模/求解或进行工程签核。
