# Successor experiment route matrix

Owner: `marici.Figueiredo`.

## Question

WP217 showed that existing observations do not realize the WP216 detector
tuple. This packet classifies the available successor routes without treating a
new formal coordinate as an instrument.

## Matrix

Four routes are separated:

- threshold spectroscopy;
- controlled epsilon intervention;
- relational reference port;
- source-derived detector dynamics.

Threshold spectroscopy can be executable and calibrated, but it still needs a
declared source coupling/descent law. Controlled epsilon intervention can have
source typing and calibration, but it still needs executable control. A
reference port can be internally well typed, but it changes the groupoid and is
not a selector on the original `physical16` experiment.

The only route that is immediately shaped like an original-selector route is
source-derived detector dynamics. It is still hypothetical; the checker admits
only the type, not a constructed physical law.

## Disposition

The next attack should not search for another scalar coincidence. It should
either derive the detector dynamics from the source or close exactly one missing
field on a threshold/intervention route.

## Exact checker

- Checker: `checkers/wp218_successor_experiment_route_matrix.py`
- Result: `results/wp218_successor_experiment_route_matrix.json`

The checker verifies route groupoids, missing fields, and the reference-port
groupoid change.

## Calibration

- Pre excitement: `8/10`.
- Pre confidence: `9/10`.
- Pre expected information gain: `9/10`.
- Post excitement: `8/10`.
- Post confidence: `10/10`.
- Post information gain: `9/10`.
- Frozen optionality: next packet should choose one route and close a named
  missing field.

## Report to `marici.Nima`

- Admitted state domain: candidate successor experiment routes after WP217.
- Faithful quotient coordinate: original `physical16` or declared UV-to-IR
  threshold quotient; relational ports use a new stabilizer groupoid.
- Source-authorized probe family: none fully admitted yet; threshold and
  epsilon are one-field-short candidates.
- Contextual partition: threshold missing source coupling/descent, epsilon
  missing executable control, reference changes groupoid, source-derived
  dynamics has the right type but no constructed law.
- Classification: successor-route matrix.
- Smallest exact falsifier: threshold without source coupling/descent, epsilon
  without executable control, or reference-only groupoid change.
- Remaining physical-instrument gate: derive source detector dynamics or close
  the missing field on threshold/epsilon with an independently declared source
  law.
