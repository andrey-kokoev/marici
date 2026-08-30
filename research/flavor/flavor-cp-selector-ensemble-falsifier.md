# CP-selector ensemble falsifier (WP352)

## Complete fitted test

WP351 predicts

\[
J^2=\frac1{543}
\]

on every nondegenerate radial stratum of the selected projector rays. WP352
tests (J^2), so both CP-conjugate signs are admitted and no orientation port
can affect the comparison.

All 1,210 canonical fitted sheets are loaded from the frozen WP20 ensemble.
Zero sheets match at the declared log-squared tolerance. The predicted
magnitude exceeds every fitted magnitude by more than three orders, and the
closest squared-log gap is greater than 10.

## Disposition

This is a clean falsification, not a failure of selector typing. WP351 is a
genuine conditional numerical selector of normalized CP geometry, and the
complete fitted ensemble rejects its prediction.

Radial normalization, CP sign choice, detector calibration, and texture-chart
rephasing cannot repair the result because they were removed before comparison.
Changing the projector geometry or sector characters defines a new source
model and must be justified independently of the desired (J).

Run `uv run python
research/flavor/checkers/wp352_cp_selector_ensemble_falsifier.py` to regenerate
the complete-ensemble audit.
