# Reciprocal spectral density is the sign-regularity invariant

## General criterion

For the completed spectral kernel

\[
b(t,\lambda)
=t^{5/4}\lambda(2\pi t\lambda-3)e^{-\pi t\lambda},
\qquad t\ge1,
\]

let \(\Lambda=\{\lambda_j\}\) be any strictly increasing positive labelled
spectrum. Integral squares are one example, but the all-order proof uses
only the reciprocal-density condition

\[
\boxed{
\sup_{t\ge1}\sum_j\frac1{\pi t\lambda_j}<\frac23.
}
\]

Equivalently, because the supremum occurs at \(t=1\),

\[
\boxed{
\sum_j\lambda_j^{-1}<\frac{2\pi}{3}.
}
\]

Under this condition every finite ordered minor

\[
\det[b(t_i,\lambda_j)]
\]

has sign \((-1)^{n(n-1)/2}\). Thus the labelled family is strictly reverse
sign regular of all orders.

## Proof

For any finite subset, the general Wronskian polynomial factors as

\[
Q_n(z)
=2^ne_n(z)\sum_{r=0}^n(-1)^rA_r,
\]

where

\[
A_r=\frac{(2r+1)!!}{2^r}e_r(z^{-1}),
\qquad z_j=\pi t\lambda_j.
\]

Writing \(S=\sum_jz_j^{-1}\), the elementary-symmetric inequality gives

\[
\frac{A_{r+1}}{A_r}
\le
\frac{2r+3}{2(r+1)}S
\le\frac32S.
\]

If \(S<2/3\), the positive terms \(A_r\) strictly decrease. Their alternating
sum is positive, so every initial Wronskian has the required sign. The
extended-Chebyshev criterion gives the ordered evaluation-minor signs.

## Arithmetic square margin

For \(\lambda_j=j^2\),

\[
\sum_{j\ge1}\lambda_j^{-1}
=\frac{\pi^2}{6},
\]

so

\[
S_{\max}=\frac1\pi\frac{\pi^2}{6}=\frac\pi6.
\]

The available margin to the sufficient threshold is

\[
\frac23-\frac\pi6
=\frac{4-\pi}{6}>0.
\]

This quantifies integrality protection. The theorem is robust under spectral
perturbations or added labels as long as their total reciprocal mass stays
within that margin.

Without invoking the Basel identity, the earlier telescoping estimate gives
the weaker but still strict \(S<2/3\).

## Hostile density mechanism

The continuous order-seven witness clusters seven labels near
\(\lambda=1\). Its reciprocal mass is near

\[
\frac7\pi>\frac23,
\]

well outside the protected chamber. The failure is therefore not merely
“continuity versus discreteness”; it is excessive reciprocal spectral
density near the endpoint.

The criterion is sufficient, not necessary. Exceeding \(2/3\) does not by
itself prove a wrong-sign minor. It removes the alternating-term domination
certificate and opens the door to failure. The explicit continuous
order-seven determinant supplies the actual falsifier.

## Source-local interpretation

The relevant arithmetic property is:

> the completed source has sufficiently sparse low-energy labels in
> reciprocal mass.

Square growth is one source grammar that enforces this. Any alternative
source with the same reciprocal-density bound inherits the all-order
variation law, while a type-erased or clustered source need not.

This is more informative than treating “integrality” as an indivisible
magic word. It isolates the exact quantitative resource used by the proof.

## Cross-sector form

The same pattern appears outside arithmetic:

- resource labels may be individually valid while their aggregate inverse
  slack exceeds a stability threshold;
- fault-model witnesses may be individually admissible while overlap
  density is insufficient;
- encoded modes may be individually constructible while low-cost resource
  congestion destroys a global schedule law.

The general warning is that local typing plus positivity does not imply a
global orientation; an aggregate density inequality may be the missing
source invariant.

## Boundary

Reciprocal sparsity proves spectral \(\mathrm{SSR}_\infty\), not the
de Branges normal-current inequality. The entire Gaussian counterexample
already shows that even perfect spectral sign regularity does not survive
the positive-summation/cosine constructor automatically.

