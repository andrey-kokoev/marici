# Broad concavity survives in the tail and reaches a boundary conditioning wall

The reciprocal-slope chord falsifier was widened to 15 endpoints from `10^-6`
through `10^8`, giving 105 arithmetic-midpoint tests in each of two independent
height/depth runs.

The result splits cleanly by regime:

- for chords whose left endpoint is at least `1`, both runs are positive; the
  smallest gaps are about `3.41257e-4` and agree to roughly `8e-15`;
- the only negative raw gaps occur near the `x=0` boundary;
- the most negative boundary gap is about `-5.52e-8`, while the maximum
  baseline/control discrepancy is about `7.71e-8`;
- no negative survives subtraction of that global discrepancy scale.

Thus no robust counterexample appears over fourteen decades. The
archimedean tail is exceptionally stable, while the small-`x` boundary cannot
be decided by the present double-precision boundary-slope evaluator.

## Next gate

The hostile region is now localized: certify reciprocal-slope concavity near
`x=0`. This should be attacked by a dedicated Taylor/interval expansion in the
central `s` coordinate, where `t=(s-1/2)^2`, rather than by shrinking complex
steps. A rigorous negative chord there would falsify the Pick program; a
positive interval neighborhood would close the only unstable regime found by
this broad scan.

A subsequent 70--80 digit central-coordinate evaluation resolves the raw
negative gaps as binary64 cancellation: all tested boundary chords through
`10^-8` are positive with cross-run discrepancies eight orders below the
smallest margin. See `reduced-source-central-decimal-concavity-resolution.md`.

This remains finite numerical reconnaissance and does not prove global
concavity, Loewner positivity, or RH.

## Durable verification

- Checker: `checkers/reduced_source_reciprocal_slope_broad_scan.py`
- Result: `results/reduced-source-reciprocal-slope-broad-scan.json`
