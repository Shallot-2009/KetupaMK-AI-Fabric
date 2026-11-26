# 仓库检查 / Repository checks

[Home / 项目主页](../README.md) · [Documentation / 文档](../docs/README.md)

点击语言标题即可在本页切换；另一语言会自动折叠。 / Select a language below; the other section collapses on this page.

<details name="readme-language">
<summary><strong>English</strong></summary>

From a full Git checkout with its original history and tags, run:

```bash
python3 tools/check_repository.py
```

The checker uses the Python standard library. It verifies the complete 111-file foundation, 17 preserved distribution records, three public entitlements, installer/tag metadata, third-party hashes, separate product READMEs, same-page guide sections, links/anchors, and known secret patterns. It does not execute archived code, installers, licensing operations, or EDA workflows.

Tag-map commits must be full commit hashes. A tagged publication snapshot may use `self` for its own HEAD; after tagging, the next `main` commit records the concrete hash. The checker still requires the resolved local tag to match and never relaxes the six original tag baselines. The sanitized compatibility acceptance record distinguishes supplied prior tests from publication checks.

GitHub Actions runs the same command. A shallow clone must fetch the original history and tags before validation. Changes to published artifact baselines require explicit review; editing a manifest alone must not redefine the preserved foundation.

</details>

<details name="readme-language" open>
<summary><strong>简体中文</strong></summary>

在包含完整原始历史和标签的 Git 副本根目录执行：

```bash
python3 tools/check_repository.py
```

脚本仅使用 Python 标准库，核对完整的 111 文件基础项目、17 个发行保全记录、三个公开授权、安装包/标签元数据、第三方哈希、产品主页双文件、指南同页语言区域、链接/锚点及已知凭据特征。它不执行归档代码、安装器、授权操作或 EDA 工作流。

标签映射应记录完整提交哈希；已打标签的发布快照可使用 `self` 表示自身 HEAD，后续 `main` 提交改记具体哈希。检查器仍要求本地标签解析一致，不放宽六个原有标签基准。兼容版脱敏验收记录区分提供的既往测试与本次发布核验。

GitHub Actions 执行相同命令。浅克隆需先取得原始历史和标签。已发布文件基准的变更需要明确审核，不应只修改清单就重新定义基础项目的保全依据。

</details>
