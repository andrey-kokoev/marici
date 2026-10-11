# Barycenter walks retain assembly order and form orthogonal flags

## Question

For the existing regular tetrahedron, does the final barycenter characterize its assembly, and what geometry is carried by the walk through successive barycenters?

## Source and test

Use A=(1,1,1), B=(1,-1,-1), C=(-1,1,-1), D=(-1,-1,1), as in the 1836 construction. For each of the 24 vertex orders, take the equal-weight barycenters of its one-, two-, three- and four-vertex prefixes. This is a specified filtration of known geometry, not a newly implemented WG vertex-generation rule. Stage number has no physical-time interpretation.

Compare ABCD with ABDC:

| Stage | ABCD | ABDC |
|---|---|---|
| Point | (1,1,1) | (1,1,1) |
| Edge | (1,0,0) | (1,0,0) |
| Triangle | (1/3,1/3,-1/3) | (1/3,-1/3,1/3) |
| Whole tetrahedron | (0,0,0) | (0,0,0) |

## Exact results

All 24 walks are distinct, but all have the same final barycenter. Their successive displacement vectors are pairwise perpendicular, with squared lengths 2, 2/3 and 1/3. Thus the right-angle phenomenon appears concretely in regular-simplex barycentric flags, not as a consequence of simplicial incidence alone.

Each walk's four points form a small tetrahedron of volume 1/9. Twelve orders have positive and twelve negative determinant orientation under the path-order convention. Their absolute volumes sum to 8/3, the original body's volume. This is the maximal-flag construction of barycentric subdivision. The earlier `barycentric-witness-packet.md` checks that incidence pattern using a different, standard affine tetrahedron; the present regular metric is what yields orthogonality.

The complete indexed walk recovers the original ordered vertices:

    x_(n+1) = (n+1)c_(n+1) - n*c_n.

The initial center is the first vertex. Checking this identity at each later step recovers every assembly order. Keeping only the final center, the step lengths or the flag volume does not recover the order.

A nonregular control changes D to (-1,-1,2), preserving the tetrahedral incidence while breaking displacement orthogonality. Its step dot products include -1/4 and -1/12. This detects an erroneous promotion of the metric result to all simplicial structures.

## Disposition

The barycenter is a common representative of the assembled body, but not a faithful record of its construction. The full indexed barycenter walk is faithful for this vertex-insertion construction and carries an orthogonal flag in the regular realization. No operator has yet been selected that makes its displacement directions eigenlines; that is separate from the verified geometry.

## Verification

`python research/nima/checkers/check_barycenter_assembly_walk.py` passed via structured-command execution `structured_command_execution:e_32876_1791221693706217100_18`. Exact rational checks cover all 24 orders, reconstruction, orthogonality, step norms, determinant volumes and the nonregular control. Results: `results/barycenter-assembly-walk.json`. No publication or commit is claimed.
