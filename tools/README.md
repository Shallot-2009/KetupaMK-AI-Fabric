# Repository checks

[简体中文](README.zh-CN.md) · English · [Home](../README.md) · [Documentation](../docs/README.md)

From a full Git checkout with its original history and tags, run:

```bash
python3 tools/check_repository.py
```

The checker uses the Python standard library. It verifies the complete 111-file foundation, 17 preserved distribution records, two public entitlements, installer/tag metadata, third-party hashes, language pairs, links/anchors, and known secret patterns. It does not execute archived code, installers, licensing operations, or EDA workflows.

GitHub Actions runs the same command. A shallow clone must fetch the original history and tags before validation. Changes to published artifact baselines require explicit review; editing a manifest alone must not redefine the preserved foundation.
