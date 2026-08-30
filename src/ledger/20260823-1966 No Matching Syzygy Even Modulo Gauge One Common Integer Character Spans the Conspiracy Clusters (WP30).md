---
author: marici.Figueiredo
---

# WP30: no matching syzygy even modulo gauge; one common integer character spans the conspiracy clusters

Direct answer to Nima's 23:03 request (exact combinatorial test, typed outcomes,
minimal-support integer relations instead of regressions).

Method (checker `checkers/wp30_exact_characters.py`, results
`results/wp30_exact_characters.json`, 755 classes, 5/5 gates):

- A. widened exact syzygy: encode EVERY perfect-matching exponent vector (both
  sectors) plus the 12-vector rephasing lattice (row/column sums) and test
  rational row-space membership of each class's WP21e monomial exponent vector.
  Typed outcomes: T1 exact matching syzygy; T2 syzygy modulo rephasing gauge;
  T3 no syzygy.
- B. conspiracy characters: over class-mean vectors (lnM, lnW, lngap, lnDo),
  enumerate all primitive integer characters with coefficients in [-6,6] and
  find the minimal-spread combination per cluster; compare with the WP26
  reduced-form character (1,1,-1,-1) = lnL; test cross-cluster commonality.

## Findings

1. T1 = 0 and T2 = 0 over all 755 classes. The monomial M is not a
   perfect-matching product, not even up to rephasing gauge. Combined with
   WP29 (0/731 against the det vectors): there is NO exact algebraic identity
   behind the rigid-cluster lnM freeze at any level of the graph's matching
   lattice. Every class is T3 - the freeze lives only in the viable fitted set.

2. The WP26 character (1,1,-1,-1) is the UNIQUE optimal small-integer
   character in every conspiracy cluster: best primitive q with |q_i| <= 6 is
   exactly +/-(1,1,-1,-1) in clusters 0, 3 and 4. One common character spans
   all three conspiracy clusters (spreads 0.162 / 0.039 / 0.089); the nearest
   competitor character leaves 4..6 nats. The conspiracy is therefore ONE
   source-derived character - the reduced form L = M W/(gap D_other) - not a
   per-cluster numerical coincidence.

3. The conspiracy is approximate, not exact: residual lnL spreads are
   0.039..0.162, far above machine zero - this residual is precisely the
   per-class L-level property of WP25b. Cancellation ratios (largest input
   coordinate std / character spread) are 27x..59x.

4. New exact freezes in the rigid clusters (controls): cluster 1's lngap is
   frozen between classes to machine zero (spread 0.0) - for diagonal-up
   textures H_u is diagonal so the gap is literally mass data; cluster 2's
   lnW is exactly 0 between classes (all W = +/-1, reconfirming WP26's
   all-330 census at character level).

## Interpretation

The trichotomy Nima requested resolves cleanly: no exact syzygy, no torsion
quotient - the only exact structure is the single reduced-form character
itself, shared by all conspiracy clusters, plus cluster-specific exact
single-coordinate freezes (gap in cluster 1, W in cluster 2, det_u in
cluster 1 via the y_t anchor). The fitted viable set is the selective object;
the graph matching lattice contributes no hidden identities.

Artifacts: checkers/wp30_exact_characters.py, results/wp30_exact_characters.json.
Depends on: claim:83e79fa2a84099e8cd4d, WP20, WP21e, WP25, WP26, WP28, WP29.
