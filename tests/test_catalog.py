"""Regression tests for dependency extraction and catalog integrity."""
import hashlib
from pathlib import Path
import tempfile
import unittest
from urllib.parse import unquote
import xml.etree.ElementTree as ET

from tools.generate_catalog import NS, generate, parse_extension, resolve, version_tuple

ROOT = Path(__file__).resolve().parents[1]
Q = '{' + NS + '}'


def parse(body, title='Example', author='Writer', version='1'):
    return parse_extension(f'{author}/{title}.i7x',
                           f'Version {version} of {title} by {author} begins here.\n\n{body}\n\n{title} ends here.\n'.encode())


class ParsingTests(unittest.TestCase):
    def test_comments_strings_i6_and_documentation_are_ignored(self):
        ext = parse('''[ Include Fake by Someone. [Nested comment] ]
"Include Fake by Someone."
Include (- [ Test; print "Include Fake by Someone."; ]; -).
After reading a command when the player's command does not include "x": say "ok".
Include Real by Someone.
Example ends here.
---- DOCUMENTATION ----
Include Fake by Someone.''')
        self.assertEqual([d['title'] for d in ext.dependencies], ['Real'])

    def test_multiline_multiple_and_versioned_includes(self):
        ext = parse('Include version 2.4 of Real\nby A. Writer. Include Other by Someone;')
        self.assertEqual([(d['title'], d['author']) for d in ext.dependencies],
                         [('Real', 'A. Writer'), ('Other', 'Someone')])
        self.assertEqual(ext.dependencies[0]['version'], '2.4')

    def test_nested_conditional_scope(self):
        ext = parse('''Book A (for use with First by Writer)
Chapter B (for use without Second by Writer)
Include Nested by Writer.
Chapter C
Include Parent by Writer.
Book D
Include Always by Writer.''')
        deps = [d for d in ext.dependencies if d['kind'] == 'include']
        self.assertEqual([len(d['conditions']) for d in deps], [2, 1, 0])
        self.assertEqual(deps[0]['conditions'][1]['present'], 'false')
        self.assertEqual(len([d for d in ext.dependencies if d['kind'] == 'integration']), 2)

    def test_missing_punctuation_retains_dependency_and_warns(self):
        ext = parse('Include Real by Someone\n\nSection Next\n')
        self.assertEqual(ext.dependencies[0]['author'], 'Someone')
        self.assertEqual(len(ext.warnings), 1)

    def test_malformed_include_fails(self):
        with self.assertRaises(ValueError):
            parse('Include mystery.\n')

    def test_legacy_encoding_and_header_qualifiers(self):
        ext = parse_extension('A/X.i7x', b'Version 2 of X (for Glulx only) by A begins here.\n"caf\xe9"\nX ends here.')
        self.assertEqual((ext.title, ext.qualifiers, ext.encoding), ('X', 'for Glulx only', 'windows-1252'))

    def test_unversioned_header_and_legacy_version(self):
        ext = parse_extension('A/X.i7x', b'X by A begins here.\nX ends here.')
        self.assertEqual(ext.version, '')
        self.assertEqual(version_tuple('6/040426'), (6, 0, 40426))

    def test_matching_author_and_version_constraints(self):
        candidates = [parse('', title='Real', version=v) for v in ['2.3', '2.7.2', '3']]
        for number, candidate in enumerate(candidates):
            candidate.path = f'Writer/Real-{number}.i7x'
        index = {candidates[0].key: candidates}
        result = resolve({'title': 'REAL', 'author': ' writer ', 'version': '2.4'}, index)
        self.assertEqual(result, {'status': 'internal', 'targets': candidates[1].id})
        self.assertEqual(len(resolve({'title': 'Real', 'author': 'Writer'}, index)['targets'].split()), 3)
        self.assertEqual(resolve({'title': 'Real', 'author': 'Other'}, index)['status'], 'external')
        self.assertEqual(resolve({'title': 'Real', 'author': 'Writer', 'version': '4'}, index)['status'], 'version-mismatch')

    def test_url_encoding_recursive_discovery_and_determinism(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            p = root / 'A B' / 'nested' / "Café's & Stuff.i7x"
            p.parent.mkdir(parents=True)
            p.write_bytes(b'X by A begins here.\nX ends here.')
            first = generate(root, 'owner/repo', 'feature/catalog')
            self.assertEqual(first, generate(root, 'owner/repo', 'feature/catalog'))
            download = ET.fromstring(first).find(f'{Q}extension/{Q}download')
            self.assertIn('feature%2Fcatalog/A%20B/nested/Caf%C3%A9%27s%20%26%20Stuff.i7x', download.get('url'))


class RepositoryTests(unittest.TestCase):
    def test_every_file_checksum_reference_and_source_line(self):
        tree = ET.fromstring(generate(ROOT, 'interactivefiction/inform7extensions', '10.1'))
        paths = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*.i7x')}
        self.assertEqual({e.get('path') for e in tree}, paths)
        ids = {e.get('id') for e in tree}
        self.assertEqual(len(ids), len(paths))
        for entry in tree:
            data = (ROOT / entry.get('path')).read_bytes()
            download = entry.find(f'{Q}download')
            self.assertEqual(download.get('sha256'), hashlib.sha256(data).hexdigest())
            self.assertEqual(int(download.get('bytes')), len(data))
            self.assertTrue(unquote(download.get('url')).endswith('/' + entry.get('path')))
            source_lines = data.decode(entry.get('encoding').replace('windows-1252', 'cp1252')).splitlines()
            for dep in entry.findall(f'{Q}dependencies/{Q}dependency'):
                line = source_lines[int(dep.get('line')) - 1].lower()
                self.assertIn('include' if dep.get('kind') == 'include' else 'for use', line)
            for tag in ['dependency', 'condition']:
                for dep in entry.findall(f'.//{Q}{tag}'):
                    targets = dep.get('targets', '').split()
                    self.assertEqual(bool(targets), dep.get('status') == 'internal')
                    self.assertTrue(set(targets) <= ids)

    def test_known_transitive_chain_and_external_identity(self):
        tree = ET.fromstring(generate(ROOT, 'interactivefiction/inform7extensions', '10.1'))
        entries = {e.get('title') + ' by ' + e.get('author'): e for e in tree}
        package = entries['Conversation Package by Eric Eve']
        self.assertEqual({d.get('title') for d in package.findall(f'{Q}dependencies/{Q}dependency')},
                         {'Conversation Nodes', 'Conversation Suggestions'})
        framework = entries['Conversation Framework by Eric Eve']
        dep = framework.find(f'{Q}dependencies/{Q}dependency')
        self.assertEqual((dep.get('title'), dep.get('status')), ('Epistemology', 'external'))


if __name__ == '__main__':
    unittest.main()
