# The imaginary-character pullback is uniformly holomorphic on compact strata

## Question

Can the identity

\[
\Theta(t,\xi)=e^{-t\xi^2}\mathcal K(t,-2it\xi)
\]

be interchanged with the gamma integral, infinite prime sum, and parameter derivatives?

## Parameter stratum

Fix

\[
0<t_0\le t\le t_1<\infty,
\qquad
|\operatorname{Re}\xi|\le X,
\qquad
|\operatorname{Im}\xi|\le Y.
\]

All estimates below are uniform on this compact stratum. Arbitrarily large derivative orders are not included in one bound.

## Gamma integral

The shifted Gaussian satisfies

\[
|e^{-t(u-\xi)^2}|
\le
\exp(t_1Y^2)
\exp[-t_0(u-\operatorname{Re}\xi)^2].
\]

The digamma weight grows only logarithmically. Multiplying the majorant by any fixed polynomial in `u-xi`, produced by finitely many `t` or `xi` derivatives, remains integrable uniformly on the stratum. Dominated holomorphic convergence therefore permits:

- entire continuation in `xi`;
- differentiation under the gamma integral;
- the imaginary-character substitution.

## Prime sum

For `L=log n`, the shifted prime terms and their derivatives are bounded by a constant times

\[
\frac{\Lambda(n)}{\sqrt n}
(1+L)^d
\exp\!\left[-\frac{L^2}{4t_1}+YL\right]
\]

for a fixed derivative degree `d`. Completing the square in `L` shows Gaussian decay after the linear strip-growth term. With `Lambda(n)<=L`, the resulting series converges absolutely and uniformly.

The Weierstrass theorem therefore gives holomorphic dependence on `xi`, termwise differentiation, and exact passage from the heat--character prime sum to the cosine sum. The same estimate supplies differentiated cutoff tails by replacing `d` with the cell's derivative degree.

## Heat--character kernel

For complex `z` in a compact set, the gamma integrand

\[
e^{-tu^2}e^{izu}w_\Gamma(u)
\]

is dominated by a Gaussian times `exp(|Im z||u|)` and a logarithm. The prime term

\[
e^{-(L-z)^2/(4t)}
\]

has the same log-Gaussian domination. Hence `K(t,z)` is entire in `z` for each positive real `t`, locally uniformly on compact `(t,z)` strata.

## Endpoint term

The endpoint contribution is a finite sum of entire evaluations, so substitution and differentiation are automatic. Its pullback reproduces

\[
e^{t/4-t\xi^2}\cos(t\xi).
\]

## Disposition

The imaginary-character comparison is analytically valid on every compact positive-width and bounded-complex-center stratum, including any fixed finite derivative bidegree. The residual curvature of this cross-family cell is therefore exactly zero for the completed source. At finite arithmetic cutoff, only the explicitly bounded omitted prime tail remains.
