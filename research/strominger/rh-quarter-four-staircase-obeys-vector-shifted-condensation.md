# The quarter four-staircase obeys vector-shifted condensation

## Question

Does the four-staircase determinant admit the same condensation structure as the half-Weibull two-staircase?

For a parameter vector \(\mathbf s=(s_1,s_2,s_3,s_4)\), define

\[
S_n(\mathbf s)=
\det\left[
\prod_{m=1}^4(s_m+i)_j
\right]_{i,j=0}^{n-1},
\qquad
q_i(\mathbf s)=\prod_{m=1}^4(s_m+i).
\]

Desnanot--Jacobi condensation, followed by extraction of the first Pochhammer factor from shifted columns, gives

\[
S_n(\mathbf s)S_{n-2}(\mathbf s+2)
=
q_{n-1}(\mathbf s)
S_{n-1}(\mathbf s)S_{n-1}(\mathbf s+2)
-q_0(\mathbf s)S_{n-1}(\mathbf s+1)^2.
\]

Here \(\mathbf s+c\) shifts every component by \(c\). The source vector is

\[
\mathbf s_0=\left(1,\frac54,\frac32,\frac74\right).
\]

## Disposition

Resolve the exact recurrence underlying the four-staircase term. The \(13/48\) coefficient is not obtained by discarding the cross minor; its relative size must be controlled.

The next leaf is `quarter-four-staircase-cross-ratio`: determine the asymptotic order and leading coefficient of

\[
\Theta_n=
\frac{q_0S_{n-1}(\mathbf s_0+1)^2}
{q_{n-1}S_{n-1}(\mathbf s_0)S_{n-1}(\mathbf s_0+2)}.
\]

## Claim boundary

The recurrence is exact but nonlinear and subtractive. It does not alone prove a logarithmic free-energy coefficient.
