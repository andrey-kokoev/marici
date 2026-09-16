# Adaptive theta boxes certify boundary mean--variance from 0.085 to infinity

## Refined subdivision

The tail-certified theta checker was refined on the lower centered interval.

It now uses width-

\[
0.005
\]

boxes between \(0.05\) and \(0.15\), followed by the previously certified wider boxes up to \(0.5\).

The checker and durable result remain:

- `research/voevodsky/checkers/arb_theta_boundary_box_probe.py`
- `research/voevodsky/results/arb-theta-boundary-box-probe.json`

## Result

Every listed box beginning at approximately

\[
x=0.085
\]

has a strictly positive Arb lower bound for

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

The positive boxes overlap, so they form one certified interval:

\[
\boxed{
G(x)>0
\qquad
(0.085\le x\le0.5).
}
\]

The analytical mean--variance argument proves the same sign for \(x\ge0.5\). Therefore

\[
\boxed{
G(x)>0
\qquad
(x\ge0.085).
}
\]

In the original coordinate \(s=1/2+x\), boundary monotonicity is certified for

\[
\boxed{
s\ge0.585.}
\]

## Indeterminate boxes

The boxes below approximately \(0.085\) are indeterminate at width \(0.005\). Their Arb lower bounds are negative because interval dependency exceeds the cubic positive margin.

No negative point or negative certified interval was found.

## Remaining central interval

The unresolved interval is now

\[
0<x<0.085.
\]

Direct theta boxes become inefficient there because

\[
G(x)
\sim

g_0x^3,
\qquad

g_0
\approx
0.369828580243844611.
\]

The correct chart is the normalized analytic function

\[
\widetilde G(x)
=
\frac{
G(x)
}
{
x^3
},
\]

with its removable value

\[
\widetilde G(0)
=

g_0>0.
\]

## Next certification step

Use the existing directed centered Xi jet to construct a Taylor model for \(\widetilde G\), then certify its remainder on an initial interval \([0,\varepsilon]\). Moderate theta boxes can cover \([\varepsilon,0.085]\).

A practical split is:

1. Taylor chart on \([0,0.01]\);
2. narrower theta boxes on \([0.01,0.085]\);
3. current certified theta chart on \([0.085,0.5]\);
4. analytic exterior for \([0.5,\infty)\).

## Scope

This remains a scalar real-boundary result. It does not prove the complex Pick inequality.

## Disposition

Tail-certified positive theta integration has reduced the possible real-boundary failure region to

\[
\boxed{
0<x<0.085.
}
\]

All larger positive centered coordinates are rigorously controlled.
