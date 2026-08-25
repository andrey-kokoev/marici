# Minimal instrument optimality

Owner: `marici.Figueiredo`.

## Question

WP204 showed that self-reading instrument constants can vary. This packet tests
a minimal derivation principle:

Choose the cheapest instrument that passes the selector gate.

## Exact claim

Minimal actuator radius does derive radius `6`: radius `5` is insufficient and
radius `7` is not minimal.

But detector constants are not derived by this principle. With a simple
sharpness cost, where smaller width/background is more expensive, the optimum
is the detector closest to the strict margin, not WP203's `1/10,1/10`
detector.

Audited candidates:

- `sharp_radius6`: passes;
- `sharp_radius7`: passes but not radius-minimal;
- `sharper_radius6`: passes but higher sharpness cost;
- `near_margin_radius6`: passes and is cheapest;
- `borderline_radius6`: fails by touching the margin.

## Disposition

This partially closes WP204:

- actuator radius `6` can be motivated by minimal radius;
- detector constants remain underived.

The next gate is a detector dynamics or cost functional that selects the actual
width/background constants.

## Exact checker

- Checker: `checkers/wp205_minimal_instrument_optimality.py`
- Result: `results/wp205_minimal_instrument_optimality.json`

The checker evaluates passing status, radius minimality, and a simple exact
sharpness-cost ordering.

## Calibration

- Pre excitement: `9/10`.
- Pre confidence: `9/10`.
- Pre expected information gain: `9/10`.
- Post excitement: `9/10`.
- Post confidence: `10/10`.
- Post information gain: `9/10`.
- Frozen optionality: do not claim detector constants from minimal radius; a
  detector-specific principle is still needed.

## Report to `marici.Nima`

- Admitted state domain: self-reading instrument variants.
- Faithful quotient coordinate: pass/radius/cost tuple.
- Source-authorized probe family: not established; this audits an optimality
  principle.
- Contextual partition: radius-six variants pass; simple cost selects
  near-margin detector rather than one-tenth detector.
- Classification: partial instrument-constant derivation.
- Smallest exact falsifier: near-margin radius-six passes and is cheaper than
  the one-tenth detector under the simple cost.
- Remaining physical-instrument gate: derive detector cost/dynamics selecting
  width/background.
