# RH is avoidance of a Maslov divisor, not pentagon coherence

Author: `marici.Nima`

Date: 2026-08-26

Status: exact categorical DPC and finite hostile family

## Categorical target

Let \(\mathbb H\) be the completed split hyperbolic carrier and let
\(L_+\subset\mathbb H\) be the product-formula Lagrangian in one rigged
chart. Suppose the source-derived Fourier--theta correspondence transports the
reciprocal boundary relation to a family

\[
L(z)\in\operatorname{Lag}(\mathbb H).
\]

The fixed Lagrangian defines its Maslov divisor

\[
\Sigma_{L_+}
=
\{L\in\operatorname{Lag}(\mathbb H):L\cap L_+\ne0\}.
\]

When the determinant or pure-spinor bridge is constructed, its scalar section
vanishes precisely when \(L(z)\) enters this divisor, with multiplicity given
by the appropriate Fredholm or determinant-line intersection index.

The categorical RH statement is therefore a factorization through the open
transverse locus on each open half-plane:

\[
L:B\setminus H
\longrightarrow
\operatorname{Lag}(\mathbb H)\setminus\Sigma_{L_+}.
\]

Equivalently, the pullback divisor \(L^*\Sigma_{L_+}\) must be supported on
the critical seam \(H\).

This makes the earlier phrase "cannot enter" precise. It means that the
source functor has no morphism into the Maslov divisor from either open-sector
object.

## Why the pentagon is insufficient

Associator coherence compares five presentations of a four-stage composite.
If all intermediate correspondences are defined, the pentagon proves that
their composites agree. It says nothing about whether the resulting
Lagrangians are transverse.

A perfectly coherent functor may land entirely inside a degeneracy locus.
Therefore neither a vanishing pentagon residual nor a trivial associator
holonomy can orient the scalar section.

## Exact reciprocal hostile

Take \(V=\mathbb R^2\) and its hyperbolic double

\[
\mathbb H(V)=V\oplus V^*.
\]

For a scalar \(t\), define the skew map

\[
A_t=
\begin{pmatrix}
0&t\\
-t&0
\end{pmatrix}
\]

and its graph

\[
L_t=\{(x,A_tx):x\in V\}.
\]

Every \(L_t\) is maximal isotropic because \(A_t+A_t^T=0\). Relative to the
fixed primal Lagrangian \(L_0^{\mathrm{fix}}=V\oplus0\), one has

\[
L_t\cap L_0^{\mathrm{fix}}=\ker A_t.
\]

Hence \(L_t\) is transverse exactly when \(t\ne0\).

Now choose the reciprocal-even family

\[
t(z)=z^2-a^2,
\qquad a\ne0.
\]

It obeys \(t(-z)=t(z)\) and crosses the Maslov divisor at the off-seam pair
\(z=\pm a\). Every matrix composition remains associative, every
parenthesization agrees, and reciprocal symmetry is exact. Nevertheless the
scalar Pfaffian coordinate \(t(z)\) vanishes off seam.

This is the finite categorical version of the hostile symmetric multiplier.

## Missing source law

The required new theorem must restrict the image of the theta correspondence,
not merely its coherence. Possible categorical forms include:

- a positive Lagrangian semigroup whose action preserves one transverse
  chamber;
- a source-derived monotone crossing form with a fixed sign;
- a causal cone in the split carrier invariant under every admitted
  constructor;
- an exactness theorem making open-sector intersections impossible;
- a Fredholm index law whose only allowed support is the reciprocal fixed
  locus.

Each proposal must reject the reciprocal-even family above before inspecting
its divisor. If it accepts the family and only later notices \(z=\pm a\), it
has not supplied source orientation.

## Relation to completion

In the rigged infinite-dimensional setting, ordinary intersection dimension
is replaced by a Fredholm pair and its determinant line. Completion can create
an intersection when a transverse angle collapses to zero. Thus the global
theorem needs both:

1. pointwise source transversality at every finite stage;
2. a uniform or strict completion law preventing escape into the Maslov
   divisor at infinity.

This restates the earlier observability and closed-range obstructions in
intrinsic categorical language.

## Verification

The checker verifies the split form, maximal isotropy of every graph,
transversality for nonzero \(t\), rank loss at \(t=0\), reciprocal symmetry of
\(t(z)=z^2-a^2\), and off-seam crossings at a rational hostile pair.

