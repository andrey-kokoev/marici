# Vanishing Mixed-Prism Curvature on the Scalar Occurrence Module

## Record

Date: 2026-08-13

Status: the first mixed scalar-refinement/physical-cut obstruction vanishes strictly on the
decorated scalar occurrence module at ten points and remains zero with the first nontrivial
spectator cores at twelve points.

This closes the coefficient-level gap isolated in entry 33 through the first universal and
spectator-stable tests. It does **not** yet construct the filtered Pochhammer/Cousin current or
prove a finite-(\alpha') worldsheet comparison.

## Question

Entry 33 reduced the missing coefficient naturality to

\[
\Omega_e
=
G_e h_{\rm scalar}
-
h_{\rm split}G_e.
\]

A slogan that the prism square commutes is insufficient. The physical cut has two scalar slots,
so the actual question is whether the cut of a marked scalar edge lifts termwise to a canonical
sum of marked scalar edges at the enlarged physical core.

## The occurrence complex

Let

\[
x_0\longrightarrow x_1
\]

be the lower scalar-refinement edge of a mixed prism and let (P) be its common physical core.
Choose one scalar contact mark in every component of the polygon cut by (P).

The regional Catalan bijection sends each decorated endpoint to a marked full quadrangulation

\[
(x_i;\mathbf m)
\longmapsto
(Q_i;\mathbf m).
\]

The established physical coaction along (e\notin P) is

\[
G_e[Q_i,P;\mathbf m]
=
-\frac1{X_e}
\sum_{\sigma=0}^{1}
X_{d_e^\sigma}
[Q_i,P\cup\{e\};
 \mathbf m\cup\{d_e^\sigma\}],
\]

where (d_e^0,d_e^1) are the two scalar diagonals of the new sink quadrilateral.

## Exact support naturality

For every decorated mixed edge tested,

\[
e\in Q_0
\quad\Longleftrightarrow\quad
e\in Q_1.
\]

Thus no asymmetric-support obstruction occurs.

If \(e\) is absent from both quadrangulations, both cut routes are zero.

If \(e\) is present, the two directed edges have:

- the same source quadrilateral;
- the same two scalar slots (d_e^0,d_e^1);
- the same global and spectator component marks;
- possibly different target quadrilaterals.

The target can slide under scalar refinement, but it does not enter the coefficient map. Therefore

\[
G_e[Q_0,P;\mathbf m]
quad\text{and}\quad
G_e[Q_1,P;\mathbf m]
\]

have exactly the same two Laurent coefficients and mark labels.

At ten points the supported transports split evenly between fixed and sliding target behavior for
the original prism occurrences: twenty of each per polarity.

## The correct upper transport

Apply regional inverse Catalan descent separately to both endpoints of each matched cut term. For
each slot \(\sigma\), the resulting pair

\[
y_0^\sigma
\longrightarrow
y_1^\sigma
\]

is a genuine scalar flip edge at core (P\cup\{e\}).

Exactly one of the two slot-labelled edges is the visible upper edge of the forced prism square.
The other is a parallel scalar edge elsewhere in the associahedral envelope.

Consequently the correct action of the cut on the lower one-cell is

\[
\boxed{
G_e(h)
=
-\frac{X_{d_e^0}}{X_e}h_e^0
-
\frac{X_{d_e^1}}{X_e}h_e^1 .
}
\]

It is not merely the top edge of the original square.

Taking cellular boundaries gives

\[
\partial G_e(h)
=
G_e(\partial h)
\]

term by term. Hence

\[
\boxed{\Omega_e=0}
\]

on the tested occurrence module. No higher primitive is required at this level.

## Ten-point universal audit

There are twenty distinct mixed scalar squares per polarity and forty original marked prism
occurrences.

For the original occurrences:

- every cut is supported;
- every cut produces two terms;
- every transport contains one forced upper edge and one parallel slot edge;
- twenty have fixed target cells;
- twenty have sliding target cells;
- every curvature support is empty.

Allowing every scalar mark common to a lower edge gives 120 distinct decorated transports:

- 50 supported transports;
- 70 common zero-support transports;
- no asymmetric support.

Run:

    python -B research/nima/check_mixed_prism_curvature.py
    python -B research/nima/check_mixed_prism_spectator_stability.py

## Twelve-point spectator audit

At twelve points there are 336 distinct mixed squares per polarity and 2,568 decorated transports.

The audit includes:

- base core degree zero with one twelve-gon region;
- base core degree one with regional profiles (4+10);
- base core degree one with regional profiles (6+8).

The exact support counts are:

\[
1092
\quad\text{supported},
\qquad
1476
\quad\text{zero on both routes},
\qquad
0
\quad\text{asymmetric}.
\]

Every supported transport again has two terms, one forced edge, one parallel edge, and zero
curvature. One-step rotation maps the complete atlas to the opposite polarity sheet.

## What is established

1. The regional marked Catalan map has an explicit inverse at partial physical core.
2. Cut support is natural under every tested mixed scalar refinement.
3. The source quadrilateral and its two coefficient slots are invariant when the cut is supported.
4. Target-cell motion is harmless because the target is not coefficient data.
5. Both cut terms lift to genuine scalar edges at the enlarged core.
6. The physical coaction extends strictly from vertices to every tested mixed prism one-cell.
7. The result survives the first nontrivial spectator/product configurations.
8. The construction is integral, local at occurrence level, and deck-equivariant.

## Strong inference, not yet theorem

The calculation strongly suggests the all-arity cellular formula

\[
G_P:
C_*^{\rm cell}(\operatorname{AssEnv}(\Phi);\mathcal L)
\longrightarrow
C_*^{\rm cell}(\operatorname{AssEnv}(\Phi);\mathcal L)
\otimes \operatorname{Cut}(P)
\]

with (G_e) acting on scalar one-cells by the two-slot formula above.

The block-face theorem of entry 31 and regional tensor factorization of entry 27 make spectator
stability structurally natural. Nevertheless an all-arity proof must show, directly from the
rooted dual-tree rule, that support and source-cell invariance hold for an arbitrary remote mark
and arbitrary base core.

Do not promote the n=10/n=12 audit alone to that theorem.

## Remaining worldsheet gap

The scalar carrier and its occurrence-level coefficient coaction are now separate from the
remaining comparison problem.

Still missing are:

1. a loaded Pochhammer/Cousin current for every decorated scalar cell;
2. a finite-nonresonant-(\alpha') proof that the two-slot edge formula is a twisted-chain map;
3. control of the Laurent/nearby-cycle limit at physical divisors;
4. identification of the resulting derived class with ((\operatorname{Pf}'A)^2);
5. compatibility with the inverse scalar pairing before taking cohomology.

Thus the first mixed curvature is not an obstruction. The frontier has moved from scalar cellular
geometry to the filtered scalar-to-worldsheet comparison.

## Decision

Promote:

> At the first universal mixed prism, and with all spectator configurations through twelve points,
> the scalar-refinement/physical-cut Beck--Chevalley curvature vanishes strictly on the decorated
> occurrence module. The cut of a scalar edge is the weighted sum of two canonically reconstructed
> upper scalar edges.

Retain as open:

> Prove the all-arity rooted-tree naturality lemma and lift this strict cellular coaction to
> finite-(\alpha') loaded twisted chains.
