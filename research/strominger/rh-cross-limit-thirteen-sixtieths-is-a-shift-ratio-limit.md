# Cross limit thirteen sixtieths is a shift-ratio limit

## Question

What exact staircase asymptotic is equivalent to

\[
n^2\Theta_n\to\frac{13}{60}?
\]

For the source vector

\[
\mathbf s_0=\left(1,\frac54,\frac32,\frac74\right),
\]

define

\[
R_m=
\frac{S_m(\mathbf s_0+1)^2}
{S_m(\mathbf s_0)S_m(\mathbf s_0+2)}.
\]

The condensation cross ratio satisfies exactly

\[
\Theta_n=
\frac{q_0(\mathbf s_0)}{q_{n-1}(\mathbf s_0)}R_{n-1},
\]

with

\[
q_0(\mathbf s_0)=rac{105}{32},
\qquad
q_{n-1}(\mathbf s_0)\sim n^4.
\]

Therefore

\[
n^2\Theta_n\to\frac{13}{60}
\]

is equivalent to

\[
\frac{R_m}{m^2}	o
\frac{13/60}{105/32}
=rac{104}{1575}.
\]

The factor \(m^2\) shows that the common parameter shift has a nontrivial second discrete curvature in the leading staircase free energy.

## Disposition

Resolve the cross-limit conjecture to the exact shift-ratio theorem above. The next leaf is `quarter-staircase-shift-ratio-104-1575`: prove the limit using an LU factorization, vector equilibrium, or a parameter-uniform determinant asymptotic.

## Claim boundary

This equivalence does not prove either limit. Pointwise asymptotics for one parameter vector are insufficient; the ratio requires uniform control across \(\mathbf s_0,\mathbf s_0+1,\mathbf s_0+2\).
