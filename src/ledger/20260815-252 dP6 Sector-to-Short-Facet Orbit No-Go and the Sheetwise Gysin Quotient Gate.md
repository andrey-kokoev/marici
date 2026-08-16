# dP6 Sector-to-Short-Facet Orbit No-Go and the Sheetwise Gysin Quotient Gate

## Scoped no-go

The six oriented sectors of the single dP6 boundary and the six literal
entry143 short facets are not isomorphic as \(D_3\)-sets.

Index the dP6 sectors cyclically by \(i\in\mathbb Z/6\). The fan calculation
of entry 249 gives

\[
\rho(i)=i+2,\qquad \sigma(i)=1-i.
\]

This is one free transitive \(D_3\)-orbit: the reflection has no fixed
sector. Index the short diagonals by
\(x_k=(k,k+2)\). Entry143's physical action is

\[
\rho(x_k)=x_{k+2},\qquad \sigma(x_k)=x_{-k}.
\]

The short facets split into the even and odd three-element normalization
sheet orbits, and reflection fixes \(x_0\) and \(x_3\). Exhaustive integral
enumeration finds six equivariant set maps from sectors to short facets, but
every one has image equal to exactly one parity orbit and every nonempty
fiber has multiplicity two. There is no equivariant bijection.

Therefore the missing \(12\to6\) comparison cannot be constructed by
labelling each dP6 sector with one distinct short facet. Such a declaration
would silently identify inequivalent stabilizers.

## Minimal repair

The geometry must retain both normalization-sheet parity orbits and use a
sheetwise multiplicity-sensitive Gysin quotient. On each sheet the two
sector germs over a short facet must be integrated by a relative
normal-circle/connector homotopy; the positive and negative quotients must
then be clutched over the conductor with the physical polarity action.

This is exactly where the shifted pair-facet maps of entry 245 must enter:
the two-to-one fibers cannot be collapsed by an ordinary degree-zero
relabeling. The required global map must derive the unit Gysin coefficient,
all normal-circle and Tor rows, and the reflected sheet clutching. Entry249's
single constructible boundary and entry251's target defect do not yet supply
that quotient.

This is not a no-go for the full log-excess correspondence. It is the
earliest falsifier for a sectorwise bijective realization and specifies the
additional geometric operation that the next matrix must encode.

## Evidence

- research/voevodsky/check_dp6_short_facet_d3_orbit_no_go.rs
- entries 143, 245, 249, 250, and 251.

~~~json
{
  "status": "falsified_scoped_equivariant_sector_relabelling",
  "source_sectors": 6,
  "source_D3_orbits": 1,
  "source_reflection_fixed_points": 0,
  "target_short_facets": 6,
  "target_D3_orbits": 2,
  "target_reflection_fixed_points": 2,
  "equivariant_maps": 6,
  "equivariant_bijections": 0,
  "every_equivariant_map_image_size": 3,
  "every_nonempty_fibre_multiplicity": 2,
  "sheetwise_Gysin_quotient_required": true,
  "global_correspondence_no_go": false,
  "mapping_fiber_instantiated": false,
  "physical_p_defined": false,
  "physical_bockstein_defined": false,
  "D8_Jordan_tested": false,
  "graph_admission_claimed": false
}
~~~
