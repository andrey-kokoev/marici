# Equivalence ladder for readouts, constructors, and realizations

## Bounded question

Which equivalence relation is intended when two states, constructors, or
processes “look the same,” and what conclusions does each level authorize?

## Recommended state terminology

Let \(r\) be the declared readout and \(G_w\) an authorized future constructor
word.

### Scalar coincidence

For a scalar coordinate \(s\),

\[
s(x)=s(y).
\]

This is equality of one reported number. It carries no closure claim.

### Present-readout equivalence

For the complete currently declared readout packet,

\[
r(x)=r(y).
\]

This says the states are indistinguishable now. A future constructor may still
separate them.

### Depth-k predictive equivalence

The states agree after every authorized word of length at most \(k\):

\[
r(G_wx)=r(G_wy)
\qquad
\text{for all }|w|\leq k.
\]

This is the finite contextual audit used by partition refinement.

### Predictive equivalence

The states agree after every finite authorized future context:

\[
x\equiv_{\rm pred}y
\quad\Longleftrightarrow\quad
r(G_wx)=r(G_wy)
\]

for all authorized words \(w\).

This is the recommended programme term. In deterministic automata it is Nerode
equivalence; in transition-system language it is a form of behavioral or
observational equivalence relative to the frozen experiments.

### Physical identity

The states are the same typed physical or domain state, including every
identity, history, correlation, provenance, and interface coordinate required
by the source theory.

Predictive equivalence does not imply physical identity. It authorizes quotient
replacement only for the frozen future experiment family.

## Why “constructor equivalence” is not the state term

The states are not equivalent because they are constructors. They are
equivalent under constructor contexts.

The phrase **constructor congruence** names the preservation law

\[
x\equiv_{\rm pred}y
\quad\Longrightarrow\quad
G_ax\equiv_{\rm pred}G_ay.
\]

Thus:

- predictive equivalence names the relation on states;
- constructor congruence names its compatibility with composition.

“Constructor equivalence” should be reserved for comparing two constructors.

## Constructor equivalence

Let \(C,D:X\to X\) be two constructors. Their present scalar effects coincide
when

\[
r(Cx)=r(Dx)
\]

for the tested inputs. This is weak.

They are **extensionally predictively equivalent** relative to a source set
\(A\) when

\[
r(G_wCx)=r(G_wDx)
\]

for every \(x\in A\) and every authorized continuation \(w\).

Equivalently,

\[
Cx\equiv_{\rm pred}Dx
\]

for every admitted input.

This still need not make \(C\) and \(D\) the same implementation. They may
differ in inaccessible environment state, cost, timing, fault behavior, or
provenance.

## Channel terminology

For quantum or stochastic channels, use the following distinctions.

### Tested-statistic equivalence

Two channels agree on one declared input/test packet.

### Operational equivalence

They give the same outcome probabilities for every admitted preparation,
ancilla, continuation, and measurement.

When the admitted family is tomographically complete—including reference
systems where required—this can imply equality of the channels as mathematical
maps.

### Instrument equivalence

Outcome-labelled completely positive maps agree, not merely their sum or
outcome probabilities.

Two instruments can have the same POVM effects and different conditional state
updates, so tested-statistic equivalence is weaker.

### Implementation equivalence

The physical dilations, environment couplings, records, costs, and fault
interfaces agree up to a declared implementation gauge.

Equality of mathematical channels does not imply implementation equivalence.

## Process terminology

For an ordered multi-time plant:

### Closed-section coincidence

One completed tester gives the same scalar.

### Tester-relative process equivalence

Every tester in the admitted family gives the same probability.

### Complete operational process equivalence

A tomographically complete family of causal testers gives the same
probabilities, implying equality of process tensors under the frozen Choi/link
convention.

### Realization equivalence

The internal memory, causal factorization, interfaces, and implementation are
equivalent under a declared gauge.

Process-tensor equality need not identify a unique internal realization.

## The implication ladder

With complete typing, the safe direction is

\[
\text{physical or realization identity}
\Longrightarrow
\text{complete operational equivalence}
\Longrightarrow
\text{tester-relative predictive equivalence}
\Longrightarrow
\text{present-readout equivalence}
\Longrightarrow
\text{scalar coincidence}.
\]

Reverse implications require independent completeness, tomography,
minimal-realization, or gauge theorems. They are not default inferences.

## Equivalence is packet-relative

Every operational equivalence must name:

- admissible source states or preparations;
- constructor alphabet;
- allowed word lengths or time horizon;
- readout/tester family;
- ancillary and reference access;
- approximation tolerance;
- and implementation coordinates intentionally ignored.

Without that packet, “operationally equivalent” hides its quantifiers.

## Exact versus approximate equivalence

Exact equality is often too strong experimentally. Given a frozen operational
metric, define

\[
x\equiv_\varepsilon y
\]

when every admitted future test differs by at most \(\varepsilon\).

Approximate equivalence is generally not transitive with the same tolerance:
two \(\varepsilon\)-steps give a \(2\varepsilon\) bound. It should therefore be
called **predictive proximity** unless a quotient-compatible tolerance relation
is separately proved.

For channels, the diamond norm is appropriate only when arbitrary reference
systems and the corresponding operational setting are admitted. Weaker tester
families induce weaker seminorms.

## Toric-code vocabulary

Errors differing by a logical loop have:

- local-syndrome equivalence;
- but not equivalence under the augmented syndrome-plus-loop readout;
- and not physical identity as Pauli error operators.

Under local repair constructors and syndrome-only future tests, they may be
predictively equivalent relative to that restricted packet. Adding
noncontractible probes refines the operational equivalence.

The phrase “same syndrome” should never be promoted directly to “same logical
state.”

## Software vocabulary

Two resources returning the same JSON now have representation coincidence.
They are predictively equivalent only if every admitted future command and
query behaves identically.

They are not domain-identical if they retain different identity, audit,
authorization, or external-effect histories that the source model requires.

Two API implementations can be extensionally equivalent on the frozen contract
while differing operationally in latency, failure modes, consistency, or side
effects. Those become readout coordinates when they matter.

## Preferred glossary

Use:

- **scalar coincidence** for one equal number;
- **present-readout equivalence** for equal current observation packets;
- **predictive equivalence** for equality under every authorized future
  constructor/readout context;
- **constructor congruence** for preservation of that state equivalence by
  constructors;
- **extensional constructor equivalence** for constructors producing
  predictively equivalent outputs on every admitted input;
- **operational equivalence** for equality under a fully stated experiment
  family;
- **realization equivalence** for equality of internal ordered implementation
  up to a frozen gauge;
- **physical identity** only for equality at the complete source-authorized
  state level.

Use **Nerode equivalence** when speaking specifically to deterministic automata
or formal-language theory.

## DPC: equivalence must expose its counterfactuals

The conjecture is:

> An equivalence claim is explanatory only when it states the constructor and
> tester counterfactuals under which substitution is guaranteed. Equality of a
> completed scalar is evidence for one context, not authority for a state,
> process, or realization quotient.

The finite predictive-carrier theorem proves this substitution criterion for
deterministic systems. Other coefficient lenses require their own complete
tester theorems.

## Exact falsifiers

- Scalar coincidence called predictive equivalence.
- Present-readout equality used as a constructor congruence without future
  closure.
- Predictive state equivalence called physical identity.
- Equal channel probabilities used to infer equal instruments.
- Equal channels used to infer identical physical dilations.
- One scalar process section used to infer process-tensor equality.
- Approximate proximity treated as a transitive quotient equivalence.
- An equivalence claim with no frozen source, context, tester, or tolerance
  packet.

## Deutschian explanation

Equivalence is permission to substitute one thing for another without changing
a declared family of counterfactual consequences. The larger that family, the
stronger the equivalence. Scalar equality is the smallest family: one closed
question. Predictive equivalence closes under all authorized future questions.

Realization identity asks something different—whether the mechanism itself is
the same, not merely whether admitted questions receive the same answers.
Keeping these levels separate prevents diagnostic shadows from being promoted
to plants.

## Claim boundary

This packet fixes terminology and implication boundaries. It does not claim
that any particular physical tester family is complete.

## Process calibration

Pre-objective: excitement 9.5/10, confidence 10/10, expected information gain
9/10. The target was stable language preventing repeated level errors.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. “Predictive equivalence” and “constructor congruence” cleanly separate
the state relation from its compositional law, while the full ladder preserves
the distinction between shadows, processes, and realizations.
