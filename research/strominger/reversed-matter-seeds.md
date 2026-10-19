# Anti versions in the arrow collection

The collection now contains nine records: proton, neutron, electron, neutrino #1, positron, photon, antiproton, antineutron and antineutrino.

## One reversal rule

For every supplied seed generator T, use T^-1. Keep the vertex labels, metrics, seed roles and interface records unchanged. With several generators, invert each separately rather than replacing the library by one inverse composite.

| Pair | Seed operation | Result |
|---|---|---|
| Neutrino / antineutrino | ABC A -> ACB A | Same triangle; inverse cycle |
| Electron / positron | ABCDE A -> AEDCB A | Same four-simplex; inverse cycle |
| Proton / antiproton | invert both three-cycle generators | Same tetrahedral assembly |
| Neutron / antineutron | invert the simultaneous rim rotation | Same belt and reserved interfaces |

The checker retains labelled per-generator arrow tables, including fixed vertices. Every forward seed arrow has its backward counterpart. It verifies affine inverses on an affine basis, unchanged complete geometry and unchanged centroid selection. Twenty exact checks pass for the three new anti records; the existing positron has twelve passing checks.

This is seed-library reversal. The full native coefficient protocols are not replaced or silently declared reversed.

## Files

Sources: `research/strominger/inputs/relative-antiproton-candidate.json`, `relative-antineutron-candidate.json`, and `relative-antineutrino-candidate.json`.

Result: `research/strominger/results/reversed_matter_seeds.json`.
Collection: `research/strominger/results/arrow_particle_collection.json` (v3, nine records).

```sh
python research/strominger/checkers/check_reversed_matter_seeds.py
python research/strominger/checkers/build_arrow_particle_collection.py
```

The collection builder verifies input/result source hashes before assembling the nine entries. Re-running individual checks does not overwrite the collection with a smaller historical set.
