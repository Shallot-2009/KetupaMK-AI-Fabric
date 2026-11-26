# 项目结构导航 / Project map

[Home / 主页](../README.md) · [Documentation / 文档](README.md)

<details name="readme-language">
<summary><strong>English</strong></summary>

This repository is the public product/distribution index. Current protected implementation and customer projects are not stored here.

| Location | Responsibility | Start here |
| --- | --- | --- |
| Root README files | English/Chinese product entry points | [English](../README.md), [Chinese](../README.zh-CN.md) |
| `docs/product/` | Engineering domains and version-specific capability boundaries | [Domains](product/DOMAINS.md), [capabilities](product/README.md) |
| `docs/installation/` | Platform selection, installation and verification | [Installation](installation/README.md) |
| `docs/releases/` | Version notes, exact downloads and checksums | [Releases](releases/README.md) |
| `releases/` | Installer inventories and download checksums | [Metadata guide](../releases/README.md) |
| `licenses/` | Maintainer-published test entitlements and usage instructions | [Test LIC guide](../licenses/README.md) |
| `history/` | Preserved v0.0.3 foundation and original project records | [Foundation](../history/README.md) |
| `third-party/` | Component notices, licenses and corresponding source archives | [Third-party guide](../third-party/README.md) |
| `tools/` and `.github/` | Repository validation and contribution checks | [Tools](../tools/README.md), [governance](governance/README.md) |

Use the product in this order:

1. Choose Windows, standard Linux or Legacy Linux in the [release index](releases/README.md).
2. Download one suitable installer and verify its current SHA-256.
3. Follow the [installation guide](installation/README.md) and validate your version-scoped entitlement.
4. Prepare the actual layout/stackup/network or Touchstone/specification inputs for the selected workflow.
5. Keep global selection in CIR, project details in includes, and execute through `ketupa run -sh main.cir`.
6. Review results and retain source versions, mappings, specifications and reports together.

Do not move customer projects, private entitlements, activation records, signing material or build caches into this public repository. Published tags and original foundation files remain unchanged when the current documentation index is updated.

</details>

<details name="readme-language" open>
<summary><strong>简体中文</strong></summary>

本仓库负责公开产品与发行导航，不存放现行受保护实现和客户工程。

| 位置 | 职责 | 阅读入口 |
| --- | --- | --- |
| 根目录 README | 中英文产品主页 | [英文](../README.md)、[中文](../README.zh-CN.md) |
| `docs/product/` | 技术方向、各版本能力与范围 | [技术方向](product/DOMAINS.md)、[产品功能](product/README.md) |
| `docs/installation/` | 平台选择、安装和检查 | [安装说明](installation/README.md) |
| `docs/releases/` | 版本说明、准确下载链接和校验值 | [发行索引](releases/README.md) |
| `releases/` | 安装包清单与下载校验值 | [元数据说明](../releases/README.md) |
| `licenses/` | 维护者公开的测试授权及使用说明 | [测试 LIC 说明](../licenses/README.md) |
| `history/` | 保全的 v0.0.3 基础项目与历史依据 | [基础项目](../history/README.md) |
| `third-party/` | 第三方声明、许可与对应源码 | [第三方说明](../third-party/README.md) |
| `tools/`、`.github/` | 仓库检查与协作规范 | [检查工具](../tools/README.md)、[维护规范](governance/README.md) |

按以下顺序使用产品：

1. 在[发行索引](releases/README.md)选择 Windows、标准 Linux 或 Legacy Linux。
2. 下载适合本机的一种安装包，核对当前 SHA-256。
3. 按[安装说明](installation/README.md)完成安装并确认适用版本授权。
4. 为选定工作流准备真实版图、层叠、网络，或 Touchstone、规范文件。
5. CIR 写全局选择，include 写具体项目，通过 `ketupa run -sh main.cir` 执行。
6. 审核结果，将输入版本、映射、规范与报告一同归档。

客户工程、私有授权、激活记录、签名材料和构建缓存不得放入公开仓库。当前文档索引更新不移动既有标签，也不改写基础项目原件。

</details>
