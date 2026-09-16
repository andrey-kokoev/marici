# High-precision scouting finds positive boundary mean--variance margin throughout the centered interval

## Target

For

\[
0<x<
\frac12,
\]

define

\[
m(x)
=
\frac{
\Xi'(x)
}
{
\Xi(x)
},
\]

\[
m'(x)
=
\frac{
\Xi''(x)
}
{
\Xi(x)
}
-
m(x)^2,
\]

and

\[
G(x)
=
(
1+4x^2
)
m(x)
-
x(
1-4x^2
)
m'(x).
\]

Boundary Loewner monotonicity is equivalent to

\[
G(x)
\ge0.
\]

## Scout

A new 80-decimal-digit checker evaluates the completed Xi function directly:

`research/voevodsky/checkers/scout_xi_boundary_mean_variance.py`

It uses:

1. 120 logarithmically spaced points approaching the branch point;
2. 400 approximately uniform points across \((0,1/2)\);
3. direct high-precision differentiation of the completed Xi expression;
4. an independent small-\(x\) scan of \(G(x)/x^3\).

The durable result is:

`research/voevodsky/results/xi-boundary-mean-variance-scout.json`

## Result

All 520 sampled points were positive.

The smallest raw value occurred at

\[
x
\approx
6.1687345
\times
10^{-13},
\]

where

\[
G(x)
\approx
8.68138
\times
10^{-38}.
\]

This tiny value is expected from the cubic branch-point vanishing and is not evidence of a near interior sign change.

The normalized ratio stabilizes rapidly:

\[
\frac{
G(x)
}
{
x^3
}
\longrightarrow
0.369828580243844611\ldots
\]

as \(x\downarrow0\).

Thus the first nonzero branch-point coefficient is comfortably positive.

## Interpretation

The scan suggests:

1. no boundary monotonicity failure in the centered interval;
2. the smallest unnormalized margin occurs only because \(G(0)=0\) to cubic order;
3. the natural central quantity for interval certification is \(G(x)/x^3\), not \(G(x)\);
4. the exterior theorem at \(x\ge1/2\) and central positivity appear compatible without a narrow transition layer.

## Scope boundary

The computation is not interval certified. It uses high-precision floating arithmetic and numerical differentiation.

Therefore it proves neither

\[
G(x)
\ge0
\]

on the continuum nor any RH-equivalent interior Pick property.

It is reconnaissance for a one-dimensional interval proof.

## Certification plan

A rigorous proof should use three charts.

### Central chart

Use the existing directed Xi logarithmic-derivative jet and certify

\[
G(x)
=
x^3
(

g_0
+

g_1x^2
+
\cdots
)
\]

with

\[
g_0
>0
\]

and an explicit Taylor remainder on \([0,\varepsilon]\).

### Interior chart

Use Arb complex balls for \(\Xi,\Xi',\Xi''\) or a box-valued theta integral on adaptive intervals

\[
[
\varepsilon,
1/2-
\varepsilon_1
].
\]

### Exterior seam

Near \(x=1/2\), use the exact identity

\[
G(1/2)
=
2m(1/2)
>0
\]

and interval continuity. For \(x\ge1/2\), positivity is already analytical.

## Relation to the full Pick gate

Boundary monotonicity is necessary for the Loewner/Pick property but not sufficient for matrix monotonicity or positivity in the upper half-plane.

A successful interval proof would nevertheless exclude real-boundary slope failure and force any hostile Pick obstruction into a genuinely interior complex configuration.

## Disposition

High-precision reconnaissance supports the conjecture

\[
\boxed{
G(x)>0
\quad
(0<x<1/2).
}
\]

The next task is interval certification of this one-dimensional statement, using the normalized central quotient \(G(x)/x^3\).
