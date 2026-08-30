# Directional response certificate

## Result

The level-44 experiment does not require 44 independent full-operator error
bounds.

Freeze one normalized source-derived test mode `f` and its ideal response
`Tf`. Before applying unsigned norm gain, coherently tomograph the complete
realized response `T_hat f`. Then

`|Re <f,(T_hat-T)f>| <= ||(T_hat-T)f||`.

Therefore a confidence upper bound below `1e-6` on the response-vector
residual discharges the entire systematic quadratic-form budget.

This certificate is end-to-end. It automatically includes filter mismatch,
phase error, channel leakage, endpoint-coupler error, and coherent summation
error as they act on the actual preregistered mode.

## Why vector tomography is required

A scalar bridge measurement alone can miss an error orthogonal to `f`. That
error may later contaminate unsigned norm balancing and reduce phase
visibility. Full coherent response tomography detects it and bounds its norm.

The order is fixed:

1. freeze `f` and the ideal vector `Tf` from the source model;
2. tomograph the unamplified realized vector `T_hat f`;
3. accept the transfer only when the residual upper bound is below `1e-6`;
4. apply unsigned norm balancing;
5. acquire the phase-reversed sign record.

If the residual is unresolved, the run abstains. Measuring after the large
balancing gain is not a substitute because it hides the pre-gain transfer
error under the same amplification.

## Implication

The difficult calibration scales with the dimension of the response field,
not with all entries of the 44-channel operator. The experiment tests one
source-selected direction with a complete vector certificate, which is the
minimal sufficient instrument for the 43/44 sign prediction.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_directional_response_certificate.py
```
