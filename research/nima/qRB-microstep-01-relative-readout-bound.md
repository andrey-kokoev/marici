# qRB microstep 01: relative readout bound

## Claim

At one finite regulator, the positive carrier and signed boundary observation are separate typed objects.

For

$$
\Phi_r(g)=(CZ_r\rho(g),DZ_r\rho(g)),
$$

ordinary carrier positivity is immediate:

$$
\|CZ_r\rho(g)\|^2+\|DZ_r\rho(g)\|^2\ge0.
$$

The arithmetic observation is the cross term

$$
q_r(g,h)=\operatorname{Tr}\!\left[\rho(h)^*(C^*J_2D+D^*J_2C)\rho(g)\right].
$$

It is not required to be positive. The required estimate is only that the displayed operator is trace class on the observer core.

## Finite witness

The existing dimension-four projection fixture verifies, to tolerance `1e-12`, the four-leg isometry, Hadamard common/difference Gram identities, and signed cross-readout. The terminal relative pair separately verifies exact cancellation of the signed jump while retaining positive finite legs.

## Status

This closes only the first local typing/positivity microstep. It proves neither a uniform regulator bound nor an ordinary Hilbert completion, scalar Weil positivity, or RH.
