# Literal Q Even-Degree No-Go and the Odd Boundary-Crossing Connector

> **Superseded by entries 275--276.** The degree-two premise below applies
> only to the sheet-summed full-log carrier. Entry 275 derives two labelled
> hemispheres, each with primitive relative \(Q\)-coefficient one. Therefore
> the historical conclusion that the admitted source has image \(2\mathbb Z\)
> must not be cited as a current obstruction. The separate endpoint connector
> torsor remains, as recorded in entry 276.

## Exact obstruction

Entry266 computes that the coherently oriented full-log carrier reaches the
primitive K6 top with coefficient two. Entry176 supplies an abstract local
central exceptional coefficient +1, but its constructed support lies in the
road/boundary subcomplex F_B. Under the literal entry143 quotient to Q, every
such support-preserving correction is zero.

The presently typed generic row is therefore

    [2, 0],

not [2,1]. Its Smith factor is 2 and its cokernel is Z/2. No integral source
coordinate maps to the primitive value qSigma with coefficient one.

This is the earliest global obstruction after the complete finite
occurrence, Boolean, Tor, Cech, edge, and facet matrices of entries266, 339--343.
It occurs at the boundary-crossing Q projection.

## Minimal additional datum

Adjoin a connector whose literal Q coefficient is m. The augmented row is

    [2, m].

Its cokernel vanishes exactly when m is odd. The minimal primitive choices
are m=+1 or m=-1, with the sign fixed by the established orientation.

Thus the missing datum is not another local cap coefficient: that coefficient
is already +1. It is a support-typed proper/log-excess boundary-crossing map
transporting the central exceptional generator from F_B through E into the
literal generic Q top with independently proved odd coefficient.

Until this arrow is constructed, using the abstract +1 as the Q column is
circular. The pointed endpoint/Q mapping fiber and physical parity remain
undefined.

## Evidence

- research/voevodsky/check_literal_q_even_degree_obstruction.rs
- entries 143, 176, 266-268.

~~~json
{
  "status": "superseded_historical_sheet_summed_no_go",
  "superseded_by": [275, 276],
  "carrier_Q_coefficient": 2,
  "existing_central_Q_coefficient": 0,
  "current_row": [2, 0],
  "current_smith_factors": [2],
  "current_cokernel": "Z/2",
  "primitive_qSigma_reachable": false,
  "abstract_local_exceptional_coefficient": 1,
  "abstract_coefficient_has_literal_Q_support_map": false,
  "repair_row": "[2,m]",
  "repair_iff_m_odd": true,
  "minimal_primitive_connector_coefficients": [-1, 1],
  "mapping_fiber_instantiated": false,
  "physical_p_defined": false,
  "physical_bockstein_defined": false,
  "D8_Jordan_tested": false,
  "graph_admission_claimed": false
}
~~~
