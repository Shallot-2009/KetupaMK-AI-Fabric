#!/usr/bin/env python3
"""Check preserved project material, distribution metadata, and documentation."""

from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
FOUNDATION_COMMIT = 'b5f44c111fef3d32b5cdeb3c18d4af40e5c81306'
FOUNDATION_TREE = 'ea29d263d3a6c98b62ef9cb17c326523e5cc383b'
DISTRIBUTION_COMMIT = '67d7ffd815fea925f0fc50ece3cb8dfc53424aae'
ARCHIVE = 'history/Ketupa_v0.0.3'
REPOSITORY = 'Shallot-2009/KetupaMK-AI-Fabric'
PRESERVED_RELEASE_MANIFEST = '16807b04bf08ad0f45e9488b71ee1265669d9943e98335cae95e2fae205e7469'
ORIGINAL_TAGS = {
    'legacy-v0.0.3': FOUNDATION_COMMIT,
    'openketupamk-v1.0.2': 'c53e6494f4cec19004964d2cb7502fefc5175e09',
    'openketupamk-v1.0.1': 'fd53347e31aeca8f7babf0ff33b270fd92ae359e',
    'openketupamk-v1.0.0': 'f6e37747ba1c9a82bd66b8408ca2e162ffdb983f',
    'openketupamk-runtime-v1.0.0': 'f6e37747ba1c9a82bd66b8408ca2e162ffdb983f',
    'openketupamk-beta': 'f6e37747ba1c9a82bd66b8408ca2e162ffdb983f',
}
FROZEN_MARKDOWN = {
    'docs/provenance/Ketupa-AI-Fabric-README.before-migration.md',
    'docs/provenance/internal-test-README.before-flattening.md',
    'docs/provenance/third-party-README.before-review.md',
}
PUBLIC_LIC = {
    'Ketupa-ketupamk_offline_test_12w-20261116-232329-233.lic':
        '2d1c5e8ae2e09ada57ffe6aa434d8016f4c9393c3eb08fb447c022778eb60031',
    'openketupamk-internal-test-12w.lic':
        '37ee8efa33d74c5197092a2678bda1daa0e6f074c3a04cc378873396c266db01',
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


def read_json(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8'))


def blob_id(data):
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()


def verify_file(row, key='path'):
    path = ROOT / row[key]
    require(path.is_file(), f'Missing preserved file: {row[key]}')
    data = path.read_bytes()
    require(len(data) == row['size_bytes'], f'Size changed: {row[key]}')
    require(hashlib.sha256(data).hexdigest() == row['sha256'], f'SHA-256 changed: {row[key]}')
    if 'git_blob' in row:
        require(blob_id(data) == row['git_blob'], f'Git blob changed: {row[key]}')
    if 'mode' in row and os.name != 'nt':
        mode = '100755' if path.stat().st_mode & stat.S_IXUSR else '100644'
        require(mode == row['mode'], f'File mode changed: {row[key]}')


def verify_foundation():
    manifest = read_json('history/archive-manifest.json')
    require(manifest['source_commit'] == FOUNDATION_COMMIT, 'Foundation baseline changed')
    require(manifest['original_tree'] == FOUNDATION_TREE, 'Foundation tree baseline changed')
    require(git('rev-parse', FOUNDATION_COMMIT + '^{tree}').decode().strip() == FOUNDATION_TREE,
            'Original foundation Git tree missing or changed; fetch full history')
    require(git('rev-parse', 'legacy-v0.0.3^{commit}').decode().strip() == FOUNDATION_COMMIT,
            'Foundation tag target changed')
    require(manifest['file_count'] == len(manifest['files']) == 111, 'Foundation file count changed')
    actual = {p.relative_to(ROOT / ARCHIVE).as_posix() for p in (ROOT / ARCHIVE).rglob('*') if p.is_file() or p.is_symlink()}
    require(actual == {row['original_path'] for row in manifest['files']}, 'Foundation path set changed')
    original = {}
    for record in git('ls-tree', '-rz', FOUNDATION_COMMIT).split(b'\0'):
        if record:
            meta, name = record.split(b'\t', 1)
            mode, kind, oid = meta.decode().split()
            original[name.decode()] = (mode, kind, oid)
    require(set(original) == actual, 'Archive differs from original complete project')
    for row in manifest['files']:
        require(row['archived_path'] == ARCHIVE + '/' + row['original_path'], 'Archive manifest path changed')
        require(original[row['original_path']] == (row['mode'], 'blob', row['git_blob']), 'Original blob metadata changed')
        verify_file(row, 'archived_path')
    for source in [FOUNDATION_COMMIT, DISTRIBUTION_COMMIT]:
        require(subprocess.run(['git', 'merge-base', '--is-ancestor', source, 'HEAD'], cwd=ROOT).returncode == 0,
                'Original repository history is no longer reachable: ' + source)
    return 111


def verify_distribution():
    manifest = read_json('docs/provenance/distribution-file-manifest.json')
    require(manifest['source_commit'] == DISTRIBUTION_COMMIT, 'Distribution baseline changed')
    require(manifest['unchanged_file_count'] == len(manifest['files']) == 17, 'Preservation file count changed')
    for row in manifest['files']:
        verify_file(row)
        original_path = row.get('original_path', row['path'])
        original = git('rev-parse', DISTRIBUTION_COMMIT + ':' + original_path).decode().strip()
        require(original == row['git_blob'], 'Distribution source identity changed: ' + original_path)
    source_readme = git('show', DISTRIBUTION_COMMIT + ':README.md')
    require((ROOT / 'docs/provenance/Ketupa-AI-Fabric-README.before-migration.md').read_bytes() == source_readme,
            'Original distribution README changed')
    return 17


def checksum_map(path):
    result = {}
    for line in (ROOT / path).read_text().splitlines():
        digest, name = line.split('  ', 1)
        require(bool(re.fullmatch(r'[0-9a-f]{64}', digest)), 'Invalid digest in ' + path)
        require(name not in result, 'Duplicate checksum entry in ' + path)
        result[name] = digest
    return result


def verify_licenses(all_files):
    directory = ROOT / 'licenses'
    expected = {'README.md', 'README.zh-CN.md', 'manifest.json', 'SHA256SUMS', *PUBLIC_LIC}
    require({p.name for p in directory.iterdir()} == expected, 'Unexpected license files or subdirectories')
    require(all(p.is_file() for p in directory.iterdir()), 'Keep licenses/ flat')
    manifest = read_json('licenses/manifest.json')
    require({r['file'] for r in manifest['files']} == set(PUBLIC_LIC), 'Public entitlement manifest changed')
    require(checksum_map('licenses/SHA256SUMS') == PUBLIC_LIC, 'Entitlement checksum list changed')
    for row in manifest['files']:
        require(row['sha256'] == PUBLIC_LIC[row['file']], 'Public entitlement hash baseline changed')
        verify_file({**row, 'path': 'licenses/' + row['file']})
        require(row['download_url'] == f'https://raw.githubusercontent.com/{REPOSITORY}/main/licenses/{row["file"]}',
                'Entitlement download URL changed')
    require({name for name in all_files if name.endswith('.lic')} == {'licenses/' + n for n in PUBLIC_LIC},
            'Unexpected entitlement file; do not commit private licenses')
    return len(PUBLIC_LIC)


def verify_releases():
    manifest = read_json('releases/manifest.json')
    require(manifest['repository'] == REPOSITORY, 'Release repository identity changed')
    baseline_bytes = (ROOT / 'docs/provenance/release-manifest.before-review.json').read_bytes()
    require(hashlib.sha256(baseline_bytes).hexdigest() == PRESERVED_RELEASE_MANIFEST, 'Preserved release baseline changed')
    baseline = json.loads(baseline_bytes)
    by_tag = {r['tag']: r for r in manifest['releases']}
    require(len(by_tag) == len(manifest['releases']), 'Duplicate release tag')
    for release in baseline['releases']:
        require(by_tag.get(release['tag']) == release, 'Preserved release metadata changed: ' + release['tag'])
    assets = [a for release in manifest['releases'] for a in release['assets']]
    require(len({a['name'] for a in assets}) == len(assets), 'Installer filenames must be unique in SHA256SUMS')
    require(checksum_map('SHA256SUMS') == {a['name']: a['sha256'] for a in assets}, 'Installer checksum lists disagree')
    for release in manifest['releases']:
        tag = release['tag']
        require(bool(release['assets']), 'Release has no installers: ' + tag)
        for suffix in ['', '.zh-CN']:
            note = (ROOT / f'docs/releases/{tag}{suffix}.md').read_text()
            home = (ROOT / f'README{suffix}.md').read_text()
            for asset in release['assets']:
                url = f'https://github.com/{REPOSITORY}/releases/download/{tag}/{asset["name"]}'
                require(asset['download_url'] == url, 'Invalid installer download URL')
                require(url in note and asset['sha256'] in note, 'Release note missing asset/digest: ' + tag + suffix)
                require(url in home, 'Installer missing from product home: ' + asset['name'])
    mapping = read_json('releases/tag-map.json')
    require({r['tag'] for r in mapping['tags']} == {r['tag'] for r in manifest['releases']} | {'legacy-v0.0.3'},
            'Tag map and release manifest disagree')
    for row in mapping['tags']:
        if row['tag'] in ORIGINAL_TAGS:
            require(row['commit'] == ORIGINAL_TAGS[row['tag']], 'Original tag baseline changed: ' + row['tag'])
        require(git('rev-parse', row['tag'] + '^{commit}').decode().strip() == row['commit'],
                'Published tag target changed: ' + row['tag'])
    return len(assets)


def verify_third_party():
    manifest = read_json('third-party/manifest.json')
    inventory = {r['path'] for r in manifest['files']}
    actual = {p.relative_to(ROOT / 'third-party').as_posix() for folder in ['sources', 'licenses']
              for p in (ROOT / 'third-party' / folder).rglob('*') if p.is_file()}
    require(inventory == actual and len(inventory) == len(manifest['files']), 'Third-party inventory disagrees with published files')
    for row in manifest['files']:
        verify_file({**row, 'path': 'third-party/' + row['path']})
    require(checksum_map('third-party/SHA256SUMS') == {r['path']: r['sha256'] for r in manifest['files']},
            'Third-party checksum lists disagree')
    return len(manifest['files'])


def markdown_anchors(text):
    anchors = set(re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)["\']', text))
    seen = Counter()
    outside_code = re.sub(r'```[^\n]*\n.*?```', '', text, flags=re.S)
    for heading in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', outside_code, flags=re.M):
        heading = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', heading)
        slug = re.sub(r'[^\w\s-]', '', heading.lower()).replace(' ', '-')
        count = seen[slug]
        seen[slug] += 1
        anchors.add(slug + (f'-{count}' if count else ''))
    return anchors


def verify_markdown(all_files):
    checked, paired = 0, 0
    for name in sorted(n for n in all_files if n.endswith('.md')):
        if name.startswith(ARCHIVE + '/') or name in FROZEN_MARKDOWN:
            continue
        file = ROOT / name
        text = file.read_text(encoding='utf-8')
        if name not in {'EULA.md', '.github/PULL_REQUEST_TEMPLATE.md'}:
            peer = name.replace('.zh-CN.md', '.md') if name.endswith('.zh-CN.md') else name[:-3] + '.zh-CN.md'
            require((ROOT / peer).is_file(), 'Missing language counterpart: ' + peer)
            relative = Path(os.path.relpath(ROOT / peer, file.parent)).as_posix()
            require(f']({relative})' in '\n'.join(text.splitlines()[:6]), 'Missing language switch: ' + name)
            paired += 1
        for target in re.findall(r'!?\[[^\]\n]*\]\(([^)\n]+)\)', text):
            target = target.strip()
            target = target[1:target.index('>')] if target.startswith('<') and '>' in target else target.split(' "', 1)[0].split(" '", 1)[0]
            url = urlsplit(target)
            if url.scheme or url.netloc:
                local = None
                for prefix in [f'https://github.com/{REPOSITORY}/blob/main/', f'https://github.com/{REPOSITORY}/tree/main/',
                               f'https://raw.githubusercontent.com/{REPOSITORY}/main/']:
                    if target.startswith(prefix):
                        local = ROOT / unquote(url.path.split('/main/', 1)[1])
                        break
                if local is None:
                    continue
            else:
                local = file.parent / unquote(url.path) if url.path else file
            require(local.exists(), f'Broken link in {name}: {target}')
            if url.fragment and local.suffix == '.md':
                require(unquote(url.fragment) in markdown_anchors(local.read_text()), f'Broken anchor in {name}: {target}')
            checked += 1
    return checked, paired // 2


def check_sensitive_patterns(all_files):
    patterns = {
        'private key': rb'-----BEGIN (?:RSA |EC |DSA |OPENSSH |ENCRYPTED )?PRIVATE KEY-----',
        'GitHub token': rb'(?:gh[pousr]_[A-Za-z0-9]{36,}|github_pat_[A-Za-z0-9_]{40,})',
        'provider key': rb'sk-[A-Za-z0-9_-]{32,}',
    }
    for name in all_files:
        path = ROOT / name
        if path.stat().st_size > 2 * 1024 * 1024 or path.suffix in {'.png', '.bmp', '.pdf', '.7z', '.rpm', '.xz', '.gz'}:
            continue
        data = path.read_bytes()
        for kind, pattern in patterns.items():
            require(not re.search(pattern, data), f'Potential {kind} in {name}; inspect privately without printing the value')


def main():
    all_files = {n for n in git('ls-files', '--cached', '--others', '--exclude-standard', '-z').decode().split('\0') if n}
    all_files = {n for n in all_files if (ROOT / n).is_file()}
    result = {
        'foundation_files_preserved': verify_foundation(),
        'distribution_files_preserved': verify_distribution(),
        'public_entitlements_verified': verify_licenses(all_files),
        'installer_assets_in_manifests': verify_releases(),
        'third_party_files_verified': verify_third_party(),
    }
    result['markdown_links_verified'], result['language_pairs_verified'] = verify_markdown(all_files)
    check_sensitive_patterns(all_files)
    result['tracked_or_pending_files_reviewed'] = len(all_files)
    result['known_secret_patterns_found'] = 0
    result['status'] = 'passed'
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    try:
        main()
    except (ValueError, KeyError, OSError, subprocess.CalledProcessError) as exc:
        print('Repository check failed: ' + str(exc), file=sys.stderr)
        sys.exit(1)
