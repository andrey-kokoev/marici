# Delegation creates conditional sub-obligations, not discharged accountability

Owner: `marici.Sontag`

Source: Delegated Cognition Organization Protocol and 2026-08-17 run report

Status: exact workflow reconstruction with observed hostile

## Bounded question

When a parent task is decomposed across agents, does delegation transfer the
original obligation, or construct a dependency-indexed family of
sub-obligations?

The source protocol defines three output-dependent stages: extract, reduce,
and audit. Downstream stages receive only validated predecessor output,
authority may not increase downstream, and failed or malformed predecessors
must block descendants. The recorded run supplies a real hostile: Stage A
failed while B and C remained in a waiting state instead of reaching durable
dependency-blocked terminals.

## Workflow state

Represent each stage by

\[
s_i\in\{\text{waiting},\text{running},\text{succeeded},
\text{failed},\text{blocked}\}.
\]

The parent outcome monitor is

\[
o_P\in\{\text{pending},\text{discharged},\text{failed}\}.
\]

Initially A runs while B and C wait. A validated success activates B; B's
validated success activates C; C's validated audited result discharges the
parent outcome. Worker termination alone is insufficient: malformed output is
a failed contract, not success evidence.

## Conditional obligation activation

B is not immediately obliged to execute when the pipeline is submitted. Its
obligation is conditional on a valid Stage-A evidence packet. Likewise C is
conditional on B. This prevents premature work and prevents invalid data from
crossing a stage boundary.

The handoff relation is therefore

\[
\text{validated predecessor evidence}
\Longrightarrow
\text{activate successor obligation}.
\]

Transport of arbitrary bytes does not activate the successor. Validation is
the evidence-bearing trigger.

## Failure propagation and zombie obligations

If A fails or returns malformed output, B cannot safely execute and C cannot
become reachable. Their correct terminal state is `blocked`, not `waiting`.
A descendant that remains waiting after its enabling condition has become
impossible is a zombie obligation: it is neither executable, discharged,
cancelled, nor terminally reported.

In supervisory-control language, the workflow is blocking because it has
entered a reachable state from which its marked completion state is
unreachable while live-looking pending states remain. Durable blocked
reconciliation converts that ambiguity into an explicit terminal outcome.

## Parent accountability is retained

Submitting A, B, and C does not discharge the parent obligation to produce a
validated audited result. Nor does A's success discharge it. Only the final
validated C output closes the parent outcome monitor.

Delegation therefore factors accountability rather than transporting it away:

- each worker bears a scoped conditional stage obligation;
- the orchestrator bears dependency and terminal-state reconciliation duties;
- the parent outcome remains pending until the declared terminal evidence is
  admitted.

An explicit authority rule could novate or transfer responsibility, but task
transport alone does not do so.

## Authority monotonicity

Every downstream worker's authority must be a subset of the authority admitted
for its predecessor and the root run. An output packet can add information but
cannot grant mutation, filesystem, network, or publication powers absent from
the parent authorization.

This is a controlled invariant:

\[
U_C\subseteq U_B\subseteq U_A\subseteq U_{\mathrm{root}}.
\]

Violation means the delegation controller amplifies authority through data
flow.

## Idempotence and recovery

Replaying the same validated predecessor event must not launch duplicate
workers. Completed valid stages must survive restart, while failed predecessors
must rehydrate their descendants as blocked. These are persistence properties
of the workflow controller, separate from worker reasoning quality.

## Control-theoretic interpretation

The pipeline is an event-driven discrete controller or safe workflow net:

- validated outputs are enabling tokens;
- malformed output and timeout are uncontrollable failure events;
- stage launch is a controllable transition;
- blocked and succeeded are marked terminal states;
- authority sets are monotone resource invariants;
- audit completion is the parent discharge observation.

Marici adds actor identity, authority basis, typed evidence imports, and durable
responsibility. Workflow reachability alone cannot say who remains accountable
for reconciliation.

## Verdict

Multi-agent delegation creates conditional sub-obligations and retains parent
accountability unless an explicit transfer constructor says otherwise. The
2026-08-17 run supplies a concrete nonblocking defect: terminal predecessor
failure did not reconcile waiting descendants. The finite checker verifies the
correct transition system and reproduces the hostile.

The exact checker is
`checkers/delegated_obligation_workflow_control.py`; results are recorded in
`results/delegated_obligation_workflow_control.json`.

Pre-activation: excitement 10/10, confidence 10/10, expected information gain
10/10. The live branches were obligation transfer, retained accountability,
terminal failure propagation, and indefinite descendant waiting.

Post-activation: excitement 10/10, confidence 10/10, realized information
gain 10/10. Intermediate success does not discharge the parent monitor;
validated terminal audit does. Malformed and failed predecessors force
transitive blocking, while the recorded run reproduces the zombie-waiting
hostile. Authority monotonicity and event replay tests also pass. The checker
passes 14 of 14. Graph admission is recorded at
`ev-000000005088-6e87ab6a-3775-4a45-9bc0-1343a3971ff4`.

