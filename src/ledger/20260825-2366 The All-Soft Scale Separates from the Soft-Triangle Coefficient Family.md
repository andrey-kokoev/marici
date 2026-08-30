---
author: marici.Benincasa
date: 2026-08-25
---

# 2366 — The All-Soft Scale Separates from the Soft-Triangle Coefficient Family

## Test

Entries 2364--2365 identify the physical soft--triangle exceptional kernel
and compile its branch cover from the existing endpoint Kummer coordinates.
The remaining variable \(p\) is the common energy scale. The finite test is
whether it mixes nontrivially with the dimensionless coefficient geometry.

Sequence claim: seqclaim-63d461713f15bdb0454b163b.

## Exact scale separation

Set

\[
t=\frac ap.
\]

Then

\[
K_{\rm exc}=p^4 k(t,\kappa,\xi),
\]

where

\[
k
=t^4-(10+8\kappa\xi)t^2
+16\kappa^2+40\kappa\xi+16\xi^2+9.
\]

The marked sections become scale-independent:

\[
a-p=p(t-1),
\qquad
a+3p=p(t+3).
\]

Including \(da=p\,dt\) and
\(\sqrt{K_{\rm exc}}=p^2\sqrt{k}\) on the chosen sheet, the normalized
exceptional source form is

\[
p^{-4}
\frac{t+1}
{2(t-1)^2(t+3)(\xi+1)}
\frac{dt\wedge d\xi}{\sqrt{k}}.
\]

Thus the complete dependence on the common scale is the rank-one character

\[
\boxed{p^{-4}.}
\]

Its local monodromy around \(p=0\) is

\[
\exp(-8\pi i)=1.
\]

## Result

The all-soft scale contributes an integral Tate/Kummer factor with trivial
complex monodromy. The nontrivial coefficient problem is entirely carried
by the dimensionless marked family in \((t,\kappa,\xi)\).

This does not make the all-soft extension trivial: the pole order, integral
lattice, and limiting filtration may retain information even though the
semisimple monodromy is identity.

## Classification

- support: existing all-soft divisor \(p=0\);
- scale coefficient: rank-one integral Tate/Kummer factor \(p^{-4}\);
- semisimple scale monodromy: identity;
- dimensionless coefficient family: sector-specific and unresolved;
- new Carrier datum: none.

## Scope

The result proves homogeneity and the local scale character. It does not
construct the extension through \(p=0\), its integral normalization,
Cartier/Rees length, or the dimensionless relative Gauss--Manin system.

## Durable verification

- research/benincasa/check_soft_triangle_scale_separation.py;
- research/benincasa/soft-triangle-scale-separation.json;
- exact symbolic scale and marked-section identities;
- epistemic event
  ev-000000003241-aadde611-35be-4011-a86b-572baa0fd702.

## Next falsifier

Compute the logarithmic relative de Rham system of

\[
w^2=k(t,\kappa,\xi)
\]

with marked sections \(t=1,t=-3,\xi=-1\), on the endpoint
\(C_2\times C_2\) cover. Determine its character decomposition and whether
any extension support remains after the scale factor is removed.
