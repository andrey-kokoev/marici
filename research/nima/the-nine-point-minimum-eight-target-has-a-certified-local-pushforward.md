# Certified local four-pair pushforward at the minimum-eight-support target

The exact positive target previously shown to require eight source labels is now tested at the DIFFERENTIAL-FORM level on its four-pair eight-dimensional cell. This closes a gap left by the two rational sample computations: the distinguished target itself is algebraic in the paired-cell source chart.

The source fibre's four paired-minor equations express `(a,b,c,d)` as rational affine functions of a determinant coordinate `q`. The exact graph equation defines a rational QUADRATIC polynomial `P(q)` (frozen in `nine-point-paired-cell-exact.json`). The checker bisects the root interval by 130 exact rational sign steps, reconstructs the source in the positive paired-cell chart, computes the eight-by-eight Jacobian of

    B = (CZ)[:,0:2]^-1 (CZ)[:,2:6]

and divides the previously normalized four-pair source-form coefficient by that Jacobian. All calculations from `q` to the final form are made with OUTWARD-ROUNDED rational intervals on a `10^-80` grid; every division checks that its denominator interval avoids zero. The final exact rational intervals, recorded in `nine-point-algebraic-target-local-pushforward.json`, enclose approximately

    det(dB/dsource) ~ 1.4185061091925,
    oriented source density ~ -7.119653340793478e13,
    local target-form density ~ -5.019120675374054e13.

The density is large in this coordinate chart; it is not itself a geometric residue or a physical amplitude comparison. The exact algebraic local coefficient is unambiguously specified by `P(q)`, its isolated positive-cell root, the source chart and the determinant expression; the displayed decimal values are only aids to reading the rational enclosures. An independent high-precision Plücker-derivative stress checker reproduces the three enclosures and refuses three altered bounds. The rational-interval checker, not that numerical stress test, is the rigorous certification.

The quadratic has exactly one OTHER graph-realizable root. The packet isolates it near `q=-281.08041026` and proves that ordered retained minor `(1,5)` is STRICTLY NEGATIVE throughout its rational root interval. Hence only ONE of the two graph-realizable four-pair lifts at this fixed target belongs to the positive paired cell. This rules out a missing second positive branch at THIS target, not across the entire image.

IMPORTANT SUBSEQUENT OBSTRUCTION: a nonsquare quadratic discriminant and unequal conjugate sheet densities prove that the ONE-SHEET coefficient is generically nonrational in target coordinates; see `a-nine-point-four-pair-single-sheet-form-is-not-rational.md`. Thus it CANNOT by itself equal a rational generalized-R history form globally. The algebraic pushforward requires the two-sheet trace, including the nonpositive real branch. Still open: source a nine-point history and compare its same-external-data canonical form (orientation, poles and normalization) to that TRACED form. Neither local branch data nor this obstruction prove global coverage or an analytic cutoff-completion rate.

Reproduce:

    uv run --with sympy python research/nima/checkers/check_nine_point_algebraic_target_pushforward.py
    uv run --with sympy --with mpmath python research/nima/checkers/verify_nine_point_algebraic_target_pushforward.py

Artifacts: `research/nima/results/nine-point-algebraic-target-local-pushforward.json` and `nine-point-algebraic-target-local-pushforward-verification.json`.
