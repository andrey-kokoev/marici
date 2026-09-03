# Heat-regularized Gaussian--arithmetic commutator

## Regularized comb

Let the heat-smoothed integer comb be

`mu_t(x)=sum_(n in Z) (4 pi t)^(-1/2) exp(-(x-n)^2/(4t))`, `t>0`.

Poisson summation gives

`mu_t(x)=sum_(k in Z) exp(-4 pi^2 t k^2) exp(2 pi i k x)`.

Define regularized diagonal formation by `S_t(f)=mu_t f` and retain the
Gaussian annihilator `D=partial_x+2 pi x`.

## Exact commutator

Because the zeroth-order part of `D` commutes with multiplication,

`[D,S_t]f=mu_t' f`.

For every finite `t>0`, `mu_t'` is nonzero: its Fourier coefficients at
`k=+/-1` are nonzero. Therefore for the Gaussian vacuum `g>0`,

`[D,S_t]g=mu_t' g != 0`.

Heat regularization improves the sharp derivative-delta defect to a smooth
periodic current, but it does not make the commutator vacuum-exact.

## Limiting tradeoff

As `t` decreases to zero, `mu_t` tends distributionally to the integer comb
and `mu_t'` tends to `partial_x Delta_Z`, recovering the unauthorized sharp
commutator defect.

As `t` tends to infinity,

`mu_t -> 1`, `mu_t' -> 0`,

so vacuum closure is recovered only when the arithmetic modulation collapses
to the constant continuum mode. This limit loses the integer-label
information the constructor was meant to couple.

At finite `t`, subtracting the canonical current `mu_t'f` would force the
commutator to vanish for every source, including the hostile, and therefore
has no source-discrimination or confinement force.

## Decision

No heat scale simultaneously supplies exact Gaussian-vacuum commutation and
nontrivial arithmetic sensitivity. Heat smoothing changes the regularity of
the defect but not its algebraic origin. The heat-regularized commutator is
therefore not the missing boundary Green current.

This closes the simplest nonseparable annihilator--diagonal constructor route.
Any surviving coupling must use a higher relation than commutation with
multiplication—for example a separately derived relative determinant or
boundary phase-space incidence—and must still identify its scalar determinant
with the theta section without divisor input.
