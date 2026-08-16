# Unique Cross-Sheet K6 Geodesics and the Three-Segment Excess Lift Gate

## Canonical carrier repair

Entry263 rules out gluing a cross-sheet edge by two existing half-gallery
arms. The full literal K6 flip graph nevertheless supplies a canonical
replacement.

For every admissible cross-sheet pair with different road labels and
opposite signs, the two ordered-sector middle triangulations have distance
three in the K6 flip graph and possess exactly one shortest path. Thus each
of the six cross-sheet toric edges has a uniquely determined three-segment
literal K6 subdivision. The six paths form one D3-covariant family, and
reflection maps each oriented path to the corresponding reflected path.

This removes the carrier-chain choice without selecting a road, diagonal,
or boundary primitive. The resulting 18 literal flip edges are all genuine
K6 incidences.

## Remaining excess lift

The unique carrier paths do not by themselves construct the required
full-log correspondence. Along each three-segment path the exchanged normal
label changes at every flip. One must lift the subdivision through the full
Boolean replacement of entry262, retain both Tor grades, and prove that the
two internal-vertex restrictions agree as Beck--Chevalley maps.

Equivalently, the minimal new geometric datum can now be reduced from six
arbitrary bridges to one D3-seed three-segment log/DNC bridge whose literal
carrier is the certified geodesic. Its stabilizer and reflection squares
must be proved before transporting it to the other five pairs.

Until that lift is constructed, the eight maximal-cone equations and the
endpoint/Q mapping fiber remain uninstantiated.

## Evidence

- research/voevodsky/check_cross_sheet_unique_k6_geodesics.rs
- entries 143, 259, 262, and 263.

~~~json
{
  "status": "proved_scoped_unique_literal_K6_cross_sheet_geodesics",
  "K6_vertices": 14,
  "cross_sheet_pairs": 6,
  "shortest_length": 3,
  "shortest_paths_per_pair": 1,
  "subdivision_edges": 18,
  "D3_orbit": true,
  "reflection_covariant": true,
  "carrier_choice": false,
  "full_Boolean_excess_lift_constructed": false,
  "global_maximal_cone_gluing_constructed": false,
  "mapping_fiber_instantiated": false,
  "physical_p_defined": false,
  "physical_bockstein_defined": false,
  "D8_Jordan_tested": false,
  "graph_admission_claimed": false
}
~~~
