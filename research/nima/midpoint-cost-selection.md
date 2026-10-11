# Midpoint certificates do not yet select a route energy

## Question

Does the positive-defect construction in `marici-minimal-mathematical-formulation.md`, section 8, derive the squared-displacement route cost used in `midpoint-route-statistics.md`? The operator requested this next test. Active obligation: forward realization and readout selection, not an assumption of native-to-affine comparison.

## Claim boundary

The source defines a positive obstruction q(delta)^dagger q(delta), which vanishes when the comparison is fillable under its stated stable and definite-dagger hypotheses. It explicitly says that stability or orientation reversal alone does not supply the definite pairing. This is an obstruction measure, not a declared action charging every successful generating step.

In the affine midpoint test, all six certificate residuals 2m-a-b vanish, whereas every ancestry route has positive accumulated squared displacement. The native obstruction object has not been identified with these affine residuals. The example distinguishes a verified equation from the cost of realizing or presenting it; it does not construct that missing native comparison.

Two candidate route costs on the same retained midpoint tree are

\[
E_2(r)=\sum_{e\in r}\|d_e\|^2,
\qquad E_4(r)=\sum_{e\in r}\|d_e\|^4.
\]

Both preserve all midpoint equations, are nonnegative, invariant under Euclidean isometries and reversal, and additive under concatenation of retained edge lists. Both assign cost one to a unit edge in the fixed dimensionless coordinate convention. Their values on the eight routes are not proportional. Therefore these requirements do not select E2, even up to an overall energy scale. Adding a quadratic/parallelogram law would exclude E4, but that would be additional cost structure requiring source justification. The already verified variance identity explains why E2 is useful for fair midpoint ancestry; it does not identify physical energy.

A further distinction concerns subdivision. Replacing a unit edge by two half-edges changes E2 from 1 to 1/2 and E4 from 1 to 1/8. Neither unweighted action descends under that presentation change. A retained-generation interpretation may legitimately distinguish the two presentations; a subdivision-invariant interpretation needs additional weights or a different law. No physical duration is supplied by the stage indices.

## Disposition

The conjecture that the supplied midpoint certificates and Euclidean symmetry already select the proposed route energy fails. The strongest counterexample retains the same metric, equations and unit-edge normalization while changing the action from E2 to E4. A deliberately incorrect midpoint is detected with squared residual 4, so the all-zero certificate result is not a vacuous checker.

The finite statistical model survives as a model with a declared cost. The missing source datum is a WG cost-selection law specifying quadraticity or an alternative rule, normalization, and treatment of subdivision. The native positive obstruction cannot simply be renamed nonzero route energy. Physical energy and temperature would still require their own interpretation after that selection.

Verification: `python research/nima/checkers/check_midpoint_cost_selection.py` exited zero via `structured_command_execution:e_32876_1791222683203819900_22`. Exact results: `results/midpoint-cost-selection.json`. No commit or publication is claimed.
