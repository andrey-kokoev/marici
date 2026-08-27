# The last bridge incidence is one rank-one joint phase, not a general six-dimensional control

Owner: `marici.Kitaev`

## Bounded question

What is the smallest joint qutrit--fusion operation that realizes the remaining
bridge-incidence isometry?

It is one controlled cube-root phase on a rank-one product projector. After
choosing the first charged route as reference, no arbitrary six-dimensional
unitary is required.

Let `P_A` be the qutrit vacuum-line projector and let `P_1` project onto the
second basis state of the four-anyon fusion qubit. The complete missing
coupling is

\[
C_H
=
\exp\left(\frac{2\pi i}{3}P_A\otimes P_1\right)
=
I+(\omega-1)P_A\otimes P_1.
\]

It applies `omega` only when both the qutrit lies on its vacuum line and the
fusion controller lies in channel one. Every other joint sector is fixed.

This is an exact logical `AND` phase. Separate possession of `P_A`, `P_1`, and
their individual phase gates does not generate it. A microscopic constructor
must couple the two charge predicates coherently.

## Claim boundary

The factorization, operator-Schmidt obstruction, entanglement witness, and
fault calculations below are exact finite-dimensional results.

The packet does not identify a `D(S3)` ribbon word whose monodromy realizes
the joint projector phase, or prove that a coherent charge-extraction circuit
can be implemented and uncomputed on the lattice. It replaces the broad
controllability gap with one sharply typed coupling target.

## Exact factorization of the incidence isometry

Let the two charged qutrit routes be unitary maps `R,S` with common typed
endpoints. Define their relative holonomy

\[
H=R^*S.
\]

The desired encoding isometry is

\[
J|\psi\rangle
=
\frac1{\sqrt2}
\left(
R|\psi\rangle\otimes|0_F\rangle
+
S|\psi\rangle\otimes|1_F\rangle
\right).
\]

Prepare the fusion qubit in

\[
|+_F\rangle
=
\frac{|0_F\rangle+|1_F\rangle}{\sqrt2}.
\]

Define the controlled relative holonomy

\[
C_H
=
I\otimes|0_F\rangle\langle0_F|
+
H\otimes|1_F\rangle\langle1_F|.
\]

Then

\[
J
=
(R\otimes I)C_H(I\otimes|+_F\rangle).
\]

Thus preparation of the already identified `A_F` fusion state, followed by
one controlled relative holonomy and the common route `R`, gives exactly `J`.

## Vacuum-projector specialization

For the phase-halving constructor,

\[
H
=
\exp(2\pi iP_A/3)
=
I+(\omega-1)P_A.
\]

Let

\[
P_0=|0_F\rangle\langle0_F|,
\qquad
P_1=|1_F\rangle\langle1_F|.
\]

Substitution gives

\[
C_H
=
I\otimes P_0
+
\left(I+(\omega-1)P_A\right)\otimes P_1
\]

and therefore

\[
C_H
=
I+(\omega-1)\Pi,
\qquad
\Pi=P_A\otimes P_1.
\]

Since `Pi` is a projector,

\[
C_H=\exp(2\pi i\Pi/3).
\]

Both factors have rank one, so `Pi` has rank one on the six-dimensional joint
workspace. The missing incidence is the smallest nontrivial selective phase
possible there.

## Separate-constructor no-go theorem

Suppose every admitted coherent generator acts either on the qutrit alone or
on the fusion qubit alone. Their generated unitary group consists of product
unitaries

\[
U_L\otimes U_F.
\]

Every such unitary has operator-Schmidt rank one across the logical--fusion
cut and maps every product state to a product state.

The controlled phase has the decomposition

\[
C_H
=
I\otimes I
+
(\omega-1)P_A\otimes P_1.
\]

Because `P_A` is not scalar and `P_1` is neither zero nor identity, the two
product terms are linearly independent. Hence

\[
\operatorname{OSR}(C_H)=2.
\]

Therefore no composition of separate qutrit and fusion unitaries realizes
`C_H`. One joint constructor is necessary.

The same conclusion holds for deterministic protocols using only separate
local operations and classical communication: they cannot create entanglement
from a product input, while `C_H` does.

## Exact one-state coupling witness

Choose normalized qutrit states

\[
|a\rangle\in\operatorname{im}P_A,
\qquad
|b\rangle\in\ker P_A.
\]

Prepare

\[
|\Psi_{in}\rangle
=
\frac{|a\rangle+|b\rangle}{\sqrt2}
\otimes
\frac{|0_F\rangle+|1_F\rangle}{\sqrt2}.
\]

In the two-by-two subspace with qutrit rows `a,b` and fusion columns `0,1`,
the output coefficient matrix is

\[
M_{out}
=
\frac12
\begin{pmatrix}
1&\omega\\
1&1
\end{pmatrix}.
\]

Its determinant is

\[
\det M_{out}=\frac{1-\omega}{4},
\]

which is nonzero. The output is entangled and has Schmidt-rank two.

The squared Schmidt coefficients are exactly

\[
\frac34,
\qquad
\frac14.
\]

Indeed, the reduced density matrix has trace one and determinant `3/16`.
This product input is therefore a compact exact witness that a joint
constructor acted. No product-unitary model reproduces it.

The witness is necessary evidence for coupling but not full process
tomography: another entangling operation could produce the same Schmidt
spectrum.

## General phase-angle witness

For a candidate phase

\[
C(\varphi)
=
I+(e^{i\varphi}-1)\Pi,
\]

the same product probe has concurrence

\[
\mathcal C(\varphi)
=
\left|\sin\frac{\varphi}{2}\right|.
\]

At the intended angle `2 pi/3`, this is

\[
\mathcal C=\frac{\sqrt3}{2}.
\]

Thus a coherent angle error is visible in one invariant entanglement
coordinate, although the sign of the angle is not: conjugate phases have the
same concurrence. An oriented interference probe is still required to
distinguish `omega` from its conjugate.

## Why measuring the two predicates is not the gate

One can measure `P_A` and `P_1`, compute their classical conjunction, and
apply a conditional phase. That procedure records which joint sector was
occupied. For an unknown superposition, it dephases exactly the coherence the
controlled unitary must preserve.

A valid measurement-mediated implementation must instead:

1. extract both predicates coherently into an ancillary workspace;
2. apply the cube-root phase to their logical conjunction;
3. uncompute the extracted predicate values;
4. return the ancilla and every charge reference to one fixed state.

The conjunction phase or its equivalent joint monodromy is still a genuine
coupling resource. Classical feed-forward cannot manufacture it without
having first destroyed coherence.

## Candidate topological form

The preferred microscopic realization is a closed ribbon or probe history
whose action is

\[
W
=
I+(\omega-1)P_A\otimes P_1
\]

on the joint protected space and scalar on every persistent ancillary port.

This asks for a topological probe that sees the conjunction of:

- vacuum fusion of the selected qutrit pair;
- the `D_2` rather than `D_1` channel of the orientation fusion qubit.

A probe that sees only one predicate factors through a marginal charge
readout and cannot implement the required selective joint phase. The
microscopic search should therefore be over linked ribbon histories or
coherently uncomputed joint charge extraction, not over another scalar Wilson
loop on either subsystem alone.

## Algebraic presence versus physical execution

The joint projector belongs to the abstract tensor-product endpoint algebra
once both local projectors are admitted:

\[
P_A\otimes P_1
\in
\operatorname{End}(H_L\otimes H_F).
\]

That establishes algebraic addressability. It does not establish that the
Hamiltonian, braid group, or measurement instrument can exponentiate this
product projector.

This is the same constructor boundary encountered throughout the programme:
an element may exist in the completed algebra while no admitted source
operation realizes it.

## Fault classes

### Missing incidence

Replace `C_H` by a product unitary. The qutrit and fusion systems never become
entangled, and the one-state witness has Schmidt rank one.

### Wrong angle

Implement `C(phi)` with the correct joint projector but an incorrect phase.
The operation remains unitary and joint, but the later LCU branch generally
fails the exact reversible-branch equation.

### Wrong joint projector

Phase `P_B` or a larger qutrit subspace instead of `P_A`, or phase both fusion
channels. The operation may remain entangling while coupling the wrong typed
sectors.

### Predicate record leakage

The coherent extractor leaves either predicate in an environment or
controller. Tracing it out turns the joint phase into dephasing and raises the
branch Choi rank.

### Common orientation conjugation

Conjugate `omega`, the bridge holonomy, fusion monodromy, and every internal
probe together. The complete constructor remains coherent and implements the
conjugate universal gate alphabet. Only an independently anchored orientation
test distinguishes it.

## Exact falsifiers

- `J` is treated as an irreducible arbitrary six-dimensional unitary rather
  than the displayed controlled-holonomy factorization.
- Separate qutrit and fusion operations are claimed to generate an
  operator-Schmidt-rank-two gate.
- The product projector is exponentiated by separately exponentiating its two
  factors.
- Classical measurement of both predicates is called coherent control.
- Entanglement generation is inferred from correlated classical outcomes.
- The one-state Schmidt spectrum is promoted to full process certification.
- The correct angle is applied to the wrong joint sector.
- A joint charge record is discarded before uncomputation.
- Algebraic membership of `P_A` times `P_1` is treated as physical authority
  to implement its exponential.

## Shared Carrier geometry and quantum coefficient lens

Shared Carrier geometry supplies joint incidence, marginal versus conjunctive
predicates, preparation--control--uncomputation, record leakage, and the
distinction between algebraic addressability and executable coupling.

The quantum coefficient lens supplies controlled holonomy, product
projectors, operator-Schmidt rank, entanglement witnesses, concurrence,
Kraus dephasing, and oriented phase conjugation.

## Disposition

The last broad bridge-controllability gap reduces to one rank-one joint phase:

\[
C_H=I+(\omega-1)P_A\otimes P_1.
\]

Preparing the fusion qubit in its intrinsic `A_F` superposition and applying
this phase gives the entire route-incidence isometry after the common route
`R`. Product constructor families cannot realize it, and one exact product
probe witnesses the required coupling through Schmidt spectrum `3/4,1/4`.

The next microscopic search is correspondingly narrow: find one linked ribbon
or coherently uncomputed charge-extraction process whose protected action is
the exponential of `P_A` times `P_1`, with no persistent predicate record.

No build, checker, or Git operation was run for this research-only packet.
