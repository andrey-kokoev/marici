# Entry143 Generic Top Defect and the dP6 Twelve-to-Six Comparison Gate

## Result

The literal empty-face generator of entry 143 is a canonical graded lift in
\(E=F_K/F_V\) of the generic top generator in \(Q=F_K/F_B\). Its promoted
Čech differential has nine facet terms:

- the three long-facet terms survive in \(Q\), with coefficients
  \(X_D/u_D\) and augmentation three;
- the six short-facet terms lie in \(P=F_B/F_V\) and form the defect of the
  graded section \(Q\dashrightarrow E\).

At the cellular incidence level all nine coefficients are primitive. The
six-entry short-facet defect vector has Smith factor one. Rotation and
reflection preserve the long/short partition; reflection reverses the
oriented top with the already fixed road-orientation character.

This refines entry 250. The target does possess a canonical interior top
lift, but completing the source map now requires a concrete comparison from
the twelve oriented dP6 boundary intervals to these six short-facet defect
rows:

\[
 C_1(\partial dP_6)\longrightarrow P
 \quad\text{with}\quad
 d_E(\widetilde q_\Sigma)-\widetilde{d_Qq_\Sigma}
 =\Phi_\partial(d[dP_6]).
\]

Entries 249, 334 give each local interval and its carrier image. They do
not yet derive the global \(12\to6\) mixed-variance matrix on every
occurrence, normal-circle, Tor, and Čech grade. Consequently this entry does
not instantiate the endpoint/Q mapping fiber.

## Minimal next executable

Enumerate the twelve oriented dP6 edges and the six literal short-facet
generators, expand both sides through entry143's \([S,H]\) differential,
and solve

\[
M_{12\to6}\,\partial[dP_6]=\delta_P(\widetilde q_\Sigma)
\]

with the already fixed local Rees/KN columns, endpoint framing, reflection,
and \(D_3\). Its homogeneous kernel and Smith form will decide whether the
interior lift is canonical, ambiguous, or obstructed. No matrix entry may be
inserted merely from the carrier quotient.

## Evidence

- research/voevodsky/check_entry143_generic_top_defect.rs
- research/voevodsky/check_global_k6_koszul_cech_promotion.rs
- entries 143, 249, 334, and 250.

~~~json
{
  "status": "proved_scoped_target_top_defect",
  "E_top_lift_canonical": true,
  "total_facet_terms": 9,
  "Q_long_terms": 3,
  "P_short_defect_terms": 6,
  "Q_augmentation": 3,
  "P_defect_smith": [1],
  "D3_partition_covariant": true,
  "dp6_boundary_to_short_defect_rows_constructed": false,
  "mixed_variance_kernel_constructed": false,
  "mapping_fiber_instantiated": false,
  "physical_p_defined": false,
  "physical_bockstein_defined": false,
  "D8_Jordan_tested": false,
  "graph_admission_claimed": false
}
~~~
