# The last held-out case is ambiguous, and the diagonal solver has an exact completeness boundary

## Version note

The interval-calibration obstruction below concerns the version-1 FIXED-source witness schema. Version 2 now resolves this thin-data example with an explicitly calibration-dependent witness; see `calibration-dependent-source-witnesses-close-the-thin-data-certificate-gap.md`. The exact-calibration completeness proof and the historical held-out resolution are unchanged.

## Result

The remaining held-out case is now certified AMBIGUOUS, with two robust source witnesses giving vacuum sums approximately

`-0.00168804` and `+0.00034659`.

The original data, source budget, prior order and target were unchanged. The calibration calculation also used the SAME 32768 cells, 192-bit precision and scaled cutoff as before.

The gap came from exchanging that calculation through a conservatively rounded printed Arb ball. Passing its exact rational lower and upper endpoints recovers enough already-computed information to construct the witnesses. Thus the previous unresolved result was numerical enclosure slack; the settled answer is genuine source ambiguity.

The solver additionally has a precise completeness boundary: it always decides its finite exact-calibration model, but interval-calibration refinement alone need not ever decide under the current fixed-witness certificate schema.

## 1. Resolve the actual held-out input

The acquired A=3 vacuum interval is

`[-2683/250000, -5327/500000]`.

With the printed calibration enclosure, the necessary minimum source cost was about 39.899, below the budget of 40, while the sufficient robust-witness construction cost about 40.0073. Neither infeasibility nor a compatible fixed source was established by those bounds.

The checker recomputes the existing physical E_0 enclosure and exports its exact dyadic endpoints as rational strings. It verifies that they lie strictly inside the previous conservative input interval. Every acquisition interval, cost weight and target remains byte-for-byte unchanged.

The reusable solver then supplies two source vectors fitting every calibration in the tighter enclosure, each within budget and with opposite task signs. The separate verifier accepts both. This is not selection of different physical calibrations to make the two witnesses fit.

The saved artifact contains the complete revised problem and its independently verified ambiguity certificate. The auxiliary tail coefficients retain their previously justified finite-source realizations.

## 2. Exact-calibration completeness theorem

For the declared finite diagonal model, suppose each positive calibration is known exactly as a rational, E_i=e_i=f_i. Then the solver never needs UNRESOLVED.

Proof:

1. Outer and inner coefficient boxes coincide. The weighted closest-to-zero point gives the exact minimum budget cost. Thus infeasibility is decided exactly.
2. If feasible, start at that minimum-cost point. To maximize a linear target, only moves toward its favorable box endpoint can help. Each such move has constant gain per extra budget cost, |t_i|/w_i. Sorting those ratios and spending the remaining budget is the exact continuous-knapsack solution. Apply the same procedure to the negative target to find the minimum.
3. A supporting multiplier for either optimum can be chosen from zero and the finite ratios |t_i|/w_i. At a partial fill it is the marginal gain ratio; at a fully filled optimum zero suffices; at the minimum-cost budget a largest required marginal ratio suffices. The resulting scalar dual bound attains the primal optimum. This is also the elementary strong-duality statement for this box/l1 linear program.
4. If the minimum exceeds the threshold, the target is universally true. If the maximum is at most the threshold, it is universally false. Otherwise the attained minimum and maximum give opposing witnesses for the strict target.

Degenerate intervals, zero budget and equality at the target threshold are included. This is a proof for arbitrary supported dimension, not an extrapolation from the existing 300 small exact vertex-oracle tests.

## 3. Why shrinking calibration intervals does not guarantee termination

The present feasible-witness schema asks for one source vector that works for EVERY calibration value in its enclosure. This is a sound sufficient condition, but stronger than existence for the actual fixed calibration.

Consider the one-dimensional problem

`data=[1,1]`, `calibration=[2-delta,2+delta]`,

`|x|<=1`, target `x>0`, with `0<delta<=1/2`.

For every permitted calibration E the source x=1/E exists, is within budget and is strictly positive. Nevertheless no SINGLE fixed x fits the exact datum for both distinct calibration endpoints. The robust inner box is empty for every positive delta.

The version-1 fixed-witness engine therefore returns UNRESOLVED for the sequence delta=2^(-k), however far it is refined. The checker exercises k=1,...,20, now also checking that version 2 resolves each case. At exact calibration [2,2] it returns TARGET_TRUE with source x=1/2.

This failure has positive target and budget slack. It is not an equality of the target to its threshold. The obstruction is a thin exact observation together with the fixed-source-witness requirement. A future parametric witness schema could address it, but the present verifier must not claim that certificate already exists.

## 4. Sufficient conditions for refinement to settle a case

Let nested calibration intervals shrink to fixed positive calibrations, with data, target and budget unchanged.

- A strictly infeasible limiting minimum cost is eventually detected, because the outer minimum-cost bound converges.
- Suppose a feasible witness persists under sufficiently small calibration perturbations, and the limiting universal target bound has a strict margin. Then sufficiently fine enclosures certify the corresponding universal conclusion. Compactness of the budget-bounded source set prevents outer-box extrema from retaining an incorrect limiting bound.
- If two opposing witnesses both persist under sufficiently small calibration perturbations, ambiguity is eventually certified by exact optimization on the inner boxes.

A convenient sufficient condition for persistence is strict slack in every relevant data constraint for the fixed source vector. Its predicted error under calibration perturbation delta_i is at most |x_i| delta_i. The source budget need not be changed. Zero coordinates or other exact identities can also persist without strict data slack.

These are sufficient conditions, not necessary ones. At a threshold equality, a fragile feasible boundary or a thin exact datum, interval refinement alone has no general termination guarantee. The engine correctly leaves such cases unresolved unless another supported certificate is available.

## 5. Certificate exchange must preserve precision

Exact-rational verification cannot recover information discarded before the verifier receives its input. Printed Arb balls are conservative, so the previous exchange was sound, but it unnecessarily weakened the problem.

For analytical calibration handoff, export exact certified endpoints and keep the readable ball only as a display. The problem digest should bind those exact endpoints. The rational verifier still checks only consequences of the supplied enclosure; its analytic validity remains the responsibility of the owning completed-theta calculation.

In this case no new sensor reading or stronger prior was needed. The decisive action was preserving numerical evidence already available.

## Verification

`uv run --with python-flint --with sympy python research/nima/checkers/resolve_heldout_calibration_case.py`

Artifact: `research/nima/results/resolved-heldout-calibration-case.json`.

The run reproduces the sole unresolved leaf of the saved acquisition catalogue, changes only its calibration endpoint representation, verifies the opposite-sign source certificate independently, and tests the persistent thin-data obstruction and exact-calibration control.

This closes the last case in that saved finite catalogue. It does not claim completeness for uncertain calibration, arbitrary correlated sensor models or all possible returned intervals.
