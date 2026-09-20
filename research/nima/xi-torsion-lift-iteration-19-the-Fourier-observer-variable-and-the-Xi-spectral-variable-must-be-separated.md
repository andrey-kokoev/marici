# Xi-torsion lift iteration 19: the Fourier observer variable and the Xi spectral variable must be separated

## Notational correction

The translated-theta recovery theorem uses two different variables that earlier
iterations denoted by the same letter:

- `zeta`: the Xi/Evans spectral parameter;
- `xi`: the Fourier variable dual to common-history time.

For a spectral coefficient section `c(zeta)`, the raw history satisfies

\[
\widehat{J_\theta c}(\zeta,\xi)
=
\widehat\Phi(\xi)
F_c(\zeta,\xi),
\]

where

\[
F_c(\zeta,\xi)
=
\sum_\lambda a_\lambda
\left(c_\lambda^+(\zeta)e^{i\xi L_\lambda}
+c_\lambda^-(\zeta)e^{-i\xi L_\lambda}\right).
\]

The two-horizontal-line observer acts in complexified `xi`, not in `zeta`.

## Correct strictness theorem

For every compact spectral set `K` and every spectral jet order `j`, define

\[
S_{K,j,R}(F)
=
\sup_{\zeta\in K}
\max_\pm\sup_{x\in\mathbb R}
\left|
\partial_\zeta^jF(\zeta,x\pm iR)
\right|.
\]

The Bohr extraction estimate applies pointwise in `zeta` and uniformly on `K`:

\[
q_{K,j,\delta}(c)
\le
K_{R-\delta-1/2}S_{K,j,R}(F_c),
\qquad R>\delta+\frac32.
\]

The converse estimate follows from the stronger source seminorm. Hence the
common-history codiagonal is strict in a graph category that is:

- compact-open/Silva in the Xi variable `zeta`;
- two-line Fourier--Köthe in the observer variable `xi`.

## Correct horizontality statement

Because `J_theta` is independent of `zeta`,

\[
\partial_\zeta J_\theta c
=J_\theta(\partial_\zeta c).
\]

Thus it is horizontal for the trivial spectral connection, and likewise for a
declared coefficient connection if its label term is intertwined explicitly.

By contrast,

\[
\partial_\xi F_c
\]

multiplies coefficients by `+-iL_lambda`. This proves regularity in the observer
variable; it is not the Xi spectral connection. Iteration 1 conflated these two
claims.

## Consequence for H-border

The endpoint formula

\[
E_{e^{\zeta\cdot},\delta_b}(\zeta)
=
\frac12e^{\zeta b}-\frac12e^{\zeta(2a-b)}
\]

uses the Xi spectral variable itself as the exponential-sum variable. Its Bohr
observer, when available, runs vertically in `zeta`, unlike the theta recovery
observer, which runs in `xi`.

Therefore the two recovery theorems do not define one common analytic graph by
mere renaming. A bridge must relate spectral dependence of the bordered packet
to Fourier dependence of the common history.

## Revised status of objective 1

Objective 1 is proved in the explicit two-variable graph category above,
conditional only on retaining the deconvolved Fourier observer. Its
horizontality is spectral compact-open horizontality, while its coefficient
recovery occurs in the independent Fourier variable.

This correction further confirms that objective 2 is not a consequence of
objective 1: `H_border` has a separate spectral-exponential recovery mechanism.

## Final remaining audit

The last iteration should state the strongest theorem actually established and
separate it from the false “equivalently” clause, so that no Xi/Haar conclusion
is attributed to a collision of the variables `zeta` and `xi`.