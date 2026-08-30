# Reciprocal doubling makes the spectral generator Hamiltonian but still indefinite

## Frozen finite calculation

Center the seam parameter as

\[
s=\frac12+z.
\]

For the positive-orientation tail equation, the \(z\)-coefficient of the generator is \(-1\) on the tail coordinate. Under reciprocal reflection \(s\mapsto1-s=\frac12-z\), the opposite tail carries coefficient \(+1\).

Ignoring the affine forcing and constant channels for this spectral-symbol calculation, the doubled tail plane therefore has

\[
A_1=
\begin{pmatrix}
-1&0\\
0&1
\end{pmatrix}.
\]

With the standard source-oriented symplectic matrix

\[
J=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix},
\]

one has

\[
A_1^{*}J+JA_1=0.
\]

Thus reciprocal doubling repairs the first defect: the spectral coefficient is Hamiltonian.

But the canonical Hamiltonian extracted from \(A_1=-JH\) is

\[
H=JA_1=
\begin{pmatrix}
0&-1\\
-1&0
\end{pmatrix}.
\]

Its eigenvalues are \(+1\) and \(-1\). It is Hermitian but indefinite.

## Consequence

Reciprocal doubling alone cannot produce the positive canonical system needed for the Hermite–Biehler argument. It converts the one-sided non-Hamiltonian spectral action into a legitimate Krein-space Hamiltonian pencil, but not into a Hilbert-positive one.

This is valuable because it locates the exact role of the omitted channels. The wall, square, and archimedean energies must do more than restore endpoint bookkeeping: after adjoining and reducing them, their Schur contribution must convert the reciprocal off-diagonal form into a positive semidefinite Hamiltonian on the reachable zero-trace quotient.

## Signature obstruction

The signature cannot be changed by an invertible congruence on the same doubled tail plane. Therefore no bounded source change of coordinates confined to these two tail coordinates can turn this \(H\) positive.

There are only three legitimate exits:

1. enlarge the state by the missing positive channels and take a source-authorized Schur reduction;
2. quotient a declared radical after enlargement;
3. retain an indefinite canonical/Krein system and prove a stronger definitizability theorem instead of invoking de Branges positivity.

A fitted \(J\)-unitary gauge on the two-dimensional tail plane does not solve the signature problem.

## Next finite matrix

Let the complete finite-cell Hamiltonian be written

\[
\mathcal H=
\begin{pmatrix}
H_{\mathrm{tail}}&C\\
C^{*}&D
\end{pmatrix},
\qquad
H_{\mathrm{tail}}=
\begin{pmatrix}
0&-1\\
-1&0
\end{pmatrix},
\]

where \(D\) contains the independently derived wall, square, and archimedean energies. If \(D\) is positive on reduced support, the effective tail Hamiltonian is

\[
H_{\mathrm{eff}}
=
H_{\mathrm{tail}}-CD^{\dagger}C^{*}
\]

for the displayed block convention.

Since subtracting a positive Schur return cannot repair a negative direction, this convention itself signals that either:

- the tail block sign/order is different in the complete Green form;
- the positive tail system is obtained by eliminating the tail variables rather than the auxiliary variables;
- or the complete object remains indefinite.

The precise block orientation must therefore be derived before any positivity claim.

## Reduced frontier

The first finite pilot should output the complete doubled Green matrix and identify which block is eliminated. The signature of every candidate Schur complement is then a cheap decisive test. Reciprocal symmetry supplies Hamiltonianity; positivity must come from the full boundary architecture and the correct reduction direction.
