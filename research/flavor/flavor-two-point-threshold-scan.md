# Two-point threshold scan (WP372)

## Bounded scan design

WP371 found a one-dimensional kernel when one fixed differential background
is fitted together with \((L,\Omega)\) at one threshold setting. Use two known
mass settings

\[
L_0=L,
\qquad
L_1=L+d,
\qquad d>0,
\]

and assume the same additive differential background \(\delta(1,-1)^T\) is
shared across both records.

Up to the known nonzero factor \(c=\mu^2/2\), the threshold coordinates at
mass setting \(z\) are

\[
u(z,\Omega)=
\begin{pmatrix}
-cz/(z^2+\Omega^2)\\
-c\Omega/(z^2+\Omega^2)
\end{pmatrix}.
\]

Stacking the two records gives four observations for the three local
parameters \((L,\Omega,\delta)\).

## Exact rank certificate

One three-by-three Jacobian minor factors as

\[
-\frac{c^2dP(L,\Omega,d)}
{(L^2+\Omega^2)^2((L+d)^2+\Omega^2)^2},
\]

where

\[
\begin{aligned}
P={}&2L^3+2L^2\Omega+5L^2d+2L\Omega^2+2L\Omega d\\
&+4Ld^2+2\Omega^3+3\Omega^2d+d^3.
\end{aligned}
\]

Every term is positive on the admitted domain. The stacked Jacobian therefore
has rank three everywhere for \(L,\Omega,d,c>0\). Two distinct source-supported
scan points remove the fixed-background kernel exactly.

Calibrated detector confusion with positive contrast acts by an invertible
two-channel matrix at each scan point and preserves this rank. It changes
conditioning, not contextual equivalence.

## Failure modes and disposition

At \(d=0\), the determinant vanishes: repeated measurements at one setting do
not create a second context. If the background is not shared across scan
points, the three-parameter theorem does not apply. Likewise, choosing the
second setting after inspecting the desired answer would not be a
source-authorized scan design.

This is a progressive physical-instrument result for threshold source
identification. It still neither selects a numerical flavor packet nor repairs
the projection from `physical16` to \(J^2\). Its smallest exact falsifier is
the collapsed scan \(d=0\). The remaining gate is a calibrated mechanism that
sets the two mediator masses and validates background stability across them.

Run `uv run --with sympy python
research/flavor/checkers/wp372_two_point_threshold_scan.py` to regenerate the
exact result.
