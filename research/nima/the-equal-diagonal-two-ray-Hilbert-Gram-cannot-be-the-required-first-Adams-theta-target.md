# The equal-diagonal two-ray Hilbert Gram cannot be the required first-Adams theta target

## Required target

Write the Stieltjes endpoint Gram as

\[
G_{\rm St}=
\begin{pmatrix}
a&u+iv\\
u-iv&b
\end{pmatrix}.
\]

For the fixed comparison

\[
Q=
\begin{pmatrix}
\frac12&\frac14\\
\frac12&-\frac14
\end{pmatrix},
\]

the unique required theta target is

\[
G_\theta^{\rm req}
=
\begin{pmatrix}
a+4b+4u&a-4b-4iv\\
a-4b+4iv&a+4b-4u
\end{pmatrix}.
\]

Its diagonal difference is

\[
(G_\theta^{\rm req})_{11}-(G_\theta^{\rm req})_{22}=8u.
\]

## Source sign

The Stieltjes windows `W_L` and `W_(2L)` have the same strict sign on the
nontrivial source support. Hence their real cross-pairing is positive:

\[
u=\operatorname{Re}\langle W_L,W_{2L}\rangle_{\rm St}>0.
\]

Therefore the required target has unequal diagonal entries:

\[
(G_\theta^{\rm req})_{11}>(G_\theta^{\rm req})_{22}.
\]

## Comparison with the available four-grade Hilbert Gram

The exact ordinary two-ray four-grade Gram has the reciprocal form

\[
G_{\rm Hilb}^{\rm ray}
=
\begin{pmatrix}
D&C\\
C&D
\end{pmatrix}.
\]

Its diagonal entries are equal. It can coincide with
`G_theta^req` only if `u=0`, contradicting the strict same-sign Stieltjes
cross-pairing.

Thus the already computed ordinary four-grade Hilbert table is not merely
incomplete as evidence. It is structurally the wrong target metric for the
first Adams comparison.

## Required correction

The completed relative Green construction must introduce a diagonal
polarization of exact size

\[
8u.
\]

This contribution must come from the wall, tail/PV, relative extension, or
radical/Schur structure absent from the ordinary two-ray Hilbert Gram. The
fourth Gaussian grade alone cannot repair the mismatch while reciprocal ray
norms remain equal.

## Finite falsifier

Any proposed target calculation that preserves equal ray diagonals fails the
first Adams matrix-unit test before off-diagonal or completion analysis. The
first executable check on a candidate target table is therefore

\[
H_{11}-H_{22}=8\operatorname{Re}
\langle W_L,W_{2L}\rangle_{\rm St}.
\]