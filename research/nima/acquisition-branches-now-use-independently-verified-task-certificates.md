# Acquisition branches now use independently verified task certificates

## Result

The A=3 acquisition experiment now runs through the reusable rational solver and its separate verifier, rather than hand-written sign tests.

The run produced 113 verified certificates, including 100 newly generated possible returned intervals. Their final classifications were:

- 53 target-certified;
- 12 ambiguous with opposing feasible sources;
- 34 incompatible with the fixed prior;
- 1 unresolved after the available calibration refinement.

The unresolved case is retained as a gap, not reclassified by inference. The run is a finite conditional outcome catalogue, not coverage of all possible real measurements.

## Fixed model

The prior remains sum_A (A/2)^12 p(x_A)<=40. The old raw feature data and A=2 vacuum interval remain fixed unless an explicitly recorded refinement narrows that interval.

The rational model uses a_0 at A=2, b_2, b_3, b_4 and the aggregate unacquired vacuum tail at A>=5. The last variable has a prior-derived interval, not a fictitious measured reading. Its cost weight is 8*(5/2)^12; a finite forgotten source at A=5 realizes a witness value. Splitting b_4 from this tail permits an actual A=4 acquisition without double counting it.

The target is strict positivity of the aggregate vacuum sum. The independently proved baseline residual positivity is not recomputed or inferred by the rational engine. Analytic calibration validity and the source embedding remain external justified inputs.

## Reproduced decision routes

Every substantive branch has a source witness, universal dual bound, opposing-source pair or cost contradiction accepted by the standalone verifier:

1. A=3 vacuum interval [-0.001,0.001]: TARGET_TRUE.
2. A=3 interval [-0.011,-0.009]: AMBIGUOUS.
3. On that ambiguous branch, an A=4 near-zero reading: still AMBIGUOUS, with verified compatible sources.
4. Specified refinements of the existing A=2 and A=3 vacuum intervals: TARGET_TRUE.
5. The previously open positive-centered A=3 outcome: UNRESOLVED under coarse calibration, then INFEASIBLE with the supplied tighter calibration, without changing observations.

These are conditional conclusions about returned intervals. They do not predict what a measurement will return, assert physical acquisition precision or establish a globally optimal action policy.

## Held-out outcome checks

One hundred additional A=3 centers and radii are generated with a fixed seed, separately from the motivating branch fixtures. Each is classified through the same engine. If unresolved, the procedure tries the independently supplied refined calibration and produces another certificate.

Every certificate is checked by `verify_diagonal_task.py`, which imports no solver code. Parent/child transitions are also audited: budgets, target coefficients and source-cost weights remain identical; observation or calibration intervals may only narrow. Thus a successful branch cannot secretly strengthen its prior or change its question.

Infeasible outcomes mean that the returned interval and declared assumptions cannot all hold. They are not negative task evidence. Ambiguous outcomes have actual conflicting-source witnesses. Unresolved outcomes assert neither feasibility nor impossibility.

## What is now reusable, and what is not

The branch evidence and verification are reusable. Candidate actions currently come from an explicitly supplied finite catalogue; the code compares their specified outcomes rather than inventing new sensors or proving an optimal policy over a continuum of outcomes.

This is enough to distinguish helpful calibration work, helpful refinement, a successful new coordinate and a candidate observation that leaves ambiguity. Measurement/computation costs and guaranteed coverage of all future outcomes remain outside this deliverable.

Filtered attachment or relative-completeness interpretations require their own declared structural inputs. Nothing in these numerical branch certificates reconstructs ideal actions, a filtration or a source-comparison map.

## Reproduction

`python research/nima/checkers/check_certificate_acquisition_planner.py`

Artifact: `research/nima/results/certificate-acquisition-planner.json`.

The artifact contains every complete problem, its separately checked certificate, its parent branch and the held-out classifications. It consumes the previously saved calibrated source fixtures; those analytical assumptions are not re-proved by the exact-rational verifier.
