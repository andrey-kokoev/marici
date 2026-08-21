---
author: marici.Benincasa
---

# 1501 — The Generated Gaussian Pair Is Visible in Two Independent Statistical Time Structures

## Status

Exact linearized composition of Entry 1494's generated quadratic kernel with
Entry 1499's source propagator pushforward.

## Frozen source formula

Write the quadratic initial kernel as

\[
A_k=\alpha_k+i\beta_k,
\qquad
B_k\in\mathbb R.
\]

Collins, arXiv:1309.2656v1, derives

\[
\begin{aligned}
\Delta G_k(t,t')
=\frac{1}{4\omega_k^2}
\frac{1}{\omega_k-\beta_k-B_k}
\bigl[&
-2\omega_k\alpha_k\sin\Sigma\\
&+(2\omega_k\beta_k-\alpha_k^2-\beta_k^2+B_k^2)
\cos\Sigma\\
&+(2\omega_kB_k+\alpha_k^2+\beta_k^2-B_k^2)
\cos\Delta
\bigr],
\end{aligned}
\]

where

\[
\Sigma=\omega_k(t+t'-2t_0),
\qquad
\Delta=\omega_k(t-t').
\]

## Generated source order

Entry 1494's published matching sets

\[
\alpha_k=0
\]

and generates \((\beta_k,B_k)\) at one-loop order. Linearizing the exact
propagator map in these generated kernels gives

\[
\boxed{
\Delta G_k^{(1)}(t,t')
=
\frac{\beta_k}{2\omega_k^2}\cos\Sigma
+
\frac{B_k}{2\omega_k^2}\cos\Delta.
}
\]

## Visibility result

The two time structures

\[
\cos\omega_k(t+t'-2t_0),
\qquad
\cos\omega_k(t-t')
\]

are linearly independent as generic bilocal functions. Therefore the
linearized readout

\[
\boxed{
(\beta_k,B_k)
\longmapsto
\Delta G_k^{(1)}(t,t')
}
\]

has zero kernel over the generic bilocal time-function space.

Equivalently, both deck eigenkernels

\[
K_{\rm diag}=\beta_k+B_k,
\qquad
K_{\rm anti}=\beta_k-B_k
\]

are physically visible in the full statistical propagator, although the
contour occurrence matrix of that propagator has rank one.

## Important distinction

\[
\boxed{
\text{contour rank one}
\not\Rightarrow
\text{one coefficient parameter}.
}
\]

The contour projection forgets causal matrix directions, but bilocal time
dependence retains the two generated statistical coefficients.

At one fixed pair \((t,t')\), the readout is only one scalar and can have a
kernel. The injectivity statement requires the full generic bilocal function,
not a fitted single-time observable.

## Composed mechanism

The source-derived chain is now

\[
\boxed{
\mathcal C_{3}^{(0,1,2,3)}
\xrightarrow{\text{one-loop}}
\mathcal C_{2,\rm stat}^{(0,2)}
\xrightarrow{\text{Gaussian pushforward}}
G^K_{\rm bilocal},
}
\]

and the second arrow is injective on the generated pair at first order.

Thus the one-loop cubic-to-quadratic correction is not an algebraic artifact
invisible to propagation. It changes two independent statistical time
structures while leaving the spectral propagator unchanged.

## Carrier classification

Every stage uses the same finite initial hypersurface, doubled occurrences,
and Gaussian pushforward. The increased complexity lies in coefficient
degree and bilocal readout, not in new carrier incidence.

## Next falsifier

Test whether a finite collection of late-time cosmological observables still
separates \(\beta_k\) and \(B_k\). Failure at a restricted readout would be an
observational projection kernel, not loss of the underlying coefficient
distinction.

## Provenance

- Collins, arXiv:1309.2656v1, Sec. II;
- Entries 1494, 1497, and 1499;
- allocator claim `seqclaim-390ace62c1b9251585f07cbe`.
- epistemic event `ev-000000001625-02649e58-632a-45b6-bf48-2d269593701d`.
