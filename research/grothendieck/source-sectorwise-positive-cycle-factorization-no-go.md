# The explicit-formula sectors do not give a sectorwise positive cycle factorization

## Question

Can the spectral wedge sum be reproduced by assigning independent positive rectangle energies to endpoint, archimedean, and prime sectors?

## Unnormalized arithmetic inequalities

Write `K(a)=K_t(a)` and put `A=log2`, `B=log3`. Before division by `K(0)^2`, the parity numerators are

`N_+=[K(0)+K(A+B)][K(0)+K(B-A)]-[K(A)+K(B)]^2`,

`N_-=[K(0)-K(A+B)][K(0)-K(B-A)]-[K(A)-K(B)]^2`.

When `K(0)>0`, rectangle positivity is exactly `N_+>=0` and `N_->=0`. These are two source-side Turan inequalities for the completed explicit formula.

## Endpoint sector is radical, not a positive reserve

The endpoint kernel is

`E_t(a)=exp(t/4) cosh(a/2)`.

Using hyperbolic addition identities, each endpoint parity block has rank one. Hence

`N_+(E)=N_-(E)=0`.

The polar endpoint contributes no standalone positive cycle reserve. It is an imaginary-frequency radical component.

## Signed source sectors

The prime kernel is a negative sum of paired Gaussian atoms centered at `plus/minus log n`. Its coefficients are `-Lambda(n)/sqrt(n)`. The archimedean kernel contains a signed log-pi Gaussian plus a cosine transform of `Re psi`. Neither displayed sector is a positive stationary measure.

Since a determinant is quadratic, substituting

`K=E+Gamma+P`

produces self terms and mixed terms `E--Gamma`, `E--P`, and `Gamma--P`. The endpoint self term vanishes, but its mixed terms need not vanish or have fixed sign. Therefore positivity of the completed rectangle cannot be obtained by simply summing separately positive endpoint, gamma, and prime cycle energies in the displayed explicit-formula decomposition.

This does not prove that no transformed positive arithmetic decomposition exists. It proves that the canonical additive sectors are not already such a decomposition.

## Consequence for forest--cycle factorization

The original programme sought positive one-prime forest pivots plus positive residue-aware cycle pivots. At the first mixed-prime rectangle, the source formula instead presents a signed cancellation problem governed by two Turan inequalities. A viable arithmetic factorization must introduce a nontrivial regrouping or transform that makes the mixed sector terms into squares. Naming the spectral wedge formula does not construct that regrouping because positive spectral weights are the target conclusion.

## Cheapest falsifier for proposed regroupings

Any proposed sectorwise positive decomposition must pass three tests:

1. reproduce the zero endpoint self determinant;
2. reproduce every mixed endpoint--gamma and endpoint--prime term rather than dropping them;
3. express the remaining signed prime--gamma contribution as admitted squares or exhibit its exact residual.

Failure of any test rejects the decomposition even if the total sampled determinant is positive.

## Disposition

A naive source-sectorwise forest--cycle factorization is rejected. The surviving target is narrower: derive the two completed Turan inequalities by a source-authorized regrouping of mixed endpoint, gamma, and prime terms, or find a certified negative rectangle.
