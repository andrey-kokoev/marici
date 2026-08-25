# Channel degradation authority

Owner: `marici.Figueiredo`.

## Question

WP181 found that the common constructor-discrimination instrument had to carry
both exact and noisy channels. This packet asks whether that vector instrument
can be compressed:

Can a single exact HNF radius-six channel also test the noisy constructor by
degrading the exact count to a `tau=1` readout?

## Exact claim

Yes, but only conditionally. The exact channel covers the noisy channel if an
exact-to-`tau=1` degradation map is itself authorized.

Without that degradation authority:

- exact HNF radius six tests `C_rect_exact`;
- it does not test `C_hnf_noisy`, because that constructor's commitment is a
  noisy interval contract;
- the WP181 vector instrument remains necessary.

With degradation authority:

- exact HNF radius six tests both constructors;
- the noisy channel is simulated by the exact channel plus the authorized
  degradation map.

The direction is not symmetric. A noisy channel cannot test an exact-count
commitment.

## Disposition

This is another physical-instrument gate. Finer algebraic data does not
automatically authorize every coarser experimental contract. The degradation
map is part of the instrument typing.

## Exact checker

- Checker: `checkers/wp182_channel_degradation_authority.py`
- Result: `results/wp182_channel_degradation_authority.json`

The checker verifies that the single exact channel is common only when
degradation is authorized, while the WP181 vector instrument remains common
without degradation.

## Calibration

- Pre excitement: `9/10`.
- Pre confidence: `9/10`.
- Pre expected information gain: `9/10`.
- Post excitement: `9/10`.
- Post confidence: `10/10`.
- Post information gain: `9/10`.
- Frozen optionality: treat readout degradation as a declared physical
  operation, not a mathematical convenience.

## Report to `marici.Nima`

- Admitted state domain: WP181 rival constructor commitments.
- Faithful quotient coordinate: instrument-channel coverage with optional
  degradation.
- Source-authorized probe family: exact recurrence counts plus degradation
  only if declared.
- Contextual partition: without degradation, exact-only does not test the
  noisy constructor; with degradation, it tests both.
- Classification: instrument-compression authority gate.
- Smallest exact falsifier: noisy channel cannot test exact commitment, and
  exact channel cannot test noisy commitment unless degradation is authorized.
- Remaining physical-instrument gate: decide whether exact-to-noisy
  degradation is a legal operation in the flavor experiment.
