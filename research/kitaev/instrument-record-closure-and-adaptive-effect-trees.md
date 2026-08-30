# Instrument record closure and adaptive effect trees

## Bounded question

When does an environmental branch become source data that a controller may use,
and what information about an adaptive quantum protocol survives in its final
scalar success probability?

## Channel branches are not records

A completely positive map may be written

\[
\Phi(X)=\sum_a K_aXK_a^*.
\]

The index \(a\) is not automatically an observable event. Equivalent Kraus
families are related by isometries on the coefficient space and describe the
same unrecorded channel. Treating \(a\) as controller input before declaring a
physical environment measurement changes the constructor family.

A typed instrument is stronger data:

\[
\mathcal I=\{\mathcal I_a\}_{a\in\Omega},
\qquad
\sum_a\mathcal I_a=\Phi,
\]

where \(a\) is written to an authorized classical record port. The outcome
probability and conditional state are

\[
p(a|\rho)=\operatorname{Tr}\mathcal I_a(\rho),
\qquad
\rho_a=\frac{\mathcal I_a(\rho)}{p(a|\rho)}
\]

when the denominator is nonzero.

The record requires four typed arrows:

1. a physical coupling from system to environment or apparatus;
2. an environment readout defining the instrument decomposition;
3. a classical storage channel preserving the outcome label;
4. controller access authorizing later choices to depend on that label.

Environmental interaction alone supplies none of the last three.

## Adaptive instrument tree

Let a history \(h=(a_1,\ldots,a_j)\) label a node. At that node the controller
selects an authorized instrument or channel as a function of the recorded
history. Each leaf \(\ell\) therefore carries a completely positive path map

\[
\mathcal M_\ell
=
\mathcal I_{h_{j-1},a_j}\circ\cdots\circ\mathcal I_{\varnothing,a_1}.
\]

Choose a set \(S\) of successful leaves and a final target projector \(P_B\).
Define the success effect

\[
E_S=\sum_{\ell\in S}\mathcal M_\ell^*(P_B).
\]

Then

\[
p_S(\rho)
=
\sum_{\ell\in S}
\operatorname{Tr}\bigl(P_B\mathcal M_\ell(\rho)\bigr)
=
\operatorname{Tr}(E_S\rho).
\]

Thus every finite adaptive protocol has a scalar diagnostic shadow: one
positive effect satisfying \(0\leq E_S\leq I\) for a normalized instrument
tree.

Positivity again forbids cancellation between successful leaves. A positive
success probability means at least one successful recorded path has positive
weight.

## Effect equivalence is not realization equivalence

The success effect determines the probability functional and nothing more.
It does not determine:

- the leaf maps;
- the conditional output states;
- the record distribution;
- the disturbance on failure leaves;
- the controller decisions available at intermediate nodes;
- or the correlations with an environment.

The smallest witness uses one qubit and the common effect

\[
E=|0\rangle\langle0|.
\]

Two single-Kraus success maps are

\[
K_0=|0\rangle\langle0|,
\qquad
K_1=|1\rangle\langle0|.
\]

Both satisfy

\[
K_0^*K_0=K_1^*K_1=E,
\]

so they give the same success probability on every input. Their successful
outputs are orthogonal. Scalar readout therefore cannot reconstruct the
operator-valued lift.

At the total-channel level, dephasing in the \(Z\) basis and dephasing in the
\(X\) basis both have normalization effect \(I\), yet preserve different
classical algebras and destroy different coherences. Normalization is a still
coarser shadow.

## Record coarsening theorem

Let a record map \(q:\Omega\to\bar\Omega\) forget distinctions between fine
outcomes. The coarsened instrument is

\[
\bar{\mathcal I}_{\bar a}
=
\sum_{a:q(a)=\bar a}\mathcal I_a.
\]

Every controller using only \(\bar a\) must choose the same continuation on all
fine histories in a fibre of \(q\). Hence coarsening has two exact effects:

- it adds the corresponding positive path maps and effects;
- it removes policies that distinguish histories inside one fibre.

A fine controller descends through the record quotient exactly when its future
action is constant on every reachable fibre, up to an authorized equivalence
of continuations.

This is the classical record analogue of descent through a carrier quotient.
The lost datum is not merely a label; it is the conditional constructor choice
that the label enabled.

## Feedback can exceed open-loop word mixing

Consider a qubit promised to be either \(|0\rangle\) or \(|1\rangle\). Admit a
computational-basis measurement and a bit flip conditioned on its recorded
outcome. The adaptive policy is:

- on outcome zero, do nothing;
- on outcome one, apply \(X\).

Both inputs end as \(|0\rangle\) with probability one.

If the measurement record is erased before control, the unconditioned
measurement merely dephases. A continuation that cannot depend on the outcome
must either flip both branches or neither; it cannot send both orthogonal
inputs to \(|0\rangle\) using only the admitted identity and bit flip.

Classical randomization between those open-loop continuations reaches success
probability at most one half on the hostile input distribution. The adaptive
advantage comes from correlation between the recorded branch and its future
constructor, not from selecting a hidden Kraus term after the fact.

## Closure criterion for usable real-world interaction

An interaction has become usable source data only relative to a declared
closure packet containing:

\[
(\text{instrument},\ \text{record alphabet},\ \text{storage},\
\text{transport},\ \text{controller access}).
\]

If any arrow is absent, the correct effective description is coarser:

- no readout: sum over environmental branches;
- readout without storage: a transient outcome, unavailable later;
- storage without transport: a local record outside the controller interface;
- transport without typing: bits with no admitted outcome semantics;
- typed record without actuation authority: diagnostic data only.

Therefore closure does not mean that every real interaction is automatically
recorded. It means that every distinction transported through the complete
declared packet is available to downstream source constructors. Availability
is a theorem about the full path, not a property of interaction alone.

## DPC: record-relative constructor closure

The Deutsch-Popperian conjecture is:

> Every reproducible adaptive advantage over an unrecorded channel is explained
> by a source-derived record distinction that survives storage and transport
> and changes at least one authorized continuation. If no such distinction
> exists, the claimed advantage can be reproduced by a controller on the
> coarsened channel, or the model has imported hidden branch authority.

This is explanatory rather than merely confirmatory because it identifies what
must be physically different: an accessible record fibre on which continuation
laws differ. It prohibits explaining feedback by renaming mathematical Kraus
indices.

## Critic of the DPC

The conjecture is false if “record” is restricted to explicit classical bits.
Coherent quantum feedback can route a control system through an ancilla without
ever producing a classical outcome. The correct broader carrier is an
accessible control memory, classical or quantum.

With that correction, the conjecture becomes:

> Adaptive advantage requires an accessible memory system whose distinguishable
> states remain correlated with the relevant interaction alternatives and
> condition inequivalent authorized continuations.

The classical instrument theorem in this packet proves the finite commutative
case. A coherent-memory version requires quantum combs or process tensors and
cannot be inferred from the scalar success effect.

## Machine-readable first failures

Suggested obstruction codes are:

```json
{
  "code": "branch_label_is_not_an_authorized_record",
  "missing_arrow": "readout | storage | transport | typing | controller_access",
  "coarse_channel": "sum of inaccessible branch maps",
  "claimed_conditional_action": "continuation identifier"
}
```

and

```json
{
  "code": "adaptive_policy_does_not_descend_through_record_quotient",
  "coarse_outcome": "record fibre",
  "fine_histories": ["h1", "h2"],
  "continuations": ["C1", "C2"],
  "authorized_equivalence": false
}
```

## Exact falsifiers

- A Kraus index used as feedback data without a typed instrument port.
- Two fine histories merged while retaining different downstream actions.
- Identical success effects presented as proof of identical state update.
- A scalar success probability used to reconstruct the instrument tree.
- A transient detector event presented as stored controller memory.
- A stored bit whose semantic relation to an instrument outcome is untyped.
- An adaptive advantage reproduced after all claimed record distinctions are
  coarsened while preserving the same authorized continuation family.
- A classical-record theorem promoted to coherent quantum feedback without an
  accessible quantum-memory model.

## Deutschian explanation

Feedback works because interaction alternatives are copied into an accessible
memory and that memory changes which constructor is applied next. Erasing the
record does not merely reduce knowledge; it identifies histories that formerly
carried different future laws. That quotient removes a physical control
capability.

The scalar effect is a diagnostic shadow of the complete tree. It tells how
often the declared success occurs for each input, but not how the plant was
disturbed, which histories occurred, or which conditional mechanisms produced
the result. Those missing structures are precisely why an ordered realization
cannot be inferred from its scalar completed section.

## Claim boundary

This packet proves finite classical-instrument and effect identities. It does
not derive a laboratory instrument, certify record fidelity, treat indefinitely
long feedback, or prove the coherent-memory extension.

## Process calibration

Pre-objective: excitement 10/10, confidence 9/10, expected information gain
10/10. The target was the exact point where an environmental alternative
becomes legitimate controller data.

Post-objective: excitement 10/10, confidence 9.5/10, realized information gain
10/10. The boundary is the instrument-to-record-to-controller path. Scalar
effects completely capture success probabilities but erase the realization;
record coarsening removes exactly the policies that vary inside a forgotten
fibre. Coherent memory is the next genuine generalization.
