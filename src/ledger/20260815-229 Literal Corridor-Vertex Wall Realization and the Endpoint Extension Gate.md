# Literal Corridor-Vertex Wall Realization and the Endpoint Extension Gate

## Record

Date: 2026-08-15

Status: proved in the literal entry143 face/Boolean incidence complex. The
six ordered pair packets admit a primitive 48-row realization on six legal
common triangulation vertices, with both adjacent-edge relative residues and
the physical endpoint reflection. The three-pair unoriented quotient has the
expected 24 rows. Identification with the normalization/log source, endpoint
extension, and the generic-Q connector remain unconstructed. No graph
admission is claimed.

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
external face: it can land on three positive literal entry143 vertices.
Physical reflection $v\mapsto3-v$ produces three disjoint negative vertices,
matching entry221's six ordered pair objects.

For $|V_D|=3$, the Boolean packet has profile
\[
1+3t+3t^2+t^3.
\]
After the uniform codimension-one Gysin shift it becomes
\[
t+3t^2+3t^3+t^4=P(t)(1+t),
\]
exactly the two-normal packet with Tor grades zero and one. The labelled map
is the identity on the resulting three Boolean axes. Across all six ordered
pairs it is a $48\times48$ identity matrix, so its rank is 48 and every Smith
factor is one. The unoriented three-pair quotient retains 24 rows.

## Adjacent-edge Beck--Chevalley maps

Each corridor edge is obtained from $V_D$ by deleting one label. The
relative quotient of the vertex Boolean cube by states not containing that
label is canonically isomorphic to the edge Boolean cube by oriented residue.
The checker derives all 48 residue rows and all 48 nonzero normal-removal
squares. The entry143 sign difference between $|S|=3$ and $|S|=2$ is
exactly canceled by the contraction sign. Each residue block has a unit
minor; no occurrence or normal section is inverted.

The earlier two-edge rank obstruction remains correct for its stated target
$P\oplus P$. It is bypassed—not contradicted—by using the literal common
vertex and one uniform Gysin shift. Likewise the odd two-boundary suspension
cocycle of entry228 is the truncation shadow of changing which vertex axis is
treated as the Tor direction; the full three-axis vertex packet carries the
ordinary entry143 reflection action.

## Physical symmetry

Rotation $v\mapsto v+2$ preserves and cycles each three-vertex sheet.
Physical reflection $v\mapsto3-v$ exchanges the positive and negative
endpoint sheets, their vertices, and their exact selected edge pairs. The
induced exterior permutation signs commute with every normal differential.
Thus the six oriented vertex packets and all 48 adjacent-edge residues are
strictly reflection closed. The target-only reflection $v\mapsto2-v$ used in
the target Cech checker is a different convention and must not be substituted
for the physical endpoint reflection.

## Remaining gate

This closes the literal oriented pair-wall incidence problem. It does not yet prove
that the normalization/log-excess object $W_{ij}$ pushes forward to this
vertex relative quotient. The required next comparison must:

1. identify each of the six ordered source packets and its Tor axis with the
   corresponding oriented vertex packet and omitted edge label;
2. restrict to the already normalized endpoint odd counits;
3. extend the three vertex packets through the entry223 top to the based
   $q_\Sigma$ row in literal entry143.

Until those source and endpoint/generic comparisons are constructed, the
pointed endpoint/$Q$ mapping fiber and physical parity remain undefined.

## Executable evidence

Checker:
`research/voevodsky/check_dp6_literal_vertex_wall_realization.rs`

SHA-256:
`2785b5cee56bb15fd94fa7c4d8fd5db799ed7e0bb1a2f9bcdec714b391b86301`

Fresh `rustfmt --check`, warnings-denied optimized compilation, runtime
assertions, and JSON output passed. Native PowerShell was used only because
the user-site structured-command surface cannot access this repository or
invoke `rustc`.

## Outcome contract

~~~json
{
  "claim": "The six oriented common legal triangulation vertices of the complementary two-edge corridors supply literal entry143 three-label Boolean wall packets. After one uniform Gysin shift they realize the full two-normal times Tor packets with a primitive 48-by-48 matrix; the three-pair unoriented quotient has 24 rows, and the two relative residues derive all 48 adjacent-edge BC rows.",
  "status": "proved_scoped_literal_oriented_vertex_wall_realization",
  "scope": "literal entry143 face incidence and Boolean normal complex; source normalization/log pushforward and endpoint/Q extension excluded",
  "matrix": {
    "source_states": 48,
    "literal_vertex_rows": 48,
    "unoriented_quotient_rows": 24,
    "rank": 48,
    "all_smith_factors": 1,
    "adjacent_edge_residue_rows": 48,
    "relative_normal_bc_squares": 48
  },
  "uniform_gysin_shift": 1,
  "D3_rotation": true,
  "physical_reflection": "v -> 3-v exchanges endpoint sheets",
  "oriented_edge_blocks_reflection_closed": true,
  "base_inversions": false,
  "unconstructed": [
    "normalization/log-excess source identification",
    "literal endpoint extensions",
    "based qSigma connector",
    "endpoint/Q mapping fiber",
    "p_partial_Q and Bockstein",
    "D8 and Jordan coherence"
  ],
  "checker": "research/voevodsky/check_dp6_literal_vertex_wall_realization.rs",
  "checker_sha256": "2785b5cee56bb15fd94fa7c4d8fd5db799ed7e0bb1a2f9bcdec714b391b86301"
}
~~~
