# Gauss–Manin stability selects one active relative parity minor

## Question

Of the two nondegenerate active-boundary minors of the published intersection matrix, which one defines subspaces preserved by the displayed dual and canonical Gauss–Manin connections?

## Claim boundary

This is a source-matrix subconnection result in the worked relative-cohomology example. It does not identify that example with the conductor geometry or establish an integral lattice.

## Dual active subspace

In dual basis order

\[
(\check\varphi_1,\check\varphi_2,\check\varphi_3,\check\varphi_4)
=(S_3,S_{12},S_{23},S_{13}),
\]

the displayed dual connection has zero pattern

\[
\check A=
\begin{pmatrix}
*&0&*&*\\
0&*&0&0\\
0&0&*&0\\
0&0&0&*
\end{pmatrix}.
\]

With the source convention

\[
\check\nabla\check\varphi_a=\check A_{ab}\wedge\check\varphi_b,
\]

the active subspace

\[
\check V_{\rm act}=\langle\check\varphi_1,\check\varphi_3,\check\varphi_4\rangle
\]

is preserved: its rows have no component along \(\check\varphi_2\). The inactive \(S_{12}\) line is separately preserved.

## Canonical connection candidates

The canonical connection has generic zero pattern

\[
A_\vartheta=
\begin{pmatrix}
*&*&*&0\\
0&*&*&*\\
0&*&*&*\\
0&*&*&*
\end{pmatrix}.
\]

The candidate obtained by omitting canonical column 1 retains

\[
V_{\widehat1}=\langle\vartheta_2,\vartheta_3,\vartheta_4\rangle.
\]

Rows 2–4 have zero first column, so this subspace is preserved.

The other nondegenerate candidate omits column 4 and retains

\[
V_{\widehat4}=\langle\vartheta_1,\vartheta_2,\vartheta_3\rangle.
\]

Rows 2 and 3 have generically nonzero fourth-column entries, so this subspace is not preserved. Its leakage forms are

\[
d\log\frac{X_2+Y}{X_1+X_2},
\qquad
d\log\frac{X_1+X_2}{X_1+Y}.
\]

## Selected restricted pairing

Gauss–Manin stability therefore selects

\[
C_{\widehat1}=
\begin{pmatrix}
-1&1&0\\
1&0&1\\
0&1&-1
\end{pmatrix}

town

det C_{\widehat1}=2,
\qquad
\operatorname{Smith}(C_{\widehat1})=(1,1,2).
\]

It pairs the active dual subconnection \((S_3,S_{23},S_{13})\) with the canonical subconnection \((\vartheta_2,\vartheta_3,\vartheta_4)\).

## Consequence for the conductor conjecture

The source now supplies one specific three-dimensional connection-stable pairing of the exact arithmetic type required by an elementary conductor factor. The earlier column-4 candidate is rejected by generic connection leakage.

Still missing is a source-derived parameter and basis map carrying this selected pairing and connection to \((J_i,A_{(i)})\). Equality of dimension, determinant, and zero-pattern role does not construct that comparison.

## Disposition

The candidate fiber has collapsed from two minors to one connection-stable relative pairing. Its transport to either conductor wall remains unconstructed.
