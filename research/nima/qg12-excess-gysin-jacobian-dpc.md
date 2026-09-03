# Excess-Gysin Jacobian: second conjecture cycle

## Problem

The marked normal `x` shifts `q_g2` from grade `-2` to grade `-1` but does not close the `q_g1`–`q_g2` node. Closure would require the additional factor `(3-kappa)/(4p)`.

## Bold conjecture

The required factor is the determinant of the local two-wall normal map or its weighted exceptional strict transform; hence a canonical excess-Gysin correspondence supplies it.

## Named rivals

1. only the labeled collision coefficient `kappa-1` enters the excess map;
2. the local normal determinant is a unit and cannot repair the residue mismatch;
3. the grade `-2` class is a separate supported summand, and any comparison requires nonlocal denominator or lower-point source data.

## Risky consequences

An independent differentiation of the wall equations must produce `(3-kappa)/(4p)` without using residue closure. The result must be stable under replacing physical wall coordinates by the weighted exceptional coordinates.

## Strongest falsification attempt and residual

Use

\[
q_{g1}=b-y-z,
\qquad q_{g2}=a-x-z,
\qquad q_{g31}=a-y.
\]

Execution `structured_command_execution:e_7396_1788302399269308100_4` gives

\[
\det\frac{\partial(q_{g1},q_{g2})}{\partial(a,b)}=-1.
\]

On the exceptional fiber, with strict transforms `q_g1/x=xi+1` and `q_g2=a-p`, it again gives

\[
\det\frac{\partial(q_{g1}/x,q_{g2})}{\partial(a,\xi)}=-1.
\]

The labeled collision coefficient is independently `kappa-1`. None equals `(3-kappa)/(4p)` generically. The bold conjecture is falsified: the fitted factor does not come from first-order wall-normal geometry.

## Disposition and residual conjecture

The `q_g2` grade `-2` logarithmic class is a separate excess-support summand rather than an incompletely normalized grade `-1` node class. Any lawful map to grade `-1` must use data absent from the local normal bundle, such as the remaining denominator restrictions or a lower-point source normalization. The next discriminating test is to compute whether the full unsplit denominator numerator defines a triangular extension between grades, rather than a grade-identifying isomorphism.

## Evidence

- `research/nima/checkers/check_qg12_node_normal_jacobian.py`
- `research/nima/qg2-marked-normal-grade-shift-dpc.md`
