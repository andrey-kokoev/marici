# Degree-Two Full-Log Carrier and the Central Exceptional Primitive Repair

## Oriented degree

The coherently oriented maximal-cone fillers of entry266 sum to twice the
primitive K6 fundamental sphere. The full-log carrier therefore reaches the
generic target top with coefficient two, not one.

This factor is derived from the signed-ray determinant orientations and all
nine facet coefficients. It is not the unsigned fact that every facet occurs
twice.

## Primitive exceptional repair

Entry176 independently proves that the central exceptional relative cap has
normalized coefficient +1. Adjoining it to the degree-two carrier gives the
top/framing row

    [2, 1].

Its Smith form is [1], so the row is saturated and has zero cokernel. With
the certified central value k=1, the primitive top equation

    2 a + k = 1

has carrier coordinate a=0. The corresponding finite local top parity is
zero.

This is the exact integral mechanism that repairs the global degree-two
carrier without division by two.

## Remaining support gate

The calculation does not identify the central exceptional generator with
the literal entry143 generic-top/endpoint-Q defect. Entry176 explicitly
leaves that spatial comparison unconstructed. Therefore the zero computed
here is a local augmented-top coordinate, not the physical
p_partial_Q.

The next required arrow is a support-typed proper/log-excess comparison that
simultaneously realizes the facet lift of entry343 and transports the
central exceptional unit into the literal generic-Q top. Only then can the
pointed endpoint/Q mapping fiber be instantiated.

## Evidence

- research/voevodsky/check_full_log_maximal_cone_k6_fillers.rs
- research/voevodsky/check_degree_two_central_exceptional_repair.rs
- entries 143, 176, 266, and 267.

~~~json
{
  "status": "proved_scoped_degree_two_central_exceptional_repair",
  "carrier_degree": 2,
  "central_coefficient": 1,
  "augmented_row": [2, 1],
  "smith_factors": [1],
  "cokernel": 0,
  "normalized_central_k": 1,
  "carrier_coordinate": 0,
  "local_top_parity": 0,
  "spatial_central_to_entry143_top_map_constructed": false,
  "mapping_fiber_instantiated": false,
  "physical_p_defined": false,
  "physical_bockstein_defined": false,
  "D8_Jordan_tested": false,
  "graph_admission_claimed": false
}
~~~
