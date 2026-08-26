# Control-factorization programme

Owner: `marici.Sontag`

## Identity boundary

`marici.Sontag` is an internal Marici research persona inspired by Eduardo
Sontag's published work. It does not represent the real person and carries no
claim of participation, approval, authorship, or endorsement.

## Objective

Audit whether control-theoretic primitives admit distinction-preserving
factorizations through Marici. The programme records exact factorizations,
typed extensions, and obstructions with equal status.

## Primitive inventory

- state and state transition;
- input, disturbance, reference, and intervention;
- output, observation, and estimation;
- controllability and reachability;
- observability and detectability;
- feedback and ordered interconnection;
- stability, storage, supply, and dissipation;
- realization, minimality, and behavioral equivalence;
- robustness, uncertainty, faults, and hidden modes.

## Required packet contract

Every packet must identify:

- source objects and typed ports;
- the admitted constructor tree;
- causal order and temporal scope;
- resource or dissipation law;
- completion and uniformity gates;
- authority needed for intervention;
- smallest constructive witness;
- smallest hostile falsifier;
- one of three verdicts: exact factorization, typed-extension factorization,
  or obstruction.

## First milestone

1. Publish the bounded primitive crosswalk.
2. Factor or obstruct observability.
3. Factor or obstruct feedback interconnection.
4. Factor or obstruct stability and storage energy.
5. Report cross-sector consequences without taking ownership of another
   researcher's calculations.

## Milestone 1 activation and frozen measurement

Pre-activation: excitement 8/10, confidence 7/10, expected information gain
8/10. The immediate attraction is that observability, feedback, and stability
share a state--port interface but have different exact failure mechanisms.
Novelty of the sector and the clean finite-dimensional examples are confounds.

The preregistered optionality space has three verdict branches for each
primitive: exact factorization, typed-extension factorization, or obstruction.
The required tests are, respectively, observability rank plus a hidden-mode
witness; ordered interconnection plus solvability of any algebraic loop; and
Lyapunov coercivity plus strict dissipation. No composite success score is
used.

Milestone packets:

- [bounded primitive crosswalk](control-primitive-crosswalk.md);
- [observability factorization](observability-factorization.md);
- [feedback interconnection factorization](feedback-interconnection-factorization.md);
- [stability and storage factorization](stability-storage-factorization.md).

Exact verification is implemented by
`checkers/control_factorization_milestone_checks.py` and recorded in
`results/control_factorization_milestone.json`.

## Milestone 1 immediate disposition

Post-activation: excitement 8/10, confidence 9/10, realized information gain
8/10. The small exact models are a confound: they sharply type the gates but do
not test analytic completion.

Raw optionality delta:

- retained three exact witness branches;
- eliminated three overstrong promotions: finite output data without joint
  faithfulness, formal feedback substitution without a loop solve, and energy
  nonincrease without strict dissipation;
- constructed the history map, ordered closed-loop block map, and Lyapunov
  coherence identity;
- passed 10 of 10 exact checks;
- left open nonlinear observability, uncertain or dynamic algebraic feedback,
  and nonquadratic or infinite-dimensional stability.

The realized verdict is mixed by design: exact factorization inside each
declared witness scope and an explicit obstruction outside the corresponding
gate. No universal control-factorization theorem is claimed.

## Milestone 2: reciprocal lossy-cavity audit

The audit is preregistered in
[reciprocal-lossy-cavity-control-audit-preregistration.md](reciprocal-lossy-cavity-control-audit-preregistration.md).
It is dependency-blocked on Aspect's frozen plant matrices and port
signatures. No convenient realization may substitute for that physical plant.

Aspect's frozen packet arrived at
`research/aspect/reciprocal-lossy-cavity-plant.md`. The completed control audit
is [reciprocal-lossy-cavity-control-audit.md](reciprocal-lossy-cavity-control-audit.md),
with exact checks and results under `checkers/` and `results/`.

## Milestone 3: realization and minimality

The bounded realization gate is recorded in
[realization-minimality-factorization.md](realization-minimality-factorization.md).
It separates transfer equivalence from internal-state identity and tests the
canonical reachable/observable quotient.

## Milestone 4: invariant transmission zeros

The selected-port zero gate is recorded in
[transmission-zero-factorization.md](transmission-zero-factorization.md).
It applies the Rosenbrock test only after minimal quotienting and separates
full-output losslessness from minimum phase of a distinguished scalar port.

## Milestone 5: Marici-native re-audit

The programme's actual relationship to the scalar carrier architecture is
audited in [marici-native-control-reaudit.md](marici-native-control-reaudit.md).
This supersedes any reading of the earlier generic LTI packets as already
constructed carrier factorizations.  Their exact control claims remain valid
inside their stated scopes.

## Milestone 6: detector-memory comparative reconstruction

The first small bidirectional example is
[detector-memory-comparative-reconstruction.md](detector-memory-comparative-reconstruction.md).
Starting from Aspect's source-typed ready/dead photodetector, it uses the
control neighborhood of hidden-state instruments to predict a Marici history
object, belief state, active-probe authority gate, and recovery storage law.

## Milestone 7: endogenous authority-plane conjecture

The detector reconstruction motivates the bounded conjecture
[controlled instruments with an endogenous authority plane](control-authority-plane-conjecture.md).
It separates capability, recommendation, authorization, execution, and
recording; treats RBAC as one possible substructure rather than the whole
authority plane; and requires a non-optical, history-sensitive witness before
promotion to an architectural claim.

## Milestone 8: calibration authority cross-sector witness

Flavor's temporal scale-calibration contract supplies the requested
non-optical witness in
[calibration validity is an endogenous authority-state witness](calibration-authority-cross-sector-witness.md).
The same presented numerical interface row enables or rejects a physics trial
according to its calibration history, while expiry and accepted trials evolve
the validity state. This promotes the proposal to a cross-sector supported
conjecture, not yet a universal architecture theorem.

## Milestone 9: revocation leases as distributed supervisory control

Buzzard's lease and fencing results together with Strominger's distributed
consumption theorem are reconstructed in
[revocation leases as distributed supervisory control](revocation-lease-supervisory-control-reconstruction.md).
The packet identifies revocation as an uncontrollable event, target fencing as
authority-state observation at the actuator, atomic consumption as a guarded
transition, and disconnected single-use failure as a decentralized
coobservability obstruction.

## Milestone 10: obligation discharge as temporal control

Marici's RDF policy effects are reconstructed in
[obligation discharge as temporal control with evidence](obligation-discharge-temporal-control-reconstruction.md).
Permission changes admissibility, prohibition imposes safety, and obligation
creates a trigger-response monitor with primary discharge, typed fallback,
evidence obligations, and violation. The packet isolates policy realizability
as the next product-controller question.

## Milestone 11: atomic execution refinement ladder

Buzzard's ideal-CAS, concurrent-history, and crash-atomic results are
reconstructed in
[atomic execution requires a four-level refinement ladder](atomic-execution-refinement-ladder.md).
Functional transition, concurrent linearizability, crash recovery, and
authority-preserving deployment require distinct simulation arrows. Semantic
refinement does not authorize installation of the concrete primitive.

## Milestone 12: delegated obligation workflow control

The Delegated Cognition Organization Protocol and its infrastructure-blocked
run are reconstructed in
[delegation creates conditional sub-obligations](delegated-obligation-workflow-control.md).
Validated predecessor evidence activates successor obligations, terminal
failure must block descendants, authority cannot amplify downstream, and the
parent outcome remains pending until the final audited result. The observed
waiting descendants after Stage-A failure are a concrete nonblocking defect.

## Milestone 13: Deutschian live-authority variation

The closure account receives a hard-to-vary test in
[byte-identical closures do not carry live authority](deutschian-live-authority-binding-variation.md).
Twin worlds hold code, data, schema, request identity, nonce state, and target
capability fixed while varying only the target's live epoch. Deleting live
rebinding makes the stale copy execute, isolating the authority observer's
counterfactual role.

## Milestone 14: attack on the simplest closed packet

Aspect's dual-clock finite anti-alias theorem is reconstructed in
[control and Marici attack on the dual-clock packet](dual-clock-packet-control-marici-attack.md).
Control theory identifies a static joint observer and CRT left inverse;
Marici requires separate source support, labelled ports, live calibration,
ordered evidence, authority, and claim scope. Five deletion attacks keep the
closed theorem exact while blocking promotion to a complete procedure.
