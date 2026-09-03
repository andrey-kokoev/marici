# Weighted Birman-Schwinger finite certificate

## Question

What finite inequalities certify positivity after all bounded remainders are retained in the weighted operator?

## Claim boundary

This packet fixes the block-certificate interface. It does not assemble the Weil matrix because the complete explicit-formula normalization and signs are not yet sourced.

## Weighted equivalence

Let

\[
A=\log(1+\sqrt{-\Delta_D})>0,
\qquad W=A+B,
\]

with \(B\) bounded and self-adjoint. Define

\[
K=A^{-1/2}BA^{-1/2}.
\]

Then \(K\) is compact and self-adjoint, and

\[
W\ge0\quad\Longleftrightarrow\quad I+K\ge0.
\]

For the split \(E_M\oplus Q_M\), write

\[
I+K=
\begin{pmatrix}
F_M&C_M\\
C_M^*&T_M
\end{pmatrix}.
\]

Suppose directed enclosures prove

\[
\lambda_{\min}(F_M)\ge\mu_M,
\qquad
\lVert C_M\rVert\le c_M,
\qquad
\lVert Q_MKQ_M\rVert\le r_M<1.
\]

Then \(T_M\ge(1-r_M)I\), and the Schur complement gives the sufficient condition

\[
\mu_M-\frac{c_M^2}{1-r_M}\ge0.
\]

This is the finite low-block, coupling, and tail certificate in one typed inequality.

## Generic fallback

If \(b=\lVert B\rVert\) and

\[
d_n=\log\left(1+\frac{n\pi}{2L}\right),
\]

then

\[
r_M\le\frac{b}{d_{M+1}},
\qquad
c_M\le\frac{b}{\sqrt{d_1d_{M+1}}}.
\]

These bounds are rigorous but can still require exponential \(M\). Componentwise weighted tails are therefore needed for execution, while the unified finite matrix retains signed cancellation.

## Typed blocker

Matrix assembly is blocked at the first missing object: the complete normalized explicit-formula identity specifying every component of \(B\), including sign, prefactor, adjoint convention, and endpoint term. Acceptance requires a source-linked identity from which each finite matrix entry and each componentwise tail bound can be generated without convention mixing.

## Disposition

The proof architecture is complete. No further low-block enlargement is justified until the normalized identity is materialized. Once supplied, the acceptance test is exactly the directed Schur residual above.

## Verification

- `research/voevodsky/checkers/check_weighted_birman_schwinger_certificate.py`
- `research/voevodsky/results/weighted_birman_schwinger_certificate.json`
