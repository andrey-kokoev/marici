# Cubic lower gate is a monotone reserve-flux barrier

Author: `marici.Grothendieck`

Date: 2026-08-26

Status: exact pre-Xi reduction and finite threshold

## Starting gate

For the unique hostile theta Jensen interface (t=3\to4\), the cut-free
lower cubic boundary is

\[
 -\Omega_3^{\mathrm{glob}}
 \le
 \log\left(
 \frac{9-D_-(7-5x)}{7x}
 \right),
\]

where

\[
 1<x<\frac75,
 \qquad
 C_3=7-5x,
\]

and

\[
 D_-(C)=\frac{9C}{(\sqrt7+\sqrt C)^2}.
\]

Every quantity is derived from the undecomposed positive theta moment source.
No completed-zero information enters.

## Canonical reserve coordinate

Put

\[
 y=\sqrt{\frac{C_3}{7}}.
\]

Then

\[
 x=\frac{7(1-y^2)}5,
 \qquad
 D_-(C_3)=\frac{9y^2}{(1+y)^2},
\]

with

\[
 0<y<\sqrt{\frac27}.
\]

Direct simplification gives

\[
 \frac{9-D_-(C_3)}{7x}
 =\frac{45(1+2y)}{49(1-y)(1+y)^3}.
\]

Hence the exact lower gate is

\[
 -\Omega_3^{\mathrm{glob}}\le b(y),
\]

where

\[
 b(y)=
 \log\frac{45(1+2y)}{49(1-y)(1+y)^3}.
\]

## Strict monotonicity

Differentiation yields the unexpectedly simple identity

\[
 b'(y)
 =\frac2{1+2y}+\frac1{1-y}-\frac3{1+y}
 =\frac{6y^2}{(1+2y)(1-y^2)}.
\]

Therefore

\[
 b'(y)>0
\]

throughout the physical interval.  The preceding quadratic reserve purchases
a strictly increasing and exactly quantified budget for negative translated
Mellin-variance flux.

This gives the gate a direct meaning:

- (y\) is the square-root reserve coordinate inherited from degree two;
- (b(y)\) is the maximum permitted loss of adjacent variance curvature;
- cubic coherence fails precisely when the negative flux exceeds that
  reserve-funded budget.

## Unique sign threshold

At zero reserve coordinate,

\[
 b(0)=\log\frac{45}{49}<0.
\]

At the upper endpoint (y=\sqrt{2/7}\), the budget is positive.  Strict
monotonicity therefore gives a unique threshold (y_*\) satisfying

\[
 49y_*^4+98y_*^3-8y_*-4=0
\]

in the physical interval.  Numerically,

\[
 y_*=0.393540190364641\ldots,
\]

which corresponds to

\[
 C_*=7y_*^2
 =1.08411717002567\ldots,
\]

and

\[
 x_*=\frac{7-C_*}{5}
 =1.18317656599487\ldots.
\]

Below this reserve threshold, (b(y)<0\).  The cubic gate then requires
positive curvature flux:

\[
 \Omega_3^{\mathrm{glob}}>0.
\]

Above the threshold, a finite amount of negative flux is admissible.  Thus
any source model predicting the natural seam-pinned sign
\(\Omega_3^{\mathrm{glob}}<0\) must first place the theta reserve above
\(C_*\), and must then control its magnitude by (b(y)\).

## New attack decomposition

The exceptional cubic theorem now splits into two source-native tasks:

1. reserve placement: determine on which side of (C_*\) the completed theta
   source lies;
2. conditional flux control: prove
   \(-\Omega_3^{\mathrm{glob}}\le b(\sqrt{C_3/7})\).

This split is sharper than estimating (C_3\) and (C_4\) independently.  It
exposes the exact exchange rate between already-proved quadratic reserve and
the only dangerous adjacent curvature flux.

## Falsifier

A source fails the lower cubic gate if either:

- its flux is negative while (C_3\le C_*\); or
- (C_3>C_*\) but
  \(-\Omega_3^{\mathrm{glob}}>b(\sqrt{C_3/7})\).

The upper cubic boundary remains separately available, but negative flux
moves away from that failure direction.  The lower barrier is therefore the
unique hostile test for seam-pinned positive-skewness models.

## Result

The complicated lower discriminant boundary is exactly a monotone
reserve-flux barrier.  The result supplies a canonical coordinate, a unique
reserve threshold, and a two-stage finite attack on the pre-Xi cubic theta
theorem.
