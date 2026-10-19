# Neutral F-19: positive local-reference witness

**9P/10N/9e** passes at maximum realization origin **4** under the unchanged
reference-only-proton grammar, canonical root and original uniform subdivision.
Origin cap 3 returned UNSAT; cap 4 returned SAT and the search stopped.

The witness has 28 occupied bodies, 51 selected reader records, 50 rooted
construction operations and 32 occupied face contacts. Every contact has a
selected operation witness and every selected reader reaches an E exit.

A fresh-process checker regenerated the source universe without invoking Z3,
matched saved packets/charts/body coordinates, replayed every construction step
and prefix, and rechecked counts and the original whole-configuration audit.
Direct vertex-based contact enumeration and reverse BFS separately confirmed
all contacts and exit reachability. This shares source geometry/rules; it is
not an independent physical model.

No transport/contact law or subdivision was changed. Reference proton geometry
need not be occupied. This is a fresh target search, not a retained O-18 growth
process. No physical stability, binding energy, global coupled-field sewing,
uniqueness or minimum-record result is asserted. The origin-3 negative is a
bounded solver result, not an independently checked formal UNSAT proof.

## Viewer

Both selectors include **Fluorine-19 · local reference (origin 4)** at
`/experiments/particle-overlap-tetrahedron/vacuum.html`. Runtime source-rule
replay gates admission; intermediate display prefixes are not certified
synthesis steps. Model and browser tests passed for primary and comparison
selection, including regressions for N-15, O-16, O-17 and O-18.

## Evidence and reproduction

Evidence: `results/reference-f19-search/verification.json`,
`D4-verification.json` (full witness) and `replay-verification.json`.
Viewer receipts/screenshots: `results/local-reference-viewer/`.

```sh
node research/strominger/checkers/search_reference_f19.mjs
node research/strominger/checkers/check_reference_f19.mjs
node research/strominger/checkers/export_local_reference_viewer.mjs
node research/strominger/checkers/prepare_particle_overlap_viewer.mjs
node research/strominger/checkers/check_local_reference_viewer.mjs
```
