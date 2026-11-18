# 公开测试授权

简体中文 · [English](README.md) · [项目主页](../README.zh-CN.md) · [文档](../docs/README.zh-CN.md)

两个 LIC 文件直接存放在本目录。它们由维护者指定用于公开测试，文件内容保持不变。

| 文件 | 字节数 | 直接下载 |
| --- | --- | --- |
| [Ketupa-ketupamk_offline_test_12w-20261116-232329-233.lic](Ketupa-ketupamk_offline_test_12w-20261116-232329-233.lic) | 4,781 | [LIC](https://raw.githubusercontent.com/Shallot-2009/KetupaMK-AI-Fabric/main/licenses/Ketupa-ketupamk_offline_test_12w-20261116-232329-233.lic) |
| [openketupamk-internal-test-12w.lic](openketupamk-internal-test-12w.lic) | 4,836 | [LIC](https://raw.githubusercontent.com/Shallot-2009/KetupaMK-AI-Fabric/main/licenses/openketupamk-internal-test-12w.lic) |

<a id="offline-test"></a>

## 离线测试

`Ketupa-ketupamk_offline_test_12w-20261116-232329-233.lic` 于 2026-11-18 从维护者提供的 `package` 目录同步。请使用所安装产品版本支持的流程导入或配置。

<a id="internal-test"></a>

## 内测授权

`openketupamk-internal-test-12w.lic` 为此前已经公开的内测授权文件。[原始说明](../docs/provenance/internal-test-README.before-flattening.md)作为来源记录保留。

## 使用范围与发布规则

`.lic` 是软件使用授权文件，与仓库的[著作权及合同条款](../LICENSE.zh-CN.md)分别处理。实际版本、模块、期限、设备限制及商用权利以原文件和有效协议为准。文件名中的 `12w` 为原始命名，下载或移动文件不会重新计算有效期。

此目录仅发布这两个指定的公开测试文件。不得上传客户/生产授权、私有签发密钥、设备指纹、API key 或服务凭据。范围、兼容性、到期及签发问题请私下联系维护者。公开文件不等于签发、续期、扩大或验证授权。

## 校验文件

将 [SHA256SUMS](https://raw.githubusercontent.com/Shallot-2009/KetupaMK-AI-Fabric/main/licenses/SHA256SUMS) 与两个 LIC 下载到同一目录，执行：

```bash
sha256sum -c SHA256SUMS
```

```text
2d1c5e8ae2e09ada57ffe6aa434d8016f4c9393c3eb08fb447c022778eb60031  Ketupa-ketupamk_offline_test_12w-20261116-232329-233.lic
37ee8efa33d74c5197092a2678bda1daa0e6f074c3a04cc378873396c266db01  openketupamk-internal-test-12w.lic
```

哈希只验证文件一致性，不证明签名有效、已经激活、离线运行成功或所有模块可用；文件不包含第三方 EDA 工具授权。

[文件元数据](manifest.json) · [授权联系](mailto:asenjoaupa@gmail.com)
