# Interface and geometry review; concrete dynamics discriminator

## Decisions

Accepted `observation-resource-interface` and `geometric-realization-binding` at their declared model scope.

The observation contract supplies preparations, operation/outcome maps, complete records, positive-likelihood filtering and separate energy/photon/readiness ledgers. Its physical preparation and calibration slots are the next instrument/protocol tasks, rather than missing mathematical interface definitions.

The geometry supplies a concrete Fock/memory source, coherent-state and finite-detector maps, the occupation-basis metric, retained port/time-bin ordering and a composed instrument comparison. The all-sector statement follows from the written symmetric-tensor/direct-sum construction; finite-sector tests corroborate its implementation. Thirty additional basis/prefix squares compare the independent field-interface implementation against the ten-mode realization through all three rounds.

`passive-port-fock-memory.v1` is added as a versioned supplement to the base source register. Its Fock/CP ingredients are explicitly imported. It does not identify the original Bool, exchange or marked137 sources.

Dynamics selection remains open: linear creation covariance supplies a conditional uniqueness theorem, while the local nonlinear phase rival shows why that premise needs source justification or a discriminating measurement.

## A usable phase-rival test

Prepare the same returning cavity mode at nominal coherent intensities `lambda1=1/4` and `lambda2=1`, with other active inputs vacuum. Measure complex field means A1 and A2 using phase-referenced readout. Use

`S = |A2| / (2 |A1|)`.

The denominator must have a positive confidence lower bound. A common unknown complex multiplicative readout gain cancels. Photon-number counts do not measure this statistic: the phase rival preserves their distributions.

The prediction design requires independent bounds

```
lambda1 in [0.24,0.26]
lambda2 in [0.99,1.01]
relative readout magnitude gain in [0.99,1.01].
```

These are required calibration bounds, not claimed measurements. Propagating the whole box gives:

| Model | Certified enclosing interval for S |
|---|---|
| Passive linear lift | [0.9659087955, 1.0359682514] |
| Active-port phase rival, chi*t=pi/2 | [0.2070725914, 0.2405894075] |

The decimal rival endpoints are rounded outward for display. The checker stores exact rational bounds obtained from factorial-series remainder bounds for the exponential and integer-square-root bounds. Both intervals remain separated by 1/2 after adding the charter's 1/100 discrepancy allowance.

The passive formula is `r*sqrt(lambda2/lambda1)/2`; the rival multiplies it by `exp(-2*(lambda2-lambda1))`. An unrestricted between-setting gain could mimic the exponential factor, so the relative-gain bound is part of the test, not a parameter to fit afterward.

The test distinguishes the named phase rival. Small phases, different source laws and actual data coverage remain separate questions. The next protocol can now specify the field-mean estimator, simultaneous intervals, trial count and calibration/validation split around this concrete statistic.

Contract: `contracts/physics-phase-discriminator.v1.json`.

## Formal freshness repaired by compilation

Ran a fresh safe Cubical/guarded Agda closure of Sontag's unchanged `RetainedHistoryTransport.agda`, ignoring interfaces. Compilation passed with stable inputs and the complete current inventory of 2194 files.

The independent receipt is `results/physics-retained-history-agda-v1.json`. Sontag's original receipt and manifests remain intact; the prior inventory blocker is retained as a historical observation.

Another unrelated module appeared after this successful compile. The old equality-to-all-live-files test would invalidate an unchanged proof indefinitely during parallel research. The explicit successor policy `contracts/physics-formal-freshness-policy.v2.json` instead preserves every recorded source hash and inventory entry, compiler/runner identity, receipt and log hashes, and checks resolution of every compiler-traced module against the live include paths. New unrelated files are allowed; changed source, missing entries, shadows and ambiguous imports fail. Temporary-directory controls verify both unrelated-file acceptance and import-shadow rejection.

The receipt is therefore backed by an actual fresh compiler run and dependency-resolution checks, rather than by a blanket ban on other researchers adding files.

## Verification

```
python research/nima/checkers/refresh_physics_retained_history_receipt.py
python research/nima/checkers/check_physics_interface_geometry_admission.py
python research/aspect/scc/scc.py check physics-programme-v18
```

The admission checker verifies the source-register supplement, thirty independently implemented three-round basis squares and rigorous nuisance-box separation. The existing observation, geometry, dynamics and target tests remain in the central SCC run.
