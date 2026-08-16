# dP6 Boundary Adjacency No-Go and the Octahedral Log-Correspondence Gate

## Exact adjacency comparison

The entry241 labelled vertex dictionary determines, without an extra
assignment, which two short facets meet each of the six ordered long-road
sectors. It gives twelve sector--short incidences. Every short facet occurs
twice, so these incidences determine six edges between sector vertices.

Those six literal facet-sharing edges are

\[
\{0,2\},\{2,4\},\{4,0\}
\quad\sqcup\quad
\{1,3\},\{3,5\},\{5,1\}.
\]

They are the two parity-sheet triangles. By contrast, entry249's oriented
dP6 boundary edges are

\[
\{0,1\},\{1,2\},\ldots,\{5,0\},
\]

and every one joins opposite parity sheets. The two edge sets are disjoint.
Therefore no dP6 boundary node connector is itself the pair-facet
corestriction required by the literal entry143 short-facet defect.

This falsifies the proposed identification of the oriented dP6 boundary
cycle with the missing \(12\to6\) facet comparison. It does not falsify a
larger log-excess correspondence.

## Minimal combinatorial completion

The union of the six dP6 boundary edges and the six literal sheetwise edges
is

\[
K_6\setminus\{\{0,3\},\{1,4\},\{2,5\}\},
\]

the octahedral graph. It has twelve edges and a canonical completion by
eight triangular faces; every edge occurs in two faces and

\[
6-12+8=2.
\]

Thus the smallest symmetry-compatible carrier containing both already
certified incidence systems is the octahedral two-sphere. Geometrically, the
next datum must be a normalization-provenanced log/excess correspondence
whose one-skeleton contains:

1. the cross-sheet dP6 conductor hexagon;
2. the positive and negative sheetwise facet triangles; and
3. eight Beck--Chevalley two-cells comparing their alternating composites.

Its sheetwise edges must carry the shifted pair-facet Gysin maps of entry245,
while its cross-sheet edges carry the Rees/KN endpoint and center connectors
of entries246 and 249. Only such a two-dimensional comparison can map the
interior top to entry251's canonical lift while deriving all six short
defect rows.

The octahedral completion is presently a forced finite carrier, not yet an
admitted log space or six-functor kernel. Constructing that spatial
realization and its eight loaded two-cells is now the earliest remaining
geometric gate.

## Evidence

- research/voevodsky/check_dp6_literal_facet_adjacency_obstruction.rs
- entries 143, 241, 245, 246, 249, 250, 251, and 252.

~~~json
{
  "status": "falsified_scoped_dp6_boundary_as_literal_facet_clutching",
  "ordered_sectors": 6,
  "sector_short_incidences": 12,
  "literal_short_facet_edges": 6,
  "dp6_boundary_edges": 6,
  "common_edges": 0,
  "literal_edges_same_sheet": true,
  "dp6_edges_cross_sheet": true,
  "minimal_union_graph": "octahedral_K6_minus_matching",
  "union_edges": 12,
  "octahedral_faces": 8,
  "euler_characteristic": 2,
  "octahedral_log_correspondence_constructed": false,
  "global_correspondence_no_go": false,
  "mapping_fiber_instantiated": false,
  "physical_p_defined": false,
  "physical_bockstein_defined": false,
  "D8_Jordan_tested": false,
  "graph_admission_claimed": false
}
~~~
