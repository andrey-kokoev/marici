# Full-Log Maximal-Cone K6 Fillers and the Nine Facet BC Gate

## Canonical two-dimensional carrier

Entries264 and 265 fix the literal image of every edge in the full-log
octahedral fan. The boundary of each of its eight maximal cones can therefore
be evaluated in the complete 14-vertex, 21-edge K6 flip graph.

The two all-positive and all-negative cones collapse through their common
sheet endpoint, so their carrier boundary is zero. Each of the six mixed
cones gives an eight-edge loop. Exhaustive integral solution against the
nine associahedral facet boundaries shows that every mixed loop has a unique
minimum-support filler consisting of three oriented facets.

Across all six mixed cones there are 18 facet occurrences. Every one of the
nine K6 facets occurs exactly twice. Identifying the two occurrences gives
nine disjoint primitive BC rows of type [1,-1], hence rank nine, nine unit
Smith factors, and no integer torsion.

The second carrier layer is therefore canonical after the unique-geodesic
edge subdivision: two zero fillers and six unique minimal three-facet
patches.

## Remaining literal and geometric lift

The checker certifies the complete cellular carrier matrix, but it does not
yet distribute each oriented facet through all literal entry143 Boolean,
Tor, and Cech states. That full packet must restrict to the edge matrices of
entry265 and prove the nine paired-facet BC equations state by state.

After that finite lift, the still-essential geometric arrow remains the
proper/log-excess comparison from the product-branch Rees Cech carrier into
the literal entry143 BM-Cech diagram. Without that spatial map the carrier
fillers cannot be promoted to the requested normalization-provenanced global
chain map.

## Evidence

- research/voevodsky/check_full_log_maximal_cone_k6_fillers.rs
- entries 143 and 259-265.

~~~json
{
  "status": "proved_scoped_full_log_maximal_cone_K6_fillers",
  "K6_vertices": 14,
  "K6_edges": 21,
  "K6_facets": 9,
  "maximal_cones": 8,
  "same_sheet_zero_fillers": 2,
  "mixed_cones": 6,
  "mixed_loop_edge_support": 8,
  "minimal_facets_per_mixed_filler": 3,
  "minimal_fillers_per_mixed_cone": 1,
  "facet_occurrences": 18,
  "distinct_facets": 9,
  "occurrences_per_facet": 2,
  "facet_BC_equalities": 9,
  "facet_BC_rank": 9,
  "facet_BC_smith_unit_factors": 9,
  "integer_torsion": false,
  "literal_full_Boolean_facet_lift_constructed": false,
  "global_endpoint_Q_map_constructed": false,
  "mapping_fiber_instantiated": false,
  "physical_p_defined": false,
  "physical_bockstein_defined": false,
  "D8_Jordan_tested": false,
  "graph_admission_claimed": false
}
~~~
