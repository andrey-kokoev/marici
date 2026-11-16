# Current result provenance: pinned metadata, not a new replay

<a href="/research/provenance/current-results.v1.json" target="_self">Download the compact v1 provenance manifest</a> · [Result summaries](/research/results/)

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
node scripts/prepare-current-research-provenance.mjs --check
```

To create a **metadata-only review candidate**, without overwriting the versioned config or running suppliers:

```sh
node scripts/prepare-current-research-provenance.mjs --capture
```

The candidate is written under ignored `.ai/`. A source/status change requires explicit review of a successor snapshot; do not silently refresh pins to silence a failed build or call recapture a scientific replay. The regular website preparation validates `config/current-research-provenance.v1.json` and emits the small generated JSON copy.

No scientific checker, proof assistant, measurement or shared research disposition is executed or changed by these metadata commands.
