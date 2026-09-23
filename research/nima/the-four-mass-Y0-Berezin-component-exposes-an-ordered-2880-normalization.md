# The four-mass Y0 Berezin component exposes an ordered 2880 normalization

## Exact comparison on the polynomial open set

With `h_{a j}=Σ_{A=1}^4 φ_j^A η_{aA}` and only `η_1^A,η_5^A` nonzero, the exact two-sheet Y0 polynomial from the preceding result reduces, on each sheet, to

    [source_density(C)/J_z(C)] * det(C_1,C_5)^4 * det(H_η)^4,

where `H_η` is the two-by-two matrix of contractions of the two `φ` rows with the two independent η rows. An explicit exterior-algebra calculation with ordered generators `(φ1^1..4,φ2^1..4,η1^1..4,η5^1..4)` gives top coefficient **2880** in `det(H_η)^4`. The independent small-`N` checks yield `(-1)^N (N+1)(N!)²` at `N=1,2,3,4`; this is a nontrivial normalization factor, not silently one.

At TWO independently chosen rational four-dimensional `z` data sets obtained from the positive Y0 witnesses, the Berezin-top coefficient from the source-pushforward `Σ[source_density/J_z] det(C_1,C_5)^4`, and the FULL starred `ψ[A1234][B5678]` component calculated by a separate quadratic-field companion trace, have the exact ratio **+2880** at both points. Both computations include both roots; the ψ result includes its complete prefactor and both five-bracket denominators. Thus dividing the RAW ordered exterior integral by 2880 matches this sourced component at these two tests. This does not, on its own, prove a functional identity or fix the primary source's implicit Berezin measure conventions.

**Orientation warning:** the previous source-coordinate audit found that our declared cyclic residue pulls back to **minus** the published ordered `dlog α1∧...∧dlog α8`. The displayed +2880 ratio pertains to the raw declared cyclic residue and the explicit χ conventions in the independent ψ checker. If that form's orientation is reversed to the authored ordered source chart, the same raw Grassmann ordering yields −2880. A global plus-ψ assertion requires reconciling BOTH the source form orientation and the normalization convention; neither can be hidden by reporting a one-sample numerical agreement.

Still open: a source-consistent global orientation/normalization audit, a pole-residue comparison and an explicit global target rational coefficient away from Y0. Assignment to an authored nine-point generalized-R history remains independent.

Checker: `research/nima/checkers/check_four_mass_Y0_Berezin_component.py`; result: `research/nima/results/four-mass-Y0-Berezin-component.json`.
