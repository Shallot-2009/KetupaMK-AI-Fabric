# 技术方向 / Engineering domains

[Home / 主页](../../README.md) · [Product scope / 产品功能](README.md) · [Project map / 项目导航](../PROJECT_MAP.md)

<details name="readme-language">
<summary><strong>English</strong></summary>

KetupaMK connects engineering data, CIR configuration, compatible EDA tools and reproducible outputs across five application directions.

| Direction | Engineering focus | Current product connection |
| --- | --- | --- |
| Analog IC | Chip-to-package and board-level electrical interfaces | Project input preparation and package/interconnect workflows; this does not identify KetupaMK as a transistor-level SPICE or PDK signoff solver |
| Channel algorithms | Multiport channel data, port mapping and specification-driven analysis | Touchstone processing and cascading; DDR S21 delay and relative-skew reporting with explicit mappings |
| Advanced packaging | Package/PCB assembly and exposed electrical interfaces | PKG and Merge workflows; layout, XML stackup, bump, solderball, orientation and port configuration |
| Interposer | GDS-based intermediate interconnect structures | Explicit GDS Interposer import workflow; 1.0.2 scope is import-only, not solver execution or electrical signoff |
| SI/PI | Signal and power integrity engineering workflows | DDR/PCIe/SerDes/clock/custom project preparation and interconnect modeling; reports and acceptance criteria depend on the selected workflow and supplied specifications |

The application directions do not replace version-specific capability checks. See [published 1.0.2 scope](README.md) and [release notes](../releases/README.md).

Typical path: prepare inputs → configure CIR/includes → run the licensed KetupaMK entry → review model/channel results → apply approved specifications and archive reports.

Author: **Asenjo HB** · [asenjoaupa@gmail.com](mailto:asenjoaupa@gmail.com) · [3405802009@qq.com](mailto:3405802009@qq.com)

</details>

<details name="readme-language" open>
<summary><strong>简体中文</strong></summary>

KetupaMK 通过工程数据、CIR 配置、兼容的 EDA 工具与可追溯输出，连接五个应用方向。

| 方向 | 工程关注点 | 当前产品衔接 |
| --- | --- | --- |
| 模拟 IC | 芯片到封装、板级接口的电气环境 | 工程输入准备、封装与互连工作流；不等同于晶体管级 SPICE 或 PDK 签核求解器 |
| 信道算法 | 多端口信道、端口映射与规范驱动分析 | Touchstone 处理与级联；基于显式映射的 DDR S21 延迟与相对 skew 报告 |
| 先进封装 | 封装/PCB 装配与外露电气接口 | PKG、Merge 工作流；版图、XML 层叠、bump、solderball、朝向和端口配置 |
| Interposer 中介层 | 基于 GDS 的中介层互连结构 | 独立的 GDS Interposer 导入工作流；1.0.2 的功能范围是导入，不包含求解或电气签核 |
| SI/PI | 信号完整性与电源完整性工程工作流 | DDR/PCIe/SerDes/时钟/自定义工程准备与互连建模；报告及验收项依具体工作流和输入规范确定 |

技术方向不替代版本功能确认。具体见[1.0.2 产品功能](README.md)与[发行说明](../releases/README.md)。

典型流程：准备输入 → 配置 CIR/include → 通过已授权的 KetupaMK 入口执行 → 审核模型/信道结果 → 按已批准的规范判定并归档报告。

作者：**Asenjo HB** · [asenjoaupa@gmail.com](mailto:asenjoaupa@gmail.com) · [3405802009@qq.com](mailto:3405802009@qq.com)

</details>
