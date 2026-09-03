# The Dirichlet tail, not a scalar frequency floor, is the source-derived resonance object

## Problem

After correcting the zero-frequency maximizer, one might impose an arbitrary scalar floor `xi>=xi_0`. On a finite support interval this is not yet source-derived: zero-extension prime translations and endpoint localization do not commute with the whole-line Fourier multiplier.

## Canonical low/high split

On `(-L,L)`, let

`phi_n(x)=L^(-1/2) sin(n pi (x+L)/(2L))`,

with Dirichlet frequencies

`lambda_n=n pi/(2L)`.

Let `E_N` project onto the first `N` modes and `Q_N=1-E_N`. Then the source-derived tail floor is

`xi_0=lambda_(N+1)=(N+1)pi/(2L)`.

For the Dirichlet logarithm,

`Q_N log(1+sqrt(-Delta_D)) Q_N`

`>=log(1+lambda_(N+1))Q_N`.

This is the correct high-mode reserve used by a finite low-block enclosure.

## Why the scalar symbol is insufficient

A zero-extension translation `T_a` on the interval does not preserve the Dirichlet eigenspaces and is not diagonal in `xi`. Consequently

`sup_(xi>=xi_0) S_L(xi)`

does not by itself bound `Q_N P_L Q_N`. Boundary truncation creates mode mixing, and the finite-tail coupling `E_N P_L Q_N` also enters a Schur complement.

The nontrivial resonance quantities are therefore operator norms:

`R_tail(L,N)=||Q_N P_L Q_N||`,

`R_mix(L,N)=||E_N P_L Q_N||`.

Any scalar phase estimate must be transported to these compressed operators through a proved comparison map.

## Explicit matrix fixture

For a translation distance `a` with `0<=a<2L`, each matrix element is an elementary overlap integral

`<phi_m,T_a phi_n>`

`=integral_(-L)^(L-a) phi_m(x) phi_n(x+a) dx`

`=L^(-1) integral_(-L)^(L-a) sin(m pi(x+L)/(2L)) sin(n pi(x+a+L)/(2L)) dx`. Product-to-sum gives closed sine and cosine expressions; at `m=n`, the removable denominator is evaluated by its limit.

The prime operator is a finite weighted sum over `a=log n` for `n<=exp(2L)`. Hence every finite block `E_M P_L E_M`, including the low block and finite tail approximants, is explicitly computable with interval arithmetic.

## Certification architecture

A complete low/high certificate needs:

1. an interval enclosure of `E_N W_L E_N`;
2. a lower bound for `Q_N W_L Q_N` combining the Dirichlet logarithm, bounded archimedean remainder, localization constant, and a tail-prime estimate;
3. an enclosure of `E_N W_L Q_N`;
4. a Schur-complement positivity test;
5. a certified remainder bound beyond a finite matrix cutoff `M>N`.

The absolute prime norm remains a valid fallback for items 2 and 3 but yields the previously observed very large mode threshold.

## Disposition

The arbitrary scalar-tail formulation is withdrawn as a standalone route. The next executable arithmetic object is the Dirichlet-basis translation matrix and its finite-tail norm, with scalar resonance estimates admitted only after they bound that matrix compression.
