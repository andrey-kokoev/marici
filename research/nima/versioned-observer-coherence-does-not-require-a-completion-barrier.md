# Versioned observer coherence does not require a completion barrier

## Implemented temporal test

The bounded-resource control note raises a concrete coherence issue: unequal-cost realization routes can finish on different source versions. They must not be compared as if they observed the same instantaneous input.

The new checker imports the four declared latency schedules from `../voevodsky/checkers/check_bounded_resource_tact_challenge.py` without rerunning or changing its control experiment. It uses two dedicated single-job workers, no queue, and independent immediate restarts. There is no common release or completion barrier.

This is a **coherence and retention test, not a controller**. Open-loop rational commands replace the control loop, and a conservative bound on unobserved disturbance per step is declared explicitly. No tracking or settling result is claimed.

## 1. Transport the evidence, not just its center

The admitted plant is

`x[t+1]=x[t]+u[t]+w[t+1]`, with `|w[t]|<=1/10`.

A report retains its immutable sample timestamp, completion timestamp, interval, normalization, route label and command integral at sampling. The receiver knows command history and the disturbance bound. It does not receive the actual kick times or values.

Transport from sample time s to current time t adds the known command integral and the full admitted uncertainty interval

`[-(t-s)/10, +(t-s)/10]`.

The checker verifies that this transport composes across intermediate times and commutes with three invertible affine observer coordinates, including a negative scale. It also checks both algebraic source-evaluation routes `A(B+C)` and `AB+AC` on their labelled input snapshot.

Different versions are not forced to have equal raw readings. Their transported evidence must admit a common history. A point predictor that ignores unobserved disturbances fails the sensor-only error bound in every schedule; a model declaring zero disturbance becomes inconsistent with the retained reports.

## 2. Retain the joint trajectory

The historical state is a closed rational difference-bound system containing the admitted dynamics, initial interval and every arrived observation. It represents all compatible trajectories, not independent intervals at each time.

The incremental implementation is checked against an independent full closure calculation. Adding the same reports in reverse order gives the identical closed joint constraint system. Thus asynchronous arrival ordering changes when evidence becomes available, not its eventual joint meaning.

Independent state marginals are insufficient: the test exhibits individually admitted endpoints that violate a between-time dynamical constraint when combined.

## 3. Freshness and archival retention are different policies

Reports older than twelve units are excluded from the current fresh-report calculation. They remain unchanged in the historical archive and can constrain the joint history through the declared model.

All four schedules have mixed-version updates and stale exclusions. Updates can use one fresh report rather than wait for a paired completion. Every omitted stale report remains recoverably present.

Pending worker snapshots at the finite horizon are retained separately. They are not yet delivered and are never used in observer updates. This prevents the audit boundary from silently erasing in-flight source evidence.

A contradictory later report yields an empty compatible-history set; it does not rewrite an earlier reading.

## 4. What this establishes

In this finite model, the temporal observer squares and evidence-retention discipline do not require a shared execution cycle. They do require causal version labels, command history, an admitted dynamics/error model and correctly transported joint evidence.

This is consistent with the owning control experiment but does not extend its gain sweep or prove control stability. There is no claim about shared-processor contention, equal energy, communication loss, adversarial delays, paired-evidence tasks or unknown disturbance bounds.

The test belongs to the observer-realization lane because it checks whether different computation routes and historical versions can be compared coherently. Scheduling agreement is not substituted for source/observer compatibility, and a freshness gate is not interpreted as permission to erase history.

## Verification

`python research/nima/checkers/check_versioned_observer_history_without_tact.py`

Artifacts:

- `research/nima/results/versioned-observer-history/tests.json`
- `research/nima/results/versioned-observer-history/retained-history-example.json`

The report preserves individual schedules, work counts, version-mixing counts and failure witnesses. All coherence/retention assertions pass; the checker intentionally demonstrates the inadequacy of unjustified point-only and zero-disturbance models.
