# Broadcastability is the algebraic record boundary

## Bounded question

When does a mathematical pointer alternative become a record that can be
distributed to several future consumers without changing the information it
carries?

## Frozen definition

Let \(S\) be a family of density operators on a finite-dimensional carrier
\(A\). The family is broadcastable when there is a channel

\[
\mathcal B:A\longrightarrow A_1\otimes A_2
\]

such that, for every \(\rho\in S\),

\[
\operatorname{Tr}_{A_2}\mathcal B(\rho)=\rho,
\qquad
\operatorname{Tr}_{A_1}\mathcal B(\rho)=\rho.
\]

Broadcasting preserves the state in both marginals. It need not produce the
product state \(\rho\otimes\rho\), so it is weaker than cloning.

## Finite no-broadcasting theorem

A finite family \(S\) is broadcastable exactly when its members commute
pairwise:

\[
[\rho,\sigma]=0
\]

This holds for every \(\rho,\sigma\in S\).

Necessity is the no-broadcasting theorem. Sufficiency is constructive. Jointly
diagonalize the family in a basis \(\{|i\rangle\}\), measure that classical
label, and prepare the correlated state

\[
\mathcal B(\rho)
=
\sum_i\langle i|\rho|i\rangle
|i,i\rangle\langle i,i|.
\]

Both marginals equal \(\rho\) for every state diagonal in the common basis.

Thus a state family admits nondestructive informational fanout precisely on a
commutative sector. The algebraic boundary between a quantum carrier and a
copyable record is not orthogonality alone; it is the commutative algebra that
survives repeated broadcasting.

## Pure-state core

Suppose an isometry copies two pure states with a fixed blank state:

\[
V|\psi_j\rangle|0\rangle
=
|\psi_j\rangle|\psi_j\rangle.
\]

Preservation of inner products gives

\[
\langle\psi_1|\psi_2\rangle
=
\langle\psi_1|\psi_2\rangle^2.
\]

Hence the overlap is zero or one. Distinct pure states can be copied only when
orthogonal. The mixed-state theorem replaces orthogonality of individual
states by simultaneous classical diagonalizability of the whole family.

## Pointer sectors versus records

For a finite instrument, orthogonal pointer projectors \(\Pi_r\) generate a
commutative algebra:

\[
\mathcal C_R
=
\left\{
\sum_r c_r\Pi_r
\right\}.
\]

The label \(r\) can be copied to another register by classical fanout:

\[
|r\rangle|0\rangle
\longmapsto
|r\rangle|r\rangle.
\]

Coherence between sectors cannot be included in the copied record algebra. A
copying interaction that exposes \(r\) either removes that coherence from the
reduced carrier or moves it into inaccessible correlations.

This yields a strict ladder:

1. A pointer decomposition supplies mutually exclusive mathematical sectors.
2. A readout distinguishes their labels.
3. Broadcastability lets several downstream consumers receive the same label.
4. Dynamical stability preserves the label over the required time.
5. Calibration gives the copied symbol a source-authorized meaning.
6. A feedback port makes the record available to future constructors.

Only the third item follows from commutativity. Durability, cost, calibration,
and access remain separate implementation theorems.

## Redundant records

Once one classical record exists, the copying map can be iterated:

\[
r\longmapsto(r,r)\longmapsto(r,r,r,r).
\]

This is not a corresponding fanout operation on arbitrary quantum states. The
record can proliferate because its admitted state family lies in a
commutative algebra.

The multiplicity of copies is therefore evidence about a selected classical
observable, not evidence that the entire premeasurement quantum carrier was
copied. Redundant observers may agree on \(r\) while all remain blind to a
conjugate phase.

## Instrument factorization

Let a recorded instrument have branches \(\mathcal I_r\). Its classical-output
channel is

\[
\widehat{\mathcal I}(\rho)
=
\sum_r
\mathcal I_r(\rho)\otimes|r\rangle\langle r|.
\]

Copying the record register gives

\[
\rho
\longmapsto
\sum_r
\mathcal I_r(\rho)
\otimes|r\rangle\langle r|
\otimes|r\rangle\langle r|.
\]

The conditional output state is not copied. Only the commutative record label
is broadcast. This separates three resources that scalar readout conflates:

- branch probability;
- branch-conditioned quantum state;
- broadcastable classical record.

## Toric-code instance

Ideal star and plaquette syndrome values form commuting classical bits after
extraction. They may be copied into controller memory and sent to several
decoder components.

The encoded logical state is not thereby broadcast. In particular, copying a
syndrome record gives no authority to copy or jointly expose conjugate logical
loop observables. The syndrome algebra and the logical algebra occupy different
parts of the carrier.

This explains why controller redundancy can protect a syndrome command while
leaving quantum actuator faults and logical coherence outside its scope.

## Optical instance

A detector click can be amplified into many correlated classical registers.
The incident polarization qubit cannot generally be broadcast. The click
records one commutative outcome algebra selected by the instrument.

Adding a third polarizer may expose intensity hidden by a two-polarizer setup,
but the visible intensity remains a scalar record of a new ordered
intervention. It does not broadcast the unknown incoming polarization state.

## Software instance

An immutable event value can be duplicated across logs, queues, and consumers.
The copy operation preserves the declared symbol. It does not guarantee that
all copies retain provenance, ordering, authorization, or exactly-once
semantics.

The software analogue of the commutative record algebra is a set of values that
can be fanned out without consumer order changing their meaning. Mutable
capabilities, linear resources, and transaction handles are not such records;
duplicating their identifiers does not duplicate their operative state.

## DPC: the copyable-record criterion

The conjecture is:

> A claimed physical record is structurally adequate only after the programme
> identifies the commutative source-derived algebra that can be broadcast to
> independent future consumers. Pointer distinguishability supplies candidate
> alternatives; broadcasting supplies classical fanout; stability and
> calibration supply physical record authority.

This is explanatory rather than merely confirmatory. It says why records can
become public while arbitrary quantum state does not: the interaction selects
a commutative quotient whose information admits fanout.

## Critics

### Measurement and preparation can broadcast commuting states destructively

Correct. The theorem establishes preservation of the admitted marginal state,
not preservation of hidden purification, phase relations, or microscopic
trajectory. A stronger nondemolition claim requires an instrument-level test.

### Approximate broadcasting is possible

Correct. Approximate cloning and approximate broadcasting trade fidelity
against disturbance. The exact theorem identifies the zero-error boundary;
an engineering packet must state the norm, error budget, and accumulation law.

### A restricted noncommuting family might look classical to weak testers

It may be observationally indistinguishable under that tester family, but it
is not exactly broadcastable as states. Weak observational equivalence must not
be upgraded to a copying constructor.

### Broadcasting already proves objective reality

No. It proves that one commutative label can be redundantly distributed.
Objectivity also needs stable transport, independent access, calibration, and
an account of correlations and failure modes.

### A formal classical register is already a record

No. It is a mathematical output type. A physical record requires a constructor
that creates, transports, and preserves the register in the declared medium.

## Exact falsifiers

- A proposed exact broadcaster for two noncommuting density operators.
- A copying map whose two marginals fail to reproduce every admitted input.
- Redundant copies of one pointer label used to infer access to conjugate
  quantum information.
- A record claim based only on orthogonal sectors, without a downstream copying
  or readout constructor.
- A broadcastability theorem used to infer storage lifetime or thermodynamic
  cost.
- A duplicated software token treated as duplication of a linear capability.
- Equality of record probabilities used to infer equality of conditional state
  updates.

## Machine-readable boundary

```json
{
  "code": "broadcastability_record_boundary",
  "admitted_state_family": "S",
  "pairwise_commuting": true,
  "broadcast_channel": "B",
  "both_marginals_preserved": true,
  "copied_algebra": "commutative pointer algebra",
  "conditional_quantum_state_copied": false,
  "physical_stability": "unproved",
  "calibration": "unproved",
  "consumer_access": "unproved"
}
```

## Deutschian explanation

A record becomes shareable because the interaction has converted some
distinction into a commutative carrier. That carrier supports fanout: several
future systems can acquire the same label without competing for an unknown
quantum state. What becomes public is the selected classical distinction, not
the full state that produced it.

The explanation also locates the remaining physical problem. A mathematical
broadcast channel says which information could be copied. It does not say what
apparatus performs the copying, why the copies persist, or why their symbols
mean the claimed source event.

## Claim boundary

This packet states the exact finite-dimensional no-broadcasting boundary and
applies it to recorded instruments. It does not prove approximate-error bounds,
macroscopic stability, thermodynamic feasibility, or source calibration.

## Process calibration

Pre-objective ratings were excitement 10/10, confidence 9.5/10, and expected
information gain 10/10. The confound was that broadcastability might be mistaken
for durability or macroscopic implementation.

Post-objective ratings are excitement 10/10, confidence 10/10, and realized
information gain 10/10. The programme now has an exact algebraic boundary:
copyable record information is commutative, while physical record status still
requires stability, transport, and calibration.
