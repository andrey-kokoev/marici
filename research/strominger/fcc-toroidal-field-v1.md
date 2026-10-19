# Four-class FCC torus: field frames and the native refinement gate

## Result

The four-class FCC quotient realizes the required twelve-channel A4 action and admits exact field-pose transport. Two stronger fixed-structure interpretations fail:

- **Only 4 of the 12 affine A4 elements preserve the chosen native octahedral subdivision.**
- **Reusing one globally fixed field frame B fails for 9 of the 12 affine actions.** Rebuilding frames from the actual transformed cell and its center restores all twelve squares and the metric.

A family containing the three possible diagonal subdivisions is equivariant. This is a geometric family, not permission to change the native primitive under an existing reader record. The production grammar is unchanged.

## Coordinates and quotient

The actual source uses integer barycentric points `(b0,b1,b2,b3)` with sum one. The map

```
F(b) = (b1+b2, b1+b3, b2+b3)
```

identifies these points with the FCC lattice `L={x in Z3 : sum(x) even}` and preserves the induced Euclidean metric. The root tetrahedron becomes

```
000, 110, 101, 011.
```

Quotient by `2 Z3`, not by `2 L`, to obtain these four classes. Quotienting by `2 L` instead would give eight classes.

The chosen generators are the four translation classes and the 120-degree coordinate cycle

```
rho(x,y,z)=(z,x,y).
```

This direction of the cycle matches the earlier triangular-torus channel convention. The twelve maps `x -> rho^k x+t` act on the four classes as A4. Their 144 products are checked with the discarded even translation retained as an explicit deck displacement.

On the covering space the translations have infinite order. This chosen lift has group `L semidirect C3`; its finite quotient has group `V4 semidirect C3 = A4`.

The honeycomb also admits the different A4 action of proper rotations fixing the root tetrahedron. Together with translations that supplies the familiar crystallographic subgroup `L semidirect A4`. The two A4 actions agree as sets of permutations of four classes, but a torus half-period translation is not the same Euclidean motion as a root-tetrahedron half-turn.

No realization origin or coefficient history is identified by the spatial quotient.

## Actual source geometry, not a new ambient tiling

The checker imports `lattice-items.mjs` and transforms its regular tetrahedra (both orientations) and octahedra. All 36 template/action combinations match source-generated cells. It also verifies **192 boundary-neighbor covariance squares** using the actual `acrossFace` routine, rather than inferring adjacency solely from equal cell shapes.

However, the source octahedron is subdivided into four tetrahedra around one chosen diagonal. Coordinate cycling sends that diagonal to another one. For the affine quotient action, precisely the four translation elements preserve the fixed subdivision; the other eight do not.

For the separate proper root-tetrahedron A4 action, four of twelve rotations preserve the subdivision. Requiring preservation of the root's named C/M vertex partition reduces that set to two. These are stabilizer counts for those declared geometric markings, not a classification of complete native operations with all phases and contexts.

## Two alternative refinement policies

### Transport the subdivision choice

The three opposite-vertex diagonals each give a valid four-tetrahedron subdivision of the same octahedron. The full tested A4 action permutes this three-element family exactly.

This supports a **refinement-indexed family**. It does not support simultaneously occupying the components of all three subdivisions, or treating one choice as the existing fixed primitive after a rotation. A native transport rule would have to retain that index and specify its effect on reader incidence and coefficients.

### Replace the native subdivision

Coning all eight boundary triangles to the octahedron center gives an invariant eight-tetrahedron alternative. The center is `(1,1,1)` in the tested FCC coordinates and is not an FCC vertex. This changes the primitive set and is **not native under the present grammar**. The checker records it only as a geometric alternative, not as an adopted repair.

Centers used in exact tests are computed by summing integer coordinates before division. The source's floating-point drawing centers are not used for exact equality decisions.

## Field-frame test

The source field tetrahedron has edge length `2 sqrt(2)`, whereas these FCC coordinates give root-edge length `sqrt(2)`. One explicit uniform factor two converts centered FCC cell coordinates to the field's units. A fixed proper orthogonal coordinate map Q then gives

```
B_FCC = (I12 tensor Q) B,
B_FCC* B_FCC = K.
```

For each affine action, the checker independently reconstructs the target frames from the transformed vertices, transformed left-face centroids and target cell center. If V is the endpoint action and W is the actual Euclidean vector action plus channel permutation, it verifies

```
W B_source = B_target V.
```

All twelve such squares hold, as do the metric and transported L/G/C identities.

But substituting `B_target = B_source` fails for the nine elements with nonzero translation class. Actual Euclidean translation has identity linear action on vectors; it is not the same spatial rotation that the equivalent four-class permutation induces on a fixed tetrahedron.

The appropriate object is consequently a **position/frame-indexed field presentation**, not one frozen frame attached solely to a parity label. Recentring is explicit and the target center remains recorded; it is not forgotten positional data.

## What this establishes

There is an exact route from the FCC quotient to the existing field structure, provided cell pose is retained. There is also an exact symmetry-compatible family of diagonal refinements. The attempted interpretation with one fixed native refinement and one fixed global frame does not have the full claimed A4 symmetry.

This test does not construct a native five-coefficient transfer across refinement choices. Geometric covariance of the family cannot by itself license that transfer. The corresponding hypothesis and its discriminator are registered in the toroidal space evaluation net.

## Reproduce

```
python research/strominger/checkers/check_fcc_toroidal_field.py
```

This freshly runs the native geometry checker and the prerequisite field tests. Outputs:

- `research/strominger/results/fcc-toroidal-geometry/verification.json`
- `research/strominger/results/fcc-toroidal-field/verification.json`

No production rule or viewer is modified.
