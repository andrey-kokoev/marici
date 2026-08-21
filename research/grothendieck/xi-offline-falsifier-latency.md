# Off-line zeros can evade arbitrarily many finite Toeplitz ranks

## Phase defect

Let

`rho=1/2+alpha+i beta`, with `alpha>0`,

and `u(rho)=1-1/rho`. Then

`|u(rho)|^2=1-2alpha/|rho|^2 < 1`.

The reflected zero `1-rho` has phase `u(rho)^(-1)`, whose modulus is greater
than one. Hence its high-order Li and moment contributions eventually grow
exponentially.

## Latency scale

Put `epsilon=2alpha/|rho|^2`. For a near-line or high zero,

`-log|u|=-1/2 log(1-epsilon)`

`       =alpha/|rho|^2+O(alpha^2/|rho|^4)`.

Therefore order-`k` amplification becomes substantial only when

`k` is comparable to `|rho|^2/alpha`.

As `alpha` tends to zero or `|beta|` tends to infinity, this latency becomes
arbitrarily large.

## Consequence for computation

Positivity of the first `N` Li coefficients or Toeplitz ranks cannot exclude
all off-line zeros. A hostile quartet sufficiently high and sufficiently
close to the line can remain invisible below any prescribed finite `N`.

This does not make finite tests useless. They are strong falsifiers for
defects within their sensitivity window and can reject proposed universal
identities. They cannot establish RH by extrapolation.

## Consequence for explanation search

The best research target is not a larger uncertified finite-rank sweep. It is
an all-order arithmetic mechanism—such as a source-positive Herglotz
representation or a semigroup monotonicity theorem—that rules out the entire
exponential defect family simultaneously.

The latency estimate also explains why extremely small Gram eigenvalues are
expected and why floating-point sign tests become rapidly fragile.

## Falsifier

Any claim that checking a fixed number of Li/Toeplitz inequalities proves RH
is false without an independent theorem bounding the location and distance
of every possible off-line zero.
