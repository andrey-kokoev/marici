# Native screw-periodic continuation of the finite winding patch

## Result and limits

A finite native patch with a **four-block screw-periodic core** can be constructed while retaining the entire previous certified five-body patch, including both of its E reader records. Each block advances its ordered P reference frame by a proper half-turn plus a nonzero translation along the screw axis. No cells are repositioned to fit a helix.

This passes the nonzero-displacement gate for a **tessellated screw pattern**, but not all stronger helix claims:

- P boundary centroids lie on a sampled constant-radius screw orbit.
- Intermediate N centroids can lie on the axis itself. The actual centroid path is not a constant-radius helix.
- A discrete half-turn does not distinguish rotation by +pi from -pi. We have not selected handedness or established two oppositely handed strands.
- No middle separating sheet or binding to the rung-12 field metric has been derived.

## Native word

Use two native subwords, with species determined by the current source:

```
B = PN, NN-phase-advance, NN-phase-advance, inverse-PN,
    P reader-phase-advance

A = PN, N reader-phase-advance, inverse-PN

block = B followed by A
```

B moves to another P body and rereads it. A passes through a neighboring N reader and its same-body advance to another P reference. Every spatial move uses its actual shared primitive face. A same-body reader advance is not counted as a spatial attachment.

One block contains eight transfer steps and advances realization origin by four. Four blocks are checked, from P origin 0 through origins 4, 8, 12 and 16. Some transfers revisit already-selected records; construction receipts distinguish such walk steps from adding a new reader.

## Exact screw motion

Coordinates are the source's four barycentric coordinates with sum equal to one, using the induced Euclidean metric. Let

```
d = (-1, 0, 1, 0),
a = (0, 1/2, 0, 1/2).
```

The checker derives an integer affine matrix T from the four ordered P vertex images in the first block. It verifies:

- metric preservation on the sum-zero displacement space;
- determinant +1;
- a nontrivial half-turn around the line a + t*d;
- T(a) = a + d;
- T squared sends every point x to x + 2*d;
- all five P reference marks obey the same T in all four blocks;
- every intermediate chart's complete reference marks also repeat under T.

Thus this is not merely a fit to two centroid positions. The actual cell references repeat under a proper screw motion.

The axial increment per half-turn is sqrt(2), in the convention where a root tetrahedron edge has length sqrt(2). The displacement per full turn is 2*d, of length **2*sqrt(2)**, or two root-edge lengths.

The P boundary centroids have the exact form

```
c_k = a + k*d + (-1)^k*r,   r = (1,-1,1,-1)/4.
```

Here r is perpendicular to d and has squared length 1/4. These are half-turn samples of a radius-1/2 helical orbit. A smooth interpolation between them is not a native construction rule.

## This uses a different axis

The earlier octahedral turn used the diagonal direction

```
D = (-1, 1, -1, 1).
```

The new screw axis is perpendicular to D. Measured along the original D direction, the P centroids alternate in height as 0,2,0,2,0: there is still no sustained climb along that old axis.

The new axis was derived from the nonzero translation in T squared, not chosen merely to make an arbitrary displacement look axial. The construction changes from a turn within one octahedron to a screw-periodic arrangement across neighboring cells.

## Contact completion and retained evidence

The previous [native winding patch](native-winding-patch-v1.md) is reconstructed first and retained unchanged as a selected subset. A final E exit is added at the far end of the new walk.

The bare four-block walk is locally compatible and exit-reachable but leaves **four incidental PN face contacts unwitnessed**. For each, the checker adds the native branch

```
N reader advance, inverse-PN, P reader advance, PN
```

and follows the corresponding remaining native suffix to an E exit. All these additional reader records occupy bodies already present. No extra primitive is introduced to repair a contact.

The completed patch has **24 occupied primitives (9 P, 13 N, 2 E) and 66 reader records**. This is a geometric test patch, not a neutral isotope target.

Equal cell, chart or origin does not imply equal field history: the repairs retain full five-slot permutations and distinct records. The completed patch passes native transfer validation, construction-prefix compatibility, all occupied-face witness checks and an independent reverse traversal from selected E exits. Construction is also replayed in a second engine, comparing semantic references and geometry rather than assuming equal lazy-generated IDs.

Incomplete prefixes may have contact-witness obligations. The final patch discharges them; we do not label every intermediate prefix a completed exit certificate.

## Finite scope

The far E cap occupies the next prospective NN continuation body. Attempting to occupy that body as N at the same time is rejected. The retained old cap does not obstruct this construction, but this does **not** establish indefinite retained-prefix extension of the new capped patch.

The result is not an isotope stability claim, a new native rule, a reference-only-neutron constructor, or a classification of all possible screw words. Earlier trial words produced closed turns or translations; this checker records one explicit successful finite screw construction, not an exhaustive search or shortest-word proof.

In particular, the native C/M occurrence grammar has not been identified with the field tower's three-component one-plus-two decomposition. Full rung-12 metric and symmetry compatibility remains a separate gate.

## Reproduce

```
node research/strominger/checkers/check_native_screw_patch.mjs
```

Outputs:

- `research/strominger/results/native-screw-patch/verification.json`
- `research/strominger/results/native-screw-patch/native-screw-patch.svg`

The drawing uses actual lattice coordinates. Production rules, the isotope solver and the viewer are unchanged.
