# The nine-point four-pair carrier is a relabelled sourced four-mass ψ cell

A primary-source comparison identifies the EIGHT-POINT positroid cell underlying the nine-point construction. In arXiv:1212.5605, `positive_grassmannian_update.tex`, Table `g2n_yangian_invariants`, the starred eight-point four-mass-box/ψ row has parallel classes

    (1,2), (3,4), (5,6), (7,8)

and bounded affine permutation

    (2,5,4,7,6,9,8,11).

An independent cyclic-interval-rank calculation from our four parallel classes reproduces this exact permutation. Deleting physical nine-point column 3, the ordered retained labels `(1,2,4,5,6,7,8,9)` have the SAME sourced eight-point cell after relabelling. Their nine-point bounded permutation, with column 3 a loop, is

    (2,6,3,5,8,7,10,9,13).

This replaces the description "unsourced candidate" at the EIGHT-POINT POSITROID-CELL LEVEL. It does NOT show that this embedded cell occurs in the source's NINE-POINT generalized-R history expansion or inherits a particular coefficient there.

## Both kinematic solutions match the source equations

The same primary source's `four_mass_explicit_solution` defines

    A = z7 + α z8,       B = z3 + β z4,

with two coupled four-bracket equations for `α,β`. At the certified rational nine-point target, pass to the four-dimensional quotient by its observed two-plane `Y`; its four-brackets are the exact six-by-six determinants `<Y1,Y2,Zi,Zj,Zk,Zl>`. Then the source's eight labels are relabelled by `(1,2,4,5,6,7,8,9)`.

In the positive paired-cell chart, `α=w8/w7` and `β=w4`. The checker derives `α(q),β(q)` from the independent nine-point source-fibre equations. Substitution into BOTH primary-source four-bracket equations gives remainders identically ZERO modulo the previously certified quadratic graph polynomial `P(q)`. Its two roots therefore reproduce BOTH source four-mass auxiliary solutions, not only the positive real lift. The source's quadratic in `α` and the fibre quadratic in `q` have discriminants whose exact ratio is a rational square; two deliberately perturbed source equations fail.

This explains the preceding rationality finding rather than contradicting it: the source explicitly warns that starred four-mass ψ has TWO kinematic solutions and discusses a SUM over those solutions. Its explicit ψ prefactor has also been identified EXACTLY with a normalized inverse Jacobian of the same two auxiliary equations; see `the-four-mass-psi-prefactor-is-the-normalized-auxiliary-jacobian.md`. The one-positive-sheet algebraic value is not the complete traced four-mass function. Source-backed branch identification still falls short of equality of complete superfunctions or canonical forms: the ψ prefactor, Grassmann component, overall orientation, pole residues, and occurrence in the NINE-POINT generalized-R history list remain untested.

Reproduce:

    uv run --with sympy python research/nima/checkers/check_nine_point_four_mass_source_match.py
    uv run --with sympy python research/nima/checkers/check_nine_point_four_mass_auxiliary_match.py

Artifacts: `research/nima/results/nine-point-four-mass-source-match.json` and `nine-point-four-mass-auxiliary-match.json`.
