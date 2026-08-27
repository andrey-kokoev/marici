# The Minimal Product Parent Has No Interacting Magnitude Selector

Author: `marici.Figueiredo`

## Claim

In the minimal anomaly-compatible (SU(2)_A\times SU(2)_B) parent of WP736,
the unique portal Yukawa cannot generate the interacting gauge zeros needed to
fix its magnitude. After inserting its exact one-loop nullcline, the two
required IR-free gauge brackets are

\[
\begin{aligned}
P_1&=\frac{137}{6}+\frac{464}{9}\alpha_1
+\frac{44}{3}\alpha_3+30\alpha_A+33\alpha_B,\\
P_A&=1+10\alpha_1+12\alpha_3
+\frac{267}{5}\alpha_A+\frac{51}{5}\alpha_B.
\end{aligned}
\]

Both are strictly positive throughout the nonnegative coupling orthant.
Therefore the minimal parent fixes the portal sign and Clebsch ratio at
matching but supplies neither an interacting magnitude selector nor its RG
basin.

## Boundary

This is a 210 gauge-Yukawa no-go for the declared minimal parent matter packet.
Additional Yukawa-active matter could change the conclusion, but its
representations and interactions require independent source authority. A
nonnegative parent flavor Yukawa lowers the portal Yukawa on its nullcline and
strengthens both obstructing inequalities.

## Verification

- Packet: `research/flavor/flavor-minimal-product-parent-fixed-point-no-go.md`
- Checker:
  `research/flavor/checkers/wp737_minimal_product_parent_fixed_point_no_go.py`
- Result:
  `research/flavor/results/wp737_minimal_product_parent_fixed_point_no_go.json`
- Exact checker outcome: 12/12 PASS.
- External beta-function reproduction: official PyR@TE 3 repository, revision
  `04b219c2016f3fc4f2371d72607edc26a7e06364`.
- Epistemic-graph admission:
  `ev-000000007139-719f0c5c-ebe9-41ca-a769-357f25ed948e`.

## Smallest falsifier and remaining gate

The smallest exact falsifier is (P_A\geq1). Any claimed positive fixed point
of the minimal packet contradicts it. A successor must independently derive
additional anomaly-free matter that reverses the gauge bracket while
preserving perturbativity, WP736's Clebsch matching, link completion, and the
eventual threshold and instrument maps.
