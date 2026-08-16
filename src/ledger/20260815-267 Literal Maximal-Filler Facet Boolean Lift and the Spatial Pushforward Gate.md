# Literal Maximal-Filler Facet Boolean Lift and the Spatial Pushforward Gate

## Complete facet-state matrix

Entry266 pairs the 18 oriented facet occurrences into two copies of every
one of the nine K6 facets. The literal entry143 packet on a facet labelled by
one diagonal has two Boolean states and two retained Tor grades.

Lifting all occurrences therefore gives 72 assignment occurrences onto 36
distinct literal facet generators. Every target generator occurs exactly
twice, so the 36 Beck--Chevalley equality rows are disjoint primitive
[1,-1] rows. Their matrix has rank 36, 36 unit Smith factors, and no integer
torsion.

The six short-diagonal facets are pentagons and the three long-diagonal
facets are squares, giving 42 boundary edges. Across both occurrences, both
Boolean states, and both Tor grades, the checker derives 336 literal radial
Cech rows and 36 normal-removal rows. It verifies all 168 radial/normal mixed
squares: the entry143 normal signs at support sizes one and two are opposite,
so the two orders cancel integrally.

The complete two-dimensional finite literal lift is D3- and
reflection-stable.

## Remaining geometric realization

The cellular and BM-Cech matrices are now fixed through maximal-cone degree.
What remains is not another finite incidence choice. It is the support-typed
proper/log-excess transformation from the normalization-provenanced
product-branch Rees Cech carrier into these literal entry143 generators.

That transformation must realize the already certified 336 radial rows,
36 normal rows, and 36 paired-facet BC equalities, restrict to the
three-segment edge lift of entry265, and preserve endpoint framing. Until
this pushforward is constructed, the generic Q top and pointed endpoint/Q
mapping fiber remain uninstantiated.

## Evidence

- research/voevodsky/check_maximal_fillers_literal_facet_boolean_lift.rs
- entries 143 and 259-266.

~~~json
{
  "status": "proved_scoped_literal_maximal_filler_facet_Boolean_lift",
  "facets": 9,
  "short_pentagons": 6,
  "long_squares": 3,
  "facet_boundary_edges": 42,
  "facet_occurrences": 18,
  "state_Tor_assignment_occurrences": 72,
  "distinct_literal_facet_generators": 36,
  "paired_facet_BC_equalities": 36,
  "BC_matrix_rank": 36,
  "BC_smith_unit_factors": 36,
  "radial_Cech_rows": 336,
  "normal_rows": 36,
  "mixed_square_checks": 168,
  "integer_torsion": false,
  "D3": true,
  "reflection": true,
  "spatial_Rees_to_entry143_BC_constructed": false,
  "global_endpoint_Q_map_constructed": false,
  "mapping_fiber_instantiated": false,
  "physical_p_defined": false,
  "physical_bockstein_defined": false,
  "D8_Jordan_tested": false,
  "graph_admission_claimed": false
}
~~~
