# Compressed instrument authority

Owner: `marici.Figueiredo`.

## Question

WP178 enumerated the four authority fields for recurrence-growth selection.
WP182 added a new issue: a single exact channel can replace the WP181 vector
instrument only if exact-to-noisy degradation is authorized.

This packet folds that into the authority table.

## Fields

Base selector fields:

- `order_cap_K`;
- `quotient_domain`;
- `count_error_tau`;
- `executable_radius`.

Compression field:

- `degradation_map`.

## Exact claim

There are now two distinct valid instrument regimes:

1. **Vector selector:** all four base fields are authorized, but the
   degradation map is not. The exact and noisy channels must both be present.
2. **Single-channel compressed selector:** all four base fields plus the
   degradation map are authorized. A single exact channel can then simulate the
   noisy contract.

The degradation map does not replace any base field. It only compresses the
instrument after the selector gate is already authorized.

## Exact checker

- Checker: `checkers/wp183_compressed_instrument_authority.py`
- Result: `results/wp183_compressed_instrument_authority.json`

The checker enumerates all `32` authorization patterns and verifies that only
one pattern authorizes single-channel compression.

## Calibration

- Pre excitement: `8/10`.
- Pre confidence: `10/10`.
- Pre expected information gain: `8/10`.
- Post excitement: `8/10`.
- Post confidence: `10/10`.
- Post information gain: `8/10`.
- Frozen optionality: distinguish selector authority from instrument
  compression authority.

## Report to `marici.Nima`

- Admitted state domain: recurrence-growth authority patterns with optional
  degradation.
- Faithful quotient coordinate: five-field authorization tuple.
- Source-authorized probe family: vector or compressed recurrence instruments
  depending on degradation authority.
- Contextual partition: base gate without degradation requires vector channel;
  base gate with degradation permits single exact channel.
- Classification: compressed-instrument authority audit.
- Smallest exact falsifier: degradation without any missing base field still
  does not produce a selector.
- Remaining physical-instrument gate: decide whether exact-to-noisy degradation
  is a legal operation in the experiment.
