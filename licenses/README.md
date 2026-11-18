# KetupaMK 测试许可证 / Test licenses

[中文主页](../README.zh-CN.md) · [English home](../README.md)

两个 LIC 文件直接保存在本目录，说明与校验清单统一维护。

Both LIC files are stored directly in this directory, with shared instructions and a checksum list.

| 类型 / Type | 文件 / File | 直接下载 / Direct download |
| --- | --- | --- |
| [离线测试 / Offline test](#offline-test) | [Ketupa-ketupamk_offline_test_12w-20261116-232329-233.lic](Ketupa-ketupamk_offline_test_12w-20261116-232329-233.lic) | [下载 LIC / Download LIC](https://raw.githubusercontent.com/Shallot-2009/KetupaMK-AI-Fabric/main/licenses/Ketupa-ketupamk_offline_test_12w-20261116-232329-233.lic) |
| [既有内测 / Existing internal test](#internal-test) | [openketupamk-internal-test-12w.lic](openketupamk-internal-test-12w.lic) | [下载 LIC / Download LIC](https://raw.githubusercontent.com/Shallot-2009/KetupaMK-AI-Fabric/main/licenses/openketupamk-internal-test-12w.lic) |

<a id="offline-test"></a>

## 离线测试 / Offline test

- 文件名 / Filename: `Ketupa-ketupamk_offline_test_12w-20261116-232329-233.lic`
- 大小 / Size: **4,781 bytes**
- 同步日期 / Synchronized on: **2026-11-18**
- SHA-256: `2d1c5e8ae2e09ada57ffe6aa434d8016f4c9393c3eb08fb447c022778eb60031`

中文：维护者指定的离线测试 LIC，按本地 `package` 目录中的原文件逐字节同步。下载后使用对应 KetupaMK 版本的许可证导入或配置流程。

English: This maintainer-designated offline test LIC is copied byte for byte from the original file in the local `package` directory. Import or configure it using the license workflow for the applicable KetupaMK version.

<a id="internal-test"></a>

## 既有内测 / Existing internal test

- 文件名 / Filename: `openketupamk-internal-test-12w.lic`
- 大小 / Size: **4,836 bytes**
- SHA-256: `37ee8efa33d74c5197092a2678bda1daa0e6f074c3a04cc378873396c266db01`

中文：原发行仓库已公开的内测许可证，文件内容原样保留。原始说明作为[来源记录](../docs/provenance/internal-test-README.before-flattening.md)逐字节保留，当前下载入口见上表。

English: The internal-test license previously published in the distribution repository retains its original bytes. Its original instructions are preserved byte for byte as a [provenance record](../docs/provenance/internal-test-README.before-flattening.md); use the table above for current downloads.

## 使用范围 / Scope

中文：这些是维护者指定公开的测试授权文件。离线文件由维护者提供的 `package` 目录原样同步；各文件的实际模块范围、适用版本、有效期及设备约束以原授权文件和对应软件验证为准。同步不会签发、续期或修改许可，也不授予第三方 EDA 工具的授权。

English: These test-license files are published at the maintainer's direction. The offline file is copied unchanged from the supplied `package` directory. Module scope, supported versions, validity, and device constraints are governed by each original file and the corresponding software's validation. Synchronization does not issue, renew, or modify a license, or grant third-party EDA entitlements.

中文：文件名中的 `12w` 为原始命名，下载、同步或目录整理不会重新计算有效期。哈希用于核对文件一致性，不代表已验证签名、激活、离线运行或所有模块可用。

English: The `12w` identifier is retained from the original filenames. Downloading, synchronization, or directory reorganization does not restart validity. Digests verify file consistency; they do not establish signature validation, activation, offline execution, or availability of every module.

## SHA-256

[统一校验清单 / Shared checksum list](SHA256SUMS)

在同时下载两个 LIC 与 `SHA256SUMS` 的目录内执行 / In the directory containing both downloaded LIC files and `SHA256SUMS`, run:

```bash
sha256sum -c SHA256SUMS
```

作者 / Author: **Asenjo HB**

邮箱 / Email: [asenjoaupa@gmail.com](mailto:asenjoaupa@gmail.com) · [3405802009@qq.com](mailto:3405802009@qq.com)
