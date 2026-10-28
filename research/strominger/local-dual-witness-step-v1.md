# One local dual-to-witness realization

## Question

Can a step transform retained interfaces into explicit witness cells, rather
than merely change the camera or label an already chosen target subdivision?

The operator authorized a local test on the central P and its four immediately
attached P,E,N,N cells. This source patch is taken from Step 2 of the existing
viewer. The operation itself does not read the rest of esd7, target counts or a
Pb-208 loadout. It is a test on supplied geometry, not generation from nothing.

## Declared operation

1. Retain the entire source simplicial complex, including boundary faces.
2. For every primal face sigma, construct its relative barycentric dual block:
   simplices are chains sigma < ... < tetrahedron. Dimension is 3-dim(sigma).
   Boundary blocks remain truncated blocks, not erased dangling incidences.
3. Each shared triangular face supplies a dual connection from one incident
   tetrahedron center through the face center to the other tetrahedron center.
4. Realize that connection as the union of the two cones from these centers to
   the original shared face. This is a two-sided bipyramidal witness region,
   triangulated by the shared face into two tetrahedra.
5. Retain all other face cones. They complete a subdivision of each original
   tetrahedron, so witness regions are not added on top of unchanged occupied
   volumes. Old cells survive as parent records and unions of four children.

Steps 4–5 are an explicit geometric thickening/subdivision policy, not a
consequence of bare graph duality or a uniquely selected Witness Generation law.
The relative dual uses full coface flags, not just the four-link dual graph.

## Measured result

| Object | Source | Face-cone realization |
|---|---:|---:|
| Vertices | 8 | 13 |
| Edges | 18 | 38 |
| Triangular faces | 16 | 46 |
| Tetrahedra | 5 | 20 |
| Distinct supporting planes of triangular faces | 8 | 32 |

The full relative dual has block counts (5,16,18,8) in dimensions 0,1,2,3.
Four interior dual connections give four bipyramidal witness regions, comprising
8 tetrahedra. The remaining 12 tetrahedra fill the residual parent regions.
All 12 original outer triangular faces are unchanged.

**Plane-count convention:** these are distinct affine supporting planes of
triangular cells. They are not counts of plane orientations, parallel families,
or the recently proposed realization/proposition–proof slicing planes.

The source is unchanged; P/N/E roles remain on its parent records. Witness cells
have no assigned species. There is no derivation of 137 leaves or 1836/144
coefficient arrows from these counts.

## Checks and geometric justification

Every cell center is strictly interior to its original tetrahedron; coning it
to the four faces partitions that tetrahedron. Shared-face centers of the two
parents are checked to lie in opposite open half-spaces. Hence the two witness
halves meet on the entire original face, with no interior overlap. The supplied
five-cell patch is a subcomplex of the existing esd7 triangulation.

The checker verifies retained flags, exact parent volumes, identical exterior
boundary triangles, incidence/Euler counts, input recovery, and traversal-order
independence. Unit tests additionally verify all dual flag inclusions, retained
boundary dual blocks, the disjoint partition of output cell identities into
witnesses and residuals, and integer-translation covariance of the counts.
Supporting planes are normalized with integer arithmetic in coordinates x'=4x.

This changes cellularization inside a fixed body: it refines primitive cells.
It does not move rigid unit cells outward or supply the previous fixed-unit
layer-growth operation. No new plane-sweep law or physical dynamics is inferred.

## Files and reproduction

- Pure operation: `research/realization-tower/interface-witness-generation.mjs`
- Source-bound test: `research/strominger/checkers/check_local_dual_witness_step.mjs`
- Full retained output: `research/strominger/results/local-dual-witness-step-v1.json`
- Tests: `tests/interface-witness-generation.test.mjs`

```sh
node research/strominger/checkers/check_local_dual_witness_step.mjs
node --test tests/interface-witness-generation.test.mjs
```

Fresh executions pass. No viewer or native construction rule was changed.
Next distinguish this face-cone realization from the desired rule that creates
new distinguished space: the geometric realization and its counts exist, but
its selection as the intended Witness Generation transition remains open.
