# Cross-Polytope Literal-Support No-Go and the Fourteen Extraordinary Cells Gate

## Literal support census

The six cross-polytope vertices already map to the six exact entry329
triangulation vertices. The eight triangular faces of entry336 therefore
have a fully determined literal K6 support census.

The two pure-sheet faces have three pairwise intersections, each a genuine
one-label short facet. Every mixed face has:

- one same-sheet edge with a one-label short-facet intersection; and
- two cross-sheet edges whose endpoint triangulations have empty
  intersection.

After dividing by the fact that every octahedral edge belongs to two faces,
the twelve distinct edges split as:

\[
6\ \text{sheetwise supported edges}
\quad\sqcup\quad
6\ \text{cross-sheet edges with empty common support}.
\]

Moreover, the intersection of the three endpoint triangulations is empty
for every one of the eight faces.

Entry143's ordinary face-poset diagram has generators only for literal
compatible faces and their inclusions. Hence it contains neither an
ordinary common-support corestriction for the six cross-sheet edges nor an
ordinary face object for any of the eight triangular BC cells. The
cross-polytope cannot be realized by an ordinary support-preserving functor.

## Scoped no-go and minimal datum

This is a scoped no-go for ordinary face-poset realization, not for the
requested bivariant/log-excess construction.

The minimal spatial enlargement has fourteen extraordinary cells:

1. six cross-sheet edge correspondences landing in supported road/endpoint
   costalks despite empty common face support; and
2. eight triangular Beck--Chevalley two-cells whose boundaries compare
   those cross edges with the six already supported sheetwise Gysin edges.

The empty triple intersection explains why the interior Gysin class of
entry337 cannot be sent to the literal generic top merely by a poset map.
The eight face maps must instead land through an extraordinary
generic-costalk/nearby-cycle transformation and jointly identify their
primitive boundary with entry251's six-term short-facet defect.

All occurrence ideals, normal circles, conductor Tor grades, Čech
localizations, endpoint frames, and symmetry signs must be carried by these
fourteen transformations. Until they exist in one Hom complex, the global
chain map and endpoint/Q mapping fiber remain uninstantiated.

## Evidence

- research/voevodsky/check_cross_polytope_literal_support_no_go.rs
- entries 143, 249, 251, 253, 256, 329, 333--334, 336, and 257.

~~~json
{
  "status": "falsified_scoped_ordinary_face_poset_realization",
  "octahedral_faces": 8,
  "pure_sheet_faces": 2,
  "mixed_faces": 6,
  "pair_incidences_with_one_label_support": 12,
  "distinct_sheetwise_supported_edges": 6,
  "pair_incidences_with_empty_support": 12,
  "distinct_cross_sheet_unsupported_edges": 6,
  "triple_support_empty_faces": 8,
  "ordinary_cross_edge_corestrictions_exist": false,
  "ordinary_face_corestrictions_exist": false,
  "extraordinary_cross_edge_and_face_maps_required": true,
  "global_extraordinary_correspondence_no_go": false,
  "mapping_fiber_instantiated": false,
  "physical_p_defined": false,
  "physical_bockstein_defined": false,
  "D8_Jordan_tested": false,
  "graph_admission_claimed": false
}
~~~
