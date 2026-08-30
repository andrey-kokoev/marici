# Even and odd completion packets share one universal truncated Jordan matrix

## Graded bases

Set
\[
X=\pi x^2.
\]

For the even Gaussian packet define
\[
e_k=X^ke^{-X},
\qquad k=0,1,2.
\]

For the odd connection packet define
\[
o_k=xX^ke^{-X},
\qquad k=0,1,2.
\]

Let
\[
A=x\partial_x.
\]

Then
\[
Ae_k=2k\,e_k-2e_{k+1},
\]
while
\[
Ao_k=(2k+1)o_k-2o_{k+1}.
\]

The completion polynomial is
\[
P_{\mathrm{even}}(A)=A(A+1)
\]
on the even packet and
\[
P_{\mathrm{odd}}(A)=(A-1)A
\]
on the odd packet.

## Exact coefficient identity

A direct calculation gives, for either parity packet \(v_k=e_k\) or \(v_k=o_k\) with its correctly shifted polynomial,
\[
P v_k
=
2k(2k+1)v_k
-
(8k+6)v_{k+1}
+
4v_{k+2}.
\]

Thus the grade coefficients are identical after the parity shift is respected.

For \(k=0\),
\[
Pv_0=-6v_1+4v_2,
\]
which is the familiar completed theta polynomial.

For \(k=1\),
\[
Pv_1=6v_1-14v_2+4v_3.
\]

For \(k=2\),
\[
Pv_2=20v_2-22v_3+4v_4.
\]

## Three-grade quotient matrix

On the quotient by grades \(v_3,v_4,\ldots\), the common matrix in the ordered basis
\[
(v_0,v_1,v_2)
\]
is
\[
J_3
=
\begin{pmatrix}
0&0&0\\
-6&6&0\\
4&-14&20
\end{pmatrix},
\]
with columns representing the images of basis vectors.

Therefore the even and odd length-three packets are not governed by two unrelated matrices. They are two parity realizations of one universal truncated Jordan operator.

## Categorical meaning

The degree shift
\[
e_k
\longleftrightarrow
o_k
\]
intertwines
\[
A(A+1)
\quad\text{with}\quad
(A-1)A
\]
at the coefficient level.

Analytic parity remains different, but the type-fiber completion matrix is common. This is exactly the structure needed for a shared Adams grade compiler:

\[
\mathbb C^3_{\mathrm{grade}}
\otimes
\left(
\mathbb C_{\mathrm{even}}
\oplus
\mathbb C_{\mathrm{odd}}
\right),
\]
with \(J_3\) acting on grade and reflection character acting on the second factor.

## Important quotient qualification

The span of the first three grades is not invariant under completion for arbitrary inputs: \(v_1\) and \(v_2\) generate \(v_3\) and \(v_4\).

Hence \(J_3\) is exact only as:

- the matrix on the quotient by grades at least three;
- the front \(3\times3\) block of the infinite upper-grade operator;
- or the cyclic packet generated from \(v_0\) when only its first completed image is required.

Calling it a closed three-dimensional invariant system without one of these typings would be false.

## Adams comparison

The common matrix removes one prospective obstruction: no parity-dependent scalar renormalization is needed to align the even and odd completion coefficients.

The remaining Adams type-fiber theorem must compare its grade-doubling generator with \(J_3\) while retaining:

- the reflection-character factor;
- the label factor \(n^{-1}\) on the odd connection;
- higher-grade leakage when iterated completion is admitted;
- endpoint and wall coordinates.

## Hostile

Use \(A(A+1)\) directly on the odd analytic basis. The coefficient identity fails because the necessary degree shift is omitted. Conversely, use the common \(J_3\) but claim the first three grades form an invariant subspace; iteration then leaks into \(v_3,v_4\).

## Frontier

The finite one-label coefficient calculation is now complete. The next irreducible question is whether the source Adams type edge acts on the common grade factor by this \(J_3\), its exponential/transfer, or a distinct incidence matrix related by a proved comparison cell.
