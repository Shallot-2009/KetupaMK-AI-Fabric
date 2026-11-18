# Installation and environment

[中文](INSTALLATION.zh-CN.md) · [Downloads](../README.md#downloads)

## Choose a distribution

Select one of the five release groups. Standard 1.0.0 and Runtime 1.0.0 are different distributions, not interchangeable filenames. Version 1.0.2, 1.0.1, and Beta retain their original pre-release status. Each group offers one Windows x64 EXE and two alternative Linux formats. Exact filenames, sizes, digests, and URLs are in the [release manifest](../releases/manifest.json).

Download only the asset for your platform, then compare it against [SHA256SUMS](../SHA256SUMS). On Linux, download that checksum file into the same directory and run:

```bash
sha256sum --ignore-missing -c SHA256SUMS
```

On Windows PowerShell, compare the selected installer's digest with its line in SHA256SUMS:

```powershell
Get-FileHash -Algorithm SHA256 .\your-selected-installer.exe
```

Replace the example filename with the exact downloaded filename. Checksums establish file consistency with the migrated release, not trust in every dependency or successful execution.

## Windows x64

Run the selected EXE and follow its installer instructions. The 1.0.2 release documents a Windows Launcher. Configure the external engineering tools and the applicable KetupaMK license according to that version's instructions. Renaming the GitHub repository does not rename or rebuild installed products.

## Linux x64 / amd64

Choose one format:

- DEB: on a compatible Debian/Ubuntu system, install the exact local file with `sudo apt install ./your-selected-package.deb`, reviewing the requested dependency changes.
- TAR.GZ: extract the selected archive with `tar -xzf your-selected-package.tar.gz`, read its bundled installation instructions, and use that package's documented launcher or command. Do not infer a common internal folder layout across versions.

The 1.0.2 release describes Linux as a CLI distribution without the Windows Launcher. On a configured 1.0.2 installation, read-only checks include `ketupa --version`, `ketupa license status`, and `ketupa license-service status`. Follow the [1.0.2 release notes](releases/openketupamk-v1.0.2.md) for the published CIR workflow scope.

## Runtime, vendor tools, and inputs

The installers/runtime distributions and all previously published third-party source and notice materials are hosted in this repository and its Releases. No private first-party development environment or core source is added. Packaging a runtime does not include separate commercial EDA entitlements or assert compatibility with an unspecified vendor version.

Prepare the compatible Ansys/Cadence or other tools required by your selected workflow, the corresponding vendor licenses, approved engineering input files, and a valid version-appropriate KetupaMK license. The existing [internal-test license](../licenses/README.md#internal-test) is preserved, not renewed; its signed validity and module entitlements govern its use.

The v0.0.3 source snapshot has a separate historical dependency record. Follow the [archive guide](../history/README.md); do not apply its old requirements file to the current proprietary product.

This migration verifies archive preservation, license-file retention, release attachment sizes and SHA-256 digests, and repository links. It does not execute installers, activate licenses, run EDA modeling/solving, or establish engineering signoff.
