# Euler cap degeneracies recover both magnetic support thresholds

For the stable top-jet direction

\[
\phi_a=x^{-a-g}(1+x)^g,
\]

the two universal boundary operators act by

\[
A_-\phi_a=(1+x)(1-Q-a-g)\phi_a,
\]

\[
A_+\phi_a=(1+x)(1+Q-a-g)\phi_a,
\qquad Q=q+2.
\]

## Minus-spine theorem candidate

For \(a\ge0\), \(g\ge2\), and \(Q\ge3\),

\[
1-Q-a-g\neq0.
\]

Thus the minus top observation never degenerates at an admissible depth. This
is the source explanation for the exact bounded fact that every minus column
is retained by consecutive-depth Hall elimination.

On the top direction, inverse descent is division by the affine depth factor
\(a+g+Q-1\). In the depth-generating variable this is the regular solution of

\[
(y\partial_y+g+Q-1)u=f,
\]

namely

\[
u(y)=y^{-(g+Q-1)}
\int_0^y s^{g+Q-2}f(s)\,ds.
\]

This is the explicit Euler inverse that replaces opaque elimination along the
minus spine.

## Plus degeneration

The plus top observation vanishes at

\[
a_\ast=Q-g+1=q-g+3.
\]

This zero does not automatically remove a plus pivot. Exact Hall elimination
over all \(135\) cases

\[
2\le g\le10,\qquad 1\le q\le15
\]

shows two further source conditions.

First, the zero becomes an actual Hall hole precisely when

\[
q\ge g+2,
\]

equivalently

\[
a_\ast\ge5=\beta+1
\]

for the native source \(\beta=4\). Below the source-window boundary, lower jet
components repair the vanished top observation.

Second, the two distinguished threshold-hole packets are

\[
\{a_\ast\},
\qquad
g+2\le q\le2g,
\]

and

\[
\{a_\ast-1,a_\ast\},
\qquad
q\ge2g+1.
\]

The second threshold is exactly

\[
2g+1=2g+\beta-3,
\]

the high support-separation boundary of the native two-wedge law.

## Interpretation

The finite plus cap can have further collision holes. The two holes singled
out here are controlled by two typed events:

1. an Euler top-observation zero crossing beyond the finite source window;
2. activation of the second boundary observation at the high two-wedge
   support-separation locus.

Thus the Euler atlas identifies two canonical coordinates within the Hall
matroid. It does not identify total Hall deficiency with cokernel width. The
first coordinate records failure of the plus top observation after source
repair is exhausted. The second is aligned with separation of the dual
boundary supports, without yet proving that both belong to one invariant.

## Status

The Euler factors and inverse formula are exact. The native \(135\)-case
census supports the finite-cap normal form and permits additional internal
collision holes; it does not support the displayed packets as exhaustive.
The proof target is to filter
the plus column by the finite source window and show:

- lower jets restore the \(A_+\) zero exactly for \(a_\ast\le\beta\);
- one primitive relation remains for
  \(\beta+1\le a_\ast<g+\beta\);
- a second primitive relation appears at
  \(q=2g+\beta-3\).

This would derive the finite cap and the two-wedge boundary from one filtered
Euler-resolvent presentation.

## Beta-deformed global audit

The prediction was tested with rank-invariant exact elimination for

\[
2\le\beta\le8,\qquad 2\le g\le10,qquad 1\le q\le15.
\]

All \(945/945\) cases satisfy the global hole law above. The first hole occurs
at \(q=g+\beta-2\), and the adjacent second hole occurs at
\(q=2g+\beta-3\). Exact primitive circuit extraction verifies the full
column relations, not merely vanishing of their top Euler coordinates.

A discarded one-pass sparse eliminator produced a false counterexample because
its pivot rows were not monotone. The corrected pivot-map normal form reduces
by row identity and therefore computes column dependence independently of
pivot discovery order.

Counterfactual \(\beta\neq4\) remains diagnostic rather than a claim about a
native magnetic sector. Within that diagnostic family, however, the cap law
and two-wedge law have identical threshold parameters.
