# Intersection Becomes Commutation Only Through the Quantum Bicharacter

Let \(\Sigma_g\) be a closed oriented surface. Carrier geometry supplies the
integral intersection pairing

\[
I:H_1(\Sigma_g;\mathbf Z)
\times H_1(\Sigma_g;\mathbf Z)
\longrightarrow\mathbf Z.
\]

In a symplectic basis

\[
(a_1,b_1,\ldots,a_g,b_g),
\]

its matrix is

\[
J_g=
\bigoplus_{j=1}^g
\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]

This pairing is unimodular and topological. By itself it is not an operator
commutation law.

Let the untwisted abelian quantum coefficient group be a finite abelian group
(A), with character group

\[
\widehat A=\operatorname{Hom}(A,U(1)).
\]

The perfect evaluation bicharacter

\[
\langle\chi,a\rangle=\chi(a)
\]

turns geometric intersection into the electric--magnetic Weyl relation

\[
E_\chi(\eta)M_a(\gamma)
=
\chi(a)^{I(\eta,\gamma)}
M_a(\gamma)E_\chi(\eta).
\]

The exponent comes from shared Carrier geometry. The phase
(\chi(a)), and hence whether the operators commute, anticommute, or acquire a
higher root of unity, comes from the quantum coefficient lens.

## Qubit toric code

For

\[
A=\mathbf Z_2,
\]

the nontrivial character satisfies

\[
\chi(1)=-1.
\]

A single transverse crossing has (I=1), hence

\[
EM=-ME.
\]

Disjoint or homologically parallel representatives have zero intersection and
commute. This recovers Pauli anticommutation from operator coefficients and
intersection together, rather than declaring it from a diagram.

For (A=\mathbf Z_n), the standard character gives

\[
\chi(1)=e^{2\pi i/n},
\]

so one crossing yields the clock--shift relation. Anticommutation is the
special (n=2) case.

## Nondegeneracy

The surface intersection form is unimodular, and the evaluation pairing

\[
\widehat A\times A\to U(1)
\]

is perfect. Their product therefore gives a nondegenerate logical commutation
pairing between electric and magnetic homology labels. Every nontrivial
magnetic logical class is detected by some electric loop, and conversely.

This is stronger than syndrome faithfulness. Local star and plaquette
syndromes detect endpoints and curvature but vanish on closed
noncontractible loops. The logical commutation pairing detects their global
class.

## Port counts

For one flat (A)-valued sector on \(\Sigma_g\), the logical label space is
modeled by

\[
H^1(\Sigma_g;A)\simeq A^{2g}
\]

for constant finite coefficients. A symplectic set of (2g) loop probes,
with a character family separating (A), is jointly faithful on that one
sector modulo local repairs.

The full untwisted logical operator algebra has both magnetic and electric
generators:

\[
2g\text{ magnetic generators}
\quad+\quad
2g\text{ electric generators}.
\]

They are not one jointly commuting classical readout. Crossing electric and
magnetic generators obey the Weyl relation above. Thus:

- (2g) commuting coordinates can label one logical sector;
- (4g) elementary generators present the full electric--magnetic algebra;
- simultaneous physical measurement of all generators is obstructed by their
  coefficient-dependent commutation.

On the torus, (g=1): two loop probes recover one \(A^2\) sector, while four
elementary logical loop operators generate the paired algebra.

## Shared Carrier versus quantum lens

Shared Carrier geometry supplies:

- the chain condition;
- local boundary and coboundary incidence;
- homology and cohomology classes;
- oriented intersection number;
- the symplectic rank (2g).

The quantum coefficient lens supplies:

- the electric character group and magnetic coefficient group;
- the evaluation bicharacter;
- concrete clock/shift or Pauli operators;
- the resulting Weyl phase and measurement incompatibility.

Physical implementation remains a third layer: possessing the logical Weyl
algebra does not construct fault-tolerant loop actuators or measurements.

## Falsifiers

- Inferring anticommutation from intersection without a coefficient
  bicharacter.
- Calling every nonzero intersection phase (-1) for (A\ne\mathbf Z_2).
- Counting four torus logical generators as four simultaneously commuting
  classical bits.
- Using local syndrome to choose a preferred representative of a homology
  class.
- Treating abstract Weyl generators as executable fault-tolerant controls.
- Importing the quantum bicharacter into a nonquantum coefficient sector.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
10/10. The aim was to reattach operator anticommutation to the recovered
Carrier cohomology without conflating their authority.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Intersection supplies the exponent, the coefficient bicharacter
supplies the phase, and physical control remains a separate compiler problem.
