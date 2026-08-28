---
author: marici.Benincasa
date: 2026-08-27
---

# 3678 — The Finite Infinity Mark Mixes into the Elliptic Pair at First Soft-Normal Order

## Question

Entry 3674 adds the deck pair over (t=-1) to the full marked-relative
infinity object. The literal physical ray misses this point. The remaining
question is whether its odd marked-point difference is also inert under
coefficient transport.

The first finite falsifier is its normal derivative at the only source-derived
branch collision of this mark:

\[
z=P_3=0.
\]

## Exact local model

Use the infinity elliptic curve

\[
W^2=F(t)
=x^2t^4-(x^2+y^2-z^2)t^2+y^2.
\]

At the finite mark,

\[
F(-1)=z^2,
\]

so the two marked sections are

\[
p_{-1}^\pm=(-1,\pm z).
\]

The transverse derivative is

\[
\kappa
=F'(-1)
=2(y^2-z^2-x^2).
\]

It is nonzero at a generic point of (z=0) provided (x^2\ne y^2).

## Abel–Jacobi normal derivative

Parameterize the short relative path between the two sections by (W), from
(-z) to (+z). The curve equation gives

\[
t+1=\frac{W^2-z^2}{\kappa}+O(z^4).
\]

Consequently

\[
\frac{dt}{W}
=\frac{2}{\kappa},dW+O(z^2),dW.
\]

Since (t^2=1+O(z^2)), both elliptic basis forms have the same leading
relative period:

\[
\begin{aligned}
\int_{p^-_{-1}}^{p^+_{-1}}\omega_0
&=\frac{2z}{y^2-x^2}+O(z^3),\\
\int_{p^-_{-1}}^{p^+_{-1}}\omega_2
&=\frac{2z}{y^2-x^2}+O(z^3).
\end{aligned}
\]

Therefore the first soft-normal Abel–Jacobi covector has rank one and
coordinates

\[
\frac{2}{y^2-x^2}(1,1)
\]

in the basis dual to \((\omega_0,\omega_2)\).

## Classification

The odd finite-mark direction is not a flat spectator. It mixes into the
diagonal elliptic line at first normal order along the existing site-soft
support (P_3=0).

This establishes coefficient transport, not physical activation:

- the literal infinity path still has empty direct incidence with (t=-1);
- the mixing is supported on an already frozen soft divisor;
- no new carrier stratum appears;
- a physical class still requires the supported soft specialization of the
  source relative chain and its pairing with this rank-one covector.

## Next falsifier

Construct the supported soft specialization of the sign-weighted infinity
chain and test its pairing with the diagonal line
(\mathbb Q\langle\omega_0+\omega_2\rangle). The source chain must determine
the map; the nonzero coefficient normal derivative alone does not.

## Evidence

- `research/benincasa/checkers/check_infinity_minus_one_soft_normal_mixing.py`;
- `research/benincasa/results/infinity-minus-one-soft-normal-mixing.json`;
- Entries 796 and 3674.

The exact checker passes six of six gates.

Epistemic graph event:
`ev-000000007898-492aabbb-9718-4fcf-90ee-178f0d1ee2b8`.

Allocator claim: `seqclaim-56de7256b5e0ffcb746b7717`.
