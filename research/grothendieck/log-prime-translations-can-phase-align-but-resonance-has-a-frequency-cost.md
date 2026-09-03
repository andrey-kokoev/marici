# Log-prime translations can phase-align, but resonance has a frequency cost

## Question

Can the exponential absolute prime norm be replaced by uniform cancellation on all sufficiently high modes?

## Phase alignment obstruction

For a fixed support window, only finitely many primes occur. The numbers `log p` for distinct primes are linearly independent over the rationals: a rational relation would exponentiate to a forbidden multiplicative relation among primes.

Kronecker approximation therefore gives arbitrarily large frequencies `xi` for which

`xi log p` is simultaneously close to an integer multiple of `2pi`

for every prime in a prescribed finite set. Prime-power phases then align as well. In a translation-invariant model, the negative prime trigonometric polynomial can consequently approach its full absolute coefficient mass at arbitrarily high frequencies.

Thus no uniform high-frequency cancellation bound strictly below the coefficient mass can hold merely because the shifts are distinct.

## Finite-window qualification

On `[-L,L]`, translations are truncated by the boundary. A broad oscillatory packet has overlap approximately proportional to `1-|a|/(2L)` for shift `a`. Prime powers with `log n` near `2L` are suppressed, but the subfamily with `log n<=L` retains a fixed overlap reserve. Its absolute mass still grows exponentially, on the scale suggested by `exp(L/2)`.

Hence boundary truncation does not create logarithmic operator growth by itself.

## Resonance-cost mechanism

Simultaneous alignment of many rationally independent phases may require an enormous frequency. Dirichlet approximation across `d` independent prime phases produces denominators exponential in `d`; here `d` is approximately the number of primes below the active cutoff. The archimedean reserve is `log|xi|`, so the cost of constructing a near-maximal prime resonance grows with the phase dimension.

This changes the viable target. One should not seek cancellation at every high frequency. Instead prove a resonance-cost inequality:

`negative_prime_symbol(xi,L) <= log(1+|xi|)+C(L)`.

Such an inequality permits near-alignment only when the required frequency has accumulated enough archimedean reserve to pay for it.

## Arithmetic content

A quantitative proof requires lower bounds for simultaneous approximation of the vector

`(log p_1/(2pi),...,log p_d/(2pi))`.

Unique factorization gives qualitative rational independence but no adequate uniform Diophantine constant as `d` grows. Baker-type lower bounds for linear forms in logarithms address individual integer relations; converting them into a sharp simultaneous resonance-cost estimate is a separate step and may produce constants too large for the desired inequality.

## Strongest falsification attempt

Search for frequencies with prime Rayleigh quotient more negative than the available logarithmic reserve. A reproducible sequence with

`-P_L(xi)-log(1+|xi|) -> infinity`

would reject the resonance-cost programme. Near-resonance alone does not suffice; its frequency must be included in the residual.

## Disposition

Uniform prime cancellation is rejected as the wrong target. The surviving arithmetic target is a quantitative phase-alignment cost bounded by the archimedean logarithm. This is a direct meeting point between unique factorization and local Weil positivity, but no adequate bound is currently proved.
