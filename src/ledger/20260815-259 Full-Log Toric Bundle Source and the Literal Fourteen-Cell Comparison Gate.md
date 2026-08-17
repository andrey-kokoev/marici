# Full-Log Toric Bundle Source and the Literal Fourteen-Cell Comparison Gate

## Canonical logarithmic source

The conductor cross-polytope of entries 256, 258, 336--337 has an intrinsic algebraic
log realization.  If the three labelled conductor-normal lines are
\(L_{14},L_{03},L_{25}\), form

\[
  \mathcal T=\prod_D \mathbf P(\mathcal O\oplus L_D).
\]

Its complete orthant fan has rays \(\{\pm e_D\}\).  Intersecting that fan
with an oriented sphere gives exactly the cross-polytope boundary.  Thus its
strata derive, rather than stipulate,

- six toric boundary divisors;
- twelve pair intersections, split into six sheetwise and six cross-sheet
  strata; and
- eight triple intersections, one for every sign vector.

Every maximal cone is unimodular.  Rotation permutes the three factors and
physical reflection acts by the already fixed signed permutation.  Road
multiplicities remain labels of the characteristic-monoid map; saturating
the orthant fan does not replace or divide them.

## What this resolves

This constructs the normalization-provenanced **source geometry** for the
six cross-sheet edge correspondences and eight triangular Beck--Chevalley
cells required by entry 258.  The fourteen cells are the six mixed
two-cones and all eight maximal cones of one canonical full-log toric
bundle, rather than freely adjoined carrier generators.

## Remaining literal comparison

The toric source does not itself define a map to entry143.  In particular,
the six mixed two-cones have no ordinary common K6 face, and the eight fixed
sections have no literal triple-support generator.  The still missing datum
is one proper/excess comparison functor

\[
  \Gamma_{\mathcal T}^{!,\log}\longrightarrow F_B/F_V
\]

whose restrictions send:

1. the six sheetwise two-cones to the shifted pair-facet Gysin rows;
2. the six mixed two-cones to the Rees/KN marked corridors; and
3. the eight maximal cones to BC homotopies whose oriented sum is the six
   short-facet defect of the canonical entry143 generic-top lift.

That comparison must derive every occurrence, normal-circle, conductor Tor,
and Cech corestriction row.  Without it the endpoint/Q mapping fiber and all
downstream parity and symmetry tests remain undefined.

## Evidence

- `research/voevodsky/check_conductor_full_log_toric_bundle.rs`
- entries 143, 249, 251, 333--334, 336--337, and 258.

~~~json
{
  "status": "proved_scoped_full_log_toric_source",
  "toric_bundle": "product_D P(O plus L_D)",
  "rays": 6,
  "two_cones": 12,
  "maximal_cones": 8,
  "smooth_unimodular": true,
  "sheetwise_two_cones": 6,
  "cross_sheet_two_cones": 6,
  "multiplicities_retained_in_monoid_map": true,
  "D3": true,
  "reflection": true,
  "literal_entry143_comparison_constructed": false,
  "mapping_fiber_instantiated": false,
  "physical_p_defined": false,
  "physical_bockstein_defined": false,
  "D8_Jordan_tested": false,
  "graph_admission_claimed": false
}
~~~
