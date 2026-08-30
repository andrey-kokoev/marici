---
author: marici.Figueiredo
---

# 1951 — The a₁ Classification Is Topology-General: All 6,552 Full-Rank One-Cycle Nine-Link Textures, and the Exact CP-Triviality Rule (WP23a)

Date: 2026-08-23
Author: marici.Figueiredo
Status: established as stated, on the full-rank one-cycle nine-link
support space; derivation from first principles (WP23b) in progress
Supersedes: nothing. Extends 1950 (WP22) from the 755-texture viable
ensemble to the entire admissible support space of 1054.

## 1. Question

1950 classified a₁ on the 755 viable textures into four classes with
graph-combinatorial selection rules. Left open: is the classification
an artifact of the viable ensemble, or does it hold on every
admissible support? And what happens on supports where the viable
ensemble never lands?

## 2. The enumeration

All connected nine-link support pairs (mask_u, mask_d), splits
(3,6)/(4,5)/(5,4)/(6,3) = 2106/8019/8019/2106 = 20,250 connected
topologies (anchor reproduced exactly). Imposing the 1054 hypothesis
— both sectors full-rank (perfect matching each) — leaves **6,552**
topologies (468/2808/2808/468). Phase placed canonically on the first
sorted cycle edge (one representative per rephasing orbit of
placements).

For each topology the full WP22 analysis runs symbolically with
algebraically independent edge magnitudes.

## 3. Result: the four classes cover everything, plus one new class

| class | count |
|---|---|
| 4cycle_trivial (B = ±χ_b(s)) | 3456 |
| 6cycle_row_diff (B = ±χ_b(s)·(H_ii − H_jj)) | 1296 |
| diagonal (B = ±g₀₁g₀₂g₁₂) | 720 |
| 4cycle_leafcol_diff (B = ±χ_b(s)·(col Gram diff)) | 432 |
| detC_zero (detC ≡ 0 identically) | 648 |

- All 5,904 topologies with detC ≢ 0 verify B = ±F with the WP22
  selection rules — **zero anomalies, zero new classes**. The WP22
  classification is topology-general, not a viable-ensemble artifact.
- The 648 detC_zero topologies are CP-trivial by support alone:
  J ≡ 0 for every choice of magnitudes and phase. No viable texture
  can live on them (consistent with 1950: all 755 viable verify).

## 4. The exact CP-triviality rule

Certified as an if-and-only-if on all 6,552 (cross-tab: 648/648
true-positive, 5,904/5,904 true-negative):

  detC ≡ 0  ⟺  (decomposed sector diagonal AND connected sector has
                ≥ 1 disjoint row pair)
            ∨  (decomposed sector block-2+1 AND connected sector has
                ≥ 2 disjoint row pairs)

where "disjoint row pair" means two Q-rows whose column supports in
the connected sector are disjoint (the corresponding Gram off-diagonal
vanishes identically). Mechanism: for a diagonal decomposed sector,
detC is proportional to x₁₂x₂₃x̄₁₃ − x₁₃x̄₁₂x̄₂₃, and a single zero
off-diagonal kills both 3-cycle products; the block-2+1 reduction
needs two. All 648 cases are 4-cycles; no 6-cycle topology is
CP-trivial.

Boundary: the rule is certified on this support space, phase on the
canonical cycle edge. Phase-placement independence within a topology
is certified by 1054 for the support theorem but not re-audited here
for the class labels.

## 5. Meaning for the program

- Roughly 9.9% of admissible one-cycle topologies are CP-trivial by
  support. The paper's viable textures avoid them; the overlap-graph
  predicate says exactly which.
- The classification theorem is now stated on the natural domain
  (full-rank one-cycle supports) with no viability input anywhere —
  it is a pure support theorem, the right substrate for the WP23b
  first-principles derivation.
- Nothing changes the typing: all factors remain chart data.

## 6. Durable verification

- Checker: `research/flavor/checkers/wp23_topology_enumeration.py`
  (enumeration + classification + detC_zero rule cross-tab)
- Certificate: `research/flavor/results/wp23_topology_enumeration.json`
  (n_topologies 6552, n_verified 5904, split anchor ok,
  detc_zero_rule_ok true)
- WP22 checker patch (detC_zero distinguished from support anomaly):
  verified not to alter the committed WP22 census (755/755 still sign)
- Commit: bab761b2 (pushed)
- Sequence claim: seqclaim-731fe404d8a1f68a11538825 (value 1951)
- Epistemic event: ev-000000002443 (claim + test + reports to Nima/Benincasa;
  admitted via tools/mcp_stdio_client.py, standing loader disclosure)
