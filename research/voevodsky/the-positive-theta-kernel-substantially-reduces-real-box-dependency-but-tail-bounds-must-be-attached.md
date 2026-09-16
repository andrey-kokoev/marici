# The positive theta kernel substantially reduces real-box dependency, but tail bounds must be attached

## Probe

The checker

`research/voevodsky/checkers/arb_theta_boundary_box_probe.py`

uses the rescaled Riemann kernel

\[
\Psi(v)
=
2\Phi(2v)
=
\sum_{n\ge1}
\left[
4\pi^2n^4e^{9v}
-
6\pi n^2e^{5v}
\right]

e^{-\pi n^2e^{4v}}
\]

so that

\[
\Xi(x)
=
\int_0^\infty
\Psi(v)
\cosh(xv)
\,dv.
\]

It simultaneously encloses the truncated integrals for

\[
\Xi(x),
\qquad
\Xi'(x),
\qquad
\Xi''(x)
\]

on real \(x\)-boxes.

## Preliminary result

Using only five theta terms and the finite integration interval \(0\le v\le3\), Arb can already retain positive information on boxes of radius \(0.05\) near the upper part of the centered interval.

This is many orders of magnitude wider than boxes obtained by direct interval evaluation of

\[
s(s-1)
\Gamma(s/2)
\zeta(s).
\]

The lower boxes remain indeterminate at that coarse width because \(G(x)\) vanishes cubically at the center.

## Why the result is conditional

The probe has not yet attached:

1. the theta-series tail \(n>N\);
2. the integration tail \(v>U\).

Its output is therefore explicitly marked

`interval_certified: false`.

No sign claim is made from the probe.

## Elementary tail architecture

Both missing tails admit source-independent positive bounds.

For \(0\le x\le1/2\) and derivative order \(k=0,1,2\),

\[
\left|
\partial_x^k
\cosh(xv)
\right|
\le
v^k

e^{v/2}.
\]

Dropping the negative term in each positive theta summand gives

\[
\Psi_n(v)
\le
4\pi^2n^4

e^{9v}

e^{-\pi n^2e^{4v}}.
\]

For the integration tail \(v=U+w\), convexity gives

\[

e^{4(U+w)}
\ge

e^{4U}
(
1+4w
).
\]

Hence

\[
\Psi_n(U+w)

e^{(U+w)/2}
\le
4\pi^2n^4

e^{(19/2)U-
\pi n^2e^{4U}}

e^{-r_{n,U}w},
\]

where

\[
r_{n,U}
=
4\pi n^2

e^{4U}
-
\frac{19}{2}.
\]

The moments needed for derivatives are elementary:

\[
\int_0^\infty

e^{-rw}
\,dw
=
\frac1r,
\]

\[
\int_0^\infty
(
U+w
)

e^{-rw}
\,dw
=
\frac U r
+
\frac1{r^2},
\]

\[
\int_0^\infty
(
U+w
)^2

e^{-rw}
\,dw
=
\frac{U^2}{r}
+
\frac{2U}{r^2}
+
\frac2{r^3}.
\]

For the series tail, use

\[

e^{4v}
\ge
1+4v
\]

to obtain

\[
\Psi_n(v)

e^{v/2}
\le
4\pi^2n^4

e^{-\pi n^2}

e^{-r_{n,0}v}.
\]

Summing these explicit bounds over \(n>N\) gives a rapidly convergent certified tail. The remaining infinite \(n\)-sum can be bounded geometrically because consecutive terms have ratio dominated by

\[
\left(
1+
\frac1n
\right)^4

e^{-\pi(2n+1)}.
\]

## Next implementation step

Attach these two positive error budgets independently to the Arb enclosures of \(\Xi,\Xi',\Xi''\). Then rerun adaptive subdivision with:

1. the directed central Taylor model near zero;
2. theta boxes in the interior;
3. the analytic exterior inequality at and above \(x=1/2\).

## Disposition

The theta chart is numerically suitable for interval certification and has explicit elementary tails. The remaining work is implementation of those tail budgets; direct zeta-product boxes should be abandoned for this task.
