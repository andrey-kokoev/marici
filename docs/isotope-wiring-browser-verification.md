# Isotope wiring — current browser verification

## Recorded working-tree checkpoint

The current Neutron-only legacy-editor matrix completed **30/30 automated runs**, with zero failures and zero unrun cases, during website currency iteration 3. This is ten distinct current-contract cases on each of:

| Engine | Observed version |
|---|---|
| Chromium | 151.0.7922.34 |
| Firefox | 153.0 |
| WebKit | 26.5 |

The run used Node v24.19.0 and Playwright 1.62.1 on Windows. Its base commit is `3ace86e33`, with an explicitly dirty working tree; **that commit alone does not identify the tested source**. Exact tested byte hashes, per-case engine versions and diagnostic-log identities are retained in `config/isotope-wiring-browser-evidence.v1.json`. Run ID: `6fe2eda2-6376-49d8-bd32-7507e7e6d27e`. The host-clock timestamp in that record is not an independently verified calendar or scientific execution date.

The delivered self-contained HTML, embedded snapshot, host wrapper, matrix and case-script identities were unchanged during the run. This is a declared fingerprint set, not a complete transitive-dependency or authenticity certificate. Detailed local logs remain under `.ai/isotope-browser-matrix/<run-id>/`; only their byte identities and compact results are retained in the reviewed evidence config.

## Coverage

`config/isotope-wiring-browser-matrix.v1.json` owns the ten cases and their scope:

1. Reachable HTTP requests are blocked while the local self-contained file loads.
2. Read-only authored drawings, absent SVG routing/overlays and visible keyboard Inspect at 1440px/390px.
3. Removed EP controls, old preference/reference migration, Definition-only Undo, project reload, missing/throwing structural runtime and failed-storage feedback.
4. Reference provenance labels, preferences, missing data, export provenance, mobile bounds and denied local storage.
5. Pinned Ne-20 Turtle inventory, exact download, edited-inventory mismatch and corrupt/missing snapshot refusal.
6. Catalog filtering, complete captions, persistence and desktop/mobile empty-result recovery.
7. Stationary mouse/keyboard catalog selection, remembered scrolling and reload recovery.
8. Current panel/selection/camera/format persistence, custom-definition recovery and malformed/denied storage.
9. Actual built-site navigation and iframe, current read-only controls, keyboard entry, retained text across host theme changes, full-window route and byte-exact downloadable HTML.
10. Definition replay, metadata deletion, exact export/fresh-context import/reload, retained unapplied drafts/discard and cyclic-update refusal. Placement and survey functions are checked through the delivered isolated JSON/data bridge; **no placement-dialog UI is claimed**.

The first complete attempt had 29 passes and one WebKit failure: the new import test reloaded before the UI reported completion of its IndexedDB write. Waiting for the existing **Definitions saved in this browser** signal corrected the test's persistence boundary; no arbitrary delay or application storage change was used. A fresh complete rerun, not a combination of partial passes, produced the recorded 30/30 result.

## Why this is not the historical 33-run result

The earlier runner used eleven cases per engine, including retired EP editing, canvas-difference overlays and placement dialogs. Its first recorded source report is `c1025e302`, without exact tested-source/engine provenance. The fresh old-runner reproduction fails in its legacy standalone workflow. That report remains historical, not current acceptance.

The replacement follows the pre-existing Neutron-only contract in `examples/isotope-wiring/UI-REVIEW.md` and the [regression contract review](isotope-wiring-regression-contract.md). It preserves the meaningful storage, replay, export, source-isolation, missing-runtime, corrupt-data and network failure controls without reintroducing removed mechanisms. Ten current cases are not equivalent to eleven historical cases; the counts must not be merged.

## Reproduce and qualify results

After building the publication with the installed dependencies and declared inputs:

```sh
node scripts/test-isotope-wiring-browsers.mjs
node scripts/check-isotope-wiring-browser-evidence.mjs
```

The matrix runs sequentially and records a JSON report and per-case logs. Missing engines and failed cases fail the run; remaining cases after a failure are recorded as unrun, not passed. Source drift invalidates the report. Engine versions from each child are checked against the observed preflight version.

For diagnosis only:

```sh
node scripts/test-isotope-wiring-browsers.mjs webkit --case=definition-model-workflows
```

A successful subset is explicitly `partial_pass`, never a full matrix pass. Unit controls reject missing/duplicate/unrun/failed cases and source drift. The evidence checker validates the recorded coverage and current matching raw bytes; **it does not replay browsers**. If source identities no longer match, inspect the change and perform an appropriate new run rather than editing hashes to silence the check. Preserve prior evidence when recording a successor checkpoint.

## Limits

- These are automated desktop engines and emulated viewport sizes, not shipping Safari/iOS/Android, real-device, screen-reader, performance or universal accessibility acceptance.
- Keyboard/mouse interaction is checked; this record does not certify multi-touch or every pointer device.
- WebKit's Windows native offline mode rejects local-file navigation. Its file cases instead abort HTTP(S) through routing, with an independent reachable-server isolation control. This is not represented as a passing native-offline file test.
- Built-site checks use the local production output, not the deployed Worker. Live release verification remains task T14.
- The separate typed Vue application's authored routing and Morse model have separate checks. This matrix establishes neither their equivalence to legacy behavior nor physical isotope adequacy, scientific source admission or formal correctness.
