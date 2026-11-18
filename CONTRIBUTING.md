# 协作指南 / Contributing

[Home / 项目主页](README.md) · [Documentation / 文档](docs/README.md)

点击语言标题即可在本页切换；另一语言会自动折叠。 / Select a language below; the other section collapses on this page.

<details name="readme-language">
<summary><strong>English</strong></summary>

This public repository accepts product reports, documentation corrections, translation improvements, and preservation/metadata fixes. Current proprietary core development is maintained separately.

## Report a problem

Use the issue forms with the product version, platform, installer filename, expected behavior, minimal reproduction, and sanitized output. Documentation reports should identify the page and language. Use [private security reporting](SECURITY.md) for vulnerabilities, private entitlements, customer data, or licensing disputes.

## Propose a change

1. Keep the change focused and explain its reason. Update both maintained language versions and their navigation.
2. Preserve `history/Ketupa_v0.0.3/`, original legal texts, source snapshots, installer hashes, and existing tag targets. Add historical corrections outside the frozen archive.
3. Keep downloads directly linked to official release assets. Do not add installers to Git or include private credentials/entitlements.
4. Run `python3 tools/check_repository.py` and include the result in the pull request.

Submit only material you have the right to disclose and contribute. Identify third-party sources and their applicable terms. A contribution does not transfer unrelated intellectual property, grant current proprietary core access, or relicense existing historical/third-party material. Licensing questions should be agreed with the maintainer before inclusion.

</details>

<details name="readme-language" open>
<summary><strong>简体中文</strong></summary>

本公开仓库接收产品反馈、文档纠正、翻译改进及保全/元数据修正。现行专有核心开发单独维护。

## 反馈问题

使用 Issue 表单提供产品版本、平台、安装包文件名、预期行为、最小复现及脱敏输出。文档问题应注明页面和语言。漏洞、私有授权、客户数据或授权争议请通过[私密安全渠道](SECURITY.md)联系。

## 提交变更

1. 说明原因，保持范围明确，同时更新对应中英文文档与导航。
2. 保留 `history/Ketupa_v0.0.3/`、原始法律文本、来源快照、安装包哈希及既有标签指向。历史纠正写在冻结归档之外。
3. 下载直接指向正式 Release 附件，不向 Git 添加安装包或私密凭据/授权。
4. 运行 `python3 tools/check_repository.py`，在 PR 中附上结果。

仅提交自己有权披露和贡献的材料，注明第三方来源及适用条款。贡献不转移无关知识产权，不授予现行专有核心访问权，也不重新许可历史/第三方资料。许可问题应在纳入前与维护者明确。

</details>
