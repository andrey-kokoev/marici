# Oriented dP6 Boundary Connectors and the Six-Functor Lift Gate

## Record

Date: 2026-08-16

Status: proved for the normalization-provenanced constructible/log-KN
connector geometry. The algebraic mixed-variance six-functor kernel into
literal entry143 remains unconstructed. No graph admission is claimed.

## Canonical global source geometry

For the regular positive-sheet conductor ideal
(J=(x_1,x_3,x_5)), the projectivized normal cone is the labelled
(mathbf P(J/J^2)congmathbf P^2). Blowing up its three labelled
coordinate points gives the toric del Pezzo surface (dP_6). This operation
is canonical from the labelled conductor directions and uses neither a
choice of road nor division by three.

The certificate now derives this fan rather than supplying its six cones.
It starts from the primitive (mathbf P^2) rays
((1,0),(0,1),(-1,-1)), star-subdivides each adjacent two-cone by the sum
of its rays, and verifies that all six successive determinants are (+1).
The six ordered road sectors and their unique shared labels are then
generated from the cyclic three-road indexing.

Its toric boundary has six nodes. Real-oriented blowup of those nodes
separates the two incident boundary germs and replaces each node by an
oriented connector interval. Consequently the positive KN boundary is a
12-gon alternating:

- six proper Rees/KN corridor intervals from entry246; and
- six node-connector intervals.

The six connector boundaries are derived from the two incident germ images.
Exactly three join the two normalization endpoints and exactly three join
distinct shifted road centers. Thus the connector columns used
conditionally in entry248 are geometric cellular boundaries, not freely
inserted identity equations.

## Integral chain calculation

The twelve target edges telescope around the oriented boundary, so their
total boundary is zero. Their image uses the five target vertices
(v_+,v_-,q_0,q_1,q_2). The target incidence matrix has rank four and four
unit Smith factors, witnessed by a unit spanning tree. The oriented
two-cell filling the 12-gon has primitive boundary coefficients.

Rotation sends boundary cone (i) to (i+2). Reflection sends it to
(1-i) and reverses the boundary orientation. These are precisely the
(D_3) permutation and road-orientation actions already fixed locally.

## Exact scope boundary

This constructs a canonical normalization-provenanced topological/log-KN
source and derives its endpoint and center connector cells. Together with
entry246, every boundary edge has a literal local entry143 corridor image.

It does not yet produce a single algebraic six-functor kernel. The missing
comparison must promote the constructible oriented-boundary pushforward to
the reciprocal-regular/BM-Cech variance of entry143, preserving every
occurrence line, normal circle, conductor Tor grade, and Cech
corestriction. It must also identify the oriented disk filler with the
normalized W012/qSigma top in the same Hom complex.

Therefore entry158's pointed mapping fiber remains uninstantiated. The
entry248 values (p_{partial,Q}=0) and Bockstein zero remain conditional.
D8 and Jordan tests remain downstream.

## Executable evidence

Checker:
`research/voevodsky/check_dp6_oriented_boundary_connector_realization.rs`

SHA-256:
`66a6bb5b6084ecce39d283dd49ebeaf2330450547fb3a0210246f154ca9262ca`

Rustfmt, warnings-denied optimized compilation, linked runtime assertions,
and JSON emission passed.

## Outcome contract

~~~json
{
  "claim": "The labelled conductor normal cone canonically produces a toric dP6 whose real-oriented boundary blowup is a 12-edge KN cycle deriving three endpoint and three center connectors, with primitive integral top coherence and D3/reflection covariance.",
  "status": "proved_scoped_normalization_provenanced_constructible_KN_descent",
  "geometry": {
    "normal_cone": "P(J/J^2)=P2",
    "P2_fan_rays": 3,
    "coordinate_blowups": 3,
    "star_subdivision_rays": 6,
    "smooth_fan_determinants_all_one": true,
    "shared_road_rays_derived": true,
    "surface": "dP6",
    "oriented_boundary_nodes": 6,
    "KN_boundary_edges": 12,
    "local_corridor_edges": 6,
    "endpoint_connectors": 3,
    "center_connectors": 3
  },
  "matrix": {
    "target_vertices": 5,
    "incidence_rank": 4,
    "smith": [1, 1, 1, 1],
    "top_boundary_primitive": true
  },
  "symmetry": {
    "D3": true,
    "reflection_reverses_boundary_orientation": true
  },
  "global_six_functor_kernel_constructed": false,
  "mapping_fiber_instantiated": false,
  "minimal_additional_datum": "a mixed-variance six-functor realization of the oriented dP6 boundary and disk into literal entry143, preserving all occurrence/normal/Tor/Cech rows and the normalized qSigma top",
  "unconstructed": [
    "literal global six-functor kernel",
    "pointed endpoint/Q mapping fiber",
    "physical p_partial_Q and Bockstein",
    "D8 covariance",
    "Jordan coherence"
  ],
  "checker": "research/voevodsky/check_dp6_oriented_boundary_connector_realization.rs",
  "checker_sha256": "66a6bb5b6084ecce39d283dd49ebeaf2330450547fb3a0210246f154ca9262ca"
}
~~~
