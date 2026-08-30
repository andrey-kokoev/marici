# Finite instruments factor through pointer sectors

## Bounded question

What mathematical interaction structure underlies every finite recorded quantum
instrument, and which parts of that structure are record semantics rather than
Kraus representation gauge?

## Frozen instrument

Let \(H_A\) and \(H_B\) be finite-dimensional Hilbert spaces. Let

\[
\mathcal I=\{\mathcal I_r\}_{r\in R}
\]

be an instrument with finite record alphabet \(R\). Choose Kraus operators for
each branch:

\[
\mathcal I_r(\rho)
=
\sum_{\alpha=1}^{m_r}
K_{r\alpha}\rho K_{r\alpha}^*.
\]

Normalization of the instrument is

\[
\sum_{r,\alpha}K_{r\alpha}^*K_{r\alpha}=I_A.
\]

The branch probability is

\[
p_r(\rho)=\operatorname{Tr}[\mathcal I_r(\rho)].
\]

## Pointer-dilation theorem

Introduce an ancilla space with orthonormal basis

\[
\{|r,\alpha\rangle_E}.
\]

Define

\[
V:H_A\to H_B\otimes H_E
\]

by

\[
V|\psi\rangle
=
\sum_{r,\alpha}
K_{r\alpha}|\psi\rangle\otimes|r,\alpha\rangle_E.
\]

Normalization gives

\[
V^*V=I_A,
\]

so \(V\) is an isometry.

For each record value, define the pointer projector

\[
\Pi_r
=
\sum_\alpha|r,\alpha\rangle\langle r,\alpha|.
\]

Then

\[
\mathcal I_r(\rho)
=
\operatorname{Tr}_E
\left[
(I_B\otimes\Pi_r)V\rho V^*(I_B\otimes\Pi_r)
\right].
\]

Thus every finite instrument factors mathematically through one isometric
interaction and an orthogonal pointer decomposition.

## Three indices with different types

The dilation contains three distinct labels.

- The input state label belongs to the source carrier.
- The declared record label \(r\) indexes pointer sectors and instrument
  branches.
- The refinement label \(\alpha\) indexes Kraus alternatives within one record
  sector.

The instrument exposes \(r\), not \(\alpha\). Summing over \(\alpha\) defines
the conditional branch state. Treating \(\alpha\) as an additional record
refines the instrument and requires a new pointer port.

## Within-sector Kraus gauge

For each fixed \(r\), replace the Kraus family by

\[
L_{r\beta}
=
\sum_\alpha u^{(r)}_{\beta\alpha}K_{r\alpha},
\]

where \(u^{(r)}\) is an isometry on the coefficient space. This leaves
\(\mathcal I_r\) unchanged.

On the dilation space, this is an environment isometry that preserves every
pointer sector:

\[
U\Pi_r=\Pi_rU.
\]

Therefore within-sector Kraus refinement is representation gauge for the
declared instrument.

The individual \(\alpha\) alternatives have no record authority unless the
pointer decomposition is physically refined and read out.

## Cross-sector mixing changes record semantics

An environment unitary that mixes the subspaces \(\Pi_rH_E\) generally changes
the pointer projectors and hence the branch maps. The forgotten channel

\[
\Phi=\sum_r\mathcal I_r
\]

may remain unchanged, because it depends only on tracing the entire environment.
The recorded instrument need not remain unchanged.

Thus the gauge group depends on the object being compared:

- for the forgotten channel, arbitrary environment isometry is dilation gauge;
- for the recorded instrument, only isometries transporting the pointer sectors
  and every named record structure are gauge;
- for a physical apparatus, detector modes, energies, locations, and fault
  interfaces may restrict the gauge further.

## Coarse-graining pointer sectors

Given a record map

\[
q:R\to\bar R,
\]

define

\[
\bar\Pi_{\bar r}
=
\sum_{r:q(r)=\bar r}\Pi_r.
\]

The induced coarse branch is

\[
\bar{\mathcal I}_{\bar r}
=
\sum_{r:q(r)=\bar r}\mathcal I_r.
\]

Pointer coarse-graining and instrument coarse-graining are therefore the same
mathematical operation under the dilation.

The fine record can support conditional continuations that do not descend to
the coarse pointer. The dilation displays exactly which orthogonal sectors were
merged.

## Record forgetting

Forgetting the record replaces all pointer projectors by the identity on the
ancilla and traces out the ancilla:

\[
\Phi(\rho)
=
\operatorname{Tr}_E(V\rho V^*)
=
\sum_r\mathcal I_r(\rho).
\]

This erases the pointer-sector algebra from the accessible output packet. It
does not prove that the environment sectors ceased to exist physically; it
states that the reduced channel and its tester family ignore them.

Actual erasure, decoherence, thermalization, and inaccessible retention are
different physical mechanisms with the same reduced mathematical operation.

## From isometry to unitary interaction

In finite dimension, the isometry \(V\) can be extended to a unitary on a
larger space after adjoining a fixed ancilla preparation. Therefore every
finite instrument has a mathematical model consisting of:

1. an ancilla initialized in a fixed state;
2. a joint unitary interaction;
3. an orthogonal pointer measurement;
4. a partial trace over unobserved ancilla refinement.

This is a realization theorem inside quantum mechanics. It does not identify a
laboratory Hamiltonian, interaction time, stable macroscopic pointer, or
fault-tolerant readout.

## Physical record gate

The pointer projectors define mutually exclusive mathematical alternatives. A
stable physical record additionally requires:

- dynamically distinguishable pointer states;
- suppression or control of interference between record sectors over the
  required time;
- a readout coupling to a downstream carrier;
- persistence under expected noise;
- semantic calibration of the labels;
- and consumer access.

Without these, the dilation supplies an ancilla decomposition but no completed
record interface.

Decoherence can help stabilize a pointer algebra. It does not select the
pointer decomposition from the channel alone; the interaction Hamiltonian and
environment coupling supply that source structure.

## Same POVM, different branch state

The record effect of branch \(r\) is

\[
E_r=\mathcal I_r^*(I_B)
=
\sum_\alpha K_{r\alpha}^*K_{r\alpha}.
\]

The effects determine record probabilities:

\[
p_r(\rho)=\operatorname{Tr}(E_r\rho).
\]

They do not determine the conditional output maps \(\mathcal I_r\).

Two instruments may have identical \(E_r\) and different output states. Their
pointer probabilities agree while future branch-conditioned tests distinguish
them. The full morphism is the instrument, not its POVM shadow.

## Minimal qubit witness

Consider the record effects

\[
E_0=|0\rangle\langle0|,
\qquad
E_1=|1\rangle\langle1|.
\]

One instrument preserves the measured basis states:

\[
\mathcal I_j(\rho)=P_j\rho P_j.
\]

Another prepares state zero after either record:

\[
\mathcal J_j(\rho)
=
|0\rangle\langle j|\rho|j\rangle\langle0|.
\]

Both have the same record probabilities for every input. Their conditional
outputs differ for record one. A future \(Z\) test on that branch distinguishes
them perfectly.

This is the smallest witness that effect equivalence is weaker than instrument
equivalence.

## Composition at the dilation level

Let a second instrument act conditionally on record \(r\). Its dilation uses a
new ancilla with pointer sectors indexed by \(s\). Sequentially composing the
isometries produces a joint environment whose pointer sectors are indexed by
the history pair \((r,s)\).

Tracing out both refinements gives the composite branch maps

\[
\mathcal J_{s|r}\circ\mathcal I_r.
\]

Thus the record-history composition law of predictive-carrier morphisms has a
direct pointer-sector realization. Erasing \(r\) before the second interaction
removes the possibility of choosing the conditional dilation indexed by \(r\).

## Toric-code instance

Ideal syndrome extraction can be dilated by coupling data qubits to ancillas,
with orthogonal ancilla pointer sectors labelled by syndrome values. Internal
fault paths within one reported syndrome are refinement labels, not additional
trusted records.

A physical syndrome port requires ancilla measurement, classical storage, and
calibration. Fault-tolerant extraction must prove that hidden refinement paths
do not create uncontrolled logical errors and that record faults are typed.

The syndrome POVM alone does not determine the recovery map or the conditional
post-extraction data state.

## Optical instance

A polarization measurement can be modeled by unitary coupling to spatial or
detector modes followed by pointer detection. The detector label is physical
only when the modes propagate to stable, distinguishable records.

A lossy polarizer that retains only transmission is a coarse instrument with a
discarded or unobserved complementary port. Introducing a mathematical reflected
mode does not prove that the apparatus preserved and exposed it.

## Software instance

The analogue of \(r\) is a declared response or event type. The analogue of
\(\alpha\) is an internal execution path producing the same external record.

Refactoring internal paths within one response class is representation change
when every future domain effect agrees. Mixing paths across response classes
changes the contract. Exposing an internal trace identifier as a new API field
refines the record interface and requires explicit authority.

## DPC: pointer-sector factorization

The conjecture is:

> Every declared finite quantum record should be audited through a pointer-sector
> dilation. The declared record labels must correspond to source-derived pointer
> sectors; hidden Kraus refinements remain gauge inside those sectors; and
> physical record status requires an independent stability and transport
> theorem.

The finite dilation theorem proves existence of the mathematical factorization.
The source-native pointer decomposition and physical stability remain the
explanatory work.

## Critics

### The dilation is highly nonunique

Correct. Minimal dilations are unique only up to the relevant environment
isometry. Named pointer sectors reduce the admitted gauge to isometries that
transport them coherently.

### Orthogonal pointer sectors already look classical

They define a commutative projector algebra, but physical classicality requires
stability and accessible copying or readout. Orthogonality alone is not a
macroscopic record theorem.

### Continuous records are excluded

Correct. They require measurable pointer spaces and operator-valued measures.

### Unitary realization makes every instrument executable

No. It proves abstract finite-dimensional realization after arbitrary ancilla
and unitary enlargement. Laboratory locality, energy, precision, timing, and
fault constraints remain unproved.

## Machine-readable factorization

```json
{
  "code": "finite_instrument_pointer_dilation",
  "instrument_records": ["r"],
  "kraus_refinements": ["alpha"],
  "isometry": "V",
  "pointer_projectors": ["Pi_r"],
  "normalization_verified": true,
  "within_sector_gauge": "block isometry",
  "cross_sector_mixing_changes_instrument": true,
  "physical_pointer_stability": "unproved",
  "record_transport": "unproved"
}
```

## Exact falsifiers

- An instrument with branch maps not recovered by the proposed pointer
  projectors and partial trace.
- A dilation map failing the isometry normalization.
- An internal Kraus refinement presented as a record without a refined pointer
  port.
- Cross-sector environment mixing called instrument gauge while record branches
  change.
- Equal POVM effects used to infer equal conditional branch maps.
- An abstract unitary extension presented as a laboratory implementation.
- Orthogonal ancilla sectors presented as stable physical records without a
  persistence and transport theorem.
- A forgotten complementary optical port presented as accessible because it
  appears in a dilation.

## Deutschian explanation

An instrument is not an arbitrary list of branch maps. All branches can arise
from one interaction whose ancilla decomposes into pointer sectors. The record
label identifies a sector; hidden Kraus labels describe unresolved structure
inside it. Coarse-graining merges sectors, while forgetting removes the pointer
algebra from future access.

The theorem explains the mathematical unity of state update and record
probability. It also identifies what mathematics does not explain: why one
pointer decomposition is physically stable, transported, and meaningful to a
consumer.

## Claim boundary

This packet proves the finite-dimensional instrument dilation and gauge
typing. It does not derive a physical pointer basis, decoherence rate, detector,
or implementation cost.

## Process calibration

Pre-objective ratings were excitement 10/10, confidence 9.5/10, and expected
information gain 10/10. The target was a common interaction factorization for
recorded instrument morphisms.

Post-objective ratings are excitement 10/10, confidence 10/10, and realized
information gain 10/10. Every finite instrument factors through orthogonal
pointer sectors; record labels and internal Kraus refinements now have distinct
gauge types. Physical pointer stability remains the exact source boundary.
