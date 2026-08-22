# Seventy-eight central reciprocal-slope chords are interval-positive

Let `H(t)=1/sqrt(F'(t))`. Use the thirteen endpoints obtained by inserting
`3*10^k` between successive powers of ten from `10^-8` through `10^-2`.
Every one of the 78 arithmetic-midpoint gaps

\[
 H((x+y)/2)-(H(x)+H(y))/2
\]

is strictly positive under directed 90-digit Decimal interval propagation.
The weakest certified enclosure, on `[10^-8,3*10^-8]`, is

\[
 [1.7964066808888\ldots,1.8106786498949\ldots]\times10^{-21}.
\]

The calculation differentiates the coupled source analytically. Its intervals
include the depth-120 Euler tails through `eta''`, omitted-term bounds for
digamma and trigamma after recurrence to argument 100, and a Machin enclosure
of `pi`. No finite-difference remainder remains.

Two implementation defects were repaired before accepting the certificate.
Bernoulli coefficients in exploratory checkers had been constructed under the
default 28-digit Decimal context; they are now exact rationals. Unary Decimal
negation in the first interval attempt also invoked that default context; it is
now exact `copy_negate()`. Both defects materially changed tiny exploratory
gaps. This certified interval supersedes all earlier central minimum values.

This is an unconditional finite source calculation using no zero locations.
It certifies 78 selected chords, not continuum concavity, the full Loewner
kernel, the Pick property, or RH.

## Durable verification

- Checker: `checkers/reduced_source_central_interval_chords.py`
- Result: `results/reduced-source-central-interval-chords.json`
