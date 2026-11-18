# KetupaMK-AI-Fabric

[简体中文](README.zh-CN.md) · English · [Project history](history/README.md) · [Releases](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases)

The continuing Ketupa project: the complete original **Ketupa_v0.0.3** project is preserved in [`history/Ketupa_v0.0.3/`](history/Ketupa_v0.0.3/), including its source code, documentation, assets, and engineering files, while the current **KetupaMK** installers, runtime distributions, licensing materials, and required third-party sources are maintained here.

This is the original `Shallot-2009/Ketupa_v0.0.3` repository renamed to `KetupaMK-AI-Fabric`, with repository identity, stars, fork relationships, and existing issues retained. The former `Ketupa-AI-Fabric` distribution repository has been integrated into this repository. Its one star is not transferred or added to the original repository's stars. See the [migration record](docs/MIGRATION.md).

## Downloads

**Five release groups, fifteen installers.** Runtime 1.0.0 and standard 1.0.0 are separate distributions. Installer names and bytes are preserved, including historical `OpenKetupa` and `Ketupa-AI-Fabric` naming. The release status labels below match the source releases.

| Version / 版本 | Status / 状态 | Windows x64 | Linux x64 | Linux amd64 |
| --- | --- | --- | --- | --- |
| [KetupaMK 1.0.2](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/tag/openketupamk-v1.0.2) | Pre-release / 预发布 | [EXE](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.2/openketupa-ai-fabric-1.0.2-Windows-x64-Setup.exe) | [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.2/openketupa-ai-fabric-linux-1.0.2-x64.tar.gz) | [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.2/openketupa-ai-fabric-linux_1.0.2_amd64.deb) |
| [KetupaMK 1.0.1](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/tag/openketupamk-v1.0.1) | Pre-release / 预发布 | [EXE](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.1/Ketupa-AI-Fabric-1.0.1-Windows-x64-Setup.exe) | [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.1/ketupa-ai-fabric-linux-1.0.1-x64.tar.gz) | [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.1/ketupa-ai-fabric-linux_1.0.1_amd64.deb) |
| [KetupaMK 1.0.0](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/tag/openketupamk-v1.0.0) | Release / 正式发布 | [EXE](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.0/openketupa-1.0.0-Windows-x64-Setup.exe) | [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.0/openketupa-1.0.0-Linux-x64.tar.gz) | [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.0/openketupa-1.0.0-linux-amd64.deb) |
| [KetupaMK Runtime 1.0.0](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/tag/openketupamk-runtime-v1.0.0) | Release / 正式发布 | [EXE](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-runtime-v1.0.0/ketupa-runtime-1.0.0-Windows-x64-Setup.exe) | [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-runtime-v1.0.0/ketupa-runtime-1.0.0-Linux-x64.tar.gz) | [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-runtime-v1.0.0/ketupa-runtime-installer_1.0.0_amd64.deb) |
| [KetupaMK Beta](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/tag/openketupamk-beta) | Pre-release / 预发布 | [EXE](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-beta/openketupa-Beta-Windows-x64-Setup.exe) | [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-beta/openketupa-Beta-linux-x64.tar.gz) | [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-beta/openketupa-Beta-linux-amd64.deb) |

Choose either TAR.GZ or DEB on Linux. Installers are attached to this repository's Releases, rather than duplicated in the Git working tree. GitHub-generated Source code ZIP/TAR files are repository snapshots; they are not product installers.

Use [SHA256SUMS](SHA256SUMS) to verify downloads. The [release manifest](releases/manifest.json) records original publication dates, exact filenames, byte sizes, SHA-256 digests, and current download URLs. The three 1.0.2 digests in the previous repository's README were stale; the current values match the actual release assets. An unchanged copy of that README is retained as a [provenance record](docs/provenance/Ketupa-AI-Fabric-README.before-migration.md).

## Installation and engineering environment

Follow the [English installation guide](docs/INSTALLATION.en.md) or [中文安装说明](docs/INSTALLATION.zh-CN.md), and the notes for your chosen version. Version 1.0.2 remains a **pre-release**. Its published capabilities include licensed CIR workflow entry points, AI preprocessing/integration materials, Windows Launcher, Linux CLI, and an import-only GDS Interposer workflow. Refer to the [1.0.2 release notes](docs/releases/openketupamk-v1.0.2.md) for exact scope and limitations.

Installers provide the version's packaged software/runtime; they do not grant Ansys, Cadence, MATLAB, Polar, or other vendor entitlements. Compatible external EDA tools, approved input data, and the applicable KetupaMK license remain necessary. This repository migration verifies preservation and download integrity; it does not establish successful installation, physical simulation acceptance, or engineering signoff.

The existing author-published [internal-test license and instructions](licenses/internal-test/README.md) are retained unchanged. Its signed scope, version applicability, and validity govern its use; migration does not renew or broaden it.

The maintainer-published [offline test LIC](licenses/offline-test/README.md) is also available. See the [license index](licenses/README.md) for both files and their scope.

## Origins and archive

Ketupa v0.0.3 is the origin of this project. Its original README records an initial-release date of **August 14, 2025**, the author name **Asenjo.HB.L.**, and work on HFSS patch antennas, transmission lines, measurement correlation, MATLAB/CNN exploration, LLM interaction, and desktop automation. These are historical descriptions, not acceptance claims for the current product. The retained Git history begins on **June 20, 2025**; that Git date and the release date recorded in the README describe different events.

The archive contains all **111 tracked files** from commit `b5f44c111fef3d32b5cdeb3c18d4af40e5c81306`, with their original contents, copyright statements, license, notices, and engineering artifacts. The [`legacy-v0.0.3`](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/tree/legacy-v0.0.3) tag preserves the original root layout. Both repositories' original commit histories are retained as parents of the consolidation merge.

Start with the [archive guide](history/README.md). Historical setup commands, paths, and dependency names may be outdated and are not silently rewritten. See [ORIGIN.md](history/ORIGIN.md) for the chronology and provenance inventory.

## License scopes

| Material | Applicable terms |
| --- | --- |
| Original first-party v0.0.3 source in `history/Ketupa_v0.0.3/` | [Archived Apache-2.0 LICENSE](history/Ketupa_v0.0.3/LICENSE) and [original NOTICE](history/Ketupa_v0.0.3/NOTICE); earlier BSD-2-Clause copies retain their original grants |
| Current proprietary first-party product and product materials | [LICENSE.txt](LICENSE.txt), [EULA.md](EULA.md), and any applicable valid written agreement |
| Third-party notices, source archives, and components | Their respective licenses; see [third-party/README.md](third-party/README.md) |
| Third-party engineering files, documentation, data, and generated artifacts in the archive | Any separately applicable rights; the archive's source-code license does not automatically cover them |

Read the bilingual [scope clarification](LICENSE.md) and [NOTICE](NOTICE). Public availability and the historical open-source license do not make the current proprietary product open source. The proprietary product terms do not retroactively revoke rights already granted in v0.0.3 or third-party materials. `OpenKetupa` in an original filename is a historical product identifier, not a license grant.

## Author and contact

Current public attribution: **Asenjo HB**. Historical attribution **Asenjo.HB.L.** is preserved in the v0.0.3 archive.

Email: [asenjoaupa@gmail.com](mailto:asenjoaupa@gmail.com) · [3405802009@qq.com](mailto:3405802009@qq.com)
GitHub: [Shallot-2009](https://github.com/Shallot-2009/) · [asen-tech.com](https://asen-tech.com)
