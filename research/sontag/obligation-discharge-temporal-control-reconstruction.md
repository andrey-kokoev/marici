# Obligation discharge as temporal control with evidence

Owner: `marici.Sontag`

Source: Marici authoritative RDF/SHACL agent policy

Status: bounded governance-sector reconstruction

## Bounded question

What structure distinguishes an obligation from permission or prohibition in
the Marici authority plane?

The source policy supplies all three effects. In particular, direct operator
instruction obliges execution unless a safety or authority exception applies,
with a typed blocking report as fallback. State-changing execution separately
obliges recording changed files and a checkpoint. These rules expose a
temporal structure that a static RBAC permission relation cannot represent.

## Safety and response specifications

A prohibition has the safety form

\[
\text{condition}\Longrightarrow \text{never perform forbidden action}.
\]

A permission expands the admissible event set but requires no event to occur.
An obligation has a response form

\[
\text{trigger}\Longrightarrow
\text{eventually(primary discharge or typed fallback)}.
\]

Therefore permission and obligation can authorize the same action while
inducing different accepted history languages. The empty future satisfies a
permission but violates a due obligation.

## Monitor state

Use the finite obligation state

\[
o\in\{\text{inactive},\text{pending},\text{discharged},
\text{fallback-discharged},\text{violated}\}.
\]

A triggering instruction moves `inactive` to `pending`. Traceable execution
moves `pending` to `discharged`. If the declared exception is established,
the specified blocking report moves it to `fallback-discharged`. Expiry of a
declared response horizon while still pending moves it to `violated`.

The horizon is not silently invented by control theory. Some obligations are
bounded by the current turn or lease; others require an independently declared
deadline or fairness assumption. Without either, only an unbounded liveness
claim is available and finite monitoring cannot certify violation.

## Evidence-carrying discharge

An action occurrence and evidence of its occurrence are distinct. For
state-changing work, primary execution can discharge the direct-action
obligation while activating a separate record-execution obligation. The total
governance state is therefore a vector of monitors rather than one Boolean:

\[
(o_{\mathrm{act}},o_{\mathrm{record}}).
\]

After execution without a checkpoint the state is

\[
(\text{discharged},\text{pending}),
\]

not globally complete. Recording the required evidence discharges the second
component. A success message without evidence does not perform that transition.

## Fallback is a typed controller branch

Fallback is not arbitrary nonperformance. It is an authorized alternate
transition enabled by the rule's declared exception. A blocking report without
the safety or authority exception does not discharge the primary obligation;
nor may a different convenient action substitute for the named fallback.

Thus a policy rule defines a small controller with:

- trigger and scope;
- primary controlled event;
- exception observation;
- typed fallback event;
- evidence requirement;
- priority for conflicts;
- terminal and violation states.

## Conflict and feasibility

An obliged action can simultaneously be prohibited by a higher-priority safety
rule. The correct product controller does not execute the prohibited action.
It takes the obligation's declared fallback when available. If no admissible
primary or fallback transition exists, the specification is unrealizable and
must be reported as a conflict, not treated as silent permission to stop.

This is the control-theoretic realizability question for Marici policy:
whether a strategy exists that satisfies all applicable safety and response
conditions under the declared environment events.

## Marici addition to temporal synthesis

Temporal logic and supervisory control supply trigger-response monitors,
safety languages, realizability, and strategy synthesis. Marici additionally
types:

- who bears the obligation;
- which authority created it;
- its target and locus;
- its exception and priority basis;
- which exact fallback is admitted;
- what evidence counts as discharge;
- which durable record carries that evidence.

The result is not merely policy evaluation. It is accountable temporal agency.

## Verdict

Obligation is an endogenous authority-state component with liveness semantics.
It cannot be reduced to a permission bit. The finite witness distinguishes
action discharge from evidence discharge and distinguishes typed fallback from
unjustified nonperformance. Universal policy realizability, deadline
semantics, and multi-agent transfer of obligations remain open.

The exact trace checker is
`checkers/obligation_discharge_temporal_control.py`; results are recorded in
`results/obligation_discharge_temporal_control.json`.

Pre-activation: excitement 9/10, confidence 10/10, expected information gain
9/10. The branches were obligation-as-permission, obligation-as-unbounded
liveness, bounded monitor semantics, and unrealizable safety conflict.

Post-activation: excitement 9/10, confidence 10/10, realized information gain
9/10. Empty-trace and deadline tests eliminate obligation-as-permission;
separate action and evidence monitors eliminate Boolean global completion;
typed fallback resolves the declared safety exception while absence of both
primary and fallback exposes unrealizability. The checker passes 13 of 13.
Graph admission is recorded at
`ev-000000005055-737ffa88-b15c-43ce-8cb0-2578cb840935`.

