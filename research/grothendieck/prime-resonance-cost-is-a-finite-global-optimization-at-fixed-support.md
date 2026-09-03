# Tail-restricted prime resonance cost is a finite optimization at fixed support

Status: corrected. The unrestricted optimization is trivial because its maximum occurs at zero frequency. Only a declared positive tail floor or the actual interval overlap operator is nontrivial.

## Setup

For fixed support `L`, define the finite prime-power trigonometric polynomial

`S_L(xi)=sum_(log n<=2L) Lambda(n)/sqrt(n) cos(xi log n)`

with the declared explicit-formula prefactor restored afterward. Define the resonance-cost residual

`F_L(xi)=S_L(xi)-log(1+xi)`,

for `xi>=0`.

## Zero-frequency correction

All coefficients are nonnegative, so

`S_L(xi)<=M_L=sum Lambda(n)/sqrt(n)`.

At zero frequency every cosine equals one, hence

`F_L(0)=M_L`.

Therefore the unrestricted sharp constant is exactly

`max_(xi>=0)F_L(xi)=M_L`.

Unrestricted scalar resonance optimization gives no improvement over absolute mass.

The nontrivial quantity must declare a tail floor `xi_0>0`:

`C_L(xi_0)=max_(xi>=xi_0)F_L(xi)`.

Because `F_L` tends to negative infinity, this restricted maximum is finite and attained.

## Certified truncation

For any trial upper bound `C`, the absolute-mass estimate proves `F_L(xi)<=C` whenever

`xi>=exp(M_L-C)-1`.

Thus certification of `C_L(xi_0)<=C` reduces to interval branch-and-bound on

`[xi_0,exp(M_L-C)-1]`.

The interval may be enormous when `C` is much smaller than `M_L`, but it is finite and source-derived.

## Derivative bounds

The residual has derivative

`F_L'(xi)=-sum Lambda(n)log(n)/sqrt(n) sin(xi log n)-1/(1+xi)`.

Therefore

`|F_L'(xi)|<=D_L`,

where

`D_L=1+sum Lambda(n)log(n)/sqrt(n)`.

A grid interval of width `h` with midpoint value `v` has the rigorous Lipschitz upper bound

`sup F_L<=v+D_L h/2`,

once coefficient and transcendental evaluations are interval enclosed. Sharper branch bounds retain each cosine phase interval rather than using the global derivative sum.

## Relation to phase recurrence

Kronecker recurrence shows that `S_L` returns arbitrarily close to `M_L`, but those returns occur at unbounded frequencies where the subtractive logarithm grows. They do not prevent attainment of the maximum at finite frequency. The relevant arithmetic question is computational complexity and support growth of `C_L^*`, not existence.

## Interval-operator limitation

`S_L` is the translation-invariant symbol. The actual support-window operator includes translation-overlap and boundary effects. Its sharp constant requires an operator-valued analogue, not merely the scalar polynomial maximum. The scalar optimization is a necessary fixture and may upper-bound interior wave packets, but it does not certify the full interval operator.

## Disposition

Unrestricted scalar resonance cost is exactly the absolute mass and offers no gain. Tail-restricted resonance cost is finitely certifiable once `xi_0` is source-derived from the low/high decomposition. The actual interval overlap operator remains the stronger target.
