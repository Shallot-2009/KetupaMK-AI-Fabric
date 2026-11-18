# Installation

[简体中文](README.zh-CN.md) · English · [Home](../../README.md) · [Documentation](../README.md)

## Select and download

Use the [download table](../../README.md#downloads) to select a version and platform. Click EXE, TAR.GZ, or DEB to download the actual installer. Linux TAR.GZ and DEB are alternatives. Runtime 1.0.0 is a separate distribution; 1.0.2, 1.0.1, and Beta retain their pre-release status.

Download [SHA256SUMS](https://raw.githubusercontent.com/Shallot-2009/KetupaMK-AI-Fabric/main/SHA256SUMS) into the installer directory. Exact names, sizes, and digests are recorded in the [release manifest](../../releases/manifest.json).

## Verify the download

On Linux, with the downloaded installer and checksum list in the same directory:

```bash
sha256sum --ignore-missing -c SHA256SUMS
```

In Windows PowerShell:

```powershell
Get-FileHash -Algorithm SHA256 .\your-selected-installer.exe
```

Replace the example with the exact filename and compare the result with its entry in SHA256SUMS. A matching digest establishes file consistency, not code-signing identity or functional acceptance.

## Windows x64

Run the selected EXE and follow its installer. Review the [EULA](../../EULA.md#english) and configure the external tools and entitlement required by that version. Version 1.0.2 provides a Windows Launcher. A repository rename does not rename installed products or rebuild historical installers.

## Linux x64 / amd64

- DEB: on a compatible Debian/Ubuntu system, use the exact filename with `sudo apt install ./your-selected-package.deb`; review the dependencies before installation.
- TAR.GZ: extract with `tar -xzf your-selected-package.tar.gz`, then follow the instructions included in that package. Internal paths and launchers may differ by version.

Version 1.0.2 is a CLI distribution on Linux. On an installed and configured system, the documented read-only checks are:

```bash
ketupa --version
ketupa license status
ketupa license-service status
```

## Entitlements and engineering environment

The [public test LIC files](../../licenses/README.md) are supplied unchanged. Use the entitlement-import or configuration workflow documented by your installed version. Their actual signed restrictions govern use; copying a file does not activate or renew it.

Prepare the compatible Ansys/Cadence or other tools, vendor licenses, layouts, stackups/XML, connector models, and project data required by the selected workflow. [Product scope](../product/README.md) describes the published boundaries. External commercial tools are not licensed by a KetupaMK download.

GitHub Source code ZIP/TAR files and a Git clone are repository snapshots. The foundational [v0.0.3 project](../../history/README.md) has its own historical dependencies, which should not be applied to the current proprietary product.

## Report a problem

Include the product version, operating system, package filename, checksum result, minimal steps, and sanitized error text in an issue. Send private entitlements, sensitive logs, or security findings through the [private reporting channel](../../SECURITY.md).
