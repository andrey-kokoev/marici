# Intrinsic Cross-Polytope Interior Gysin and the Eight-Face Realization Gate

## Intrinsic odd interior class

Entry256 identifies the unit odd interior column required to repair the
strict octahedral face trace. That column is already present geometrically:
it is the relative fundamental class of the full conductor cross-polytope.

Let

\[
B_\Diamond=\operatorname{conv}
\{\pm e_{14},\pm e_{03},\pm e_{25}\}.
\]

This is a canonical three-ball in the direct sum of the three labelled
conductor-normal lines. Its boundary is entry336's octahedral sphere. The
cellular boundary of its single interior generator is the signed sum of the
eight triangular faces,

\[
d[B_\Diamond]
=\sum_{s\in\{\pm1\}^3}(s_{14}s_{03}s_{25})[F_s].
\]

All eight coefficients are units, their gcd is one, and the checker verifies
that the subsequent edge boundary is zero. Thus

\[
H_3(B_\Diamond,\partial B_\Diamond)\cong\mathbb Z
\]

has a primitive normalized generator.

## Reflection and the top trace

Physical reflection acts on the conductor basis by

\[
e_0\mapsto-e_0,qquad
e_1\mapsto-e_2,qquad
e_2\mapsto-e_1.
\]

Its determinant is \(+1\), so it preserves the geometric three-ball
orientation. The single retained source orientation twist contributes
\(-1\). Therefore the loaded interior class is reflection odd, exactly like
the loaded entry143 generic target line.

The relative BM/Gysin counit

\[
C_3(B_\Diamond,\partial B_\Diamond)\longrightarrow
\mathbb Z_{\rm generic}
\]

is consequently equivariant and sends the interior class to \(+1\).
It supplies the missing column in

\[
[2,-6,1],
\]

whose Smith factor is one. The \(\mathbb Z/2\) obstruction of entry256 is
therefore removed intrinsically at the conductor-carrier level; no external
central cell or fitted scalar is needed.

## Remaining realization gate

This does not yet give a map to the literal entry143 complex. The boundary
of the interior class has eight triangular faces, so the unit top counit can
be used only after constructing eight loaded Beck--Chevalley maps whose
edge restrictions are simultaneously:

- the six same-sheet shifted pair-facet Gysin maps;
- the six cross-sheet Rees/KN conductor connectors; and
- the literal entry143 short-facet defect rows.

The chain equation must identify the image of
\(d[B_\Diamond]\) with the \(P\)-defect of entry251's canonical generic
top lift. Until those eight maps exist in one mixed-variance Hom complex,
the interior counit is a geometric carrier theorem rather than the global
six-functor correspondence.

## Evidence

- research/voevodsky/check_conductor_cross_polytope_interior_gysin.rs
- entries 93, 143, 249, 251, 253, 333, 336, and 256.

~~~json
{
  "status": "proved_scoped_intrinsic_cross_polytope_interior_Gysin",
  "cross_polytope_dimension": 3,
  "boundary_faces": 8,
  "boundary_edges": 12,
  "d2_d3_zero": true,
  "interior_boundary_primitive": true,
  "geometric_reflection_determinant": 1,
  "source_orientation_twist": -1,
  "loaded_interior_character": -1,
  "loaded_target_character": -1,
  "interior_counit": 1,
  "repaired_row": [2, -6, 1],
  "repaired_smith": [1],
  "loaded_face_BC_maps_constructed": false,
  "literal_entry143_interior_map_constructed": false,
  "mapping_fiber_instantiated": false,
  "physical_p_defined": false,
  "physical_bockstein_defined": false,
  "D8_Jordan_tested": false,
  "graph_admission_claimed": false
}
~~~
