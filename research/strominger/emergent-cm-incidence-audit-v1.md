# Do C/M roles emerge from the existing assembly?

## Scope

Audit the actual upright-seed assembly with its 1/4/44/126 item layers. Do not
use the displayed C/M names as structural input. Preserve the seed cell as a
set, item types, shared-face incidence, and arrows from earlier to later
construction layers. Test both before and after octahedron subdivision.

## Findings

All four seed vertices have identical incidence signatures: 3 seed edges,
12 nearest-neighbor edges, 2 subdivision diagonals, 8 incident regular
tetrahedra and 6 incident octahedra. Their incident-item layer histograms also
agree. The 3 local edges are included in the 12 ambient nearest-neighbor
edges. No edge direction follows from this count.

All 24 structural-coordinate permutations preserve the untriangulated
assembly, the seed, item types, and directed layer adjacency. They act
transitively on the four seed vertices. Consequently no proper labeled C/M
vertex partition is invariant under this supplied structure.

Exactly 8 of these coordinate permutations preserve the particular
triangulation diagonals. The four orientation-preserving members still act
transitively on the seed vertices. For example, permutation (1,0,3,2) exchanges
C0/M0 and C1/M1 while preserving spatial orientation and the layer arrows.
Thus orientation and growth direction do not establish fixed C versus M
vertex classes either.

However, the full eight-element tested subdivision symmetry subgroup has
ONE invariant **unordered** 2+2 partition. It agrees with the displayed
{C0,C1} / {M0,M1} pairing. Its two blocks can be exchanged: neither is
intrinsically named C or M. Before subdivision, none of the three possible
2+2 partitions is invariant under all 24 coordinate permutations. Restricting
to the four orientation-preserving subdivision symmetries makes all three
partitions invariant, so spatial orientation alone does not uniquely pick it.

## Interpretation

The local-versus-ambient incidence distinction is genuinely present. A
candidate exchangeable two-block structure is also present **if the chosen
octahedral diagonal is part of the intended mechanics**. It is not intrinsic
to the tetrahedral–octahedral assembly without that additional subdivision.
The particular subdivision was previously an implementation choice, not a
source-derived physical rule.

The graph does not yet supply a directed 12-in / 3-out operation. Nor is the
seed barycenter a lattice node with twelve incident lattice edges: it is not
in the integer structural node table. A barycenter interface would require
additional incidence data.

These explicit symmetries suffice for the negative vertex-class conclusion;
this audit does not claim to enumerate the complete abstract automorphism
group. It also does not exclude roles attached to a marked edge/face, a
cell–vertex incidence, transported state, or a dynamical process.

## Evidence

Run `node research/strominger/checkers/check_emergent_cm_roles.mjs`.
Full permutations, orbit sizes, vertex signatures, candidate partitions,
role-swap witness, and source hashes are in
`results/emergent-cm-roles/verification.json`.
