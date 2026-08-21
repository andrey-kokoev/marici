# The Li increment measure is finite

## Conditional spectral model

For a functional-equation zero pair on the critical line, set

`u_rho=1-1/rho`.

Then `|u_rho|=1`, and its paired contribution to the Li coefficient is

`a_n(rho)=|1-u_rho^n|^2=2-u_rho^n-u_rho^(-n)`.

Taking the centered second difference gives

`(a_(k+1)-2a_k+a_(k-1))/2 = |1-u_rho|^2 Re(u_rho^k)`.

Moreover,

`|1-u_rho|^2=1/|rho|^2`.

Therefore the increment correlations have the conditional moment formula

`c_k = integral_T Re(z^k) d mu(z)`,

where the symmetric measure is obtained by placing the positive weight
`|rho|^(-2)` at the phase `u_rho` (with the normalization dictated by the
chosen functional-pair convention).

Its total mass is `c_0=lambda_1`, hence finite. The original zero-counting
measure is infinite, but discrete differentiation supplies precisely the
inverse-square weight needed to make the increment measure finite.

## Revised Gate C target

Construct this finite positive measure from the arithmetic source without
using zero locations. It is enough to construct a positive functional `L`
on trigonometric polynomials satisfying

`L(cos(k theta))=c_k`

for every `k>=0`. Positivity means `L(|p|^2)>=0` for every analytic
trigonometric polynomial `p`; finite truncations are exactly the Toeplitz
minor tests.

This is more economical than constructing the homogeneous Li space first.
The GNS construction applied to `L` automatically produces the increment
Hilbert space, its unitary shift, and the cocycle obtained by discrete
integration.

## Noncircularity boundary

The zero-phase measure above proves what the desired object looks like under
RH. It cannot serve as the source construction. A valid proof must derive
`L` from the prime, archimedean, and endpoint sides of the explicit formula
and establish positivity there.

The main falsifier is now concrete: find a trigonometric polynomial `p` for
which the source evaluation of `L(|p|^2)` is negative.
