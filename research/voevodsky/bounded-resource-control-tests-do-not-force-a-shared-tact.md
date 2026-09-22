# Bounded-resource control tests do not force a shared tact

## The question and the fixed definition

Can unequal-cost coupled routes meet the same control requirements without a common periodic schedule or a repeated completion barrier?

Before testing, shared tact was defined as either of those two coordination mechanisms. Shared timestamps, a plant model and knowledge of actuator commands were NOT defined as a tact. The asynchronous policy is not retrospectively relabelled synchronized merely because it retains that common information.

The experiment is finite and deterministic. It does not establish a universal asynchronous-control theorem or any Planck-scale interpretation.

## Model and resource contract

Both routes implement the same anchored transformation:

    A(B+C)x = ABx+ACx = x.

They receive immutable labelled source snapshots, but have different completion costs. Four stipulated latency patterns include skew, bursts and a reversed bottleneck. All costs lie between one and twelve scheduler units.

The plant is x[k+1]=x[k]+u[k], with step-reference changes and unannounced additive state kicks. The controller holds u=-g*(estimate-reference) between updates.

Every policy has two dedicated single-worker routes, at most one job per worker, no job queue and one message per completion. The same latency sequences, plant, disturbances and gain are used for each policy at a given comparison point.

This equal-capacity contract does not require equal work actually performed. Asynchronous workers often complete more jobs while synchronized policies idle. Actual work and completion counts are reported; equal energy expenditure is not claimed. There is no processor contention or communication loss in this model.

All controllers transport old readings to the current control time using the known actuator integral. No current true plant value or unknown disturbance is supplied to the controller. This prediction is exact for the integrator between unknown kicks, up to numerical accumulation error.

## Policies

1. Fixed tact: sample and commit at the worst-case common period.
2. Completion barrier: wait for both routes, then commit and release the next common batch.
3. Independent pair: each worker restarts immediately; update from the latest available reports without waiting for matching versions.
4. Independent fresh: the same independent scheduling, but exclude over-age reports from the CURRENT control calculation. An update may use one or two fresh reports.

Excluding a report from current actuation is not authorization to erase acquired historical evidence under the source-retention rule.

The last policy uses no recurring join barrier. It needs a fresh estimate of the plant, not simultaneous agreement from both redundant routes. A task requiring fresh paired evidence at EVERY actuation would be a different contract.

## Baseline: the asynchronous policies failed

At gain 0.035, the requirements were:

- sample age at update at most 12;
- settling deadline 120 units after a reference change or kick;
- maximum error over the last 20 steps at each deadline below 0.03;
- tracking error outside settling windows below 0.35.

Fixed tact and the completion barrier passed all four schedules. The independent-pair policy violated freshness. Freshness gating removed those violations but still missed the settling test: deadline-window errors were approximately 0.0369 to 0.0386.

That failure is preserved in the artifact. The thresholds were not relaxed.

## Diagnostic gain sweep

A labelled POST-BASELINE sweep then varied the same gain for every policy. Budgets, schedules, disturbances and acceptance limits stayed unchanged.

Numbers below are passing schedules out of four:

| Gain | Fixed tact | Barrier | Independent pair | Independent fresh |
|---|---:|---:|---:|---:|
| 0.025 | 0 | 0 | 0 | 0 |
| 0.035 | 4 | 4 | 0 | 0 |
| 0.050 | 4 | 4 | 0 | 4 |
| 0.075 | 4 | 4 | 0 | 4 |
| 0.150 | 1 | 4 | 0 | 4 |
| 0.200 | 0 | 4 | 0 | 4 |

The naive independent pair continues to violate the age bound. The freshness-gated independent controller meets the entire contract at several common gains without imposing a shared release or completion cycle.

At gain 0.05, 73–90% of its updates combine different source versions. Only 10–13% of worker release times coincide. Maximum consumed age remains twelve. Its deadline-window errors are approximately 0.0065–0.0074.

These observations are not evidence of emergent phase locking. The restart policy and stipulated cost schedules do not adapt their phases to the plant.

## Why the ranking changes

The same numerical gain does not have the same discrete-time effect under different hold intervals. In an undisturbed interval of length h, with an exact current-state estimate and constant reference, the held controller gives

    e_next=(1-g*h)e.

Frequent small updates can settle more slowly than less frequent held commands at one gain. A long fixed hold can become oscillatory or expansive at another gain. The observed ranking therefore cannot be attributed to synchronization alone.

This is why the baseline success of fixed tact did not establish necessity, and why selecting only the successful asynchronous gain would also have been misleading.

## What the test establishes

Within this model, a fixed common tact or repeated completion barrier is NOT necessary for meeting the tested contract. Versioned prediction and freshness gating provide another mechanism.

The test does not remove timing requirements. It still uses a common causal time reference, bounded ages, actuator history, a model and a control deadline. It separates these requirements from the stronger requirement of a common execution cycle.

The result is conditional on a simple, accurately known plant and redundant routes. The most important remaining challenges are model error, irreversible coupled actions requiring both branches, shared-resource contention, work/energy quotas, sensor uncertainty and adversarial rather than enumerated delay schedules.

## Reproduction

    python research/voevodsky/checkers/check_bounded_resource_tact_challenge.py

Artifact: `results/bounded-resource-tact-challenge.json`.

The report's `passed` field means experiment-integrity checks passed. Individual policy failures remain explicit. Baseline results are reproduced exactly inside the sensitivity sweep.
