# Optical test of the source-derived damping crossing

## Question

Can the calibrated determinant instrument resolve the source-derived finite
NPT crossing for `Theta_1` while retaining `Theta_2` as a no-finite-crossing
control?

## Frozen source prediction

Under dual local amplitude damping with strength `p`, the source supplies

```text
Delta_NPT = (1-p)^2 |beta|^2 (|alpha|^2-p^2|beta|^2).
```

For `Theta_1`, the squared amplitudes are `1/4` and `3/4`, so the unique
finite crossing is `p=1/sqrt(3)`. `Theta_2` swaps the weights. It has equal
initial concurrence, but its formal crossing is `sqrt(3)`, outside the
physical interval. Thus `Theta_2` remains NPT for every `p<1`.

These are source-derived predictions, not trajectories fitted from the
determinant records.

## Calibrated bracketing test

Use population radius `1/1000` and coherence-quadrature radius `1/200`. At
`p=1/2`, below the `Theta_1` crossing, the exact determinant is `3/256` and
the one-sided NPT lower bound remains positive. At `p=2/3`, above the crossing,
the exact determinant is `-1/144` and the corresponding one-sided upper bound
is negative. The same instrument therefore resolves both sides without
estimating the crossing location from the data.

At `p=9/10`, the `Theta_2` control remains robustly NPT. Close to complete
damping, the mathematical determinant stays positive but tends to zero; at
`p=99/100` the frozen calibration box becomes inconclusive. This is an
instrument-resolution limit, not an additional physical crossing.

## Remaining optical obligation

The damping strength must be set or independently measured, and the phase
frame joining the four correlation settings must remain calibrated.
Differential phase drift can corrupt the reconstructed coherence and is not
absorbed into the source damping parameter.

## Verification

Run:

```text
uv run --with sympy python research/aspect/checkers/check_amplitude_damping_crossing_instrument.py
```

The checker uses exact symbolic radicals, verifies the source crossing and
control, and applies the previously derived one-sided calibration bounds.
