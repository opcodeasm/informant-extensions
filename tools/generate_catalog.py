#!/usr/bin/env python3
"""Generate the download catalog using only Python 3.10+ standard-library modules."""
from __future__ import annotations

import argparse
from dataclasses import dataclass, field
import hashlib
from pathlib import Path
import re
import sys
import unicodedata
from urllib.parse import quote
import xml.etree.ElementTree as ET

NS = "urn:inform7:extension-catalog:1"
ET.register_namespace("", NS)
VERSION = r"\d+(?:\.\d+){0,2}(?:/\d+)?"
HEADER = re.compile(
    rf"\A\s*(?:Version\s+(?P<version>{VERSION})\s+of\s+)?"
    r"(?P<title>.+?)\s+by\s+(?P<author>.+?)\s+begins?\s+here\s*\.", re.I | re.S
)
IDENTITY = re.compile(
    rf"(?:version\s+(?P<version>{VERSION})\s+of\s+)?"
    r"(?P<title>.+?)\s+by\s+(?P<author>.+)", re.I | re.S
)
HEADING = re.compile(r"^[ \t]*(Volume|Book|Part|Chapter|Section)\b[^\n]*", re.I | re.M)
INCLUDE = re.compile(r"\bInclude\s+(?!\s*\(-)", re.I)
CONDITION = re.compile(r"\(\s*for\s+use\s+(with|without)\s+(.+?)\)", re.I)
LEVELS = {name: i for i, name in enumerate(("volume", "book", "part", "chapter", "section"))}


def compact(value: str) -> str:
    return " ".join(value.split())


def normalize(value: str) -> str:
    return compact(unicodedata.normalize("NFC", value)).casefold()


def version_tuple(value: str) -> tuple[int, int, int]:
    if "/" in value:
        major, date = value.split("/")
        return int(major), 0, int(date)
    numbers = [int(n) for n in value.split(".")]
    return tuple((numbers + [0, 0])[:3])


def identity(value: str) -> dict[str, str]:
    match = IDENTITY.fullmatch(compact(value))
    if not match:
        raise ValueError(f"Unsupported extension reference: {value!r}")
    return {key: compact(val) for key, val in match.groupdict().items() if val}


def mask_noncode(source: str) -> str:
    """Hide nested comments, quoted text and I6 inclusions, preserving offsets/lines."""
    out = list(source)
    i = 0
    while i < len(source):
        start = i
        if source[i] == '[':
            depth = 1
            i += 1
            while i < len(source) and depth:
                depth += (source[i] == '[') - (source[i] == ']')
                i += 1
        elif source[i] == '"':
            i += 1
            while i < len(source) and source[i] != '"':
                i += 1
            i += i < len(source)
        elif source.startswith('(-', i):
            end = source.find('-)', i + 2)
            if end < 0:
                raise ValueError("Unterminated Inform 6 inclusion")
            i = end + 2
        else:
            i += 1
            continue
        for j in range(start, i):
            if out[j] not in '\r\n':
                out[j] = ' '
    return ''.join(out)


@dataclass
class Extension:
    path: str
    title: str
    author: str
    version: str
    qualifiers: str
    encoding: str
    data: bytes
    dependencies: list[dict] = field(default_factory=list)
    warnings: list[tuple[int, str]] = field(default_factory=list)

    @property
    def id(self) -> str:
        return 'ext-' + hashlib.sha256(self.path.encode('utf-8')).hexdigest()[:24]

    @property
    def key(self) -> tuple[str, str]:
        return normalize(self.title), normalize(self.author)


def parse_extension(path: str, data: bytes) -> Extension:
    try:
        source = data.decode('utf-8-sig')
        encoding = 'utf-8'
    except UnicodeDecodeError:
        source = data.decode('cp1252')
        encoding = 'windows-1252'
    # Documentation examples are never dependencies of the extension itself.
    source = re.split(r"(?im)^\s*-{2,}\s*DOCUMENTATION\s*-{2,}\s*$", source)[0]
    code = mask_noncode(source)
    header = HEADER.match(code)
    if not header:
        raise ValueError(f"{path}: cannot parse extension header")
    title = compact(header['title'])
    qualifiers = '; '.join(re.findall(r'\(([^()]*)\)', title))
    title = compact(re.sub(r'\([^()]*\)', '', title))
    ext = Extension(path, title, compact(header['author']), header['version'] or '',
                    qualifiers, encoding, data)
    end = re.search(r"(?im)^[^\n]*\bends?\s+here\s*\.", code[header.end():])
    if end:
        code = code[:header.end() + end.start()]
    else:
        ext.warnings.append((1, 'No extension end marker found.'))
    # Inline I6 includes were masked; remove their Include keyword as well.
    for match in re.finditer(r'\bInclude\s*\(-', source, re.I):
        start = match.start()
        code = code[:start] + re.sub(r'\S', ' ', code[start:start + 7]) + code[start + 7:]
    events = [(m.start(), 'heading', m) for m in HEADING.finditer(code)]
    events += [(m.start(), 'include', m) for m in INCLUDE.finditer(code, header.end())
               if re.search(r'(?:^|[.;\n])[ \t]*$', code[:m.start()])]
    scope: list[tuple[int, list[dict]]] = []
    for offset, kind, match in sorted(events, key=lambda e: e[0]):
        line = source.count('\n', 0, offset) + 1
        if kind == 'heading':
            level = LEVELS[match[1].lower()]
            scope = [(rank, conditions) for rank, conditions in scope if rank < level]
            conditions = []
            for cond in CONDITION.finditer(match[0]):
                ref = identity(cond[2])
                conditions.append(dict(ref, present=str(cond[1].lower() == 'with').lower()))
                ext.dependencies.append(dict(ref, kind='integration', line=line,
                                             when=cond[1].lower(), conditions=[]))
            scope.append((level, conditions))
            continue
        tail = code[match.end():]
        # Periods in version numbers and author initials are not sentence endings.
        stop = re.search(r'(?<!\b[A-Z])\.(?=\s|$)|;|\n[ \t]*\n', tail)
        if not stop:
            raise ValueError(f'{path}:{line}: unterminated Include declaration')
        declaration = compact(tail[:stop.start()])
        ref = identity(declaration)
        conditions = [c for _, group in scope for c in group]
        ext.dependencies.append(dict(ref, kind='include', line=line, conditions=conditions))
        if stop[0].startswith('\n'):
            ext.warnings.append((line, 'Include declaration has no terminal punctuation; inferred at blank line.'))
    return ext


def element(parent: ET.Element, tag: str, **attrs: str) -> ET.Element:
    return ET.SubElement(parent, f'{{{NS}}}{tag}', attrs)


def resolve(ref: dict, index: dict) -> dict[str, str]:
    candidates = index.get((normalize(ref['title']), normalize(ref['author'])), [])
    if not candidates:
        return {'status': 'external'}
    requested = ref.get('version')
    compatible = candidates
    if requested:
        minimum = version_tuple(requested)
        compatible = [e for e in candidates if e.version and
                      version_tuple(e.version)[0] == minimum[0] and version_tuple(e.version) >= minimum]
    if not compatible:
        return {'status': 'version-mismatch'}
    # List every acceptable candidate; consumers must intersect constraints globally.
    return {'status': 'internal', 'targets': ' '.join(e.id for e in compatible)}


def reference(parent: ET.Element, tag: str, ref: dict, index: dict, **extra: str) -> ET.Element:
    attrs = dict(title=ref['title'], author=ref['author'], **extra)
    if ref.get('version'):
        attrs['requested-version'] = ref['version']
        lower = version_tuple(ref['version'])
        attrs['min-version'] = '.'.join(map(str, lower))
        attrs['max-version-exclusive'] = f'{lower[0] + 1}.0.0'
    return element(parent, tag, **attrs, **resolve(ref, index))


def generate(root: Path, repository: str, ref: str) -> bytes:
    if not re.fullmatch(r'[\w.-]+/[\w.-]+', repository):
        raise ValueError('--repository must be a GitHub owner/repository')
    if not ref or any(c.isspace() for c in ref):
        raise ValueError('--ref must be a nonempty Git ref without whitespace')
    paths = sorted(p for p in root.rglob('*') if p.is_file() and p.suffix.lower() == '.i7x'
                   and not any(part.startswith('.') for part in p.relative_to(root).parts))
    extensions = [parse_extension(p.relative_to(root).as_posix(), p.read_bytes()) for p in paths]
    if not extensions:
        raise ValueError('No .i7x files found')
    index: dict = {}
    for ext in extensions:
        index.setdefault(ext.key, []).append(ext)
    base = f'https://raw.githubusercontent.com/{repository}/{quote(ref, safe="")}/'
    catalog = ET.Element(f'{{{NS}}}catalog', {
        'schema-version': '1', 'repository': f'https://github.com/{repository}',
        'ref': ref, 'url': base + 'catalog/extensions.xml', 'language-version': '10.1',
        'version-policy': 'inform-10-compatible', 'generator': 'tools/generate_catalog.py',
    })
    for ext in extensions:
        attrs = dict(id=ext.id, title=ext.title, author=ext.author, path=ext.path,
                     folder=str(Path(ext.path).parent), encoding=ext.encoding)
        if ext.version:
            attrs['version'] = ext.version
        if ext.qualifiers:
            attrs['qualifiers'] = ext.qualifiers
        entry = element(catalog, 'extension', **attrs)
        element(entry, 'download', url=base + quote(ext.path, safe='/'),
                filename=Path(ext.path).name, bytes=str(len(ext.data)),
                sha256=hashlib.sha256(ext.data).hexdigest())
        deps = element(entry, 'dependencies')
        for dep in ext.dependencies:
            attrs = {'kind': dep['kind'], 'line': str(dep['line'])}
            if dep.get('when'):
                attrs['when'] = dep['when']
            node = reference(deps, 'dependency', dep, index, **attrs)
            for condition in dep['conditions']:
                reference(node, 'condition', condition, index, present=condition['present'])
        for line, message in ext.warnings:
            element(entry, 'warning', line=str(line)).text = message
    ET.indent(catalog, space='  ')
    return ET.tostring(catalog, encoding='utf-8', xml_declaration=True) + b'\n'


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--repository', default='interactivefiction/inform7extensions')
    parser.add_argument('--ref', default='10.1', help='GitHub branch, tag, or commit used in download URLs')
    parser.add_argument('--output', type=Path, default=Path('catalog/extensions.xml'))
    parser.add_argument('--check', action='store_true', help='Fail if the checked-in catalog differs')
    args = parser.parse_args()
    try:
        data = generate(args.root, args.repository, args.ref)
        output = args.output if args.output.is_absolute() else args.root / args.output
        if args.check:
            if not output.exists() or output.read_bytes() != data:
                print(f'Catalog is stale: regenerate {output}', file=sys.stderr)
                return 1
        else:
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_bytes(data)
        tree = ET.fromstring(data)
        counts: dict[str, int] = {}
        for dep in tree.findall(f'.//{{{NS}}}dependency'):
            key = dep.get('kind') + '/' + dep.get('status')
            counts[key] = counts.get(key, 0) + 1
        print(f'{len(tree)} extensions; dependency declarations: {counts}')
        for entry in tree:
            for warning in entry.findall(f'{{{NS}}}warning'):
                print(f"Warning: {entry.get('path')}:{warning.get('line')}: {warning.text}", file=sys.stderr)
        return 0
    except (ValueError, OSError) as error:
        print(f'Catalog generation failed: {error}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
