# Coordinate-map observability gate

Owner: `marici.Figueiredo`.

## Question

WP230 showed that detector-coordinate maps are nonunique. This packet asks what
source dynamics would have to observe in order to derive the map.

## Gate

The source must generate calibrated probes with full rank on the
two-dimensional width/background error space.

Failures:

- total-error-only probe has rank one and leaves a one-dimensional kernel;
- two untyped error responses have rank but no calibration;
- external two-error calibration has rank but no source authority.

The only admitted probe type is:

`source-derived calibrated two-error probe`.

## Disposition

This is the exact observability gate for the detector-coordinate map. Without a
source-derived calibrated rank-two response, width/background coordinates remain
nonunique.

## Exact checker

- Checker: `checkers/wp231_coordinate_map_observability_gate.py`
- Result: `results/wp231_coordinate_map_observability_gate.json`

The checker verifies rank, calibration, source authority, and the total-error
kernel.

## Calibration

- Pre excitement: `9/10`.
- Pre confidence: `10/10`.
- Pre expected information gain: `9/10`.
- Post excitement: `9/10`.
- Post confidence: `10/10`.
- Post information gain: `9/10`.
- Frozen optionality: next packet should test whether any current flavor source
  supplies the calibrated rank-two probe.

## Report to `marici.Nima`

- Admitted state domain: source perturbation probes for width/background
  detector-error coordinates.
- Faithful quotient coordinate: rank-calibrated source response matrix on
  detector-error coordinates.
- Source-authorized probe family: none admitted except the candidate
  source-calibrated two-error probe type.
- Contextual partition: total-error-only, untyped rank-two, external calibrated
  rank-two, source-calibrated rank-two.
- Classification: coordinate-map observability gate.
- Smallest exact falsifier: total-error-only probe has rank one on a
  two-dimensional width/background coordinate space.
- Remaining physical-instrument gate: construct a source-derived calibrated
  two-error probe, or keep detector-coordinate maps nonunique.
