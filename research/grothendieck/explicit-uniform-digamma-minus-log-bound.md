# An explicit uniform digamma-minus-log bound

## Integral identity

For `Re z>0`,

`log z-psi(z)=integral_0^infinity e^(-zt)`

` * [1/(1-e^(-t))-1/t] dt`.

The bracket satisfies

`0 < 1/(1-e^(-t))-1/t < 1`

for `t>0`. Positivity follows from `1-e^(-t)<t`; the upper bound follows from `e^t>1+t`.

Therefore

`|log z-psi(z)| <= 1/Re z`.

At `z=1/4+iu/2`, this gives

`|Re psi(z)-log|z|| <= 4`.

## Comparison with the standard logarithmic symbol

For `u>=0`,

`|z|=sqrt(1/16+u^2/4)`.

The ratio `(1+u)/|z|` has maximum `sqrt(20)` at `u=1/4`, while `|z|/(1+u)<=1`. Hence

`|log|z|-log(1+u)| <= (1/2)log 20`.

Combining the estimates yields the explicit global bound

`|Re psi(1/4+iu/2)-log(1+|u|)|`

`<= 4+(1/2)log 20`.

No zero data or RH assumption enters.

## Interval consequence

The exact half-line boundary calculation identifies the principal difference between zero-extension `log|D|` and the spectral Dirichlet logarithm with the Carleman operator of norm `pi`. The present multiplier estimate controls the remaining digamma-minus-log correction.

Ignoring only Fourier-normalization constants and the harmless replacement of `log|u|` by `log(1+|u|)`, the interval remainder therefore has an explicit order-zero budget built from

`pi + 4+(1/2)log 20`

plus the bounded two-chart localization commutators. In particular the relative remainder coefficient in Voevodsky's generalized criterion can be taken as `eta=0`; no fraction of the logarithmic principal reserve is lost.

## Remaining constant

A publication-grade `C_L` still requires:

1. a fixed partition of unity near the two endpoints;
2. exact Fourier normalization;
3. norms of the localization commutators;
4. the constant log-pi and endpoint terms;
5. the finite prime translation norm.

These are additive order-zero constants. None can cancel the high logarithmic reserve.

## Disposition

The digamma correction is uniformly bounded with an explicit constant, and the boundary principal remainder is Carleman-bounded. The interval high-mode positivity theorem now lacks bookkeeping constants, not an analytic order or relative-bound gap.
