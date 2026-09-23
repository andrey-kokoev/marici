# The minimum-eight target has a certified two-sheet form trace

## Question

Does the earlier algebraic minimum-eight-support target admit a certified BOTH-sheet four-pair form pushforward rather than only its positive local branch?

## Claim boundary

At this ONE rational nine-point target, an exact quadratic isolates both graph-realizable paired-cell source lifts. The positive lift has source support eight; its conjugate has a strictly negative ordered minor `(1,5)` and is not a positive source. Both nevertheless contribute to the algebraic trace of the rational source form. The checker evaluates the nonpositive lift in the same source chart and target row-major Plücker chart using outward-rational intervals on a `10^-80` grid. It checks every division interval avoids zero and certifies the oriented eight-by-eight Jacobian is nonzero. Adding its coefficient interval to the previously certified positive-sheet coefficient gives a strict exact enclosure of the traced coefficient.

The nonpositive branch coefficient lies between `-1273764955281/10^12` and `-15922061941/12500000000` (approximately `-1.27376495528`), whereas the positive branch coefficient is near `-5.019120675374054 × 10^13`. The difference between the full trace and the positive-only value is nonzero, even though the second sheet is not a positive real source. A separate 95-digit Plücker-derivative stress checker verifies the conjugate coefficient and Jacobian enclosures and refuses two mutated bounds. The exact certification is the outward-rational interval checker, not the numerical stress check.

## Disposition

Resolved for this fixed target only. The unexpanded global rational traced target form, its comparison with the COMPLETE sourced four-mass psi superfunction, pole residues, and occurrence in a sourced nine-point generalized-R history remain open. The psi-prefactor partition `psi_+ + psi_- = 1` does not imply equality of the COMPLETE traced eight-form.

Reproduce using structured-command's admitted `uv run --with sympy python` prefix:

- `research/nima/checkers/check_nine_point_two_sheet_trace_at_minimum_eight_target.py`
- `research/nima/checkers/verify_nine_point_two_sheet_trace_at_minimum_eight_target.py`

Results: `research/nima/results/nine-point-fixed-target-two-sheet-trace.json` and `nine-point-fixed-target-two-sheet-trace-verification.json`.
