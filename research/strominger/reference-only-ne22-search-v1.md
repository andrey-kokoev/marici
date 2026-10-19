# Neutral Ne-22 and the Ne-20/21/22 comparison

**10P/12N/10e** passes at maximum realization origin **4** under the unchanged
reference-only-proton grammar, canonical root and original uniform subdivision.
Origin cap 3 returned UNSAT; cap 4 returned SAT and the search stopped.

The witness has 32 occupied bodies, 68 selected reader records, 67 rooted
construction operations and 37 occupied face contacts. Every contact has a
selected operation witness and every selected reader reaches an E exit.

Fresh-process replay regenerated the universe without Z3, matched saved
packets/charts/body coordinates, replayed every construction step/prefix and
rechecked exact counts and whole-configuration inspection. Direct vertex-based
contact enumeration and reverse BFS confirmed contacts and exit reachability.

## Comparison

| Isotope | Neutral counts | Nuclear spin | Current fixed-grammar result |
|---|---|---|---|
| Ne-20 | 10P/10N/10e | 0 | Witness at origin 5 |
| Ne-21 | 10P/11N/10e | 3/2 | UNSAT through origin 9; origin 10 untested |
| Ne-22 | 10P/12N/10e | 0 | Witness at origin 4 |

Ne-21 is a bounded missing member between two passing neighbors. The larger
Ne-22 target succeeds at a smaller origin than Ne-20, so difficulty does not
simply grow with particle count. This does not establish an odd-neutron rule:
O-17 (nine neutrons) already passes. Nuclear spin is not a constraint or derived
quantity in this generator.

The searches are independent targets, not retained-prefix growth. A candidate
next comparison is deleting each neutron from Ne-22 and checking whether the
resulting Ne-21 configurations lose contacts, exits or rooted construction,
as was done for N-15 to N-14. That deletion audit is not part of this result.

## Viewer and scope

Both selectors include **Neon-22 · local reference (origin 4)** at
`/experiments/particle-overlap-tetrahedron/vacuum.html`. Runtime source-rule
replay gates display. Model/browser checks passed for primary/comparison
selection and all previously added local references. Ne-21 remains unlisted.

No transport/contact law or subdivision was changed. Reference proton geometry
need not be occupied. These are local construction certificates, not binding
energy or global coupled-field sewing results. No minimum-record or unique
geometry claim is made. Negative bounds are solver results, not independently
checked formal UNSAT proofs.

## Evidence and reproduction

Evidence: `results/reference-ne22-search/verification.json`,
`D4-verification.json` (full witness) and `replay-verification.json`.
Viewer receipts/screenshots: `results/local-reference-viewer/`.
Ne-21 origin-9 retry: `results/reference-ne21-search/origin9-600s/verification.json`.

```sh
node research/strominger/checkers/search_reference_ne22.mjs
node research/strominger/checkers/check_reference_ne22.mjs
node research/strominger/checkers/export_local_reference_viewer.mjs
node research/strominger/checkers/prepare_particle_overlap_viewer.mjs
node research/strominger/checkers/check_local_reference_viewer.mjs
```
