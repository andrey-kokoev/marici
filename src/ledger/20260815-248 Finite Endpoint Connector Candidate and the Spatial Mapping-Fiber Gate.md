# Finite Endpoint Connector Candidate and the Spatial Mapping-Fiber Gate

## Record

Date: 2026-08-16

Status: proved for the finite integral connector presentation and for its
conditional reduced parity consequence. The normalization-provenanced
six-functor restriction into literal entry143 is not constructed, so the
physical endpoint/Q mapping fiber and its class remain undefined. No graph
admission is claimed.

## Finite connector presentation

The ordinary six-chart KN corridor gluing obstruction of entry247 has three
endpoint mismatches and three shifted-center mismatches. Adjoining one
primitive candidate endpoint connector for each road, the three already
available shifted-center homotopies, and the normalized W012 top filler gives
seven nonzero Smith factors, all equal to one. The finite presentation is
integral, has no denominator or torsion, and is compatible with the stated
D3 and reflection permutations.

This is a candidate mapping-cone presentation, not a derivation of the
endpoint connector maps. Its identity endpoint columns encode the required
primitive boundary. A geometric proof still has to identify those columns
with the normalization/log-excess source under an actual support-typed
six-functor restriction to entry143.

## Conditional parity calculation

If that missing restriction extends the intrinsic odd KN counit and the
based qSigma comparison to entry158's pointed mapping fiber, the reduced
endpoint row is [2,1]. Its Smith form is [1]. Positive normalization fixes
the odd coordinate to one, so 2a+1=1 gives a=0. Under this hypothesis,

- p_partial,Q = 0 in H1(D3; Z_or);
- its polarity Bockstein is 0 in H2(D3; Z).

These are conditional consequences, not yet physical invariants. The
four-term generic boundary [1,-1,-1,-1] is primitive and preserves the
augmentation 3-1-1-1=0, but it does not itself construct the required
restriction r_partial,Q.

## Earliest remaining datum

Construct the normalization-provenanced support/nearby-cycle comparison
r_partial,Q from the full source kernel to literal entry143, with the three
endpoint connector columns, the three center homotopies, and the normalized
generic qSigma top living in one Hom complex. Only after its chain,
reflection, and endpoint framing squares are proved may the pointed mapping
fiber be instantiated and the conditional zero promoted to physical p=0.

D8 and Jordan coherence remain downstream of that realization.

## Executable evidence

Checkers:

- `research/voevodsky/check_dp6_global_kn_corridor_descent_no_go.rs`
  SHA-256 `88180223b6c65e364fe086e1a9284ae523644d0b66be31359cc846bc01cd3e5e`
- `research/voevodsky/check_dp6_endpoint_q_mapping_fiber.rs`
  SHA-256 `b5eb4a34f9426615cf6af40e24c91449ea92f780cc7354690f9d85669b039c3a`

Rustfmt and warnings-denied metadata compilation passed for both checkers.
The native linked runtime was not rerun in this increment.

## Outcome contract

~~~json
{
  "claim": "The endpoint and center mismatch presentation admits a primitive torsion-free finite connector candidate; conditional on its missing spatial six-functor realization, the reduced endpoint/Q calculation gives p_partial_Q=0 and Bockstein=0.",
  "status": "proved_scoped_finite_candidate_with_conditional_parity",
  "finite_connector": {
    "endpoint_columns": 3,
    "center_homotopies": 3,
    "top_fillers": 1,
    "nonzero_smith_factors": [1, 1, 1, 1, 1, 1, 1]
  },
  "conditional_mapping_fiber": {
    "row": [2, 1],
    "smith": [1],
    "p_partial_Q": 0,
    "polarity_bockstein": 0
  },
  "physical_mapping_fiber_instantiated": false,
  "physical_p_defined": false,
  "minimal_additional_datum": "normalization-provenanced support/nearby-cycle restriction r_partial_Q deriving the endpoint, center, and generic-Q connector columns in literal entry143",
  "unconstructed": [
    "literal six-functor realization of endpoint connector columns",
    "entry158 pointed endpoint/Q mapping fiber",
    "physical p_partial_Q and Bockstein",
    "D8 covariance of the instantiated fiber",
    "Jordan coherence"
  ]
}
~~~
