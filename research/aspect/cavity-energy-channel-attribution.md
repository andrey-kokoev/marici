# Cavity energy-channel attribution beyond a lossless mirror

## Question

What extra instrument is needed when the cavity mirror may absorb power rather
than merely reflect or transmit it?

## Two records leave one physical fiber

Use parameters mirror amplitude return `m`, internal amplitude survival `eta`,
and mirror absorbed-power fraction `alpha`. With normalized incident power,

```text
round-trip record = m eta
transmitted power = 1 - m^2 - alpha.
```

Their Jacobian has rank two on a three-parameter domain. The checker freezes
records `round-trip=3/5` and `transmission=1/4`. Both parameter triples

```text
(m, eta, alpha) = (4/5, 3/4, 11/100)
(m, eta, alpha) = (7/10, 6/7, 13/50)
```

produce those same two records. Better precision on either detector cannot
separate the fiber.

## The smallest attribution port

Add an independently calibrated absorbed-power channel, for example mirror
calorimetry or complete scatter collection. The record map becomes

```text
(m eta, 1-m^2-alpha, alpha).
```

Its Jacobian determinant is `2m^2`, hence it is full rank on the positive
amplitude chamber. The frozen records recover `m=4/5`, `eta=3/4`, and
`alpha=11/100` exactly.

An equivalent port is calibrated reflected power together with transmitted
power and complete energy closure. The word “complete” matters: uncollected
scatter is another energy channel and restores an ambiguity if it is omitted.

## A subtle distinction

Measuring total mirror nonreturn `1-m^2` is enough to recover `m` and hence
separate mirror return from internal survival. But total nonreturn does not
partition useful transmission from parasitic absorption. In the frozen case,
the total deficit `9/25` equals `1/4 + 11/100`.

Thus parameter identification and fault attribution require different port
counts. The first asks how much returned; the second asks where every missing
unit of power went.

## Claim boundary

The audit assumes one scalar mode, normalized incident power, positive return
amplitude, and complete energy accounting. Detector calibration uncertainty,
mode-dependent scatter, thermal delay, and light outside the collection
aperture are excluded.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_cavity_energy_channel_attribution.py
```
