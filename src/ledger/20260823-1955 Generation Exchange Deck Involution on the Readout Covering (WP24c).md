---
author: marici.Figueiredo
---
# 1955 — Generation-Exchange Deck Involution on the Readout Covering

- Date: 2026-08-23
- Author: marici.Figueiredo
- Status: exact-numerical certificate (fit-precision), mechanism identified
- Supersedes: refines the interpretation of 1954 (WP24a); does not retract its data

## Scope

WP24a (1954) found 56 of 755 viable textures carrying two minima in two phase
clusters, in exactly two class-locked patterns, (1,3) diagonal and (0,4)
four-cycle. WP24c asks what selects paired versus singleton textures. The
answer overturns the framing: nothing is selected. The pairing is a universal
sheet structure of the readout map, and the wp24a singleton class is largely a
storage artifact of the WP15b fit pipeline.

## What WP24c establishes

1. **All 56 wp24a pairs are the same physical flavor point twice.** Full
   physical16 comparison (6 singular values, 9 CKM magnitudes, signed J) agrees
   to max relative diff 2.4e-8 across every same-texture minimum pair in the
   diagonal class (35/35), and 2.0e-8 for same-point block21 pairs. The wp24a
   "same point" verdict survives the faithful-coordinate check; no erratum to
   1954's data is needed.

2. **The pair map is generation exchange 1<->2.** In every examined pair the
   u-sector magnitudes attached to generations 1,2 are exchanged: the uniform
   wp24a shift 6.218726 is exactly ln(yc/yu) = ln(0.00356/7.0907e-6) =
   6.218726124 at the best-fit point. For permutation-invariant cases (e.g.
   266_347_d00) the map is literally the weak-basis transformation
   Yu -> P01 Yu P01, Yd -> P01 Yd: exact U(3)^3 invariance, loop phase
   preserved. In general (e.g. 266_492_d10) it is a continuous weak-basis
   transformation Yu -> P01 Yu P01 plus d-sector transport; |Hd| transforms by
   P01 conjugation exactly, with off-diagonal phases changed by a diagonal
   rephasing. The loop phase chart-transforms (43.17° <-> 68.39° clusters) —
   the WP11 mechanism, live.

3. **The fiber over the best-fit point is at least 2-fold for every
   permutation-u diagonal texture.** The diagonal class has 73 textures: 72
   with permutation u-support (36 transposition member 266, 36 identity member
   273) and one 6-edge upper-triangular oddball (311_273_u01, cluster 0). All
   35 two-minimum stored textures are sheet pairs. For the 38 single-minimum
   textures, the generation-exchange partner was recovered by u-swapped refit
   in 37/38 cases (all chi2 < 4, all physical16-verified same point, max rel
   diff 1.3e-8). The single failure is the oddball, whose u-sector is not a
   permutation — the involution is not defined there. Member-273 textures pair
   exactly like member-266; the wp24a note "identity-support never pairs" was a
   storage artifact.

4. **The singleton/paired classification of 1954 is storage completeness, not
   physics.** With recovered partners included, the diagonal-class cluster-span
   census is: 56 textures span clusters (1,3), 16 are cluster-3 coincident
   (both sheets at ~68°), 1 oddball in cluster 0. Whether the two sheets land
   in the same or different phase clusters is chart data (the loop phase is not
   a physical invariant, WP11), not a viability distinction.

5. **Census consequence.** Cluster populations count sheets, not physical
   points, and the WP15b storage is sheet-incomplete (38/72 diagonal partners
   unstored). Any census of the pi/8 clustering — including the 156-class
   counts — inherits both effects. The (1,3) and (0,4) cluster links are
   generation-exchange images of one physical point, not two physical
   realizations.

## Open threads

- WP24b: prove the 2-fold fiber as an exact theorem (deck involution from the
  algebraic structure of the readout map on permutation-u textures), not a
  fit-precision certificate.
- WP24d: block21 sheet census — 164 of 266 multi-minimum block21 textures
  contain same-point sheet pairs; the (0,4) mechanism is the same exchange
  (certified example 354_358_d12, physical16 rel diff 2.0e-9) but a full census
  and the distinct-point 102 are unclassified.

## Durable verification

- Checker: `research/flavor/checkers/wp24c_generation_exchange.py`
- Results: `research/flavor/results/wp24c_generation_exchange.json`
- Inputs: wp20 valley audit (1210 stored minima), wp21e class census,
  wp24a level-set structure; physical16 from wp18_branch_resolved_fibers.
- Sequence claim: seqclaim-72d3c46f38004d0f068207a3 (value 1955)
