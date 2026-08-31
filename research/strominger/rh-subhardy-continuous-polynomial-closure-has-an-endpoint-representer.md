# Sub-Hardy continuous polynomial closure has an endpoint representer

## Question

Is evaluation at \(x_0=\log3\) uniformly bounded on the closure of polynomials in the continuous Weibull norm?

## Shifted moment measure

Let

\[
d\nu(x)=e^{-2ax^\beta}\mathbf 1_{[x_0,\infty)}(x)dx,
\qquad 0<\beta<\frac12.
\]

After shifting \(y=x-x_0\), the density is

\[
w_0(y)=e^{-2a(y+x_0)^\beta},
\qquad y\geq0.
\]

The Stieltjes Krein logarithmic-density integrand has tail order

\[
\frac{-\log w_0(y^2)}{1+y^2}
\asymp y^{2\beta-2}.
\]

It is integrable exactly in the sub-Hardy range \(\beta<1/2\). The continuous shifted Weibull moment problem is therefore indeterminate.

## Evaluation theorem

For an indeterminate Hamburger or Stieltjes moment problem, the orthonormal-polynomial kernel

\[
K(z,z)=\sum_{n\geq0}|P_n(z)|^2
\]

converges locally uniformly in \(z\). Consequently polynomial evaluation is bounded on its \(L^2(\nu)\) closure. By Riesz representation, there is a unique

\[
k_{x_0}\in\overline{\mathbb C[x]}^{L^2(\nu)}
\]

such that

\[
p(x_0)=\langle p,k_{x_0}\rangle_{L^2(\nu)}
\]

for every polynomial \(p\). Hence

\[
|p(x_0)|^2\leq K(x_0,x_0)Q_{\rm cont}(p)
\]

with a finite degree-independent constant.

The endpoint part of the quadrature error therefore satisfies

\[
R_{\rm end}(p)
\leq
\frac{e^{-2ax_0^\beta}}{3}K(x_0,x_0)Q_{\rm cont}(p).
\]

## Quantitative boundary

Indeterminacy proves finiteness but does not provide the numerical cap required by the remaining coercivity budget. The finite Christoffel values increase to the unknown limit from below; the observed degree-six ratio near \(0.0422\) is not an upper bound.

## Disposition

Endpoint evaluation is uniformly bounded in degree on the continuous comparator space. The endpoint blocker is reduced from existence to a quantitative kernel estimate. The derivative form remains separate.

## Claim boundary

This theorem concerns the continuous Weibull comparator, where the Krein criterion applies. It does not transfer indeterminacy to the atomic logarithmic-label measure and does not prove total quadrature coercivity below one.
