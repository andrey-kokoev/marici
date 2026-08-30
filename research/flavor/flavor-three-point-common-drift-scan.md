# Three-point common-drift scan (WP374)

## Minimal context count

Allow one unknown common-mode offset \(\eta(1,1)^T\) shared across a scan and
an independent differential offset \(\delta_j(1,-1)^T\) at every setting.
There are two pole parameters, one common nuisance, and one differential
nuisance per setting. Three settings are dimensionally minimal:

\[
L,
\qquad
L+d,
\qquad
L+2d,
\qquad d>0.
\]

They supply six records for the six local parameters
\((L,\Omega,\eta,\delta_0,\delta_1,\delta_2)\).

## Exact common-channel reduction

The free differential channels solve the three \(\delta_j\). Pole information
therefore lies in the three common-channel sums

\[
f(z)=-\frac{c(z+\Omega)}{z^2+\Omega^2}+2\eta.
\]

Subtract the first setting from the other two to eliminate \(\eta\). The
resulting two-by-two Jacobian for \((L,\Omega)\) has determinant

\[
-\frac{8\Omega c^2d^3P(L,\Omega,d)}
{(L^2+\Omega^2)^2((L+d)^2+\Omega^2)^2
((L+2d)^2+\Omega^2)^2},
\]

where

\[
\begin{aligned}
P={}&3L^4+12L^3d+6L^2\Omega^2+15L^2d^2
+12L\Omega^2d\\
&+6Ld^3+3\Omega^4+7\Omega^2d^2.
\end{aligned}
\]

All eight monomials are positive. The reduced determinant never vanishes on
the admitted domain.

The common/difference transformation is invertible. Its nuisance block is
diagonal with entries 2, so the original six-by-six record Jacobian is also
full rank. The exact reconstructed determinant is positive and equals minus
twice the reduced determinant.

## Boundary

Three source-supported contexts therefore repair one shared common offset plus
arbitrary differential drift. Two settings are insufficient by parameter
count for this nuisance grammar. If common offsets drift independently at all
three settings, eight parameters act on six records and a kernel remains.

This is a threshold-identification theorem, not flavor selection. It depends
on freezing an equally spaced three-setting scan independently of the desired
answer and on validating that the common offset is actually shared.

The smallest exact falsifier is \(d=0\), which kills the determinant with a
cubic spacing factor. The remaining instrument gate is physical realization
of three calibrated mass settings and a background model justifying the
shared common component.

Run `uv run --with sympy python
research/flavor/checkers/wp374_three_point_common_drift_scan.py` to regenerate
the exact result.
