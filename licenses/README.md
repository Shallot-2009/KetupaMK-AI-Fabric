# 测试许可证 / Test licenses

[Home / 项目主页](../README.md) · [Documentation / 文档](../docs/README.md)

<details name="readme-language">
<summary><strong>English</strong></summary>

## Select a license

| Test license | Version scope |
| --- | --- |
| [Offline test](openketupamk-offline-test-12w.lic) | Signed for Beta and 1.0.0–1.0.2. |
| [Internal test](openketupamk-internal-test-12w.lic) | Signed for Beta and 1.0.0–1.0.2. |

KetupaMK 1.0.3 for Windows and Linux accepts the two listed test licenses within their existing signed terms. A newly issued 1.0.3 license must include the 1.0.3 modules required by your workflow. Available activation methods depend on the signed policy and the installed client.

## Download and activate

1. Open the file link and select **Download raw file** on GitHub to save the `.lic`.
2. Use the license manager or activation workflow in your installed KetupaMK version. Follow the device and server prompts.
3. On Linux versions with CLI activation, use `ketupa license machine` to find the device address, then `ketupa license install <file.lic> --mac <local-MAC>` and `ketupa license status`.
4. Confirm that the client reports valid entitlement for the modules you need. Follow the [installation guide](../docs/installation/README.md) for your package. EDA tools require separate installation and licensing.

Downloading or copying a file does not restart its validity period. For optional file verification, use [SHA256SUMS](SHA256SUMS). See the [software terms](../LICENSE.md) or [contact the maintainer](mailto:asenjoaupa@gmail.com) about license scope and compatibility.

</details>

<details name="readme-language" open>
<summary><strong>简体中文</strong></summary>

## 选择测试许可证

| 测试许可证 | 适用版本 |
| --- | --- |
| [离线测试](openketupamk-offline-test-12w.lic) | 签名范围为 Beta 和 1.0.0–1.0.2。 |
| [内部测试](openketupamk-internal-test-12w.lic) | 签名范围为 Beta 和 1.0.0–1.0.2。 |

Windows 和 Linux 的 KetupaMK 1.0.3 可按原签名条款使用上表两份测试许可证。新签发的 1.0.3 授权需包含工作流所需的 1.0.3 模块。可用的激活方式取决于签名策略和已安装的客户端。

## 下载和激活

1. 打开对应文件链接，在 GitHub 文件页点击 **Download raw file** 保存 `.lic`。
2. 使用已安装版本的许可证管理器或激活流程，按提示填写设备信息和连接服务器。
3. Linux 如支持命令行激活，先用 `ketupa license machine` 查看本机地址，再运行 `ketupa license install <file.lic> --mac <local-MAC>` 和 `ketupa license status`。
4. 确认客户端显示所需模块已获有效授权。各格式操作见[安装说明](../docs/installation/README.md)。EDA 工具需另行安装和授权。

重新下载或复制文件不会重置有效期。如需核对文件，使用 [SHA256SUMS](SHA256SUMS)。适用条款见[软件许可说明](../LICENSE.md)，授权范围和兼容性问题请[联系维护者](mailto:asenjoaupa@gmail.com)。

</details>
