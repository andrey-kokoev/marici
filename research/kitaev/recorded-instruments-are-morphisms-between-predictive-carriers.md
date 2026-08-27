# Recorded instruments are morphisms between predictive carriers

## Bounded question

Can recording, state update, test transport, record forgetting, and conditional
feedback be placed in one compositional structure without treating a formal
branch label as a physical record?

## Finite recorded instrument

Let \(A\) and \(B\) be finite-dimensional quantum state carriers. A recorded
instrument from \(A\) to \(B\), with finite record alphabet \(R\), is a family

\[
\mathcal I=\{\mathcal I_r:A_\ast\to B_\ast\}_{r\in R}
\]

of completely positive trace-nonincreasing maps such that

\[
\sum_{r\in R}\mathcal I_r
\]

is trace preserving.

For input state \(\rho\), the instrument produces the classical–quantum state

\[
\widehat{\mathcal I}(\rho)
=
\bigoplus_{r\in R}\mathcal I_r(\rho).
\]

The trace of block \(r\) is the record probability. The normalized block, when
its trace is positive, is the conditional output state.

The direct-sum carrier is mathematical. Calling its index a stable physical
record additionally requires a source-derived apparatus, storage, transport,
and access map.

## Future tests on the recorded carrier

A binary future test that may depend on the record is a tuple of effects

\[
B=(B_r)_{r\in R},
\qquad
0\leq B_r\leq I_B.
\]

Its effect value on the instrument output is

\[
\sum_r\operatorname{Tr}[B_r\mathcal I_r(\rho)].
\]

Define the Heisenberg pullback

\[
\mathcal I^*(B)
=
\sum_r\mathcal I_r^*(B_r).
\]

Then

\[
\sum_r\operatorname{Tr}[B_r\mathcal I_r(\rho)]
=
\operatorname{Tr}[\mathcal I^*(B)\rho].
\]

This pullback is the canonical transport of future questions through the
recording transition.

## Predictive-carrier packet

A finite predictive-carrier packet consists of:

- a state carrier \(A\);
- an admitted future-test family \(T_A\);
- the predictive equivalence induced by \(T_A\);
- and the source authority describing which tests and constructors are physical.

A recorded instrument is a typed morphism from packet \(A\) to packet \(B_R\)
when

\[
\mathcal I^*(T_{B_R})\subseteq T_A.
\]

Every admitted future question on the output then has an admitted pulled-back
question on the input.

If two input states are predictively equivalent under \(T_A\), no output test
in \(T_{B_R}\) can distinguish their instrument images. Therefore the
instrument descends through the predictive quotient.

## Composition of recorded instruments

Suppose \(\mathcal I\) produces record \(r\in R\). After observing \(r\), an
authorized downstream instrument

\[
\mathcal J^{(r)}=\{\mathcal J_{s|r}\}_{s\in S_r}
\]

acts on the conditional output.

The composite instrument has record pairs \((r,s)\) and branches

\[
\mathcal K_{r,s}
=
\mathcal J_{s|r}\circ\mathcal I_r.
\]

Complete positivity is preserved, and summing every pair is trace preserving.

Composition is associative because composition of the branch maps is
associative. The identity morphism is the singleton-record identity channel.
Record alphabets combine as typed histories rather than being erased between
steps.

## Pullback functoriality

Let \(C_{r,s}\) be a future effect conditioned on the complete record pair. The
composite pullback is

\[
\mathcal K^*(C)
=
\sum_{r,s}
\mathcal I_r^*\!\left(
\mathcal J_{s|r}^*(C_{r,s})
\right).
\]

This equals first pulling the test through \(\mathcal J\), retaining its
dependence on \(r\), and then pulling through \(\mathcal I\).

Therefore typed predictive-carrier morphisms compose. If every output test of
\(\mathcal J\) pulls into the admitted middle family and every admitted middle
test pulls through \(\mathcal I\), every composite future test pulls into the
admitted source family.

The backward transport of tests is contravariant to the forward transition of
states.

## Record forgetting

The record-forgetting channel maps the block state to

\[
\mathcal F
\left(
\bigoplus_r\sigma_r
\right)
=
\sum_r\sigma_r.
\]

Composing with the recorded instrument gives the unconditioned channel

\[
\Phi=\sum_r\mathcal I_r.
\]

A future test after forgetting must use the same effect \(B\) in every record
block. Its pullback is

\[
\Phi^*(B)=\sum_r\mathcal I_r^*(B).
\]

Record-dependent effects are absent from this smaller future tester family.
Forgetting is therefore a quotient of control capability, not merely deletion
of a redundant label.

## Record coarse-graining

Let

\[
q:R\to\bar R
\]

merge fine records. The coarse instrument is

\[
\bar{\mathcal I}_{\bar r}
=
\sum_{r:q(r)=\bar r}\mathcal I_r.
\]

A downstream controller descends through this quotient exactly when its chosen
continuation is constant, up to authorized equivalence, on every reachable
fibre of \(q\).

Coarse-graining changes both the record algebra and the admissible conditional
constructor family. It is not fully specified by summing probabilities alone.

## Conditional feedback

For a family of channels \(C_r:B_\ast\to C_\ast\), record-conditioned feedback
produces

\[
\Psi(\rho)=\sum_r C_r(\mathcal I_r(\rho)).
\]

If the record is forgotten before control, only one common channel \(C\) may be
applied:

\[
\Psi_{\rm coarse}(\rho)=C\left(\sum_r\mathcal I_r(\rho)\right).
\]

These maps generally differ. Their difference is the operational value of the
record relative to the admitted controller family.

The record provides no advantage when all authorized continuations \(C_r\) are
equivalent on every reachable branch. This is the exact zero-value condition.

## Same channel, different instruments

Two instruments can satisfy

\[
\sum_r\mathcal I_r
=
\sum_s\mathcal J_s
\]

while having different record alphabets, branch maps, and conditional feedback
capabilities.

They are equivalent after record forgetting but not necessarily as recorded
morphisms. A channel therefore does not determine its instrument decomposition.
Stinespring uniqueness of the channel does not select a detector basis or
record map.

## Minimal qubit witness

Consider computational-basis dephasing. One instrument records the projective
branches:

\[
\mathcal I_j(\rho)=P_j\rho P_j.
\]

Another description forgets the record and retains only

\[
\Phi(\rho)=P_0\rho P_0+P_1\rho P_1.
\]

The unconditioned system state is identical. With the fine record, a controller
may apply \(X\) after record one and the identity after record zero, resetting
both basis inputs to state zero. Without the record, that branch-dependent
policy is unavailable.

The difference is neither the closed channel nor a hidden Kraus label. It is an
accessible classical port coupled to an authorized continuation family.

## Predictive equivalence transport

Let two source states agree on every pulled-back output test:

\[
\operatorname{Tr}[\mathcal I^*(B)\rho]
=
\operatorname{Tr}[\mathcal I^*(B)\sigma]
\]

for every admitted \(B\). Then their recorded outputs are predictively
equivalent relative to the output test packet.

This gives a morphism-relative source equivalence. It can be coarser than the
full input predictive equivalence if the instrument discards information, and
finer than equality under the unconditioned channel when record-dependent tests
are retained.

## Classical and software specialization

For a finite deterministic system, every instrument branch is a partial state
transition with a record label. The direct sum becomes a disjoint union of
recorded successor states. The same composition, coarse-graining, and feedback
laws reduce to ordinary labelled transition systems.

In software, a command returning a response and changing domain state is an
instrument-like morphism. Forgetting the response, redacting fields, and
allowing later commands to depend on it are distinct API operations. A response
object that is never durably delivered is not an accessible record port.

## Toric-code specialization

Ideal syndrome extraction is an instrument whose record blocks are syndrome
sectors. Forgetting the syndrome gives a dephasing-like channel across those
sectors. Retaining it permits syndrome-conditioned recovery.

Logical classes within one syndrome block remain unresolved unless additional
authorized probes refine the record. A decoder is a conditional continuation,
not part of the syndrome effect itself. Different decoders can follow the same
instrument record.

Fault-tolerant extraction requires a richer morphism containing ancilla faults,
record errors, repeated rounds, and propagation constraints.

## Physical-record authority boundary

The classical–quantum direct sum proves a mathematical factorization. To call
\(r\) a physical record, independently derive:

- a record-producing interaction;
- distinguishable stable record states;
- persistence over the required time;
- transport to the consumer;
- semantic typing of record values;
- and authorized conditional actuation.

If only the branch maps are known, the object is a mathematical instrument. If
the stable port is established but actuation is absent, it is a diagnostic
record. If conditional control is established, it is a feedback interface.

## DPC: predictive-carrier morphism principle

The conjecture is:

> Operational processes should be represented as morphisms between predictive
> carriers. A morphism transports states forward and future tests backward,
> while its record port determines which conditional continuations exist.
> Forgetting and coarse-graining are explicit quotient morphisms, not silent
> changes of interpretation.

The finite recorded-instrument composition and pullback laws prove the
mathematical core. Source authority for physical record stability remains
sector-specific.

## Critics

### The direct sum already assumes a classical record

It represents a classical label mathematically. Physical classicality and
stability still require a decoherence and readout theorem. Coherent memories
need a tensor-factor process model instead.

### Instruments with continuous records are omitted

Correct. They require measurable fields and integration rather than finite
direct sums.

### Predictive test families may change after feedback

Correct. That is why objects are packets and morphisms must state their output
tester family. Composition is defined only where the middle packets agree.

### Equal recorded probabilities may hide different branch states

Correct. Recorded morphism equivalence must test branch-conditioned future
effects, not only the record distribution.

## Machine-readable morphism packet

```json
{
  "code": "predictive_carrier_instrument_morphism",
  "source_carrier": "A",
  "target_carrier": "B",
  "record_alphabet": ["r"],
  "branch_maps": ["I_r"],
  "unconditioned_channel": "sum_r I_r",
  "future_test_pullback": "sum_r I_r_star(B_r)",
  "record_stability": "proved | unproved",
  "coarse_graining": "q or null",
  "conditional_controllers": ["C_r"],
  "predictive_descent_verified": true
}
```

## Exact falsifiers

- Branch labels treated as stable physical records without a record map.
- A future output test with no admitted input pullback.
- Composite branch maps whose record histories are silently erased.
- Record forgetting presented as preserving record-conditioned control.
- A coarse controller that differs inside one merged record fibre.
- Equal unconditioned channels presented as equal recorded instruments.
- Equal record probabilities presented as equal branch states.
- A coherent quantum memory forced into a classical direct-sum carrier without
  a decoherence theorem.

## Deutschian explanation

A record matters because it changes the morphisms available afterward. The
instrument creates correlated successor blocks; future questions pull backward
through those blocks, and controllers may choose different continuations in
each one. Forgetting identifies the blocks and removes those distinctions from
the control language.

The structure explains both observation and intervention with one composition
law. It also identifies the exact physical gap: a formal block index becomes a
record only when a source-derived interface makes it stable and accessible.

## Claim boundary

This packet proves the finite classical-record instrument composition and test
pullback structure. It does not derive physical record stability, continuous
records, or coherent-memory implementation.

## Process calibration

Pre-objective ratings were excitement 10/10, confidence 9/10, and expected
information gain 10/10. The target was a compositional structure for recording
without manufacturing physical record authority.

Post-objective ratings are excitement 10/10, confidence 10/10, and realized
information gain 10/10. Recorded instruments compose as predictive-carrier
morphisms; state flow, test pullback, forgetting, coarse-graining, and feedback
now occupy distinct canonical maps.
