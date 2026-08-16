# Equivariant Face-Trace Evenness No-Go and the Relative Interior Q Counit

## Symmetry forces even ordinary traces

The degree-two obstruction of entry269 cannot be repaired by changing the
fillers of the two collapsed pure-sheet faces or by rescaling the six mixed
face fillers.

Reflection pairs the pure faces with coefficients a and -a. Their coherently
oriented top contribution is 2a. It pairs the three one-negative faces with
the three two-negative faces with coefficients b and -b, contributing -6b.
Every D3/reflection-equivariant ordinary face trace is therefore

    2a - 6b,

which is even. The row [2,-6] has Smith factor 2 and cokernel Z/2; it never
reaches the normalized primitive value one.

Thus normalization saturation, ramification, and the fundamental-sphere
ambiguity do not supply the missing odd Q column while preserving literal
support and symmetry.

## Minimal symmetry-compatible enlargement

Entries264-267 construct the finite literal images of the six cross-sheet
edges and eight triangular faces of the conductor cross-polytope. The
smallest remaining class is its reflection-odd relative interior class.

If an extraordinary proper/log-excess counit maps that class to literal Q
with primitive coefficient +1, the top row becomes

    [2, -6, 1].

Its Smith factor is one, and the relative interior generator alone reaches
the normalized value one. This is the minimal symmetry-compatible repair.

The finite boundary maps do not construct the relative interior counit. The
missing datum is a support-typed map of the cross-polytope relative
fundamental class into the literal generic Q top, compatible with all six
edge maps, all eight facet BC cells, and endpoint framing.

## Evidence

- research/voevodsky/check_equivariant_face_trace_evenness_no_go.rs
- entries 143, 264-269.

~~~json
{
  "status": "falsified_scoped_equivariant_face_trace_oddness",
  "ordinary_equivariant_trace": "2a-6b",
  "ordinary_row": [2, -6],
  "ordinary_smith_factors": [2],
  "ordinary_cokernel": "Z/2",
  "primitive_value_one_reachable": false,
  "minimal_enlarged_row": [2, -6, 1],
  "enlarged_smith_factors": [1],
  "required_new_class": "reflection-odd relative interior Q counit",
  "cross_polytope_edges_constructed_finitely": 6,
  "cross_polytope_faces_constructed_finitely": 8,
  "relative_interior_to_literal_Q_constructed": false,
  "mapping_fiber_instantiated": false,
  "physical_p_defined": false,
  "physical_bockstein_defined": false,
  "D8_Jordan_tested": false,
  "graph_admission_claimed": false
}
~~~
