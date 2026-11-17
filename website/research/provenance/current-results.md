# Current result provenance: pinned metadata, not a new replay

<a href="/research/provenance/current-results.v2.json" target="_self">Download the compact v2 successor manifest</a> · Historical: <a href="/research/provenance/current-results.v1.json" target="_self">Download the compact v1 provenance manifest</a> · [Result summaries](/research/results/)

## Reviewed successor v2

Snapshot `current-results-publication-v2` adds **two result families and three explanation guides**, with **36 immediate source identities, 27 checker/build-source identities and 19 historical artifact identifiers**. It references the unchanged ten-family v1 snapshot by canonical JSON SHA-256; it does not rewrite, recapture or enlarge v1's pins. The publisher validates both snapshots. V2 is file metadata only, not a scientific replay, receipt/source compatibility audit or full dependency closure.

| New coverage | Verification boundary retained |
|---|---|
| [WG common-witness assembly](/research/results/source-certified-coherent-assembly) | Source-reported certified-input completion, not arbitrary native admission or physical adequacy. Compiler identities in historical artifacts are not newly executed binaries. |
| [Ramsey retained/candidate assembly](/research/results/ramsey-retained-assembly-coherence) | Scoped Cubical correspondence checks are distinct from the written unbounded exact-integer candidate theorem and its finite certificate. No new kernel certification or parent descent. |
| [November mathematical programme](/research/programs/ramsey-mathematical-programme-2026-11) | Written arguments, conditional finite heptagon certificates, counterexamples and conjectures remain distinct; three heptagon receipts do not verify the entire programme. |
| [Typed-editor/Morse explanation](/experiments/typed-wiring-development) | Development-only source/rotation/handle interpretation, not a computed atlas, gradient flow, public app release or physical geometry. |
| [Held P/E status](/experiments/pe-net-publication-status) | Current source wording/checker assume registration that the five-net public selection intentionally excludes. A historical pass does not establish present registration or native K. |

The three named rigidity/stability helpers were not located; neither was a concrete identity for the described rigidity cycle-rank JSON attachment. Reflected-simplex sibling packages are absent from the reviewed tree. The heptagon Rust frontend and its Cargo manifest/lockfile are pinned as immediate checker/build inputs. Heptagon CNF/DRAT payloads remain local artifacts, not website downloads. V2 preserves these unavailable-input boundaries rather than fabricating script, certificate or successful-run identities.

Receipt headers such as `passed`, `UNSAT` or a scoped `++` are copied historical metadata, not a new result. Recorded compiler identities differ between packets; no shared, freshly validated compiler environment is inferred. The P/E registration mismatch is an explicit compatibility limitation, not a scientific rejection. **Receipt/source compatibility is not revalidated.**

## Historical v1 selection

Snapshot `current-results-publication-v1` covers ten selected result families. It records **17 immediate source-packet identities, 17 checker-source identities and 16 historical receipt identifiers**. Compiler version/hash fields are retained only where found in the selected receipt metadata. The manifest publishes no raw scientific receipt, execution log, matrix archive or screenshot.

## What is checked during publication

The publisher checks the versioned manifest's structure, result/status bindings, checker selection and pinned source/checker digests. It rejects a missing or changed source, changed status, malformed receipt identifier or stale generated copy. Builds do not execute the scientific checkers or require the ignored receipt files to be present.

- **Source and checker hashes:** SHA-256 of UTF-8 text with CRLF/CR normalized to LF; a BOM is preserved. This explicitly supports checkout newline differences. It is not a claim about every byte used in an earlier scientific execution.
- **Historical receipt hashes:** SHA-256 of the exact captured receipt bytes, including any BOM/newlines, plus their byte sizes. The paths identify owner-local artifacts, not public download URLs.
- **Recorded compiler identities:** copied historical metadata, not newly inspected or executed binaries. Absent runtime/compiler identities are not fabricated; checker-source identity is not the same as binary/toolchain identity.
- **Capture clock:** the recorded capture time comes from the host UTC wall clock. It is not a scientific execution date or an independently verified calendar statement.

A successful metadata check means the selected publication files match their pins under the declared hash basis. It does not establish mathematical truth, authenticate an author, accept a physical interpretation or promote a source disposition.

## Selected coverage and retained limits

| Result family | Evidence reported by its source | Limit preserved in the manifest |
|---|---|---|
| [Witness continuation/admission](/research/results/witness-continuation-admission) | Safe Cubical source-relative continuation and retained higher admission. | The exact atomic presentation is excluded; arbitrary policies are not admitted. |
| [Native SU32 record comparison](/research/results/su32-native-record-comparisons) | Corrected Boolean reader/classification theorem and separate release audit. | Current-value uniqueness is not original release or physical signal execution. |
| [Ramsey readers](/research/results/ramsey-history-covariant-readers) | Coefficient theorem and finite live reader repair. | Complete semantic descent is open; coefficient and runtime claims remain separate. |
| [Dependent four-return](/research/results/coherent-dependent-four-return) | Coherent-action construction and interpretation controls. | The return fibre may be empty; no native successor is selected. |
| [Cellulation/source roles](/research/results/cellulation-order-and-source-roles) | Complete local counterexample, incomplete global search and stricter role audit. | Weaker-model nonconfluence is not a repaired strict construction; the role patch is blocked. |
| [SU32 actions/content/operations](/research/results/su32-comparison-content-and-operations) | Executable symmetry/span checks and a separate rank obstruction. | Static identification is rejected; native boundary-operation interpretation remains missing. |
| [Analytical/native pilot](/research/results/analytical-native-two-route-pilot) | Exact native transport and a bounded negative chosen analytical residual. | The intended analytical witness/boundary map is absent. |
| [Optical control/integration](/research/results/conditional-optical-control-integration) | Conditional mathematical/statistical assembly and an integration delta. | The delta is unapplied; empirical apparatus is deferred. |
| [Local contour closure](/research/results/local-contour-covariance-closure) | Ten-checker local construction audit. | The selected physical contour and global gates remain open. |
| [Atom-route transport](/research/results/atom-retained-source-transport) | Actual chart/history adapter with frame covariance and hostile controls. | Its coefficient skeleton is not a physical gauge selection or an identified T9 representation. |

This is selected immediate provenance, **not a full transitive dependency closure**. In particular, the manifest does not claim that every historical receipt was produced by today's pinned source/checker versions. **Receipt/source compatibility is not revalidated.** Negative, conditional, blocked and incomplete findings remain visible rather than being coerced into a generic “passed” label.

## Reproduction and independent inspection

For a result, find its slug in the manifest, then follow the named source packet's invocation and declared environment/toolchain. The checker-source digest fixes the script being discussed. Obtain historical artifacts separately if needed and compare their exact SHA-256 identifiers; their large payloads are intentionally not bundled with the website.

To check only this publication's metadata and generated copy:

```sh
node scripts/prepare-research-provenance-successor.mjs --check
```

To create a **metadata-only review candidate**, without overwriting the versioned config or running suppliers:

```sh
node scripts/prepare-research-provenance-successor.mjs --capture
```

The candidate is written under ignored `.ai/`, not into the versioned configuration. Inspect its sources, status bindings, receipt headers, missing inputs and compatibility limits. The optional `--accept-reviewed-candidate SHA256` command creates a new v2 file exclusively from those exact reviewed bytes and refuses to overwrite an existing config. It supplies no scientific or graph admission. A source/status change requires explicit review of a successor snapshot; do not silently refresh pins to silence a failed build or call recapture a scientific replay. The regular website preparation validates the frozen `config/current-research-provenance.v1.json`, reviewed `config/current-research-provenance.v2.json` and its editorial selection, then emits both small JSON copies. The new result pages and all three guides link here. Builds neither require historical receipt payloads nor rerun their suppliers.

No scientific checker, proof assistant, measurement or shared research disposition is executed or changed by these metadata commands.
