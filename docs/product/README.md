# 产品说明 / Product scope

[Home / 项目主页](../../README.md) · [Documentation / 文档](../README.md)

点击语言标题即可在本页切换；另一语言会自动折叠。 / Select a language below; the other section collapses on this page.

<details name="readme-language">
<summary><strong>English</strong></summary>

## Purpose

KetupaMK is oriented toward analog IC, channel algorithms, advanced packaging, Interposer and SI/PI engineering. CIR configuration organizes PCB, package and interconnect workflows, input preparation, compatible external tools and traceable outputs. See [engineering domains](DOMAINS.md) for the application directions and their current boundaries. This public repository distributes packaged products and documentation; current proprietary core source is maintained separately.

## What it can do

The current 1.0.3 preview provides PCB, package, and cascade CIR workflows, Touchstone conversion, DDR reports, and Skill/Agent/MCP input preparation. The detailed capabilities below are documented for 1.0.2 and should be checked against the installed version and [1.0.3 release guide](../releases/openketupamk-v1.0.3.md).

| Capability | Scope and required inputs |
| --- | --- |
| CIR execution | `ketupa run -sh main.cir`; global settings in CIR and project details in include files |
| Existing workflow entries | Fifteen entries across existing protocols and PKG/PCB/Merge combinations; queues and network workers have separate resource controls |
| PKG and Merge configuration | Bump, solderball, chip orientation, and port impedance; actual geometry follows layout, stackup, and project parameters |
| Sweep units | Hz, kHz, MHz, and GHz may be mixed within a sweep |
| DDR `.tap` reports | Touchstone, specifications, and explicit port mapping produce S21 delay and relative-skew Excel reports; missing signal or reference-plane approval does not automatically yield PASS |
| Traceability | Timestamped batches and project/scenario/channel/PKG/PCB identifiers in outputs |
| AI input preparation | Network inventory review, classification mapping, and Excel preprocessing; PKG/PCB need their layout and XML, Merge needs both layouts and both XML files, and connectors need their real models |
| Client integration | Optional configuration for detected Skill/Agent/MCP clients, preservation of user settings, editable workspace `ai` materials; MCP is read-only by default in the published description |
| Web integration | Authenticated local HTTPS interfaces and a frontend SDK; no production website integration is asserted |
| GDS Interposer | Import-only assistance, without solver execution or electrical signoff |
| Platforms | Windows Launcher and Linux CLI; valid version-scoped licensing is required |

The detailed scope comes from the [1.0.2 release guide](../releases/openketupamk-v1.0.2.md). The fifteen entries do not establish physical acceptance for every scenario.

## How to use a workflow

| Workflow | Prepare | Start with |
| --- | --- | --- |
| PKG or PCB | Layout, matching XML stackup, network selection and project configuration | `ketupa run -sh main.cir check` |
| Merge | Both layouts, both XML files, connection mapping and project configuration | `ketupa run -sh main.cir check` |
| DDR report | Touchstone file, explicit port map, frequencies, reference planes and approved specification | The `.tap` workflow in the installed product |
| GDS Interposer | GDS source and import settings | Import and inspect the resulting structure |

For a connector, provide its actual `.a3dcomp` model. Confirm inputs with the [installation and environment guide](../installation/README.md) before executing modeling or analysis.

## Inputs, dependencies, and outputs

Workflow inputs may include CIR/include files, layouts, stackups/XML, network selections, connector models, Touchstone data, and specification templates. Supply the items required by the selected workflow and confirm data rights before use.

External Ansys, Cadence, MATLAB, Polar, or other vendor software requires separate compatible installations and vendor entitlements where applicable. Product installation does not supply those commercial rights. Outputs require engineering review for the actual project and reference planes.

## Distribution types

KetupaMK product releases and the historical Runtime 1.0.0 distribution have separate release tags and installers. The historical Beta is a separate pre-release. Version numbers and names alone do not establish interchangeable interfaces or compatibility. Use the [release index](../releases/README.md) and [installation guide](../installation/README.md).

The [Legacy Linux 1.0.2 environment](../releases/openketupamk-kernel-legacy-v1.0.2.md) is a separate compatibility build of the application and bundled runtime for x86_64/glibc ≥ 2.28, including Rocky/RHEL 8 and Ubuntu 20.04 userspaces. RPM, DEB, RUN and TAR.GZ are four alternatives, not four components. This build changes the binary compatibility baseline rather than replacing the operating system/kernel or restoring v0.0.3 algorithms; native EDA and kernel support need separate validation.

## Foundation

[Ketupa_v0.0.3](../../history/README.md) is the original foundational project. It preserves research in HFSS antennas, transmission lines, MATLAB/CNN, LLM interaction, and desktop automation. It is retained as a complete historical project; its old setup instructions are not current-product installation instructions.

</details>

<details name="readme-language" open>
<summary><strong>简体中文</strong></summary>

## 产品用途

KetupaMK 面向模拟 IC、信道算法、先进封装、Interposer 与 SI/PI 工程，通过 CIR 配置组织 PCB、封装和互连工作流，衔接输入准备、兼容的外部工具与可追溯输出。各技术方向及当前范围见[技术方向](DOMAINS.md)。本公开仓库提供产品发行与文档，现行专有核心源码单独维护。

## 能做什么

当前 1.0.3 预览版提供 PCB、封装、级联 CIR 工作流，以及 Touchstone 转换、DDR 报告和 Skill/Agent/MCP 输入准备。下表详细功能依据 1.0.2 文档，使用时应与已安装版本和 [1.0.3 发行说明](../releases/openketupamk-v1.0.3.md)核对。

| 功能 | 范围与输入要求 |
| --- | --- |
| CIR 执行入口 | `ketupa run -sh main.cir`；CIR 定义全局设置，include 文件配置具体工程 |
| 既有工作流入口 | 现有协议与 PKG/PCB/Merge 组合形成 15 种入口；工程队列与网络 worker 分别控制资源 |
| PKG 与 Merge 配置 | bump、solderball、芯片朝向、端口阻抗；实际几何依版图、层叠与工程参数确定 |
| 扫频单位 | 同一条扫频可混用 Hz、kHz、MHz、GHz |
| DDR `.tap` 报告 | Touchstone、规范及显式端口映射生成 S21 延迟与相对 skew Excel；缺少信号或参考面审批时不自动判 PASS |
| 结果追溯 | 输出批次带时间戳，保留工程、场景、通道及 PKG/PCB 版本来源 |
| AI 输入准备 | 网络清单审核、分类映射和 Excel 预处理；PKG/PCB 需要版图与 XML，Merge 需要两份版图与两份 XML，连接器需要真实模型 |
| 客户端集成 | 可选配置已检测的 Skill/Agent/MCP 客户端，保留用户已有设置，工作区 `ai` 资料可编辑；公开说明中的 MCP 默认为只读 |
| Web 接口 | 带鉴权的本地 HTTPS 接口与前端 SDK；不宣称生产网站已经完成联调 |
| GDS Interposer | 仅提供导入辅助，不包含求解或电气签核 |
| 平台 | Windows Launcher、Linux CLI；执行需要适用版本的有效授权 |

详细范围依据 [1.0.2 发行说明](../releases/openketupamk-v1.0.2.md)。15 种入口本身不表示所有场景都已完成真实物理验收。

## 怎么使用工作流

| 工作流 | 准备输入 | 先执行 |
| --- | --- | --- |
| PKG 或 PCB | 版图、对应 XML 层叠、网络选择和工程配置 | `ketupa run -sh main.cir check` |
| Merge | 两份版图、两份 XML、连接映射和工程配置 | `ketupa run -sh main.cir check` |
| DDR 报告 | Touchstone 文件、明确端口映射、频率、参考面和获批规范 | 已安装产品的 `.tap` 工作流 |
| GDS Interposer | GDS 源文件和导入设置 | 导入并检查所得结构 |

涉及连接器时，还需提供真实 `.a3dcomp` 模型。执行建模或分析前，按[安装与环境指南](../installation/README.md)确认输入。

## 输入、依赖与输出

按工作流准备 CIR/include、版图、层叠/XML、网络选择、连接器模型、Touchstone 数据及规范模板等实际所需输入，并确认资料使用权。

涉及 Ansys、Cadence、MATLAB、Polar 等外部软件时，需要另外准备兼容安装环境与厂商许可。安装 KetupaMK 不会取得这些商业工具的授权。输出应结合实际工程与参考面进行专业核验。

## 发行类型

KetupaMK 产品发行与历史 Runtime 1.0.0 具有独立标签和安装包，历史 Beta 也是单独的预发布组。版本号和名称本身不证明接口或兼容性可互换。请结合[发行索引](../releases/README.md)与[安装说明](../installation/README.md)选择。

[旧版 Linux 1.0.2 兼容环境](../releases/openketupamk-kernel-legacy-v1.0.2.md)是面向 x86_64/glibc ≥ 2.28 的独立兼容构建，包括 Rocky/RHEL 8 和 Ubuntu 20.04 用户空间。RPM、DEB、RUN、TAR.GZ 是四种可选格式，不是四个组件。它调整二进制兼容基线，不替换操作系统/内核，也不恢复 v0.0.3 业务算法；实际 EDA 与内核支持需另行核验。

## 基础项目

[Ketupa_v0.0.3](../../history/README.md) 是项目的起源与基础，保留 HFSS 天线、传输线、MATLAB/CNN、LLM 交互及桌面自动化研究。该项目整体作为历史归档保留，原有环境命令不作为现行产品安装说明。

</details>
