# Extraordinary Pair Objects and Adjacent-Facet Beck--Chevalley

## Record

Date: 2026-08-15

Status: proved inside the explicitly enlarged finite labelled
bivariant/Rees--Čech correspondence category. This entry constructs the six
external pair objects required by entry220 and certifies their coefficient,
Boolean, Tor, endpoint, and adjacent-facet matrices. It does not identify
those external objects with literal entry143 six-functor stalks, and it does
not yet supply triple generic-(Q) coherence. No graph admission is claimed.

## Construction

For every ordered pair of distinct long roads ((i,j)), adjoin an
extraordinary object (W_{ij}). It is not a new (K_6) face: the two long
roads cross. Its finite Rees--Čech presentation consists of the two labelled
branch charts and their relative (mathbf G_m) overlap.

The chain-valued support-switch map sends each Boolean state of (W_{ij})
to the same Boolean state on the two legal edges of the complementary marked
corridor (q_k). The occurrence boundary matrix on outer, middle, and inner
corridor rows is
[
egin{pmatrix}
-1&0\\
1&-1\\
0&1
end{pmatrix}.
]
The middle row cancels, while the endpoint boundary is primitive. The two
chart restrictions to the adjacent long-facet packets are unit maps with
oriented Čech residues ((-1,+1)).

For each of the six orientations there are four normal-circle states. Their
differential is the two-label exterior differential: singleton removal has
sign (-1), top removal has signs ((-1,+1)), and (d^2=0). Both conductor
Tor grades are external spectators. The source and target normal
differentials agree under both chart restrictions, so every adjacent-facet
Beck--Chevalley square commutes in this finite category.

Rotation transports the six objects in two (D_3)-orbits. Polarity reverses
the ordered road pair, the normalization sheet, interval orientation, and
the two residue signs. The endpoint framing is consequently compatible with
the same road-orientation convention already used by the marked corridors.

## Integral matrix

The support-switch top block has 24 columns and 48 legal corridor rows.
Selecting one legal edge row per column gives an integral identity minor, so
the block has rank 24 and 24 nonzero Smith factors, all equal to 1.

Decorating both adjacent-facet restrictions with both Tor grades gives a
96-by-96 signed permutation matrix. It has rank 96 and every nonzero Smith
factor is 1. Hence there is no integer torsion, no factor 2 or 3, and no base
section is inverted.

## Exact remaining gate

This result constructs the local objects and both adjacent-facet BC cells
only in the finite extraordinary category. The next equation is the cyclic
triple/top coherence of the three unoriented pair objects. It must produce
the normalization-provenanced generic (q_Sigma) row and descend the
external road-costalk maps to the literal entry143 filtered target.

Until that triple comparison is constructed, the endpoint/(Q) mapping
fiber is not instantiated. Therefore (p_{partial,Q}), its Bockstein, and
the loaded (D_8)/Jordan tests remain undefined.

## Executable evidence

Checker:
`research/voevodsky/check_dp6_extraordinary_pair_objects.rs`

SHA-256:
`537f24bdf7546eb2c235b00513749b57012c2c8c223ca7baad8ae995a549f1b6`

Fresh rustfmt, warnings-denied Rust compilation, runtime assertions, and JSON
output passed. Native PowerShell was used only because structured-command MCP
was not exposed in this session.

## Outcome contract

~~~json
{
  "claim": "After adjoining six explicitly labelled external Rees-Cech pair objects W_ij, the full 24-state support-switch map and both adjacent-long-facet Beck-Chevalley restrictions are canonical, D3/reflection compatible, saturated, and torsion-free in the finite extraordinary category.",
  "status": "proved_scoped_finite_extraordinary_pair_category",
  "scope": "finite labelled external W_ij correspondence category; no literal entry143 six-functor realization",
  "objects": {
    "ordered_pair_objects": 6,
    "rees_charts_per_object": 2,
    "cech_overlaps_per_object": 1,
    "boolean_columns": 24,
    "legal_corridor_rows": 48,
    "tor_grades": [0,1]
  },
  "beck_chevalley": {
    "adjacent_facet_rows": 48,
    "tor_decorated_matrix_rank": 96,
    "all_nonzero_smith_factors": 1,
    "normal_d_squared": 0,
    "endpoint_framing": true,
    "D3_rotation": true,
    "reflection": true
  },
  "integral_top_matrix": {
    "rows": 48,
    "columns": 24,
    "rank": 24,
    "all_nonzero_smith_factors": 1,
    "torsion": false,
    "base_inversions": false
  },
  "unconstructed": [
    "literal entry143 six-functor realization",
    "three-pair triple/top qSigma coherence",
    "endpoint/Q mapping fiber",
    "p_partial_Q and Bockstein",
    "loaded D8 and Jordan coherence"
  ],
  "checker": "research/voevodsky/check_dp6_extraordinary_pair_objects.rs",
  "checker_sha256": "537f24bdf7546eb2c235b00513749b57012c2c8c223ca7baad8ae995a549f1b6"
}
~~~
