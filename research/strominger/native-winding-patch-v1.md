# Native finite patch: a tessellated turn, not yet a helix

## Result

A finite native face-attached patch does exist. For the canonical marking, it contains **one P, three N and one E occupied primitive**, represented by seven distinct reader records. Every construction step is native, every occupied face contact has a selected witness in the completed patch, and every selected record reaches an E exit.

The four N/E primitives fill the four fixed tetrahedral sectors of one octahedron. They form a **closed tessellated turn around its internal diagonal**, with the root P attached outside. Their centroids have **zero axial rise**. This is not a nonzero-pitch helix.

There is a useful two-by-two distinction:

- the native five-slot coefficient permutation repeats after **two NN steps**;
- the NN geometry and chart repeat after **four NN steps**;
- the absolute realization origin has advanced by four and must **not** be identified with its initial value.

These are measured periods of declared native operations, not an imposed modulo-two rule. More specifically, the C occurrences alternate between two diagonal endpoints while the M occurrences visit four surrounding vertices. This is not a pair of independent order-two symmetries: the geometric turn has order four after forgetting absolute origins.

## What was constructed

Start with the canonical marking from the existing hydrogen attachment fixture. The main word is

```
P[0] --PN--> N_a[0]
             --NN--> N_b[1]
                       --NN--> N_c[2]
                                 --NE--> E_d[2].
```

Here brackets denote realization origins, not spatial heights. All NN steps cross actual shared primitive faces and advance origin by one. The PN and NE steps preserve origin and retain their source-defined occurrence identifications.

This five-record path is locally admissible and every record reaches E, but it is **not yet a certified patch**: E_d also touches N_a along another face, and that contact has no selected transfer witness.

The native completion is

```
N_a[0] --same-body reader advance--> N_a'[1] --NE--> E_d'[1].
```

The primed records occupy the same N_a and E_d bodies already present. They add two readers, not two particles. Their phases and full coefficient maps remain distinct. In particular, E_d[2] and E_d'[1] have different coefficient permutations and must not be merged because their occupied cell is the same.

The completed construction has:

- five occupied primitives: 1 P, 3 N, 1 E;
- seven selected reader records;
- six forward construction operations;
- no unwitnessed occupied face contact;
- a selected E exit path from every selected reader.

All construction prefixes pass the native species, C/M-role and face-contact compatibility checks. Some prefixes have an outstanding contact-witness obligation; it is discharged by the final native completion. We do not claim every incomplete prefix is already exit-certified.

## Geometry of the turn

The four N/E cells are exactly the four components of one source octahedron's fixed subdivision, not tetrahedra repositioned to match a drawing.

They have:

- six distinct geometric vertices;
- one common internal diagonal;
- four internal triangular faces, with a four-cycle adjacency graph;
- eight external triangular faces.

The outer boundary has six vertices, twelve edges and eight faces, with every boundary edge incident to two boundary faces and Euler characteristic 2. It is the existing octahedral boundary, not a newly derived helical separating sheet.

The diagonal endpoints are C-labelled; the four surrounding vertices are M-labelled. The ordered cell centroids form an exact square perpendicular to the diagonal: adjacent radial vectors are orthogonal, all have equal nonzero length, and opposite vectors negate each other. Thus the four-sector path really makes a turn, rather than merely forming an abstract graph cycle.

For each tetrahedron, project its centroid onto the common diagonal. Integer-scaled barycentric dot products are identical for all four centroids. The four internal face centroids have the same axial projection as well. Therefore this centroid-and-interface turn has **zero axial pitch** in the native Euclidean lattice metric. The displayed projection is not used to infer this result.

The four internal faces all contain the central edge. Their union is a branching interface there, not automatically a single smooth middle sheet. Nor does the existence of the outer octahedral boundary establish a surface separating two proposed field strands.

## Available four-step NN orbit versus selected occupancy

Following available NN transfers gives

```
N_a[0] -> N_b[1] -> N_c[2] -> N_d[3] -> N_a[4].
```

After two steps the five-slot permutation is back to its initial value, but the chart is in the opposite spatial sector. After four steps the initial chart and permutation return. The origin remains four larger.

This orbit is **available reference data**, not the occupancy of the completed patch. The selected patch assigns E to sector d. Its occupied geometry closes around the diagonal, but its selected directed transfer does not loop through E: E is terminal. Selecting N_d[3] in addition would assign N and E to the same body and is rejected. Similarly, selecting the early E exit from N_a conflicts with the N_b continuation body.

The checker also replaces the final orbit target with the old origin-zero packet as a negative control. Native transfer validation rejects that apparent geometric closure because it has the wrong realization increment. Geometry and coefficient repetition do not justify forgetting phase occurrences.

## The purely rereading two-step motif

A separate small patch follows the root P through two same-body reader advances, attaching its native N and E at each origin 0, 1 and 2. It is also exit-certified. Its first and third P charts and coefficient permutations agree, but their origins differ by two.

This shows why the two-by-two C/M window alone cannot establish a spatial helix: it can repeat while the proton never leaves its original primitive. The NN turn above is a distinct test of actual spatial face crossings.

## Marking dependence and search scope

The checker freshly constructs the initial NN orbit for all 24 bijective markings of the root tetrahedron:

- **8 markings** admit the four-sector NN turn and return to their original chart after four steps;
- **16 markings** do not admit even the first native NN continuation from their initial N reader.

Thus the turn is not a marking-independent law or a proof of full tetrahedral symmetry for the selected directed patch.

A preliminary general origin-2 enumeration reached its 50,000-configuration cap and was incomplete. No exhaustion or impossibility conclusion is drawn from that exploratory run. The reported witnesses and negative controls are freshly reconstructed directly from the explicit native words above; they do not depend on that enumeration.

## Scope relative to rung 12

This tests the proposed winding using the **native C/M occurrence and cell grammar**. It does not identify C/M with the earlier field tower's one-plus-two component decomposition. The native five-slot transfer permutation is also not the field tower's three-component corner-cycle operator.

No binding of the complete rung-12 field metric and named operators to this occupied patch has been established here. No global helix, full A4 spatial symmetry, infinite tessellation, physical stability or isotope prediction follows from this finite witness. In particular, it supplies no reference-only-N attachment constructor.

To obtain a genuine sloped winding, the next gate is a native continuation to successive sectors with **nonzero axial displacement**, retaining the contact witnesses and absolute phase records. A phase-level drawing with artificial vertical spacing would not satisfy that gate.

## Reproduce

```
node research/strominger/checkers/check_native_winding_patch.mjs
```

Outputs:

- `research/strominger/results/native-winding-patch/verification.json`
- `research/strominger/results/native-winding-patch/native-patch.svg`

The SVG separates actual lattice geometry from a reader-history diagram. Its history levels are not physical heights. Production rules and the viewer are unchanged.
