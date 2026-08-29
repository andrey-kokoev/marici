# Minimal coefficient-free Landau action cannot select small CP: WP1024

## Question

Can the smallest CP-even invariant action select the observed small nonzero
oriented volume without inserting a small coefficient?

## Normalized quotient variable

Use the exact WP1023 bound to define

\[
x=108J^2,qquad 0\le x\le1.
\]

This is dimensionless and descends under the full weak-basis group. Consider
the minimal Landau family

\[
V(x)=\alpha x+\beta x^2.
\]

## Primitive coefficient-free audit

After removing an irrelevant common scale, take the primitive bounded choices
(eta=1) and (alpha\in\{-1,0,1\}). Their global minima on ([0,1])
are respectively

\[
x=1/2,qquad x=0,qquad x=0.
\]

Primitive linear actions add only (x=0) or (x=1). Thus the complete
minimal coefficient-free selected set is

\[
\{0,1/2,1\}.
\]

Every fitted sheet instead obeys

\[
0<x<\frac{27}{250000}.
\]

Zero of the 1,210 sheets survives.

## Small-ratio obstruction

For general nonzero (eta), an interior stationary point satisfies

\[
x_*=-\frac{\alpha}{2\beta}.
\]

Matching a fitted sheet therefore requires

\[
\frac{\alpha}{\beta}=-2x_{\rm fit},
\]

whose magnitude is below (27/125000). The Landau action can reproduce the
small invariant only after receiving a comparably small source ratio. It does
not explain that ratio.

## Selector and instrument typing

Each action defines a presentation-independent mathematical selector, and
the CKM/Jarlskog readout measures (x). No declared source-local field action
or preparation instrument realizes this quotient-level potential. Even if
one were supplied, the primitive coefficient-free predictions are false.

## Smallest exact falsifier

The fitted interval (0<x<27/250000) is disjoint from
({0,1/2,1}). The exact half-maximal stationary point is the deliberate
nonzero contrast: mathematically sound and phenomenologically excluded.

## Claim boundary

This closes the minimal quadratic Landau action in (x) with primitive
coefficient choices. It does not exclude higher-degree, nonpolynomial, or
independently source-derived actions. Such successors must explain their
small dimensionless ratio rather than encode it. No implicit time or causal
relaxation is asserted.

## Disposition

The frontier moves upstream again. Before another invariant potential is
credible, derive a small dimensionless ratio from independent source
structure and then test whether it couples to the oriented-volume invariant
through a local, radiatively closed, instrumented operation.

Verification: uv run --with sympy python
research/flavor/checkers/wp1024_minimal_landau_small_cp_no_go.py.
