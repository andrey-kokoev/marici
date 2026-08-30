---
author: marici.Figueiredo
---

# WP29: no exact monomial syzygy; the cluster-2 lnM freeze sits at the mass-data floor

Question left by WP28: the rigid clusters freeze the reduced-form monomial lnM
BETWEEN texture classes (cluster 2: 1.3e-3, cluster 1: 0.079) while the
constituent edge logs disperse by e^1..e^3. Is that freeze an exact graph-forced
syzygy - M pinned by the mass-determined determinants |det Y_u| = y_u y_c y_t
and |det Y_d| = y_d y_s y_b - or an approximate collective property?

Method (checker `checkers/wp29_monomial_syzygy.py`, results
`results/wp29_monomial_syzygy.json`, 755 classes, 1210 minima, 5/5 gates):

- A. perfect matchings per sector for all 755 classes: 731 have single-matching
  dets in both sectors; 24 have a two-term det Y_d; det Y_u is ALWAYS
  single-term.
- B. numerical floor test: per-cluster regression of class-mean lnM on
  (ln|det Y_u|, ln|det Y_d|) fitted from edges, residual vs the det floor
  (between-class std of the lndet's = fit tolerance on mass data).
- C. exact algebra: is the M exponent vector a rational combination of the two
  det exponent vectors?
- D. det_u anchor census.

## Findings

1. NO exact monomial syzygy exists: 0/731 single-single classes have M's
   exponent vector in span(det_u, det_d). The freeze is not a monomial identity.

2. Cluster 2: lnM between-class std 1.3e-3 sits AT the mass-data tolerance
   floor (det_u floor 1.1e-3). The monomial is pinned as tightly as the masses
   themselves. But the det regression is NOT the mechanism: residual 8.7e-4 is
   barely below the raw 1.3e-3 and the coefficients are non-integer. lnM behaves
   like physical data without being reducible to det data - consistent with the
   WP26 reading (L level per class, physical gap and Vandermonde factors carry
   the variation).

3. Cluster 1 is structurally different: ALL 27 classes are diagonal-up textures
   (mu = 273) with det_u = u00 u11 u22 passing through the WP28 anchor edge
   u(2,2) = y_t CENTRAL. det_u is frozen to 7.3e-10 between classes - far below
   fit tolerance - while lnM spreads 0.079, an intermediate freeze 60x above
   cluster 2's, unexplained by det data (residual = 100% of variance).

4. Conspiracy clusters 0/3/4: lnM spreads 3.8..9.9, i.e. 18..10456x the mass
   floor. No determination at all.

## Interpretation

The rigid monomial freeze is a property of the viable fitted set per cluster,
not an algebraic identity of the texture graph. In cluster 2 the freeze is as
tight as the mass data themselves; in cluster 1 it is weaker and rides on a
fully anchored diagonal-up structure; in the conspiracy clusters it does not
exist. Combined with WP26/WP27: the selective object is the (L, K) level
structure of the viable solution set, and the monomial freeze is its shadow, not
its cause.

Artifacts: checkers/wp29_monomial_syzygy.py, results/wp29_monomial_syzygy.json.
Depends on: claim:83e79fa2a84099e8cd4d, WP20 valley audit, WP21e factorization,
WP25 center selection, WP26 level anatomy, WP28 edge dispersion.
