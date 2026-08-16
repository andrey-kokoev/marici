# Rees Kato–Nakayama Abstract Corridor Packet and the Literal Cell-Assignment Gate

## Correction

Date: 2026-08-16

The checker proves the positive Kato–Nakayama five-cell packet of each
multiplicity-sensitive product-branch Rees exceptional interval. It does not
enumerate K6 faces or entry143 `[S,H]` generators. The earlier wording that
called its declared five-cell basis a literal entry143 spatial pushforward
was too strong and is retracted here.

For the labelled Rees equation
[
cA-abB=0,
]
the positive exceptional (mathbf P^1) is an oriented interval with fixed
sections ([1:0]), ([0:1]), and intrinsic marked overlap ([1:1]).
Preservation of the labelled equation forces any diagonal projective
rescaling to be common, so it is projectively trivial.

The abstract packet has vertices (o,m,i), edges (e_L,e_R), and
[
d e_L=m-o,qquad d e_R=i-m.
]
Tensoring with the complete two-normal Boolean packet and both conductor Tor
grades gives 240 abstract labelled rows. The coefficient matrix is the
identity, has rank 240, and has 240 unit Smith factors. Ninety-six
occurrence-line factors cancel by principal-dual evaluation; no base section
or integer is inverted. The total cellular–Boolean differential squares to
zero, and rotation/reflection preserve the packet.

## Exact remaining gate

No function in the checker maps (o,m,i,e_L,e_R) to actual K6 faces or to
entry143 generators. Consequently it proves neither literal endpoint/facet
restrictions nor a spatial corestriction square.

The first missing datum is a support-typed assignment from each Rees/KN
packet to an actual marked K6 corridor, expanded on every occurrence,
normal-circle, Tor, and Čech state. It must then be compared on overlaps and
attached to the generic (Q) top. Entries 258–260 show that an ordinary
face-poset assignment cannot provide the cross-sheet and maximal-cone cells;
the eventual map must be extraordinary/mixed-variance.

Until that assignment exists, the global normalization kernel, pointed
endpoint/Q mapping fiber, (p_{partial,Q}), its Bockstein, and the
(D_8)/Jordan tests remain undefined.

## Executable evidence

Checker:
`research/voevodsky/check_dp6_rees_kn_literal_corridor_pushforward.rs`

The current checker output explicitly records that K6 faces and entry143
generators are not enumerated and that the literal cell assignment is
unconstructed.

## Outcome contract

~~~json
{
  "claim": "The labelled product-branch Rees exceptional P1 has a canonical positive KN five-cell subdivision with a saturated abstract corridor packet, compatibly with Boolean normals, both Tor grades, reflection, and D3.",
  "status": "proved_scoped_positive_KN_Rees_abstract_corridor_packet",
  "scope": "six local labelled Rees/KN abstract five-cell packets; literal K6/entry143 cell assignment, global normalization-conductor descent, and Q attachment excluded",
  "matrix": {
    "ordered_cones": 6,
    "corridor_cells_per_cone": 5,
    "boolean_states": 4,
    "tor_grades": [0, 1],
    "abstract_labelled_rows": 240,
    "occurrence_principal_dual_evaluations": 96,
    "rank": 240,
    "smith_unit_factors": 240,
    "torsion": false
  },
  "geometry": {
    "intrinsic_marked_overlap": "[1:1]",
    "independent_Rees_rescaling_allowed": false,
    "proper_positive_KN_packet": true,
    "D3": true,
    "reflection": true
  },
  "K6_faces_enumerated": false,
  "entry143_generators_enumerated": false,
  "literal_entry143_cell_assignment_constructed": false,
  "unconstructed": [
    "literal K6 face and entry143 [S,H] cell assignment",
    "global normalization-conductor six-functor descent",
    "global W012/qSigma attachment inside the same kernel",
    "pointed endpoint/Q mapping fiber",
    "p_partial_Q and Bockstein",
    "D8 and Jordan coherence"
  ],
  "checker": "research/voevodsky/check_dp6_rees_kn_literal_corridor_pushforward.rs",
  "graph_admission_claimed": false
}
~~~
