# Toroidal map, tetrahedral realization and its two dual realizations

## Result

The explicit four-class realization **recovers the existing field realization map B**, using the declared left-face convention and one common orthogonal coordinate identification. The field metric is recovered from those realized centroid-edge frames, not merely copied as an unrelated torus decoration.

For the dual there are two different outcomes:

1. The **collapsed dual tetrahedron** gives the same frames up to an overall minus sign in common coordinates.
2. The **faithful cube/Petrie-dual realization** retains all eight dual vertices, but its hexagon centroids vanish. Applying the same centroid-edge frame recipe gives rank two, not three, so it cannot reproduce the invertible B.

These are different realizations, not interchangeable pictures of one faithful surface embedding.

## Source

B. Monson and A. Ivić Weiss, *Realizations of Regular Toroidal Maps*, Canadian Journal of Mathematics 51 (1999), 1240–1257, DOI 10.4153/CJM-1999-056-3.

Relevant points are §2, Theorem 3.2/Table 1 and remarks on pp. 1250–1251, and the dual cases on p. 1253 with Figures 5–6. Our map is `{3,6}_{(2,0)}`. Its full abstract automorphism group has order 48, not 12. The existing selected A4 action is a subgroup.

## Explicit primal realization

For vertex class (a,b), use

```
phi(a,b) = ((-1)^a, (-1)^b, (-1)^(a+b)).
```

All six squared intervertex distances are eight. The points have zero centroid and form a regular tetrahedron.

The existing field source labels its tetrahedron differently in Cartesian coordinates. With the already fixed class-to-label correspondence A=00, B=10, C=01, D=11, the required coordinate map is

```
H(x,y,z) = (y,x,z).
```

H has determinant **-1**. This is recorded explicitly as an orthogonal coordinate identification; it is **not** introduced as a new admitted native spatial mirror. A proper rotation cannot replace H while keeping this particular labelled correspondence unchanged. For the antipodal dual vertices, the corresponding map -H is proper, but it is a different coordinate identification. One cannot use separate identifications to erase the distinction between both tetrahedra in their common frame.

## Recovering B from the torus's left faces

Each directed torus channel has one left and one right triangular face. For each channel a→b:

1. realize its left face using phi;
2. take that face's centroid;
3. form the ordered three-column matrix `[centroid, phi(a), phi(b)]`.

The left-face vertex sets agree with all twelve independently supplied source `surfaceTriangle` declarations. If the resulting block matrix is B_phi, the exact identity is

```
(I12 tensor H) B_phi = B.
```

Consequently `B_phi* B_phi = B* B`: the coefficient metric is recovered geometrically from these realized sectors. The checker also reconstructs L using the source's declared positive cyclic mode `(1, omega, omega^2)`, reconstructs G by averaging the twelve proper spatial group actions, and checks the corner-cycle realization identity.

The positive cyclic mode and choice of orientation remain declared structure. They do not follow uniquely from a bare unoriented flat torus. In particular, using the right face instead preserves some geometric similarities but fails the required B/L correspondence; the checker includes this negative control.

The torus has eight faces, two for each realized tetrahedral face. The four left-face representatives and their three centroid-edge sectors produce the twelve field frames. This is a geometric collapse and a selected sector construction, not a homeomorphism of surfaces.

## Collapsed dual tetrahedron

A vertex of the abstract dual is a triangular face of the primal torus. If that face omits vertex label i, assign the dual vertex

```
q(face) = -phi(i).
```

This is three times the realized primal face centroid. The eight dual vertices map two-to-one onto four vertices of the antipodal tetrahedron.

Each dual hexagonal face becomes a triangular boundary traversed twice. Its centroid equals the centroid of the corresponding three distinct dual tetrahedral vertices. The associated centroid-edge frames, ordered by the induced dual channel labels, satisfy

```
(I12 tensor H) B_dual = -B.
```

Their coefficient metric is therefore unchanged. In common coordinates the two tetrahedra form the stella octangula of the paper. Nothing here assigns them to P/N/E carriers or establishes a new native transfer between them.

## Faithful cube/Petrie-dual alternative

Assign opposite signs to the two triangular-face orbits of the torus:

```
q_cube(face) = face_sign * phi(missing_vertex),
face_sign = +1 for an upward face, -1 for a downward face.
```

The eight images are all cube vertices `(±1,±1,±1)`. The twelve abstract dual edges become the twelve cube edges. The four dual faces are **skew six-edge Petrie cycles**, not the six ordinary square faces of a cube.

The checker constructs all 48 torus automorphisms and verifies their orthogonal actions on these cube vertices. This action is faithful. By contrast, their action on the four primal tetrahedron vertices has image order 24 and kernel order two. Its proper tetrahedral subgroup is the previously selected A4.

Every Petrie hexagon has centroid zero: it contains all cube vertices except one antipodal pair. A frame formed from that centroid and two adjacent vertices has a zero first column and rank exactly two. Thus the same centroid-edge recipe cannot give the source's invertible three-component B in this faithful dual realization. A different dual field decoration would require its own construction and checks.

The cube and collapsed-dual-tetrahedron realizations are not related by a single linear map in this three-space: antipodal cube vertices would have to map to the same nonzero dual-tetrahedron vertex.

## Edge duality is not endpoint relabelling

Orient a dual edge from the primal channel's left face to its right face. After the dual tetrahedral collapse, this gives a bijection of the twelve ordered endpoint channels. For example,

```
AB -> DC.
```

This channel permutation is an involution. It preserves the shared fiber metric, L, G, the internal cycle and A4 equivariance. However, it is **not induced by any permutation of the four primal endpoints**. Arrows sharing one primal source do not generally share one dual source.

Therefore it is an operator-level equivalence in a category allowing arbitrary channel permutations, not a source-fiber-preserving automorphism of the original typed comparison structure. The existing 137-slot comparison protocol cannot simply be carried across as an endpoint relabelling. That is an additional duality/transport gate, not an established native move.

## Reproduce

```
python research/strominger/checkers/check_toroidal_tetrahedral_realizations.py
```

Outputs:

- `research/strominger/results/toroidal-tetrahedral-realizations/verification.json`
- `research/strominger/results/toroidal-tetrahedral-realizations/primal-and-dual.svg`

All coordinate, metric, rank and finite-group checks use exact arithmetic. The source PDF is hash-linked. The prerequisite torus and field checks are freshly rerun. Production rules and the viewer are unchanged.
