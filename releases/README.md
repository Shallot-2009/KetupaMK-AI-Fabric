# 发行元数据 / Release metadata

[Home / 项目主页](../README.md) · [Documentation / 文档](../docs/README.md)

点击语言标题即可在本页切换；另一语言会自动折叠。 / Select a language below; the other section collapses on this page.

<details name="readme-language">
<summary><strong>English</strong></summary>

This directory holds machine-readable records, not installer binaries.

- [manifest.json](manifest.json): six public release groups / twenty-three attachments (nineteen unique packages), exact filenames, byte sizes, SHA-256 values, original publication times, and download URLs.
- [tag-map.json](tag-map.json): seven tags and their exact commit targets.
- [contact-refresh-20261119.json](contact-refresh-20261119.json): reviewed before/after attachment records for the contact correction; tag targets and release status remain fixed.
- [kernel-legacy-v1.0.2-acceptance.json](kernel-legacy-v1.0.2-acceptance.json): sanitized prior userspace-test scope and source-report digests for the new Linux compatibility distribution.
- [Root SHA256SUMS](../SHA256SUMS): installer checksums for command-line verification.

For downloads and notes, use the [release index](../docs/releases/README.md). Product binaries are attached to GitHub Releases. Compatibility environment notes are [here](../docs/releases/openketupamk-kernel-legacy-v1.0.2.md); the [GitHub tags page](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/tags) links to the release. A `commit` value of `self` is permitted only in a tagged publication snapshot and resolves to that checkout's HEAD; subsequent `main` records the concrete commit hash without moving the tag. The `main` branch can evolve while published tags retain their historical snapshots.

</details>

<details name="readme-language" open>
<summary><strong>简体中文</strong></summary>

本目录保存机器可读的发行记录，不存放安装包二进制。

- [manifest.json](manifest.json)：6 个公开发行组 / 23 个安装附件（19 个唯一安装包）的准确文件名、字节数、SHA-256、原始发布时间与下载 URL。
- [tag-map.json](tag-map.json)：7 个标签及其准确提交指向。
- [contact-refresh-20261119.json](contact-refresh-20261119.json)：联系方式修正的审核前后附件记录；标签指向及发布状态不变。
- [kernel-legacy-v1.0.2-acceptance.json](kernel-legacy-v1.0.2-acceptance.json)：新增 Linux 兼容发行组的脱敏用户空间测试范围与来源报告校验值。
- [根目录 SHA256SUMS](../SHA256SUMS)：供命令行验证的安装包校验值。

下载与说明见[发行索引](../docs/releases/README.md)，产品二进制附件位于 GitHub Releases。兼容环境见[专页](../docs/releases/openketupamk-kernel-legacy-v1.0.2.md)，[GitHub 标签页](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/tags)可跳转到对应发行。已打标签的发布快照可用 `commit: self` 表示该副本的 HEAD，后续 `main` 记录具体哈希，标签不移动。`main` 可以继续演进，已发布标签保留其历史快照。

</details>
