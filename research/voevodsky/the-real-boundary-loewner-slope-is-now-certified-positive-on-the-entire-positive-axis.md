# The real-boundary Loewner slope is now certified positive on the entire positive axis

## Central chart

Let

\[
Q(t)
=
\frac{G(\sqrt t)}{t^{3/2}}
=
4[4L(t)-(1-4t)L'(t)],
\qquad
L(t)=\frac d{dt}\log\Xi(\sqrt t).
\]

The directed centered Xi jet gives a degree-four polynomial enclosure on

\[
0\le t\le0.085^2=0.007225
\]

with lower endpoint

\[
Q_4(t)
\ge
0.3698199776056205986744622113741\ldots.
\]

## Certified Cauchy remainder

The checker

`research/voevodsky/checkers/arb_normalized_margin_cauchy_circle.py`

covers the circle

\[
|t|=0.5
\]

with 2048 Arb arcs. Reflection \(z\mapsto-z\), which leaves \(t=z^2\) and \(Q\) unchanged, keeps the completed-zeta evaluation on the numerically stable half of the circle.

Arb certifies:

\[
\Xi(\sqrt t)
\ne0
\qquad
(|t|=0.5),
\]

and

\[
|Q(t)|
\le
182.798526287078857421875\ldots
\qquad
(|t|=0.5).
\]

Cauchy's estimate therefore bounds the tail after degree four by

\[
\left|
Q(t)-Q_4(t)
\right|
\le
1.1685122330355422216161
\times10^{-7}
\]

throughout \(0\le t\le0.007225\).

Consequently

\[
Q(t)
\ge
0.3698198607543972951202400497739\ldots
>0.
\]

Since

\[
G(x)=x^3Q(x^2),
\]

this proves

\[
\boxed{
G(x)>0
\qquad
(0<x\le0.085).
}
\]

The durable result is

`research/voevodsky/results/arb-normalized-margin-cauchy-circle.json`.

## Joining the charts

The tail-certified positive-theta boxes prove

\[
G(x)>0
\qquad
(0.085\le x\le0.5).
\]

The analytical tilted-measure argument proves

\[
G(x)>0
\qquad
(x\ge0.5).
\]

The charts overlap at their endpoints. Hence

\[
\boxed{
G(x)>0
\qquad
\text{for every }x>0.
}
\]

At the branch point itself,

\[
G(0)=0,
\]

with positive cubic coefficient.

## Meaning

This closes the scalar real-boundary Loewner monotonicity gate for the endpoint-reduced function. There is no hostile real-boundary slope configuration.

Any failure of the desired Pick property must therefore be genuinely complex-interior or matrix-level; it cannot arise from a negative scalar derivative on the real boundary.

## Scope

This theorem does not by itself prove that the function maps the upper half-plane to itself. Boundary monotonicity is necessary but not sufficient for the full Pick property, and therefore this result does not prove RH.

## Disposition

The real-boundary problem is closed:

\[
\boxed{
(1+4x^2)m(x)-x(1-4x^2)m'(x)>0
\quad(x>0).
}
\]

The next open gate is the genuinely interior coupled theta-kernel inequality.
