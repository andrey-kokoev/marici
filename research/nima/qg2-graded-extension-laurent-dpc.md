# `q_g2` Laurent extension: third conjecture cycle

## Problem

If `q_g2` is a separate grade `-2` summand, its full unsplit form may nevertheless contain a grade `-1` subleading coefficient defining an off-diagonal extension into the sewn `q_g1/q_g3` class.

## Bold conjecture

The source-derived grade `-1` Laurent coefficient of the complete `q_g2` wall form closes the `q_g1`–`q_g2` node without an external normalization map.

## Named rivals

1. the subleading coefficient is nonzero but is only a triangular self-deformation of `q_g2`;
2. an ordered Čech face supplies an additional node term;
3. no cross-grade differential exists and the graded pieces remain a direct sum.

## Risky consequences

After expanding both the rational denominator and wall-restricted square root to first subleading order, the `q_g2` grade `-1` endpoint residue plus the `q_g1` node residue must vanish exactly.

## Strongest falsification attempt and residual

On `q_g2`, the wall-restricted kernel satisfies

\[
K/x^2=16p^4(\kappa+\xi)^2
+8xp^3(\kappa+\xi)(\xi+1)(2\kappa+\xi+1)+O(x^2).
\]

Execution `structured_command_execution:e_7396_1788302502960649000_5` expands the complete wall form, including the square-root correction. Its grade `-1` endpoint residue is

\[
\frac{1}{64p^4(\kappa-1)}.
\]

Adding the `q_g1` node residue gives

\[
\frac{3-\kappa}{64p^4(\kappa-1)^2}
+
\frac{1}{64p^4(\kappa-1)}
=
\frac{1}{32p^4(\kappa-1)^2}.
\]

The residual is nonzero generically. The bold conjecture is falsified.

## Disposition and residual conjecture

The nonzero subleading coefficient proves a triangular Laurent deformation exists, but it is not by itself the sewn extension boundary. The exact remaining residual is simpler than either summand and is independent of the numerator factor `3-kappa`. By analogy with the previously constructed ordered Čech residue cocycle, the surviving conjecture is that the oppositely oriented `q_g1/q_g2` face contributes

\[
-\frac{1}{32p^4(\kappa-1)^2}
\]

and closes the grade `-1` total-complex differential. This coefficient is an acceptance target; the next test must derive it from the ordered face boundary rather than insert it.

## Evidence

- `research/nima/checkers/check_qg2_graded_extension_laurent.py`
- `research/voevodsky/cosmology-relative-residue-cocycle.md`
- `research/nima/qg12-excess-gysin-jacobian-dpc.md`
