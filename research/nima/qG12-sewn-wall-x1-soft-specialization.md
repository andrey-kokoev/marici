# `q_G12` sewn-wall `X1`-soft specialization

## Question

What are the exact weighted soft valuations and leading rational factors of the three sewn shared-wall forms before conductor normalization?

## Exact chart

Use

\[
X_1=x,
\qquad X_2=p+\frac{x\kappa}{2},
\qquad X_3=p-\frac{x\kappa}{2},
\qquad b=2p+x(1+\xi).
\]

Execution `structured_command_execution:e_30844_1788299490776561500_4` substitutes this chart into the exact source-unsplit wall formulas.

## Results

For `q_g1`, the rational wall factor has soft valuation zero and leading coefficient

\[
\frac{a+p}{2p(a-p)^2(a+3p)}.
\]

Its differential remains `-da`. This is exactly the `xi+1` residue coefficient of the normalized exceptional bulk source factor.

For `q_g2`, the rational factor has valuation `-2`; pulling back `db=x dxi` leaves valuation `-1`. Its leading coefficient before the differential factor is

\[
-\frac{1}{4p(\kappa-1)(\xi+1)}.
\]

The extra soft pole is sourced by two simultaneous degenerations: `q_g1=x(xi+1)` and `q_g2-q_g31=x(kappa-1)`.

For `q_g3`, the rational factor has valuation `-1`; `db=x dxi` cancels it, leaving valuation zero. Its leading coefficient before the differential factor is

\[
-\frac{1}{16p^2(\xi+1)}.
\]

Thus the three wall forms do not enter the weighted soft chart at one uniform rational grade. The `q_g2` class is distinguished by a residual simple soft pole after differential pullback, while `q_g1` and `q_g3` are finite at this level.

## Typing boundary

These valuations exclude the wall-restricted `sqrt(K)` factor, relative reduction, analytic epsilon normalization, and cycle pairing. The exceptional kernel can add wall-dependent valuations at `xi=±1` or `kappa=±1`; therefore the result does not yet assign final Rees grades.

## Oddball disposition

The nonuniform `q_g2` valuation is a reproducible unresolved observation, not a convention mismatch. It can change which wall class reaches the positive-cut grade. The cheapest discriminating test is to restrict the exceptional kernel separately to each wall and include its square-root valuation.

## Acceptance test

1. restrict the exceptional Cayley–Menger kernel to each pulled wall;
2. factor its normal powers of `x`, `xi+1`, and `kappa-1`;
3. combine square-root, differential, and rational valuations;
4. reduce each leading form in the exceptional relative complex;
5. compare its orientation with the positive-cut generator;
6. perturb away from `kappa=1` and `xi=-1` as deliberate failures of supported localization.

## Disposition

The rational-differential specialization is exact. `q_g1` and `q_g3` are finite, while `q_g2` retains a simple soft pole. Final normalized grades await wall-restricted exceptional square-root and relative-cohomology reduction.

## Evidence

- `research/nima/checkers/check_qG12_sewn_wall_x1_soft.py`
- `research/benincasa/check_x1_soft_physical_strict_transform.py`
- `research/benincasa/physical_g12_shared_wall_residues.py`
