# Full Boolean Flip Replacement and the Twenty-Four Literal Rows

## Canonical repair of the local mismatch

Entry338 shows that a half-gallery changes one exclusive normal label.  The
literal middle triangulation already supplies the canonical repair.  Write

\[
E_L=\{p,a\},\qquad E_R=\{p,b\},\qquad
S_{\rm mid}=E_L\cup E_R=\{p,a,b\}.
\]

The two edge Boolean cubes cover six of the eight subsets of
\(S_{\rm mid}\).  The exactly missing states are

\[
H=\{a,b\},\qquad H=\{p,a,b\}.
\]

They are not chosen: they are the two subsets containing both the outgoing
and incoming exclusive normals.  Adding them is precisely the full-log
flip-normal replacement.

With two conductor Tor grades and six rotated/reflected half-galleries this
gives

\[
6\cdot2\cdot2=24
\]

new literal entry143 generator rows.  Their assignment matrix is the
identity in the labelled bases, hence has rank 24 and 24 unit Smith factors.

## Derived occurrence, normal, and Cech rows

The checker uses the actual K6 labels of every half-gallery.  It verifies:

- all 96 edge-to-middle radial rows, with the added label contributing the
  legal target coefficient \(X_c/u_c\) because \(c\notin H\);
- all 60 normal-removal terms forced from the 24 new states by entry143's
  ordered Boolean sign formula;
- \(d_{\rm normal}^2=0\) on all 48 complete middle cubes before duplicating
  the spectator Tor grade; and
- no occurrence section, normal section, or integer is inverted outside its
  legal Cech summand.

This closes the local constant-Boolean defect of entry338 at the finite
literal BM–Cech level.  It preserves both Tor grades and is automatically
transported across the six halves by the established label action.

## Remaining global gate

The 24 literal rows now exist locally.  What remains is to identify the
three pairwise restrictions at each of the eight full-log maximal cones and
prove that their oriented BC sum gives the six short-facet terms in the
entry143 generic-top defect.  That is a global overlap equation, not another
local normal-state choice.

Until that eight-cone equation and the endpoint/generic-Q comparisons are
assembled in one chain map, the pointed mapping fiber and downstream parity
tests remain undefined.

## Evidence

- `research/voevodsky/check_literal_half_gallery_full_boolean_replacement.rs`
- entries 143, 260, 333, and 261.

~~~json
{
  "status": "proved_scoped_literal_full_Boolean_flip_replacement",
  "literal_half_galleries": 6,
  "middle_states_per_half": 8,
  "edge_union_states_per_half": 6,
  "missing_states_per_half": 2,
  "tor_grades": [0, 1],
  "new_literal_generator_rows": 24,
  "radial_Cech_rows_verified": 96,
  "forced_missing_normal_rows": 60,
  "normal_d_squared_checks": 48,
  "new_block_rank": 24,
  "new_block_smith_unit_factors": 24,
  "integer_torsion": false,
  "base_inversions": false,
  "global_maximal_cone_gluing_constructed": false,
  "mapping_fiber_instantiated": false,
  "physical_p_defined": false,
  "physical_bockstein_defined": false,
  "D8_Jordan_tested": false,
  "graph_admission_claimed": false
}
~~~
