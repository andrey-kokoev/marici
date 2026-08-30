# Half-density centering makes prime reciprocity an exact inverse but trivializes the Schur feedback

## Raw reciprocal product

The prime-loop family satisfies

\[
L(s)L(t)=L(s+t).
\]

Under the Riemann reflection \(s\mapsto1-s\),

\[
L(s)L(1-s)=L(1).
\]

Thus the raw reciprocal sector is not the inverse of \(L(s)\). The residual factor is the fixed Euler density

\[
E=L(1),\qquad Ee_p=p^{-1}e_p.
\]

This is an operator identity on the projective exponential Köthe source, not merely a scalar determinant relation.

## Half-density normalization

Let

\[
H=L\left(\frac12\right),
\qquad
A(s)=H^{-1}L(s)=L\left(s-\frac12\right).
\]

Since every \(L(z)\) is a Köthe automorphism,

\[
A(s)^{-1}
=
L\left(\frac12-s\right)
=
A(1-s).
\]

Therefore

\[
A(s)A(1-s)=A(1-s)A(s)=I.
\]

The Euler half-density is exactly the normalization that turns Riemann reflection into operator inversion on the prime source.

This closes the prime-loop instance of the reciprocal operator law. No determinant or scalar functional equation is needed.

## Compact-uniform control

For compact \(C\subset\mathbb C\), the families

\[
A(s),\qquad A(s)^{-1}=A(1-s)
\]

are equicontinuous in the projective Köthe topology. The required seminorm shift is controlled by

\[
\sup_{s\in C}\left|\operatorname{Re}s-\frac12\right|.
\]

Thus reciprocal inversion persists under prime cutoff completion at the source level.

## Supply cancellation

In any Hilbert realization where the normalized maps and adjoints are defined on a common core, the operator supply cocycle gives

\[
R(A(1-s))
=
-A(1-s)^*R(A(s))A(1-s).
\]

Hence the two centered sectors carry exactly opposite transported supply. This is the source-prime specialization of reciprocal lossless sewing.

The identity is conditional only on the chosen Hilbert realization. The inverse law itself is already exact on the Köthe source.

## The Schur-feedback trap

It is tempting to use the reciprocal inverse as the second off-diagonal arrow in

\[
\mathcal T_{\mathrm{rec}}(s)
=
\begin{pmatrix}
I&A(s)\\
A(1-s)&I
\end{pmatrix}.
\]

But its Schur complement is

\[
I-A(1-s)A(s)=0.
\]

Therefore this block is singular for every \(s\), not only at zeta zeros.

Exact reciprocal transport cannot simultaneously be the nontrivial determinant feedback. If the backward link is literally the inverse of the forward link, the closed loop has unit gain identically.

This is not a defect in reciprocity. It proves that transport coherence and spectral closure are different constructors.

## Three distinct arrows

The completed architecture must distinguish:

1. **Prime propagation**
   \[
   A(s)=L\left(s-\frac12\right).
   \]

2. **Reciprocal transport**
   \[
   A(1-s)=A(s)^{-1}.
   \]

3. **Boundary feedback**
   \[
   F(s),
   \]
   assembled from seam, endpoint, archimedean, and Green boundary data.

Only the third arrow may close the loop to produce a nontrivial characteristic operator such as

\[
I-F(s)A(s).
\]

Replacing \(F(s)\) by the reciprocal transport \(A(1-s)\) makes the characteristic operator vanish identically.

## Consequence for the companion identity return

The elementary Euler companion uses \(N=I\), giving

\[
I-L(s).
\]

The reciprocal transport uses \(N=A(1-s)\), giving zero after half-density centering. Neither arrow is yet the completed RH boundary feedback:

- \(I\) is a linearization evaluation arrow;
- \(A(1-s)\) is the reciprocal inverse;
- \(F(s)\) must encode the completed boundary condition.

Conflating these three maps produces either the open Euler determinant or an identically singular block, but not the completed \(\Xi\) pencil.

## Source authority gained

The half-density normalization is no longer merely a favorable weight. It is characterized by the inverse equation.

More generally, if \(B=L(\beta)\) and

\[
B^{-1}L(s)
\]

is required to invert under \(s\mapsto1-s\), then

\[
L(s-\beta)L(1-s-\beta)=L(1-2\beta)=I.
\]

Faithfulness of the diagonal prime action forces

\[
\beta=\frac12.
\]

Thus the centering exponent is uniquely determined.

## Hostiles

1. Use raw \(L(1-s)\) as the inverse of \(L(s)\) and omit the fixed density \(L(1)\).
2. Insert exact reciprocal inverses as both links and interpret the resulting permanent kernel as the zeta zero set.
3. Use the companion identity return and call it reciprocal sewing.
4. Absorb the half-density into an untyped scalar normalization.
5. Infer the missing boundary feedback from transport inversion alone.

## Verdict

Euler half-density centering gives the exact source-level reciprocal law

\[
A(1-s)=A(s)^{-1}.
\]

But this advance also proves a no-go: reciprocal inversion is a coherence transport, not the spectral feedback arrow. The first genuinely missing operator is now the boundary feedback \(F(s)\) that couples the centered prime loop to seam, endpoint, archimedean, and Green data without becoming either \(I\) or \(A(s)^{-1}\).
