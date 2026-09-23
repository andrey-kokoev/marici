# One positive sheet of the nine-point four-pair map is not a rational target form

An important correction to the nine-point form program is now exact: the positive-cell LOCAL branch density is **not** the algebraic pushforward of the cell's rational source form. For a generically degree-two source-to-target map, the latter is the **TRACE over both complex preimages**, including a second branch that may fail real positivity. Dropping that branch can change the target form and create a square-root dependence.

The four paired-minor equations on the eight-support source fibre leave a quadratic graph equation `P_Y(q)=0`. At the earlier FIXED RATIONAL minimum-eight-support target, its rational discriminant is positive but NOT a square (checked by integer square roots of its numerator and denominator). The elimination denominators are nonzero there. Consequently the generic quadratic cover does not split over the rational function field of the target: the two branches are Galois conjugates. Rationality of a single-sheet target differential form would require its two conjugate coefficients to AGREE identically.

They do not. At TWO regular rational target points, exact continuation of the intrinsic source form to the second (nonpositive) graph-realizable sheet gives a coefficient different from the positive sheet's coefficient. For the all-unit weight sample `(t,u)=(3,2)`:

    positive-sheet coefficient  = -2560000/21039669,
    second-sheet coefficient    = -41642572755547958240000000
                                   /1480489021341160462173201970401.

Both chart Jacobians and the roots are nonzero and distinct. Another independently chosen positive sample gives the same inequality. Their exact sums are frozen in `nine-point-paired-two-sheet-trace.json`; the trace coefficients are rational, as quadratic field theory requires. The rationality-obstruction checker certifies the nonsquare discriminant and both inequalities, and a separate replay refuses four mutations.

**Deduction.** The coefficient on ONE generic paired-cell sheet is genuinely algebraic, not a rational function of target coordinates. It therefore cannot, by itself, equal any single rational generalized-R history form as a TARGET-FORM IDENTITY. A SUBSEQUENT PRIMARY-SOURCE AUDIT identifies the eight-point four-pair source cell with the STARRED four-mass ψ class and matches BOTH of the source's auxiliary kinematic solutions to this quadratic fibre; see `the-nine-point-four-pair-carrier-is-a-relabelled-sourced-four-mass-psi-cell.md`. This is not yet a sourced NINE-POINT generalized-R history or a complete ψ/canonical-form equality: normalization and pole data remain unmatched. The full two-sheet trace is rational and remains a viable candidate for later comparison; sums with other cells may also be rational. The second sheet need not be positive on the real target, but it still enters the algebraic trace defining the rational pushforward.

This makes the form gate more precise: compute and compare the **global traced** pushforward, not the positive local branch density from earlier samples, before attempting a sourced generalized-R identification. The earlier certified local density remains correct AS A LOCAL BRANCH VALUE, but it lacks stand-alone rational-history authority.

Reproduce:

    uv run --with sympy python research/nima/checkers/check_nine_point_paired_trace_samples.py
    uv run --with sympy python research/nima/checkers/check_nine_point_branch_rationality_obstruction.py
    uv run --with sympy python research/nima/checkers/verify_nine_point_branch_rationality_obstruction.py

Artifacts: `research/nima/results/nine-point-paired-two-sheet-trace.json`, `nine-point-single-sheet-rationality-obstruction.json`, and `nine-point-single-sheet-rationality-obstruction-verification.json`.
