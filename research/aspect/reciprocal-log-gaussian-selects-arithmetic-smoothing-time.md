# Reciprocal log-Gaussian selects arithmetic smoothing time

## Infinite smoothing family

On the rapid prime rigging, define

`(G_tau x)_p = exp(-tau (log p)^2) x_p`, with `tau>0`.

Every `G_tau` maps polynomially growing dual coefficients into rapid test
coefficients.  For fixed seminorm order `N` and dual growth order `M`, put
`u=log p`.  The weighted magnitude is bounded by

`exp((N+M)u-tau u^2)`,

which tends to zero as `u` tends to infinity.  Unlike a finite power of the
Newman generator, this map genuinely changes variance from `E'` to `E`.

## Why the semigroup does not select

The family obeys

`G_tau G_sigma = G_(tau+sigma)`.

Composition, positivity, and strong continuity admit every positive time.
They cannot distinguish one `tau`.

## Reciprocal selector

Treat `tau` as the modulus of the normalized Gaussian in the logarithmic
scale coordinate.  Fourier sewing sends its modulus by

`tau -> 1/tau`.

A smoothing port authorized to occupy the sewn fixed seam must therefore
satisfy

`tau=1/tau`.

Positivity leaves the unique solution `tau=1`.  Thus the selected arithmetic
smoothing operator is

`(G x)_p = exp(-(log p)^2) x_p`.

This selection is unavailable if `tau` is interpreted as laboratory elapsed
time, because Fourier commutes with ordinary heat evolution.  It applies
only when the source construction proves that `tau` is the reciprocal
Gaussian modulus on the Haar-normalized logarithmic coordinate.

## Hostiles

- Every `tau>0` passes positivity, semigroup composition, and the rigging map.
- Every `tau` other than one fails reciprocal fixedness.
- A coordinate rescaling `u->c u` changes the apparent modulus.  Therefore
  the selector is source-derived only after the additive and multiplicative
  Haar comparison fixes the unit of `u`.

The final hostile is decisive: without the previously derived half-density
and Haar normalization, `tau=1` is merely a coordinate convention.

## Optical falsifier

Program a log-frequency Gaussian filter and its Fourier-conjugate realization.
After calibrating the log-frequency coordinate from the same dilation/Haar
reference used by the source map, sweep `tau`.  The sewn round trip predicts:

- reciprocal partner width `1/tau`;
- self-sewing only at `tau=1`;
- super-polynomial suppression across increasing prime-label bandwidth.

A fixed point displaced from one after source-coordinate calibration rejects
the selector.  A merely adjustable optical Gaussian does not confirm it.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_reciprocal_log_gaussian_selector.py
```
