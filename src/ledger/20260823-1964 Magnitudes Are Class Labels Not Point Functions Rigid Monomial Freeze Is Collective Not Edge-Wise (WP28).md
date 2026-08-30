---
author: marici.Figueiredo
---

# WP28: magnitudes are class labels, not point functions; the rigid monomial freeze is collective, not edge-wise

Question carried over from WP26: the rigid phase clusters freeze the reduced-form
monomial lnM to 1e-3..1e-2. Is that because each EDGE's fitted magnitude is a
universal function of the physical point within the cluster? If so, M-freeze
would be a trivial consequence of edge-wise universality.

Method (checker `checkers/wp28_edge_dispersion.py`, results
`results/wp28_edge_dispersion.json`, 1210 minima, 755 texture classes, 4/4 gates):

- A. pooled dispersion per (cluster, sector, slot) across all minima;
- B. within-class dispersion per (texture class, sector, slot);
- C. lnM contrast: between-class vs within-class std per cluster;
- D. frozen-edge census (std < 0.01, n >= 40) identified against central couplings.

## Findings

1. WITHIN a texture class the fitted magnitude vector is essentially unique:
   median within-class edge std = 1.8e-4 over 576 (class, sector, slot) groups.
   Each class has one sharp magnitude point; its multiple minima are the same point.

2. ACROSS classes of the same cluster there is no edge-wise universality:
   81/83 pooled groups with n >= 20 disperse with std 0.3..3.3
   (per-cluster medians 1.0..1.7). Different textures assign wildly different
   magnitudes to the same (sector, slot).

3. Exactly two frozen anchor edges exist cluster-wide:
   - cluster 1, u(2,2): frozen to ln(y_t CENTRAL) = -0.03355678352884276 with
     offset -7e-18 - the scan CENTER value of the top coupling, not a per-point
     fitted coupling;
   - cluster 3, u(0,2): frozen near ln y_c (offset 0.016).

4. Yet lnM is frozen BETWEEN classes in the rigid clusters while the constituent
   edges disperse by e^1..e^3:
   - cluster 2: between-class lnM std 1.3e-3 (edge median 1.72);
   - cluster 1: between-class lnM std 0.079 (edge median 1.01);
   - conspiracy clusters 0/3/4: between-class lnM std 3.8..9.5.

## Interpretation

The rigid-cluster monomial is a cluster-level COLLECTIVE invariant realized by
wildly different individual edge assignments. It is invisible at the single-edge
level and sharp at the monomial level. Magnitudes are class labels, not point
functions: the fitted vector is unique per class but carries no cluster-universal
edge content. The WP26 M-freeze is therefore not explained by edge universality;
it is a genuine collective constraint on the monomial the fit preserves while
moving edges freely.

The cluster-1 anchor u(2,2) = y_t CENTRAL to machine precision says those
textures hard-wire the scan-center top coupling as an edge and build all mixing
from the remaining edges - a structural property of the texture family, not a fit
coincidence (42/42 minima, std 3e-17).

## What this refocuses

The next question is the mechanism of the collective freeze: is lnM's
between-class constancy in clusters 1/2 an EXACT syzygy the texture graph
forces (e.g. det-like products pinned by mass data), or an approximate valley
flat direction? A graph-theoretic determinant/matching computation can decide
this without fitting.

Artifacts: checkers/wp28_edge_dispersion.py, results/wp28_edge_dispersion.json.
Depends on: claim:83e79fa2a84099e8cd4d (flavor admission program), WP20 valley
audit, WP21e universal factorization, WP25 center selection, WP26 level anatomy.
