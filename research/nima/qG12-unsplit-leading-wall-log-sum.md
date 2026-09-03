# Unsplit leading sewn-wall logarithmic sum

## Question

Do the oriented leading wall forms cancel before gluing, and which residues satisfy the sewn-node matching condition?

## Oriented leading forms

With the positive exceptional square-root branch, the three source-oriented coefficients are

\[
\omega_{g1}^{(-1)}=
-\frac{a+p}{2p(a-p)^2(a+3p)(a^2+(4\kappa-5)p^2)}\,da,
\]

\[
\omega_{g2}^{(-2)}=
-\frac{d\xi}{16p^3(\kappa-1)(\kappa+\xi)(\xi+1)},
\]

\[
\omega_{g3}^{(-1)}=
-\frac{d\xi}{64p^4(\kappa-\xi)(\xi+1)}.
\]

Their grades are `(-1,-2,-1)`. Therefore the unsplit occurrence object is a graded direct sum; `q_g2` cannot cancel either grade `-1` occurrence before an explicit grade-changing normalization.

## Exact sewn-node match

Execution `structured_command_execution:e_30844_1788300082167812200_8` finds

\[
\operatorname*{Res}_{a=-3p}\omega_{g1}^{(-1)}
=\frac{1}{64p^4(\kappa+1)},
\]

\[
\operatorname*{Res}_{\xi=-1}\omega_{g3}^{(-1)}
=-\frac{1}{64p^4(\kappa+1)}.
\]

These are the two presentations of the `q_g1`–`q_g3` intersection. Their exact opposite signs establish the local sewn residue condition at that node without discarding either occurrence. Cancellation happens only after the gluing boundary map identifies the node; it is not cancellation of source numerators.

## Remaining residues

Each component separately has total residue zero. The `q_g2` residues remain the nonzero endpoint-to-conductor pair

\[
-\frac{1}{16p^3(\kappa-1)^2},
\qquad
\frac{1}{16p^3(\kappa-1)^2}.
\]

At the `q_g1`–`q_g2` collision, the raw `q_g1` residue is

\[
-\frac{\kappa-3}{64p^4(\kappa-1)^2},
\]

which is neither same-grade nor same scaling as the `q_g2` endpoint residue. No cancellation is typed there before epsilon normalization and a grade-changing comparison map.

The other `q_g1` poles lie on the two reduced exceptional square-root divisors and complete its componentwise residue theorem.

## Strongest falsification attempt

Summing the three source formulas as if they were functions on one curve would predict unrestricted cross-wall cancellation. This operation is undefined: the forms live on distinct wall components and one occurs at a different soft grade. The one valid same-grade comparison, at the `q_g1`–`q_g3` node, passes exactly with opposite oriented residues.

## Disposition

The unsplit occurrence sum retains all three classes. The grade `-1` `q_g1` and `q_g3` forms satisfy exact sewn-node compatibility; the grade `-2` `q_g2` logarithmic class remains separate and nonexact. A source-derived normalization is required before comparing it to grade `-1` or to the positive-cut generator.

## Evidence

- `research/nima/checkers/check_unsplit_wall_leading_residues.py`
- `research/nima/checkers/check_qg2_extra_soft_log_class.py`
- `research/nima/qg2-extra-soft-relative-log-class.md`
