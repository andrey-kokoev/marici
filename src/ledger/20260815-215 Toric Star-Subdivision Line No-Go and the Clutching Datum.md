# Toric Star-Subdivision Line No-Go and the Clutching Datum

## Record

Date: 2026-08-15

Status: falsified the direct toric star-subdivision realization without an
additional clutching/excess line. This is not a no-go for enlarged
log-BM, nearby-cycle, or derived correspondences. No graph admission is
claimed.

## Earliest exact obstruction

The finite matrix of entry 214 suggests subdividing each ordered (dP_6)
log-link interval at a canonical middle point. The most economical algebraic
realization is the toric blowup of the intersection of its two adjacent
boundary divisors. Its new ray is the primitive sum of the adjacent rays, so
the construction is saturated and multiplicity one.

However, if the ordered pair is ((i,j)) and (k) is the omitted road, the
exceptional section has multidegree
[
e_i+e_j,
]
whereas the second marked-corridor edge requires the independent long-road
coordinate of degree
[
e_k.
]
Over the universal nonnegatively multigraded coefficient ring, neither
difference (e_k-e_i-e_j) nor (e_i+e_j-e_k) is a polynomial degree.
Therefore no section-preserving homogeneous multiplication map exists in
either direction between the two embedded principal lines.

Entry 164's incidence equation
[
y_kG=z_kH_k
]
does not supply a unit clutching on the conductor: at (G=0) it becomes
(z_kH_k=0). Converting it into a line isomorphism requires a ratio or a
separately supplied excess/nearby-cycle transformation.

The obstruction holds for all six ordered cones and is preserved by rotation
and polarity. It is not caused by nonsaturation or integer torsion: every
star ray is primitive.

## Scoped theorem

Consequently the direct construction

1. torically star-subdivide the ordered cone;
2. identify its exceptional divisor line with the complementary road line;
3. push its two subintervals to the marked corridor

cannot realize (Gamma_{ij}^{!,log}) over the frozen universal coefficient
base. The first unsupported step is exactly step 2.

The finite Gysin matrix of entry 214 remains valid as a labelled coefficient
model. What is missing is a normalization-provenanced, branch-selected
clutching/excess morphism between the exceptional line and the complementary
long-road line, compatible with (y_kG=z_kH_k) and nonvanishing on the
conductor. A log nearby-cycle kernel could supply such a morphism; present
data do not.

Thus the literal adjacent-facet Beck--Chevalley rows, generic (q_Sigma)
connector, endpoint/Q mapping fiber, physical parity, Bockstein, and
(D_8)/Jordan tests remain unavailable.

## Certificate

Executable:
`research/voevodsky/check_dp6_star_subdivision_line_no_go.rs`

SHA-256:
`11860379f4d9cd8f01ff1cc1b5a92f50e9ae18a434e6d1b061a515bee07d4a9d`

Rustfmt, warnings-denied optimized compilation, runtime assertions, and JSON
parsing passed. Native PowerShell was used only because structured-command MCP
was unavailable.

## Outcome contract

~~~json
{
  "claim": "The direct toric star subdivision of an ordered dP6 cone cannot realize the marked-corridor support switch over the universal multigraded base: its exceptional line has degree e_i+e_j while the required complementary long-road line has independent degree e_k, and the conductor incidence relation supplies no unit clutching.",
  "status": "falsified_scoped_direct_toric_star_subdivision",
  "scope": "direct section-preserving toric blowup realization without extra clutching/excess data",
  "factorization": {
    "ordered_cones_checked": 6,
    "star_rays_primitive": true,
    "exceptional_degree": "e_i+e_j",
    "corridor_degree": "e_k",
    "forward_polynomial_map": "absent",
    "reverse_polynomial_map": "absent",
    "conductor_incidence": "z_k H_k=0",
    "integer_torsion": "none",
    "finite_entry214_matrix": "still valid",
    "global_log_BM_no_go": false
  },
  "minimal_additional_datum": "A normalization-provenanced branch-selected clutching/excess morphism between the exceptional line and the complementary long-road line, compatible with y_k G=z_k H_k and nonvanishing on the conductor.",
  "evidence_refs": [
    "research/voevodsky/check_dp6_star_subdivision_line_no_go.rs",
    "src/ledger/20260815-164 Paired-Incidence Descent and the Reduced cdh Vertex Connector.md",
    "src/ledger/20260815-214 Finite Ordered Log-Link Gysin Matrix and the Spatial Realization Gate.md"
  ],
  "checker_sha256": "11860379f4d9cd8f01ff1cc1b5a92f50e9ae18a434e6d1b061a515bee07d4a9d",
  "next_experiment": "Construct or falsify a branch-selected nearby-cycle/Rees clutching line whose special-fibre counit identifies the exceptional degree e_i+e_j with the complementary road degree e_k without localization."
}
~~~
