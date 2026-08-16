# Cross-Sheet Geodesic Full Boolean Lift Matrix and the Spatial Rees BC Gate

## Literal finite lift

Entry264 gives six unique three-segment K6 geodesics. Pulling the literal
entry143 Boolean packets over their 18 flip segments determines the complete
finite coefficient lift.

Every segment has a two-label common face. Its two radial maps add the unique
missing endpoint label, so all 288 radial rows have the legal Cech
coefficient for that added label. At the twelve internal-vertex occurrences,
the two adjacent edge cubes cover six of the eight Boolean states. The two
missing states in both Tor grades give 48 assignment occurrences.

These 48 occurrences land in 36 distinct literal target generators. Exactly
12 are repeated internal full-state assignments. Their equality conditions
are primitive rows of type [1,-1]. Therefore the BC block has rank 12 with
12 unit Smith factors, while the target assignment block has rank 36 with
36 unit Smith factors. There is no integral torsion.

The checker also verifies the normal differential squares to zero on all 96
internal complete Boolean cubes and that the construction is stable under
D3 and reflection.

## Remaining geometric arrow

This is a literal finite BM-Cech matrix, not yet the geometric
normalization/log-excess realization. The strongest existing source is the
product-branch Rees Cech carrier of entries 216 through 219. The first absent
map is the support-typed transformation

BC_Rees,143: R pi_! Tot(U_ab <- U_cross -> U_c) -> F_B/F_V.

It must realize the 288 radial rows, 48 assignments, and 12 internal
equalities derived here while preserving both adjacent long-facet packets,
endpoint framing, and both Tor grades. The finite matrix proves that no
integer or Smith obstruction remains after such a spatial comparison is
constructed; it does not supply that comparison.

## Evidence

- research/voevodsky/check_cross_sheet_geodesic_full_boolean_lift.rs
- entries 143, 216-219, 262-264.

~~~json
{
  "status": "proved_scoped_cross_sheet_geodesic_full_Boolean_lift_matrix",
  "geodesics": 6,
  "segments": 18,
  "radial_Cech_rows": 288,
  "missing_state_assignment_occurrences": 48,
  "distinct_literal_target_generators": 36,
  "internal_BC_equalities": 12,
  "BC_matrix_rank": 12,
  "BC_smith_unit_factors": 12,
  "assignment_matrix_rank": 36,
  "assignment_smith_unit_factors": 36,
  "integer_torsion": false,
  "normal_d_squared_checks": 96,
  "D3": true,
  "reflection": true,
  "spatial_Rees_to_entry143_BC_constructed": false,
  "global_maximal_cone_gluing_constructed": false,
  "mapping_fiber_instantiated": false,
  "physical_p_defined": false,
  "physical_bockstein_defined": false,
  "D8_Jordan_tested": false,
  "graph_admission_claimed": false
}
~~~
