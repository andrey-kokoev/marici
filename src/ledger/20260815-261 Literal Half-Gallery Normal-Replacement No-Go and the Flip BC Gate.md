# Literal Half-Gallery Normal-Replacement No-Go and the Flip BC Gate

## Exact literal audit

The corrected entry334 packet has five abstract cells, but a literal marked
half-gallery has three triangulation vertices and two K6 edge supports.  For
each of the six road/sign halves, those two edge supports are distinct
two-label faces.  They meet in exactly one persistent label and have one
different exclusive label each:

\[
E_L=\{p,a_{\mathrm{out}}\},\qquad
E_R=\{p,a_{\mathrm{in}}\},\qquad
a_{\mathrm{out}}\ne a_{\mathrm{in}}.
\]

Consequently no constant two-label Boolean normal basis can be identified
with both literal entry143 edge packets.  The former \(I_{240}\) statement
is valid only in the abstract declared basis; it cannot be promoted to a
literal cellwise identity.

The calculation is label-exact for all six rotated/reflected half-galleries.
It is independent of scalar signs, Tor multiplicity, or Smith reduction.

## Scoped no-go and minimal repair

This falsifies only the constant-Boolean identity shortcut.  It does not
rule out a Rees/log-excess comparison.

The minimal new local datum is one flip-normal replacement transformation
for each half-gallery.  It must:

1. keep the persistent normal-circle line fixed;
2. transport the outgoing exclusive line to the incoming exclusive line
   through the labelled Rees exceptional interval;
3. retain both conductor Tor grades and the forced double-Cech overlap;
4. commute with the two literal entry143 radial and normal-removal maps; and
5. be related by rotation and reflection to the other five transformations.

Only after these six replacement maps are constructed can the 24 maximal-
cone BC relations of entry260 be assigned to literal entry143 rows.  This
is earlier than the eight-face/global-top equation and earlier than the
endpoint/Q mapping fiber.

## Evidence

- `research/voevodsky/check_rees_kn_literal_half_gallery_normal_replacement_no_go.rs`
- entries 143, 258--259, 333--334, and 260.

~~~json
{
  "status": "falsified_scoped_constant_Boolean_identity_on_literal_half_galleries",
  "literal_half_galleries": 6,
  "vertices_per_half": 3,
  "edge_support_size": 2,
  "persistent_labels_per_flip": 1,
  "outgoing_labels_per_flip": 1,
  "incoming_labels_per_flip": 1,
  "constant_two_normal_basis_exists": false,
  "flip_normal_replacement_maps_required": 6,
  "D3": true,
  "reflection": true,
  "extraordinary_replacement_correspondence_no_go": false,
  "mapping_fiber_instantiated": false,
  "physical_p_defined": false,
  "physical_bockstein_defined": false,
  "D8_Jordan_tested": false,
  "graph_admission_claimed": false
}
~~~
