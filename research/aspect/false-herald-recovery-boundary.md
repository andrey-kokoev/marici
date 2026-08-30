# False heralds destroy the exact conditional reverse arrow

## A small false-positive fraction is a qualitative defect

Suppose the ideal heralded recovery accepts the correct state, but a conditional
fraction `epsilon` of accepted events are actually loss events reconstructed as
`|0>`. The reported conditional state is then a mixture of the intended input
and `|0>` contamination.

For `epsilon=1/100`, the three probe fidelities are:

- `|0>`: `1`;
- `|1>`: `99/100`;
- equal superposition: `199/200`.

Their average is `199/200`, which looks excellent. Yet the exact reverse-arrow
claim is already false, and the worst-case infidelity is `1/100`. The `|0>`
probe alone is completely blind to the defect.

## Redundant heralding suppresses but does not repair

If two independent herald detectors must agree, a false-positive probability
`d` can fall from `d` to `d^2`. For `d=1/100`, this improves the worst-case
infidelity from `1/100` to `1/10000` under the ideal independence model.
It does not restore exactness: every nonzero contamination leaves a nonzero
worst-case error.

This distinguishes:

- proof of an exact conditional constructor;
- a high-fidelity approximate constructor;
- a statistical upper bound on false acceptance.

The second and third are experimentally valuable but cannot be silently
promoted to the first.

## Optical instrument

Use a spanning polarization set, time-tag every herald and output event, and
include a deliberately blocked-signal run that directly measures accepted
false heralds. Redundant detectors should retain separate event streams so the
independence assumption can be tested rather than imposed. Report worst-case
conditional fidelity and accepted false-event fraction, not average fidelity
alone.

## Claim boundary

The checker uses a fixed `|0>` contamination state and independent redundant
false heralds. State-dependent dark counts, afterpulsing, common-mode pickup,
and finite-sample confidence bounds remain open.

## Verification

```text
python research/aspect/checkers/check_false_herald_recovery_boundary.py
```
