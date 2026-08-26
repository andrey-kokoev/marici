# Three-point spacing optimum (WP375)

## Frozen design benchmark

WP374 proves rank for every positive spacing but does not establish robust
conditioning. Freeze the dimensionless equal mass-width benchmark
\(L=\Omega=1\), remove the irrelevant positive coupling scale, and assume
setting-independent record covariance and cost.

The magnitude of WP374's reduced determinant becomes

\[
D(d)=
\frac{d^3(3d^3+11d^2+12d+6)}
{(d^2+2d+2)^2(2d^2+2d+1)^2},
\qquad d>0.
\]

It obeys

\[
\lim_{d\to0^+}D(d)=0,
\qquad
\lim_{d\to\infty}D(d)=0.
\]

Both a collapsed scan and an excessively separated scan lose information
volume.

## Unique finite optimum

The derivative numerator factors as

\[
-d^2Q(d),
\]

with

\[
Q(d)=12d^7+66d^6+108d^5+33d^4-126d^3-200d^2-132d-36.
\]

In descending order, the coefficients of \(Q\) have exactly one sign change.
Descartes' rule therefore permits exactly one positive root because
\(Q(1)=-275\) and \(Q(3/2)=3339/4\) prove existence. Since \(D\) is positive
and vanishes at both boundaries, this root is the unique global maximum. Its
numerical location is approximately

\[
d_\star\simeq1.270374202.
\]

The decimal is a locator, not the authority-bearing result; the exact design
is the unique positive root of \(Q\), bracketed by 1 and \(3/2\).

## Scope and disposition

This is a D-optimal spacing result only for the frozen equal mass-width,
constant-covariance, equal-cost benchmark. It is not a universal detector
setting and must not be fitted to flavor data. Width ratio, count-rate changes,
control cost, and background covariance will move the optimum and require a
new predeclared design calculation.

WP375 strengthens rank into a finite robustness prescription while leaving
selector authority unchanged. The smallest exact falsifier of monotonic
spacing improvement is the large-spacing limit \(D(d)\to0\).

Run `uv run --with sympy python
research/flavor/checkers/wp375_three_point_spacing_optimum.py` to regenerate
the exact result.
