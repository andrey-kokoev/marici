# Closure-planning remediation

**Subsequent execution:** the selected source-contract audit returned `+-`; see `source-contract-audit.md`. The planner now consumes that observation, stops this one-shot portfolio, and reports `replan_required_after_observed_attempt`. The central numbers and 48-scenario recommendation below describe the **pre-attempt forecast**, not a recommendation to repeat the audit.

## Failure corrected

The previous bridge calculator optimized local information gain and did not invoke the existing sequential planner. Its ranking was then described as an optimal next test for closure. That substituted the wrong objective and omitted downstream costs and unlocks. The existing engine already supported prerequisites, branch effects, target decoders, and sequential expected cost; it needed a populated model and integration, not a replacement engine.

## Authoritative calculation for the declared objective

- Contract: `contracts/current-problem-closure-planning.v1.json`.
- Compiler/checker: `checkers/check_closure_planning.py`.
- Engines reused: `research/conjecture_net/interpretation_planner.py` and `objective_projection.py`.
- Result: `results/closure-planning.json`.
- Objective: maximize **positive closure probability for the current source-derived whole-section route**, then minimize expected total effort.

This is not the ten-topic theorem, universal uniqueness, or an optimization of positive-or-negative resolution of every possible lift. Rejection of a particular operational construction does not negatively close the general lift conjecture. A different objective must be declared and computed separately.

## Inputs and execution semantics

Five stages encode the source-contract audit, source derivation, ScheduledNormBound, remaining phase analytics, and whole-section integration. There are nine directional actions (the audit has only a proof direction). The analytics stage explicitly covers pi endpoints, continuity, generator compatibility, and fresh verification, rather than treating unit norm as the whole bridge.

Hypothetical successes add named interfaces. The final decoder requires the typed source contract, source derivation, the actual norm certificate, the full phase interface, reconstruction, and schedule coherence. An audit alone cannot certify the lift; a source derivation conditional on analytics cannot close the route until those premises are discharged.

The portfolio allows one bounded attempt per stage. An inconclusive result stops this portfolio and triggers replanning; it does not refute the claim. Prove/reject alternatives consume the same stage ticket. These restrictions and subjective conditional-on-arrival probabilities are explicit modeling assumptions, not properties of all possible research strategies. The audit's success probability and remaining-analytics costs are new assistant estimates; source estimates are provisional until the audit fixes the contract.

## Central result

**First test: the one-cycle source-contract audit.**

| Forced first action | Positive closure probability | Expected total effort |
|---|---:|---:|
| Source-contract audit | 0.00477603 | 4.462886 |
| Prove ScheduledNormBound | 0.00477603 | 8.089886 |
| Reject ScheduledNormBound | 0 | 4 |

These are portfolio forecasts, not probabilities of mathematical truth. Expected effort includes early abandonment. The all-success path costs **23 cycles**, not 4.46. The low closure probability reflects demanding that five bounded attempts all succeed in this one-shot portfolio.

The computed all-success policy is: audit → source derivation → scheduled norm → remaining analytics → whole-section integration. Starting with the cheap structural bottleneck avoids expensive analytic work on branches where the source contract or derivation fails.

The audit remains first in all **48 tested low/high sensitivity scenarios**. That is finite stress-test stability, not a globally optimal research policy or robustness proof over the full parameter space. The earlier local-information report remains available only as a non-authoritative diagnostic.

## Numerical defect also corrected

The shared planner and objective projection compared success probabilities with exact floating-point ordering. Equivalent products computed in different orders differed at about `1e-18`, causing the engine to choose more expensive policies. Both now use a relative-only `1e-12` tie tolerance before comparing cost; zero is never tied with a positive probability. The planner also skips zero-probability branches.

Regression tests cover downstream-cost ordering, missing decoder prerequisites, no false unlock from inconclusive outcomes, audit versus source derivation, impossible analytics, zero-probability branches, numerical ties, genuinely different success probabilities, and exclusion of rejection from positive closure. Existing shared-engine regression scripts also pass.

## Reproduction

1. `python research/nima/checkers/check_closure_planning.py`
2. `python research/nima/checkers/check_bridge_planning.py`
3. `python research/nima/checkers/check_current_problem_conjecture_net.py`

The net's `optimizer` now comes from the sequential closure result. The previous local single-claim optimizer is explicitly historical. Source hashes prevent using stale planning results. No scientific outcome has been promoted by this remediation.
