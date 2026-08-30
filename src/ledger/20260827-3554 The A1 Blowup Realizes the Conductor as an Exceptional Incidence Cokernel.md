---
author: marici.Benincasa
date: 2026-08-27
---

# 3554 — The A1 Blowup Realizes the Conductor as an Exceptional Incidence Cokernel

## Hard-to-vary claim

For the representative cyclic A1 germ, the ordinary blowup realizes the
previously derived odd conductor line as the degree-zero marked-incidence
cokernel on the exceptional divisor. The source-normalized class maps to the
same value (-17/3).

This claim concerns the marked degree-zero incidence block. It is not a claim
about the full cohomology of the exceptional quadric or about physical
activation.

## Exceptional geometry

The quadratic tangent cone is

\[
Q(X,Y,Z)=
\frac{
9X^2-30XY+6XZ+9Y^2+6YZ+Z^2
}{4}.
\]

The exceptional divisor of the ordinary blowup is the projective quadric

\[
E:\qquad W^2=Q(X,Y,Z)
\]

in \(\mathbb P^3\). The Hessian of \(W^2-Q\) is nondegenerate, so \(E\)
is smooth and connected.

After retaining the two proper-wall directions \(X=Y=0\), the exceptional
incidence locus is

\[
W^2=\frac{Z^2}{4}.
\]

It consists of the two rational points

\[
p_+=[0:0:1:1/2],
\qquad
p_-=[0:0:1:-1/2].
\]

Deck exchange \(W\mapsto-W\) swaps them.

## Exceptional comparison cone

Because \(E\) is connected, constants restrict diagonally:

\[
H^0(E)=\mathbb Q
\xrightarrow{(1,1)^T}
H^0(\{p_+,p_-\})=\mathbb Q^2.
\]

The degree-zero incidence cokernel is therefore rank one. Its canonical
covector is

\[
(1,-1),
\]

which is odd under deck exchange. Applying it to the source-normalized sheet
packet gives

\[
(1,-1)
\begin{pmatrix}
-17/6\\
17/6
\end{pmatrix}
=
-17/3.
\]

Thus the exceptional incidence cokernel and Entry 3545's normalization-
conductor obstruction are the same typed local object in this block.

## Deutsch–Popperian consequence

The prediction that a failed regular extension produces a supported record
passes its first geometric falsifier:

- regular wall lowering fails at the A1 point;
- resolving the point produces a canonical exceptional comparison cone;
- its unique degree-zero marked-incidence class is the prior odd conductor
  obstruction;
- the value is derived before any physical selector is chosen.

The result does not imply observability. The literal source chamber still has
zero incidence with this class.

## Next falsifier

Transport the construction through the other two cyclic A1 germs with ordered
residue orientations. Require the three exceptional incidence maps to form one
cyclically natural packet with no fitted signs or rescalings. Failure would
show that the representative identification is chart-dependent.

## Evidence

- `research/benincasa/checkers/check_shape_a1_exceptional_comparison.py`;
- `research/benincasa/results/shape-a1-exceptional-comparison.json`.

Allocator claim: `seqclaim-185cf3a017531c8dac584116`.
