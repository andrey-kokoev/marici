# Adaptive relation depth lower bound

Owner: `marici.Figueiredo`.

## Question

WP168 says that a source-derived exponent cap `E` makes relation testing
faithful at depth `E`. This packet asks whether an adaptive protocol can do
better by asking fewer, cleverer, or branch-dependent relation questions.

## Frozen domain

- State domain: `Z^2` versus `(Z/EZ)^2` with the same two labelled ports.
- Faithful coordinate: identity answers for queried words in
  `+e1,-e1,+e2,-e2`.
- Instrument resource: maximum queried word length.
- Audited cap: `E=8`.

## Exact claim

No adaptive relation/fusion protocol whose longest queried word has length
less than `E` can distinguish `Z^2` from `(Z/EZ)^2`.

The reason is pointwise, not statistical. Every possible under-depth query has
coordinate sums `(a,b)` with `|a|,|b| < E`. Such a word is an identity in
`(Z/EZ)^2` exactly when it is already the zero-sum identity in `Z^2`.
Therefore every branch transcript available to an adaptive protocol is shared
by both models.

At depth `E`, the word `+e1^E` separates them.

## Disposition

WP168's depth requirement is a real resource lower bound. Exhaustiveness is
not the essential cost; maximum word depth is. Asking all `21845` words through
depth seven still cannot certify infinite closure against `(Z/8Z)^2`, while a
single depth-eight query can separate the hostile pair once the source has
already supplied the exponent cap.

Thus:

`source exponent cap E + depth-E relation instrument -> conditional selector`.

But:

`source exponent cap E + under-depth adaptive relation instrument -> rigidifier`.

The remaining physical gate is not clever querying. It is deriving the cap and
building an instrument that can execute the required word depth.

## Exact checker

- Checker: `checkers/wp169_adaptive_relation_depth_lower_bound.py`
- Result: `results/wp169_adaptive_relation_depth_lower_bound.json`

The checker confirms agreement for the complete under-depth language, verifies
three representative adaptive transcripts, and confirms that the first
distinguishing word appears exactly at depth eight.

## Calibration

- Pre excitement: `9/10`.
- Pre confidence: `10/10`.
- Pre expected information gain: `7/10`.
- Post excitement: `8/10`.
- Post confidence: `10/10`.
- Post information gain: `8/10`.
- Frozen optionality: do not spend effort on adaptive relation scheduling
  until the source cap and executable word-depth budget are typed.

## Report to `marici.Nima`

- Admitted state domain: two labelled closure stories `Z^2` and `(Z/EZ)^2`.
- Faithful quotient coordinate: identity-relation transcripts.
- Source-authorized probe family: adaptive relation/fusion queries bounded by
  maximum word length.
- Contextual partition: all under-depth transcripts place `Z^2` and
  `(Z/EZ)^2` in the same class.
- Classification: under-depth protocols are rigidifiers only; depth-`E`
  protocols become conditional selectors only with a source exponent cap.
- Smallest exact falsifier: at `E=8`, every word of length at most seven
  agrees; `+e1^8` first separates.
- Remaining physical-instrument gate: execute depth `E` and derive `E` from
  source data.
