# Arb certifies positive boundary mean--variance at 1011 real points

## Certified point test

The checker

`research/voevodsky/checkers/arb_xi_boundary_mean_variance_points.py`

uses the vendored python-flint Arb backend to evaluate

\[
G(x)
=
(
1+4x^2
)
\frac{
\Xi'(x)
}
{
\Xi(x)
}
-
x(
1-4x^2
)
\left[
\frac{
\Xi''(x)
}
{
\Xi(x)
}
-
\left(
\frac{
\Xi'(x)
}
{
\Xi(x)
}
\right)^2
\right]
\]

with directed complex-ball arithmetic.

It evaluates:

1. 999 uniformly spaced decimal points from approximately \(0.0005\) to \(0.4995\);
2. the twelve central points \(10^{-1},\ldots,10^{-12}\).

The Xi value and first two derivatives are produced simultaneously by an order-two `acb_series` evaluation of the completed expression

\[
\xi(s)
=
\frac12
s(s-1)
\pi^{-s/2}
\Gamma(s/2)
\zeta(s),
\qquad
s=
\frac12+x.
\]

## Result

All 1011 Arb balls have strictly positive lower endpoints.

The durable result is

`research/voevodsky/results/arb-xi-boundary-mean-variance-points.json`.

At \(x=10^{-12}\), Arb certifies

\[
G(x)
\in
[3.69828580243844611367600430744628\ldots,
3.69828580243844611367600430744641\ldots]
\times10^{-37}.
\]

This agrees with the high-precision branch-point coefficient

\[
G(x)
\sim
0.369828580243844611\ldots
x^3.
\]

No sampled point is indeterminate or negative.

## What is certified

For each listed decimal input \(x_j\), the statement

\[
G(x_j)>0
\]

is rigorous relative to Arb's special-function implementation.

The result is stronger than floating-point reconnaissance because rounding and special-function evaluation errors are enclosed.

## What is not certified

The checker does not cover intervals between adjacent points. It therefore does not prove

\[
G(x)>0
\qquad
(0<x<1/2).
\]

A continuous sign change between points remains logically possible.

It also does not address the complex interior Pick inequality.

## Interval obstacle

A direct interval evaluation of the completed product

\[
s(s-1)
\Gamma(s/2)
\zeta(s)
\]

suffers substantial dependency inflation, especially near the removable zeta pole at \(s=1\). Preliminary boxes require widths around \(10^{-7}\) near \(x=1/4\) before the naive enclosure becomes sign-definite, which is too inefficient for a whole-interval proof.

The interval implementation should therefore use one of:

1. the positive theta-kernel integral for \(\Xi,\Xi',\Xi''\);
2. an eta-based expression that removes the pole before interval evaluation;
3. Taylor models centered on a moderate number of certified points;
4. the existing directed central Xi jet near \(x=0\).

## Disposition

The real-boundary mean--variance conjecture has now passed both high-precision reconnaissance and 1011 rigorous point evaluations:

\[
\boxed{
G(x_j)>0
\quad
\text{for every certified point }x_j.
}
\]

The remaining real-boundary task is interval coverage, not point accuracy.
