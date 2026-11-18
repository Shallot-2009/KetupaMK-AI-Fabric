# 产品说明

简体中文 · [English](README.md) · [项目主页](../../README.zh-CN.md) · [文档](../README.zh-CN.md)

## 产品用途

KetupaMK 通过 CIR 配置组织 PCB、封装与互连工程工作流，帮助工程师准备输入、配置建模任务、协调外部工具并查看可追溯结果。本公开仓库提供产品发行与文档，不公开现行专有核心源码。

## 1.0.2 已发布功能

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

以上依据 [1.0.2 发行说明](../releases/openketupamk-v1.0.2.zh-CN.md)，不推定旧版具备相同功能。15 种入口本身不表示所有场景都已完成真实物理验收。

## 输入、依赖与输出

按工作流准备 CIR/include、版图、层叠/XML、网络选择、连接器模型、Touchstone 数据及规范模板等实际所需输入，并确认资料使用权。

涉及 Ansys、Cadence、MATLAB、Polar 等外部软件时，需要另外准备兼容安装环境与厂商许可。安装 KetupaMK 不会取得这些商业工具的授权。输出应结合实际工程与参考面进行专业核验。

## 发行类型

KetupaMK 产品发行与历史 Runtime 1.0.0 具有独立标签和安装包，历史 Beta 也是单独的预发布组。版本号和名称本身不证明接口或兼容性可互换。请结合[发行索引](../releases/README.zh-CN.md)与[安装说明](../installation/README.zh-CN.md)选择。

## 基础项目

[Ketupa_v0.0.3](../../history/README.zh-CN.md) 是项目的起源与基础，保留 HFSS 天线、传输线、MATLAB/CNN、LLM 交互及桌面自动化研究。该项目整体作为历史归档保留，原有环境命令不作为现行产品安装说明。
