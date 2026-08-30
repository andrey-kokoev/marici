# 1629 — The Mixed Fourth Cumulant Requires a Canonical Quantum Gram Companion

## Objective

Construct the smallest quantum phase-space positivity object that contains the two fourth moments entering Entry 1627's residual and retains the canonical commutator before taking an associated grade.

## Operator basis

Scale the canonical pair by

\[
[Q,P]=2i
\]

and define

\[
S=\frac{QP+PQ}{2}.
\]

Use the operator column

\[
\mathcal O=(1,Q^2,S)^T.
\]

For every positive density matrix, its Gram object

\[
M=\langle\mathcal O^\dagger\mathcal O\rangle
\]

is positive semidefinite.

## Exact commutator entry

The canonical relation gives

\[
[Q^2,S]=4iQ^2.
\]

Writing

\[
Q_2=\langle Q^2\rangle,
\quad
R=\langle S\rangle,
\quad
U=\langle Q^4\rangle,
\quad
Z=\operatorname{Re}\langle Q^2S\rangle,
\quad
W=\langle S^2\rangle,
\]

the Gram matrix is

\[
\boxed{
M=
\begin{pmatrix}
1&Q_2&R\\
Q_2&U&Z+2iQ_2\\
R&Z-2iQ_2&W
\end{pmatrix}
\succeq0.
}
\]

The imaginary entry is forced; omitting it would forget the quantum normal direction.

## Determinant inequality

The Schur complement gives

\[
\boxed{
\operatorname{Var}(Q^2)\operatorname{Var}(S)
\geq
\operatorname{Cov}(Q^2,S)^2+4Q_2^2.
}
\]

The real mixed entry \(Z\) contains the Weyl-ordered \(pqqq\) fourth moment needed by Entry 1627.  It is controlled only together with \(W=\langle S^2\rangle\).

## Finite unboundedness test

At the fixed lower data

\[
Q_2=1,
\qquad
R=0,
\qquad
U=2,
\]

every real \(Z\) lies on the determinant boundary after choosing

\[
W=Z^2+4.
\]

The checker verifies 5,670 positive-semidefinite integer packets and 201 such unbounded mixed-moment witnesses.

## Narrow result

\[
\boxed{
\text{The mixed fourth cumulant is not dynamically controlled by covariance and }Q^4\text{ alone; the canonical companion }\langle S^2\rangle\text{ is mandatory.}
}
\]

Positive semidefiniteness of this truncated Gram object is necessary, not sufficient, for extension to a full quantum state.

## Architectural consequence

The coefficient object is intrinsically multi-grade and noncommutative:

- the fourth-cumulant coordinate;
- its companion fourth moment;
- the commutator-fixed imaginary extension;
- the lower covariance block.

Projecting to \(\kappa_{pqqq}\) alone destroys the positivity constraint.  This is coefficient complexity over the existing labelled carrier, not evidence for a new carrier cell.

## Durable artifacts

- `research/benincasa/checkers/quantum_fourth_moment_gram.rs`
- `research/benincasa/results/quantum-fourth-moment-gram.json`
- `research/benincasa/quantum-fourth-moment-gram.md`

## Next falsifier

Test extension of this \(3\times3\) Gram packet to the full degree-four Weyl moment matrix with basis

\[
(1,Q,P,Q^2,S,P^2).
\]

Compute whether the Entry 1627 residual functional remains unbounded on fixed covariance fibers after all degree-four commutator and positivity constraints are imposed.  If it does, degree-six/eight moments are required; if bounded, derive the sharp bound without fitting.
