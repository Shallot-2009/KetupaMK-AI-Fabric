# 历史版本归档 / Historical archive

[中文主页](../README.zh-CN.md) · [English home](../README.md) · [起源与来源 / Origin and provenance](ORIGIN.md)

## 中文

`Ketupa_v0.0.3/` 是项目起源 Ketupa v0.0.3 的完整历史快照，来自原 `Shallot-2009/Ketupa_v0.0.3` 的提交 `b5f44c111fef3d32b5cdeb3c18d4af40e5c81306`。全部 111 个跟踪文件原样迁入，原始 README、LICENSE、NOTICE、作者署名及工程资料保持原始字节。此快照冻结用于查阅与研究，不作为现行产品入口。

原仓库在该基准提交中的项目整体迁入此目录：保留所有跟踪文件及其相对目录层级，包括源码、文档、资源、仿真工程、模型、输入数据和结果资料。2026-11-18 按原项目名称将归档目录由 `0.0.3/` 更名为 `Ketupa_v0.0.3/`；目录内部文件的名称、内容和 Git 文件模式均未改变。归档的 Git tree 与原项目根目录一致：`ea29d263d3a6c98b62ef9cb17c326523e5cc383b`。完整的原提交历史继续保留在主仓库中，`legacy-v0.0.3` 标签仍指向原基准提交。

- [原始项目说明](Ketupa_v0.0.3/README.md)
- [Apache-2.0 原始许可](Ketupa_v0.0.3/LICENSE)与[原始 NOTICE](Ketupa_v0.0.3/NOTICE)
- [文件来源与 SHA-256 清单](archive-manifest.json)

原 README 记载 v0.0.3 于 2025-08-14 初始发行；Git 历史最早提交为 2025-06-20。这两个日期不混同。原有研究内容及计划不直接证明现行版本功能，也不表示原代码在当前环境下已经验证可运行。

### 获取归档

```bash
git clone https://github.com/Shallot-2009/KetupaMK-AI-Fabric.git
cd KetupaMK-AI-Fabric/history/Ketupa_v0.0.3
```

若需原始根目录结构，在独立 checkout 中使用 `git switch --detach legacy-v0.0.3`。保留自己的未提交工作后再切换标签。

原 README 中的旧克隆地址、`./Ketupa/` 路径、依赖名称及脚本拼写可能不再适用。例如原依赖文件写为 `pytorch==2.2.2`，原 README 的 `Auto_desk.py` 与归档中的 `Auto_desktop.py` 不一致。归档保持记录原貌，不保证其安装命令可直接执行。涉及 Windows COM、HFSS、SI9000、MATLAB 等内容时，需自行准备兼容环境、厂商授权及工程文件的使用权。

历史源码继续受归档 LICENSE/NOTICE 约束；既有 BSD-2-Clause 授权不追溯撤销。第三方软件及工程数据不因归档而取得额外授权。现行产品请使用[主仓库下载页](../README.zh-CN.md#下载安装包)。

## English

`Ketupa_v0.0.3/` is the complete archival snapshot of the project's origin, Ketupa v0.0.3, from commit `b5f44c111fef3d32b5cdeb3c18d4af40e5c81306` in the original `Shallot-2009/Ketupa_v0.0.3` repository. All 111 tracked files are preserved byte for byte, including the original README, LICENSE, NOTICE, author credits, and engineering artifacts. This frozen snapshot is for historical reference and research.

The entire project at that baseline commit is preserved here, including every tracked file and its relative directory structure: source code, documentation, assets, simulation projects, models, input data, and results. On 2026-11-18, the archive directory was renamed from `0.0.3/` to `Ketupa_v0.0.3/` to retain the original project name. Internal filenames, contents, and Git file modes remain unchanged. The archive Git tree is identical to the original project root: `ea29d263d3a6c98b62ef9cb17c326523e5cc383b`. The complete original commit history remains in the primary repository, and `legacy-v0.0.3` still points to the original baseline commit.

The original README records an initial-release date of 2025-08-14; the earliest retained Git commit is dated 2025-06-20. They describe different events. Historical descriptions and planned work do not establish current-product functionality or compatibility with today's environment.

Clone the main repository and enter `history/Ketupa_v0.0.3` as shown above. For the original root layout, use a separate checkout at `legacy-v0.0.3`, preserving any uncommitted work before switching.

Historical clone URLs, `./Ketupa/` paths, package names, and script spellings may be obsolete. For example, the original dependency file uses `pytorch==2.2.2`, and the README names `Auto_desk.py` although the archived file is `Auto_desktop.py`. These records are intentionally unchanged; their setup commands are not asserted to run as written. Windows COM, HFSS, SI9000, MATLAB, and engineering-file rights must be supplied separately where applicable.

Original first-party source remains subject to its archived LICENSE and NOTICE; previously granted BSD-2-Clause rights are not retroactively withdrawn. Third-party software and engineering artifacts retain their separate rights. Use the [current product downloads](../README.md#downloads) for present distributions.
