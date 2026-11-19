#!/usr/bin/env python3
"""Refresh current release indexes from a separately verified public inventory."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
SOURCE_COMMIT = 'cf968d04f40db391946faabe7826974f3f84fd1c'
REPO = 'Shallot-2009/KetupaMK-AI-Fabric'
DATE = '2026-11-19'


def write_json(file, value):
    with file.open('w', encoding='utf-8', newline='\n') as stream:
        stream.write(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--inventory', type=Path, required=True)
    args = parser.parse_args()
    inventory = json.loads(args.inventory.read_bytes())
    if inventory.get('status') != 'PASS' or len(inventory.get('releases', [])) != 6:
        raise ValueError('A verified six-release inventory is required')
    before_bytes = subprocess.check_output(['git', 'show', SOURCE_COMMIT + ':releases/manifest.json'], cwd=ROOT)
    before = json.loads(before_bytes)
    old_by_tag = {r['tag']: r for r in before['releases']}
    incoming = {r['tag']: r for r in inventory['releases']}
    if set(old_by_tag) != set(incoming):
        raise ValueError('Do not add, remove or rename release groups')
    current = json.loads(before_bytes)
    rank = {'exe': 0, 'deb': 1, 'tar.gz': 2, 'rpm': 3, 'run': 4}
    replacements = {}
    revisions = []
    for release in current['releases']:
        tag = release['tag']
        source = incoming[tag]
        if source['prerelease'] != release['prerelease']:
            raise ValueError('Release status changed')
        assets = []
        for asset in source['assets']:
            if asset['state'] != 'uploaded' or not re.fullmatch(r'sha256:[a-f0-9]{64}', asset['digest']) or asset['size'] <= 0:
                raise ValueError('Invalid or unfinished asset')
            name = asset['name']
            url = f'https://github.com/{REPO}/releases/download/{tag}/{name}'
            if asset['browser_download_url'] != url or Path(name).name != name:
                raise ValueError('Invalid public asset URL')
            assets.append(dict(name=name, size_bytes=asset['size'], sha256=asset['digest'][7:], download_url=url, github_asset_id=asset['id']))
        def key(asset):
            name = asset['name']
            extension = 'tar.gz' if name.endswith('.tar.gz') else name.rsplit('.', 1)[-1]
            return rank.get(extension, 99), name
        assets.sort(key=key)
        after_by_name = {a['name']: a for a in assets}
        for old in release['assets']:
            if old['name'] not in after_by_name:
                raise ValueError('Existing download name disappeared: ' + old['name'])
            new = after_by_name[old['name']]
            replacements[old['sha256']] = new['sha256']
            replacements[f"{old['size_bytes']:,}"] = f"{new['size_bytes']:,}"
        revisions.append(dict(tag=tag, before_name=release['name'], after_name=source['name'],
                              before_assets=release['assets'], after_assets=assets))
        release['name'] = source['name']
        release['assets'] = assets
    if sum(len(r['assets']) for r in current['releases']) != 23:
        raise ValueError('Expected 23 attachments')
    current['synchronized_on'] = DATE
    journal = dict(schema_version=1, recorded_on=DATE, author='Asenjo HB',
                   reason='Synchronize contact-corrected installers and current download metadata without moving tags',
                   source_commit=SOURCE_COMMIT, source_manifest_sha256=hashlib.sha256(before_bytes).hexdigest(),
                   contacts=['asenjoaupa@gmail.com', '3405802009@qq.com'], releases=revisions)
    write_json(ROOT / 'releases/contact-refresh-20261119.json', journal)
    write_json(ROOT / 'releases/manifest.json', current)
    all_assets = [a for release in current['releases'] for a in release['assets']]
    if len({a['name'] for a in all_assets}) != 23:
        raise ValueError('Duplicate public attachment filename')
    (ROOT / 'SHA256SUMS').write_text(''.join(f"{a['sha256']}  {a['name']}\n" for a in all_assets), encoding='utf-8')
    maintained = [ROOT / 'README.md', ROOT / 'README.zh-CN.md']
    maintained += [p for folder in ['docs', 'releases', 'tools'] for p in (ROOT / folder).rglob('*.md')
                   if 'provenance' not in p.parts and p != ROOT / 'docs/governance/REVIEW.md']
    for file in maintained:
        text = file.read_text(encoding='utf-8')
        for old, new in replacements.items():
            text = text.replace(old, new)
        text = text.replace('six public groups / nineteen installers', 'six public groups / twenty-three attachments (nineteen unique packages)')
        text = text.replace('six public release groups / nineteen installers', 'six public release groups / twenty-three attachments (nineteen unique packages)')
        text = text.replace('6 个公开发行组、19 个安装包', '6 个公开发行组、23 个安装附件（19 个唯一安装包）')
        text = text.replace('6 个公开发行组 / 19 个安装包', '6 个公开发行组 / 23 个安装附件（19 个唯一安装包）')
        text = text.replace('Original filenames, bytes, tags, and release flags are retained.', 'Original download names, tag targets and release flags are retained; installer bytes follow the dated contact revision record.')
        text = text.replace('原文件名、字节、标签指向与发布标记保留。', '原下载文件名、标签指向与发布标记保留；安装包字节以有日期的联系方式修订记录为准。')
        text = text.replace('This historical distribution retains its original package files and publication status.', 'This historical distribution retains its version scope and publication status; current packages include the contact correction.')
        text = text.replace('This historical distribution is retained with its original package files and publication status.', 'This historical distribution retains its version scope and publication status; current packages include the contact correction.')
        text = text.replace('本历史发行组保留原安装包和发布状态', '本历史发行组保留原版本范围和发布状态，当前安装包已包含联系方式修正')
        text = text.replace('Original installers are published unchanged; no rebuild or re-signing was performed here.', 'The current contact-corrected packages are synchronized from audited development releases; earlier publication records remain historical evidence.')
        file.write_text(text, encoding='utf-8')
    for release in current['releases']:
        file = ROOT / 'docs/releases' / (release['tag'] + '.md')
        text = file.read_text(encoding='utf-8')
        text = re.sub(r'\n<!-- current-assets:start -->.*?<!-- current-assets:end -->\n', '', text, flags=re.S)
        rows = '\n'.join(f"| [{a['name']}]({a['download_url']}) | {a['size_bytes']:,} |" for a in release['assets'])
        blocks = [
            '\n<!-- current-assets:start -->\nContact-corrected downloads · 2026-11-19. Original names and tag targets retained; see the [revision record](../../releases/contact-refresh-20261119.json).\n\n| Installer | Bytes |\n| --- | --- |\n' + rows + '\n<!-- current-assets:end -->\n',
            '\n<!-- current-assets:start -->\n联系方式修正版 · 2026-11-19。保留原文件名与标签指向，见[修订记录](../../releases/contact-refresh-20261119.json)。\n\n| 安装包 | 字节数 |\n| --- | --- |\n' + rows + '\n<!-- current-assets:end -->\n',
        ]
        pieces = text.split('</details>')
        if len(pieces) != 3:
            raise ValueError('Expected exactly two language sections')
        checksum = '```text\n' + ''.join(f"{a['sha256']}  {a['name']}\n" for a in release['assets']) + '```'
        for index in range(2):
            pieces[index], count = re.subn(r'(?m)^\|[^\n]*\n\|[ |:\-]+\n(?:\|[^\n]*\n)+', lambda _: blocks[index], pieces[index], count=1)
            if count != 1:
                raise ValueError('Missing installer table: ' + release['tag'])
            pieces[index] = re.sub(r'```text\n(?:[a-f0-9]{64}  [^\n]+\n)+```', lambda _: checksum, pieces[index])
        text = '</details>'.join(pieces)
        file.write_text(text, encoding='utf-8')
    main = next(r for r in current['releases'] if r['tag'] == 'openketupamk-v1.0.2')
    mirrored = [a for a in main['assets'] if 'kernel-legacy' in a['name']]
    for filename, heading in [('README.md', 'The same corrected Legacy packages are also available in the primary 1.0.2 release: '), ('README.zh-CN.md', '同一套 Legacy 修正版也保留在主 1.0.2 发布页：')]:
        file = ROOT / filename
        text = file.read_text(encoding='utf-8')
        marker = '\n<!-- legacy-mirrors:start -->'
        text = re.sub(r'\n<!-- legacy-mirrors:start -->.*?<!-- legacy-mirrors:end -->\n', '', text, flags=re.S)
        links = ' · '.join(f"[{a['name'].rsplit('.', 1)[-1].upper() if not a['name'].endswith('.tar.gz') else 'TAR.GZ'}]({a['download_url']})" for a in mirrored)
        block = marker + '\n' + heading + links + '\n<!-- legacy-mirrors:end -->\n\n'
        text = text.replace('<a id="licenses"></a>', block + '<a id="licenses"></a>', 1)
        file.write_text(text, encoding='utf-8')
    print(json.dumps({'status': 'PASS', 'release_groups': 6, 'attachments': 23, 'journal_sha256': hashlib.sha256((ROOT / 'releases/contact-refresh-20261119.json').read_bytes()).hexdigest()}))


if __name__ == '__main__':
    main()
