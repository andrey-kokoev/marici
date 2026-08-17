# KN-to-Literal Vertex-Star Pushforward and the Facet-Corridor Gate

## Record

Date: 2026-08-15

Status: constructed the finite constructible pushforward from all six
oriented KN augmented kernels to their literal entry143 vertex-star
packets. The pushforward is integral, proper in the finite exit-path sense,
and symmetry equivariant. Extension through the lower facet/corridor rows,
endpoints, and generic \(Q\) remains open. No graph admission is claimed.

## Source and target incidence categories

For each ordered long-road pair, entry328 supplies the oriented KN
augmented boundary
\[
D=\iota_\tau+\iota_{n_0}-\iota_{n_1}.
\]
The uniquely forced axis dictionary sends
\[
(\tau,n_0,n_1)
\]
to the three labels of the corresponding legal entry143 triangulation
vertex. A source Boolean state \(H\) maps to the identically labelled
literal vertex state \([S,H]\).

Its three boundary roles map respectively to:

1. the third wall edge obtained by omitting \(\tau\);
2. the second Rees-chart edge obtained by omitting \(n_0\); and
3. the first Rees-chart edge obtained by omitting \(n_1\).

The source coefficient on each axis contains \(J_a^\vee\), while the
literal radial corestriction supplies the matching principal section
\(J_a\). The canonical evaluation
\[
J_a^\vee\otimes J_a\longrightarrow\mathcal O
\]
turns every row into the required primitive unit without identifying
distinct occurrence lines or localizing the base.

## Finite proper pushforward

The six ordered kernels land on six distinct literal triangulation
vertices. Their complete incident stars contain eighteen distinct
two-label edges. Consequently:

- all 48 vertex-state support fibres are singletons;
- all 72 vertex-to-edge incidence support fibres are singletons; and
- no overlap choice or multiplicity occurs at these two grades.

Finite proper pushforward, equivalently left Kan extension on this finite
exit-path support, is therefore the identity on each labelled fibre. The
resulting vertex map has rank 48 with 48 unit Smith factors. Its full
boundary has rank 42 with 42 unit Smith factors, and all 72 two-step
equations cancel.

This is stronger than a coefficient dictionary: the oriented KN source
objects, their three boundary supports, the literal target strata, and the
finite proper fibres are all specified.

## Symmetry

Rotation permutes the six singleton-fibre kernels. Physical reflection
exchanges the positive and negative triples and their complete stars.
Reflection reverses both the KN interval orientation and the
anti-diagonal wall orientation, so the loaded wall coefficient remains
\(+1\). Principal sections and their duals transform inversely.

Thus the finite constructible pushforward is strictly \(D_3\)- and
reflection-equivariant at the vertex and edge grades.

## Remaining facet/corridor gate

The first possible gluing ambiguity now occurs one support grade lower.
The eighteen edge boundaries land in the nine one-label facets, each of
which is shared by two oriented pair packets. Extending the kernel requires
actual corridor chains and homotopies in those facets, not another
vertex-star identity.

The next matrix must:

1. compute the edge-to-facet restrictions of all six KN kernels;
2. identify their cyclic sum with the three facet rows of entry223's
   projectivized-conductor top;
3. prove the resulting facet/corridor homotopies agree with the literal
   entry143 differential and the established AW collars; and
4. determine the homogeneous solution module rather than assuming that
   the earlier rank-nine ambiguity has disappeared.

Only after that extension can the unique entry223 top coefficient be
transported to the literal \(q_\Sigma\) row and then joined to the two
endpoint odd counits.

## Executable evidence

Checker:
research/voevodsky/check_dp6_kn_literal_vertex_pushforward.rs

SHA-256:
84ccd2765634f6d4f86c208e698bb04731415459e439db42dece967ee4d55222

Fresh rustfmt --check, warnings-denied optimized compilation, runtime
assertions, and JSON output passed. Native PowerShell was used because no
repository-scoped structured-command MCP capable of invoking Rust is
exposed.

## Outcome contract

~~~json
{
  "claim": "The six oriented KN augmented kernels admit a canonical finite constructible proper pushforward to the six literal entry143 vertex stars. All 48 vertex fibres and 72 incidence fibres are singleton, all matching principal-line evaluations are primitive, and the complete vertex-edge kernel is D3/reflection equivariant.",
  "status": "proved_scoped_finite_constructible_KN_to_literal_vertex_pushforward",
  "scope": "finite constructible KN and literal entry143 vertex/edge exit-path grades; lower facet/corridor, endpoint, and generic-Q extension excluded",
  "pushforward": {
    "ordered_pairs": 6,
    "source_KN_vertex_states": 48,
    "literal_entry143_vertex_states": 48,
    "vertex_support_fibres_all_singleton": true,
    "literal_vertices": 6,
    "literal_incident_edges": 18,
    "edge_support_fibres_all_singleton": true,
    "boundary_rows": 72,
    "primitive_principal_line_evaluations": 72,
    "total_d_squared": 0,
    "vertex_rank": 48,
    "vertex_smith_all_ones": true,
    "boundary_rank": 42,
    "boundary_smith_all_ones": true,
    "base_inversions": false
  },
  "symmetry": {
    "D3_rotation": true,
    "physical_reflection": true,
    "loaded_wall_sign": 1
  },
  "unconstructed": [
    "lower facet/corridor extension and homogeneous solution module",
    "literal entry223 top and based qSigma connector",
    "endpoint extensions",
    "endpoint/Q mapping fiber",
    "p_partial_Q and Bockstein",
    "D8 and Jordan coherence"
  ],
  "checker": "research/voevodsky/check_dp6_kn_literal_vertex_pushforward.rs",
  "checker_sha256": "84ccd2765634f6d4f86c208e698bb04731415459e439db42dece967ee4d55222"
}
~~~
