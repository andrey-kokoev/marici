# Minimal Gaussian--arithmetic commutator audit

## Candidate and exact calculation

Let

`D=partial_x+2 pi x`

be the Gaussian annihilator, let `Delta_Z=sum_n delta_n`, and let diagonal
integer formation be the distribution-valued map

`S(f)=f Delta_Z`.

Apply `D` distributionally on the target. The product rule gives

`D(Sf)=partial_x(f Delta_Z)+2 pi x f Delta_Z`
`     =(f'+2 pi x f)Delta_Z+f partial_x Delta_Z`.

Since `S(Df)=(f'+2 pi x f)Delta_Z`, the exact commutator is

`[D,S]f=f partial_x Delta_Z`.

This is label-sensitive and is defined before Poisson aggregation, but it is a
first-order derivative-delta current at every occupied integer.

## Gaussian and hostile tests

For the standard Gaussian `g`, `Dg=0`, yet

`[D,S]g=g partial_x Delta_Z != 0`.

Thus the minimal commutator does not vanish for the vacuum. Nor is it an
already authorized exact boundary current: the positive atomic Fock grammar
contains weighted order-zero atoms, while derivative-delta currents have
positive distributional order.

For a Gaussian-polynomial hostile `h`, the output is likewise
`h partial_x Delta_Z`. Although `Dh` separately detects oscillator excitation,
the commutator itself does not isolate that excitation; its universal comb
derivative term is present for both sources. Subtracting the Gaussian output
or fitting a counterterm would require an independently authorized boundary
operation.

## Relation to hostile multipliers

The distributional-order test already shows that nonconstant polynomial
Mellin multipliers force derivative-delta label sources and hence leave the
positive atomic source category. The commutator calculation reaches the same
boundary immediately: coupling a first-order archimedean differential directly
to sharp diagonal sampling exits the declared arithmetic value type.

## Decision

The naive annihilator--sampling commutator is not the missing Green current.
It fails the required vacuum exactness and produces an unauthorized
order-one label distribution. A viable nonseparable constructor must either

1. enlarge the source category with a source-derived derivative-label boundary
   complex and prove its Green incidence, or
2. regularize diagonal formation (for example through heat/Poisson evolution)
   so that the commutator lands in an admitted boundary-current topology.

Neither repair follows from the bare Gaussian annihilation equation.
