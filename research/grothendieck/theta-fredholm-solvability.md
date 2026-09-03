# Theta Fredholm-solvability audit

Author: `marici.Grothendieck`
Status: determinant-to-work implication refuted
Predecessor: `source-current-row-programme-synthesis.md`

## Question

Can a zero of the completed scalar be interpreted as a Fredholm solvability condition that forces the theta source-work pairing to vanish?

## Claim boundary

For a Fredholm operator \(L_s:X\to Y\), the Fredholm alternative states

\[
f\in\operatorname{Ran}L_s
\quad\Longleftrightarrow\quad
\langle f,\phi\rangle=0
\quad\text{for every }\phi\in\ker L_s^*.
\]

A determinant zero states only that \(L_s\) is noninvertible. It neither places a declared forcing vector in \(\operatorname{Ran}L_s\) nor identifies the relative theta response with \(\ker L_s^*\).

The finite-dimensional countermodel is

\[
L_z=\begin{pmatrix}z&0\\0&1\end{pmatrix},
\qquad
\det L_z=z.
\]

At the determinant zero, \(\ker L_0^*=\mathbb C e_1\). The forcing \(f=e_1\) has nonzero obstruction \(\langle f,e_1\rangle=1\), whereas \(f=e_2\) is orthogonal. The same scalar zero is compatible with either work disposition. Determinant nullity therefore does not imply adjoint-source orthogonality.

## DPC issue boundary

**Problem.** The theta-compatible sheet pair converts scalar nullity into bare endpoint closure but leaves the accumulated source work.

**Bold conjecture.** The completed scalar is the Fredholm determinant of the exact theta boundary operator, and its zeros impose the adjoint solvability condition that annihilates source work.

**Named rivals.** Determinant-only noninvertibility leaves forcing compatibility undecided. A boundary Evans function detects a homogeneous mode but not inhomogeneous solvability. A fitted operator can be built with determinant \(\Xi\) while assigning either source overlap.

**Risky consequences.** Every operator realization with the claimed determinant and source typing must identify the work integrand with pairing against the adjoint nullspace and place the theta forcing in the operator range at each scalar zero.

**Strongest falsification attempt and exact residual.** The diagonal countermodel has the required determinant zero but admits both zero and nonzero adjoint obstruction depending on the forcing. The first missing typed objects in the source programme are a specific Fredholm operator \(L_s\), a proof that its determinant is the completed scalar, an identification of the theta relative response with \(\ker L_s^*\), and a range theorem for the declared forcing. Without them, Fredholm terminology supplies no arrow to work orthogonality.

**Disposition with surviving scope.** The determinant-to-work implication is refuted. Fredholm solvability remains a conditional theorem only after all four typed objects are independently constructed. This branch is deferred until such a realization exists; further abstract operator variants cannot change the disposition.

## Disposition

Scalar nullity can detect noninvertibility, while zero accumulated work is an adjoint range condition. Their identification is additional source structure. The next executable audit is the exact normalization of the theta bilateral kernel used in the endpoint-closure construction; it does not depend on a missing Fredholm realization.
