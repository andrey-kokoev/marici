# Rees Kato–Nakayama Corridor Pushforward and the Global Six-Functor Gate

## Record

Date: 2026-08-16

Status: proved for the proper positive Kato–Nakayama realization of each
multiplicity-sensitive product-branch Rees exceptional interval and its
literal entry143 marked corridor. The six local spatial pushforwards are
integral and symmetry-compatible. Their global attachment to the
normalization/conductor source and generic (Q) target remains unconstructed.
No graph admission is claimed.

## Geometric realization

For the Rees equation
[
cA-abB=0
]
the exceptional (mathbf P^1) has positive KN locus an oriented closed
interval. Its fixed sections ([1:0]) and ([0:1]) are the two adjacent
long-facet restrictions. The labelled overlap ([1:1]) subdivides the
interval into the two edges of the complementary marked corridor.

This subdivision is intrinsic. A diagonal projective rescaling
([A:B]mapsto[alpha A:eta B]) preserving the labelled equation over the
fixed base forces (alpha=eta); it is projectively the identity.
Independent rescaling is not an automorphism of the labelled Rees object.

The resulting proper cellular pushforward is
[
e_Lmapsto(m-o),qquad e_Rmapsto(i-m),
]
with the three vertices mapping identically. Tensoring with the complete
two-normal Boolean packet and both conductor Tor grades yields 240 literal
cell/state rows. The map is the labelled identity, has rank 240, and has 240
unit Smith factors. Ninety-six occurrence-line factors are cancelled by the
tautological principal-dual evaluations; no base section is inverted.

The total cellular–Boolean differential squares to zero. Rotation permutes
the six ordered Rees intervals. Reflection exchanges their endpoints and
reverses both oriented edges, agreeing with the physical road-orientation
twist.

## Scope boundary

This constructs the previously missing **local spatial** KN/log-BM
pair-to-corridor pushforward, including its endpoint and adjacent-facet
restrictions. It does not yet construct one global correspondence over the
normalization/conductor cdh groupoid. In particular, the comparison maps
which identify the six local Rees sources on their conductor overlaps and
attach the normalized (W_{012}	o q_Sigma) top have not been promoted to
a single six-functor kernel.

Therefore the pointed endpoint/(Q) mapping fiber, (p_{partial,Q}), its
Bockstein, and the (D_8)/Jordan tests remain undefined. The next exact gate
is global descent of these six proper KN intervals together with the already
unique shifted top comparison.

## Executable evidence

Checker:
`research/voevodsky/check_dp6_rees_kn_literal_corridor_pushforward.rs`

SHA-256:
`c45584948b419ec38cba59c86f8409c82763db22a6a552e35f5da48fa989464f`

Rustfmt, warnings-denied optimized compilation, linked runtime assertions,
and JSON emission passed. The temporary executable was removed.

## Outcome contract

~~~json
{
  "claim": "The labelled product-branch Rees exceptional P1 has a canonical positive KN interval subdivision whose proper cellular pushforward is the complete literal entry143 marked corridor, compatibly with Boolean normals, both Tor grades, reflection, and D3.",
  "status": "proved_scoped_local_spatial_Rees_KN_to_literal_corridor_pushforward",
  "scope": "six local labelled Rees/KN correspondences; global normalization-conductor descent and Q attachment excluded",
  "matrix": {
    "ordered_cones": 6,
    "corridor_cells_per_cone": 5,
    "boolean_states": 4,
    "tor_grades": [0,1],
    "literal_rows": 240,
    "occurrence_principal_dual_evaluations": 96,
    "rank": 240,
    "smith_unit_factors": 240,
    "torsion": false
  },
  "geometry": {
    "intrinsic_marked_overlap": "[1:1]",
    "independent_Rees_rescaling_allowed": false,
    "proper_positive_KN_pushforward": true,
    "adjacent_facet_restrictions": true,
    "endpoint_restrictions": true,
    "D3": true,
    "reflection": true
  },
  "unconstructed": [
    "global normalization-conductor six-functor descent",
    "global W012/qSigma attachment inside the same kernel",
    "pointed endpoint/Q mapping fiber",
    "p_partial_Q and Bockstein",
    "D8 and Jordan coherence"
  ],
  "checker": "research/voevodsky/check_dp6_rees_kn_literal_corridor_pushforward.rs",
  "checker_sha256": "c45584948b419ec38cba59c86f8409c82763db22a6a552e35f5da48fa989464f"
}
~~~
