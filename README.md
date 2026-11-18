# KetupaMK-AI-Fabric

[English](README.md) · [简体中文](README.zh-CN.md) · [Documentation](docs/README.md) · [Releases](docs/releases/README.md) · [Tags](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/tags)

KetupaMK automates PCB, package, and interconnect modeling workflows. It uses CIR configuration files to organize engineering inputs, invoke compatible EDA tools, and produce traceable results. Version 1.0.2 also provides DDR Touchstone delay/skew reports and AI-assisted preparation of network data.

This is the public distribution and documentation repository for KetupaMK. Current proprietary core source is maintained separately. Windows and Linux installers, runtime distributions, test entitlement files, and third-party materials are published here.

**Project foundation — [Ketupa_v0.0.3](history/Ketupa_v0.0.3/).** The complete original project is preserved as the foundation of this work: 111 tracked files, original directory structure, author credits, LICENSE, NOTICE, and engineering artifacts. Its Git history and [`legacy-v0.0.3`](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/tree/legacy-v0.0.3) tag remain intact. [Read the origin record](history/ORIGIN.md).

The project began in **2023**, and the maintainer confirms early project commits in **May–June 2024**. The earliest Git evidence currently retained here is dated 2025-06-20; that date is not the project beginning. See the [project timeline](history/ORIGIN.md) for dates and source labels.

## What it does

| Area | Published scope in 1.0.2 |
| --- | --- |
| CIR workflow control | One entry point, project includes, project queues, and network workers for existing PKG, PCB, and Merge workflows |
| Package/interconnect setup | Bump, solderball, chip orientation, port impedance, mixed-unit frequency sweeps, and traceable output naming |
| DDR reporting | `.tap` reads Touchstone files, explicit port maps, and specifications to report S21 delay and relative skew to Excel |
| AI integration | Network inventory, classification mapping, Excel preprocessing, and optional Skill/Agent/MCP integration |
| Interfaces | Windows Launcher, Linux CLI, and authenticated local HTTPS interfaces with a frontend SDK |
| GDS Interposer | Import assistance; the published scope does not include solving or electrical signoff |

Compatible EDA software, vendor licenses, approved engineering inputs, and a version-appropriate KetupaMK entitlement are required for the workflows that use them. See [product scope](docs/product/README.md) for the version-specific boundaries.

<a id="downloads"></a>
<a id="downloads-en"></a>

## Download

**Current preview: KetupaMK 1.0.2** — [Windows EXE](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.2/openketupa-ai-fabric-1.0.2-Windows-x64-Setup.exe) · [Linux TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.2/openketupa-ai-fabric-linux-1.0.2-x64.tar.gz) · [Linux DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.2/openketupa-ai-fabric-linux_1.0.2_amd64.deb)

These links download the installer directly. For the standard Linux build, choose TAR.GZ or DEB; see the compatibility build below for Rocky/RHEL 8, Ubuntu 20.04 and similar environments. Version 1.0.2 remains a pre-release; choose and validate a version for your intended workflow.

| Distribution | Status | Windows x64 | Linux x64 | Linux amd64 |
| --- | --- | --- | --- | --- |
| [KetupaMK 1.0.2](docs/releases/openketupamk-v1.0.2.md) | Pre-release | [EXE](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.2/openketupa-ai-fabric-1.0.2-Windows-x64-Setup.exe) | [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.2/openketupa-ai-fabric-linux-1.0.2-x64.tar.gz) | [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.2/openketupa-ai-fabric-linux_1.0.2_amd64.deb) |
| [KetupaMK 1.0.1](docs/releases/openketupamk-v1.0.1.md) | Pre-release | [EXE](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.1/Ketupa-AI-Fabric-1.0.1-Windows-x64-Setup.exe) | [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.1/ketupa-ai-fabric-linux-1.0.1-x64.tar.gz) | [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.1/ketupa-ai-fabric-linux_1.0.1_amd64.deb) |
| [KetupaMK 1.0.0](docs/releases/openketupamk-v1.0.0.md) | Historical release | [EXE](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.0/openketupa-1.0.0-Windows-x64-Setup.exe) | [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.0/openketupa-1.0.0-Linux-x64.tar.gz) | [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.0/openketupa-1.0.0-linux-amd64.deb) |
| [Runtime 1.0.0](docs/releases/openketupamk-runtime-v1.0.0.md) | Historical release | [EXE](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-runtime-v1.0.0/ketupa-runtime-1.0.0-Windows-x64-Setup.exe) | [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-runtime-v1.0.0/ketupa-runtime-1.0.0-Linux-x64.tar.gz) | [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-runtime-v1.0.0/ketupa-runtime-installer_1.0.0_amd64.deb) |
| [Beta](docs/releases/openketupamk-beta.md) | Pre-release | [EXE](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-beta/openketupa-Beta-Windows-x64-Setup.exe) | [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-beta/openketupa-Beta-linux-x64.tar.gz) | [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-beta/openketupa-Beta-linux-amd64.deb) |

<a id="legacy-linux"></a>

### Legacy Linux environments · 1.0.2

For older userspaces such as Rocky/RHEL 8 and Ubuntu 20.04: **x86_64, glibc ≥ 2.28**. Choose one of four Linux application/runtime installer formats.

| Target / installation method | Direct download |
| --- | --- |
| Rocky / RHEL 8 | [RPM](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-kernel-legacy-v1.0.2/ketupa-ai-fabric-kernel-legacy-1.0.2-1.x86_64.rpm) |
| Ubuntu 20.04 / Debian | [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-kernel-legacy-v1.0.2/ketupa-ai-fabric-kernel-legacy_1.0.2_amd64.deb) |
| Self-extracting installation | [RUN](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-kernel-legacy-v1.0.2/ketupa-ai-fabric-kernel-legacy-1.0.2-x64.run) |
| Dedicated-prefix installation | [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-kernel-legacy-v1.0.2/ketupa-ai-fabric-kernel-legacy-1.0.2-x64.tar.gz) |

[Compatibility notes and tested scope](docs/releases/openketupamk-kernel-legacy-v1.0.2.md) · [Release](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/tag/openketupamk-kernel-legacy-v1.0.2) · [Tags](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/tags)

This distribution remains a pre-release. Recorded acceptance covers isolated EL8.1 and Ubuntu 20.04 userspaces, not native Rocky kernels or EDA solving. Keep compatibility and standard payloads out of the same installation prefix.

[Installation guide](docs/installation/README.md) · [Download SHA256SUMS](https://raw.githubusercontent.com/Shallot-2009/KetupaMK-AI-Fabric/main/SHA256SUMS) · [Release notes](docs/releases/README.md)

Runtime 1.0.0 is a separate distribution. Original installer names, bytes, and release status are retained. GitHub's **Source code** ZIP/TAR files contain repository snapshots; product installers are the EXE, DEB, RPM, RUN, and TAR.GZ assets listed above.

<a id="licenses"></a>
<a id="licenses-en"></a>

## Test entitlements and software terms

Maintainer-published test files: [offline test LIC](https://raw.githubusercontent.com/Shallot-2009/KetupaMK-AI-Fabric/main/licenses/Ketupa-ketupamk_offline_test_12w-20261116-232329-233.lic) · [internal-test LIC](https://raw.githubusercontent.com/Shallot-2009/KetupaMK-AI-Fabric/main/licenses/openketupamk-internal-test-12w.lic) · [instructions and checksums](licenses/README.md).

The `.lic` files are software entitlements, distinct from copyright licenses. Their version, module, device, and validity restrictions follow the original files and software validation; download does not renew them or grant commercial use.

| Material | Terms |
| --- | --- |
| Original first-party v0.0.3 source | [Archived Apache-2.0 LICENSE](history/Ketupa_v0.0.3/LICENSE) and [NOTICE](history/Ketupa_v0.0.3/NOTICE); earlier BSD-2-Clause grants remain effective |
| Current proprietary product | [LICENSE.txt](LICENSE.txt), [EULA.md](EULA.md#english), and applicable valid written agreements |
| Third-party components and engineering materials | Their separate terms, notices, and source obligations; see [third-party materials](third-party/README.md) |

Read the [license scope](LICENSE.md) and [commercial delivery review](docs/governance/REVIEW.md). The repository is not offered under one blanket open-source license.

## Repository map

```text
KetupaMK-AI-Fabric/
├── docs/          Product, installation, release notes, governance, provenance
├── history/       Ketupa_v0.0.3 foundation, origin record, preservation manifest
├── licenses/      Public test LIC files, instructions, checksums
├── releases/      Installer manifest and immutable tag map
├── third-party/   Component notices and corresponding source archives
├── tools/         Repository integrity checks
└── .github/       Automated checks and issue/PR templates
```

`main` is the current documentation and distribution index. Tags preserve specific historical snapshots: `legacy-v0.0.3` for the original project, `openketupamk-v*` for product releases, `openketupamk-runtime-v*` for Runtime, and `openketupamk-kernel-legacy-v*` for legacy Linux environments. A tag is a fixed reference, not a branch. [Branch and release policy](docs/governance/README.md).

## Documentation and contact

[Documentation index](docs/README.md) · [Project foundation](history/README.md) · [Migration record](docs/MIGRATION.md) · [Security reporting](SECURITY.md)

Current public author attribution: **Asenjo HB**. The foundational project's original attribution **Asenjo.HB.L.** is retained. The original GitHub repository continues under this name, retaining its repository identity, stars, forks, and issues.

For licensing, rights, and private security reports: [asenjoaupa@gmail.com](mailto:asenjoaupa@gmail.com) · [3405802009@qq.com](mailto:3405802009@qq.com). Public issues are for reproducible product and documentation reports; remove customer data and private entitlements before posting.
