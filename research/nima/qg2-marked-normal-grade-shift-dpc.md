# Marked-normal grade shift: first conjecture cycle

## Problem

The `q_g2` wall class occurs at soft grade `-2`, while `q_g1` and `q_g3` form a sewn class at grade `-1`. Prior marked-axis results suggest that a source-labeled normal section may define a grade-changing correspondence forbidden without that mark.

## Bold conjecture

The canonical soft normal

\[
x=\frac{q_{g2}-q_{g31}}{\kappa-1},\qquad \kappa\ne1,
\]

shifts the `q_g2` class to grade `-1` and, by itself, closes the `q_g1`–`q_g2` node.

## Named rivals

1. the unnormalized collision section `q_g2-q_g31=x(kappa-1)` is the correct marked section;
2. a full excess-Gysin map needs a nontrivial node Jacobian in addition to the normal section;
3. no geometric grade shift is valid, and physical normalization comes only from lower-point source insertions.

## Risky consequences

The shifted `q_g2` node residue must be the negative of the existing `q_g1` residue. The same test must fail at `kappa=1`, where the marked section ceases to separate the collision.

## Strongest falsification attempt and residual

Execution `structured_command_execution:e_7396_1788302266889745000_2` compares exact residues. The `q_g1` node residue is

\[
\frac{3-\kappa}{64p^4(\kappa-1)^2},
\]

whereas multiplication by `x` gives the shifted `q_g2` residue

\[
-\frac{1}{16p^3(\kappa-1)^2}.
\]

Their closure residual is

\[
-\frac{\kappa+4p-3}{64p^4(\kappa-1)^2},
\]

which is generically nonzero. Multiplication by the full collision section also leaves a generically nonzero residual. The bold conjecture is falsified.

Exact closure would require multiplying the `x`-shifted `q_g2` residue by

\[
-\frac{\kappa-3}{4p}.
\]

## Disposition and residual conjecture

The marked normal supplies the correct grade shift but not the sewn-node map. The surviving conjecture is that a source-derived excess-Gysin correspondence combines multiplication by `x` with the exact node Jacobian `-(kappa-3)/(4p)`. This factor is presently an inferred acceptance target, not an authorized map. The next falsification test is to derive the Jacobian independently from the two-wall normal bundle or disprove that derivation.

## Evidence

- `research/nima/checkers/check_qg2_marked_normal_grade_shift.py`
- `research/strominger/a-marked-axis-constructs-the-grade-changing-endpoint-correspondence.md`
- `research/nima/qG12-unsplit-leading-wall-log-sum.md`
