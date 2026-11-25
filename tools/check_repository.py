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
CONTACT_SOURCE_COMMIT = 'cf968d04f40db391946faabe7826974f3f84fd1c'
CONTACT_SOURCE_MANIFEST = '98e2518ac8bad3cb94bca70dd2d83961a54f05a8286278f62db2f8dae574f9f6'
CONTACT_REVISION_DIGEST = '15129137772819ebf98474d852ec00e85888cc3ee148af5aa19f9900c2fc209e'
ROCKY_SOURCE_COMMIT = '6ec5bbba4da41de4288132a621894c930cf75192'
ROCKY_SOURCE_MANIFEST = '646e32b30912b431645372283758365cb5a4eb07f947a50960f6b235770369ad'
ROCKY_REVISION_DIGEST = '5d5cef0dd5e4b7382aca25b17f10770db0383c05bc2e717a890bbaf84c263a7b'
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
    'openketupamk-1.0.3-internal-test-12w.lic':
        'cdd73ecc64179446f2bd9645a6c2f40feadda0673b937fcae953d25f10c9bf14',
    'openketupamk-offline-test-12w.lic':
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
    for line in (ROOT / path).read_text(encoding='utf-8').splitlines():
        digest, name = line.split('  ', 1)
        require(bool(re.fullmatch(r'[0-9a-f]{64}', digest)), 'Invalid digest in ' + path)
        require(name not in result, 'Duplicate checksum entry in ' + path)
        result[name] = digest
    return result


def verify_licenses(all_files):
    directory = ROOT / 'licenses'
    expected = {'README.md', 'manifest.json', 'SHA256SUMS', *PUBLIC_LIC}
    require({p.name for p in directory.iterdir()} == expected, 'Unexpected license files or subdirectories')
    require(all(p.is_file() for p in directory.iterdir()), 'Keep licenses/ flat')
    manifest = read_json('licenses/manifest.json')
    require({r['file'] for r in manifest['files']} == set(PUBLIC_LIC), 'Public entitlement manifest changed')
    require(len(manifest['files']) == len(PUBLIC_LIC) == 3, 'Expected exactly three designated test licenses')
    require([r['issued_beijing'] for r in manifest['files']] ==
            sorted((r['issued_beijing'] for r in manifest['files']), reverse=True),
            'List test licenses newest first')
    require(checksum_map('licenses/SHA256SUMS') == PUBLIC_LIC, 'Entitlement checksum list changed')
    for row in manifest['files']:
        require(row['sha256'] == PUBLIC_LIC[row['file']], 'Public entitlement hash baseline changed')
        verify_file({**row, 'path': 'licenses/' + row['file']})
        require(row['download_url'] == f'https://raw.githubusercontent.com/{REPOSITORY}/main/licenses/{row["file"]}',
                'Entitlement download URL changed')
        require(row['page_url'] == f'https://github.com/{REPOSITORY}/blob/main/licenses/{row["file"]}',
                'Entitlement page URL changed')
        require(row['max_instances'] == 3 and row['duration'] == '12w', 'Test license scope metadata changed')
        content = (directory / row['file']).read_text(encoding='utf-8')
        require(re.search(r'^max_instances=3\r?$', content, re.M), 'Do not publish an unlimited test license')
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
    source_bytes = git('show', CONTACT_SOURCE_COMMIT + ':releases/manifest.json')
    require(hashlib.sha256(source_bytes).hexdigest() == CONTACT_SOURCE_MANIFEST,
            'Pre-contact release snapshot changed')
    source = json.loads(source_bytes)
    source_by_tag = {r['tag']: r for r in source['releases']}
    for release in baseline['releases']:
        require(source_by_tag.get(release['tag']) == release,
                'Original release metadata missing from preserved snapshot: ' + release['tag'])
    contact_bytes = git('show', ROCKY_SOURCE_COMMIT + ':releases/manifest.json')
    require(hashlib.sha256(contact_bytes).hexdigest() == ROCKY_SOURCE_MANIFEST,
            'Pre-Rocky release snapshot changed')
    contact = json.loads(contact_bytes)
    contact_by_tag = {r['tag']: r for r in contact['releases']}
    revision_bytes = (ROOT / 'releases/contact-refresh-20261119.json').read_bytes()
    require(hashlib.sha256(revision_bytes).hexdigest() == CONTACT_REVISION_DIGEST,
            'Reviewed contact revision record changed')
    revision = json.loads(revision_bytes)
    require(revision['source_commit'] == CONTACT_SOURCE_COMMIT and
            revision['source_manifest_sha256'] == CONTACT_SOURCE_MANIFEST,
            'Contact revision source mismatch')
    require(revision['recorded_on'] == contact.get('synchronized_on') == '2026-11-19' and
            revision['author'] == 'Asenjo HB' and
            revision['contacts'] == ['asenjoaupa@gmail.com', '3405802009@qq.com'],
            'Contact revision attribution mismatch')
    revisions = {r['tag']: r for r in revision['releases']}
    require(len(revisions) == len(revision['releases']) == len(contact_by_tag) == 6 and
            set(revisions) == set(contact_by_tag) == set(source_by_tag), 'Contact release group mismatch')
    require({k: v for k, v in contact.items() if k not in {'releases', 'synchronized_on'}} ==
            {k: v for k, v in source.items() if k != 'releases'}, 'Release provenance changed')
    for tag, release in contact_by_tag.items():
        old, change = source_by_tag[tag], revisions[tag]
        require(change['before_assets'] == old['assets'] and change['after_assets'] == release['assets'],
                'Installer revision mismatch: ' + tag)
        require(change['before_name'] == old['name'] and change['after_name'] == release['name'],
                'Release display title revision mismatch: ' + tag)
        require({k: v for k, v in release.items() if k not in {'assets', 'name'}} ==
                {k: v for k, v in old.items() if k not in {'assets', 'name'}},
                'Release identity, status or publication provenance changed: ' + tag)
        require({a['name'] for a in old['assets']} <= {a['name'] for a in release['assets']},
                'Historical installer download name removed: ' + tag)
    rocky_bytes = (ROOT / 'releases/legacy-rocky8-20261120.json').read_bytes()
    require(hashlib.sha256(rocky_bytes).hexdigest() == ROCKY_REVISION_DIGEST,
            'Rocky rebuild revision record changed')
    rocky = json.loads(rocky_bytes)
    require(rocky['source_commit'] == ROCKY_SOURCE_COMMIT and
            rocky['source_manifest_sha256'] == ROCKY_SOURCE_MANIFEST and
            rocky['recorded_on'] == manifest.get('synchronized_on') == '2026-11-20',
            'Rocky rebuild provenance mismatch')
    acceptance = (ROOT / 'releases/legacy-rocky8-20261120-acceptance.json').read_bytes()
    require(hashlib.sha256(acceptance).hexdigest() == rocky['acceptance_summary_sha256'],
            'Rocky acceptance summary changed')
    acceptance_record = json.loads(acceptance)
    legacy_assets = by_tag['openketupamk-kernel-legacy-v1.0.2']['assets']
    require(acceptance_record['distribution_tag'] == 'openketupamk-kernel-legacy-v1.0.2' and
            acceptance_record['build_date'] == '2026-11-20' and
            acceptance_record['installer_assets'] == [
                {k: asset[k] for k in ('name', 'size_bytes', 'sha256')}
                for asset in legacy_assets
            ],
            'Rocky acceptance summary does not match current installers')
    changes = {r['tag']: r for r in rocky['releases']}
    require(len(changes) == len(rocky['releases']) == 2 and
            set(changes) == {'openketupamk-v1.0.2', 'openketupamk-kernel-legacy-v1.0.2'} and
            set(by_tag) == set(contact_by_tag),
            'Rocky rebuild release group mismatch')
    require({k: v for k, v in manifest.items() if k not in {'releases', 'synchronized_on'}} ==
            {k: v for k, v in contact.items() if k not in {'releases', 'synchronized_on'}},
            'Release provenance changed after contact revision')
    for tag, release in by_tag.items():
        previous = contact_by_tag[tag]
        if tag in changes:
            change = changes[tag]
            require(change['before_assets'] == previous['assets'] and
                    change['after_assets'] == release['assets'] and
                    change['before_acceptance_summary'] == previous.get('acceptance_summary') and
                    change['after_acceptance_summary'] == release.get('acceptance_summary'),
                    'Rocky installer revision mismatch: ' + tag)
            expected = {**previous, 'assets': change['after_assets']}
            if change['after_acceptance_summary'] is not None:
                expected['acceptance_summary'] = change['after_acceptance_summary']
            require(release == expected, 'Unrelated release metadata changed: ' + tag)
        else:
            require(release == previous, 'Unrelated release changed: ' + tag)
    assets = [a for release in manifest['releases'] for a in release['assets']]
    require(len(assets) == 23 and len({a['sha256'] for a in assets}) == 19,
            'Expected 23 attachments containing 19 unique packages')
    for asset in assets:
        require(bool(re.fullmatch(r'[0-9a-f]{64}', asset['sha256'])) and asset['size_bytes'] > 0,
                'Invalid installer size/digest')
    require(len({a['name'] for a in assets}) == len(assets), 'Installer filenames must be unique in SHA256SUMS')
    require(checksum_map('SHA256SUMS') == {a['name']: a['sha256'] for a in assets}, 'Installer checksum lists disagree')
    for release in manifest['releases']:
        tag = release['tag']
        require(bool(release['assets']), 'Release has no installers: ' + tag)
        notes = language_sections((ROOT / f'docs/releases/{tag}.md').read_text(encoding='utf-8'))
        homes = {'English': (ROOT / 'README.md').read_text(encoding='utf-8'),
                 '简体中文': (ROOT / 'README.zh-CN.md').read_text(encoding='utf-8')}
        for language in ['English', '简体中文']:
            note, home = notes[language], homes[language]
            for asset in release['assets']:
                url = f'https://github.com/{REPOSITORY}/releases/download/{tag}/{asset["name"]}'
                require(asset['download_url'] == url, 'Invalid installer download URL')
                require(url in note and asset['sha256'] in note, 'Release note missing asset/digest: ' + tag + language)
                require(url in home, 'Installer missing from product home: ' + asset['name'])
    mapping = read_json('releases/tag-map.json')
    require({r['tag'] for r in mapping['tags']} == {r['tag'] for r in manifest['releases']} | {'legacy-v0.0.3'},
            'Tag map and release manifest disagree')
    for row in mapping['tags']:
        if row['tag'] in ORIGINAL_TAGS:
            require(row['commit'] == ORIGINAL_TAGS[row['tag']], 'Original tag baseline changed: ' + row['tag'])
        # A publication snapshot cannot embed its own commit hash. Only that
        # snapshot may use "self"; the next main commit records its concrete ID.
        expected = row['commit']
        if expected == 'self':
            expected = git('rev-parse', 'HEAD').decode().strip()
        require(bool(re.fullmatch(r'[0-9a-f]{40}', expected)), 'Invalid tag commit: ' + row['tag'])
        require(git('rev-parse', row['tag'] + '^{commit}').decode().strip() == expected,
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


def language_sections(text):
    pattern = r'<details name="readme-language"(?P<open> open)?>\s*<summary><strong>(?P<language>English|简体中文)</strong></summary>\s*(?P<body>.*?)\s*</details>'
    sections = list(re.finditer(pattern, text, flags=re.S))
    require(len(sections) == 2, 'Expected two language sections on the same page')
    require({m['language'] for m in sections} == {'English', '简体中文'}, 'Missing language section')
    require([m['language'] for m in sections if m['open']] == ['简体中文'], 'Expected one default language in the shared disclosure group')
    return {m['language']: m['body'] for m in sections}


def verify_origin_records():
    history = read_json('history/origin-records.json')
    events = {e['id']: e for e in history['events']}
    require(len(events) == len(history['events']), 'Duplicate origin event')
    beginning = events['project-beginning']
    early = events['early-commits']
    require(beginning['period'] == '2023' and beginning['source_type'] == 'maintainer-statement', 'Project beginning/source changed without review')
    require(early['period_start'] == '2024-05' and early['period_end'] == '2024-06', 'Early project history range changed')
    require(early['source_type'] == 'maintainer-statement', 'Keep the original maintainer history statement')
    for event in history['events']:
        if event.get('git_object_verified'):
            commit = event.get('commit', '')
            require(bool(re.fullmatch(r'[0-9a-f]{40}', commit)), 'Invalid origin Git evidence reference')
            require(git('cat-file', '-t', commit).decode().strip() == 'commit', 'Missing origin Git evidence')
            require(git('show', '-s', '--format=%as', commit).decode().strip() == event['date'], 'Origin Git evidence date mismatch')
        if event['source_type'] == 'maintainer-statement':
            require(event.get('git_object_verified') is False, 'A maintainer statement must not be relabeled as verified Git evidence')
    retained = events['earliest-currently-retained-commit']
    require(retained['commit'] == '82251a75bb98532dcd2350d6c691ea0b7cbd7f3a', 'Current retained history baseline changed')
    return len(events)


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
    checked, bilingual = 0, 0
    for name in sorted(n for n in all_files if n.endswith('.md')):
        if name.startswith(ARCHIVE + '/') or name in FROZEN_MARKDOWN:
            continue
        file = ROOT / name
        text = file.read_text(encoding='utf-8')
        if name in {'README.md', 'README.zh-CN.md'}:
            top = '\n'.join(text.splitlines()[:6])
            require('](README.md)' in top and '](README.zh-CN.md)' in top,
                    'Keep both product README language links at the top: ' + name)
            require('<details' not in text, 'Product READMEs must be separate full pages: ' + name)
        elif name not in {'EULA.md', '.github/PULL_REQUEST_TEMPLATE.md'}:
            require(not name.endswith('.zh-CN.md'), 'Keep maintained languages on one page: ' + name)
            language_sections(text)
            bilingual += 1
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
                require(unquote(url.fragment) in markdown_anchors(local.read_text(encoding='utf-8')), f'Broken anchor in {name}: {target}')
            checked += 1
    return checked, bilingual


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
        'origin_events_recorded': verify_origin_records(),
        'distribution_files_preserved': verify_distribution(),
        'public_entitlements_verified': verify_licenses(all_files),
        'installer_assets_in_manifests': verify_releases(),
        'third_party_files_verified': verify_third_party(),
    }
    result['markdown_links_verified'], result['same_page_bilingual_documents_verified'] = verify_markdown(all_files)
    result['separate_product_readmes_verified'] = 2
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
