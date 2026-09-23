# A nine-point positive target requires at least eight source labels

The nine-point determinantal carrier has an important geometric test beyond its algebraic lifting formula. Zero-padding a seven-point separated-pair source cell into nine columns (columns 8 and 9 zero) DOES give a legitimate eight-dimensional positive source-cell image. The two zero columns force four of the six hidden kernel coefficients to vanish, leaving the original two-dimensional affine seven-point fibre. Its target Jacobian at the checked positive moment-curve point is `102400/194481`, and its two remaining pair constraints pin the lift with determinant `-882`. Thus curved ambient fibres can contain full-dimensional **polyhedral cell strata**.

But seven-label strata CANNOT suffice to cover the nine-point image. A deterministic exact search found a strictly positive nine-column source with signed row-one weights (first seven negative, last two positive) recorded in `nine-point-support-stress.json`. For its target `Y=CZ`, every one of the `binomial(9,7)=36` possible retained seven-label supports has an EMPTY nonnegative source-lift fibre.

This negative assertion is not based on sampling candidate vertices or assuming boundedness. For each retained support, an independently reconstructed rank-one-kernel fibre has 21 affine ordered-minor inequalities. An exact Farkas certificate combines at most THREE of those required nonnegative minors with strictly positive rational coefficients; their `a,b` coefficients cancel and their weighted constant is strictly NEGATIVE. Such an identity is impossible if all the chosen minors are nonnegative. All 36 source-independent impossibility packets are replayed by a separate verifier, which also checks the original nine-column source has all 36 ordered minors STRICTLY positive. Four controls reject a negative weight, false constant, omitted support and changed source.

Consequently the lower bound on this admitted `Y` is eight. A subsequent exact construction now supplies an eight-label lift with column 3 zero, so its minimum support is EXACTLY eight; see `the-nine-point-positive-target-has-exact-minimum-eight-label-support.md`. The original nine-label lift is still separately admitted. Any proposed universal `n=9` positive-cell compiler whose cells all have at most seven nonzero source columns is falsified on this fixed target. This does not falsify the sourced nine-point generalized-R histories or determine which eight-/nine-support cells they require.

The mechanism clarifies the path to `n>8`: zero-padding can reuse seven-point polyhedral cells locally, but it cannot replace genuine higher-support semialgebraic or other positive cells globally. The hidden determinant terms are not merely a coordinate nuisance; increasing multiplicity forces new source-support obligations.

Reproduce:

    uv run --with sympy python research/nima/checkers/check_nine_point_determinantal_fibre.py
    uv run --with sympy python research/nima/checkers/check_nine_point_seven_support_cell.py
    uv run --with sympy python research/nima/checkers/check_nine_point_support_stress.py
    uv run --with sympy python research/nima/checkers/verify_nine_point_no_seven_support.py
    uv run --with sympy python research/nima/checkers/check_nine_point_no_seven_support_packet.py

Artifacts: `research/nima/results/nine-point-seven-support-cell.json`, `nine-point-support-stress.json`, `nine-point-no-seven-support-verification.json`, and `nine-point-no-seven-support-packet-verification.json`.
