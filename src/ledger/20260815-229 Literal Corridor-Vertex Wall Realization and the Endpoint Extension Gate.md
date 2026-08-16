# Literal Corridor-Vertex Wall Realization and the Endpoint Extension Gate

## Record

Date: 2026-08-15

Status: proved in the literal entry143 face/Boolean incidence complex. The
three pair packets admit a primitive 24-row realization on legal common
triangulation vertices, with both adjacent-edge relative residues and exact
`D3` rotation covariance. The vertex cube is reflection-covariant, but
reflection closure of the selected two-edge residues requires twelve
additional third-edge rows. Identification with the normalization/log source,
that endpoint extension, and the generic-Q connector remain unconstructed. No
graph admission is claimed.

## The missing literal wall was already a vertex

For $W_{03,25}$, the two positive $q_{14}$ corridor edges are
\[
S_0=\{x_5,x_1\},\qquad S_1=\{D_{14},x_1\}.
\]
Their union
\[
V_{14}=\{x_1,D_{14},x_5\}
\]
is a legal noncrossing triangulation vertex of $K_6$. Rotation gives legal
vertices $V_{03}$ and $V_{25}$. Thus the shifted wall need not be an
external face: it can land on three literal entry143 vertices.

For $|V_D|=3$, the Boolean packet has profile
\[
1+3t+3t^2+t^3.
\]
After the uniform codimension-one Gysin shift it becomes
\[
t+3t^2+3t^3+t^4=P(t)(1+t),
\]
exactly the two-normal packet with Tor grades zero and one. The labelled map
is the identity on the resulting three Boolean axes. Across all three pairs
it is a $24\times24$ identity matrix, so its rank is 24 and every Smith
factor is one.

## Adjacent-edge Beck--Chevalley maps

Each corridor edge is obtained from $V_D$ by deleting one label. The
relative quotient of the vertex Boolean cube by states not containing that
label is canonically isomorphic to the edge Boolean cube by oriented residue.
The checker derives all 24 residue rows and all 24 nonzero normal-removal
squares. The entry143 sign difference between $|S|=3$ and $|S|=2$ is
exactly canceled by the contraction sign. Each residue block has a unit
minor; no occurrence or normal section is inverted.

The earlier two-edge rank obstruction remains correct for its stated target
$P\oplus P$. It is bypassed—not contradicted—by using the literal common
vertex and one uniform Gysin shift. Likewise the odd two-boundary suspension
cocycle of entry228 is the truncation shadow of changing which vertex axis is
treated as the Tor direction; the full three-axis vertex packet carries the
ordinary entry143 reflection action.

## Symmetry and the third-edge gate

Rotation $v\mapsto v+2$ cycles the three vertices. Entry143 reflection
$v\mapsto2-v$ preserves their orbit. The induced exterior permutation signs
commute with every normal differential, so the 24 vertex rows are strictly
reflection-covariant.

The selected two-edge residue block is not itself reflection closed.
Reflection can send one selected edge to the third edge of the same literal
triangulation vertex. Closing the block therefore requires all three edge
residues: 36 rows rather than 24. The twelve additional unit rows are fixed
inside entry143, but no current source/endpoint map lands on them. They are
the first exact endpoint-extension gate, not a sign ambiguity.

## Remaining gate

This closes the literal pair-wall incidence problem. It does not yet prove
that the normalization/log-excess object $W_{ij}$ pushes forward to this
vertex relative quotient. The required next comparison must:

1. identify the source Tor axis with the vertex label omitted by each
   adjacent edge, compatibly on their overlap;
2. restrict to the already normalized endpoint odd counits;
3. extend the three vertex packets through the entry223 top to the based
   $q_\Sigma$ row in literal entry143.

Until those source and endpoint/generic comparisons are constructed, the
pointed endpoint/$Q$ mapping fiber and physical parity remain undefined.

## Executable evidence

Checker:
`research/voevodsky/check_dp6_literal_vertex_wall_realization.rs`

SHA-256:
`e0e844a7072fc05631e88a07e6897159526ec5ae7a28d3dd5cf8b78b89239806`

Fresh `rustfmt --check`, warnings-denied optimized compilation, runtime
assertions, and JSON output passed. Native PowerShell was used only because
the user-site structured-command surface cannot access this repository or
invoke `rustc`.

## Outcome contract

~~~json
{
  "claim": "The common legal triangulation vertex of each complementary two-edge corridor supplies a literal entry143 three-label Boolean wall packet. After one uniform Gysin shift it realizes the full two-normal times Tor packet with a primitive 24-by-24 matrix, and its two relative residues derive all 24 adjacent-edge BC rows.",
  "status": "proved_scoped_literal_vertex_wall_realization_with_reflection_closure_gate",
  "scope": "literal entry143 face incidence and Boolean normal complex; source normalization/log pushforward and endpoint/Q extension excluded",
  "matrix": {
    "source_states": 24,
    "literal_vertex_rows": 24,
    "rank": 24,
    "all_smith_factors": 1,
    "adjacent_edge_residue_rows": 24,
    "relative_normal_bc_squares": 24,
    "reflection_closed_edge_residue_rows": 36,
    "additional_reflection_edge_rows_required": 12
  },
  "uniform_gysin_shift": 1,
  "D3_rotation": true,
  "vertex_reflection": true,
  "selected_two_edge_block_reflection_closed": false,
  "base_inversions": false,
  "unconstructed": [
    "normalization/log-excess source identification",
    "twelve third-edge endpoint/reflection extension rows",
    "based qSigma connector",
    "endpoint/Q mapping fiber",
    "p_partial_Q and Bockstein",
    "D8 and Jordan coherence"
  ],
  "checker": "research/voevodsky/check_dp6_literal_vertex_wall_realization.rs",
  "checker_sha256": "e0e844a7072fc05631e88a07e6897159526ec5ae7a28d3dd5cf8b78b89239806"
}
~~~
