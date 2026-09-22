# Refined calibration resolves both open vacuum outcomes as infeasible

## Result

Both previously unresolved A=3 outcomes are now certified INFEASIBLE under the unchanged prior and acquisition data.

They are the intervals centered at -0.012 and +0.012, each with radius 0.001. Every compatible source would require normalized moment cost greater than 40.25824473, whereas the declared budget is 40.

The change was computational: increase the complete-cell calibration quadrature from 2048 to 32768 cells per scaled residual window. The raw reading intervals, physical calibration, 192-bit arithmetic precision, integration cutoff, source family and order-12 prior were NOT changed.

All 29 previously scanned outcomes are now classified:

- 19 task-certified;
- 4 ambiguous, with opposite-sign feasible sources;
- 6 incompatible with the prior;
- none unresolved in this finite scan.

This is not a complete classification of every possible real returned interval.

## 1. Keep the data fixed while improving knowledge of calibration

The script reads the EXACT original rational A=2 raw feature center and radius from the previous outcome artifact. It does not regenerate them from the refined calibration midpoint.

Only the enclosure of E_0 is narrowed. The old printed ball is approximately [1.4e-194 +/- 3.70e-196]; the refined one is [1.41e-194 +/- 2.65e-197]. The checker verifies strict containment of the new interval in the old one using their exact endpoints, not their rounded printed forms.

The two suspect A=3 intervals both require |b_3|>=0.011. The old A=2 vacuum reading requires b_2>=0.009. The positive raw feature reading requires

`a_0 >= (z_0 center - radius)/upper(E_0)`.

Consequently every feasible source must pay at least

`32 a_0_min +8*0.009 +8*(3/2)^12*0.011`.

The refined lower bound exceeds 40.25824473. Crossed feature coefficients and unobserved sources cannot reduce it: their path costs are nonnegative. The sign of b_3 does not affect this budget contradiction.

## 2. A reusable diagonal budget certificate

The new function `certify_diagonal_budget` accepts real data intervals, positive diagonal calibration intervals, positive source-cost weights and a budget. It returns FEASIBLE, INFEASIBLE or UNKNOWN with exact rational certificates.

For d_i in [l_i,u_i], calibration E_i in [e_i,f_i] with e_i>0, the source coefficient satisfies the outer interval obtained from all four endpoint quotients. Summing the weighted minimum absolute values of those outer intervals gives a necessary cost lower bound. If this exceeds the budget, infeasibility is proved even when the physical calibration coordinates are correlated.

For sufficient feasibility, intersect

`[l_i/e_i,u_i/e_i]` and `[l_i/f_i,u_i/f_i]`.

Every coefficient in this inner interval fits the data for EVERY calibration value in its enclosure. Choose its closest point to zero. If all such intervals are nonempty and the resulting weighted cost fits the budget, this supplies a robust finite source witness.

If neither certificate succeeds, return UNKNOWN. The function does not treat independently varied calibration intervals as the true physical parameter space or claim that an outer-box minimum is attained physically. Correlations can leave genuine enclosure gaps.

In this application the weights are 32 for the retained cubic coefficient, 8 for b_2 and 8*(3/2)^12 for b_3. The crossed row admits coefficient zero. Other source coordinates can be zero in a feasibility witness and only add cost in an infeasibility test.

## 3. Preserve, rather than replace, the other certificates

The checker reruns feasibility tests for all 29 saved outcome intervals. It also checks the previous positive and opposing-source witnesses against the REFINED calibration enclosure, original raw intervals and unchanged moment budget.

The 19 sign certificates and four ambiguity certificates remain valid. The only changed classifications are the two formerly unresolved cases. Their old necessary lower bounds did not exceed 40, while the refined ones do; hence the previous uncertainty was an enclosure gap rather than demonstrated source ambiguity.

The positive-centered unresolved case illustrates why feasibility cannot be skipped: its old universal vacuum lower bound was positive, but its feasible set is now proved empty. Reporting it as a successful task conclusion would have been vacuous.

## 4. Consequence for acquisition planning

Here the productive next action was better calibration computation, NOT another sensor reading and NOT a stronger source prior. The improved certificate locates the contradiction without claiming whether a real-world prior or observation would be at fault.

The solver supplies a reusable feasibility component for this diagonal acquisition family. It is not yet a general optimizer for arbitrary mixed sensors, calibration correlations or all possible target objectives. Remaining exact-boundary cases may still require further refinement or remain unknown.

No intrinsic module boundary, source action or normalized source-comparison map is inferred from these state-value certificates.

## Reproduction

First create the unchanged baseline outcome artifact if absent:

`uv run --with python-flint --with sympy python research/nima/checkers/check_vacuum_outcome_branches.py`

Then refine and resolve:

`uv run --with python-flint --with sympy python research/nima/checkers/resolve_vacuum_outcomes.py`

Artifact: `research/nima/results/resolved-vacuum-outcomes.json`.

The output retains the exact original raw data, refined cost inequalities, source witnesses and all outcome classifications. Fixtures remain synthetic acquisition intervals, not physical measurements.
