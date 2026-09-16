# The positive theta chart certifies boundary mean--variance on the entire interval from three tenths to one half

## Certified theta enclosure

The theta-box checker now includes rigorous bounds for both omitted directions:

1. the theta-series tail \(n>N\);
2. the integration tail \(v>U\).

The checker is

`research/voevodsky/checkers/arb_theta_boundary_box_probe.py`,

and its output is

`research/voevodsky/results/arb-theta-boundary-box-probe.json`.

It uses \(N=5\), \(U=3\), and directed Arb integration.

## Tail bounds

For derivative order \(k=0,1,2\), the omitted mass is bounded by positive elementary majorants. At the chosen cutoffs, the resulting error budgets are approximately

\[
8.82
\times
10^{-48},
\]

\[
1.99
\times
10^{-50},
\]

and

\[
8.99
\times
10^{-53},
\]

for \(\Xi,\Xi',\Xi''\), respectively.

These tails are negligible compared with interval dependency; nevertheless they are included in the final directed balls.

## Certified boxes

The checker tests the four boxes

\[
[0.1,0.2],
\qquad
[0.2,0.3],
\qquad
[0.3,0.4],
\qquad
[0.4,0.5].
\]

The two upper boxes have strictly positive Arb lower bounds for

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
\right].
\]

Therefore

\[
\boxed{
G(x)>0
\qquad
(0.3\le x\le0.5).
}
\]

This is a whole-interval theorem, not a point scan.

The lower boxes remain indeterminate at radius \(0.05\); they are not negative.

## Combined analytical region

The probability identity already proves

\[
G(x)>0
\]

for

\[
x\ge1/2.
\]

The interval certificate joins that theorem continuously and extends the rigorously controlled boundary region to

\[
\boxed{
x\ge0.3.}
\]

In the original coordinate

\[
s
=
\frac12+x,
\]

this gives boundary monotonicity for

\[
\boxed{
s\ge0.8.}
\]

The reflected exterior follows from the completed symmetry convention.

## Remaining interval

The unresolved positive centered boundary interval is now

\[
0<x<0.3.
\]

The two coarse boxes there fail only because interval dependency dominates the small cubic margin near the center.

The next subdivision should use:

1. narrower theta boxes on \([\varepsilon,0.3]\);
2. the directed central Taylor model for \([0,\varepsilon]\);
3. the normalized quantity \(G(x)/x^3\) in the near-center chart.

## Scope

This result proves scalar real-boundary Loewner monotonicity only. It does not prove the complex upper-half-plane Pick inequality or RH.

It does, however, force any real-boundary failure into the compact interval

\[
0<x<0.3.
\]

## Disposition

With explicit theta and integration tails attached, Arb certifies

\[
\boxed{
G(x)>0
\text{ on }[0.3,0.5].
}
\]

Together with the analytic exterior argument, the real-boundary gate is closed for every \(x\ge0.3\).
