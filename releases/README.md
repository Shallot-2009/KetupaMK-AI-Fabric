# Release metadata

[简体中文](README.zh-CN.md) · English · [Home](../README.md) · [Documentation](../docs/README.md)

This directory holds machine-readable records, not installer binaries.

- [manifest.json](manifest.json): five public release groups, exact filenames, byte sizes, SHA-256 values, original publication times, and download URLs.
- [tag-map.json](tag-map.json): the six preserved tags and their exact commit targets.
- [Root SHA256SUMS](../SHA256SUMS): installer checksums for command-line verification.

For downloads and notes, use the [release index](../docs/releases/README.md). Product binaries are attached to GitHub Releases. The `main` branch can evolve while published tags retain their historical snapshots.
