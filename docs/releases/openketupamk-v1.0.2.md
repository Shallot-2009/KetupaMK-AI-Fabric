## KetupaMK 1.0.2

Windows / Linux x64 · 预发布 / Pre-release

### 1.0.2 功能

1. **CIR 统一入口**：通过 `ketupa run -sh main.cir` 调用工作流；CIR 定义全局参数，include 配置具体工程。
2. **15 种工作流入口**：支持现有协议与 PKG、PCB、Merge 场景组合；工程队列与网络 worker 分开控制，执行受许可证及资源约束。
3. **封装建模参数**：PKG/Merge 接入 bump、solderball、芯片朝向和端口阻抗配置；实际结构以输入版图、层叠及工程参数为准。
4. **多单位扫频**：CIR/include 支持 Hz、kHz、MHz、GHz，同条扫频可混用单位。
5. **DDR 抽头报告**：通过 `.tap` 读取 Touchstone、spec 和显式端口映射，输出 S21 delay 与相对 skew Excel；缺少信号或参考面审批时不自动判 PASS。
6. **可追溯命名**：输出批次带时间戳；工程、设计和 S 参数保留项目、场景、通道及 PKG/PCB 版本来源，避免多工程混淆。
7. **AI 数据接口**：开放全量网络审核、分类映射及 Excel 预处理；Skill/Agent 提醒检查 PKG/PCB 的版图和 XML、Merge 的两份版图和两份 XML，以及涉及连接器时所需的真实模型。
8. **Skill / Agent / MCP**：可选配置已检测客户端，保留用户已有设置；工作区 `ai` 目录用于手动定制与备份，MCP 默认只读。
9. **Web 连接接口**：提供鉴权 HTTPS 本地接口与前端 SDK，供网页 UI 接入；不等同于特定生产网站已完成联调。
10. **GDS Interposer 辅助工作流**：按统一工作流架构组织导入流程；目前仅导入，不包含求解或电气签核。
11. **平台与保护**：Windows 提供 Launcher，Linux 为命令行；原生模块、加密资源和签名清单继续使用，执行需要有效的 1.0.2 许可证。

本次发布不代表 15 种场景已全部完成真实物理验收；建模需要兼容的 Ansys/Cadence 环境及相应厂商授权。

### 下载与安装

| 系统 / Platform | 安装包 / Package |
| --- | --- |
| Windows x64 · EXE | [openketupa-ai-fabric-1.0.2-Windows-x64-Setup.exe](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.2/openketupa-ai-fabric-1.0.2-Windows-x64-Setup.exe) |
| Linux x64 · TAR.GZ | [openketupa-ai-fabric-linux-1.0.2-x64.tar.gz](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.2/openketupa-ai-fabric-linux-1.0.2-x64.tar.gz) |
| Linux amd64 · DEB | [openketupa-ai-fabric-linux_1.0.2_amd64.deb](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.2/openketupa-ai-fabric-linux_1.0.2_amd64.deb) |

- **Windows x64**：下载 EXE，运行安装器，完成许可证配置后使用。
- **Linux x64**：TAR.GZ 与 DEB 二选一，不需要重复安装。Linux 不包含 Launcher。
- **安装与激活步骤**：[产品下载页](https://106.54.223.4:8081/#/downloads)。
- **许可与第三方材料**：[EULA](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/blob/main/EULA.md) · [Third-party](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/tree/main/third-party)。

### What's new

- Unified licensed CIR entry point: `ketupa run -sh main.cir`, with project-specific include modules.
- Fifteen existing workflow entry points, project queues, network workers, and parameterized PKG/Merge bump/ball/port configuration.
- Mixed Hz/kHz/MHz/GHz sweep units and traceable timestamped project/channel/source naming.
- DDR-only `.tap` S21 group-delay and relative-skew Excel reports using explicit port maps and specification templates.
- Editable AI network-inventory/Excel preprocessing, modeling-input checks, opt-in Skill/Agent/MCP integration, and authenticated HTTPS interfaces with a frontend SDK.
- GDS Interposer import-only workflow; Windows Launcher and Linux CLI distribution.
- Native modules, encrypted resources and signed manifests; a valid version-scoped license is required. No absolute anti-reversing guarantee is implied.

This pre-release is not a claim of completed fifteen-case physical acceptance. Compatible EDA tools and their vendor entitlements remain required. GitHub's automatically generated source archives contain repository materials, not the protected product installers.

### SHA-256

```text
b97ce055bf5390b2f63a4eb6200bc121f6144b081ea944e151e953b1a2412258  openketupa-ai-fabric-1.0.2-Windows-x64-Setup.exe
f37a9a68af7b97fcdc6c1488b61bd6aad43d96d11ed1a702936a0bbff6f19567  openketupa-ai-fabric-linux-1.0.2-x64.tar.gz
3afda8a1882d9a23d69f1c3a6927f6beeebe8c498304ed2ad04f0e968a872901  openketupa-ai-fabric-linux_1.0.2_amd64.deb
```

---

作者 / Author: **Asenjo HB**  
邮箱 / Email: [asenjoaupa@gmail.com](mailto:asenjoaupa@gmail.com) · [3405802009@qq.com](mailto:3405802009@qq.com)


---

迁移来源 / Migration provenance: first published / 原始发布时间 `2026-11-12T06:10:33Z` in repository ID `1424671956`; migrated to repository ID `1005327414` on 2026-11-18. Installer filenames, bytes, and pre-release status are preserved. 原安装包文件名、字节与预发布状态保持不变。See / 详见 [migration record](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/blob/main/docs/MIGRATION.md).
