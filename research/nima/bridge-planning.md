# Open-bridge attempt planning

**Scope correction:** this report ranks local information only. It is not authoritative for closure decisions. The existing sequential planner is now wired through `contracts/current-problem-closure-planning.v1.json`; see `closure-planning-remediation.md`. It accounts for prerequisites and downstream costs and selects the source-contract audit under the declared positive-closure objective.

Contract: `contracts/current-problem-bridge-planning.v1.json`.
Recompute: `python research/nima/checkers/check_bridge_planning.py`, then run `check_current_problem_conjecture_net.py`.

## Status and scope

These are assistant-proposed subjective estimates, not observed frequencies or operator-approved priors. They do not change conjecture outcomes. Costs are bounded work-cycle budgets, not elapsed time or guaranteed closure costs. The prior net's top-level lift cost model remains a historical, differently scoped estimate.

Each of the three bridges now has a scoped next claim, separate proof/rejection protocols and costs, stopping rules, conditional certificate probabilities, dependencies, and outcome consequences. Ranges are low/central/high stress-test values, not confidence intervals.

| Scoped target | Prior truth (central) | Proof budget | Rejection budget | Ready? |
|---|---:|---:|---:|---|
| Actual scheduled norm bound | .95 | 6 | 4 | Yes |
| Audited source-derived lift | .20 | 4 | 3 | No: contract audit first |
| Whole-section replacement coherence | .70 | 4 | 3 | No: source and full phase interfaces first |

The completion target is only ScheduledNormBound: pi, endpoints, continuity, and generator laws are not included in its budget. Source-contract estimates must be revised after the claim is typed; they are not solver admission.

## Ranking and sensitivity

Local expected information is `H(prior) - P(inconclusive)*H(posterior | inconclusive)` under a sound-certificate model. Divide by the attempt budget. A failed proof or rejection is still logically inconclusive; Bayesian changes occur only under the explicitly subjective likelihood model.

The central conditional ranking in bits/work-cycle is:

1. Whole-section rejection: .0794 (blocked).
2. Whole-section proof: .0754 (blocked).
3. Source-lift proof: .0595 (blocked).
4. Source-lift rejection: .0300 (blocked).
5. Scheduled-bound rejection: .0201 (ready).
6. Scheduled-bound proof: .0080 (ready).

This is NOT an optimal closure plan. It measures information about separate local claims, excludes prerequisite costs from conditional actions, and does not value successful construction itself. For a high-prior theorem, rejection can have higher information gain even when proving it is the useful engineering task.

One-at-a-time changes already change the winner. In 2,000 seeded range scenarios, all six actions win at least once (counts: 801, 479, 367, 287, 57, 9 in the order above). Counts are sensitivity diagnostics, not probabilities that an action is optimal. Dependencies and cross-claim correlations prohibit adding these information gains into a total-net score.

## Decision

No stable optimum is established. Run the **one-cycle source-contract audit** before committing to a long downstream proof: type the source-derived lift, list external choices, and test the interface against the known pointwise-selection obstruction. The diagnostic has no invented outcome distribution or IG score; it is selected as a cheap structural prerequisite.

After the audit, revise the target claims, readiness, costs and likelihoods; rerun the ranking. Preserve the scoped evidence whether the audit succeeds or merely exposes missing definitions.
