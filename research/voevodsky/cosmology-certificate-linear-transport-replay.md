# Certificate replay through the linear generator map

## Result

A staged exact replay localized the prior mismatch:

- 1,224 A12 certificate equations: zero failures;
- 2,448 transported source-row maps: zero failures;
- 2,448 transported target-row maps: zero failures;
- 2,448 transported coefficient words: zero failures.

The defective transport check used p-tangent `T` rows where transported `nx` target rows were required. Repairing that interface eliminates every claimed residual, coefficient correction, and DAG enlargement. The labelled generator map and all stored coefficient words commute from A12 to A14.

The earlier graph dispositions rejecting identity transport, re-solving, and the alleged 780 DAG closures relied on this checker defect and are scientifically superseded by the repaired results; immutable graph history remains provenance, not evidence.

## Claim boundary

This establishes A12-to-A14 algebraic transport. Direct-versus-iterated A16 composition remains unverified. No source differential, geometric support, DNC comparison, or horn consequence follows.

## Verification

- `research/voevodsky/check_cosmology_certificate_linear_transport_replay.py` — exit 0
- `research/voevodsky/results/cosmology_certificate_linear_transport_replay.json`
