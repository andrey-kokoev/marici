# Neutral O-16: positive local-reference witness

Viewer follow-up: this witness is now available as **Oxygen-16 · local reference
(origin 4)** in both selectors. Runtime source-rule replay gates display;
prefixes are display-only, not certified synthesis. Browser checks and
screenshots: `results/local-reference-viewer/`.

A **8P/8N/8e** reference exists at maximum realization origin **4** under the
unchanged prior reference-only-proton grammar and original uniform subdivision.
Origin cap 3 returned UNSAT; cap 4 returned SAT and the search stopped.
No mixed subdivisions or new particle/contact laws were introduced.

The witness has **24 occupied bodies**, **49 selected reader records**, a rooted
construction word of **48 operations**, and **28 occupied face contacts**.
All contacts have selected operation witnesses; every selected reader can
reach an E exit. Multiple readers on one cell do not count as extra particles.

The search checked exact counts and original whole-configuration inspection,
then reconstructed and validated every construction prefix. A fresh-process
checker regenerated the finite universe without invoking Z3, compared saved
packets/charts and body coordinates, replayed every step, and rechecked the
original contact/exit certificate. Direct vertex-based face-contact enumeration
and a separate reverse BFS confirmed all 28 contacts and all-record exit
reachability. This replay shares the original geometry/rule implementation.

This is a local representation for neutral oxygen-16, **not** a derivation of
its physical stability, binding energy or global coupled-field sewing. Reference
proton geometry need not be occupied. No uniqueness or minimum-record claim is
made. The origin-3 negative is a bounded solver result, not an independently
checked formal UNSAT proof. The search itself left production/viewer and prior isotope evidence
unchanged; the O-16 search does not require retaining an N-15 prefix.

## Reproduction

```sh
node research/strominger/checkers/search_reference_o16.mjs
node research/strominger/checkers/check_reference_o16.mjs
```

Evidence in `results/reference-o16-search/`:
- `verification.json`: target, source hashes and bounded search summary;
- `D4-verification.json`: complete positive witness and construction;
- `D3-solver.json`, `D4-solver.json`: solver receipts;
- `replay-verification.json`: fresh replay, hashes and contact audit.
