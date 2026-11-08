# Extension download catalog

[`extensions.xml`](extensions.xml) is the complete download and dependency index
for the `.i7x` files in this repository's Inform 10.1 branch.
[`extensions.xsd`](extensions.xsd) defines its XML Schema 1.0 format. Consumers
need only the XML: URLs, identities, constraints, and internal references are
embedded in it. The XSD is an optional development-time validation resource.
This catalog describes downloads; it does not describe installation.

After these files are committed and pushed to the `10.1` branch, applications
can fetch the catalog at:

```text
https://raw.githubusercontent.com/interactivefiction/inform7extensions/10.1/catalog/extensions.xml
```

## XML contract

The namespace is `urn:inform7:extension-catalog:1`. XML queries must account for
that default namespace. Reject unsupported `schema-version` values.

| Element / attribute | Meaning |
| --- | --- |
| `catalog/@schema-version` | Format version, currently `1`. |
| `catalog/@repository`, `@ref`, `@url` | GitHub repository, source branch/tag/commit, and catalog URL. |
| `catalog/@language-version`, `@version-policy` | `10.1` and `inform-10-compatible`; these describe this branch's intended language and version comparison policy, not a compilation guarantee. |
| `catalog/@generator` | Repository path of the generator. |
| `extension/@id` | Unique opaque file identity, derived from its repository-relative path. Stable across content edits, changes on rename. |
| `extension/@title`, `@author`, `@version` | Declared source-header metadata. Version is omitted when undeclared; filenames are not authoritative versions. |
| `extension/@qualifiers` | Optional header restrictions, such as `for Glulx only`, preserved as text. |
| `extension/@path`, `@folder` | Relative source path and containing folder; nested folders are supported. |
| `extension/@encoding` | Source encoding (`utf-8` or legacy `windows-1252`); downloaded bytes must be preserved. |
| `download/@url` | Absolute HTTPS raw-file URL with path characters percent-encoded. Usable directly by wget or an HTTP client. |
| `download/@filename` | Suggested download filename. Use `extension/@path` to avoid collisions between authors/folders. |
| `download/@bytes`, `@sha256` | Exact original file length and lowercase SHA-256 checksum. |
| `dependencies` | Direct references only, possibly empty. Transitive dependencies are obtained by traversing entries. |
| `dependency/@title`, `@author` | Referenced extension identity, including references absent from this repository. |
| `dependency/@kind` | `include` is an explicit Include declaration; `integration` is an optional heading reference. |
| `dependency/@line` | One-based source line of the declaration or conditional heading. |
| `dependency/@when` | For integrations only: `with` or `without`. Neither makes the referenced package a required download. |
| `@requested-version` | Source spelling of a requested version, when present. |
| `@min-version`, `@max-version-exclusive` | Numeric lower-inclusive / upper-exclusive bounds, when a version is requested. |
| `@status` | `internal`, `external`, or `version-mismatch`, as defined below. |
| `@targets` | Space-separated candidate extension IDs for `internal` references only. All candidates satisfy this individual reference. |
| `dependency/condition` | An enclosing conditional heading for an Include. Uses the same reference attributes, plus boolean `present`. All conditions must hold. |
| `extension/warning` | Extraction caveat, with one-based `@line`; consumers should make this visible. |

An `internal` reference has at least one matching downloadable entry. An
`external` reference has no matching title **and author** in this repository.
A `version-mismatch` has matching identities but no compatible version.
External and mismatched references have no `targets` and no invented download
URL. The application/user must supply them or report an incomplete download
plan. Some external references may already be provided by the user's Inform
environment; this catalog does not assume that they are available.

For example, Commonly Unimplemented includes Smarter Parser:

```xml
<dependency xmlns="urn:inform7:extension-catalog:1"
  title="Smarter Parser" author="Aaron Reed" kind="include" line="9"
  requested-version="16" min-version="16.0.0" max-version-exclusive="17.0.0"
  status="internal" targets="ext-4e818abd0922eea9bb96847e" />
```

The target entry supplies its own download URL and dependencies. By contrast,
`Basic Screen Effects by Emily Short` is explicitly marked `external`; a
similarly named file or a different author is not substituted.

## Dependency resolution by an application

1. Index entries by `id`, and package identities by normalized `(title, author)`.
   Normalize Unicode to NFC, collapse whitespace, and case-fold both fields.
   Do not infer identity from a filename, folder, or title alone.
2. Start with the user's chosen extension(s). Follow `kind="include"` edges;
   use a visited set to avoid repeated traversal and infinite loops in cycles.
   Do not follow `kind="integration"` edges automatically. `when="without"`
   describes fallback code, not a conflict or a negative dependency.
3. Intersect the constraints from **all** active incoming Includes for each
   package identity. Choose one candidate satisfying that intersection, not one
   independently per edge. Multiple suitable candidates need a deterministic
   policy (for example, highest compatible version); equal-version files may
   require user selection. Report an empty intersection as a conflict.
4. If an Include has `condition` children, activate it only when all conditions
   hold for the final selected/provided package set. `present="true"` requires
   the named package; `present="false"` requires its absence. A condition is
   a predicate, not an instruction to fetch that package. Re-evaluate after
   package selection changes, retract edges that cease to apply, and reject
   inconsistent or oscillating selections. Ask the caller about externally
   provided packages when their presence is unknown. A resolver using only
   unconditional Includes is sufficient for the current catalog, but should
   detect conditional Includes before claiming a complete plan for future data.
5. Collect unresolved **active Includes** and version conflicts with their
   source paths/lines. Optional integrations alone do not make the plan
   incomplete. External resolution, including any external package's own
   dependencies, belongs to the caller. Download each selected internal file
   once and verify both its length and SHA-256 checksum. A graph cycle does not
   require repeated downloads; this catalog prescribes no installation order.

For example, Conversation Package → Conversation Nodes → Conversation Responses
→ Conversation Framework → external Epistemology. Following only the first
entry's immediate dependencies would miss part of the download closure.

Inform 10 version requests use a lower bound within the same major version:
`2.4` permits `2.4.0` through versions below `3.0.0`, not version `3`.
Missing numeric components are zero; legacy `6/040426` means `6.0.40426`.
Compare integer components, never strings. An unversioned Include accepts any
version, including an undeclared version. These rules follow Inform's
[version numbering documentation](https://ganelson.github.io/inform-website/book/WI_27_6.html)
and [combined dependency constraints](https://ganelson.github.io/inform-website/book/WI_27_8.html).

## Downloading from a VS Code terminal

For any selected entry, pass `download/@url` as a quoted argument and choose an
output path. For example:

```sh
wget --output-document='Commonly Unimplemented-v2.i7x' 'https://raw.githubusercontent.com/interactivefiction/inform7extensions/10.1/Aaron%20Reed/Commonly%20Unimplemented-v2.i7x'
```

An extension application can make an HTTPS GET itself; wget is not required by
the format. Pass process arguments separately instead of evaluating catalog
text as a shell command. When preserving `path`, keep it within the chosen
download directory. Public repository URLs need no credentials.

The default URLs track a branch and can change. On checksum mismatch, refresh
the catalog and resolve again; never accept different bytes silently. For a
frozen catalog, generate with a published commit SHA as `--ref`. This pins file
URLs to that snapshot. `catalog/@url` exists at that ref only if the snapshot
contains the catalog at its conventional path; an artifact generated against
an earlier source commit must be distributed separately. The catalog checksum
is an integrity check, not a signature.

## Regenerating and validating

From the repository root, using Python 3.10 or newer (no Python dependencies):

```sh
python3 tools/generate_catalog.py
python3 tools/generate_catalog.py --check
python3 -m unittest discover -s tests -v
xmllint --noout --schema catalog/extensions.xsd catalog/extensions.xml
```

The last command is optional locally and requires `xmllint`; CI runs it.
Generation recursively scans non-hidden folders for `.i7x` files, including
uppercase suffixes, and writes `catalog/extensions.xml`. Output is sorted by
relative path and omits timestamps so unchanged inputs produce identical XML.
`--check` exits nonzero if the file is missing or stale. Commit the generated XML
alongside source changes. The generator itself performs no downloads.

For a fork or another reference:

```sh
python3 tools/generate_catalog.py --repository OWNER/REPO --ref BRANCH_OR_COMMIT
```

Use `--root` to scan another checkout and `--output` to select another output
file (relative paths are resolved against `--root`). The default repository is
`interactivefiction/inform7extensions` and ref is `10.1`. URL customization
does not change the parser's Inform 10 version policy; this tool does not
implement pre-2022 version resolution. When adopting the generator in a fork,
update its defaults if the fork's checked-in catalog should reference that fork.

The [Extension download catalog workflow](../.github/workflows/extension-catalog.yml)
supports **Actions → Extension download catalog → Run workflow**. It runs tests,
regenerates for the selected repository and ref, validates the XSD, and uploads
an `extension-catalog` artifact containing XML, XSD, and this document. Download
the artifact and commit its XML to update the repository catalog. The workflow
has read-only repository permission and does not push commits. Pull requests
affecting catalog inputs also run tests and reject stale checked-in XML.
GitHub requires a dispatchable workflow on the default branch; see its
[manual workflow documentation](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/manually-running-a-workflow).

## Extraction scope and limitations

The generator reads header metadata, explicit Inform 7 Include declarations,
and `for use with/without TITLE by AUTHOR` headings. It ignores nested comments,
quoted text, embedded Inform 6 code, and documentation examples. Conditional
scope follows Volume → Book → Part → Chapter → Section. Versioned references
and multiline Includes are supported. Unsupported Include references fail
generation rather than silently creating an empty dependency list.

This is a source scanner, not an Inform compiler. It cannot discover undeclared
requirements mentioned only in prose, runtime assets, or libraries hidden in
embedded Inform 6. Other heading restrictions (such as target VM restrictions)
are not evaluated; their Includes are conservatively collected. Header
qualifiers remain available for a caller's compatibility checks. A dependency
reference proves a source declaration, not successful compilation.

Currently, `Autoundo for Object Response Tests` has an Include without terminal
punctuation. The scanner recovers it at the following blank line and emits a
warning in the XML. One file, `Questions IT`, uses legacy Windows-1252 decoding;
its checksum and download size still describe the original bytes.
