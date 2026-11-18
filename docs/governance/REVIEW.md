# Repository review and commercial delivery

[简体中文](REVIEW.zh-CN.md) · English · [Home](../../README.md) · [Documentation](../README.md)

Review date: **2026-11-18**. This review covers the public repository, publication records, and artifact consistency. Current proprietary core source and customers' installations are outside the repository reviewed here.

## Repository evidence

| Area | Evidence maintained here |
| --- | --- |
| Foundational project | All 111 tracked files match the original blobs, sizes, SHA-256 values, relative paths, and file modes; original Git tree and `legacy-v0.0.3` target retained |
| Distribution source records | Seventeen original files retain their bytes, including EULA, proprietary notice, test entitlement, and third-party records; relocated originals are mapped in the provenance manifest |
| Public installers | Five release groups, fifteen assets, 4,207,538,269 bytes; manifest values checked against GitHub asset names, sizes, digests, and direct download endpoints |
| Public test LIC | Two maintainer-designated files; bytes and SHA-256 verified, with consolidated English/Chinese instructions and direct downloads |
| Documentation | Paired language navigation, local links and anchors, release/download metadata, and repository directory checks |
| Source and legal preservation | Original EULA/notice/third-party legal texts retained, separate historical and proprietary scopes documented |
| Secret exposure checks | Known private-key and token patterns checked without printing their contents; GitHub secret scanning and push protection are enabled. These checks are not an exhaustive security audit |
| Automation | Standard-library repository validator and GitHub Actions workflow; main and published-tag safeguards are documented in the policy |

Run `python3 tools/check_repository.py` to repeat the local preservation and documentation checks. Package hashes and repository checks do not establish successful installation, signature authenticity, solver correctness, or engineering signoff.

## Requirements before commercial delivery

| Item | Existing basis | Evidence still needed for the delivery |
| --- | --- | --- |
| Legal identity and ownership | Public author attribution, publishing identifier, and preserved legal texts | Verify the legal licensor's identity, ownership/third-party authority, and contracting entity; a nickname or domain is insufficient |
| Entitlement scope | Versioned product licensing and designated public test files | Confirm the delivered version's modules, duration, users/devices/concurrency, commercial rights, and verifiable issuance/acceptance records |
| Contract acceptance | Bilingual EULA revision `2026-10-19-r2` | Evidence that the actual installer/activation/contract process obtains and retains lawful acceptance of the applicable revision |
| Dependencies and source | Identified source/notice archives and prior inspection records | A complete per-installer SBOM, exact corresponding source and required build/relink materials; encrypted 1.0.0 payloads and full 1.0.2 coverage are not resolved by repository organization |
| Privacy and external models | Product descriptions include licensing and optional AI/network interfaces | Actual data-flow inventory, destinations, telemetry/activation behavior, privacy notice, customer authority, retention, and contractual controls appropriate to deployment |
| Platform and engineering validation | Published workflow entry points and preserved binaries | Installation, update/uninstall, compatibility, representative workflow tests, known limitations, and independent validation of engineering results |
| Supply-chain provenance | Asset digests and original records | Reproducible build/provenance evidence where applicable, actual code-signing identity and verification, and a vulnerability response process |
| Commercial operations | Private contact channels and written-agreement precedence | Agreed support lifecycle, delivery/acceptance criteria, payment/refund terms where applicable, and any jurisdiction-specific obligations |

These are specific delivery requirements, not claims that contracts, privacy mechanisms, certification, or legal review have already been completed. Preserve the evidence for the actual version and transaction rather than relying on a general README statement.

## References used for organization

Repository patterns were reviewed from [VS Code](https://github.com/microsoft/vscode), [PowerToys](https://github.com/microsoft/PowerToys), and [Ollama](https://github.com/ollama/ollama). The resulting layout is adapted to a distribution repository with a protected foundation and mixed legal scopes, rather than presented as a current open-source core-code repository.
