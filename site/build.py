"""Build the offline HTML docs hub and registered documents. Never writes handoff/."""
from __future__ import annotations

import argparse
import html
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit, urlunsplit

import markdown

ROOT = Path(__file__).resolve().parents[1]
CATALOG = json.loads((ROOT / 'site/catalog.json').read_text(encoding='utf-8'))


def output_path(source: str) -> str:
    path = Path(source)
    return (path.with_name('index.html') if path.name == 'README.md' else path.with_suffix('.html')).as_posix()


MAPPING = {entry['source']: entry.get('output', output_path(entry['source'])) for entry in CATALOG}


def relative(target: str, current: str) -> str:
    return Path(os.path.relpath(ROOT / target, (ROOT / current).parent)).as_posix()


def escape(value: str) -> str:
    return html.escape(value, quote=True)


def frame(title: str, description: str, current: str, content: str) -> str:
    def link(path): return escape(relative(path, current))
    groups = []
    for category in dict.fromkeys(e['category'] for e in CATALOG):
        links = []
        for entry in CATALOG:
            if entry['category'] != category: continue
            target = MAPPING[entry['source']]
            active = target == current or (current == 'index.html' and entry['source'] == 'README.md')
            search = escape((entry['title']+' '+entry['description']).lower())
            links.append(f'<a data-nav-page data-search="{search}" href="{link(target)}"'+(' aria-current="page"' if active else '')+f'>{escape(entry["title"])}</a>')
        block = f'<section data-nav-group><h2>{escape(category)}</h2>{"".join(links)}</section>'
        if category == 'Source records': block = '<details class="source-records"><summary>Source records</summary>'+block+'</details>'
        groups.append(block)
    pager = ''
    index = next((i for i,e in enumerate(CATALOG) if MAPPING[e['source']] == current), None)
    if index is not None:
        items = []
        for label, pos in [('Previous', index-1), ('Next', index+1)]:
            if 0 <= pos < len(CATALOG):
                e = CATALOG[pos]; items.append(f'<a href="{link(MAPPING[e["source"]])}"><span>{label}</span>{escape(e["title"])}</a>')
        pager = '<nav class="page-pager" aria-label="Page navigation">'+''.join(items)+'</nav>'
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="{escape(description)}"><meta name="theme-color" content="#f8f7f2">
<title>{escape(title)} | Trueforms Docs</title><link rel="icon" href="{link('brand/handoff/v2/assets/svg/favicon.svg')}">
<link rel="stylesheet" href="{link('site/docs.css')}"><script src="{link('site/docs.js')}" defer></script></head>
<body><a class="skip" href="#main">Skip to content</a>
<header class="site-header"><a class="brand-link" href="{link('index.html')}" aria-label="Trueforms documentation home"><img src="{link('brand/handoff/v2/assets/svg/trueforms-logo.svg')}" alt="Trueforms" width="170" height="28"></a><span>Documentation</span><a href="{link('planning/saas-implementation-plan.html')}">Build path</a></header>
<div class="docs-shell"><aside class="sidebar"><details class="site-navigation" open><summary>Browse documentation</summary><div class="nav-content"><label class="search-field js-only" for="nav-search">Find a page<input id="nav-search" type="search" placeholder="Search pages" autocomplete="off"></label><nav aria-label="Documentation">{''.join(groups)}</nav><p id="nav-empty" role="status" hidden>No matching pages.</p><a class="all-files" href="{link('files.html')}">All source files</a></div></details></aside>
<div class="reading-area">{content}{pager}<footer class="site-footer"><span>Trueforms documentation</span><a href="{link('brand/handoff/v2/licenses/README.txt')}">Font notices</a><a href="#main">Back to top</a></footer></div></div></body></html>
'''


def rewrite_links(body: str, source: str) -> str:
    def replace(match):
        href = html.unescape(match.group(1))
        parsed = urlsplit(href)
        if parsed.scheme or parsed.netloc or not parsed.path:
            return match.group(0)
        resolved = ((ROOT / source).parent / unquote(parsed.path)).resolve()
        try:
            key = resolved.relative_to(ROOT).as_posix()
        except ValueError:
            return match.group(0)
        if key not in MAPPING:
            return match.group(0)
        updated = urlunsplit(('', '', relative(MAPPING[key], MAPPING[source]), parsed.query, parsed.fragment))
        return f'href="{escape(updated)}"'
    return re.sub(r'href="([^"]*)"', replace, body)


def document(entry: dict) -> str:
    source, current = entry['source'], MAPPING[entry['source']]
    text = (ROOT / source).read_text(encoding='utf-8')
    # The catalog heading replaces the Markdown H1; all remaining source content is retained.
    text = re.sub(r'\A# [^\n]+\n', '', text, count=1)
    renderer = markdown.Markdown(extensions=['tables', 'fenced_code', 'toc'], extension_configs={'toc': {'toc_depth': '2-2'}})
    body = rewrite_links(renderer.convert(text), source)
    table_index = 0

    def table(match):
        nonlocal table_index
        table_index += 1
        value = match.group(0)
        heading = re.search(r'<thead>(.*?)</thead>', value, re.S)
        if heading and heading.group(1).count('<th') > 4:
            value = value.replace('<table>', '<table class="wide">', 1)
        value = re.sub(r'<th(?=[ >])', '<th scope="col"', value)
        value = re.sub(r'<td(?: style="[^"]*")?>([DOA?])</td>', lambda m: f'<td class="evidence {"unknown" if m[1] == "?" else "observed" if m[1] == "O" else "listed"}">{m[1]}</td>', value)
        return f'<div class="table-wrap" role="region" aria-label="Table {table_index}, scroll horizontally if needed" tabindex="0">{value}</div>'

    body = re.sub(r'<table>.*?</table>', table, body, flags=re.S)
    toc = renderer.toc
    category = escape(entry['category'])
    content = f'''<main id="main"><div class="breadcrumbs"><a href="{escape(relative('index.html', current))}">Docs</a> / {category}</div>
<header class="document-header"><h1>{escape(entry['title'])}</h1><p class="description">{escape(entry['description'])}</p>
<div class="document-meta meta"><span>{escape(entry['kind'])}</span><time datetime="{entry['date']}">{entry['date']}</time><a href="{escape(relative(source, current))}">Markdown source</a><button class="quiet-button js-only" data-print>Print / Save PDF</button></div></header>
<div class="document-layout"><details class="page-toc" open><summary>On this page</summary><nav aria-label="On this page">{toc}</nav></details>
<article class="article">{body}</article></div></main>'''
    return frame(entry['title'], entry['description'], current, content)


def hub() -> str:
    return document(CATALOG[0])


def file_index(outputs: set[str]) -> str:
    # A static inventory makes raw evidence/assets discoverable without server directory listings.
    paths = sorted({p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file() and not any(part.startswith('.') or part == '__pycache__' for part in p.relative_to(ROOT).parts)} | outputs)
    groups = {}
    for path in paths:
        groups.setdefault(path.split('/')[0] if '/' in path else 'Repository', []).append(path)
    body = '<h1>All files</h1><p>Source documents, HTML pages, assets, evidence and tooling. Original file names and languages are preserved.</p>'
    for group, items in groups.items():
        body += f'<h2>{escape(group)}</h2><ul class="file-list">' + ''.join(f'<li><a href="{escape(path)}">{escape(path)}</a></li>' for path in items) + '</ul>'
    return frame('All files', 'Complete static inventory of the documentation repository.', 'files.html', f'<main id="main" class="article intro">{body}</main>')


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.ids = [], set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        for key in ('href', 'src'):
            if key in attrs:
                self.links.append(attrs[key])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Verify generated pages and local links without writing.')
    args = parser.parse_args()
    sources = {entry['source'] for entry in CATALOG}
    discovered = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*.md') if not any(part.startswith('.') for part in p.relative_to(ROOT).parts) and not p.is_relative_to(ROOT / 'brand/handoff')}
    missing = discovered - sources - {'README.md', 'AGENTS.md'}
    if missing:
        raise SystemExit(f'Unregistered Markdown documents: {sorted(missing)}')
    if len(sources) != len(CATALOG) or len(set(MAPPING.values())) != len(MAPPING):
        raise SystemExit('Duplicate source or output path in catalog')
    outputs = {MAPPING[entry['source']]: document(entry) for entry in CATALOG}
    outputs['index.html'] = hub()
    outputs['files.html'] = file_index(set(outputs) | {'files.html'})
    errors = []
    for name, content in outputs.items():
        path = ROOT / name
        if path.resolve().is_relative_to(ROOT / 'brand/handoff'):
            raise SystemExit('Refusing to overwrite preserved source')
        if args.check:
            if not path.exists() or path.read_text(encoding='utf-8') != content:
                errors.append(f'Stale HTML: {name}')
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding='utf-8', newline='\n')
    for name, content in outputs.items():
        parsed = Links()
        parsed.feed(content)
        for link in parsed.links:
            url = urlsplit(link)
            if url.scheme or url.netloc:
                continue
            target = ((ROOT / name).parent / unquote(url.path)).resolve() if url.path else ROOT / name
            if not target.exists():
                errors.append(f'{name}: missing {link}')
            elif url.fragment and target.suffix == '.html':
                target_parser = Links()
                target_parser.feed(target.read_text(encoding='utf-8'))
                if unquote(url.fragment) not in target_parser.ids:
                    errors.append(f'{name}: missing anchor {link}')
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'{"Checked" if args.check else "Built"} {len(outputs)} HTML pages; all local HTML links, assets and anchors resolve.')


if __name__ == '__main__':
    main()
