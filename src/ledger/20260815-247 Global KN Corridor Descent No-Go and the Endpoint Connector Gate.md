# Global KN Corridor Descent No-Go and the Endpoint Connector Gate

## Record

Date: 2026-08-16

Status: falsified for ordinary stratified gluing of the six local Rees/KN
corridor pushforwards. This is not a no-go for homotopy-coherent
normalization/log-excess descent. No graph admission is claimed.

## Exact obstruction

In cyclic (dP_6) cone order the ordered road pairs are
[
(0,1),(0,2),(1,2),(1,0),(2,0),(2,1).
]
The cyclic pairs select positive marked half-corridors and the reversed pairs
select negative halves. Applying the entry210 support dictionary to both
sides of every shared fan ray gives zero matching restrictions.

Three shared rays map to (v_+) from one incident cone and (v_-) from the
other. The other three map to two distinct marked road centers. Consequently
the six proper local maps of entry334 cannot be restrictions of one ordinary
stratified map from the glued (dP_6) boundary.

The three center mismatches are precisely the shifted pair/facet homotopies
constructed in entries332--333. They are already integral and coherent with
the normalized global top. The remaining mismatch is therefore the
(D_3)-orbit of physical endpoint comparisons.

## Minimal repair

The minimal additional geometric datum is one normalization-provenanced
endpoint connector cell, rotated through (D_3), whose boundary is the
difference between the two local endpoint restrictions. It must be compatible
with the intrinsic odd log counits, the conductor cdh square, and physical
reflection. A final reflection/top coherence cell must identify its cyclic
sum with the already normalized shifted top.

Without these connector cells, no global six-functor kernel exists and the
pointed endpoint/(Q) mapping fiber remains undefined. Adding them as scalar
equalities would contradict the ordinary gluing no-go; they must be genuine
homotopies in the mapping cone.

## Executable evidence

Checker:
`research/voevodsky/check_dp6_global_kn_corridor_descent_no_go.rs`

SHA-256:
`df654e007fbfdef4fac8fc03f15587c3803ee257493d37aaa521a623b83e5ca0`

Rustfmt, warnings-denied optimized compilation, runtime assertions, and JSON
emission passed. The temporary executable was removed.

## Outcome contract

~~~json
{
  "claim": "The six local positive KN Rees-to-corridor maps do not glue as one ordinary stratified map: all six shared-ray restrictions disagree, split as three physical endpoint mismatches and three distinct-center mismatches.",
  "status": "falsified_scoped_ordinary_global_KN_corridor_descent",
  "scope": "ordinary gluing of entry334 local maps; homotopy-coherent normalization/log-excess descent excluded",
  "census": {
    "maximal_cones": 6,
    "shared_ray_restriction_matches": 0,
    "endpoint_mismatches": 3,
    "distinct_center_mismatches": 3
  },
  "available_repair": {
    "shifted_center_homotopies": true,
    "normalized_global_top": true
  },
  "minimal_additional_datum": "one D3-orbit of normalization-provenanced endpoint connector cells plus reflection/top coherence",
  "unconstructed": [
    "endpoint connector cells in the literal mapping complex",
    "global normalization-conductor six-functor kernel",
    "pointed endpoint/Q mapping fiber",
    "p_partial_Q and Bockstein",
    "D8 and Jordan coherence"
  ],
  "checker": "research/voevodsky/check_dp6_global_kn_corridor_descent_no_go.rs",
  "checker_sha256": "df654e007fbfdef4fac8fc03f15587c3803ee257493d37aaa521a623b83e5ca0"
}
~~~
