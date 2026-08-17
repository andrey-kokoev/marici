# Admitted Log-Source Q Image Lattice and the Primitive Interior Correspondence Gate

Date: 2026-08-15  
Status: superseded by entry 275. The original conclusion omitted the two
normalization-sheet hemispheres and was false. No graph admission is claimed.

## Correction

Entry 275 proves that each octahedral sheet hemisphere has primitive relative
Q coefficient one. Their sum is the coefficient-two total. The corrected row
is `[2,1,1,0,0,0,0,0,0]`, with Smith factor one. The `2Z` conclusion below is
historical and must not be cited.

## Exact source image

Project every currently support-typed source class to the primitive relative
K6 top coordinate certified in entry 273. The full-log maximal-cone class has
coefficient two. The six local oriented KN wall classes and entry 272's short
hexagon filler lie in \(F_B\), hence have literal \(Q\)-coefficient zero.
Thus the admitted row is
\[
[2,0,0,0,0,0,0,0].
\]
Its Smith factor is two, its image is \(2\mathbb Z\), and its cokernel is
\(\mathbb Z/2\). No integral combination has coefficient one.

Entry 198's projective-conductor Gysin is abstractly primitive, but it is not
an admitted literal column: entry 271 proves that its two disjoint triangular
pair-incidence components cannot identify with the connected six-corridor
hexagon. Including that unit without a new correspondence would stipulate the
missing map.

## Minimal enlargement

A single independently constructed reflection-odd relative-interior column
of coefficient \(+1\) changes the row to \([2,1]\), Smith factor one. It must
come from a proper support-typed normalization/log-BM or nearby-cycle object
whose boundary is the literal connected hexagon, whose chart restrictions are
the entry 219, 328 Rees/KN packets, and whose long boundary is the based entry143
\(q_\Sigma\) row.

Until this column is geometric rather than declared, the endpoint/Q mapping
fiber and all downstream invariants remain undefined.

## Certificate

- `research/voevodsky/check_admitted_log_source_q_image_lattice.rs`

~~~json
{
  "claim": "The currently admitted support-typed normalization/log source classes map to the literal relative Q coordinate with image lattice 2Z; local primitive Rees/KN walls and the short hexagon have Q-image zero.",
  "status": "falsified_scoped_admitted_source_primitive_Q_surjectivity",
  "scope": "currently admitted source classes only; enlarged proper log-BM/nearby-cycle interior correspondences remain open",
  "matrix": {
    "admitted_Q_row": [2,0,0,0,0,0,0,0],
    "smith": [2],
    "image": "2Z",
    "cokernel": "Z/2",
    "P2_unit_literal_column_admitted": false,
    "minimal_new_column": 1
  },
  "minimal_repair": "Construct one proper support-typed reflection-odd relative-interior correspondence with literal Q coefficient +1 and boundary restrictions equal to the connected hexagon and all adjacent Rees/KN packets.",
  "physical_mapping_fiber": "unconstructed",
  "physical_p_partial_Q": "undefined",
  "physical_Bockstein": "undefined"
}
~~~
