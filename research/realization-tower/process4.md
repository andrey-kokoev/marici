# Process 4 — seed-first assembly

Open [the normal-ray viewer](normal-ray.html) and select **Process 4 — seed-first assembly**.
This replaces the mistaken preassembled-target/chart-rotation experiment.
Its new settings namespace discards that experiment's saved progress.

## What each click does

Start with one upright unit-simplex seed at the center. Across each exposed
complete triangular face, construct the unique adjoining tetrahedral/octahedral
honeycomb item from the primitive templates. Admit only items inside the declared
k=7 envelope (every barycentric coordinate <=2).

Each round reads the previous snapshot, adds its entire admissible frontier
simultaneously and retains EVERY previously admitted face-parent. Existing cells
never move, rotate, change identity or acquire a retroactive role. The first four
seed faces initiate four branches; ancestry merges rather than choosing a
privileged first-arrival branch. Shared faces, including contacts between cells
added in the same round, are retained explicitly.

The generated additions are1 seed, then4,22,24,58,24,34,4,4 whole cells.
They produce175 whole items comprising343 primitive tetrahedra. Those numbers
are outputs, not constructor quotas. The completed geometry is compared against
the independent esd7 component constructor ONLY in the tests.

## Boundary

This constructs the retained geometric carrier, not yet the Pb particle binding.
No completed Pb loadout,82/126 assignment policy, matching table or coordinate
permutation is used as input. Neutral cell colors are geometry, not P/N/E labels.
The k=7 envelope is an explicit input, not a derived isotope selection.

At the completed envelope the process stops. Native whole-body carrier bindings,
marked-contact compatibility, physical role assignment and higher witnesses
remain to be supplied. The four branch ancestries are not asserted to be four
28-step physical histories. No particle formation or stability result is claimed.

## Verify

```sh
node --test tests/retained-pb-process.test.mjs
node scripts/prepare-normal-ray.mjs
node scripts/test-process4.mjs
```

Tests cover a one-cell initial state, immutable prefixes, complete-face parents,
four branch starts, traversal-order independence, no duplicate items, independent
final geometry comparison, role-claim boundaries and saved-progress isolation.
