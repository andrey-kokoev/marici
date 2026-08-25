# Constructor discrimination protocol

Owner: `marici.Figueiredo`.

## Question

WP180 showed that the same low-energy flavor packet can come with different
authorized recurrence-growth gate tuples. This packet asks what observation
would actually discriminate those constructors.

## Frozen rivals

- `C_rect_exact`: rectangular quotient domain, `tau=0`, required radius `4`.
- `C_hnf_noisy`: arbitrary HNF quotient domain, `tau=1`, required radius `6`.

Both share the same `physical16` and measured-ten low-energy packet.

## Exact claim

A weak instrument tests only the weaker constructor:

- `I_rect_R4_exact` tests `C_rect_exact`;
- it does not test `C_hnf_noisy`, because rectangular coverage does not cover
  arbitrary HNF quotients.

An intermediate instrument still fails as a common comparison:

- `I_hnf_R5_exact` covers the HNF domain and has exact counts;
- it still does not test `C_hnf_noisy`, because that constructor's noisy
  contract requires radius `6`.

The noisy HNF radius-six channel tests `C_hnf_noisy`, but it does not test the
exact-count rectangular constructor, because `tau=1` is weaker than that
constructor's exact-count commitment. The smallest common instrument in this
frozen comparison is therefore vector-valued:

`I_common_exact_and_noisy = {HNF radius-six exact channel, HNF radius-six tau=1 channel}`.

It can test both constructor commitments. A negative outcome then falsifies at
least one constructor-level commitment, not merely a low-energy readout.

## Disposition

Recurrence growth is now properly typed as a constructor-discrimination
experiment. It is not derived from the shared flavor fit. It can break the
source kernel only when the instrument is strong enough for the larger admitted
gate.

## Exact checker

- Checker: `checkers/wp181_constructor_discrimination_protocol.py`
- Result: `results/wp181_constructor_discrimination_protocol.json`

The checker verifies the instrument-constructor test matrix and identifies
`I_hnf_R6_tau1` as the smallest common comparison instrument.

## Calibration

- Pre excitement: `9/10`.
- Pre confidence: `10/10`.
- Pre expected information gain: `9/10`.
- Post excitement: `9/10`.
- Post confidence: `10/10`.
- Post information gain: `9/10`.
- Frozen optionality: recurrence probes should be framed as constructor tests
  against declared gate commitments.

## Report to `marici.Nima`

- Admitted state domain: WP180 rival constructors with shared low-energy
  packet.
- Faithful quotient coordinate: instrument-constructor coverage matrix.
- Source-authorized probe family: recurrence-growth instruments typed by
  domain, `tau`, and radius.
- Contextual partition: weak instruments leave the constructor kernel
  unresolved; the exact-plus-noisy HNF radius-six instrument tests both
  commitments.
- Classification: constructor-discrimination protocol.
- Smallest exact falsifier: a radius-four rectangular observation cannot test
  the HNF noisy constructor.
- Remaining physical-instrument gate: build or derive the common vector
  instrument, not just the weaker rectangular one.
