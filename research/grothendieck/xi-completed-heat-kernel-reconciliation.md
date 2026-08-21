# The explicit arithmetic heat kernel reconciles with the zero heat trace

## Probe

The source expression

`K_endpoint(t)+K_gamma(t)+K_prime(t)`

was evaluated at 70 decimal digits using von Mangoldt weights through
`n=200000`. Independently, the spectral validation sum

`sum_(j=1)^80 exp(-t gamma_j^2)`

was computed from the first eighty zero ordinates. Zero locations were not
used in the source expression.

For `t` from `0.001` through `0.1`, observed source--spectral residuals ranged
from approximately `3.5e-34` to `3.1e-18`. Neither prime-tail nor spectral-tail
errors were interval-certified, so these are reconciliation data rather than
proof.

## Cancellation profile

The completed sign is highly conditioned. At `t=0.1`, approximately,

`K_endpoint = 1.0253151205`,

`K_gamma    =-0.8625096009`,

`K_prime    =-0.1628055175`,

while their sum is only

`2.1048e-9`.

Thus pointwise positivity at moderate time is a cancellation theorem at nine
or more decimal orders beyond the scale of the components. Sectorwise coarse
bounds are again structurally unsuitable.

At very short time, the prime log-Gaussians are exponentially suppressed and
the endpoint--gamma pair produces the logarithmic Weyl scale. As time grows,
the negative prime saddle becomes essential and cancels the endpoint growth.

## Research consequence

The explicit kernel is correctly normalized and appears to be the desired
heat trace. The next credible theorem is not another raw scan. It is a
controlled analytic comparison proving

`K_endpoint(t)+K_gamma(t) >= -K_prime(t)`

uniformly for every `t>0`, with regimes adapted to the cancellation:

1. small time: gamma/Weyl dominance and exponentially small primes;
2. transition time: explicit finite computation with rigorous tails;
3. large time: saddle-point cancellation tied to the prime number theorem,
   requiring a remainder strong enough to preserve the exponentially small
   positive spectral result.

The third regime is likely RH-sized: controlling the completed remainder to
the scale of the first spectral exponential is essentially controlling the
zero distribution itself.

## Falsifier

A certified negative value at any time disproves the positive heat target and
hence RH. An uncertified sign after cancellation of order-one components is
not acceptable evidence.
