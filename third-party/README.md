# Third-party notices and source

[简体中文](README.zh-CN.md) · English · [Home](../README.md) · [Documentation](../docs/README.md)

Third-party components retain their own licenses. These materials provide the notices and source archives previously identified for published distributions. They are separate from proprietary KetupaMK core source and are not product installers.

## Corresponding source records

| Component | Identified product versions | Direct source download | Origin |
| --- | --- | --- | --- |
| 7-Zip 26.04 | 1.0.1 | [7z2604-src.tar.xz](https://raw.githubusercontent.com/Shallot-2009/KetupaMK-AI-Fabric/main/third-party/sources/7z2604-src.tar.xz) | [Upstream](https://github.com/ip7z/7zip/releases/download/26.04/7z2604-src.tar.xz) |
| CentOS GCC 4.8.5-44.el7 / libquadmath | 1.0.1, Beta | [gcc-4.8.5-44.el7.src.rpm](https://raw.githubusercontent.com/Shallot-2009/KetupaMK-AI-Fabric/main/third-party/sources/gcc-4.8.5-44.el7.src.rpm) | [Upstream](https://archive.kernel.org/centos-vault/7.9.2009/os/Source/SPackages/gcc-4.8.5-44.el7.src.rpm) |
| AlmaLinux GCC 8.5.0-26.el8_10.alma.1 / libquadmath | 1.0.1 | [gcc-8.5.0-26.el8_10.alma.1.src.rpm](https://raw.githubusercontent.com/Shallot-2009/KetupaMK-AI-Fabric/main/third-party/sources/gcc-8.5.0-26.el8_10.alma.1.src.rpm) | [Upstream](https://vault.almalinux.org/8.10/BaseOS/Source/Packages/gcc-8.5.0-26.el8_10.alma.1.src.rpm) |
| FFmpeg 5.1.6 | Beta | [ffmpeg-5.1.6.tar.xz](https://raw.githubusercontent.com/Shallot-2009/KetupaMK-AI-Fabric/main/third-party/sources/ffmpeg-5.1.6.tar.xz) | [Upstream](https://ffmpeg.org/releases/ffmpeg-5.1.6.tar.xz) |
| OpenCV Python 4.11.0.86 build materials | Beta | [opencv-python-headless-4.11.0.86.tar.gz](https://raw.githubusercontent.com/Shallot-2009/KetupaMK-AI-Fabric/main/third-party/sources/opencv-python-headless-4.11.0.86.tar.gz) | [Upstream](https://pypi.org/project/opencv-python-headless/4.11.0.86/) |


Each source link downloads the archive directly. GCC source RPMs include distribution patches and build specifications. The [original component record](../docs/provenance/third-party-README.before-review.md) retains the earlier inspection notes. Version mappings here reflect that record, not a newly completed inventory of every installer.

## Notices

- [7zip-LGPL-2.1.txt](licenses/7zip-LGPL-2.1.txt)
- [7zip-License.txt](licenses/7zip-License.txt)
- [7zip-unRAR-License.txt](licenses/7zip-unRAR-License.txt)
- [FFmpeg-LGPL-2.1.txt](licenses/FFmpeg-LGPL-2.1.txt)
- [OpenCV-Python-4.11.0.86-Third-Party.txt](licenses/OpenCV-Python-4.11.0.86-Third-Party.txt)
- [OpenCV-Python-Packaging-License.txt](licenses/OpenCV-Python-Packaging-License.txt)
- [SciPy-1.17.1-Third-Party.txt](licenses/SciPy-1.17.1-Third-Party.txt)

Keep notices and source-access rights intact when redistributing or modifying covered components. The first-party EULA does not override independent LGPL/GPL or other component rights, including applicable replacement and debugging rights.

## Coverage and delivery

The two historical 1.0.0 distributions contain encrypted payloads that were not fully decoded in the earlier review. A complete package-level dependency inventory and license/source coverage for every distribution, including 1.0.2, have not been established by these records. Do not treat this directory as a complete SBOM or a full compliance certification.

Commercial delivery needs a version-specific component inventory, applicable license texts, exact corresponding source and build/relink materials where required, and distribution evidence. See the [delivery review](../docs/governance/REVIEW.md). Report missing material privately to [asenjoaupa@gmail.com](mailto:asenjoaupa@gmail.com).

## Verify published material

[manifest.json](manifest.json) records sizes and SHA-256 values for all twelve published source/notice files. From a clone containing these materials:

```bash
cd third-party
sha256sum -c SHA256SUMS
```

Installer assets remain on Releases; source archives stay accessible in this repository. Original source and legal-file bytes have been preserved.
