# Full-Log Vertex Matrix and the Third-Edge Reflection Gate

## Record

Date: 2026-08-15

Status: the pairwise full-log excess matrix is proved, while physical
reflection closure of the existing two-edge source boundary is falsified.
The exact minimal finite enlargement is one third-edge wall
Beck--Chevalley cell for each ordered pair. No graph admission is claimed.

## Derived pairwise realization

For an ordered product-Rees pair, write the original log axes as
\((a,b,c)\), with product branch \(d=a+b\), primitive excess functional
\[
\delta(a)=-1,\qquad \delta(b)=+1,\qquad \delta(c)=0,
\]
and conductor Tor axis \(\tau\). Contraction by \(\delta\) gives
\[
\Lambda^\bullet\langle a,b,c,\tau\rangle
 \longrightarrow
\Lambda^{\bullet-1}\langle d,c,\tau\rangle .
\]
The checker constructs this as an explicit integral \(8\times16\) matrix.
For each of its eight target basis vectors it exhibits a distinct source
column with coefficient \(\pm1\). Consequently its rank is eight and all
eight nonzero Smith factors are one. Across six ordered pairs, the matrix is
\(48\times96\), of rank 48, with no torsion or base inversion.

The two exact edges of the complementary marked corridor determine:

- one persistent label, their intersection;
- the moving label on the first edge;
- the moving label on the second edge.

Among all six bijections from \((\tau,n_0,n_1)\) to the three labels of
their common legal triangulation vertex, exactly one respects both chart
restrictions:
\[
\tau\longmapsto\text{persistent},\qquad
n_0\longmapsto\text{moving}_0,\qquad
n_1\longmapsto\text{moving}_1.
\]
Thus the axis dictionary is derived rather than fitted. Exterior
permutation signs make it a chain map to the literal entry143
three-label Boolean cube. The two relative contractions derive 48
adjacent-edge residue rows and 48 normal differential squares, including
the uniform codimension-one suspension sign.

## Earliest physical-reflection failure

Rotation preserves the ordered source corridor assignments. Physical
endpoint reflection is instead \(v\mapsto3-v\). It preserves and
exchanges the six legal target vertices, but it does not preserve all
source-selected boundary edges.

There are twelve selected edge restrictions. Exactly six reflect to the
selected edge pair of the reflected ordered source object. The other six,
one per ordered pair, reflect to the legal but unselected third edge of the
same triangulation vertex. Hence the pairwise matrix exists and is
primitive, but no physically reflection-equivariant realization can use
only the current two-edge \(W_{ij}\) boundary data.

This also pinpoints the convention mismatch: entry221's two-edge finite
extraordinary objects and entry321's physically reflected literal vertex
packets are each consistent in their stated scopes, but their selected
adjacent-edge diagrams are not equivariantly identical.

## Minimal additional datum

For every ordered pair, adjoin the missing third-edge wall restriction and
its Beck--Chevalley 2-cell. Equivalently, replace the two-edge boundary of
\(W_{ij}\) by the full three-edge star of its literal triangulation vertex.
The checker proves that the union of the reflected and selected edge pairs
is exactly this three-edge star; no larger finite incidence enlargement is
needed.

The new wall cell must still be derived from the product-Rees/log-BM
geometry, not declared as an identity. It must carry the occurrence line,
normal-circle signs, both conductor grades, endpoint restriction, and
physical reflection action. Only after that construction can the six
pairwise maps be glued to the entry223 top and based \(q_\Sigma\) row.

Therefore the endpoint/\(Q\) mapping fiber, \(p_{\partial,Q}\), its
Bockstein, and the physical \(D_8\)/Jordan tests remain undefined.

## Executable evidence

Checker:
`research/voevodsky/check_dp6_full_log_vertex_realization.rs`

SHA-256:
`bdbf1a27122c40f9d800c3cba60ed2bc07b10cf5d5ba126dfddd108dd6f3b45a`

Fresh `rustfmt --check`, warnings-denied optimized compilation, runtime
assertions, and JSON field checks passed. Native PowerShell was used for
Rust verification because no repository-scoped structured-command MCP
capable of invoking `rustc` is exposed.

## Outcome contract

~~~json
{
  "claim": "The six pairwise full-log product-Rees packets admit unique primitive 48-by-96 maps to the six literal entry143 vertex Boolean packets, but the existing two-edge source boundaries are not closed under physical reflection: one edge per ordered pair is sent to the unselected third edge.",
  "status": "falsified_scoped_two_edge_physical_reflection_closure",
  "scope": "finite normalization-labelled product-Rees/log exterior packets and literal entry143 incidence complex; spatial six-functor push-pull excluded",
  "positive_matrix": {
    "ordered_pairs": 6,
    "rows": 48,
    "columns": 96,
    "rank": 48,
    "all_nonzero_smith_factors": 1,
    "axis_assignment_unique": true,
    "adjacent_edge_residue_rows": 48,
    "normal_chain_squares": 48,
    "base_inversions": false
  },
  "falsifier": {
    "physical_reflection": "v -> 3-v",
    "reflected_vertex_rows": 6,
    "selected_edge_rows_preserved": 6,
    "legal_but_unselected_edge_rows": 6,
    "failure_per_ordered_pair": 1
  },
  "minimal_additional_geometry": "One geometrically derived third-edge wall Beck-Chevalley cell per ordered pair, promoting each W_ij boundary to the full three-edge literal vertex star.",
  "unconstructed": [
    "full vertex-star log-BM correspondence",
    "spatial six-functor push-pull",
    "literal endpoint extensions",
    "based qSigma connector",
    "endpoint/Q mapping fiber",
    "p_partial_Q and Bockstein",
    "D8 and Jordan coherence"
  ],
  "checker": "research/voevodsky/check_dp6_full_log_vertex_realization.rs",
  "checker_sha256": "bdbf1a27122c40f9d800c3cba60ed2bc07b10cf5d5ba126dfddd108dd6f3b45a"
}
~~~
