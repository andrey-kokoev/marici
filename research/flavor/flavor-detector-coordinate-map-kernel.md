# Detector-coordinate map kernel

Owner: `marici.Figueiredo`.

## Question

WP229 showed that a source metric needs a detector-coordinate map before it can
descend to a detector cost. This packet tests whether that coordinate map is
unique.

## Result

No. The same equal two-port source metric admits rival detector-coordinate
maps:

- symmetric map: `1/10+1/10`;
- width-heavy map: `3/20+1/20`;
- background-heavy map: `1/20+3/20`.

All can be paired with a formal pullback identity unless the coordinate map
itself is source-derived. Therefore pullback notation is not enough; the map is
the authority-bearing object.

## Disposition

The detector cost is still coordinate-gauge data until the detector-coordinate
map is derived from source dynamics. This is the precise kernel under the
source-metric route.

## Exact checker

- Checker: `checkers/wp230_detector_coordinate_map_kernel.py`
- Result: `results/wp230_detector_coordinate_map_kernel.json`

The checker verifies that the same source metric supports rival coordinate
maps and that only a source-derived symmetric map is admitted.

## Calibration

- Pre excitement: `9/10`.
- Pre confidence: `10/10`.
- Pre expected information gain: `9/10`.
- Post excitement: `9/10`.
- Post confidence: `10/10`.
- Post information gain: `9/10`.
- Frozen optionality: next packet should determine whether a source dynamics
  can derive the coordinate map or whether this branch is closed negative.

## Report to `marici.Nima`

- Admitted state domain: detector-coordinate maps from the equal two-port
  source metric.
- Faithful quotient coordinate: source metric plus source-derived coordinate
  map, not metric alone.
- Source-authorized probe family: none newly admitted.
- Contextual partition: symmetric map, width-heavy map, background-heavy map,
  source-derived symmetric map.
- Classification: detector-coordinate map kernel.
- Smallest exact falsifier: same equal source metric with symmetric map
  `1/10+1/10` and width-heavy map `3/20+1/20`.
- Remaining physical-instrument gate: derive the detector-coordinate map from
  source dynamics; otherwise the convex detector cost is coordinate-gauge data.
