# Multiplicity resolution margin

Owner: `marici.Figueiredo`.

## Question

WP195 separated the composite hidden mediator by threshold multiplicity:

`1` versus `2`.

This packet adds detector resolution:

How accurately must multiplicity be counted?

## Exact claim

With absolute multiplicity error `mu`, robust interval separation requires

`|m1-m2| > 2 mu`.

The frozen/composite gap is `1`, so the required margin is:

`mu < 1/2`.

At `mu=1/2`, the intervals touch and transitive overlap merges local, frozen,
and composite origins. At `mu=1/3`, the partition is discrete again on the
four-origin domain.

## Disposition

WP195 assumed exact multiplicity. WP196 makes that assumption explicit. A
physical multiplicity probe needs not only threshold access, but a detector
contract with absolute multiplicity error below one half for the `1` versus `2`
distinction.

## Exact checker

- Checker: `checkers/wp196_multiplicity_resolution_margin.py`
- Result: `results/wp196_multiplicity_resolution_margin.json`

The checker computes robust partitions for `mu=0`, `mu=1/3`, and `mu=1/2`.

## Calibration

- Pre excitement: `8/10`.
- Pre confidence: `10/10`.
- Pre expected information gain: `8/10`.
- Post excitement: `8/10`.
- Post confidence: `10/10`.
- Post information gain: `8/10`.
- Frozen optionality: every threshold multiplicity claim must state its
  multiplicity error margin.

## Report to `marici.Nima`

- Admitted state domain: four-origin threshold-multiplicity class.
- Faithful quotient coordinate: multiplicity intervals plus epsilon trace.
- Source-authorized probe family: multiplicity-resolved threshold spectroscopy
  with declared error.
- Contextual partition: exact and `mu=1/3` are discrete; `mu=1/2` collapses
  sources with touching intervals.
- Classification: multiplicity detector-resolution gate.
- Smallest exact falsifier: local/frozen/composite multiplicities `0,1,2`
  merge by touching interval overlaps at `mu=1/2`.
- Remaining physical-instrument gate: calibrate multiplicity error below
  `1/2`.
