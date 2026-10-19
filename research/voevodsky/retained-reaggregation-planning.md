# Retained-reaggregation portfolio: estimates and replanning

Model: `contracts/retained-reaggregation-planning.v1.json`.
Ledger: `contracts/retained-reaggregation-attempts.v1.json`.
Engine: shared `research/conjecture_net/bayesian_outcome_planner.py`.

## Estimate status

All probabilities, EU costs and bounded-attempt completion likelihoods were
estimated subjectively for this new scoped experiment. They are **not empirically
calibrated**, not copied from Nima's forecasts and not physical predictions.
An EU is one declared focused attempt cost, not elapsed minutes. Cost ranges
express uncertainty; the live ledger charges the frozen central cost.

| Conditional claim | Prior p(true) | Prove cost EU | Prove success if true | Reject cost EU | Rejection available |
|---|---:|---:|---:|---:|---|
| Common interface | .99 | 1 | .98 | 1 | yes |
| Native signed-record rule | .96 | 2 | .90 | 2 | no current portfolio action |
| Rival defect-record rule | .96 | 2 | .90 | 2 | no current portfolio action |
| Common resource accounting | .95 | 2 | .85 | 2 | no current portfolio action |
| Typed operation classification | .98 | 1 | .93 | 1 | yes |
| Same-input discriminator | .90 | 3 | .80 | 3 | yes |
| Conditional target assembly | conditional joint model | 1 | .95 | 1 | no current portfolio action |

Available rejection actions have declared success .60 when their proposition is
false. Sound ++ is impossible when false; sound -+ is impossible when true.
Unsuccessful attempts have the complementary likelihood and do not resolve truth.
The cost ranges and all likelihoods are machine-readable in the model.

## Joint truth and proof context

All seven conditional claims now have both proof and rejection actions, connecting all four outcome ports per node. The physical-admission node is intentionally outside this conditional model. The six base claims have independent *prior* estimates in this initial model.
No hard scientific contradiction has yet been admitted: the model has an explicit
empty constraint registry rather than fabricated mutual exclusions. Reviewed
`mutually_exclusive` constraints can be added only with source-pinned evidence;
the planner then conditions and renormalizes the joint worlds, and rejects stale
or unsupported constraints. Thus independence is the declared current assumption,
not a discovered fact. Shared obligations (common preparation, vacuum controls,
reference/energy accounting and readout) have one canonical owner/evidence identity
in `contracts/retained-reaggregation-coherence-invariants.v1.json`; consumers
reference those obligations rather than receiving duplicate independent priors.
The target has conditional probability .98 when all six are true, .20 otherwise,
retaining the possibility of an alternative route. Enumeration gives 128 positive
truth worlds. Observations condition this joint model, inducing correlations.
Alternative model assumptions can change the policy and require explicit review.

A truth probability of one is not a certificate. Proof prerequisites are admitted
++ results or explicitly resolved scoped imports. Parent claims are never
promoted just because prerequisites succeeded. The selected route is a certificate
dependency graph, not a logical equivalence or a universal necessity claim.

## Policy and actual history

The objective maximizes positive conditional-target closure probability within the
budget, then minimizes expected effort. The reviewed port-routing migration exposed
the already costed rejection actions for every conditional node. A second reviewed
model migration added the explicit empty hard-constraint registry and shared
obligation semantics; both preserved the hash-chained event history and one EU
already spent, without resetting budget. Abandonment is allowed. Each canonical
proof/rejection action runs once; aliases cannot be introduced as new retries.
A failed action can eliminate the positive route from this one-shot portfolio
without showing the proposition false.

Initial budget: 18 EU. Initial policy recommended `prove/freeze-common-interface`,
with estimated closure probability .3572913 and expected effort 8.6330585 EU.
That action was actually started, charged one EU, freshly checked and admitted ++.
The native signed-record action was then started, charged two EU and admitted ++
after a fresh 45-check source-bound gate across both native chiralities/doublet
choices. The live policy therefore conditions on both proofs and has **15 EU
remaining**:

    recommended action: prove/rival-defect-record-rule
    modeled positive closure probability: 0.4262334
    expected further effort: 6.7910999 EU

These forecasts do not promise real completion effort. The interface theorem is
an exact finite native-metric/projection certificate, not physical calibration.
The target and physical follow-up remain unresolved.

## Sensitivity and information

Twenty-seven scenarios combine hypothetical initial budgets 12,18,24; future
proof-cost multipliers 1,2,3; and future proof-likelihood multipliers .70,.85,1.
Every scenario preserves already spent effort and the current proof context.
They are diagnostics, not live budget changes or a command to retry an exhausted
action. Insufficient-cost scenarios can return no positive route.

The result records per-action current/conditional readiness, cost ranges, outcome
probabilities, claim/target/joint information and information per effort. A separate,
diagnostic-only coherence ranking sweeps weights 0,.1,.25,.5,1 over target
information bits per EU plus normalized transitive downstream unlocks. It does not
change the closure-optimal central policy or truth beliefs. On the current state,
zero coherence weight prefers rejecting the target for information; higher weights
prefer the high-leverage signed/rival components. This is a preference sensitivity
warning, not a scientific recommendation: arbitrary weight units make it unsuitable
as a replacement objective until reviewed. A
hypothetical prerequisite-proof context is explicitly labelled; it is not an
observed theorem. Information gain is diagnostic, not the closure objective.

## Lifecycle commands

`plan` and `status` read/revalidate the contract, evidence and authoritative ledger.
They execute no proof. `start`, `checkpoint`, `pause`, `resume`, `finish` and
`fail` and `review` append hashed events; only supported scoped conclusive receipts admit
scientific outcomes. Failure can be recorded without inventing a proof or
refutation. `run` executes a registered theorem-specific fresh runner.

An unfinished runner remains active if execution stops; continue or resume that
same nonce, or record its bounded failure. After finishing, `review <attempt-nonce>`
can append actual focused effort (EU), blocker category, review disposition and
reviewer without changing the attempt outcome or budget. The existing successful
gate has no independently recorded focused-effort measurement; do not invent a
retrospective one. Calibration reports separate observed effort/review history
from likelihood calibration: proof sensitivity needs independent truth labels for
both successes and failures. Model estimates never change automatically; a reviewed
sample and explicit pinned-model migration are required. Do not silently restart or refund its
cost. Changing the model/contract/engine invalidates the ledger context until a
reviewed migration; ordinary planning never re-pins or resets it.

All conclusive admissions and physical extensions require their own evidence.
The planner cannot infer physical charge, photon identity or calibration from
large subjective likelihoods.
