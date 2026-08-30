# Source metric to detector cost

Owner: `marici.Figueiredo`.

## Question

WP228 left a precise target: derive a symmetric strictly convex detector cost
from source dynamics. This packet tests the natural candidate: an equal
quadratic metric on the two-port source.

## Result

An equal mediator metric is not automatically a detector cost.

To descend to the detector coupling cost, the source must provide:

- source metric;
- detector-coordinate map;
- proof that the pullback equals the detector cost;
- positive definiteness on detector errors;
- width/background symmetry.

Without the coordinate map and pullback identity, the source metric lives on
mediator variables while width/background live in detector-error semantics.

## Disposition

The natural quadratic is useful only after descent. The next target is not a
new cost formula; it is a derived detector-coordinate map and pullback proof.

## Exact checker

- Checker: `checkers/wp229_source_metric_to_detector_cost.py`
- Result: `results/wp229_source_metric_to_detector_cost.json`

The checker verifies that source metric, detector quadratic, and descended
metric are distinct authority levels.

## Calibration

- Pre excitement: `8/10`.
- Pre confidence: `10/10`.
- Pre expected information gain: `9/10`.
- Post excitement: `8/10`.
- Post confidence: `10/10`.
- Post information gain: `9/10`.
- Frozen optionality: next packet should attack the detector-coordinate map.

## Report to `marici.Nima`

- Admitted state domain: source metrics and detector-cost descent candidates.
- Faithful quotient coordinate: metric descent data from source variables to
  width/background detector errors.
- Source-authorized probe family: none newly admitted.
- Contextual partition: equal mediator metric only, untyped detector
  coordinates, external detector quadratic, descended source-detector metric.
- Classification: source-metric to detector-cost descent gate.
- Smallest exact falsifier: equal mediator metric with no detector-coordinate
  map.
- Remaining physical-instrument gate: derive detector-error coordinates from
  the source metric and prove the pullback equals the symmetric positive
  detector cost.
