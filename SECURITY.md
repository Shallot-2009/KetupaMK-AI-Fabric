# 安全报告 / Security reporting

[Home / 项目主页](README.md) · [Documentation / 文档](docs/README.md)

点击语言标题即可在本页切换；另一语言会自动折叠。 / Select a language below; the other section collapses on this page.

<details name="readme-language">
<summary><strong>English</strong></summary>

## Private contact

Send vulnerability, entitlement-exposure, privacy, or rights reports to [asenjoaupa@gmail.com](mailto:asenjoaupa@gmail.com); alternative: [3405802009@qq.com](mailto:3405802009@qq.com). This is a reporting channel, not a guaranteed response-time or maintenance commitment.

Include the affected product/tag, package name and hash, platform, a minimal description, impact, and safe reproduction steps. Start with sanitized information. Coordinate any necessary sensitive transfer privately; do not post customer projects, private `.lic` files, device fingerprints, API keys, signing keys, or complete sensitive logs in issues.

## Version status

1.0.2 is the current published preview, including the separate [Legacy Linux compatibility distribution](docs/releases/openketupamk-kernel-legacy-v1.0.2.md). Distinguish standard and compatibility tags when reporting a problem; a lower ABI baseline does not establish operating-system security maintenance or guaranteed support for old kernels. 1.0.1, product/Runtime 1.0.0, Beta, and v0.0.3 remain available as historical distributions or records. Their availability does not establish an active security maintenance window. Support and update obligations follow applicable agreements; the maintainer should assess each report's affected versions.

## Publication handling

The only public entitlements approved for this repository are the two files listed in the [test license index](licenses/README.md). Do not publish other licenses or secrets. Report a suspected exposure privately and revoke/rotate affected credentials through the actual issuer where appropriate; changing a repository file does not invalidate copies or old Git objects.

GitHub secret scanning and push protection supplement review. Hashes and these checks do not certify installer safety, cryptographic authenticity, or engineering correctness. Third-party issues should also be handled under the relevant upstream disclosure process.

</details>

<details name="readme-language" open>
<summary><strong>简体中文</strong></summary>

## 私密联系

漏洞、授权暴露、隐私或权利问题请发送至 [asenjoaupa@gmail.com](mailto:asenjoaupa@gmail.com)，备用邮箱：[3405802009@qq.com](mailto:3405802009@qq.com)。此为报告渠道，不承诺固定响应时限或维护周期。

请提供受影响产品/标签、安装包名称与哈希、平台、最小问题描述、影响及安全复现步骤，初次联系先使用脱敏信息。确需传递敏感材料时另行私下协调；不要在 Issue 中上传客户工程、私有 `.lic`、设备指纹、API key、签发密钥或完整敏感日志。

## 版本状态

1.0.2 为当前公开预览版，包含独立的[旧版 Linux 兼容发行组](docs/releases/openketupamk-kernel-legacy-v1.0.2.md)。反馈时请区分标准版和兼容版标签；较低 ABI 基线不表示操作系统仍受安全维护，也不保证所有旧内核均受支持。1.0.1、产品/Runtime 1.0.0、Beta 和 v0.0.3 作为历史发行或记录保留，公开可下载不表示存在持续安全维护期。支持与更新义务依适用协议处理，维护者应逐项判断报告影响的版本。

## 发布处理

本仓库指定公开的授权仅限[测试授权索引](licenses/README.md)列出的两个文件，不应发布其他授权或凭据。发现疑似暴露时请私密报告，并按实际签发渠道处理必要的撤销/轮换；修改仓库文件不会使已有副本或旧 Git 对象失效。

GitHub secret scanning 和推送保护用于辅助检查；哈希与这些检查不认证安装包安全、密码学真实性或工程正确性。涉及第三方组件的问题还应遵循对应上游披露流程。

</details>
