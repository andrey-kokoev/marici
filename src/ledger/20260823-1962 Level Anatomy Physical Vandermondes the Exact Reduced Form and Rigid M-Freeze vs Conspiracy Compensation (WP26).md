---
author: marici.Figueiredo
---
# 1962 - Level Anatomy: Physical Vandermondes, the Exact Reduced Form, and Rigid M-Freeze vs Conspiracy Compensation

- Date: 2026-08-23
- Author: marici.Figueiredo
- Status: certified pointwise at all 1210 stored minima
- Supersedes: nothing. Continues 1947 (WP21 factorization), 1950 (WP22 W identification), 1959 (WP25a center selection), 1960 (WP25b trench landscapes)

## 1. The reduced form, certified pointwise

WP21e's reduced form is UNIVERSALLY

  L = a1/(Du Dd) = M * W / (gap * D_other),

with gap = sqrt(disc_b) for block21 (the chi_b(s) of 1947 having
cancelled against Du_sec = sqrt(disc_b) * |chi_b(s)|) and gap = the
remaining-gap product for the diagonal class. A first version of this
audit wrongly re-inserted ln chi_b(s) into the L identity; the
residual failures (lnW up to 32.7 on W = +-1 classes) exposed exactly
the cancellation and corrected the formula. Certified with the correct
identity: the residual

  lnW_residual = lnL - lnM + lngap + lnDo

is <= 1.9e-9 on all 712 minima of the W = +-1 classes and equals
ln|W|, bounded in [6.7e-2, 16.2], on all 498 minima of the 284
multi-term Gram-norm-difference textures. n = 1210/1210.

## 2. The Vandermondes are physical

Du and Dd are products of squared-mass differences - weak-basis
invariants. Certified: ln(Du Dd) is constant across all 1210 minima
with global std 4.0e-16 (machine precision). The global spread of
ln D_other (std 8.66) is exactly the u/d sector mix (D_other = Dd for
u-decomposed textures, Du for d-decomposed); within sector-pure
subsets it sits at fit precision (cluster 1: 2.2e-9).

Consequence: the chart content of L is entirely

  K := M * W / gap = a1 / D_sec,

and the five levels are five realized values of K divided by one
physical constant.

## 3. Rigid clusters are M-frozen

- Cluster 1 (42 diagonal, all u-decomposed): gap = 1 and W = +-1
  exactly (lnW std 4.6e-13), so L = M/Dd EXACTLY (residual 4e-14).
  The cluster's entire residual lnL spread (std 9.96e-3) is lnM's
  spread: corr(lnM, lnL) = 1.0.
- Cluster 2 (330 block21, all u-decomposed): every texture has
  W = +-1 (lnW std 3.5e-10; no Gram-norm-difference class occurs),
  gap near-frozen (std 2.8e-4, mean lngap = -0.067), and again the
  residual spread is M's: corr(lnM, lnL) = 0.964, std(lnL) = 1.75e-3
  vs std(lnM) = 1.94e-3.

So the rigid clusters are classes whose fitted magnitude assignments
are near-unique: the monomial M is essentially one value per class,
and L inherits it.

## 4. Conspiracy clusters compensate across factors

Clusters 0, 3, 4 show the opposite regime:

| cluster | std lnM | std lngap | std lnW | std lnL  |
|---------|---------|-----------|---------|----------|
| 0       | 8.82    | 4.45      | 4.95    | 3.3e-2   |
| 3       | 4.15    | 6.83      | 5.08    | 4.0e-3   |
| 4       | 9.12    | 6.66      | 3.55    | 3.1e-5   |

Individual chart factors range over e^{+-4..9} while lnL is frozen to
between 3.1e-5 and 3.3e-2. No single factor carries the freeze:
|corr(factor, lnL)| <= 0.67 for every factor in every conspiracy
cluster (lnW: |corr| <= 0.08). The level is a genuine multi-factor
integral of motion across the viable chart classes.

## 5. What this establishes for the selection question

The level-selection problem now decomposes cleanly:

  L_c = K_c / D_other,   D_other physical (2.2e-9 .. 4e-16),

so "why five phase clusters" is exactly "why do the viable chart
classes realize five values of K = M W/gap". The two rigid clusters
realize K through near-unique magnitude assignments (M-frozen); the
three conspiracy clusters realize K through exact compensation of
wildly varying chart factors. The remaining open object is the
mechanism that admits precisely these five K values - equivalently,
the geometry of the viable (class, magnitude-assignment) pairs over
one physical flavor point.

Typing caution unchanged: M, W, gap are chart data; Du, Dd, and
D_other are physical; K is chart data whose five realized values
organize the ensemble.

## 6. Artifacts

- Checker: research/flavor/checkers/wp26_level_anatomy.py (v2; the
  docstring records the v1 ln-chi error and its diagnostic value).
- Results: research/flavor/results/wp26_level_anatomy.json.
- Inputs: results/wp20_valley_audit.json (1210 stored minima),
  results/wp21e_universal_factorization.json (per-texture forms).
