# Order-two Stieltjes divided-difference bridge

## Question

How does the prior order-two Stieltjes target connect exactly to the compact Hausdorff cones and the single divided-difference constructor?

## Claim boundary

The factorial moments, compact support coordinate, three cone factorizations, and generating kernel are derived. Positivity of the source measure or an arithmetic J-fraction remains open.

## Source target

The prior Xi packet proposes

\[
H'(x)=
\int_{1/4}^{\infty}
\frac{d\nu(a)}{(x-1/4+a)^2},
\qquad d\nu(a)\geq0.
\]

Write

\[
r=a-\frac14\geq0.
\]

Then

\[
H'(x)=
\int_0^\infty
\frac{d\widetilde\nu(r)}{(x+r)^2}.
\]

## Factorial moments

Define

\[
q_k(x)=
\frac{(-1)^kH^{(k+1)}(x)}{(k+1)!}.
\]

Differentiating the order-two kernel gives

\[
q_k(x)=
\int_0^\infty
\frac{d\widetilde\nu(r)}{(x+r)^{k+2}}.
\]

Set

\[
y=\frac1{x+r}.
\]

For fixed positive \(x\), this lies in

\[
0<y\leq\frac1x.
\]

After absorbing \(y^2\) into the measure, \((q_k(x))\) is a compact moment sequence on \([0,1/x]\).

## Three cone families

The support interval yields

\[
(q_{i+j})\geq0,
\]

\[
(q_{i+j+1})\geq0,
\]

and

\[
\left(
\frac{q_{i+j}}x-q_{i+j+1}
\right)\geq0.
\]

These are Gram forms for multiplication by

\[
1,
\qquad y,
\qquad \frac1x-y.
\]

The GNS multiplication operator satisfies

\[
0\leq Y_x\leq\frac1x.
\]

Therefore

\[
Z_x=xY_x
\]

is a positive contraction. The compact Hausdorff contraction has now been identified directly inside the order-two Stieltjes chart.

## One divided-difference generator

Taylor expansion gives

\[
\sum_{k\geq0}q_k(x)t^k
=
\frac{H(x)-H(x-t)}{t}.
\]

Thus all factorial moments and all three matrix cones are restrictions of one divided-difference kernel.

This is more precise than treating the matrices as unrelated positivity tests. A source-positive factorization of the divided difference would generate every moment cone simultaneously.

## Relation to the heat chart

The inverse Laplace density of the order-two kernel is a rate-weighted, quarter-shifted heat density. Under the reported decay and support conditions, the transform is invertible. Consequently the Stieltjes chart does not bypass the heat positivity problem.

Its advantage is representational:

- compact support after the coordinate \(y=(x+r)^{-1}\);
- a bounded positive contraction \(Z_x\);
- Hankel/localizing matrices;
- Jacobi and continued-fraction coordinates;
- one divided-difference generator.

## Exact fixture

For positive atoms at \(r=0,2\), the checker verifies:

- seven factorial-moment identities;
- exact factorizations of all three matrix cones;
- nonnegative principal minors at rational \(x=3/2\);
- six coefficients of the divided-difference series;
- the scaled contraction support bound.

## Remaining arithmetic gate

The representation with \(d\nu\geq0\) is the target, not a premise available in an RH proof. The required constructor must start from the explicit Xi-derived divided difference and produce either:

- a source Gram factor for all three cones;
- a Jacobi operator with spectrum in \([0,1/x]\);
- or a positive J-fraction whose coefficients and convergence are derived from the source.

Numerical Jacobi reconstruction is evidence for a candidate factor, not a proof of positivity at all ranks.

## Disposition

The order-two Stieltjes, finite-difference, Hausdorff, semigroup, and entire-kernel routes now form one invertible family of charts around the same positive contraction. The first unresolved arrow is a source-derived factorization of the Xi divided-difference kernel. No additional heat observer family is needed.

## Verification

- `research/voevodsky/order-two-stieltjes-divided-difference-bridge-v1.json`
- `research/voevodsky/checkers/check_order_two_stieltjes_divided_difference_bridge.py`
- `research/voevodsky/results/order_two_stieltjes_divided_difference_bridge.json`
