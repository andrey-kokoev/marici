---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2220 — The Gaussian Score Commutes with the Component-Soft Rees Resolution

## Two-chart test

At the component-soft center \((q,y)=(0,0)\), Entry 2176 resolves the complete
route through

\[
y=qt
\qquad\text{or}\qquad
q=ys.
\]

On both charts the composed grade-two route is regular:

\[
A=8C.
\]

Introduce the physical multiplicative covariance parameter \(\lambda\) at
fixed \((q,y)\). It labels the final erased-edge contraction and therefore
acts on the fully deleted route:

\[
B(\lambda)=-8\lambda C.
\]

The strict family on both charts is

\[
F_E(\lambda)=8C-8\lambda C.
\]

Thus

\[
F_E(1)=0,
\qquad
\left.\lambda\partial_\lambda F_E\right|_{\lambda=1}=-8C.
\]

The chart transition introduces no defect:

\[
\boxed{
[\operatorname{Rees}_{(q,y)},\lambda\partial_\lambda]=0.
}

## Distinction of directions

Although the physical kernel behaves as \(K(y)\sim y^{-1}\), varying its
multiplicative normalization at fixed momentum is not the same operation as
moving along the soft normal \(y\). Keeping these directions labelled avoids
the false commutator that would result from identifying them.

## Evidence

- Entries 2176 and 2219
- `research/benincasa/checkers/soft_rees_score_commutation.rs`

