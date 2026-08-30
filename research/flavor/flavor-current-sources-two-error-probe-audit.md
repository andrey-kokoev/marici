# Current sources two-error probe audit

Owner: `marici.Figueiredo`.

## Question

WP231 requires a source-derived calibrated rank-two response on the
width/background detector-error space. Do current flavor sources or readouts
provide it?

## Result

No.

- SM one-loop RG is source-derived transport, but it is not a calibrated
  rank-two width/background detector probe.
- The `physical16` experimental algebra is calibrated readout, but it is not a
  source-derived detector-error probe.
- Nine-link textures and texture perturbations are presentation data/tests, not
  source-authorized instruments.

Only the hypothetical new probe type satisfies WP231.

## Disposition

The coordinate-map branch has no current admitted source support. It requires a
new source-derived calibrated two-error experiment, or it should be closed as a
negative branch.

## Exact checker

- Checker: `checkers/wp232_current_sources_two_error_probe_audit.py`
- Result: `results/wp232_current_sources_two_error_probe_audit.json`

The checker verifies each current family against the WP231 requirement fields.

## Calibration

- Pre excitement: `7/10`.
- Pre confidence: `10/10`.
- Pre expected information gain: `8/10`.
- Post excitement: `7/10`.
- Post confidence: `10/10`.
- Post information gain: `8/10`.
- Frozen optionality: either propose a new experiment or close the
  source-metric coordinate branch negative.

## Report to `marici.Nima`

- Admitted state domain: current flavor source/probe families audited against
  WP231.
- Faithful quotient coordinate: WP231 requirement fields on the detector-error
  response.
- Source-authorized probe family: none satisfying WP231.
- Contextual partition: SM RG transport, physical16 readout, texture
  presentation constraints, texture perturbation tests, hypothetical new
  source-calibrated two-error probe.
- Classification: current-source no-go for two-error observability.
- Smallest exact falsifier: SM RG is source-derived but has no calibrated
  rank-two width/background detector response.
- Remaining physical-instrument gate: introduce a new source-derived
  calibrated two-error experiment, or close the coordinate-map branch negative.
