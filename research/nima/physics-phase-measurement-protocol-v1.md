# Fixed-sample phase measurement protocol candidate

Status: **pending instrument-owner review**. This is a one-target, one-rival protocol candidate, not a completed protocol for both selected physical targets. No apparatus authorization, calibration bundle or measured data is supplied.

Contract: `contracts/physics-phase-measurement-protocol.v1.json`.
Checker: `checkers/check_physics_phase_measurement_protocol.py`.

## Preparation, measurement and records

Use the previously specified coherent returning-mode preparations at nominal intensities 1/4 and 1, other active inputs vacuum, and the same one-round cavity setting. Measure an unclipped phase-referenced complex field sample on every shot, in fixed independently calibrated units. Photon counts are not a replacement for field means.

Take exactly **8,000,000 shots per setting**, arranged in fixed setting-1/setting-2 pairs. Each shot requires a fresh independent preparation. Retain attempted-shot identifiers, pair identifiers, setting, timestamps, raw X/Y, validity, calibration, preparation and instrument references. No clipping, postselection, imputation, replacement shots, fitted background subtraction or outcome-driven repeats are allowed. Missing/invalid measurements abort the run, but their records remain in the manifest. An aborted run supports no exclusion decision.

Calibration is separate and frozen before validation. It must certify the intensity/relative-gain boxes already specified in the prediction contract, a common gain times port-transfer magnitude of at least 1/2, complex bias at most 1/500 per setting, and variance at most 1 for each real coordinate. Joint calibration failure probability is at most 1/200. These are requirements, not existing certificates. Calibration cannot assume passive coherent Gaussian statistics for the nonlinear rival.

The independent-shot, fixed-setting-mean assumptions and drift/reset controls need instrument-owner justification. A small empirical sample variance alone is not a distribution-free upper variance certificate. No guarantee applies if those assumptions fail.

## Simultaneous confidence interval

Compute the four coordinate arithmetic means. With n=8,000,000, coordinate variance V<=1 and coordinate radius d=1/100, Chebyshev and the union bound give

`P(any of four coordinate errors > d) <= 4 V/(n d²) = 1/200`.

The complex mean error, including bounded bias, is therefore at most

`R = sqrt(2)/100 + 1/500 <= 0.0161421357`.

Combining calibration and validation failure budgets gives simultaneous coverage at least 99/100, conditional on the declared acquisition assumptions. Gaussianity is not required. The conservative sample count is deliberate; a smaller design would require a separately justified sharper noise class.

For measured mean magnitudes m1,m2, set `Lj=max(0,mj-R)`, `Uj=mj+R`. If L1 is zero, report unidentifiable. Otherwise use

`I = [L2/(2 U1), U2/(2 L1)]`.

Arithmetic endpoints must round outward. Compare I with each full nuisance prediction interval expanded by the original 1/100 model-discrepancy allowance. Disjointness excludes only that named model. Both excluded means neither model; neither excluded means inconclusive. Compatibility does not establish uniqueness or justify creation covariance.

## Finite-sample discrimination margin

The independently required signal floor supplies a first-setting mean lower bound for each model, including Kerr attenuation. On the simultaneous coverage event, the estimated magnitudes can differ from truth by R and their confidence endpoints by **2R**. Propagating that factor, rather than treating the estimate as exact, yields:

- Passive-law confidence interval lower endpoint >= **0.79520**.
- Named phase-rival confidence interval upper endpoint <= **0.45154**.

Both are on opposite sides of 1/2; each excludes the other model's expanded prediction interval. This is a conditional finite-sample separation guarantee, not a simulated or measured experimental result.

The checker uses rational enclosures for square roots and exponential tails. It rejects an underpowered count, inflated noise bound and overspent failure budget, checks denominator abstention, and tests passive-compatible, rival-compatible and neither-model synthetic controls. All fixtures are explicitly synthetic.

## Remaining gates

1. Aspect/instrument-owner review of this one-target protocol and its physical readout/preparation/reset authority.
2. Independent calibration and variance/bias/stationarity evidence, with a frozen provenance manifest and no validation leakage.
3. A separate complete-count/dead-time detector protocol; this candidate does not close the programme-wide empirical-protocol node.
4. Authorized acquisition, record-manifest validation, and execution of the predeclared decision rule.

Verification:

```
python research/nima/checkers/check_physics_phase_measurement_protocol.py
python research/aspect/scc/scc.py check physics-programme-v18
```
