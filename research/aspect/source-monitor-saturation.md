# Saturation audit for the optical source monitor

## Question

Do dark and bright references suffice when the source monitor has quadratic
compression, and what additional structure makes the inverse physical?

## Two-level hostile

Freeze monitor response

```text
y = o + g x - h x^2
```

with `o=1/100`, `g=5/4`, and `h=1/2`. Dark and one mid-level bright reference
admit an exact affine fit with apparent gain one. That fit matches both anchors
but maps the physical science input `1/4` to `9/32`, a bias of `1/32`.

Thus dark-plus-bright calibration certifies only an affine monitor model. It
does not test saturation.

## Three-level calibration

Add a second nonzero reference level. Dark, `1/2`, and `1` identify offset,
gain, and quadratic compression exactly. The checker recovers all three frozen
parameters.

Calibrating the polynomial is not yet enough to invert it globally. The
science record has algebraic preimages `1/4` and `9/4`. The input range
`0<=x<=1` selects the physical root because the response is monotone there.
That range must come from the admitted source and monitor operating contract.

Outside a monotone range, even the exact calibrated response is ambiguous. The
checker gives equal monitor records for inputs `1` and `3/2`.

## Claim boundary

This is a static quadratic-response theorem with exact reference levels.
Higher nonlinearities, reference uncertainty, temporal drift, hysteresis, and
monitor–source crosstalk require additional anchors or a hardware-derived
response family.

## Verification

Run:

```text
uv run --with sympy python research/aspect/checkers/check_source_monitor_saturation.py
```

The checker verifies the affine hostile, three-level coefficient recovery,
the two inverse roots, and the monotone-domain gate.
