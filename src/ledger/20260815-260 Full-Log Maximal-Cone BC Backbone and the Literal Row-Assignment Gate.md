# Full-Log Maximal-Cone BC Backbone and the Literal Row-Assignment Gate

## Derived 24-row backbone

Every maximal cone of the full-log toric bundle in entry 259 selects one
signed ray in each of the three conductor-normal directions.  Its three
unordered pairs of directions give three two-step Gysin contractions.
Therefore the eight maximal cones canonically produce

\[
8\cdot\binom32=24
\]

Beck--Chevalley relations.  Reversing the contraction order reverses the
exterior sign, while both paths carry exactly the same multiplicity
monomial.  The cancellation is integral and never divides a road
multiplicity.

After orienting the two composites, every relation has primitive row
\([1,1]\).  Their block matrix has rank 24 and 24 unit Smith factors.
Rotation and reflection permute the complete set.

## Exact scope boundary

This derives the multiplicity-sensitive **source-side** 24-row BC backbone.
It does not assign those rows to literal entry143 generators.  Such an
assignment cannot be an ordinary face-poset map by entry 258: the mixed
two-cones have empty common K6 support and every maximal cone has empty
triple support.

The remaining datum is a single mixed-variance realization functor whose
local maps identify:

- each two-step source contraction with the corresponding occurrence and
  normal-circle differential in entry143;
- its two conductor Tor grades with the literal target Tor rows;
- its localization comparison with the target Cech corestriction; and
- the oriented sum of the eight maximal-cone homotopies with the six
  short-facet terms in the generic-top defect.

Without these vertical maps, the 24 unit relations are not yet the requested
24 literal rows, and the endpoint/Q mapping fiber remains untyped.

## Evidence

- `research/voevodsky/check_full_log_maximal_cone_bc_rows.rs`
- entries 143, 251, 258, 333, and 259.

~~~json
{
  "status": "proved_scoped_full_log_maximal_cone_BC_backbone",
  "maximal_cones": 8,
  "pairwise_contractions_per_cone": 3,
  "BC_rows": 24,
  "opposite_exterior_signs": true,
  "multiplicity_monomials_retained": true,
  "rank": 24,
  "smith_unit_factors": 24,
  "integer_torsion": false,
  "D3": true,
  "reflection": true,
  "literal_entry143_row_assignment_constructed": false,
  "mapping_fiber_instantiated": false,
  "physical_p_defined": false,
  "physical_bockstein_defined": false,
  "D8_Jordan_tested": false,
  "graph_admission_claimed": false
}
~~~
