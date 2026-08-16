# Conductor Cross-Polytope Carrier and the Eight Loaded Face Gate

## Canonical carrier

The octahedral completion forced by entry253 has intrinsic normalization
provenance. An ordered road pair \((i,j)\) determines:

1. the omitted road \(D_k\), where \(\{i,j,k\}=\{0,1,2\}\); and
2. the orientation sign of the ordered pair.

Hence the six ordered sectors identify canonically with the signed basis
vectors

\[
\{\pm e_{14},\pm e_{03},\pm e_{25}\}
\]

of the three conductor-normal directions. Their convex hull is the
three-dimensional cross-polytope. Its boundary is the octahedral
two-sphere found combinatorially in entry253.

The twelve edges split canonically into the two previously disjoint systems:

- six cross-sheet edges from the dP6 conductor hexagon; and
- six same-sheet edges from the literal short-facet incidence triangles.

The eight triangular faces choose one sign from each opposite pair. They
are the minimal two-cells on which the conductor and facet composites can
be compared.

## Integral cellular certificate

With the boundary orientation induced from the signed conductor basis, the
cellular complex has ranks

\[
\mathbb Z^8\xrightarrow{d_2}\mathbb Z^{12}
\xrightarrow{d_1}\mathbb Z^6.
\]

The checker derives both incidence matrices and verifies:

- \(d_1d_2=0\);
- \(\operatorname{rank}d_1=5\), with unit Smith factors;
- \(\operatorname{rank}d_2=7\), witnessed by a unimodular maximal minor;
- \(H_2\cong\mathbb Z\), \(H_1=0\), and \(H_0\cong\mathbb Z\);
- the oriented fundamental two-cycle is primitive; and
- rotation and reflection preserve the full cell structure.

Thus the global connector carrier has no integral torsion or residual
one-cycle ambiguity. Its top normalization is unique up to the already fixed
orientation.

## Remaining eight-face gate

This theorem constructs the canonical global carrier, not yet its loaded
six-functor realization. Each of its eight triangular faces must receive a
Beck--Chevalley two-cell whose boundary compares:

1. the entry245 shifted same-sheet pair-facet Gysin edge;
2. the entries246/249 cross-sheet Rees/KN connector edge; and
3. the third rotated edge.

Those maps must be expanded on every literal entry143 occurrence,
normal-circle, Tor, and Čech state. The eight face equations must then map
the primitive octahedral fundamental cycle to entry251's canonical generic
top lift and its six short-facet defect.

No carrier-level torsion remains to obstruct this. The first unconstructed
datum is now exactly the eight loaded face transformations. Until they are
geometrically realized, the endpoint cells and pointed mapping fiber remain
uninstantiated.

## Evidence

- research/voevodsky/check_conductor_cross_polytope_carrier.rs
- entries 93, 143, 241, 245, 246, 249, 251, 252, and 253.

~~~json
{
  "status": "proved_scoped_conductor_cross_polytope_carrier",
  "conductor_rank": 3,
  "signed_sector_vertices": 6,
  "opposite_pairs": 3,
  "edges": 12,
  "faces": 8,
  "d1_rank": 5,
  "d1_smith_nonzero_all_ones": true,
  "d2_rank": 7,
  "d2_smith_nonzero_all_ones": true,
  "H2_rank": 1,
  "H1_rank": 0,
  "H0_rank": 1,
  "primitive_fundamental_cycle": true,
  "D3": true,
  "reflection": true,
  "loaded_face_BC_maps_constructed": false,
  "six_functor_realization_constructed": false,
  "mapping_fiber_instantiated": false,
  "physical_p_defined": false,
  "physical_bockstein_defined": false,
  "D8_Jordan_tested": false,
  "graph_admission_claimed": false
}
~~~
