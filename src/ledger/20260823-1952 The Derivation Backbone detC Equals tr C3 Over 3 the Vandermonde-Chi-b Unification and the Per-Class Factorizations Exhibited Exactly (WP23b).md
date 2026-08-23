---
author: marici.Figueiredo
---

# 1952 — The Derivation Backbone: detC = tr C³/3, the Vandermonde–χ_b(s) Unification, and the Per-Class Factorizations Exhibited Exactly (WP23b)

Date: 2026-08-23
Author: marici.Figueiredo
Status: derivation backbone — every step exhibited exactly on one
representative per class; the census over all 6,552 topologies is
1951; a per-orbit write-up over the 18 orbits of 1054 remains open
Supersedes: nothing. Supplies the derivation for 1950–1951.

## 1. What is derived

1950–1951 classified a₁ into four classes plus the CP-trivial locus,
certified by census. This entry records the derivation chain, each
link verified symbolically on a representative:

**Universal frame.** C(z) = [H_u, H_d] is traceless, so
detC = tr C³/3; anti-Hermiticity on |z| = 1 forces
detC(z⁻¹) = −detC(z), hence odd harmonics only.

**Diagonal class (84_159).** For diagonal D and any X,
det[D, X] = −(a−b)(a−c)(b−c)(x₁₂x₂₃x̄₁₃ − x₁₃x̄₁₂x̄₂₃) — the
two-3-cycle formula. The Vandermonde is the WP22 gap product. The
bracket telescopes: with x₀₁ = d00d10·z + d01d11 and x₀₂, x₁₂
z-free, the constant terms cancel between the two 3-cycle products,
leaving exactly d00d01d10d11d21²·(z − z⁻¹). Hence W = ±1.

**Block-2+1 classes.** One determinant computation factors as
detC = ±M·(z − z⁻¹)·χ_b(s)·W with χ_b the 2×2 block's characteristic
polynomial at the singleton s, and W read off the connected sector's
attachment:

- 4cycle_trivial (85_87): W = 1;
- 4cycle_leafcol_diff (85_205): W = d02² − d21², appearing as the
  difference of squares (d02−d21)(d02+d21);
- 6cycle_row_diff (85_94): W = d01² + d02² − d20², the row-Gram
  difference on the cycle-touched rows.

**Unification.** Diagonalizing the 2×2 block (a detC-preserving
rotation) gives Vandermonde = ±(λ₁−λ₂)·χ_b(s) with
(λ₁−λ₂)² = disc_b — the WP21 identity D_sec² = disc_b·χ_b(s)². The
diagonal class is the special case where the block is already
diagonal in the texture frame; the W-forms live entirely in the
connected sector's attachment to the adapted frame.

**CP-triviality.** The bracket needs all its Gram off-diagonals: one
disjoint row pair kills both 3-cycle products in the diagonal case;
the block21 reduction distributes over fewer overlaps, needing two.
The 1951 overlap-graph rule is exactly bracket-vanishing.

## 2. Scope

Representatives cover the four classes, not every support pattern
within a class (census coverage is 1951's). Phase-placement
independence of class labels within a topology is not re-audited
beyond 1054's support-level statement. Typing unchanged: every factor
is chart data.

## 3. Durable verification

- Packet: `research/flavor/wp23b-derivation.md`
- Checker: `research/flavor/checkers/wp23b_derivation_representatives.py`
- Certificate: `research/flavor/results/wp23b_derivation_representatives.json`
  (all_checks_ok true; per-class remainders and signs recorded)
- Commits: 959f4177 (packet + checker + certificate), 5ef06c51
  (frontmatter repair on 1936/1937/1947/1950/1951)
- Sequence claim: seqclaim-25ab10a9b3fa5270906a799b (value 1952)
- Epistemic event: ev-000000002448
