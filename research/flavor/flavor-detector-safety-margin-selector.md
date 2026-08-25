# Detector safety-margin selector

Owner: `marici.Figueiredo`.

## Question

WP205 showed that minimal cost alone selects a near-margin detector, not
WP203's `1/10,1/10` constants. This packet adds a safety-margin requirement:

`width + background <= 1/5`.

Does that select the WP203 detector?

## Exact claim

With safety cap `1/5`, the near-margin detector fails:

`1/5 + 1/5 = 2/5`.

The WP203 detector passes exactly:

`1/10 + 1/10 = 1/5`.

A sharper detector also passes:

`1/20 + 1/20 = 1/10`.

Then minimal sharpness cost among safe detectors selects the WP203 constants
`1/10,1/10`.

## Disposition

This conditionally derives the detector constants, but shifts the authority
gate to the safety cap. A real explanation must derive why the safety cap is
`1/5`.

## Exact checker

- Checker: `checkers/wp206_detector_safety_margin_selector.py`
- Result: `results/wp206_detector_safety_margin_selector.json`

The checker evaluates the near-margin, sharp, and sharper radius-six detector
candidates using exact rational arithmetic.

## Calibration

- Pre excitement: `9/10`.
- Pre confidence: `9/10`.
- Pre expected information gain: `9/10`.
- Post excitement: `9/10`.
- Post confidence: `10/10`.
- Post information gain: `9/10`.
- Frozen optionality: detector constants are explained only if the safety cap
  is explained.

## Report to `marici.Nima`

- Admitted state domain: radius-six detector candidates with safety cap.
- Faithful quotient coordinate: total error and sharpness cost.
- Source-authorized probe family: conditional on safety-cap authority.
- Contextual partition: near-margin fails; sharp and sharper pass; minimal cost
  selects sharp.
- Classification: conditional detector-constant selector.
- Smallest exact falsifier: without the `1/5` safety cap, WP205 selects the
  near-margin detector.
- Remaining physical-instrument gate: derive the `1/5` safety cap.
