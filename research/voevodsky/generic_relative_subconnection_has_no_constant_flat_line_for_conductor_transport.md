# The generic relative subconnection has no constant flat line for conductor transport

## Question

Can the explicit integral equivalence between the selected relative pairing and \(J_1\) also intertwine the generic relative Gauss–Manin connection with the conductor connection by a constant integral basis change?

## Claim boundary

This tests constant integral transport over the generic relative parameter space. It does not exclude a parameter-dependent gauge or a specialization that identifies or removes divisors.

## Relative divisor residues

For the selected canonical subconnection on

\[
(\vartheta_2,\vartheta_3,\vartheta_4),
\]

expand the displayed logarithmic connection against the five irreducible linear factors

\[
A=X_1+Y,
\quad B=X_1-Y,
\quad C=X_2+Y,
\quad D=X_2-Y,
\quad E=X_1+X_2.
\]

Ignoring the common scalar \(\varepsilon\), the residue matrices are

\[
R_A=
\begin{pmatrix}0&0&0\\1&0&-1\\-1&0&1\end{pmatrix},
\quad
R_B=
\begin{pmatrix}1&0&0\\0&0&0\\1&0&0\end{pmatrix},
\]

\[
R_C=
\begin{pmatrix}0&1&1\\0&0&0\\0&1&1\end{pmatrix},
\quad
R_D=
\begin{pmatrix}0&0&0\\0&1&0\\0&-1&0\end{pmatrix},
\]

\[
R_E=
\begin{pmatrix}1&-1&-1\\-1&1&1\\0&0&0\end{pmatrix}.
\]

The vertically stacked residue matrix has rank three. Hence

\[
\bigcap_{L\in\{A,B,C,D,E\}}\ker R_L=0.
\]

There is no nonzero constant vector flat around all five generic divisors.

## Conductor obstruction

Every wallwise intermediate conductor connection has a constant flat generator. For example,

\[
A_{(2)}=
\begin{pmatrix}
a_1&0&a_1/2\\
0&a_2&0\\
0&0&0
\end{pmatrix}
\]

has the constant common right-kernel vector \((-1,0,2)^T\): the \(a_1\) residue sends it to zero and the \(a_2\) residue does likewise. Equivalently, its residue representation contains a common trivial one-dimensional summand, which becomes the third coordinate line in the enhanced frame. A constant gauge preserves the dimension of the common residue kernel.

The generic selected relative subconnection has no such summand. Therefore the unimodular matrices \(U,V\) carrying its pairing to \(J_1\) cannot, by themselves, produce a generic constant-gauge connection isomorphism.

## Consequence

Any successful conductor comparison must use at least one additional operation:

1. specialize the relative parameter arrangement so divisor residues become dependent or disappear;
2. take a source-derived subquotient rather than the full selected subconnection;
3. allow a parameter-dependent gauge and separately prove its integral normalization.

The total-energy identity between conductor discriminants and the relative Kummer radicand is only a scalar parameter coincidence until it supplies one of these operations.

## Disposition

The integral pairing equivalence survives, but generic connection transport by constant integral bases is obstructed by the absence of a common flat line. The next admissible target is an explicit support-arrangement specialization, not another constant lattice basis search.
