# 仓库审查与商业交付 / Repository review and commercial delivery

[Home / 项目主页](../../README.md) · [Documentation / 文档](../README.md)

点击语言标题即可在本页切换；另一语言会自动折叠。 / Select a language below; the other section collapses on this page.

<details name="readme-language">
<summary><strong>English</strong></summary>

Review date: **2026-11-18**. This review covers the public repository, publication records, and artifact consistency. Current proprietary core source and customers' installations are outside the repository reviewed here.

## Repository evidence

| Area | Evidence maintained here |
| --- | --- |
| Foundational project | All 111 tracked files match the original blobs, sizes, SHA-256 values, relative paths, and file modes; original Git tree and `legacy-v0.0.3` target retained |
| Distribution source records | Seventeen original files retain their bytes, including EULA, proprietary notice, test entitlement, and third-party records; relocated originals are mapped in the provenance manifest |
| Public installers | Five release groups, fifteen assets, 4,207,538,269 bytes; manifest values checked against GitHub asset names, sizes, digests, and direct download endpoints |
| Public test LIC | Two maintainer-designated files; bytes and SHA-256 verified, with consolidated English/Chinese instructions and direct downloads |
| Documentation | Language selection on the same page, local links and anchors, release/download metadata, and repository directory checks |
| Source and legal preservation | Original EULA/notice/third-party legal texts retained, separate historical and proprietary scopes documented |
| Secret exposure checks | Known private-key and token patterns checked without printing their contents; GitHub secret scanning and push protection are enabled. These checks are not an exhaustive security audit |
| Automation | Standard-library repository validator and GitHub Actions workflow; main and published-tag safeguards are documented in the policy |

Run `python3 tools/check_repository.py` to repeat the local preservation and documentation checks. Package hashes and repository checks do not establish successful installation, signature authenticity, solver correctness, or engineering signoff.

## Requirements before commercial delivery

| Item | Existing basis | Evidence still needed for the delivery |
| --- | --- | --- |
| Legal identity and ownership | Public author attribution, publishing identifier, and preserved legal texts | Verify the legal licensor's identity, ownership/third-party authority, and contracting entity; a nickname or domain is insufficient |
| Entitlement scope | Versioned product licensing and designated public test files | Confirm the delivered version's modules, duration, users/devices/concurrency, commercial rights, and verifiable issuance/acceptance records |
| Contract acceptance | Bilingual EULA revision `2026-10-19-r2` | Evidence that the actual installer/activation/contract process obtains and retains lawful acceptance of the applicable revision |
| Dependencies and source | Identified source/notice archives and prior inspection records | A complete per-installer SBOM, exact corresponding source and required build/relink materials; encrypted 1.0.0 payloads and full 1.0.2 coverage are not resolved by repository organization |
| Privacy and external models | Product descriptions include licensing and optional AI/network interfaces | Actual data-flow inventory, destinations, telemetry/activation behavior, privacy notice, customer authority, retention, and contractual controls appropriate to deployment |
| Platform and engineering validation | Published workflow entry points and preserved binaries | Installation, update/uninstall, compatibility, representative workflow tests, known limitations, and independent validation of engineering results |
| Supply-chain provenance | Asset digests and original records | Reproducible build/provenance evidence where applicable, actual code-signing identity and verification, and a vulnerability response process |
| Commercial operations | Private contact channels and written-agreement precedence | Agreed support lifecycle, delivery/acceptance criteria, payment/refund terms where applicable, and any jurisdiction-specific obligations |

These are specific delivery requirements, not claims that contracts, privacy mechanisms, certification, or legal review have already been completed. Preserve the evidence for the actual version and transaction rather than relying on a general README statement.

## References used for organization

Repository patterns were reviewed from [VS Code](https://github.com/microsoft/vscode), [PowerToys](https://github.com/microsoft/PowerToys), and [Ollama](https://github.com/ollama/ollama). The resulting layout is adapted to a distribution repository with a protected foundation and mixed legal scopes, rather than presented as a current open-source core-code repository.

</details>

<details name="readme-language" open>
<summary><strong>简体中文</strong></summary>

检查日期：**2026-11-18**。范围为公开仓库、发布记录与文件一致性；现行专有核心源码及客户实际安装环境不在本仓库检查范围内。

## 仓库核对依据

| 领域 | 本仓库保留的依据 |
| --- | --- |
| 基础项目 | 111 个跟踪文件的原始 blob、大小、SHA-256、相对路径和文件模式一致，原 Git tree 与 `legacy-v0.0.3` 指向保留 |
| 发行来源记录 | EULA、专有声明、测试授权、第三方记录等 17 个原始文件保留字节，迁移项由来源清单记录现位置 |
| 公开安装包 | 5 个发行组、15 个附件、共 4,207,538,269 字节；按 GitHub 文件名、大小、哈希与直接下载端点核对清单 |
| 公开测试 LIC | 两个维护者指定文件，核对字节与 SHA-256，提供统一中英文说明和直接下载 |
| 文档 | 同页语言切换、本地链接与锚点、下载/发行元数据及目录检查 |
| 源码与法律文本保全 | 原始 EULA、权利声明、第三方法律文本保留，历史开源与现行专有范围分别说明 |
| 凭据暴露检查 | 检查已知私钥及 token 特征，不输出内容；GitHub secret scanning 与推送保护已启用。这些检查不等于完整安全审计 |
| 自动化 | 标准库完整性检查脚本与 GitHub Actions；主分支及已发布标签的保护见维护规范 |

运行 `python3 tools/check_repository.py` 可重复执行本地保全与文档检查。文件哈希和仓库检查不证明安装成功、签名身份、求解正确或工程签核完成。

## 商业交付前应具备的依据

| 事项 | 已有基础 | 实际交付仍需的依据 |
| --- | --- | --- |
| 法律主体与权属 | 公开作者署名、发布标识及保留的法律文本 | 核实法律许可主体、权属/第三方授权及签约主体；昵称和域名不足以替代 |
| 授权范围 | 版本化产品授权及指定公开测试文件 | 确认交付版本的模块、期限、用户/设备/并发、商用范围，以及可核验的签发和接受记录 |
| 合同接受 | 中英文 EULA 修订 `2026-10-19-r2` | 实际安装器、激活或合同流程依法取得并保存适用修订的接受依据 |
| 依赖与源码 | 已识别的源码/声明归档及此前检查记录 | 逐安装包完整 SBOM、准确对应源码及必要构建/重链接材料；整理仓库未解决加密 1.0.0 载荷及 1.0.2 的完整覆盖依据 |
| 隐私与外部模型 | 产品说明涉及授权和可选 AI/网络接口 | 按实际部署梳理数据流、目的地、遥测/激活行为、隐私告知、客户权限、留存及合同控制 |
| 平台与工程验证 | 已发布入口和保留的二进制 | 安装、更新/卸载、兼容性、代表性工作流测试、已知限制及工程结果独立验证 |
| 供应链依据 | 附件哈希与原始记录 | 适用的构建/来源依据、实际代码签名身份与验证，以及漏洞响应流程 |
| 商业运营 | 私密联系渠道及专项书面协议优先规则 | 约定支持周期、交付/验收标准、适用的付款退款条款及特定法域义务 |

以上是具体交付要求，不表示合同、隐私机制、认证或法律审查已经完成。应保存实际版本和交易的依据，不能用通用 README 声明替代。

## 架构参考

本次阅读了 [VS Code](https://github.com/microsoft/vscode)、[PowerToys](https://github.com/microsoft/PowerToys) 和 [Ollama](https://github.com/ollama/ollama) 的仓库组织方式，并按“发行仓库、基础项目保全、混合许可范围”的实际情况调整结构，不将本仓库包装为现行核心源码开源仓库。

</details>
