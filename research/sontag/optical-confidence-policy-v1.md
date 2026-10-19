# Confidence-aware optical policy with abstention

## Task and public context

Success concerns unknown coherent MEAN occupation under the supplied independent Gamma preparation posterior, not photon-count precision or experimentally validated coverage. Read posterior shapes Ki, rates ri and already-incurred signal factors fi from the retained transcript. Current means are fi*Ki/ri. A positive requested target h must be in the posterior-mean contraction range. The prior/calibration model remains a precondition.

## Conservative decision rule

For a proposed source gain, nonnegative final component means m1,m2 sum to h. Gamma scaling gives variance `v=m1²/K1+m2²/K2`. Therefore

`v/h² <= [(m1/h)²+(m2/h)²]/min(K1,K2) <= 1/min(K1,K2)`.

For relative error epsilon and posterior failure bound delta, require `min(K1,K2)>=1/(delta*epsilon²)` before emitting `target_gain(current_means,h)`. Chebyshev then certifies the requested posterior preparation-mean risk. This sufficient rule is deliberately conservative: failure means ABSTAIN, not that the actual tail probability necessarily exceeds delta. A sharper mixture-specific or exact-tail policy is a successor.

Abstention emits no additional gain. The tap has already attenuated the signal and its observations remain recorded; abstention is not a reset. An infeasible target also yields abstention. Zero target uses the ideal discrete q=0 swap endpoint; it does not certify removal of apparatus backgrounds or finite continuous-rate cooling.

## Tested boundary cases

At epsilon=1/4 and delta=1/20, the sufficient minimum shape threshold is 320. The low-information context (2,3) abstains. A separately SUPPLIED concentrated preparation posterior with shapes (400,400) and rates (400,400) certifies a target of 1 from initial posterior mean total 2. This concentrated context is a mathematical fixture, not a claim that the same low-count specimen has acquired those shapes or that such preparation is free. Targets above current mean abstain, and the zero endpoint remains admitted in the ideal discrete model.

The certificate cannot substitute for calibration or prior validation. Preparation shot-to-shot variability, detector count fluctuations, unknown efficiency, optical drift and controller errors require additional terms. In particular, final count variance includes its mean as well as preparation variance. The present criterion intentionally addresses only preparation-mean uncertainty.

## Verification

`uv run --with sympy python research/sontag/checkers/optical_confidence_policy_v1.py`

12 checks pass, including target expectation, sufficient risk bound, abstention without emitting control, infeasibility and the mixture inequality. A first run exposed a structural-expression comparison in the symbolic identity test; changed it to compare the simplified difference with zero and reran successfully.

Receipt: `results/optical-confidence-policy-v1.json`.

Constructed: information-based policy with an explicit certified/abstain result type. Next net work: integrate the operator-approved scope and optical successor into a versioned review proposal, preserving the exact-reader predecessor and physical-calibration gates. Shared contract remains unchanged.
