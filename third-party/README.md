# 第三方许可与对应源码 / Third-party notices and source

[Home / 项目主页](../README.md) · [Documentation / 文档](../docs/README.md)

点击语言标题即可在本页切换；另一语言会自动折叠。 / Select a language below; the other section collapses on this page.

<details name="readme-language">
<summary><strong>English</strong></summary>

Third-party components retain their own licenses. These materials provide the notices and source archives previously identified for published distributions. They are separate from proprietary KetupaMK core source and are not product installers.

## Corresponding source records

| Component | Identified product versions | Direct source download | Origin |
| --- | --- | --- | --- |
| 7-Zip 26.04 | 1.0.1 | [7z2604-src.tar.xz](https://raw.githubusercontent.com/Shallot-2009/KetupaMK-AI-Fabric/main/third-party/sources/7z2604-src.tar.xz) | [Upstream](https://github.com/ip7z/7zip/releases/download/26.04/7z2604-src.tar.xz) |
| CentOS GCC 4.8.5-44.el7 / libquadmath | 1.0.1, Beta | [gcc-4.8.5-44.el7.src.rpm](https://raw.githubusercontent.com/Shallot-2009/KetupaMK-AI-Fabric/main/third-party/sources/gcc-4.8.5-44.el7.src.rpm) | [Upstream](https://archive.kernel.org/centos-vault/7.9.2009/os/Source/SPackages/gcc-4.8.5-44.el7.src.rpm) |
| AlmaLinux GCC 8.5.0-26.el8_10.alma.1 / libquadmath | 1.0.1 | [gcc-8.5.0-26.el8_10.alma.1.src.rpm](https://raw.githubusercontent.com/Shallot-2009/KetupaMK-AI-Fabric/main/third-party/sources/gcc-8.5.0-26.el8_10.alma.1.src.rpm) | [Upstream](https://vault.almalinux.org/8.10/BaseOS/Source/Packages/gcc-8.5.0-26.el8_10.alma.1.src.rpm) |
| FFmpeg 5.1.6 | Beta | [ffmpeg-5.1.6.tar.xz](https://raw.githubusercontent.com/Shallot-2009/KetupaMK-AI-Fabric/main/third-party/sources/ffmpeg-5.1.6.tar.xz) | [Upstream](https://ffmpeg.org/releases/ffmpeg-5.1.6.tar.xz) |
| OpenCV Python 4.11.0.86 build materials | Beta | [opencv-python-headless-4.11.0.86.tar.gz](https://raw.githubusercontent.com/Shallot-2009/KetupaMK-AI-Fabric/main/third-party/sources/opencv-python-headless-4.11.0.86.tar.gz) | [Upstream](https://pypi.org/project/opencv-python-headless/4.11.0.86/) |


Each source link downloads the archive directly. GCC source RPMs include distribution patches and build specifications. The table identifies which versions each source archive applies to.

## Notices

- [7zip-LGPL-2.1.txt](licenses/7zip-LGPL-2.1.txt)
- [7zip-License.txt](licenses/7zip-License.txt)
- [7zip-unRAR-License.txt](licenses/7zip-unRAR-License.txt)
- [FFmpeg-LGPL-2.1.txt](licenses/FFmpeg-LGPL-2.1.txt)
- [OpenCV-Python-4.11.0.86-Third-Party.txt](licenses/OpenCV-Python-4.11.0.86-Third-Party.txt)
- [OpenCV-Python-Packaging-License.txt](licenses/OpenCV-Python-Packaging-License.txt)
- [SciPy-1.17.1-Third-Party.txt](licenses/SciPy-1.17.1-Third-Party.txt)

Keep notices and source-access rights intact when redistributing or modifying covered components. The first-party EULA does not override independent LGPL/GPL or other component rights, including applicable replacement and debugging rights.

## Legacy Linux 1.0.2 inventory

The [compatibility distribution](../docs/releases/openketupamk-kernel-legacy-v1.0.2.md) includes a runtime inventory, dependency licenses, and 7-Zip notices. Consult these materials for the contents of your selected installer.

## Coverage and delivery

The material below covers the components identified in this repository. For release-specific component inventories and notices, also consult the documentation supplied with your installer.

Commercial delivery needs a version-specific component inventory, applicable license texts, exact corresponding source and build/relink materials where required, and distribution evidence. See the [delivery review](../docs/governance/REVIEW.md). Report missing material privately to [asenjoaupa@gmail.com](mailto:asenjoaupa@gmail.com).

## Verify published material

[manifest.json](manifest.json) records sizes and SHA-256 values for all twelve published source/notice files. From a clone containing these materials:

```bash
cd third-party
sha256sum -c SHA256SUMS
```

Installer assets remain on Releases; source archives stay accessible in this repository. Original source and legal-file bytes have been preserved.

</details>

<details name="readme-language" open>
<summary><strong>简体中文</strong></summary>

第三方组件保留各自许可。本目录提供已发布发行组中此前识别出的声明和源码归档，与 KetupaMK 专有核心源码分别处理，也不作为产品安装包。

## 对应源码记录

| 组件 | 原记录已识别的产品版本 | 直接下载源码 | 上游来源 |
| --- | --- | --- | --- |
| 7-Zip 26.04 | 1.0.1 | [7z2604-src.tar.xz](https://raw.githubusercontent.com/Shallot-2009/KetupaMK-AI-Fabric/main/third-party/sources/7z2604-src.tar.xz) | [上游](https://github.com/ip7z/7zip/releases/download/26.04/7z2604-src.tar.xz) |
| CentOS GCC 4.8.5-44.el7 / libquadmath | 1.0.1, Beta | [gcc-4.8.5-44.el7.src.rpm](https://raw.githubusercontent.com/Shallot-2009/KetupaMK-AI-Fabric/main/third-party/sources/gcc-4.8.5-44.el7.src.rpm) | [上游](https://archive.kernel.org/centos-vault/7.9.2009/os/Source/SPackages/gcc-4.8.5-44.el7.src.rpm) |
| AlmaLinux GCC 8.5.0-26.el8_10.alma.1 / libquadmath | 1.0.1 | [gcc-8.5.0-26.el8_10.alma.1.src.rpm](https://raw.githubusercontent.com/Shallot-2009/KetupaMK-AI-Fabric/main/third-party/sources/gcc-8.5.0-26.el8_10.alma.1.src.rpm) | [上游](https://vault.almalinux.org/8.10/BaseOS/Source/Packages/gcc-8.5.0-26.el8_10.alma.1.src.rpm) |
| FFmpeg 5.1.6 | Beta | [ffmpeg-5.1.6.tar.xz](https://raw.githubusercontent.com/Shallot-2009/KetupaMK-AI-Fabric/main/third-party/sources/ffmpeg-5.1.6.tar.xz) | [上游](https://ffmpeg.org/releases/ffmpeg-5.1.6.tar.xz) |
| OpenCV Python 4.11.0.86 build materials | Beta | [opencv-python-headless-4.11.0.86.tar.gz](https://raw.githubusercontent.com/Shallot-2009/KetupaMK-AI-Fabric/main/third-party/sources/opencv-python-headless-4.11.0.86.tar.gz) | [上游](https://pypi.org/project/opencv-python-headless/4.11.0.86/) |


点击链接直接下载源码归档。GCC source RPM 含相应发行版补丁与构建 spec。表中列明源码归档适用的版本。

## 许可声明

- [7zip-LGPL-2.1.txt](licenses/7zip-LGPL-2.1.txt)
- [7zip-License.txt](licenses/7zip-License.txt)
- [7zip-unRAR-License.txt](licenses/7zip-unRAR-License.txt)
- [FFmpeg-LGPL-2.1.txt](licenses/FFmpeg-LGPL-2.1.txt)
- [OpenCV-Python-4.11.0.86-Third-Party.txt](licenses/OpenCV-Python-4.11.0.86-Third-Party.txt)
- [OpenCV-Python-Packaging-License.txt](licenses/OpenCV-Python-Packaging-License.txt)
- [SciPy-1.17.1-Third-Party.txt](licenses/SciPy-1.17.1-Third-Party.txt)

再分发或修改相关组件时，应保留声明与源码获取权利。第一方 EULA 不覆盖 LGPL/GPL 等组件独立许可，包括适用的替换与调试权利。

## 旧版 Linux 1.0.2 组件记录

[兼容发行组](../docs/releases/openketupamk-kernel-legacy-v1.0.2.md)附带运行环境组件清单、依赖许可和 7-Zip 声明。具体内容以所选安装包随附的材料为准。

## 覆盖范围与交付要求

本页覆盖仓库列明的组件。对应发行版的组件清单和许可声明，请同时查阅所选安装包内的文档。

商业交付应形成逐版本组件清单，提供适用许可文本、必要的准确对应源码和构建/重链接材料，并保存分发依据。详见[交付检查](../docs/governance/REVIEW.md)。缺失材料请私下联系 [asenjoaupa@gmail.com](mailto:asenjoaupa@gmail.com)。

## 校验已发布材料

[manifest.json](manifest.json) 记录全部 12 个源码/声明文件的大小与 SHA-256。在包含这些材料的克隆目录中执行：

```bash
cd third-party
sha256sum -c SHA256SUMS
```

安装包附件继续位于 Releases，源码归档在本仓库直接提供。原始源码与法律文件的字节均保留。

</details>
