# KetupaMK-AI-Fabric

[English](README.md) · [简体中文](README.zh-CN.md) · [Documentation](docs/README.md) · [Releases](docs/releases/README.md) · [Tags](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/tags)

KetupaMK is a CIR-driven engineering automation platform oriented toward **analog IC, channel algorithms, advanced packaging, Interposer, and signal/power integrity (SI/PI)**. It connects PCB/package/interconnect workflows, Touchstone channel analysis, and AI-assisted input preparation on Windows and Linux.

This is the public distribution and documentation repository for KetupaMK. Current proprietary core source is maintained separately. Windows and Linux installers, runtime distributions, test entitlement files, and third-party materials are published here.

## What it does

| Area | Available workflow |
| --- | --- |
| CIR workflow control | One entry point, project includes, project queues, and network workers for existing PKG, PCB, and Merge workflows |
| Package/interconnect setup | Bump, solderball, chip orientation, port impedance, mixed-unit frequency sweeps, and traceable output naming |
| DDR reporting | `.tap` reads Touchstone files, explicit port maps, and specifications to report S21 delay and relative skew to Excel |
| AI integration | Network inventory, classification mapping, Excel preprocessing, and optional Skill/Agent/MCP integration |
| Interfaces | Windows Launcher, Linux CLI, and authenticated local HTTPS interfaces with a frontend SDK |
| GDS Interposer | Import assistance; the published scope does not include solving or electrical signoff |

Compatible EDA software, vendor licenses, approved engineering inputs, and a version-appropriate KetupaMK entitlement are required for the workflows that use them. See [product scope](docs/product/README.md) for the version-specific boundaries.

## How to use

1. Choose a [Windows or Linux installer](#downloads) and follow the [installation guide](docs/installation/README.md). Linux 1.0.3 requires x86_64 and glibc 2.34 or later; older Linux userspaces can use the 1.0.2 compatibility build.
2. Configure a [valid entitlement](licenses/README.md) and any EDA tools required by your workflow. Check the installed version and license with `ketupa --version` and `ketupa license status`.
3. Prepare the actual project inputs, put global workflow settings in `main.cir`, and put project-specific inputs in its included module. Run `ketupa run -sh main.cir check` before executing a build or analysis. See [product scope](docs/product/README.md) for the required inputs and [project map](docs/PROJECT_MAP.md) for the document layout.

<a id="downloads"></a>
<a id="downloads-en"></a>

## Download

Choose EXE for Windows or one Linux format, DEB or TAR.GZ. For Rocky/RHEL 8 and Ubuntu 20.04, see the Legacy Linux environment below. [1.0.3 installation and checksums](docs/releases/openketupamk-v1.0.3.md)

| Distribution | Status | Windows x64 | Linux x64 | Linux amd64 |
| --- | --- | --- | --- | --- |
| [KetupaMK 1.0.3](docs/releases/openketupamk-v1.0.3.md) | Preview | [EXE](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.3/Ketupa-AI-Fabric-1.0.3-Windows-x64-Setup.exe) | [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.3/ketupa-ai-fabric-linux-1.0.3-x64.tar.gz) | [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.3/ketupa-ai-fabric-linux_1.0.3_amd64.deb) |
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

Choose one package format per installation directory. Check host dependencies and EDA compatibility before running a project.

[Installation guide](docs/installation/README.md) · [Download SHA256SUMS](https://raw.githubusercontent.com/Shallot-2009/KetupaMK-AI-Fabric/main/SHA256SUMS) · [Release notes](docs/releases/README.md)

Runtime 1.0.0 is listed as a separate distribution. Choose the installer for your system from the release assets.


<!-- legacy-mirrors:start -->
The same Legacy Linux packages are also available in the primary 1.0.2 release: [DEB](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.2/openketupa-ai-fabric-kernel-legacy_1.0.2_amd64.deb) · [TAR.GZ](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.2/openketupa-ai-fabric-kernel-legacy-1.0.2-x64.tar.gz) · [RPM](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.2/openketupa-ai-fabric-kernel-legacy-1.0.2-1.x86_64.rpm) · [RUN](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/releases/download/openketupamk-v1.0.2/openketupa-ai-fabric-kernel-legacy-1.0.2-x64.run)
<!-- legacy-mirrors:end -->

<a id="licenses"></a>
<a id="licenses-en"></a>

## Test entitlements and software terms

Available test licenses are listed below. Each link opens its GitHub file page; use **Download raw file** there to save the `.lic`.

1. [Offline test](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/blob/main/licenses/openketupamk-offline-test-12w.lic)
2. [Internal test](https://github.com/Shallot-2009/KetupaMK-AI-Fabric/blob/main/licenses/openketupamk-internal-test-12w.lic)

[Selection and activation instructions](licenses/README.md).

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

[Documentation index](docs/README.md) · [Project foundation](history/README.md) · [Security reporting](SECURITY.md)

Current public author attribution: **Asenjo HB**. The [Ketupa_v0.0.3 foundation](history/README.md) retains its original author attribution and files.

For licensing, rights, and private security reports: [asenjoaupa@gmail.com](mailto:asenjoaupa@gmail.com) · [3405802009@qq.com](mailto:3405802009@qq.com). Public issues are for reproducible product and documentation reports; remove customer data and private entitlements before posting.
