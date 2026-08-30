# The source heat trace must satisfy a logarithmic Weyl law

## Conditional heat trace

For positive ordinates with multiplicity, put

`Theta(t)=sum_gamma m_gamma exp(-t gamma^2)`.

The Riemann--von Mangoldt density has leading form

`dN/dgamma ~= (1/(2pi)) log(gamma/(2pi))`.

Integrating this density against the Gaussian gives the forced short-time
asymptotic

`Theta(t)`

` ~= log(1/t)/(8sqrt(pi t))`

`    -(EulerGamma/2+log(4pi))/(4sqrt(pi t))`

up to lower-order terms requiring the refined counting remainder.

The coefficients follow from the exact integrals

`integral_0^infinity exp(-t gamma^2) dgamma=sqrt(pi)/(2sqrt(t))`,

and its logarithmic Mellin derivative.

## Operator consequence

Any source-canonical squared Hilbert--Pólya operator must reproduce this
logarithmic one-dimensional Weyl law. It is not the heat asymptotic of an
ordinary compact manifold Laplacian: the extra logarithm records the
`T log T` zero count. A proposed local geometric model with the wrong heat
scale is falsified before detailed spectral comparison.

## Limitation of Weyl matching

A finite off-line quartet contributes

`2 exp((alpha^2-beta^2)t) cos(2alpha beta t)=2+O(t)`

as `t` tends to zero. Thus any finite number of hostile quartets changes only
an `O(1)` term and leaves the leading logarithmic Weyl law unchanged.

Consequently matching zero count, operator order, determinant growth, or the
first heat coefficients cannot by itself establish RH. These are necessary
normalization gates, not positivity mechanisms.

## Source target

Construct an arithmetic heat functional with both:

1. the forced short-time Weyl expansion;
2. positivity for every positive time and a positive spectral measure on
   `[0,infinity)`.

The first controls density; the second excludes oscillatory off-line
quartets. A credible explanation needs both from one construction.

## Proof-status boundary

The Gaussian-log calculation is exact. Turning the stated density heuristic
into a full asymptotic with an explicit remainder requires the classical
Riemann--von Mangoldt formula and a justified Stieltjes integration argument;
those analytic estimates are obligations of a publication proof.
