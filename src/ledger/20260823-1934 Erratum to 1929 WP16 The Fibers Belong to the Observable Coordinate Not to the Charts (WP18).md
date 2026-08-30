---
author: marici.Figueiredo
---

# 1934 — Erratum to 1929 (WP16): The Fibers Belong to the Observable Coordinate, Not to the Charts — physical10 Is Two-to-One (WP18)

## What 1929 got wrong

Ledger 1929 (WP16) claimed that physical10 = (6 singular values,
|Vus|, |Vub|, |Vcb|, signed J) is "generically a COMPLETE coordinate on
the physical quotient", and read the multi-root fibers of the chart map
— in particular the orbit-15 chart (85,234) carrying two exact
preimages with distinct loop phases phi = -1.5755 and phi = -0.9018 —
as chart-intrinsic multiplicity over ONE physical point ("same complete
physical invariant data, different loop phase").

Both readings are wrong.  The dimension count 36 - 27 + 1 = 10 gives
generically FINITE fibers, not injectivity.  The CKM block
(|Vus|, |Vub|, |Vcb|, J) fixes the PDG parameters s12, s13, s23 and
sin delta = J / (c12 s12 c23 s23 c13^2 s13), but not sign(cos delta):
the two branches delta and pi - delta reproduce all ten observables
while differing in |Vtd|, |Vcd|, |Vcs|, |Vts|.  physical10 is
generically TWO-to-one on the physical quotient.

## The decisive checks

1. The two orbit-15 roots are NOT the same quotient point: root A has
   |Vtd| = 0.0087281843, root B has |Vtd| = 0.0112926701 (30% apart);
   |Vcd|, |Vcs|, |Vts| differ likewise.  The three measured magnitudes
   and J agree to 1e-7, as imposed.
2. The PDG branch derivation from the p* CKM block predicts
   |Vtd| = 0.0087281973 (cos delta > 0) and 0.0112926353
   (cos delta < 0); the roots match their branches to 3e-6 and 1e-6
   respectively, and mis-match the other branch at 23-29%.
   Checker `wp18a_branch_derivation.py`.
3. The sparse square-root problem is NOT degenerate: root A's exact
   down-Gram matrix H_A admits a UNIQUE same-pattern square root
   (300-start exact solve).  The two roots correspond to two genuinely
   different Gram matrices mapping to the same physical10.
4. Branch-resolved rerun over all 21 covering orbit halves
   (800 starts each, roots classified by full physical16 image):
   60 roots = 32 small-delta + 28 large-delta.  Every covering rep
   carries roots on BOTH branches (the single exception, orbit 15
   swap=True, is a sampling miss — it carried a large-branch root at
   other densities).  Per-branch per-chart degrees are 1-3 at this
   density.  Checker `wp18_branch_resolved_fibers.py`.

## Corrected statements

- The WP16 fiber degrees 1-7 were inflated by the two-sheeted
  observable coordinate (roughly a factor of 2).  Per physical quotient
  point, a covering chart carries 1-3 exact preimages at current
  sampling (still rigorous lower bounds only).
- The orbit-15 two-phase pair is one preimage per delta-branch.  It is
  NOT a realization of "same complete weak-basis invariant data,
  different phi".  That falsifier form remains realized by the WP11-WP13
  exact U(3)_Q orbit counterexample — which is unaffected, since a
  weak-basis transformation fixes the quotient point exactly.
- The loop phase varies BETWEEN the two physical points sharing the
  measured observables: within one chart, phi is a coordinate of the
  physical point (it predicts |Vtd|); across charts it does not descend
  (WP11-WP13).  Both halves of the chart-data verdict stand, now with
  the correct mechanism attached.
- WP16c coverability is unaffected: rank-10 Jacobians make each
  covering chart a local diffeomorphism onto physical10-space, hence a
  local cover of the (two-sheeted) observable image of the quotient.
- WP17 (orbit-3 exclusion) is unaffected: the certified Gram criterion
  used the seed's full exact V, and excluding the physical10 target
  excludes both branches a fortiori.

## Lesson recorded

Finite-to-one is not one-to-one.  Any future "fiber" claim about the
chart map must be made against a faithful quotient coordinate —
physical16 (6 singular values, all nine |V| entries, signed J) — not
against the ten measured observables.  Benincasa's refinement of the
falsifier language, applied to my own WP16 claims, is what the WP18
erratum implements.

## Artifacts

- `research/flavor/checkers/wp18_branch_resolved_fibers.py`,
  `wp18a_branch_derivation.py`
- `research/flavor/results/wp18_branch_resolved_fibers.json`,
  `wp18a_branch_derivation.json`
- Corrects: ledger 1929 (WP16 fiber claims only; WP16c/WP17 stand).
