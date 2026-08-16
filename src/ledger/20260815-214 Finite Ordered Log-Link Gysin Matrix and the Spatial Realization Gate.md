# Finite Ordered Log-Link Gysin Matrix and the Spatial Realization Gate

## Record

Date: 2026-08-15

Status: proved inside the finite labelled log/KN coefficient model. The
proper/log-BM six-functor realization remains unconstructed. No graph
admission is claimed.

## Construction

For each of the six oriented maximal cones of the (dP_6) boundary, take its
oriented log-link interval
[
d e=c-o.
]
Entry 210 fixes the complementary marked half-corridor and entry 213 fixes its
normalization-provenanced occurrence lines. Write its two edges as
[
d a=m-o,qquad d b=c-m.
]
The primitive Gysin map is forced by the boundary labels:
[
elongmapsto a+b,qquad olongmapsto o,qquad clongmapsto c.
]
Therefore (dGamma(e)=c-o=Gamma(de)), with the middle terms cancelling
integrally.

Tensor this map with the complete two-normal Boolean packet. The Koszul tensor
sign on the occurrence edge and the entry143 normal-removal signs give a
chain map on every generator. This produces 72 source generators, 120 target
generators, and 72 checked chain-map equations. Its top part is the requested
24-column to 48-row matrix: every source column is the primitive vector
((1,1)) on its two legal corridor edges.

## Integral matrix

The top matrix has rank 24. Choosing the first row of every two-row block
gives an identity minor, so its Smith form has 24 unit factors, no torsion,
and free cokernel rank 24.

The complete matrix has rank 72. Choosing the first-edge, outer-vertex, and
central-vertex rows in every Boolean/cone block gives an identity
(72	imes72) minor. Thus its Smith form has 72 unit factors, no integer
torsion, and free cokernel rank 48.

The endpoint restrictions are the outer and central identity rows in this
finite labelled model. The two conductor Tor grades remain spectators; they
are retained and are not consumed or double-counted. No occurrence or normal
section is inverted.

## Exact boundary

This establishes the unique primitive finite log-link Gysin matrix after the
support and occurrence-line dictionaries are fixed. It does not prove that
this matrix is induced by a proper/log-BM or nearby-cycle correspondence into
the literal entry143 six-functor diagram. In particular, the geometric
Beck--Chevalley comparison with the adjacent long-facet packets is still
missing. The finite endpoint identities cannot be promoted to physical
endpoint framing cells until that comparison exists.

Accordingly the generic (q_Sigma) connector, endpoint/Q mapping fiber,
(p_{partial,Q}), Bockstein, and (D_8)/Jordan coherence remain undefined.

## Certificate

Executable:
`research/voevodsky/check_dp6_finite_log_gysin_matrix.rs`

SHA-256:
`70e58ea31a9fe9a34833843b13e794cb85211e02d484ffdf6b012ef4376ca865`

Native PowerShell was used only because structured-command MCP was unavailable.
Rustfmt, warnings-denied optimized compilation, runtime assertions, and JSON
parsing passed.

## Outcome contract

~~~json
{
  "claim": "After the normalization-provenanced support and line dictionaries are fixed, the six ordered log links admit a unique primitive finite Gysin map to the marked half-corridors; tensoring with all Boolean normal states gives a 48x24 top matrix with Smith form 1^24 and a 120x72 full matrix with Smith form 1^72.",
  "status": "proved_scoped_finite_log_kn_model",
  "scope": "finite labelled log-link/KN coefficient model; no proper spatial six-functor realization",
  "matrix": {
    "source_generators": 72,
    "target_generators": 120,
    "chain_map_equations": 72,
    "top_shape": [48, 24],
    "top_rank": 24,
    "top_smith": "24 unit factors",
    "top_torsion": "none",
    "top_cokernel_free_rank": 24,
    "full_shape": [120, 72],
    "full_rank": 72,
    "full_smith": "72 unit factors",
    "full_torsion": "none",
    "full_cokernel_free_rank": 48
  },
  "factorization": {
    "normal_d_squared": 0,
    "endpoint_restrictions": "identity rows in finite labelled model",
    "Tor_grades": [0, 1],
    "base_inversions": false,
    "proper_log_BM_realization": "unconstructed",
    "literal_entry143_comparison": "unconstructed",
    "physical_mapping_fiber": "unconstructed"
  },
  "evidence_refs": [
    "research/voevodsky/check_dp6_finite_log_gysin_matrix.rs",
    "research/voevodsky/check_dp6_incidence_line_to_corridor.rs",
    "src/ledger/20260815-210 Ordered dP6 Log Links and the Marked Half-Corridor Support Switch.md",
    "src/ledger/20260815-213 Paired-Incidence Lines on the Ordered Marked Corridors.md"
  ],
  "checker_sha256": "70e58ea31a9fe9a34833843b13e794cb85211e02d484ffdf6b012ef4376ca865",
  "next_experiment": "Construct or falsify a proper/log-BM seed realization whose costalk matrix is this primitive block and whose two boundary restrictions are the independently constructed adjacent long-facet packets."
}
~~~
