# Readout drift can fake a coherence revival

## An uncalibrated witness can reverse the conclusion

Take a genuinely monotone sample contrast sequence

```text
1, 1/2, 1/4.
```

Let the readout gain over the same acquisitions be

```text
1, 1, 4.
```

The raw measured contrast is then `1, 1/2, 1`, which appears to decrease and
revive. Nothing returned from a hidden sample memory; the detector became four
times more responsive.

An interleaved stable reference pair experiences the same gain and reports
`1, 1, 4`. Dividing sample contrast by reference response recovers the monotone
sequence exactly. In this scalar pilot, a simultaneous reference changes the
verdict from apparent non-Markovianity to ordinary monotone decay.

## A witness needs an observation contract

Trace-distance revival is a valid memory witness only when preparation and
measurement maps are frozen or calibrated across times. The contract should
include:

- randomized or interleaved acquisition order;
- contemporaneous spanning reference probes;
- raw event retention;
- gain and analyzer-frame uncertainty;
- a rule for excluding intervals where the reference margin collapses.

A scalar reference corrects scalar gain only. Analyzer rotation or anisotropic
response requires a spanning polarization reference and a calibrated transfer
matrix. Calibration itself does not prove Markovianity; it removes one explicit
alternative explanation for apparent revival.

## Optical instrument

Interleave the memory probes with a bypassed reference polarization pair at
every delay. Route both through the same analyzer and time-tagging chain. A
source monitor upstream of the memory separates preparation drift from analyzer
drift. Permute delay order so slow gain changes cannot alias into memory time.

## Claim boundary

The checker treats a common scalar multiplicative gain known exactly from a
stable reference. Additive background, nonlinear saturation, analyzer rotation,
reference drift, and finite-sample uncertainty remain open.

## Verification

```text
python research/aspect/checkers/check_readout_drift_fakes_coherence_revival.py
```
