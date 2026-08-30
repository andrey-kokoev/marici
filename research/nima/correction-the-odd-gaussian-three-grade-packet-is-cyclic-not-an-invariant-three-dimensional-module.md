# Correction: the odd Gaussian three-grade packet is cyclic, not an invariant three-dimensional module

## Exact calculation

Let
\[
A=x\partial_x,\qquad X=\pi x^2,\qquad
b_k=xX^k e^{-X}\quad(k\ge0).
\]
Then
\[
A b_k=(2k+1)b_k-2b_{k+1}.
\]
For the shifted completion polynomial
\[
P_-(A)=(A-1)A,
\]
one obtains
\[
P_-(A)b_k
=
2k(2k+1)b_k-(8k+6)b_{k+1}+4b_{k+2}.
\]

In particular,
\[
P_-(A)b_0=-6b_1+4b_2,
\]
but
\[
P_-(A)b_1=6b_1-14b_2+4b_3,
\]
and
\[
P_-(A)b_2=20b_2-22b_3+4b_4.
\]

Therefore
\[
\operatorname{span}\{b_0,b_1,b_2\}
\]
is not invariant under \(P_-(A)\). There is no exact \(3\times3\) endomorphism
of this odd Gaussian space unless an additional quotient, projection, or jet
truncation is declared.

## What remains exactly three-grade

The source connection vector is
\[
D_xf_0=-2\pi b_0.
\]
Its single completed image is
\[
P(A)D_xf_0
=
D_xP(A-1)f_0
=
-4\pi b_0+20\pi b_1-8\pi b_2.
\]
Thus one application of theta completion to the cyclic connection vector lands
in the three odd grades \(b_0,b_1,b_2\). This is an exact three-coordinate
output statement.

It is not an invariant three-dimensional Jordan representation. Iterating the
completion polynomial generates higher odd grades.

## Consequence for the Adams comparison

The finite local comparison may legitimately use the cyclic column
\[
(-4,20,-8)^\mathsf T
\]
up to the common factor \(\pi\) and the frozen normalization. It may not use a
fitted \(3\times3\) odd Jordan matrix as though the three-grade target were
closed under completion.

There are only three authorized alternatives:

1. treat the odd packet as a one-step cyclic output;
2. retain the full odd Gaussian polynomial tower;
3. derive a source quotient whose kernel is invariant under \(P_-(A)\).

A naive truncation that drops \(b_3,b_4,\ldots\) is not source authority.

## Revised connection gate

The connection intertwiner itself is exact:
\[
\mathcal M_nD_x
=
\frac1n e^{-u}
\left(\partial_u-\frac12\right)\mathcal M_n.
\]
The remaining finite comparison is therefore between the source Adams odd
generator and the single cyclic completed column, together with proof that no
later constructor requires iteration inside an unjustified three-dimensional
odd module.

At completion, the graph domain must control the full tower if arbitrary
operator words can reapply the shifted polynomial.

## Hostile

Any proposed \(3\times3\) matrix for \(P_-(A)\) on
\(\{b_0,b_1,b_2\}\) silently projects away the nonzero coefficients
\(4b_3\) and \(4b_4\). It can reproduce the first completed connection vector
while failing on the next constructor composition.
