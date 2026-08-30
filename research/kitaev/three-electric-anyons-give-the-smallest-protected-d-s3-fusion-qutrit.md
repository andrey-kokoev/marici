# Three electric anyons give the smallest protected D(S3) fusion qutrit

## Bounded question

What is the smallest distributed \(D(S_3)\) fusion-space encoding that stores
nontrivial logical information while every accepted operator confined to one
isolated anyon acts as a scalar?

Three electric \(C\) anyons with fixed total charge \(C\) give a
three-dimensional fusion space. Two anyons cannot encode a fixed-total-charge
logical degree of freedom because the frozen fusion ring is multiplicity free.

## Frozen electric fusion rule

The simple electric charge \(C\) has quantum dimension two and obeys

\[
C\otimes C=A\oplus B\oplus C.
\]

The ring is multiplicity free. In particular,

\[
N_{ab}^c\in\{0,1\}
\]

for every triple of simple charges.

For three \(C\) anyons with total charge \(C\), the left-associated fusion
paths are

\[
(C\otimes C\to e)\otimes C\to C,
\]

with

\[
e\in\{A,B,C\}.
\]

Each intermediate channel occurs once, giving the orthonormal logical basis

\[
|A_L\rangle,
\qquad
|B_L\rangle,
\qquad
|C_L\rangle.
\]

Hence

\[
\dim V_{CCC}^{C}=3.
\]

This is the qutrit multiplicity space already used by the exact electric braid
representation.

## Minimal anyon number

For two fixed simple anyons \(a,b\) with fixed total charge \(c\), the fusion
space has dimension

\[
\dim V_{ab}^{c}=N_{ab}^{c}.
\]

Because every multiplicity is zero or one, this dimension never exceeds one.
No pair of simple \(D(S_3)\) anyons can encode a nontrivial logical system while
their individual and total charges are fixed.

Three anyons are therefore the minimum for a fixed-charge fusion encoding.
The triple \(C,C,C\) with total \(C\) realizes dimension three, so the lower
bound is attained.

Encoding across different total-charge sectors would evade the dimension
count only by using superselection labels as logical basis states. Such a
scheme is locally distinguishable by total-charge probes and is not the fixed-
sector protected encoding considered here.

## Ideal single-anyon local indistinguishability

In the ideal semisimple anyon theory, a simple object has

\[
\operatorname{End}(C)\cong\mathbb C.
\]

An accepted topological operator confined to a neighborhood of one isolated
\(C\) anyon and preserving its charge is therefore proportional to the
identity morphism on that leg. Its action on the fusion multiplicity space is

\[
P O_i P=c_i(O_i)P,
\]

where \(P\) projects onto \(V_{CCC}^{C}\).

Thus no charge-preserving single-anyon topological operator can distinguish or
rotate the logical basis \(A,B,C\). The logical information resides in the
joint fusion relation, not in any one excitation.

This is exact in the categorical model. A microscopic lattice realization
must separately bound finite-separation corrections, local leakage, accidental
degeneracy, and virtual processes.

## Charge-changing local faults

A microscopic operator near one anyon may create nearby excitations or change
the apparent local charge. Such an event leaves the accepted fixed-charge
sector and is not covered by the scalar endomorphism theorem.

Fault protection additionally requires:

- local and total charge syndrome extraction;
- a separation scale preventing one local event from reaching another anyon;
- a decoder for created excitation pairs;
- and recovery before the faulty region interacts with another logical
  constituent.

The ideal fusion-space theorem supplies the accepted compression. It does not
by itself supply the microscopic recovery apparatus.

## Existing braid action

In the basis \(A,B,C\), the two elementary electric braids generate the
three-dimensional permutation representation of \(S_3\). It decomposes as

\[
\mathbf1\oplus\mathbf2.
\]

The invariant line is spanned by

\[
|u\rangle
=\frac{\sqrt2|A_L\rangle+|C_L\rangle}{\sqrt3},
\]

and one convenient vector in the standard doublet is

\[
|w_2\rangle
=\frac{|A_L\rangle-\sqrt2|C_L\rangle}{\sqrt3}.
\]

Braiding alone preserves the line and supplies only a five-dimensional
associative block algebra, not the full qutrit algebra.

The distributed encoding therefore achieves storage before it achieves
universal actuation.

## Minimal pair-channel bridge

Let an interaction on the first two anyons apply different energies to their
fusion channels:

\[
H_{12}
=\alpha P_A^{(12)}
+\beta P_B^{(12)}
+\gamma P_C^{(12)}.
\]

In the left-associated logical basis this is

\[
H_{12}=\operatorname{diag}(\alpha,\beta,\gamma).
\]

Its incidence between the braid-invariant line and the standard doublet is

\[
\langle w_2|H_{12}|u\rangle
=\frac{\sqrt2}{3}(\alpha-\gamma).
\]

Therefore a pair-channel phase distinguishes the invariant line from the
doublet exactly when

\[
\alpha\ne\gamma.
\]

By the previously proved single-bridge sufficiency lemma, one such continuously
controllable Hermitian interaction, together with continuously pulsed braid
Hamiltonians, generates the full \(\mathfrak u(3)\) Lie algebra.

The minimum algebraic bridge can be as simple as a phase on the \(A\) channel
or a phase on the \(C\) channel. The \(B\) energy alone does not bridge the
explicit invariant line because \(|u\rangle\) has no \(B\) component.

## Support lower bound for actuation

Every accepted operator confined to one isolated anyon is scalar. Hence a
nontrivial logical actuator must have a causal support that relates at least
two anyon world tubes or changes the encoding projector in time.

The pair-channel Hamiltonian meets the algebraic support lower bound: it acts
on the joint fusion channel of anyons one and two. Physically realizing it may
require:

- bringing the pair together;
- surrounding them with a charge-sensitive loop;
- coupling them to a verified interferometric ancilla;
- code deformation;
- or a measurement-and-feed-forward instrument.

All routes open a corridor that temporarily makes joint fusion information
accessible. None is implied by the fusion projector's abstract existence.

## Protection-actuation boundary

During storage, separated single-anyon neighborhoods are correctable and act
as scalars on the qutrit. During actuation, the pair corridor deliberately
accesses a non-scalar logical observable.

An arbitrary fault in a primitive implementation of \(H_{12}\) can therefore
be a logical overrotation. Topological protection of the storage code does not
detect every actuator fault inside the opened pair corridor.

Fault-tolerant control requires an additional layer:

- encode the fusion qutrit in an outer code;
- synthesize the pair phase from transversal or verified contacts;
- use heralded charge measurement with safe rejection;
- or bound analog control error rather than calling it exactly corrected.

The distributed encoding removes single-anyon local logical faults. It does
not make the intentional nonlocal actuator self-verifying.

## Smallest protected object versus full endpoint algebra

The local 36-dimensional endpoint algebra acts on a localized regular carrier.
The fusion qutrit is a different object: a multiplicity space distributed over
three fixed-charge anyons.

Local endpoint control primitives may help create, move, braid, or measure the
constituents. They do not descend automatically to arbitrary protected qutrit
operations. The descent must preserve total charge, fusion-space coherence,
separation, and fault localization.

This is the first explicit realization of the hierarchy “local endpoint
algebra → distributed fusion encoding → protected logical compiler.”

Only the first two objects are now algebraically frozen. The final arrow
remains a physical gadget theorem.

## Exact falsifiers

- A two-anyon fixed-total-charge fusion space of dimension greater than one in
  the frozen multiplicity-free ring.
- Fewer than three simple anyons claimed to encode a nontrivial fixed-sector
  fusion qudit.
- A charge-preserving operator confined to one simple \(C\) leg acting
  non-scalar in the ideal fusion category.
- Microscopic finite-separation protection inferred from Schur's lemma without
  a lattice bound.
- Braiding alone called universal on \(V_{CCC}^{C}\).
- A pair-channel Hamiltonian with \(\alpha=\gamma\) claimed to bridge the
  explicit invariant line through the \(A,C\) sector.
- Abstract pair fusion projectors called physically executable without an
  actuation corridor.
- Storage protection claimed to detect arbitrary faults in the deliberately
  opened pair corridor.
- Local endpoint controllability identified with protected fusion-qutrit
  control.

## Machine-readable encoding packet

```json
{
  "code": "minimal_d_s3_protected_fusion_qutrit",
  "anyon_type": "C",
  "anyon_count": 3,
  "total_charge": "C",
  "logical_basis": ["A", "B", "C"],
  "logical_dimension": 3,
  "two_anyon_fixed_charge_max_dimension": 1,
  "three_anyons_minimal": true,
  "single_anyon_charge_preserving_compression": "scalar",
  "braid_representation": "1_plus_2",
  "braiding_universal": false,
  "pair_channel_bridge": "diag(alpha,beta,gamma)",
  "bridge_incidence": "sqrt(2)*(alpha-gamma)/3",
  "full_u3_if_alpha_ne_gamma_and_continuous_braid_pulses": true,
  "pair_phase_physically_compiled": false,
  "microscopic_local_indistinguishability_proved": false,
  "outer_fault_tolerance_required": true
}
```

## Deutschian explanation

Two anyons have only one allowed path once their charges and total charge are
fixed, so there is nothing to encode. Three \(C\) anyons have three different
internal fusion histories that lead to the same external charge. No isolated
anyon contains the answer to which history the system occupies.

That makes the qutrit protected during separation. To control it, an apparatus
must compare at least two histories by coupling at least two anyons. The same
corridor that makes control possible also creates a place where a fault can
become logical. Protection is restored by closing the corridor, not by
pretending it was local throughout.

## Shared Carrier geometry and quantum coefficient lens

The shared Carrier geometry is a relational code: logical alternatives are
different internal compositions with identical local marginals and identical
external type. Nontrivial access requires a constructor crossing constituent
world tubes.

The quantum coefficient lens supplies coherent fusion multiplicity, braid
representations, pair-channel projectors, and Lie closure. A scalar fusion
ring identifies the three paths but does not provide their coherent physical
actuators.

## Claim boundary

This packet proves minimality of three anyons from multiplicity freedom, the
dimension-three \(C,C,C\to C\) encoding, ideal single-anyon scalar action, and
the exact pair-channel bridge condition. It does not construct microscopic
anyon preparation, finite-separation error bounds, charge recovery, the pair
phase gadget, or an outer fault-tolerant qutrit code.

## Process calibration

Excitement is 10/10 and confidence in the fusion-level theorem is 10/10. The
programme now has a concrete protected logical carrier rather than only a
localized endpoint algebra. The next exact question is whether a
source-authorized pair-channel measurement or phase already exists in the
frozen ribbon and charge-instrument packets, and if so whether it preserves
coherence strongly enough to serve as the bridge.
