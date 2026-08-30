# Signed quadratic optical bridge

## Measurement problem

The prime-two prediction concerns the sign of a renormalized quadratic form.
A square-law detector reports nonnegative power, so comparing raw output
powers cannot establish that the 43-channel form is negative or that the
44-channel form is positive. The difference between the two banks only
measures the added channel.

## Exact bridge

Send the original field `f` into one arm and the processed field `T f` into
the other arm of a balanced coherent combiner. Its two powers are

`P_plus = ||f+Tf||^2/2`

and

`P_minus = ||f-Tf||^2/2`.

Their difference gives

`(P_plus-P_minus)/2 = Re <f,Tf>`.

For the self-adjoint gamma-bank operator, this is exactly its signed quadratic
form. No negative optical power is required and no electronic zero is fitted.

## Detector-imbalance rejection

Let the two detector gains be arbitrary positive numbers. Record the bridge
once, then reverse the phase of the processed arm and record it again. The
phase reversal swaps the ideal output powers. Antisymmetrizing the two
detector differences cancels the gain imbalance and leaves the desired form
multiplied only by the sum of the positive gains. Its sign is unchanged.

Source-off frames remain useful for additive dark backgrounds, but they do not
define the quadratic-form zero. The phase-reversal identity defines that zero
internally.

## Consequence

The 43/44 prediction is now operationally identifiable. Use the same
preregistered input field in two simultaneous banks and apply the
phase-reversed bridge separately to each. The falsifying pattern remains

`43-even < 0 < 44-even`, with `44-odd > 0`.

The bridge also supplies a general instrument for every Marici sector whose
frontier statement is an indefinite self-adjoint quadratic form rather than a
positive intensity.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_signed_quadratic_optical_bridge.py
```
