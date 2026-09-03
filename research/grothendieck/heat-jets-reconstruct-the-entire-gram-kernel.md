# Heat jets reconstruct the entire Gram kernel

## Question

What exact conformance cell makes the all-heat-jet and fixed-width translate-Gram observer families equivalent presentations of one source?

## Entire heat--character kernel

For positive `t`, define

\[
\mathcal K(t,z)
=
\langle\mathcal W,e^{-tu^2}e^{izu}\rangle.
\]

The completed source estimates make `K(t,-)` entire. Reflection symmetry makes it even in `z`, and

\[
\partial_t\mathcal K=
\partial_z^2\mathcal K.
\]

Define heat jets

\[
J_k(t)=(-1)^k\partial_t^k\mathcal K(t,0).
\]

Then

\[
\partial_z^{2k}\mathcal K(t,0)
=
\partial_t^k\mathcal K(t,0)
=
(-1)^kJ_k(t),
\]

while odd derivatives vanish.

## Reconstruction identity

The entire Taylor series gives

\[
\mathcal K(t,z)
=
\sum_{k=0}^\infty
\frac{(-1)^kJ_k(t)}{(2k)!}z^{2k}.
\]

Therefore all heat jets at one fixed positive width determine every character value. A Gram observer for a translate packet `I=(a_1,...,a_r)` is obtained by substitution:

\[
G_{I,t}
=
\left[
\sum_{k=0}^\infty
\frac{(-1)^kJ_k(t)}{(2k)!}
(a_i-a_j)^{2k}
\right]_{i,j}.
\]

Conversely, knowing `K(t,z)` for all real `z` determines its derivatives at zero and hence every heat jet. This is the explicit bidirectional comparison between the two observer families.

## Finite Taylor residual

Let

\[
T_m(t,z)=
\sum_{k=0}^m
\frac{(-1)^kJ_k(t)}{(2k)!}z^{2k}.
\]

For `|z|<=rho<R`, Cauchy's estimate gives

\[
|\mathcal K(t,z)-T_m(t,z)|
\le
M_R(t)
\frac{(\rho/R)^{2m+2}}{1-\rho/R},
\]

where

\[
M_R(t)=\max_{|z|=R}|\mathcal K(t,z)|.
\]

Endpoint, gamma, and prime source bounds provide a finite `M_R` on compact positive-width strata. For a rank-`r` packet of diameter at most `rho`, the Gram operator residual is at most `r` times this entry bound.

## Meta-observer cell

The cross-family meta-observer should return:

\[
(t,I,m,J_0,\ldots,J_m,T_m,G_{I,t},
\text{Taylor bound},\text{curvature}).
\]

Completed curvature is zero. A finite record carries both Taylor truncation error and arithmetic prime-cutoff error; these are distinct approximation residuals and their bounds add.

## Boundary

The reconstruction uses all derivative orders. No bounded jet truncation is faithful, and the Taylor cutoff needed for a target error depends on packet diameter and the complex-circle bound `M_R`. This agrees with the prior nonuniformity results.

## Disposition

The common source constructor is the entire heat--character kernel. Heat jets are its germ at zero; translate-Gram observers are its real finite restrictions; shifted Gaussians are its gauged imaginary-character restrictions. Meta-observer coherence is equality of these three pullbacks with typed truncation residuals.
