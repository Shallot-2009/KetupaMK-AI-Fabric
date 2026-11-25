# 测试许可证 / Test licenses

[Home / 项目主页](../README.md) · [Documentation / 文档](../docs/README.md)

更新 / Updated: **2026-11-25**。共三份，按签发时间从新到旧排列。 / Three files, newest first.

<details name="readme-language">
<summary><strong>English</strong></summary>

## Choose a license

### 1. Internal test for 1.0.3 — latest

[Open the GitHub download page](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/blob/main/licenses/openketupamk-1.0.3-internal-test-12w.lic)

- File: `openketupamk-1.0.3-internal-test-12w.lic`.
- Issued: **2026-11-25 14:05:03 Beijing time**; **12 weeks**, **3 concurrent instances**.
- Recorded version scopes: Beta, 1.0.0, 1.0.1, 1.0.2, and **1.0.3**. For a 1.0.3 installation, choose this file.
- The 1.0.3 scope includes `core`, `service.remote`, `workflow.preprocess`, `workflow.simulation`, `workflow.postprocess`, and `workflow.signoff`.
- This is the corrected 3-instance issue. The mistaken unlimited issue from 14:04:39 is excluded from this publication.

### 2. Offline test — earlier versions

[Open the GitHub download page](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/blob/main/licenses/openketupamk-offline-test-12w.lic)

- File: `openketupamk-offline-test-12w.lic`.
- Issued: **2026-11-16 23:23:32 Beijing time**; **12 weeks**, **3 concurrent instances**.
- Recorded version scopes: Beta and 1.0.0–1.0.2. This file contains no 1.0.3 module scope.
- The previously published bytes and filename are retained. The channel name alone does not confirm that a client supports offline activation.

### 3. Internal test — earlier versions

[Open the GitHub download page](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/blob/main/licenses/openketupamk-internal-test-12w.lic)

- File: `openketupamk-internal-test-12w.lic`.
- Issued: **2026-11-13 08:17:48 Beijing time**; **12 weeks**, **3 concurrent instances**.
- Recorded version scopes: Beta and 1.0.0–1.0.2. This file contains no 1.0.3 module scope.
- The previously published bytes and filename are retained. [Original instructions](../docs/provenance/internal-test-README.before-flattening.md) remain available as a source record.

## Download and activate

1. Check the version of your installed KetupaMK, then choose the corresponding file above.
2. The link opens the file page on GitHub. Click **Download raw file** in that page's toolbar; keep the `.lic` extension. Do not save the HTML page as a license.
3. In the installed version's license manager or activation flow, select the downloaded `.lic`. Follow its device/MAC and server connection prompts.
4. On Linux versions that provide the CLI activation flow, run `ketupa license machine`, then `ketupa license install <file.lic> --mac <local-MAC>`, and finally `ketupa license status`. For another installation layout, follow the [installation guide](../docs/installation/README.md).
5. Confirm the client reports a valid license and the required module scope before starting a task. EDA tools require their own installation and licenses.

The validity period follows the signed policy and activation records. Downloading again, renaming, or copying the file does not renew or reset it. Module availability follows the selected version's scope; a successful download is not an activation or simulation test.

## Publication and file verification

Only these three maintainer-designated public test files are published. No unlimited license is included. The original signed bytes are retained; the new file's public name is normalized without reissuing the license.

The website lists the same three files vertically, with the newest first. Each download button opens the corresponding GitHub file page. Digests are kept in [SHA256SUMS](SHA256SUMS) and [manifest.json](manifest.json), without displaying long hashes in the download cards.

For an optional file consistency check, download `SHA256SUMS` with the three `.lic` files and run `sha256sum -c SHA256SUMS`. This verifies bytes only, not activation, expiry, EDA solving, or signature trust. Terms are in [LICENSE.md](../LICENSE.md); contact [the maintainer](mailto:asenjoaupa@gmail.com) for scope and compatibility questions.

</details>

<details name="readme-language" open>
<summary><strong>简体中文</strong></summary>

## 按版本选择许可证

### 1. 1.0.3 内部测试 — 最新版

[打开 GitHub 下载页面](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/blob/main/licenses/openketupamk-1.0.3-internal-test-12w.lic)

- 文件名：`openketupamk-1.0.3-internal-test-12w.lic`。
- 签发时间：**北京时间 2026-11-25 14:05:03**；**12 周、3 并发**。
- 签发记录中的版本范围：Beta、1.0.0、1.0.1、1.0.2 和 **1.0.3**。安装 1.0.3 时选择这一份。
- 1.0.3 模块包括：`core`、`service.remote`、`workflow.preprocess`、`workflow.simulation`、`workflow.postprocess`、`workflow.signoff`。
- 这一份是修正后的 3 并发版本，14:04:39 误签发的无限并发版本不在此次发布中。

### 2. 离线测试 — 旧版本

[打开 GitHub 下载页面](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/blob/main/licenses/openketupamk-offline-test-12w.lic)

- 文件名：`openketupamk-offline-test-12w.lic`。
- 签发时间：**北京时间 2026-11-16 23:23:32**；**12 周、3 并发**。
- 签发记录中的版本范围：Beta 和 1.0.0–1.0.2，未包含 1.0.3 模块授权。
- 保留此前公开的文件名和原始内容。名称中的“离线测试”不能单独证明客户端已经支持离线激活。

### 3. 内部测试 — 旧版本

[打开 GitHub 下载页面](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/blob/main/licenses/openketupamk-internal-test-12w.lic)

- 文件名：`openketupamk-internal-test-12w.lic`。
- 签发时间：**北京时间 2026-11-13 08:17:48**；**12 周、3 并发**。
- 签发记录中的版本范围：Beta 和 1.0.0–1.0.2，未包含 1.0.3 模块授权。
- 保留此前公开的文件名和原始内容；[原始说明](../docs/provenance/internal-test-README.before-flattening.md)继续作为来源记录保存。

## 下载和激活步骤

1. 确认本机安装的 KetupaMK 版本，按上面的版本范围选择文件。
2. 链接会打开对应的 GitHub 文件页。在页面工具栏点击 **Download raw file** 下载，保留 `.lic` 扩展名，不要将网页 HTML 保存为许可证。
3. 打开对应版本的许可证管理器或激活流程，选择下载的 `.lic`，按界面要求完成本机 MAC、设备信息和服务器连接。
4. 支持命令行激活的 Linux 版本依次执行：`ketupa license machine`、`ketupa license install <file.lic> --mac <local-MAC>`、`ketupa license status`。安装路径不同的情况参考[安装说明](../docs/installation/README.md)。
5. 确认客户端显示授权有效、所需模块已授权，再启动任务；EDA 工具另行安装和授权。

有效期依据签名策略与实际激活记录计算。重新下载、改名或复制不会续期或重置。模块能否使用取决于对应版本的授权范围；下载成功不等于已激活或已完成仿真验收。

## 发布与文件核对

本目录仅公开维护者指定的这三份测试许可证，不包含无限并发版本。签名文件内容保持原样；新文件仅统一公开名称，不重新签发。

网站也按同样顺序竖排展示三份许可证，最新版本在上方。下载按钮打开各自的 GitHub 文件页。文件摘要保存在 [SHA256SUMS](SHA256SUMS) 和 [manifest.json](manifest.json) 中，下载卡片不展示长哈希。

如需核对文件是否完整，将 `SHA256SUMS` 和三份 `.lic` 放到同一目录后运行 `sha256sum -c SHA256SUMS`。此操作仅验证文件一致性，不代替激活、到期状态、EDA 求解或签名信任校验。使用条款见 [LICENSE.md](../LICENSE.md)；范围和兼容性问题请[联系维护者](mailto:asenjoaupa@gmail.com)。

</details>
