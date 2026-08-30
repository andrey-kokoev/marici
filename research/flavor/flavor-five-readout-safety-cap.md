# Five-readout safety cap

Owner: `marici.Figueiredo`.

## Question

WP206 moved the detector-constant problem to a safety cap:

`width + background <= 1/5`.

This packet asks whether a repeated-readout law can derive that cap.

## Exact claim

A five-readout detector with at most one bad subchannel gives bad fraction

`1/5`.

This derives the WP206 safety cap conditionally.

Hostile controls:

- four copies with one bad subchannel gives `1/4`, too large;
- five copies with two bad subchannels gives `2/5`, too large.

## Disposition

This conditionally explains the `1/5` cap, but shifts authority to the detector
architecture:

Why five copies? Why at most one bad subchannel?

Without that readout law, the cap remains stipulated.

## Exact checker

- Checker: `checkers/wp207_five_readout_safety_cap.py`
- Result: `results/wp207_five_readout_safety_cap.json`

The checker verifies the exact rational bad fractions for the audited readout
laws.

## Calibration

- Pre excitement: `9/10`.
- Pre confidence: `10/10`.
- Pre expected information gain: `9/10`.
- Post excitement: `9/10`.
- Post confidence: `10/10`.
- Post information gain: `9/10`.
- Frozen optionality: derive or admit the five-copy one-bad law before claiming
  the detector constants.

## Report to `marici.Nima`

- Admitted state domain: detector readout redundancy laws.
- Faithful quotient coordinate: bad subchannel fraction.
- Source-authorized probe family: five-readout detector only if admitted.
- Contextual partition: five/one passes; four/one and five/two fail.
- Classification: conditional safety-cap derivation.
- Smallest exact falsifier: four copies with one bad subchannel gives `1/4`.
- Remaining physical-instrument gate: derive the five-copy one-bad detector
  architecture.
