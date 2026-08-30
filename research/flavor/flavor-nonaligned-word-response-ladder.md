# Non-aligned word response ladder

## Bounded question

What `physical16` response rank becomes available if the aligned WP645 loop is
supplemented by the smallest existing flavon-word grammars, and does either
grammar itself supply selector authority?

## Exact witness and invariant coordinates

Use distinct exact Yukawa singular values \((1,2,4)\) and \((3,5,7)\), and an
exact CP-violating CKM matrix with rational sines and cosines

\[
(c_{12},s_{12})=(3/5,4/5),
\quad(c_{23},s_{23})=(5/13,12/13),
\quad(c_{13},s_{13})=(8/17,15/17),
\quad e^{i\delta}=i.
\]

The checker differentiates ten algebraically independent weak-basis
invariants: three spectral traces in each sector, three mixed traces, and the
CP-odd commutator cube. Rank in these coordinates is intrinsic quotient rank;
`physical16` remains the faithful sixteen-entry readout embedding.

## Rank ladder

The aligned charged loop spans only \((Y_u,0)\) and \((0,Y_d)\), giving rank
two.

WP450's identity-plus-linear word space

\[
\operatorname{span}_{\mathbb C}\{I,J_1,J_2,J_3\}
\]

in each sector supplies sixteen real perturbation coefficients. Its exact
invariant Jacobian has rank nine at the nondegenerate CP-violating witness.
Thus a single additional word layer can reach a codimension-one tangent
family, but the current charged-loop source does not derive those independent
coefficients.

WP450's degree-two nine-word basis spans every complex \(3\times3\) matrix in
each sector. Its exact invariant Jacobian has the full intrinsic rank ten.
Once those coefficients are admitted freely, the grammar restores universal
local fitting capacity rather than selection.

## Authority boundary

The rank-nine linear grammar is a conditional selector-capacity candidate,
not a selector. Its sixteen real coefficients are not fixed by a source law,
and applying arbitrary perturbations around every admissible base point does
not produce a proper global image. The rank-ten degree-two grammar is a
universal carrier.

The sharp progressive gate is now narrow: derive a source operation that
selects the linear-word coefficients independently of flavor data and prove
that its rank-nine relation is stable across the complete fitted ensemble.
Without that derivation, the non-aligned words are presentation/fitting
capacity only.

## Reproduction

Run:

    uv run --with sympy python research/flavor/checkers/wp646_nonaligned_word_response_ladder.py

The generated result is
`research/flavor/results/wp646_nonaligned_word_response_ladder.json`.
