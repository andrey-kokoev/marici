# Conditioning of cavity-assisted optical discrimination

## Question

Does near-resonant recirculation create identification power, or does it merely
amplify both the desired difference and the calibration uncertainty?

## Exact sensitivity split

For the scalar steady-state field

```text
y(a,r) = a / (1-r a),
```

the source-amplitude and loop-gain sensitivities share the same resonant
denominator:

```text
dy/da = 1/(1-r a)^2
dy/dr = a^2/(1-r a)^2.
```

Their ratio is `1/a^2`, independent of resonance. Moving toward the pole does
not improve first-order discrimination of a source change against uncertainty
in the loop gain. It increases both together.

## A large gain that does and does not help

Freeze source amplitudes `1` and `99/100` with loop gain `9/10`. A single pass
separates them by `1/100`. The cavity records are `10` and `990/109`, separated
by `100/109`. Relative to downstream additive detector noise, this is an exact
amplification by `10000/109`, approximately ninety-two.

But if the loop gain is known only to lie in `[89/100,91/100]`, the first
source amplitude alone produces the response interval `[100/11,100/9]`, whose
width is `200/99`. That uncertainty is more than twice the cavity-amplified
source separation.

So resonance is useful against noise injected after the cavity. It is not a
repair for uncertainty in the feedback parameter that creates the gain.

## A second surprise: loss and return collapse

If mirror return is `m` and internal survival is `eta`, the steady response
depends only on `m eta`. The Jacobian with respect to `(m,eta)` has rank one.
For example, `(m,eta)=(9/10,4/5)` and `(3/4,24/25)` give the same loop product
and the same steady cavity record.

A ringdown-time port, independent loss monitor, or trusted mirror calibration
is needed to attribute the loop deficit. Adding more copies of the same
steady-state detector does not separate the two loci.

## Claim boundary

This is a stable scalar coherent steady-state model with exact amplitude
records. Shot-noise scaling, transient ringdown, nonlinear saturation, and
phase drift are outside the claim.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_cavity_discrimination_conditioning.py
```
