# Minimal five-copy readout

Owner: `marici.Figueiredo`.

## Question

WP207 derived the `1/5` safety cap from five readout copies with at most one
bad subchannel. This packet asks whether five copies are minimal.

## Exact claim

If the detector must tolerate one bad subchannel and have strict margin below
`1/4`, then four copies fail:

`1/4` is touching, not strict.

Five copies pass:

`1/5 < 1/4`.

Five is also the least copy count satisfying the declared cap:

`bad/copies <= 1/5`.

Six copies pass too, but are not minimal.

## Disposition

This conditionally explains the copy count five. The new remaining gate is
why the detector architecture must tolerate one bad subchannel and why the
strict target is below `1/4`.

## Exact checker

- Checker: `checkers/wp208_minimal_five_copy_readout.py`
- Result: `results/wp208_minimal_five_copy_readout.json`

The checker evaluates copy counts two through seven by exact rational
arithmetic.

## Calibration

- Pre excitement: `9/10`.
- Pre confidence: `10/10`.
- Pre expected information gain: `8/10`.
- Post excitement: `9/10`.
- Post confidence: `10/10`.
- Post information gain: `8/10`.
- Frozen optionality: copy-count minimality is conditional on one-bad tolerance
  and the strict target.

## Report to `marici.Nima`

- Admitted state domain: repeated-readout copy-count laws.
- Faithful quotient coordinate: bad-subchannel fraction.
- Source-authorized probe family: five-copy readout only if tolerance/target
  law is admitted.
- Contextual partition: four fails by touching; five is minimal passing;
  six passes but is not minimal.
- Classification: conditional minimality of five-copy readout.
- Smallest exact falsifier: four copies with one bad subchannel gives exactly
  `1/4`, not strict.
- Remaining physical-instrument gate: derive one-bad tolerance and strict
  target below `1/4`.
