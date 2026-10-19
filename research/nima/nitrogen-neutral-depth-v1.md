# Seven-electron nitrogen searches and visual atlas

[Open the atlas](results/assembly-atlas/index.html) · [Open the nitrogen witness gallery](results/assembly-atlas/nitrogen.html)

## Deeper search results

All searches start from the marked seed, with exact occupied-body counts and unrestricted placement/history within the stated maximum origin. They require the existing local contact/selected-record exit certificate, not a physical stability condition.

| Nuclear/electron composition | Maximum origin | Result | Search nodes |
|---|---:|---|---:|
| 7P/7N/7e | 3 | UNSAT under the compiled local model | 33 |
| 7P/8N/7e | 3 | UNSAT under the compiled local model | 33 |
| 7P/7N/7e | 4 | UNSAT under the compiled local model | 269,123 |
| 7P/8N/7e | 4 | SAT, directly replayed and checked | 41 |
| 7P/7N/7e | 5 | **Incomplete: 60-second search limit** | 519,870 |

D5 was searched only for the still-unresolved N14 composition. The exact visited-node count at a wall-time stop can vary between runs. The resource guard is not an origin budget, and its stop is not evidence of absence.

The D4 N15-composition witness contains **7 protons, 8 neutrons, 7 electrons, 38 retained records and 37 representative construction operations**, with maximum origin4. Every prefix is compatible under the original whole-state guard; its final state has all contacts witnessed and every selected record can reach an E exit. This establishes a reference construction with neutral atom counts, **not** a stable neutral atom, nuclear binding energy, physical clock, or globally sewn coupled field.

The D4 N14 negative result is exhaustion of the declared CNF/cardinality search, not an external proof-assistant or independent SAT-solver certificate. The shared compiler/solver has truth-table/cardinality controls and reproduces all 1/14/459 exit-certified packet selections for D0/D1/D2. Those regressions were freshly rerun after exporting the reusable search functions and adding the time guard. Both node-limit and time-limit controls explicitly return `incomplete`, never UNSAT.

## Visual atlas

The new atlas landing page links:

1. The unchanged **complete D0–D2 configuration explorer**.
2. A **witness-only gallery** with ten saved D3 nitrogen-composition placements and the D4 seven-electron N15 witness.

The gallery includes budget/composition filters, electron visibility, actual primitive-coordinate projection, selected-record charts and maps, operation replay, independently checked prefix certificate flags, and the earlier-footprint comparisons for D3 examples. The operation index is displayed separately from maximum origin. Empty filters are not labelled as absence results.

No claim is made that the gallery exhausts D3/D4 placements. A D5 search-limit status is visible without fabricating a D5 witness.

Browser verification passed for all **11 witnesses and 315 construction prefixes**, including forward/backward replay, full-state restoration, electron visibility, the empty D4/N14 filter, and the 37-operation D4 witness. No page errors occurred. Every displayed prefix was also replayed headlessly against the original construction guards before generating the page.

## Reproduction and receipts

```sh
node research/nima/checkers/check_nitrogen_alternative_placements.mjs
node research/nima/checkers/check_nitrogen_neutral_depth.mjs
node research/nima/checkers/build_nitrogen_witness_gallery.mjs
node research/nima/checkers/check_nitrogen_witness_gallery_browser.mjs
```

- [Depth search receipt and registries](results/nitrogen-neutral-depth/verification.json)
- [Gallery source replay and hashes](results/assembly-atlas/gallery-verification.json)
- [Browser receipt](results/assembly-atlas/browser-verification.json)
- [Earlier D3 alternative-placement results](nitrogen-alternative-placements-v1.md)

The old complete atlas and base reference rules were not modified. The new landing page makes the higher-depth witness extension explicit rather than silently enlarging the complete family claim.
