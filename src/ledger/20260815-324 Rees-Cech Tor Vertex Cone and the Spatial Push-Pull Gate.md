# Rees--Čech Tor Vertex Cone and the Spatial Push--Pull Gate

## Record

Date: 2026-08-15

Status: proved in the finite labelled product-Rees/Čech/Tor
totalization and literal entry143 incidence/Boolean complex. The
vertex-supported cone repairs entry323's direct third-edge chain failure.
Proper log-BM six-functor provenance and the literal occurrence-line radial
comparison remain unconstructed. No graph admission is claimed.

## Correct totalization

The Rees overlap cannot map directly to the third edge because
\[
d_{\check C}U_\times=-U_0+U_1.
\]
Instead, map the overlap/Tor total generator to the common legal
triangulation vertex.

After the primitive log-excess cap, the three axes are
\[
(\tau,n_0,n_1).
\]
Here \(\tau\) is the conductor Tor direction and \(n_0,n_1\) are the
two chart-normal directions. With the fixed ordered-pair orientation, the
total boundary is
\[
D=\iota_\tau+\iota_{n_0}-\iota_{n_1}.
\]
The last two terms are the two Čech chart restrictions
\((-U_0,+U_1)\); the first is the wall/third-edge restriction. Since
exterior contractions anticommute,
\[
D^2=0.
\]

The unique axis dictionary of entry322 sends \(\tau\) to the persistent
corridor label and \(n_0,n_1\) to the two moving labels. Therefore the
cone has the literal entry143 three-label Boolean packet, while its three
boundary terms land on exactly the three codimension-one faces of that
vertex.

## Integral certification

Across six ordered pairs:

- the cone-to-vertex map is a \(48\times48\) labelled identity;
- it has rank 48 and 48 unit Smith factors;
- the total boundary has 72 rows, split into 48 chart rows and 24 wall rows;
- its rank is 42, with 42 unit Smith factors;
- all 72 two-step boundary equations cancel integrally;
- no base section or integer is inverted.

The empty state is the sole zero column in each \(12\times8\) boundary
block. Each of the seven nonempty states has a distinct unit pivot obtained
by contracting its least present axis.

## Degree and symmetry

The wall term combines overlap Čech degree \(+1\) with Tor contraction
degree \(-1\), hence has total degree zero. Physical reflection reverses
both orientation lines, so the loaded wall sign is \((-1)(-1)=+1\).

Rotation and physical reflection preserve all six completed vertex stars.
They may exchange chart and wall roles, but the combined totalization
retains degree zero and the fixed loaded sign. This is the finite derived
mechanism absent from the two-edge truncation.

## Remaining geometric gate

The finite cone is not yet a spatial six-functor theorem. A genuine
correspondence must construct a proper/log-BM kernel whose exceptional
vertex stratum realizes this cone and whose three boundary maps are the
literal entry143 extraordinary corestrictions.

The decisive unverified rows are the occurrence directions. Entry143
radial maps carry principal occurrence sections, whereas the Čech boundary
has unit coefficients. The spatial kernel must provide the corresponding
principal-line duals and Gysin evaluations and prove proper
Beck--Chevalley naturality; these evaluations may not be replaced by scalar
identities in advance.

Once that push--pull is constructed, its endpoint restrictions can be
compared with the established odd endpoint counits, and its three-road top
can be attached to the based \(q_\Sigma\) row. Until then the pointed
endpoint/\(Q\) mapping fiber and all downstream parity and coherence
classes remain undefined.

## Executable evidence

Checker:
`research/voevodsky/check_dp6_rees_cech_tor_vertex_cone.rs`

SHA-256:
`60ed787ae2baf4e73aeeb983d35f39cb22737b631ec2bb13537b6fa3a13d71d1`

Fresh `rustfmt --check`, warnings-denied optimized compilation, runtime
assertions, and JSON field checks passed. Native PowerShell was used for
Rust verification because no repository-scoped structured-command MCP
capable of invoking `rustc` is exposed.

## Outcome contract

~~~json
{
  "claim": "The correct finite derived repair maps the Rees-Cech/Tor overlap totalization to the common literal vertex cone, with total boundary i_tau+i_n0-i_n1. This gives a primitive 48-row vertex realization and a saturated 72-row full-star boundary with d squared zero, D3 covariance, and physical-reflection closure.",
  "status": "proved_scoped_finite_rees_cech_tor_vertex_cone",
  "scope": "finite labelled Rees-Cech/Tor totalization and literal entry143 incidence/Boolean complex; proper log-BM six-functor realization excluded",
  "matrix": {
    "ordered_pairs": 6,
    "vertex_rows": 48,
    "vertex_rank": 48,
    "vertex_smith_factors": 48,
    "boundary_rows": 72,
    "chart_rows": 48,
    "wall_rows": 24,
    "boundary_rank": 42,
    "boundary_smith_factors": 42,
    "d_squared": 0,
    "base_inversions": false
  },
  "degree_and_symmetry": {
    "cech_degree": 1,
    "tor_contraction_degree": -1,
    "wall_total_degree": 0,
    "reflection_cech_sign": -1,
    "reflection_tor_sign": -1,
    "reflection_loaded_sign": 1,
    "D3_full_star": true,
    "physical_reflection_full_star": true
  },
  "unconstructed": [
    "proper log-BM six-functor realization",
    "literal occurrence-line radial Gysin maps",
    "endpoint extensions",
    "based qSigma connector",
    "endpoint/Q mapping fiber",
    "p_partial_Q and Bockstein",
    "D8 and Jordan coherence"
  ],
  "checker": "research/voevodsky/check_dp6_rees_cech_tor_vertex_cone.rs",
  "checker_sha256": "60ed787ae2baf4e73aeeb983d35f39cb22737b631ec2bb13537b6fa3a13d71d1"
}
~~~
