# Joint compatibility can preserve the entire prediction set

## Question

Operator request: “attempt to faalsify it”. The preceding working conjecture
was: requiring geometry, dynamics, matter and measurement to share compatible
structures will restrict their free choices and produce a testable relation
among observables.

SCC obligations: forward realization, route compatibility and attachment
transport on one fixed labelled carrier. Freeze the executable claim as:
adding the joint structures specified below strictly reduces the prediction
set of the existing retained-unitary Tick annotation class.

A pair of different predictions alone cannot disprove an existential claim
about some other shared observable relation. The stronger attack constructs
a prediction-preserving completion for every member of the original class.

## Source and claim boundary

Use `tick-unitary-image-nonuniqueness.md` and its checked native-square source.
Retain the labelled complex carrier V=C^2 tensor C^2, counting inner product,
source flips L,R, commuting nonnegative Hermitian generators H_L,H_R, source
corners at angle pi, factor interchange and reflected-square law. The full
native Tick remains the structural component of each annotation. Its dependent
return section has no analytic interpretation supplied by this construction.

The joint requirements are:

- the same real state geometry for every member of the class;
- Hamiltonian generation and unitary dynamics on that geometry;
- the same two labelled state factors and preparations;
- fixed tensor-Pauli measurement effects with Born pairing;
- commuting state/effect transport and preservation of the geometry.

The matter component is the existing two-factor state model. Physical particle
species, masses, the six-port position chart, continuum spacetime and gravity
remain outside this class. The complex linearization, exponential enlargement
and Born pairing are inputs. Group parameters are dimensionless. The test uses
exact synthetic records and requires no apparatus-admission decision.

## Conjecture, rivals and risky consequence

The strict-selection conjecture predicts that these joint requirements reject
at least one original prediction law. Rivals attribute selection to the shared
metric, the Hamiltonian condition, or fixed observer transport. A fourth rival
attributes all remaining differences to parameter or phase conventions.

The counterproposal is that the completion is available for every original
annotation and preserves every fixed-protocol record. Its risky consequence is
a section of the forgetful map, with unchanged observables. A failed generic
matrix identity or a source-attachment failure would defeat this construction.

## Generic completion

Write psi=x+i y, xi=(x,y), and let R(T) denote realification:

\[
R(T)=\begin{pmatrix}\Re T&-\Im T\\\Im T&\Re T\end{pmatrix},\qquad
J=\begin{pmatrix}0&I\\-I&0\end{pmatrix}.
\]

Fix g=2I and the symplectic matrix Omega=2J. For any Hermitian H define

\[
h_H(\psi)=\psi^\dagger H\psi=\xi^T R(H)\xi,
\qquad A_H=J R(H)=R(-iH).
\]

Hermiticity gives R(H)^T=R(H) and [J,R(H)]=0. Hence

\[
-\Omega A_H=2R(H),\qquad
A_H^T g+gA_H=0,\qquad
A_H^T\Omega+\Omega A_H=0.
\]

The first identity is i_X Omega=d h_H; the other two preserve the same metric
and symplectic form. The finite-dimensional exponential gives the complete
flow exp(-i a H), preserving normalization and phase equivalence. It descends
to normalized rays with their induced projective geometry.

For every Hermitian effect E,

\[
A_H^T R(E)+R(E)A_H=R\bigl(i[H,E]\bigr).
\]

Thus state transport and Heisenberg effect transport give the same record.
The finite transport identity is

\[
\langle U\psi,E U\psi\rangle
=\langle\psi,U^\dagger E U\psi\rangle.
\]

Apply this construction to both generators. Their commutation, source corners,
interchange and return identities are inherited unchanged. The matrix
exponential converges in finite-dimensional operator norm for every finite
parameter; the universal statement uses these identities and the exponential
law, independently of the finite regression grid.

Let D be the original annotation class and C the class with these joint data.
The construction s:D->C and forgetful map p:C->D obey p s=id_D. Every preparation,
effect and unitary is preserved. Conversely each completed record is the Born
record of its underlying annotation. Therefore the full prediction sets satisfy

\[
\mathcal P(C)=\mathcal P(D).
\]

The added compatibility conditions contribute zero additional restrictions on
these observable laws. The original source restrictions remain present.

## Existing rival through the entire completion

Set P_L=(I-L)/2 and P_R=(I-R)/2. Keep the existing two choices

\[
H_{L,k}=P_L+kP_LP_R,\qquad
H_{R,k}=P_R+kP_LP_R,\qquad k\in\{0,2\}.
\]

Both receive the same geometry and fixed readout. For preparation 00 and
(a,b)=(pi/3,0), the predecessor gives these full computational-basis records:

| k | p(00) | p(01) | p(10) | p(11) |
|---|---|---|---|---|
| 0 | 3/4 | 0 | 1/4 | 0 |
| 2 | 3/16 | 3/16 | 7/16 | 3/16 |

The second-factor record 1 has probabilities 0 and 3/8. The squared amplitude
determinant is respectively 0 and 3/16. Every baseline state from a basis
preparation has determinant zero for all parameter pairs, so phase and
parameter changes leave the distinction intact. The checker retains all nine
joint Pauli settings and reconstructs the complete density matrix.

## Falsification controls and disposition rule

Reject deliberate sign errors in Hamiltonian and observer transport, a
mismatched symplectic form, a non-Hermitian generator, and an odd mixed
coefficient violating the source corner. Record the exact nonzero residuals.
Also test intermediate tensor locality: k=2 violates it. That independently
specified additional restriction would reduce the source class.

The checker is `checkers/check_joint_compatibility_free_completion.py`; its
receipt is `results/joint-compatibility-free-completion.json`. A zero exit under
the frozen challenge means the strict added-selection claim is falsified in
this completion class. The tested disposition is recorded separately in
`joint-compatibility-free-completion-result.md` to keep this preregistration
and its hashes unchanged.

This attack distinguishes compatibility from an additional selector through
an exact prediction-set equality. Applying a stronger cross-topic conjecture
requires naming its shared maps and added equations. Those maps between the
current ten research branches have yet to be constructed.
