# Refined annular carrier: construction status

Implementation: `research/realization-tower/refined-neutron-belt.mjs`.

The six original cones now each carry a full resolution-7 tetrahedron/octahedron cell complex, obtained by an affine map of the same native subdivision used by the main ESD7 graph. This is actual cell refinement, not a six-orb loop overlay.

Per belt:

- 1050 cells: 714 tetrahedra and 336 whole octahedra.
- Six cone sectors, paired 3+3 with the source circulation assignments.
- Six adjacent sector interfaces, each matching 49 complete triangular cell faces.
- 588 boundary triangles: 294 outer-panel triangles and 294 radial rim triangles.
- Two source cap cones excluded; no additional N plane removed.
- Connected shared-face graph; no triangular face has more than two owners.

The source cone shapes differ from the native regular tetrahedron. The construction preserves the native cell incidence via affine deformation, not rigid native cell lengths. Opposite circulation is a separate state parameter. Two returned carriers with opposite circulation currently occupy the same reference coordinates: they are NOT yet an embedded, interwoven pair.

## Remaining insertion problem

The current ESD7 pair has 49 directly identified seam triangles and zero gap. A volumetric insertion must replace that gluing with a specified collar and matching boundary maps. Merely translating carriers there causes overlap; projecting them into the seam collapses volume. The old annular carrier also has six radial rim faces, not two filled triangular caps. Its parent attachment must respect those actual boundary faces.

The interwoven two-belt embedding, its parent boundary matching, and a flow converter are not implemented. No new carrier has been published into the main viewer or particle accounting as a completed insertion.

Verification: `node --test tests/refined-neutron-belt.test.mjs`.
