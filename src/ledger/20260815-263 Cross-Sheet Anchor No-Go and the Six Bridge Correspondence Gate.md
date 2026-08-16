# Cross-Sheet Anchor No-Go and the Six Bridge Correspondence Gate

## Exact obstruction after the local Boolean repair

Entry262 constructs the full eight-state Boolean packet on each of the six
literal half-galleries.  This does not yet construct the six cross-sheet
two-cones of the full-log toric source.

Index a toric ray by a road and a sheet sign, ((D,epsilon)).  Associate to
it the two literal anchors of the corresponding half-gallery: its endpoint
triangulation and its road-center triangulation.  Exhaustive comparison gives:

- the six admissible sheetwise pairs share exactly one endpoint anchor;
- all six admissible cross-sheet pairs, which have different roads and
  opposite signs, have no common anchor; and
- the three opposite-sign pairs that do share a center belong to the same
  road and are precisely the forbidden opposite rays, so they are not cones
  of the product fan.

Consequently an admissible cross-sheet toric edge cannot be realized by
concatenating two already constructed half-gallery arms.  This failure is
before coefficients, normal signs, Tor grades, or Smith reduction.

## Scoped no-go

Within the literal K6 half-gallery objects of entries 246 and 262, the
cross-sheet part of the full-log source has no edge image.  Hence the eight
maximal-cone compatibility equations cannot yet be written in one literal
entry143 mapping complex.

This does not prohibit an extraordinary/log correspondence.  It proves that
the existing half-gallery anchors do not supply it.

## Minimal additional datum

For each of the six cross-sheet two-cones one must construct a bridge object
(W_{(D,+),(D',-)}) with support-typed maps to both full Boolean
half-gallery packets.  Its proper/excess-Gysin image must be a literal
entry143 chain joining the two middle triangulations, carry the occurrence
and normal-circle lines and both Tor grades, and specify the Beck--Chevalley
homotopy on its two endpoint restrictions.  Rotation and reflection may
transport one seed only after its stabilizer square is proved.

Only after these six bridges exist can the 24 local rows of entry262 be
assembled around the eight maximal cones and tested by an integral SNF.

## Evidence

- `research/voevodsky/check_full_log_cross_sheet_anchor_no_go.rs`
- entries 143, 246, 259, 260, 261, and 262.

~~~json
{
  "status": "falsified_scoped_existing_half_gallery_cross_sheet_gluing",
  "toric_two_cones": 12,
  "sheetwise_two_cones": 6,
  "sheetwise_shared_anchor": 6,
  "cross_sheet_two_cones": 6,
  "cross_sheet_shared_anchor": 0,
  "forbidden_opposite_ray_pairs": 3,
  "forbidden_pairs_shared_center": 3,
  "existing_half_gallery_concatenation_constructs_cross_sheet_edges": false,
  "new_cross_sheet_bridge_correspondences_required": 6,
  "global_maximal_cone_gluing_constructed": false,
  "mapping_fiber_instantiated": false,
  "physical_p_defined": false,
  "physical_bockstein_defined": false,
  "D8_Jordan_tested": false,
  "graph_admission_claimed": false
}
~~~
