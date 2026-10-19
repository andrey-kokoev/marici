# Neutral N-15: positive local-reference witness

Viewer follow-up: this witness is now available as **Nitrogen-15 · local
reference (origin 4)** in both selectors. The older N-15 phase-reference option
is preserved separately. Runtime source-rule replay gates display; prefixes
are display-only, not certified synthesis. Browser checks and screenshots:
`results/local-reference-viewer/`.

## Result

A **7P/8N/7e** reference exists at maximum realization origin **4** under the
unchanged prior reference-only-proton grammar and original uniform subdivision.
Origin cap 3 returned UNSAT; origin cap 4 returned SAT and the search stopped.
No mixed-diagonal rules or additional particle/contact laws were needed.

The witness has 22 occupied bodies, 44 selected reader records and a rooted
construction word of 43 operations. All 25 occupied face contacts have actual
selected operation witnesses. Every selected record can reach an E exit.
Multiple readers on a cell count as one body, not additional particles.

This is a local representation/certificate for neutral nitrogen-15, not a
calculation of its experimentally known physical stability. Global coupled-field
sewing, binding energies and synthesis dynamics remain outside this test.
Reference-only proton geometry is allowed and need not always be occupied.

## Validation

The targeted solver used fresh complete fixed-subdivision packet universes:
87 packets at origin cap 3 and 192 at cap 4. The exact target was 7 protons,
8 neutrons and 7 electrons. Compatibility, actual contact witnesses, rooted
construction and selected-record exit reachability retain the prior checks.

The search replayed the selected set through the unchanged original rules,
validated each construction prefix and saved packets, charts, body coordinates,
operations, inspection and input/source hashes.

A separate fresh-process checker regenerated the universe and replayed the
saved witness without invoking Z3. It checked every saved packet/chart against
the source generator, every construction step and prefix, the exact 7/8/7
counts and original whole-configuration inspection. In addition, direct
vertex-intersection enumeration found all 25 occupied face contacts and their
operation witnesses, and a reverse graph traversal independently checked
exit reachability for all 44 selected records. The checker shares the original
geometry/rule implementation; this is not an independent physical model.

No minimal-record or unique-geometry claim is made. The bounded origin-3
negative is a solver result, not an independently checked formal UNSAT proof.
The search itself did not change production/viewer or other-owner sources. N-14 work remains
paused; this witness does not resolve its open mixed-subdivision origin-7 query.

## Reproduction and evidence

```sh
node research/strominger/checkers/search_reference_n15.mjs
node research/strominger/checkers/check_reference_n15.mjs
```

Evidence under `results/reference-n15-search/`:

- `verification.json`: completed search summary and source hashes;
- `D4-verification.json`: full positive witness and construction;
- `D3-solver.json`, `D4-solver.json`: solver receipts;
- `replay-verification.json`: fresh replay and explicit contact audit.
