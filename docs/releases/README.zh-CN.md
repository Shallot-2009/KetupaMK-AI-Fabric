# 发行说明

简体中文 · [English](README.md) · [项目主页](../../README.zh-CN.md) · [文档](../README.zh-CN.md)

在下表选择发行组。**1.0.2 是当前预览版**，未被提升为生产正式版；原有预发布标记继续保留。

| 发行版本 | 状态 | Windows x64 | Linux x64 | Linux amd64 |
| --- | --- | --- | --- | --- |
| [KetupaMK 1.0.2](openketupamk-v1.0.2.zh-CN.md) | 预发布 | [EXE](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.2/openketupa-ai-fabric-1.0.2-Windows-x64-Setup.exe) | [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.2/openketupa-ai-fabric-linux-1.0.2-x64.tar.gz) | [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.2/openketupa-ai-fabric-linux_1.0.2_amd64.deb) |
| [KetupaMK 1.0.1](openketupamk-v1.0.1.zh-CN.md) | 预发布 | [EXE](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.1/Ketupa-AI-Fabric-1.0.1-Windows-x64-Setup.exe) | [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.1/ketupa-ai-fabric-linux-1.0.1-x64.tar.gz) | [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.1/ketupa-ai-fabric-linux_1.0.1_amd64.deb) |
| [KetupaMK 1.0.0](openketupamk-v1.0.0.zh-CN.md) | 历史正式发行 | [EXE](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.0/openketupa-1.0.0-Windows-x64-Setup.exe) | [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.0/openketupa-1.0.0-Linux-x64.tar.gz) | [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.0/openketupa-1.0.0-linux-amd64.deb) |
| [Runtime 1.0.0](openketupamk-runtime-v1.0.0.zh-CN.md) | 历史正式发行 | [EXE](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-runtime-v1.0.0/ketupa-runtime-1.0.0-Windows-x64-Setup.exe) | [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-runtime-v1.0.0/ketupa-runtime-1.0.0-Linux-x64.tar.gz) | [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-runtime-v1.0.0/ketupa-runtime-installer_1.0.0_amd64.deb) |
| [Beta](openketupamk-beta.zh-CN.md) | 预发布 | [EXE](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-beta/openketupa-Beta-Windows-x64-Setup.exe) | [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-beta/openketupa-Beta-linux-x64.tar.gz) | [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-beta/openketupa-Beta-linux-amd64.deb) |

当前有 5 个公开发行组、15 个安装包。Runtime 1.0.0 与产品 1.0.0 为独立发行组，安装包名称和字节保持原样。选择适合平台的安装包后，参阅[安装说明](../installation/README.zh-CN.md)，并用 [SHA256SUMS](../../SHA256SUMS) 核对。

| 引用 | 含义 |
| --- | --- |
| `main` | 当前文档、下载导航与保全记录 |
| `openketupamk-v*` | 产品发行快照 |
| `openketupamk-runtime-v*` | Runtime 快照 |
| `openketupamk-beta` | 保留的历史 Beta 快照 |
| `legacy-v0.0.3` | 保留原始根目录布局的基础项目 |

[标签映射](../../releases/tag-map.json)记录准确提交。部分历史发行标签共用一个文档提交，其安装包附件仍为不同发行组。既有标签继续指向原提交，不因当前 `main` 目录变化而重新指向。详见[发布规范](../governance/README.zh-CN.md)。

GitHub 自动生成的 Source code 归档包含标签对应的仓库快照，不包含受保护的产品安装器。[发行清单](../../releases/manifest.json)记录原始发布时间；GitHub 上迁移后的发布时间反映后续迁移。
