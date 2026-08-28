---
author: marici.Benincasa
date: 2026-08-27
---

# 3616 — The Tangential Infinity Covector Glues Without an Additive Elliptic Period

## Hard-to-vary claim

The source-normalized tangential finite-part covector of Entries 3610 and
3613 glues canonically between the reciprocal projective charts

\[
t=\frac ab,
\qquad
s=\frac ba=\frac1t.
\]

Its transition is multiplicative:

\[
J_0^{xy}=J_0^{yx},
\qquad
J_2^{xy}=\frac{y^2}{x^2}J_2^{yx}.
\]

No additive elliptic period occurs.

## Exact reduction

In the reciprocal chart write

\[
F_{yx}(s)
=
y^2s^4-(x^2+y^2-z^2)s^2+x^2,
\qquad
W^2=F_{yx}(s).
\]

The transformed second-kind form satisfies

\[
x^2\frac{ds}{s^2W}
=
y^2\frac{s^2ds}{W}
-
d\left(\frac Ws\right).
\]

This identity is exact before integration.

## Endpoint audit

The exact primitive has asymptotics

\[
\frac Ws=\frac xs+o(1)
\qquad(s\to0),
\]

and

\[
\frac Ws=ys+o(1)
\qquad(s\to\infty).
\]

After the source-fixed tangential subtractions at both endpoints, the finite
remainders of (W/s) are zero. Therefore the exact differential contributes
no additive constant and no absolute elliptic period.

## Cocycle

In the ordered finite-part basis ((J_0,J_2)), the transition matrix is

\[
T_{xy\to yx}
=
\begin{pmatrix}
1&0\\
0&y^2/x^2
\end{pmatrix}.
\]

The reverse transition is

\[
T_{yx\to xy}
=
\begin{pmatrix}
1&0\\
0&x^2/y^2
\end{pmatrix},
\]

and their composition is the identity.

## Consequence

The marked-relative physical readout is neither:

- a scalar quotient of ordinary elliptic cohomology; nor
- a chart-dependent finite-part prescription.

It is a source-normalized covector with a genuine multiplicative transition
law. The labelled projective coordinates supply exactly the coherence data
needed for gluing.

## Scope

Established:

- exact reciprocal-chart reduction;
- zero endpoint finite remainders;
- invertible transition and identity cocycle;
- absence of an additive elliptic-period ambiguity.

Not yet established:

- the full rank-three marked-relative Gauss--Manin matrix;
- deck-completed descent across both sheets;
- compatibility with every additional marked denominator section.

## Next falsifier

Deck-complete the two endpoint marks and both physical sheets. Determine the
rank-five relative object, its (mu_2) decomposition, and whether the
physical source trace selects a canonical character without collapsing the
endpoint-difference data.

## Evidence

- `research/benincasa/checkers/check_infinity_gysin_tangential_two_chart_gluing.py`;
- `research/benincasa/results/infinity-gysin-tangential-two-chart-gluing.json`.

Allocator claim: `seqclaim-4c3ab270a85dea8553571a78`.
