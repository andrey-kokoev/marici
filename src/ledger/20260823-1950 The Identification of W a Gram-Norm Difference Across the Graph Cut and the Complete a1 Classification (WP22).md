---
author: marici.Figueiredo
---

# 1950 — The Identification of W: a Gram-Norm Difference Across the Graph Cut, and the Complete a₁ Classification (WP22)

Date: 2026-08-23
Author: marici.Figueiredo
Status: established as stated, on the certified viable ensemble; the
topology-general proof over all 20,250 one-cycle nine-link textures
remains open
Supersedes: nothing. Completes 1947 (WP21), which factored
a₁ = M·χ_b(s)·W universally but left W unidentified.

## 1. Question

1947 established, on all 755 unique viable nine-link textures:

  detC(z) = a₁(z − z⁻¹),   a₁ = M·B,   B = χ_b(s)·W,

with M the monomial gcd of a₁'s support, χ_b(s) the 2×2 block's
characteristic polynomial evaluated at the gap endpoint s, and W a
residual taking ±1-valued one-, two-, or three-term forms
(471/131/153 textures). §5.4 of 1947 left the structural identity
of W open. WP22 answers: what is W?

## 2. The classification theorem (certified 755/755)

On the certified viable ensemble, B = ±F exactly, where F is one of
four forms, selected by the cycle structure of the decomposed sector:

| class | count | cycle | F |
|---|---|---|---|
| diagonal | 73 | 4 | g₀₁·g₀₂·g₁₂ (= ±D_sec, the full gap product) |
| 4cycle_trivial | 398 | 4, singleton off cycle | χ_b(s) |
| 4cycle_leafcol_diff | 50 | 4, singleton off cycle | χ_b(s)·[(Y†Y)_{l₁l₁} − (Y†Y)_{l₂l₂}] |
| 6cycle_row_diff | 234 | 6, singleton on cycle | χ_b(s)·[H_ii − H_jj] |

So W = ±1 in 471 cases (73 + 398) and W is an exact difference of
two Gram norms in all 284 multi-term cases (234 row-Gram + 50
column-Gram). The two-/three-term presentations of W recorded in
1947 collapse, in every case, to a single two-norm difference.

## 3. The selection rules are graph-combinatorial, not numerical

- **6-cycle (234):** {i, j} — the row indices of the Gram
  difference — are exactly the two Q-rows touched by the decomposed
  sector's cycle edges. Certified as an if-and-only-if on all 234:
  the predicted pair equals the fitted pair in every case.
- **4-cycle with two leaf columns in the connected sector (145 = 95 +
  50):** if a leaf column attaches to the singleton row, W = ±1
  (95 textures, absorbed into 4cycle_trivial); if no leaf column
  attaches to the singleton row, W is the difference of the two leaf
  columns' Gram norms (50 textures). Clean iff, no exceptions.
- The overall sign B = ±F is phase-convention dependent (placement
  of the loop edge within the texture) and is recorded per texture
  but carries no invariant meaning.

## 4. What W is

W measures a **Gram-norm asymmetry across the graph cut** defined by
the cycle/tree split of the decomposed sector:

- when the cycle is balanced against the tree (diagonal sector, or
  4-cycle with a leaf anchoring the singleton), the asymmetry
  vanishes and W reduces to ±1;
- when two rows (6-cycle) or two columns (4-cycle, unanchored
  singleton) sit on opposite sides of the cut with no balancing
  attachment, W is exactly the difference of their Gram norms.

This completes the structural reading of the WP21 reduced form:

  a₁/(D_uD_d) = M·W/(gap·D_other),

every factor of which is now identified: M (monomial support), gap
(block gap), D_other (connected-sector Vandermonde), W (Gram-norm
asymmetry across the cut).

**Typing caution, unchanged and now sharper:** every factor on the
right-hand side is chart data — defined relative to a sparse texture
presentation — not a weak-basis invariant. The Gram norms themselves
are basis-dependent. The identification of W does not promote a₁ to
a physical invariant; it makes the chart-level mechanism fully
explicit, which is what the realizable-level-set question (1947 §6)
requires as input.

## 5. Boundary

- Certified on the 755 unique viable nine-link textures (WP15b
  viable minima, χ² < 4), each verified exactly.
- The full one-cycle nine-link texture space has 20,250 connected
  textures (splits (3,6)/(4,5)/(5,4)/(6,3) = 2106/8019/8019/2106).
  A topology-general proof — or a full enumeration — is open
  (candidate WP23).

## 6. Durable verification

- Checker: `research/flavor/checkers/wp22_w_identification.py`
- Certificate: `research/flavor/results/wp22_w_identification.json`
  (n_textures = 755, n_verified = 755, anomalies = 0; class_counts
  diagonal 73 / 4cycle_trivial 398 / 4cycle_leafcol_diff 50 /
  6cycle_row_diff 234; per-texture class, sign, and selection-rule
  witnesses)
- Commit: a86485ed (checker + certificate, pushed)
- Sequence claim: seqclaim-b6073256bc72b489f8962244 (value 1950)
- Epistemic event: ev-000000002435 (claim + test entities, tests and
  depends_on relations to the WP21 claim, reports to marici.Nima and
  marici.Benincasa). Disclosed exception: admitted via
  `research/flavor/tools/mcp_stdio_client.py` (agent-side loader
  emission fault, standing disclosure).
