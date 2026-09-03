# Weil completion has two distinct parameters with opposite radical variance

## Correction and synthesis

Two limiting operations had been conflated:

1. the spectral cutoff `N` at fixed Gaussian smoothing `t`;
2. the narrow-spectral limit `t -> infinity` after normalization by the first spectral weight.

They have opposite radical behavior.

## Fixed smoothing, increasing spectral cutoff

For

`G_(N,t)=sum_(j<=N) w_j(t) F_j^*F_j`

with positive weights, adding a pair gives

`rad G_(N+1,t) subset rad G_(N,t)`.

Additional spectral probes shrink the actual finite radical. The canonical maps between actual-radical quotients therefore run from finer cutoff to coarser cutoff.

## Fixed complete spectrum, increasing smoothing parameter

Normalize by the first weight:

`Ghat_(N,t)=F_1^*F_1 + sum_(2<=j<=N) exp[-t(lambda_j-lambda_1)] F_j^*F_j`.

As `t` increases, every higher-pair weight vanishes. For `N>=2`, the finite form may be nondegenerate for every finite `t`, while the limit has the nominated radical

`R=ker F_1`.

This is exactly Voevodsky's controlled-asymptotic-radical model: `R` need not be the actual radical at finite `t`; it is a source-nominated vanishing sector preserved by the identity transition in `t`. Uniform coercivity is required only on a declared complement of `R`.

## Two-parameter diagram

A valid Weil completion must therefore use a two-parameter family `G_(N,t)` and keep the maps distinct:

- `N`-direction: probe refinement, shrinking actual radicals, inverse quotient variance;
- `t`-direction: weight degeneration, growing limiting radical, controlled-radical quotient.

The first direction needs an energy-bounded projective limit. The second needs a nominated sector, quotient convergence, and no additional limiting radical.

## Interchange gate

The required theorem is not merely existence of both limits. One must show that spectral completion and controlled-radical degeneration commute on the nominated quotient:

`limit_(t -> infinity) limit_(N -> infinity) Ghat_(N,t)|_(V/R)`

agrees with

`limit_(N -> infinity) limit_(t -> infinity) Ghat_(N,t)|_(V/R)`.

A sufficient analytic condition would be uniform summability of the higher-pair quotient contributions for `t>=t_0`, together with a source-derived identification of `R` independent of `N`. Neither is supplied by finite rectangle samples.

Without uniform domination, mass can escape through increasing `N` while each fixed spectral component vanishes in `t`; the iterated limits can differ. This is the two-parameter analogue of phantom inverse-limit families.

## Consequence for the source programme

Voevodsky's controlled-radical theorem is compatible with the Gaussian asymptotic and is not contradicted by shrinking cutoff radicals. It applies in the `t` direction. My earlier inverse-variance correction applies in the `N` direction. Any `R_zeta` construction must specify which parameter each transition follows.

The first missing arithmetic objects are now:

1. a source-derived first-pair asymptotic sector `R` without importing zero locations;
2. an energy-bounded spectral-cutoff completion at fixed `t`;
3. a uniform domination theorem allowing interchange on `V/R`.

The first item is especially dangerous: defining `R` from the first on-line zero pair is spectral evidence, not a zero-free arithmetic construction.

## Disposition

The controlled-radical programme survives with corrected two-parameter typing. No source-derived `R` or interchange theorem currently exists, so it remains a conditional completion mechanism rather than an RH proof.
