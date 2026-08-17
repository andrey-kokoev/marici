# Two-Sheet Projective Pair-Vertex Incidence No-Go and the Hexagonal Conductor Gate

Date: 2026-08-15  
Status: falsified for the naive incidence-preserving realization of the six
literal cross-sheet corridors by two sheetwise projective-conductor triangles.
Extraordinary/logarithmic enlargements remain open. No graph admission is
claimed.

## Exact incidence obstruction

Entry 198's projective conductor boundary has, on each normalization sheet,
three facets and three pairwise strata with differential \(R-I\). For both
sheets its pair-incidence graph is
\[
C_3^{(+)}\sqcup C_3^{(-)}.
\]
It has six vertices, six edges, degree two at every vertex, and two connected
components.

Entries 266, 341--343 instead construct the six literal cross-sheet corridors.
Writing their endpoints as \(v_{i,\sigma}\), with
\(i\in\mathbb Z/3\) and \(\sigma\in\{+,-\}\), their boundary is
\[
\partial e_{ij}^{\sigma}=v_{i,\sigma}-v_{j,-\sigma},
\qquad i\ne j.
\]
The resulting degree-two graph is one connected hexagon \(C_6\). Therefore
no bijection can preserve the pair-vertex boundary incidence: connectedness
would have to send two components to one. This failure precedes orientation
signs, normal circles, Tor grades, Cech rows, and Smith-form calculations.

This does not invalidate entry 198's primitive projective Gysin row. It proves
that its two sheetwise SNC triangles cannot themselves be the missing literal
pair-vertex carrier.

## Minimal repair and consequence

The smallest admissible replacement must contain a connected hexagonal or
prismatic conductor boundary whose six vertices are the labelled
\(v_{i,\sigma}\) and whose six edge boundaries are the displayed cross-sheet
differences. It must also contain an independently derived reflection-odd
relative-interior counit. Entry 270 proves why that last datum is essential:
ordinary equivariant face traces have row \([2,-6]\) and Smith factor two,
whereas adjoining a primitive odd column gives \([2,-6,1]\) and Smith factor
one.

Until this connected carrier and its support-typed map to literal entry 143
are constructed, the endpoint/\(Q\) mapping fiber is not instantiated and
\(p_{\partial,Q}\), its Bockstein, \(D_8\), and Jordan coherence remain
undefined.

## Certificate

- `research/voevodsky/check_p2_pair_vertex_cross_sheet_hexagon_no_go.rs`

~~~json
{
  "claim": "The two sheetwise P2 pair-incidence triangles cannot map bijectively and incidence-preservingly to the six literal cross-sheet K6 corridors because C3 disjoint C3 has two connected components while the literal carrier is C6.",
  "status": "falsified_scoped_naive_two_sheet_P2_pair_vertex_lift",
  "scope": "ordinary incidence-preserving identification only; no no-go for a new connected extraordinary/log conductor carrier",
  "matrix": {
    "P2_graph": "C3_disjoint_C3",
    "P2_vertices": 6,
    "P2_edges": 6,
    "P2_components": 2,
    "literal_graph": "C6",
    "literal_vertices": 6,
    "literal_edges": 6,
    "literal_components": 1,
    "incidence_preserving_bijection": false
  },
  "minimal_repair": "Construct a connected hexagonal/prismatic conductor carrier with the six literal corridor boundaries and a geometrically derived primitive reflection-odd relative-interior Q counit.",
  "physical_mapping_fiber": "unconstructed",
  "physical_p_partial_Q": "undefined",
  "physical_Bockstein": "undefined"
}
~~~
