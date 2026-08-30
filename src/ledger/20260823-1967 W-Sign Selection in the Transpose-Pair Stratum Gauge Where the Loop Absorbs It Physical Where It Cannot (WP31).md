---
author: marici.Figueiredo
---

# WP31: W-sign selection in the transpose-pair stratum - gauge where the loop absorbs it, physical where it cannot

The 15 WP27 natural-singular boundary classes all share W = m10^2 - m01^2 in
their 5-edge sector, and (WP29) the W-sector determinant is a single perfect
matching THROUGH the transpose pair, so mass data fix only the product
m01*m10. WP27 showed the natural seed kills the split; the fit generates W
from nothing. Who chooses the sign?

Method (checker `checkers/wp31_w_sign_selection.py`, results
`results/wp31_w_sign_selection.json`, 15 classes, 31 minima, 5/5 gates):

- A. census of W forms vs phase-edge sector;
- B. partner identity for same-sector classes (chi2 degeneracy, phi negation,
  observables identity);
- C. flip-refit: from every minimum, refit from the transpose-swapped,
  phi-negated point and see where it lands;
- D. structural correlate.

## Findings

1. Phase edge in the SAME sector as W (8 down-sector classes, W = d10^2-d01^2,
   phase d01/d02): exactly 2 minima per class, one per sign. Partners have
   chi2 equal to 1.5e-12, observables identical to 8.3e-7 sigma, phi negated
   to 3e-8. The sign of W is PURE CHART GAUGE: one physical point, two
   texture charts related by (m01 <-> m10, phi -> -phi). Flip-refit is an
   exact involution: 16/16 flips land on the partner at chi2 3.3628.

2. Phase edge in the OPPOSITE sector (7 up-sector classes, W = u10^2-u01^2,
   phase d00/d01): ONLY u10 > u01 is viable - 15/15 minima, including the
   non-optimal ones at chi2 3.50..3.67. The mirror chart does not exist:
   15/15 flip-refits reach the mirror sign only at chi2 235..425512, i.e.
   10..550 sigma off the data. The selection is real and data-driven.

3. The correlate holds 15/15: same-sector <=> both signs viable (gauge Z2);
   opposite-sector <=> unique sign (physical selection).

## Interpretation

Nima's boundary stratum turns out to contain BOTH phenomena, separated by
where the loop holonomy lives. When the phase edge sits in the W sector, the
transpose swap can be absorbed by the holonomy (phi -> -phi) and the fit
creates a symmetric pair of charts of one physical point - W-sign is not an
observable. When it cannot be absorbed, the data themselves select the split
direction (heavier row carries the larger off-diagonal, u10 > u01, mirror
excluded by hundreds of sigma). This is the WP10/11 chart/physics
distinction operating inside a single fitted quantity: the same W = m10^2 -
m01^2 is chart gauge in one embedding and physical in another. For the
strong-CP thread: in the gauge cases det Y_d runs through the phase edge, so
the two charts are CP-conjugate presentations of the same point - consistent
with arg det being chart data, not an observable.

Artifacts: checkers/wp31_w_sign_selection.py, results/wp31_w_sign_selection.json,
tools/wp31_flip_probe.json (probe log).
Depends on: claim:83e79fa2a84099e8cd4d, WP20, WP21e, WP27, WP29, WP30.
