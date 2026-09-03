# The natural logarithmic form domain gives a semibounded local Weil operator

## Question

Is the positive-Sobolev realization the right ambient operator for the fixed-support Weil problem?

## Natural archimedean domain

Let

`m(u)=Re psi(1/4+iu/2)`.

This real multiplier is bounded below and satisfies

`m(u)=log|u|+O(1)`.

Choose a constant `c` so that `m(u)+c>=1`, and define the logarithmic form domain on the support window by

`D_L={f in L^2([-L,L]) : integral (m(u)+c)|fhat(u)|^2 du < infinity}`, 

using zero extension before Fourier transform.

The shifted archimedean form is closed and positive on `D_L` by construction. This domain is weaker than every fixed positive Sobolev space and is matched to the actual logarithmic symbol.

## Bounded perturbations

On fixed support:

- the prime contribution is a finite sum of translated `L^2` pairings and is bounded on `L^2`;
- the endpoint contribution consists of finitely many compactly supported weighted linear functionals and is bounded on `L^2`;
- the constant log-pi term is bounded on `L^2`.

Therefore the complete local Weil form is a bounded perturbation of the closed semibounded archimedean form. The KLMN/bounded-form perturbation theorem gives a closed semibounded self-adjoint operator `W_L` on `L^2([-L,L])` without assuming RH.

This operator is more natural than the compact `H^s` Riesz representative: it retains the positive logarithmic principal growth rather than dividing it by a Sobolev weight.

## Compact resolvent

The embedding `D_L -> L^2([-L,L])` is compact. For a form-bounded sequence:

1. the high Fourier tail is uniformly small because `m(u)+c` tends to infinity;
2. on a bounded Fourier window, restriction from frequency space to a bounded spatial interval is compact by the Hilbert--Schmidt kernel criterion;
3. combining the two gives precompactness in `L^2`.

Hence `W_L` has compact resolvent. Its spectrum is discrete, bounded below, and tends to positive infinity. In particular, only finitely many eigenvalues can be negative.

## Positivity consequence

For each fixed `L`, local Weil positivity is equivalent to nonnegativity of finitely many low eigenvalues of `W_L`. High-frequency positivity is not merely conjectural in this formulation: it follows from semibounded logarithmic ellipticity plus bounded source perturbations.

A certified computation still needs a finite-dimensional enclosure theorem. Rayleigh--Ritz gives upper bounds on ordered eigenvalues, useful for finding negatives. Proving that no low eigenvalue is negative requires complementary lower bounds, such as Lehmann--Goerisch, Temple-type estimates with residual control, or a verified finite-element enclosure adapted to the nonlocal logarithmic multiplier.

## Global limitation

The number of potentially negative eigenvalues and the required low-mode threshold depend on `L`, through the finite prime norm and endpoint constants. RH requires positivity for every support window. This local compact-resolvent theorem does not provide a uniform-in-`L` bound or source factorization.

## Relation to the Sobolev realization

For every `s>0`, the embedding `H_0^s -> D_L` is continuous. The compact operator `A_(L,s)` is the pullback/Riesz shadow of the semibounded operator `W_L`. Its accumulation at zero reflects division by the stronger Sobolev metric; it does not contradict the fact that `W_L` has eigenvalues tending to positive infinity.

## Disposition

The local domain and eventual signed tail are solved at the operator-theoretic level by the natural logarithmic form domain. The remaining local task is certified enclosure of the finite negative-index sector. The remaining global task is uniform arithmetic control as `L` increases.
