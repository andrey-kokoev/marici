# The fixed-support prime translation norm has an explicit but exponential bound

## Prime operator

For a logarithmic test supported in `[-L,L]`, its autocorrelation is supported in `[-2L,2L]`. Hence only prime powers satisfying

`log n<=2L`

enter the Weil prime term.

Each symmetric translation pairing has operator norm at most one on `L^2`. Up to the fixed Fourier-convention prefactor `kappa`, the prime perturbation therefore satisfies

`||P_L|| <= kappa sum_(n<=e^(2L)) Lambda(n)/sqrt(n)`.

This is an exact finite source bound. It uses absolute values and ignores cancellation between prime translations.

## Elementary closed bound

Since `Lambda(n)<=log n<=2L` and

`sum_(n<=X) n^(-1/2)<=2 sqrt(X)`,

we obtain

`||P_L|| <= 4 kappa L e^L`.

The constant can be sharpened by exact prime-power enumeration or Chebyshev estimates, but the elementary dependence is already exponential in the support scale.

## Consequence for the high-mode threshold

Combining

`Gamma_L >= log(1+sqrt(-Delta_D))-C_gamma(L)`

with the absolute prime bound gives a sufficient tail threshold roughly determined by

`log M > C_gamma(L)+4 kappa L e^L`.

Thus the resulting mode cutoff can be doubly exponential in `L`. This proves eventual positivity for each fixed window but is computationally useless as a global RH strategy.

The obstruction is not the existence of a signed tail. It is loss of prime cancellation under the operator-norm estimate.

## Required arithmetic improvement

A viable uniform programme must exploit more than absolute coefficient mass. Candidate structures are:

1. cancellation of the trigonometric translation polynomial on high Dirichlet modes;
2. large-sieve or almost-orthogonality bounds for the distinct `log n` shifts;
3. a positive/negative decomposition paired with the archimedean density;
4. an Euler-product factorization controlling the prime operator by logarithmic rather than exponential support growth.

Any such estimate must be uniform over all vectors in the high-mode subspace. Average cancellation over modes is insufficient for an operator lower bound.

## Cheapest falsifier

Construct high-mode vectors phase-aligned with many prime translations. If their prime Rayleigh quotient approaches the absolute mass bound, no square-root or logarithmic cancellation theorem can hold uniformly. Conversely, certified sublinear growth of the high-mode prime operator norm would materially lower the threshold.

## Disposition

The prime constant is explicit and finite, closing local semiboundedness, but its absolute bound grows as `L e^L`. The next nonredundant arithmetic target is a uniform high-mode cancellation theorem for the finite prime-translation operator.
