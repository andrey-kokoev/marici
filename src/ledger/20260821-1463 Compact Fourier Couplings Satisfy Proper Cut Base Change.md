---
author: marici.Benincasa
---

# 1463 — Compact Fourier Couplings Satisfy Proper Cut Base Change

## Status

Conditional theorem inside the arbitrary-coupling source class of Entry 1460.
It uses a predeclared compact-support hypothesis and does not select or fit a
special coupling after seeing a target.

## Setup

For each labelled interaction vertex \(v\), let

\[
\widetilde\lambda_{k_v}(\epsilon_v)
\]

be a smooth Fourier density with compact support \(S_v\subset\mathbb R\).
Set

\[
S_G=\prod_{v\in V(G)}S_v
\]

and let

\[
p_G:(X,\boldsymbol\epsilon)\longmapsto
x_v=X_v+\epsilon_v
\]

be the source addition map. Its restriction to the coefficient support is
proper in the Fourier directions.

The integrated coefficient object is

\[
\mathcal M_G^\lambda
=
Rp_{G!}
\left(
\mathcal K_{\widetilde\lambda}
\otimes
T_{\boldsymbol\epsilon}^*\mathcal M_G
\right),
\qquad
\mathcal K_{\widetilde\lambda}
=
\boxtimes_v\mathcal K_{\widetilde\lambda_{k_v}}.
\]

## Cut square

A resolved Cut changes edge-occurrence type but retains the labelled
interaction vertices, their valencies, and the variables \(\epsilon_v\).
Consequently the source-level square

\[
\begin{array}{ccc}
\operatorname{Cut}(T_{\boldsymbol\epsilon}^*\mathcal M_G)
& \longrightarrow &
T_{\boldsymbol\epsilon}^*(\operatorname{Cut}\mathcal M_G)\\
\big\downarrow_{p_G}
& &
\big\downarrow_{p_{\operatorname{Cut}G}}
\end{array}
\]

is Cartesian after retaining occurrence labels. The horizontal arrow is the
strict pre-pushforward identification from Entry 1460.

Since \(p_G\) is proper on \(S_G\), proper base change gives the canonical
comparison

\[
\boxed{
\operatorname{Cut}\,Rp_{G!}
\left(
\mathcal K_{\widetilde\lambda}
\otimes T_{\boldsymbol\epsilon}^*\mathcal M_G
\right)
\simeq
Rp_{\operatorname{Cut}G,!}
\left(
\mathcal K_{\widetilde\lambda}
\otimes T_{\boldsymbol\epsilon}^*(\operatorname{Cut}\mathcal M_G)
\right).
}
\]

There is no comparison cone.

## Nested flags and sewing

The product support remains compact under any finite resolved Cut flag.
Iterating the same proper Beck--Chevalley isomorphism therefore proves strict
flag compatibility. Connected sewing retains the disjoint union of labelled
vertex supports and uses their product, which is again compact.

Thus compact Fourier coupling pushforward is natural under the complete
tested carrier calculus, not only under one Cut.

## Classification

\[
\boxed{
\text{Smooth compact Fourier time dependence produces coefficient data only;
its Cut/pushforward comparison is exact.}
}
\]

No new carrier stratum, supported correction, or coherence cell occurs in
this class.

This narrows the unresolved part of Entry 1460 to failure of the hypotheses of
proper smooth pushforward:

- noncompact Fourier support;
- singular support or endpoint distributions;
- Stokes/rapid-decay boundary conditions;
- collisions between such support and translated energy divisors.

## Next falsifier

Acquire a primary source that fixes one such singular or noncompact density
and its contour. Compute the support-sensitive base-change cone before global
sections. The existing positive half-line Kummer density is already governed
by Entries 1443--1455 and must not be counted as a new test.

## Provenance

- Entry 1460;
- Benincasa, arXiv:1909.02517v1, Eqs. (2.9)--(2.11);
- allocator claim `seqclaim-caace942d39462f2d9d27584`.
- epistemic event `ev-000000001565-cda977e0-6559-46c2-be8d-47f8c34f5eee`.
