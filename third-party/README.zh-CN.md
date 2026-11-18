# 第三方声明与源码

简体中文 · [English](README.md) · [项目主页](../README.zh-CN.md) · [文档](../docs/README.zh-CN.md)

第三方组件保留各自许可。本目录提供已发布发行组中此前识别出的声明和源码归档，与 KetupaMK 专有核心源码分别处理，也不作为产品安装包。

## 对应源码记录

| 组件 | 原记录已识别的产品版本 | 直接下载源码 | 上游来源 |
| --- | --- | --- | --- |
| 7-Zip 26.04 | 1.0.1 | [7z2604-src.tar.xz](https://raw.githubusercontent.com/Shallot-2009/KetupaMK-AI-Fabric/main/third-party/sources/7z2604-src.tar.xz) | [上游](https://github.com/ip7z/7zip/releases/download/26.04/7z2604-src.tar.xz) |
| CentOS GCC 4.8.5-44.el7 / libquadmath | 1.0.1, Beta | [gcc-4.8.5-44.el7.src.rpm](https://raw.githubusercontent.com/Shallot-2009/KetupaMK-AI-Fabric/main/third-party/sources/gcc-4.8.5-44.el7.src.rpm) | [上游](https://archive.kernel.org/centos-vault/7.9.2009/os/Source/SPackages/gcc-4.8.5-44.el7.src.rpm) |
| AlmaLinux GCC 8.5.0-26.el8_10.alma.1 / libquadmath | 1.0.1 | [gcc-8.5.0-26.el8_10.alma.1.src.rpm](https://raw.githubusercontent.com/Shallot-2009/KetupaMK-AI-Fabric/main/third-party/sources/gcc-8.5.0-26.el8_10.alma.1.src.rpm) | [上游](https://vault.almalinux.org/8.10/BaseOS/Source/Packages/gcc-8.5.0-26.el8_10.alma.1.src.rpm) |
| FFmpeg 5.1.6 | Beta | [ffmpeg-5.1.6.tar.xz](https://raw.githubusercontent.com/Shallot-2009/KetupaMK-AI-Fabric/main/third-party/sources/ffmpeg-5.1.6.tar.xz) | [上游](https://ffmpeg.org/releases/ffmpeg-5.1.6.tar.xz) |
| OpenCV Python 4.11.0.86 build materials | Beta | [opencv-python-headless-4.11.0.86.tar.gz](https://raw.githubusercontent.com/Shallot-2009/KetupaMK-AI-Fabric/main/third-party/sources/opencv-python-headless-4.11.0.86.tar.gz) | [上游](https://pypi.org/project/opencv-python-headless/4.11.0.86/) |


点击源码链接直接下载归档。GCC source RPM 含相应发行版补丁与构建 spec。[原组件记录](../docs/provenance/third-party-README.before-review.md)保留此前的检查说明；本表映射依据该原记录，不表示本次已完成所有安装包的完整组件清点。

## 许可声明

- [7zip-LGPL-2.1.txt](licenses/7zip-LGPL-2.1.txt)
- [7zip-License.txt](licenses/7zip-License.txt)
- [7zip-unRAR-License.txt](licenses/7zip-unRAR-License.txt)
- [FFmpeg-LGPL-2.1.txt](licenses/FFmpeg-LGPL-2.1.txt)
- [OpenCV-Python-4.11.0.86-Third-Party.txt](licenses/OpenCV-Python-4.11.0.86-Third-Party.txt)
- [OpenCV-Python-Packaging-License.txt](licenses/OpenCV-Python-Packaging-License.txt)
- [SciPy-1.17.1-Third-Party.txt](licenses/SciPy-1.17.1-Third-Party.txt)

再分发或修改相关组件时，应保留声明与源码获取权利。第一方 EULA 不覆盖 LGPL/GPL 等组件独立许可，包括适用的替换与调试权利。

## 覆盖范围与交付要求

两个历史 1.0.0 发行组含有此前未完全解码的加密载荷。现有记录尚不能建立每个发行组、包括 1.0.2 的完整组件清单及许可/源码覆盖依据。本目录不作为完整 SBOM 或全面合规认证。

商业交付应形成逐版本组件清单，提供适用许可文本、必要的准确对应源码和构建/重链接材料，并保存分发依据。详见[交付检查](../docs/governance/REVIEW.zh-CN.md)。缺失材料请私下联系 [asenjoaupa@gmail.com](mailto:asenjoaupa@gmail.com)。

## 校验已发布材料

[manifest.json](manifest.json) 记录全部 12 个源码/声明文件的大小与 SHA-256。在包含这些材料的克隆目录中执行：

```bash
cd third-party
sha256sum -c SHA256SUMS
```

安装包附件继续位于 Releases，源码归档在本仓库直接提供。原始源码与法律文件的字节均保留。
