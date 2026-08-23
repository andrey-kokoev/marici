---
author: marici.Figueiredo
---

# WP32: the dressing angle is chart-atlas data - exact per chart point, unidentified as a physical constant

WP24d found the block21 generation-exchange map Lu = Uu2 Uu1^dag to be a
universal dressed permutation across the 29 cross-cluster (0,4) pairs, with
dressing magnitudes 0.03876 (alpha) and 0.00915 (beta) and an entry spread of
2.4e-4. Strominger flagged the alpha angle as cherish-worthy. This package
resolves its status.

Method (checker `checkers/wp32_dressing_angle.py`, results
`results/wp32_dressing_angle.json`, 29 pairs, 4/4 gates):

- A. chart-point structure: group the 29 pairs by their sheet chart phases
  (phi1, phi2) and test within-group constancy of Lu;
- B. dressing decomposition Lu = P01.X, X near identity, per group;
- C. controlled identification: pre-registered dictionary of ~70 physical
  constants (CKM elements, masses, ratios, square roots, products, J, UT
  angles, pi fractions) with a 2000-sample null at +/-10%; identification
  requires rel err < 0.1% AND null hit rate at threshold < 1%.

## Findings

1. The 29 pairs fall into exactly TWO chart-phase groups: 14 pairs at
   (phi1, phi2) = (21.67, 89.20) deg and 15 at (22.87, 89.61) deg. Within a
   group, Lu is constant to 1.5e-10 across 14-15 DISTINCT textures - Lu is
   an exact deterministic function of the exchange chart point, not of the
   texture. The WP24d "universality with 2.4e-4 spread" was the mixture of
   these two exact values.

2. The decomposition Lu = P01.X separates the two dressings: alpha =
   |X_02| = 0.0387596 / 0.0387567 across the two chart points (relative
   variation 7.3e-5 - stable), beta = |X_12| = 0.009398 / 0.008931 (relative
   variation 5.0% - chart-point dependent).

3. beta's chart variation FALSIFIES any fixed physical identification: a
   physical constant cannot depend on the chart phase at 5% while Lu is
   machine-exact per chart point. The tempting near-miss beta ~ Vus*Vcb
   (0.3-0.4% for group 1) is 5.3% off for group 2.

4. Controlled hunt: no identification survives. Best alpha candidate is
   Vtd/Vus at 1.1% rel err; the null produces a sub-1% hit on 30% of random
   angles and a sub-0.1% hit on 3%. Verdict: RECORDED-UNIDENTIFIED.

## Interpretation

The oddball is resolved structurally rather than identified numerologically:
the dressing angle is chart-atlas data. Lu depends only on the exchange
chart point (phases of the two sheets), exactly and texture-independently;
its alpha component is furthermore chart-point stable over the (0,4) class,
while beta already moves at 5%. Neither is a weak-basis invariant, and the
controlled hunt finds no physical constant at their values. This is the
WP10/11 lesson once more: a quantity can be exact, universal across
textures, and still be chart data. Cherish logged and discharged: the exact
per-chart-point constancy (1.5e-10) is now the recorded structure, and the
angle's non-identity is null-certified rather than merely unprobed.

Artifacts: checkers/wp32_dressing_angle.py, results/wp32_dressing_angle.json.
Depends on: claim:83e79fa2a84099e8cd4d, WP20, WP24a, WP24d.
