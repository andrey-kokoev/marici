# Oriented K6 Facet Corridors and the Top-Attachment Gate

## Record

Date: 2026-08-15

Status: the nine literal one-label facets below the six entry241 vertex
stars admit canonical integral oriented corridor chains with primitive
endpoint boundaries. Rotation acts strictly. Physical reflection does not:
it exchanges the selected directed arc with the complementary arc, and the
difference is exactly one full oriented facet boundary. This is a scoped
strict no-go and a precise derived 2-cell repair. No graph admission is
claimed.

## Literal facet census

The checker reconstructs the complete (K_6) noncrossing-face complex,
with ranks
[
(1,9,21,14).
]
The six vertex packets from entry241 determine nine distinct one-label
facets:

- six short facets, forming one oriented triangle on each normalization
  sheet; and
- three long facets, framed from the positive sheet to the negative sheet.

Every such facet contains exactly two selected vertices. The inherited
cellular orientation gives a directed boundary cycle, hence a distinguished
positive arc from the framed start vertex to the framed end vertex. These
nine arcs contain 21 literal edge terms: 15 over the short facets and 6 over
the long facets.

For every corridor (c_F),
[
d c_F=v_F^{mathrm{end}}-v_F^{mathrm{start}}.
]
The combined endpoint matrix has rank nine and nine unit Smith factors.
Thus the construction is primitive and torsion-free; it uses neither a
shortest-path convention nor any base inversion.

## Symmetry and exact strict falsifier

Cyclic rotation carries every selected corridor strictly to the rotated
corridor.

Physical reflection reverses the framed endpoints and transports the
cellular coefficients with the exact vertex gauges. For all nine facets,
the reflected endpoint boundary agrees with the target endpoint boundary,
but the reflected chain is not the selected target arc. Instead
[
r(c_F)-c_{rF}=pm, d[F],
]
where ([F]) is the literal oriented two-cell of the reflected facet. The
runtime census is:

- strict reflection matches: 0;
- short-facet failures: 6;
- long-facet failures: 3;
- reflection endpoint scalar (+1): 9;
- required facet-boundary homotopies: 9.

Therefore no strictly reflection-equivariant selection of these inherited
positive arcs exists. This does not obstruct a derived corridor: the
literal facet cell supplies the minimal homotopy, with no denominator and
no torsion.

## Consequence for the full-log correspondence

The vertex/edge pushforward from entry241 extends to the facet grade only
after adjoining the nine facet-supported 2-cell homotopies. Their presence
is derived by the literal (K_6) incidence matrix; it is not a fitted
coefficient correction.

What remains is a higher coherence problem. The cyclic boundary of these
nine homotopies must be computed and compared with entry223's
projectivized-conductor top and the based (q_Sigma) row. Until that
comparison is constructed:

- the rank-nine homogeneous AW ambiguity is not known to vanish;
- the two endpoint odd counits are not joined to a common generic-(Q)
  connector;
- the endpoint/(Q) mapping fiber is not instantiated; and
- (p_{partial,Q}), its Bockstein, (D_8), and Jordan coherence remain
  undefined.

## Executable evidence

Checker:
research/voevodsky/check_dp6_oriented_facet_corridors.rs

SHA-256:
924ae64d9fec7ded7d35b032d0cc084832880c9d48cb0a878d029ef64337591c

The user-site structured-command MCP ran rustfmt, rustfmt --check,
warnings-denied optimized compilation, the executable assertions, and the
JSON output. All passed.

## Outcome contract

~~~json
{
  "claim": "The nine literal K6 facets determined by the six oriented KN vertex packets have canonical primitive directed corridor arcs. D3 rotation is strict, while physical reflection differs from the selected reflected arc by exactly one literal oriented facet boundary on every facet.",
  "status": "falsified_scoped_strict_reflection_equivariant_facet_arc_selection",
  "scope": "literal K6 vertex-edge-facet incidence and finite integral corridor chains; derived facet homotopies admitted, top/Q/endpoints excluded",
  "census": {
    "K6_face_ranks": [1, 9, 21, 14],
    "literal_facets": 9,
    "short_sheet_facets": 6,
    "long_road_facets": 3,
    "selected_vertices_per_facet": 2,
    "oriented_corridors": 9,
    "total_edge_terms": 21,
    "short_edge_terms": 15,
    "long_edge_terms": 6
  },
  "integral_matrix": {
    "corridor_boundary_rank": 9,
    "smith_factors": [1, 1, 1, 1, 1, 1, 1, 1, 1],
    "torsion": false,
    "base_inversions": false
  },
  "symmetry": {
    "D3_rotation_strict": true,
    "strict_reflection_matches": 0,
    "reflection_endpoint_scalar_plus": 9,
    "reflection_endpoint_scalar_minus": 0,
    "short_reflection_failures": 6,
    "long_reflection_failures": 3,
    "facet_boundary_homotopies_required": 9
  },
  "minimal_additional_datum": "one literal facet-supported 2-cell homotopy for each corridor, with D3/reflection coherence and source KN provenance",
  "unconstructed": [
    "cyclic top obstruction of the nine facet homotopies",
    "entry223 top and based qSigma comparison",
    "rank-nine homogeneous solution module",
    "endpoint/Q mapping fiber",
    "p_partial_Q and Bockstein",
    "D8 and Jordan coherence"
  ],
  "checker": "research/voevodsky/check_dp6_oriented_facet_corridors.rs",
  "checker_sha256": "924ae64d9fec7ded7d35b032d0cc084832880c9d48cb0a878d029ef64337591c"
}
~~~
