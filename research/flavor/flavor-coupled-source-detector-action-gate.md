# Coupled source-detector action gate

Owner: `marici.Figueiredo`.

## Question

WP225 showed that source-label automorphisms do not act on detector-error
semantics. This packet tests the next repair: add a coupled source-detector
action.

## Gate

A formal coupled action must include:

- source action;
- detector error bundle;
- coupling term;
- exchange automorphism;
- descent to detector quotient.

But that still is not enough for derivation. If the same source action admits
rival detector couplings, then the coupling is glued on externally. Exchange is
derived only when the source action uniquely entails the coupling.

## Disposition

This blocks a likely overclaim. A coupled source-detector action is useful only
if coupling uniqueness is source-derived. Otherwise it is just WP203-style
self-reading declaration in a different notation.

## Exact checker

- Checker: `checkers/wp226_coupled_source_detector_action_gate.py`
- Result: `results/wp226_coupled_source_detector_action_gate.json`

The checker verifies the formal coupled-action fields and the rival-coupling
kernel.

## Calibration

- Pre excitement: `8/10`.
- Pre confidence: `9/10`.
- Pre expected information gain: `9/10`.
- Post excitement: `8/10`.
- Post confidence: `10/10`.
- Post information gain: `9/10`.
- Frozen optionality: next target is coupling uniqueness, not merely writing a
  coupled action.

## Report to `marici.Nima`

- Admitted state domain: candidate coupled source-detector actions.
- Faithful quotient coordinate: source action plus detector coupling modulo
  rival couplings with the same source.
- Source-authorized probe family: none newly admitted unless coupling
  uniqueness is derived.
- Contextual partition: source-only, glued detector coupling, source-derived
  unique coupling.
- Classification: coupled-action derivation gate.
- Smallest exact falsifier: same source action with rival detector couplings,
  one exchange-symmetric and one asymmetric.
- Remaining physical-instrument gate: derive coupling uniqueness from the
  source action; otherwise exchange remains an appended detector law.
