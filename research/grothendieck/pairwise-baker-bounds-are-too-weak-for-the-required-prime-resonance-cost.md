# Pairwise Baker bounds are too weak for the required prime resonance cost

## Problem

Can lower bounds for linear forms in logarithms force simultaneous prime-phase alignment to occur only after the archimedean reserve `log(1+|xi|)` has paid for the prime coefficient mass?

## Elimination of the common frequency

Suppose two prime phases nearly align:

`xi log p = 2 pi k_p + delta_p`,

`xi log q = 2 pi k_q + delta_q`,

with `|delta_p|,|delta_q|<=epsilon`. Eliminating `xi` gives

`k_q log p-k_p log q`

`=(delta_p log q-delta_q log p)/(2 pi)`.

Hence

`|k_q log p-k_p log q|`

`<=epsilon(log p+log q)/(2 pi)`.

The integer coefficients satisfy `|k_p|,|k_q|` of order `|xi|L` for primes in the support window.

## What a Baker-type estimate supplies

A two-logarithm lower bound has the schematic form

`|k_q log p-k_p log q| >= c(p,q) B^(-C(p,q))`,

where `B=max(|k_p|,|k_q|)`. Combining the inequalities yields only

`epsilon >= c'(p,q)(|xi|L)^(-C(p,q))`,

or

`log|xi| >= C(p,q)^(-1) log(1/epsilon)-O(log L+log(1/c'))`.

This makes frequency cost logarithmic in required phase accuracy, with a small coefficient degraded by the logarithmic-form constant.

## Comparison with the Weil budget

The fixed-support prime mass grows on the scale `exp(L)` under the elementary absolute estimate. If a near-resonance is allowed a fixed absolute deficit `Delta`, the weighted cosine deficit behaves quadratically:

`M_L-S_L(xi)` of order `M_L epsilon^2`.

Requiring deficit at most `Delta` gives

`epsilon` of order `sqrt(Delta/M_L)`,

so `log(1/epsilon)` grows only linearly in `L`. Pairwise Baker then forces at best a logarithmic frequency reserve of order `L/C(p,q)`, not order `M_L`.

Using many primes does not repair this through naive pairwise application: the constants worsen with the number and heights of logarithms, while pairwise constraints do not sum into an additive lower bound for `log|xi|`.

## Falsification scope

This does not prove that every simultaneous Diophantine route fails. It rejects the specific route that applies standard pairwise linear-form bounds independently and expects their costs to add. A viable theorem would need a genuinely simultaneous lower bound whose exponent or entropy scales favorably with the weighted number of prime phases.

## Disposition

Standard pairwise Baker bounds are inadequate for the resonance-cost inequality at the required exponential prime-mass scale. The branch reopens only with a simultaneous theorem that converts alignment of many prime logarithms into an additive frequency cost, or with an operator argument exploiting interval overlap rather than phase exclusion.
