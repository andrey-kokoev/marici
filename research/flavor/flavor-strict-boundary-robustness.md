# Strict boundary from robustness

Owner: `marici.Figueiredo`.

## Question

WP221 identified the strict-boundary rule as one of the smallest missing
detector targets. This packet asks whether that rule can be derived rather than
declared.

## Derivation

If detector acceptance must be robust under a positive perturbation margin,
then boundary touching is not acceptable. For target `1/4`:

- `1/5` has positive margin and passes;
- `1/4` has zero margin and fails robust acceptance;
- `1/3` has negative margin and fails.

Thus robust acceptance is exactly strict acceptance:

`error < target`.

## Disposition

This conditionally derives the strict-boundary rule from a robustness
requirement. It does not derive the full selector or the physical instrument.
The robustness requirement itself must still be admitted as source/detector
law, and the remaining detector fields are untouched.

## Exact checker

- Checker: `checkers/wp222_strict_boundary_robustness.py`
- Result: `results/wp222_strict_boundary_robustness.json`

The checker verifies that non-strict comparison accepts the touching falsifier,
while robust comparison rejects it exactly because the margin is zero.

## Calibration

- Pre excitement: `8/10`.
- Pre confidence: `10/10`.
- Pre expected information gain: `8/10`.
- Post excitement: `8/10`.
- Post confidence: `10/10`.
- Post information gain: `8/10`.
- Frozen optionality: next structural target is channel-exchange action.

## Report to `marici.Nima`

- Admitted state domain: detector comparisons with target `1/4` and robustness
  under positive perturbation.
- Faithful quotient coordinate: comparison outcome plus margin sign; not a new
  `physical16` selector.
- Source-authorized probe family: conditional robust detector comparisons.
- Contextual partition: below target, touching target, above target.
- Classification: conditional structural detector-rule derivation.
- Smallest exact falsifier: touching case `error=1/4`, accepted non-strictly
  but rejected by robust margin.
- Remaining physical-instrument gate: admit robustness as a source/detector
  requirement and separately derive channel exchange, sentinel, executability,
  and calibration.
