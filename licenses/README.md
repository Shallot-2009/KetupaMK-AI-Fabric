# Public test entitlements

[简体中文](README.zh-CN.md) · English · [Home](../README.md) · [Documentation](../docs/README.md)

Both LIC files are stored directly in this directory. They were designated for public testing by the maintainer; their contents are unchanged.

| File | Bytes | Direct download |
| --- | --- | --- |
| [Ketupa-ketupamk_offline_test_12w-20261116-232329-233.lic](Ketupa-ketupamk_offline_test_12w-20261116-232329-233.lic) | 4,781 | [LIC](https://raw.githubusercontent.com/Shallot-2009/KetupaMK-AI-Fabric/main/licenses/Ketupa-ketupamk_offline_test_12w-20261116-232329-233.lic) |
| [openketupamk-internal-test-12w.lic](openketupamk-internal-test-12w.lic) | 4,836 | [LIC](https://raw.githubusercontent.com/Shallot-2009/KetupaMK-AI-Fabric/main/licenses/openketupamk-internal-test-12w.lic) |

<a id="offline-test"></a>

## Offline test

`Ketupa-ketupamk_offline_test_12w-20261116-232329-233.lic` was synchronized from the maintainer-supplied `package` directory on 2026-11-18. Import or configure it through the workflow supported by the installed product version.

<a id="internal-test"></a>

## Internal test

`openketupamk-internal-test-12w.lic` is the previously published internal-test entitlement. Its [original instructions](../docs/provenance/internal-test-README.before-flattening.md) remain preserved as a source record.

## Scope and publication rules

The `.lic` files are entitlement files, separate from the repository's [copyright and contract terms](../LICENSE.md). Actual versions, modules, duration, device restrictions, and commercial rights follow the original file and effective agreements. The `12w` text is retained from the original filenames; downloading or moving a file does not start a new validity period.

Only the two designated public test files belong here. Do not upload customer/production entitlements, private signing keys, device fingerprints, API keys, or service credentials. Contact the maintainer privately for scope, compatibility, expiry, or signing questions. Publication does not issue, renew, widen, or validate an entitlement.

## Verify the files

Download [SHA256SUMS](https://raw.githubusercontent.com/Shallot-2009/KetupaMK-AI-Fabric/main/licenses/SHA256SUMS) with both LIC files and run:

```bash
sha256sum -c SHA256SUMS
```

```text
2d1c5e8ae2e09ada57ffe6aa434d8016f4c9393c3eb08fb447c022778eb60031  Ketupa-ketupamk_offline_test_12w-20261116-232329-233.lic
37ee8efa33d74c5197092a2678bda1daa0e6f074c3a04cc378873396c266db01  openketupamk-internal-test-12w.lic
```

Hash checks verify file consistency. They do not prove signature validity, activation, offline execution, or availability of every module. No third-party EDA license is included.

[File metadata](manifest.json) · [Licensing contact](mailto:asenjoaupa@gmail.com)
