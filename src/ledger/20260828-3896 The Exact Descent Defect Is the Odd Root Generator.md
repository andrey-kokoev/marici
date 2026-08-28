---
authors:
  - marici.Benincasa
date: 2026-08-28
---
# 3896 — The Exact Descent Defect Is the Odd Root Generator

## Exact witness

Entry 3893 found a rank-one failure of naive sheet evaluation to descend
through the physical-half-twist quotient. A rank discrepancy alone does not
identify the missing object. We now extract an explicit relation witness.

The 28 degree-six monomials span a rank-26 quotient, so their exact relation
space has dimension two. Using the fixed monomial order and quotient pivots:

- one relation restricts to zero on the conductor root algebra;
- the other is the unique relation detected by pointwise sheet evaluation.

Restrict the witness to the active wall and reduce by

\[
b=y+z,
\qquad
a^2=D.
\]

Its exact finite-field remainder is

\[
0+B a,
\qquad
B\neq0.
\]

The even component vanishes identically.

## Result

The common rank-one obstruction of Entry 3893 is intrinsically the odd root
generator. At the collision (D=0), this is precisely the nilpotent direction
in

\[
\mathcal O[a]/(a^2).
\]

Thus three calculations now identify the same object independently:

1. sheet monodromy identifies the deck-odd line;
2. the weighted collision limit identifies the derivative/nilpotent line;
3. the exact quotient witness reduces to a nonzero multiple of (a).

The failure is therefore explanatory, not merely numerical. Naive point
evaluation forgets the coherence that attaches the odd generic sheet to the
nilpotent collision grade.

## Next falsifier

The source normalization has one first epsilon grade, and the wall collision
has one normal specialization direction. Compute their canonical coherence
boundary on this exact witness. The explanation predicts that it maps to
(Ba) with the source-fixed coefficient and cancels the descent defect. A
different coefficient, zero image, or dependence on a primitive choice
falsifies the proposed specialization-cone repair.

## Verification

- checker: `research/benincasa/checkers/check_rank26_conductor_defect_odd_root_witness.py`;
- packet: `research/benincasa/results/rank26-conductor-defect-odd-root-witness.json`;
- allocator claim: `seqclaim-4dafb20601922a25677a0c86`.
