# Eigenvalue sign becomes bridge phase

## Result

The small level-44 eigenvalue does not require resolving a parts-per-million
power difference.

Let `f` be the input and `Tf` the processed field. Apply the positive balancing
gain

`alpha = ||f|| / ||Tf||`.

This gain uses only an unsigned norm. It contains no information about the
sign being tested. The normalized balanced-bridge contrast becomes

`Re <f,Tf> / (||f|| ||Tf||)`.

For an exact eigenmode `Tf=lambda f`, the contrast is exactly

`sign(lambda)`.

Thus the level-43 negative mode produces a pi phase reversal and contrast
minus one. The level-44 positive mode produces zero relative phase and
contrast plus one. The predicted few-parts-per-million eigenvalue controls
the required response-arm gain, not the final sign-decision margin.

## Approximate-mode tolerance

Write `Tf=lambda f+r`, with `r` orthogonal to `f` and `||f||=1`. After unsigned
norm balancing, the contrast is

`lambda / sqrt(lambda^2+||r||^2)`.

Residual error reduces visibility but cannot reverse the sign. It therefore
creates an abstention region rather than a false sign, provided phase labels
and detector-port swaps are preregistered.

## New experimental bottleneck

The hard requirement is dynamic range before balancing. The level-44 response
must be distinguished from amplifier and reconstruction noise before applying
the large positive gain. If `||Tf||` is not above a preregistered noise bound,
the run abstains.

This is substantially better than demanding direct ppm-scale differential
photometry: the final observable is full-scale phase, while the small quantity
is isolated in a separate unsigned norm measurement.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_eigenvalue_sign_to_bridge_phase.py
```
