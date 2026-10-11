# Estimated effort and value for the completion-refinement net

Parameters: `contracts/completion-refinement-planning.v1.json`.
Computed receipt: `results/completion-refinement-planning.json`.

The original tables below are **historical subjective, uncalibrated pre-attempt estimates**, conditioned on the imported standard theorem and operational norm. They are not imported from the predecessor's stopped audit portfolio.

## Current conditioning after pi acceptance

The operator accepted the mixed pi certificate (kernel construction/endpoints plus written standard-real identification). The pi node is now proved at that level. Its old estimates are retained but its actions are removed from the current portfolio. The existing joint truth model is conditioned on pi=true; other costs and likelihoods are not re-estimated.

Regularity is now also freshly kernel-proved: the same resumed attempt constructed its dyadic modulus and full all-scale/all-time/all-increment derivative. The current model is conditioned on this additional closure and removes both resolved analytic actions. The aliased flow-rejection test is unavailable because regularity is already proved.

Current computed recommendation: **prove/operational-spectral-whole-return-certificate**. The same-phase flow and full operational half-turn are freshly kernel-checked, with standard-pi identification retained at its explicitly accepted mixed level. Their resolved actions are removed; earlier half-turn +- attempts remain historical. In the retained 24-EU scenario the central success probability is 0.672 and expected effort 4.0; these are model outputs, not measured remaining-budget forecasts or a budget reset. All 27 retained sensitivity scenarios select whole-return assembly (resolved analytic cost variations now have no effect).

Only the whole-return node remains open. See `constructed-unitary-half-turn.md` and `unit-circle-flow-progress.md` for the assembled prerequisites. See `phase-metric-regularity-progress.md` and `machin-pi-progress.md`.

## Historical pre-acceptance forecast

## Effort and bounded-attempt forecasts

An effort unit (EU) is one focused proof/edit/check work cycle, not elapsed minutes. Proof costs below are marginal costs **after prerequisite certificates exist**. Disproof attempts have no proof-prerequisite requirement. A failed attempt does not establish the opposite proposition.

| Claim | Current p(true) | Prove EU (range) | P(++) when ready | Reject EU (range) | P(-+) now |
|---|---:|---:|---:|---:|---:|
| Pi half-turn | .9800 | 8 (5–13) | 63.70% | 10 (6–18) | 0.40% |
| All-scale metric regularity | .9700 | 5 (3–9) | 72.75% | 8 (5–14) | 0.90% |
| Unit-circle flow | .9700 | 1 (1–2) | 98.00% | 8 (5–14) | 0.90% |
| Unitary half-turn | .96236 | 1 (1–3) | 95.00% | 12 (8–20) | 0.7528% |
| Whole-return certificate | .9332756 | 4 (3–8) | 67.20% | 18 (12–30) | 0.6672% |

Conditional proof-completion sensitivities given truth are .65, .75, .98, .95, .70 respectively. Conditional rejection-completion sensitivities given falsity are .20, .30, .30, .20, .10. Impossible sound outcomes have probability zero: ++ when false, and -+ when true. The remaining mass is +- or --.

The high prior plausibility reflects the standard mathematical construction. Low refutation chances reflect the need for an actual counterexample/nonexistence proof rather than an implementation timeout. Assembly remains work even when prerequisite truth entails the intermediate proposition.

## Joint model and shared evidence

The model does not multiply five independent marginal priors:

- Pi and all-scale regularity initially have probabilities .98 and .97, provisionally independent.
- Pi-scale regularity is certain if all-scale regularity holds; if all-scale regularity fails, its probability is .40.
- Unit-circle flow has the same truth value as all-scale regularity because norm is proved.
- The half-turn requires pi endpoints and pi-scale regularity. All-scale regularity is a sufficient route, not a necessary one.
- The target probability is .96 given the half-turn, and .25 if that specific half-turn fails. This preserves possible alternative implementation routes and does not create an automatic parent-refutation edge.

Flow rejection is an alias of the regularity rejection experiment. It is charged and observed once, not treated as independent evidence. Distinct canonical experiments are assumed independent conditional on a truth world. There are nine canonical actions, not ten.

Each prove action requires actual prerequisite proof certificates. Probability one is not a substitute for those certificates. Information metrics for dependent proof attempts are conditioned on their prerequisites being proved; this is why flow/half-turn assembly has zero claim information gain but substantial certificate value.

## Primary objective: obtain the positive certificate

The optimizer maximizes the probability of obtaining the target ++ within a **24-EU budget**, then minimizes expected total effort. Each canonical action is available once. It updates hypothetical world probabilities after both successful and unsuccessful attempts and allows abandonment. Refutation can save work, but does not itself satisfy this positive objective.

Central policy's success branch:

1. Prove metric regularity.
2. Prove pi half-turn endpoints.
3. Assemble unit-circle flow.
4. Assemble the unitary half-turn.
5. Assemble the whole-return certificate.

Including shared prerequisites once, the remaining successful-route costs are 8 EU for pi, 5 for regularity, 6 for flow, 15 for the half-turn, and 19 for the final certificate. The full successful path costs **19 EU**. Accounting for branches that stop early, expected work is **13.4633 EU** and positive-closure probability is **0.2899288**. These are finite-portfolio forecasts, not a 29% probability that the mathematical target is true.

After an actual attempt, record the outcome and explicitly replan. A failed proof exhausts that bounded proof action in this portfolio; the checker does not invent retries or automatically refute its claim.

## Secondary diagnostic: information per effort

Expected information about the tested claim, in bits/EU:

| Claim | Prove, when ready | Reject, now |
|---|---:|---:|
| Pi half-turn | .00372 | .00232 |
| Metric regularity | .01162 | .00596 |
| Unit-circle flow | 0 | .00596 (same rejection experiment) |
| Unitary half-turn | 0 | .00306 |
| Whole-return certificate | .01671 | .00147 |

The receipt also reports information about the final target and the whole joint world model. Target-information-per-EU alone currently favors a target rejection attempt, whereas the positive-certificate objective favors proving regularity. These are different objectives; the diagnostic is not substituted for the declared closure policy.

## Sensitivity

Across 27 combinations of pi/regularity proof costs and sensitivities:

- regularity-first: 13;
- pi-first: 11;
- no positive route within the 24-EU budget: 3.

The ordering is therefore parameter-sensitive, not robustly optimal across the tested ranges. The central recommendation is still **prove metric regularity**.

## Recompute

```text
python research/conjecture_net/test_bayesian_outcome_planner.py
python research/nima/checkers/test_completion_refinement_planning.py
python research/nima/checkers/check_completion_refinement_planning.py
python research/nima/checkers/check_completion_refinement_net.py
```

The net checker rejects stale planning receipts and keeps planning estimates separate from proof outcomes.
