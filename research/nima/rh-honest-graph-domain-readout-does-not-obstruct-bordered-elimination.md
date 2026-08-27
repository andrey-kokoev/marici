# An honest graph-domain readout does not obstruct bordered elimination

Author: `marici.Nima`

Date: 2026-08-26

Status: graph-domain no-go for the bordered route

## Closed observer setup

Let (H) be a Hilbert or locally convex state carrier, and let

\[
y:\operatorname{Dom}(y)\subset H\longrightarrow\mathbf C
\]

be a closed boundary observer. Equip its domain with the graph norm

\[
\lVert v\rVert_y=\lVert v\rVert_H+|y(v)|.
\]

Suppose the transported source state (u=Mx) has an honest ordered readout

\[
f=y(u).
\]

Then necessarily (u\in\operatorname{Dom}(y)).

## Domain preservation

The right triangular transformation acts by

\[
R(v,t)=(v-ut,t).
\]

Because the observer domain is linear and (u\in\operatorname{Dom}(y)), it
preserves (operatorname{Dom}(y)\oplus\mathbf C). Its inverse replaces
(-u) by (u) and preserves the same domain.

Moreover,

\[
\lVert v-ut\rVert_y
\le
\lVert v\rVert_y
+|t|\bigl(\lVert u\rVert_H+|y(u)|\bigr).
\]

Thus (R) and (R^{-1}) are bounded in the graph topology.

The left triangular transformation acts by

\[
L(h,s)=(h,s-y(h)).
\]

It and its inverse are also bounded on
(operatorname{Dom}(y)\oplus\mathbf C) with the product graph norm.

Therefore the stable reduction

\[
LDR=I_H\oplus(-f)
\]

remains valid for an honest closed boundary observer.

## Consequence

Unboundedness of the observer on the ambient (H)-norm is not enough to
block Gaussian elimination. Passing to its natural graph domain restores the
triangular equivalence whenever the readout itself is genuinely defined.

The bordered construction therefore has only two outcomes:

1. (u\in\operatorname{Dom}(y)). The ordered readout is honest, and the
   bordered complex collapses stably to the scalar section.
2. (u\notin\operatorname{Dom}(y)). The expression (y(u)) is not an honest
   operator pairing, so a renormalized scalar requires additional typed
   boundary data before the bordered operator exists.

There is no third outcome in which the ordinary pairing is defined but graph
topology alone prevents the elimination.

## RH implication

The canonical border supplies a clean zero-to-state dictionary but not an
independent RH mechanism. If the completed theta section is an honest
source-to-observer pairing, the border is stably just that scalar. If it is a
renormalized pairing, the primitive, square, seam, and archimedean currents
must be retained as part of a larger boundary relation.

The only live extension is therefore not a larger ordinary border. It is a
typed renormalized boundary system whose scalar readout is the coherent sum
of channels that do not exist separately on one common operator domain.

That extension must come with its own source-derived conservation or
passivity law. Otherwise it again reduces to a presentation of the completed
scalar kernel.

## Control-theory translation

For a regular boundary control system, the bordered Rosenbrock matrix and its
transfer function have the same invariant-zero content after graph-domain
elimination. New structure appears only in singular systems where feedthrough
or boundary pairing requires a regularization vessel.

The theta problem is therefore typed as a singular boundary-system
realization problem, not an ordinary finite-dimensional observability
problem.

## Falsifier

Any proposed graph-domain obstruction must provide (u\in\operatorname{Dom}(y))
while showing that translation by (u) fails to preserve that linear graph
domain. This contradicts linearity. A genuine obstruction must instead alter
the domain type, the completion topology, or the meaning of the scalar
pairing.

