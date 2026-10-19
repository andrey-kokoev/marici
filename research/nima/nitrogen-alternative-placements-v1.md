# Alternative nitrogen-composition placements at D3

## Result

Searching from the seed, without fixing any D2 nuclear footprint or retaining a D2 selection, finds locally exit-certified constructions for both nuclear compositions:

| Nuclear composition | Coordinate-distinct certified footprints saved | Electrons in saved witnesses | Representative operation lengths |
|---|---:|---|---|
| 7P/7N (N14 composition) | 5 | 3 or 4 | 24 or 27 |
| 7P/8N (N15 composition) | 5 | 3, 4 or 5 | 24, 27 or 30 |

All ten have maximum absolute origin3. Every contact is witnessed and every selected record reaches a selected E exit. Each is independently replayed from the seed with a valid whole configuration at every prefix. These are **local reference-construction certificates**, not nuclear binding, physical atom, or global coupled-field sewing certificates.

The search stopped intentionally after five distinct nuclear footprints in each case. Five is a lower bound, not the number of all solutions. Footprints are distinguished in the fixed seed coordinate system; rotations/reflections have not been quotiented out.

## Structural comparison

For each saved witness, the receipt compares its species-labelled nuclear cells against all previous N14 footprints, or all previously tested immediate N15 extension footprints.

The first successful N14 and N15 examples differ from their nearest old footprints by replacing **two occupied nuclear sites: one proton site and one neutron site**. Across the saved examples the smallest such difference is two or three sites. Thus the successful examples do not merely repair the old selected histories or append a terminal neutron to the old geometry.

This is a set difference between independently generated placements, **not** an allowed physical motion/rearrangement operation. It does not prove that two relocations are globally minimal over all possible certified solutions, nor that the change alone causes certification independent of the changed history/electron placement.

The original fixed-footprint obstruction and the new positive examples are compatible:

- retaining old nuclear placement and old records: all 720 tested parent/extension cases fail completion through D3;
- allowing another placement/history generated from the seed: certified 7P/7N and 7P/8N examples exist at D3.

The distinction suggested by the literature—connectivity and occupation geometry rather than particle count alone—therefore yields a useful discriminating test, without importing its speculative physics.

## Search and verification

The complete D3 packet universe has 87 packets. The compiler uses:

- Boolean selection variables for packets, retaining absolute origin, chart and full coefficient map;
- occupied-body variables for exact nuclear counts (not packet multiplicities);
- exact pairwise compatibility guards;
- root support on verified singleton/native-PN components with acyclic condensation;
- optional selected-record exit support and all face-contact witness requirements.

The exit-certified CNF has 250 variables and 924 clauses, plus exact body-cardinality constraints. A bounded DPLL solver propagates clauses and exact cardinalities. Nuclear-footprint blocking clauses produce alternatives rather than more histories of the same placement. The compatibility-only comparison also saves five footprints per composition; those sampled constructions have no selected electrons and are not certified.

Validation:

1. 256 three-variable CNF truth-table cases and 96 cardinality/unit-assignment controls.
2. Native D0 positive and negative controls.
3. Complete packet-selection enumeration with the new solver reproduces **1, 14 and 459** exit-certified selections at D0, D1 and D2, respectively. Every returned selection is replayed and checked against the original whole-state inspector.
4. All ten new certified witnesses and ten compatibility-only witnesses replay from the root. Every construction prefix is checked; exact final counts and applicable exit conditions are asserted.

Separate exact-cardinality searches for **7P/7N/7e** and **7P/8N/7e** return unsatisfiable under the D3 local-exit compiler, each exhausting its search in 33 nodes. This is a model/budget-relative negative result, not a physical exclusion of neutral nitrogen. The saved positive witnesses have fewer than seven electrons.

No operation-count bound is used. The one-million-node search resource guard is distinct from the origin budget; it was not reached. The full D3 family has not been enumerated or counted.

## Artifacts

- [Checker](checkers/check_nitrogen_alternative_placements.mjs)
- [Receipt with selected packets, construction words, nuclear sites, nearest-old-footprint differences, full registry, regressions and source hashes](results/nitrogen-alternative-placements/verification.json)
- [Earlier fixed-footprint test](nitrogen-contact-extensions-v1.md)

```sh
node research/nima/checkers/check_nitrogen_alternative_placements.mjs
```

The final headless run passed. Existing D0–D2 atlas files and underlying reference rules were not changed; these D3 witnesses are separate artifacts, not silently inserted into that atlas.
