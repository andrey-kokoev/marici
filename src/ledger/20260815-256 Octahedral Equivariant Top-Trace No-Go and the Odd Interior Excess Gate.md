# Octahedral Equivariant Top-Trace No-Go and the Odd Interior Excess Gate

## Scoped obstruction

Entry336 supplies the canonical octahedral carrier. Its eight faces are
indexed by sign triples

\[
(s_{14},s_{03},s_{25})\in\{\pm1\}^3.
\]

Rotation cyclically permutes the coordinates. Physical reflection sends

\[
(s_0,s_1,s_2)\longmapsto(-s_0,-s_2,-s_1).
\]

The faces therefore split into two \(D_3\)-orbits: the all-equal pair and
the remaining six faces.

Geometric reflection reverses each oriented triangular face. The single
already-retained source orientation twist contributes a second minus, so the
loaded face basis is reflection even, whereas the loaded entry143 generic
target line is reflection odd. Consequently an ordinary equivariant trace
has rotation-invariant, reflection-odd coefficients determined by two
integers:

- \(a\) on the all-positive face, with value \(-a\) on the all-negative
  face;
- \(b\) on every one-negative face, with value \(-b\) on the reflected
  two-negative faces.

Pairing this trace with the primitive octahedral fundamental cycle gives

\[
2a-6b.
\]

Thus every ordinary equivariant face trace has even image. The equation
\(2a-6b=1\), required to map the primitive carrier top to the normalized
generic \(q_\Sigma\) top, has no integral solution. The presentation row
\([2,-6]\) has Smith factor \([2]\), so the obstruction is exactly
\(\mathbb Z/2\).

This is an intrinsic no-go for an ordinary degree-zero trace on the
octahedral faces. It does not rule out the requested derived log-excess
correspondence.

## Minimal derived repair

One independently derived reflection-odd interior excess/Tor generator with
primitive counit changes the presentation to

\[
[2,-6,1],
\]

whose Smith factor is \([1]\). The normalized equation then has the
integral solution given by the unit interior column.

This column cannot be stipulated from the carrier. It must arise
geometrically as a shifted interior log-excess class whose boundary is the
eight loaded Beck--Chevalley face transformations and whose restriction to
the literal entry143 generic top is \(+1\). The central exceptional
\([2,1]\) correction of entry176 has the correct local arithmetic, but its
support is not presently connected to this interior carrier. Using it
requires a new support-typed central-to-interior BC map; otherwise the use
would be circular.

Consequently the earliest remaining datum is now sharper than “eight face
maps”: the face maps and one primitive odd interior excess cell must be
constructed together in a single normalization-provenanced six-functor
kernel.

## Evidence

- research/voevodsky/check_cross_polytope_equivariant_top_trace_no_go.rs
- entries 143, 176, 249, 251, 253, 333, and 255.

~~~json
{
  "status": "falsified_scoped_ordinary_equivariant_octahedral_top_trace",
  "geometric_face_reflection_sign": -1,
  "source_orientation_twist_sign": -1,
  "loaded_face_reflection_sign": 1,
  "loaded_target_reflection_sign": -1,
  "face_orbits": [2, 6],
  "trace_parameters": ["a", "b"],
  "fundamental_pairing_row": [2, -6],
  "smith": [2],
  "obstruction_group": "Z/2",
  "primitive_top_value_one_solution": "EMPTY",
  "minimal_repair_row": [2, -6, 1],
  "repaired_smith": [1],
  "odd_interior_excess_column_required": true,
  "odd_interior_column_geometrically_constructed": false,
  "global_correspondence_no_go": false,
  "mapping_fiber_instantiated": false,
  "physical_p_defined": false,
  "physical_bockstein_defined": false,
  "D8_Jordan_tested": false,
  "graph_admission_claimed": false
}
~~~
