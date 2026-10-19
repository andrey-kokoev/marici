# Neutral Ne-20: positive local-reference witness

**10P/10N/10e** passes at maximum realization origin **5** under the unchanged
reference-only-proton grammar, canonical root and original uniform subdivision.
Origin caps 3 and 4 returned UNSAT; cap 5 returned SAT and the search stopped.
The completed universes contain 87, 192 and 372 packets respectively.

The witness has 30 occupied bodies, 64 selected reader records, 63 rooted
construction operations and 36 occupied face contacts. Every contact has a
selected operation witness and every selected reader reaches an E exit.

A fresh-process checker regenerated the source universe without invoking Z3,
matched saved packets/charts/body coordinates, replayed every construction step
and prefix, and rechecked counts and the original whole-configuration audit.
Direct vertex-based contact enumeration and reverse BFS separately confirmed
all contacts and exit reachability. This shares source geometry/rules; it is
not an independent physical model.

No transport/contact law or subdivision was changed. Reference proton geometry
need not be occupied. This is a fresh target search, not a retained F-19 growth
process. No physical stability, binding energy, global coupled-field sewing,
uniqueness or minimum-record result is asserted. The negative bounds are solver
results, not independently checked formal UNSAT proofs.

## Viewer

Both selectors include **Neon-20 · local reference (origin 5)** at
`/experiments/particle-overlap-tetrahedron/vacuum.html`. Runtime source-rule
replay gates admission; intermediate display prefixes are not certified
synthesis steps. Model and browser tests passed for primary and comparison
selection, including regressions for N-15, O-16, O-17, O-18 and F-19.

## Evidence and reproduction

Evidence: `results/reference-ne20-search/verification.json`,
`D5-verification.json` (full witness) and `replay-verification.json`.
Viewer receipts/screenshots: `results/local-reference-viewer/`.

```sh
node research/strominger/checkers/search_reference_ne20.mjs
node research/strominger/checkers/check_reference_ne20.mjs
node research/strominger/checkers/export_local_reference_viewer.mjs
node research/strominger/checkers/prepare_particle_overlap_viewer.mjs
node research/strominger/checkers/check_local_reference_viewer.mjs
```
