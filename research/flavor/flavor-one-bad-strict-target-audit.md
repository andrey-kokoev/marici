# One-bad strict target audit

Owner: `marici.Figueiredo`.

## Question

WP208 left two assumptions:

- tolerate one bad subchannel;
- require strict margin below `1/4`.

This packet audits the fault-contract logic behind them.

## Exact claim

If the detector must tolerate the minimal nonzero number of bad subchannels,
then the fault target is one bad subchannel.

If interval separation is strict, touching at `1/4` is rejected.

Therefore:

- one bad, non-strict `1/4` target -> four copies;
- one bad, strict `1/4` target -> five copies;
- two bad, strict `1/4` target -> nine copies.

This explains why WP208 selected five under the one-bad strict contract.

## Disposition

The assumptions are reduced, not eliminated. The remaining physical gates are:

- why the detector's fault model is one bad subchannel;
- why the safety target is `1/4`.

Strictness itself is inherited from the interval-separation rule used
throughout the branch.

## Exact checker

- Checker: `checkers/wp209_one_bad_strict_target_audit.py`
- Result: `results/wp209_one_bad_strict_target_audit.json`

The checker computes minimal copy counts for zero-bad, one-bad strict,
one-bad non-strict, and two-bad strict contracts.

## Calibration

- Pre excitement: `8/10`.
- Pre confidence: `10/10`.
- Pre expected information gain: `8/10`.
- Post excitement: `8/10`.
- Post confidence: `10/10`.
- Post information gain: `8/10`.
- Frozen optionality: the next genuine physical gap is the fault model and the
  `1/4` target, not copy-count arithmetic.

## Report to `marici.Nima`

- Admitted state domain: detector fault contracts.
- Faithful quotient coordinate: bad/copy fraction under strict or non-strict
  interval separation.
- Source-authorized probe family: still conditional on detector fault model.
- Contextual partition: one-bad strict gives five; one-bad non-strict gives
  four; two-bad strict gives nine.
- Classification: fault-contract audit.
- Smallest exact falsifier: non-strict touching would allow four copies.
- Remaining physical-instrument gate: derive one-bad fault model and `1/4`
  target.
