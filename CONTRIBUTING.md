# Contributing

[简体中文](CONTRIBUTING.zh-CN.md) · English · [Home](README.md) · [Documentation](docs/README.md)

This public repository accepts product reports, documentation corrections, translation improvements, and preservation/metadata fixes. Current proprietary core development is maintained separately.

## Report a problem

Use the issue forms with the product version, platform, installer filename, expected behavior, minimal reproduction, and sanitized output. Documentation reports should identify the page and language. Use [private security reporting](SECURITY.md) for vulnerabilities, private entitlements, customer data, or licensing disputes.

## Propose a change

1. Keep the change focused and explain its reason. Update both maintained language versions and their navigation.
2. Preserve `history/Ketupa_v0.0.3/`, original legal texts, source snapshots, installer hashes, and existing tag targets. Add historical corrections outside the frozen archive.
3. Keep downloads directly linked to official release assets. Do not add installers to Git or include private credentials/entitlements.
4. Run `python3 tools/check_repository.py` and include the result in the pull request.

Submit only material you have the right to disclose and contribute. Identify third-party sources and their applicable terms. A contribution does not transfer unrelated intellectual property, grant current proprietary core access, or relicense existing historical/third-party material. Licensing questions should be agreed with the maintainer before inclusion.
