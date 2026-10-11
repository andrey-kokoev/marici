# Actual operational partial sums: norm-defect convergence

Continuation of `operational-unitary-half-turn-attempt.md`.

## What is now connected

`agda/TickDenseTrigCutoffs.agda` proves the missing parity/cutoff alignment. For every rational q and natural N, summing the dense cosine and sine sequences through degree `2N+1` gives exactly `cosinePartialSum q N` and `sinePartialSum q N`. Odd cosine coefficients and even sine coefficients vanish. Neither equality is inferred from samples. Fresh safe Agda closure passes.

`agda/TickOperationalTrigResidual.agda` combines this alignment with the normalized coefficient cancellation and the existing `AbsoluteTaylorSeriesMultiplication` residual machinery. It proves:

1. The two triangular Cauchy products sum to one.
2. The actual operational partial-sum norm defect equals the sum of the two triangular residuals.
3. Multiplying an exponential term by a cosine/sine derivative weight cannot increase its magnitude bound.
4. The already-constructed exponential majorant therefore bounds both dense trigonometric sequences.
5. The library's sharp geometric residual estimate gives, for every fixed rational q,

   `|cosinePartialSum(q,N)^2 + sinePartialSum(q,N)^2 - 1| <= K(q) * precision(N)`.

Here `T(q)` is the scale of `preferredExponentialMajorant q`, and `K(q)` is twice `fourfoldProductCoefficient T(q) T(q)`. A constructed Archimedean exponent `e(q)` absorbs this coefficient, giving the theorem `norm-defect-vanishes`:

   `|normDefect(q,e(q)+n)| <= precision(n)`.

No unproved majorant premise is left in that fixed-rational partial-sum theorem. This is a quantitative convergence result for the actual operational sums, not just a formal power-series calculation.

## Verification

- `TickDenseTrigCutoffs`: fresh safe Agda closure passes.
- `TickOperationalTrigResidual`: safe Agda check with cached dependencies passes.
- Fresh closure of the latter timed out after 600 seconds while rebuilding dependencies; the final logged module was `CompletionUnaryDescent`. This run reported no theorem rejection, but it is not a completed fresh verification.

Both runs and their dependency hashes are retained separately under `results/Tick*-fresh.json` and `results/Tick*-cached.json`. The source modules and predecessor export are unchanged by verification.

## Remaining transfer

The modulus e(q) is constructed separately for each rational q. It must not be applied uniformly to the moving rational approximations of a completion input without another proof. Two routes are available:

- compare all exponential terms at bounded inputs with the exponential terms at one positive radius, obtaining a single majorant and absorption exponent for that entire input bound; then instantiate the existing common-input controls and their error budget;
- first prove the rational completion-valued identity and transport it using quantitative sine/cosine approximation.

The first route can now reuse the actual partial-sum alignment and residual identity without rebuilding finite combinatorics. The required completion claim is still `ScheduledNormBound`; that certificate, the pi endpoint and metric regularity have not been constructed here.

The unitary half-turn attempt therefore remains **+-**. The predecessor's standard-semantics ++ remains valid and unchanged.

## Commands

```text
python research/nima/checkers/check_operational_trig_residual.py --cached
python research/nima/checkers/check_operational_trig_residual.py --module TickDenseTrigCutoffs --timeout 180
python research/nima/checkers/check_operational_trig_residual.py --module TickOperationalTrigResidual --timeout 600
python research/nima/checkers/record_operational_trig_residual_attempt.py
python research/nima/checkers/check_completion_refinement_net.py
```
