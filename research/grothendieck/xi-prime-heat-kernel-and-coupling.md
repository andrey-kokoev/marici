# The Euler product gives an explicit negative prime heat kernel

## Squared-resolvent coordinate

Put `s=1/2+sqrt(x)`. In the half-plane `s>1`, equivalently `x>1/4`, the
Euler product gives

`zeta'(s)/zeta(s)=-sum_(n>=2) Lambda(n)n^(-s)`.

Its contribution to

`B'(x)=[xi'/xi(1/2+sqrt(x))]/[2sqrt(x)]`

is

`-sum_n Lambda(n)n^(-1/2)exp(-sqrt(x)log n)/(2sqrt(x))`.

## Exact inverse Laplace transform

The identity

`exp(-a sqrt(x))/sqrt(x)`

` =integral_0^infinity exp(-xt) exp(-a^2/(4t))/sqrt(pi t) dt`

gives the prime heat kernel

`K_prime(t)`

` =-1/(2sqrt(pi t)) sum_(n>=2) Lambda(n)n^(-1/2)`

`       *exp(-(log n)^2/(4t))`.

For every fixed `t>0`, the log-Gaussian makes this sum convergent. Every term
is nonpositive.

## Endpoint kernel

The elementary completed factors satisfy

`[1/s+1/(s-1)]/(2sqrt(x))=1/(x-1/4)`.

Its inverse Laplace kernel is `exp(t/4)`. The positive-axis pole at `x=1/4`
is not a pole of the completed Stieltjes target; it is cancelled by the zeta
pole under completion.

## Coupling theorem required

The desired positive heat trace must have the form

`Theta(t)=K_endpoint(t)+K_gamma(t)+K_prime(t)`

under one common transform and continuation prescription. The prime term is
manifestly negative, while the endpoint term grows like `exp(t/4)`. Their
large-time cancellation and the gamma contribution are structural, not
optional regularization.

This supplies a concrete source-side positivity target:

`K_endpoint(t)+K_gamma(t) >= -K_prime(t)` for every `t>0`.

Proving this pointwise inequality without zero locations would construct the
positive Lévy density and hence cross the complete-Bernstein gate.

## Asymptotic warning

As `t` grows, the prime sum's saddle moves to exponentially large `n`; its
leading growth is expected to interact with `exp(t/4)`. Termwise or
finite-prime truncations cannot test the completed large-time sign reliably.

## Falsifiers

- Treating the negative prime kernel as a positive Gram block.
- Dropping the endpoint `exp(t/4)` term before zeta-pole cancellation.
- Using different continuation or cutoff schemes for the three kernels.
- Failure of their Laplace sum to reproduce `B'(x)` for `x>1/4`.
- A negative completed heat kernel at any positive time.

The inverse-Laplace identity is exact. The explicit gamma kernel and the
pointwise completed inequality remain to be derived.
