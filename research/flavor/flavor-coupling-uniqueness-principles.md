# Coupling uniqueness principles

Owner: `marici.Figueiredo`.

## Question

WP226 showed that a coupled source-detector action derives exchange only if the
source uniquely entails the coupling. This packet asks what kind of principle
could provide that uniqueness.

## Result

Cap-only is insufficient. The one-fifth cap admits all three couplings:

- width-heavy: `3/20 + 1/20`;
- equal: `1/10 + 1/10`;
- background-heavy: `1/20 + 3/20`.

External exchange symmetry selects the equal split, but it is not source
authority.

The minimal typed uniqueness principle is:

`source-derived symmetric strictly convex cost`.

Symmetry makes the equal split stationary; strict convexity makes it unique;
source derivation gives authority.

## Disposition

The exchange problem is now reduced to a precise source-law target: derive a
symmetric strictly convex detector-coupling cost. Without that, asymmetric
couplings remain legal rivals.

## Exact checker

- Checker: `checkers/wp227_coupling_uniqueness_principles.py`
- Result: `results/wp227_coupling_uniqueness_principles.json`

The checker verifies cap rivals and the minimal principle needed for unique
equal coupling.

## Calibration

- Pre excitement: `9/10`.
- Pre confidence: `9/10`.
- Pre expected information gain: `9/10`.
- Post excitement: `9/10`.
- Post confidence: `10/10`.
- Post information gain: `9/10`.
- Frozen optionality: next packet should test candidate convex costs for source
  derivation rather than optimize arbitrary functions.

## Report to `marici.Nima`

- Admitted state domain: width/background couplings saturating the one-fifth
  cap.
- Faithful quotient coordinate: coupling split plus source-derived uniqueness
  principle.
- Source-authorized probe family: none newly admitted.
- Contextual partition: cap-only rivals, external exchange, source-derived
  symmetric strictly convex cost.
- Classification: coupling uniqueness principle audit.
- Smallest exact falsifier: cap-only admits width-heavy, equal, and
  background-heavy couplings with the same source.
- Remaining physical-instrument gate: derive a symmetric strictly convex
  detector-coupling cost from the source action.
