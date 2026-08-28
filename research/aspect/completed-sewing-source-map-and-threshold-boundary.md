# Completed sewing maps and uncertainty boundary

## Source-derived maps

The maps exist algebraically. On the injective idelic trace range, the forward
map is trace after additive adelic Fourier transform, and the reverse map is
trace after inverse Fourier transform. Injectivity makes them independent of
the chosen source representative. Their authority therefore precedes scalar
Tate or zeta readout.

What we do not yet have is a finite completed typed matrix. Producing it
requires explicit source basis functions, their trace coordinates, their
Fourier images, the source Gram metric, and a cutoff-compatible graph
projection. Inserting a convenient discrete Fourier matrix would make a
unitary optical control, not a source-derived theta sewing.

## Preregistered uncertainty law

For `m=144` real quadrature means, `n` trials per setting, familywise failure
probability `alpha`, and an independently calibrated single-trial variance
upper bound `sigma_squared`, freeze

`epsilon=sqrt(2*sigma_squared*log(2m/alpha)/n)`.

This bounds every real quadrature error simultaneously under the declared
Gaussian mean model. Each complex `6x6` map then has Frobenius error radius

`e=sqrt(72)*epsilon`.

Under the source-unitary and mutually inverse null, both the unitarity and
composition residuals have statistical Frobenius threshold

`2e+e^2`.

An independently calibrated systematic Frobenius bias bound is added before
the threshold is frozen.

For the explicitly nonphysical example `sigma_squared=1`, zero systematic
bias, one million trials per setting, and 99 percent familywise confidence,
the threshold is approximately `0.0784`. This number is a compiler fixture,
not a laboratory threshold.

## Answer

We have the source-derived forward and reverse formulas. We have a
preregistered threshold law. We do not yet have their physical finite
instantiations: the typed Fourier-trace basis and measured apparatus variance
and bias bounds are the remaining inputs.
