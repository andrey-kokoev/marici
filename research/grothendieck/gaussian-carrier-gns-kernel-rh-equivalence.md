# The undecomposed Gaussian Carrier contains the source-GNS kernel

Status: exact kernel reduction and conditional equivalence; no RH claim

Let the source-defined two-variable completed Gaussian be

\[
 \Theta(t,\xi)
 =K_{\rm endpoint}(t,\xi)
  +K_\Gamma(t,\xi)+K_{\rm prime}(t,\xi),
 \qquad t>0,\quad\xi\in\mathbb R,                    \tag{1}
\]

with all three terms taken under one explicit-formula convention.  Do not
split them when imposing positivity.

For two Gaussian labels `a=(t,xi)` and `b=(u,eta)`, define

\[
 \mathcal K(a,b)=
 \exp\!\left[-\frac{tu}{t+u}(\xi-\eta)^2\right]
 \Theta\!\left(t+u,\frac{t\xi+u\eta}{t+u}\right).   \tag{2}
\]

This formula is forced by the elementary identity

\[
 t(\lambda-\xi)^2+u(\lambda-\eta)^2
 =(t+u)\left(\lambda-\frac{t\xi+u\eta}{t+u}\right)^2
 +\frac{tu}{t+u}(\xi-\eta)^2.                        \tag{3}
\]

Hence, whenever a positive real spectral measure exists,

\[
 \mathcal K(a,b)
 =\int_{\mathbb R}
 e^{-t(\lambda-\xi)^2}e^{-u(\lambda-\eta)^2}
 \,d\nu(\lambda).                                   \tag{4}
\]

It follows immediately that for every finite labelled family
`a_1,...,a_N` and real coefficients `c_i`,

\[
 \boxed{
 \sum_{i,j}c_i c_j\mathcal K(a_i,a_j)\ge0.
 }                                                    \tag{5}
\]

Equation (5) is the universal coupled positivity target.  Pointwise
positivity of `Theta(t,xi)` tests only the diagonal and is strictly weaker.

## Converse: positivity constructs the Hilbert space

Assume (5) for all finite labelled families, together with the already fixed
analytic and growth properties of the completed source.  Quotient the span
of formal Gaussian labels by the null space of `mathcal K` and complete it.
This produces a Hilbert space directly from (1)--(2), without naming any
zeros.

The label algebra is not arbitrary.  Products close by (3), and translations
of the centers act on the same fixed kernel.  Under the standard Gaussian
approximate-identity limit, positivity of every such Gram is equivalent to
positivity of the underlying tempered spectral distribution on the real
`lambda` axis.  The positive-distribution theorem then makes it a positive
measure `nu`.  Its Gaussian transform is (1).

Analytic continuation of the completed explicit formula identifies that
distribution with the Xi divisor.  Therefore its support on real `lambda`
places every nontrivial zero at

\[
 s=\frac12+i\lambda.                                 \tag{6}
\]

Conversely RH supplies the positive divisor measure and proves (4)--(5).
Subject to the explicit-formula normalization and distributional uniqueness
audit, this yields

\[
 \boxed{
 \mathrm{RH}
 \quad\Longleftrightarrow\quad
 \mathcal K\text{ is positive definite on all Gaussian labels}.}
                                                               \tag{7}
\]

## Why this is the desired source-derived self-adjointness

On the Gaussian label span, multiplication by `lambda` is encoded without
assuming translation invariance:

\[
 \lambda e^{-t(\lambda-\xi)^2}
 =\left(\xi+\frac1{2t}\partial_\xi\right)
 e^{-t(\lambda-\xi)^2}.                              \tag{10}
\]

The differentiated source kernel therefore defines the symmetric
multiplication operator on its Gaussian core.  Its self-adjoint realization
is multiplication by `lambda` in the reconstructed measure model.  Squaring
gives the nonnegative operator `B=lambda^2`; translating back to the quotient
coordinate gives `A=B+1/4>=1/4`.

Thus the quarter-shifted operator is downstream of a source-positive Carrier
kernel.  Neither its spectrum nor its lower bound is assumed.

## Exact falsifier and attack direction

The smallest falsifier is a finite labelled Gaussian packet for which the
matrix

\[
 (\mathcal K(a_i,a_j))_{i,j=1}^N                       \tag{8}
\]

has a negative quadratic form.  Finite positive packets do not prove (5).
The proof target is instead a source-level factorization

\[
 \mathcal K(a,b)=\langle D_a,D_b\rangle_{\mathcal H_{\rm source}}             \tag{9}
\]

derived from the completed theta object before endpoint/gamma/prime
projection.  Such a factorization would be the missing explanation: the
critical line is selected because only the real fixed sector admits the
positive Gaussian Carrier representation.

## Nonlinear divisor-extraction obstruction

There is no direct linear pull-through of (2) to the familiar fixed-contour
theta integral.  That integral constructs `Xi` itself,

\[
 \Xi(z)=\int_{\mathbb R}e^{izu}\Phi(u)\,du,           \tag{11}
\]

whereas `Theta(t,xi)` is linear in the *divisor* of `Xi`.  Extracting that
divisor passes through the nonlinear logarithmic derivative `Xi'/Xi` (or an
equivalent argument-principle boundary operation).  A linear transform in
`L^2(Phi du)` therefore cannot yield (9) merely by completing a square.

This identifies the kind of structure still missing.  It must combine the
fixed theta source with a canonical logarithmic or boundary construction
that turns zeros into positive norm data: for example a canonical system,
a de Branges-type energy, or a source-derived relative boundary quotient.
The direct theta convolution operator is already known to have continuous
multiplier spectrum and cannot perform this extraction.

The next analytic move is consequently to seek a Green or boundary identity
for the pole-subtracted precursor

\[
 Z(z)=(\tfrac14-z^2)F(z)                              \tag{12}
\]

whose boundary quadratic form is exactly (2).  A residual signed boundary
term would be the sharp obstruction.  Additional finite scouting is
irrelevant until that identity or its impossibility is understood.
