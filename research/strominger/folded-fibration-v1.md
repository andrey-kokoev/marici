# Coarsen, then fold 5134 onto 2134

The existing **12x12 fibration** viewer now draws a single folded carrier, not two overlaid incompatible subdivisions.

## Geometry

Per original half:

- 119 regular tetrahedra already match under V5→V2 with V1,V3,V4 fixed.
- The 224 unmatched tetrahedral pieces assemble into 56 whole octahedra.
- All 56 octahedra match under the fold, including their complete triangular boundary faces.

The coarsened carrier therefore has **175 cells: 119 tetrahedra + 56 octahedra**. Its renderer receives whole boundary polygons, not the four tetrahedral components of an octahedron. This removes 56 subdivision diagonals and 224 internal triangular cuts per half.

The fold identifies geometry once. The original two copies survive as **350 distinct flow occurrences**, two over each geometric cell. Original primitive references remain traceable. No claim is made that arbitrary independently assigned wedge coefficients could be collapsed into a single amplitude.

The folded outer surface has 196 triangles and is a closed triangulated sphere. Its volume is one half-carrier's volume; two preimages are not counted as overlapping physical material. The previous inter-copy seam becomes part of the quotient boundary, while its flow handoffs remain recorded in the unfolded occurrence network.

## Flow

−P and +P now occupy the same displayed geometric tip, labelled **V₂≡V₅**, but they retain different occurrence identities. The traversal cannot shortcut by equating those identities.

The coarsened face graph gives **23 outward rounds** from the clone's −P occurrence to the original's +P occurrence, then **23 return rounds**. Each admission and confirmation uses an actual whole shared face in the retained occurrence network. The new count follows from the coarse graph, not a forced 28-stage clock.

## Polarity without artificial triangles

Both polarity sheets remain stored. The artificial P/E half-face partition is removed, including its rendering helper. A **Whole-face polarity reading** selector chooses which sheet supplies display colours:

- Original sheet;
- Opposite sheet, the default.

Switching the selector does not change geometry, steps, histories, or either sheet's coefficients. It changes only the displayed whole-face reading. The local 2×2×2 test bank remains inspectable. Particle interpretation is still provisional.

The old fine-lattice overlay is disabled for this process so it cannot reintroduce removed octahedral diagonals.

## Verification

```
node --test tests/fibration-folded-process.test.mjs
node research/strominger/checkers/check_folded_fibration.mjs
node scripts/prepare-normal-ray.mjs
node scripts/test-fibration12-process.mjs
```

Tests cover exact primitive partition, complete face matching under the fold, two distinct preimages per cell, closed folded boundary, whole octahedral edges/faces, retained entry/exit identities, both flow directions, both polarity sheets, and rejection of a tampered return witness.

The browser test verifies the existing 12x12 process, all traversal stages, four displayed rotation anchors, the whole-face selector, persistence and return to −P. The broader focused model suite passes 26 tests.

- Model: `../realization-tower/fibration-folded-process.mjs`
- Receipt: `results/folded-fibration-v1.json`
- Prior unfolded reference remains in `../realization-tower/fibration-coherent-process.mjs`.

Refresh the viewer and choose **12x12 fibration → Restart at −P**. After the return completes at state 46, two additional steps apply and confirm the [candidate 4×4 filler comparison](four-by-four-filler-v1.md). They leave all geometry and particle-count assignments unchanged.
