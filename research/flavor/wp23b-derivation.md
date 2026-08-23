# WP23b — Derivation of the a₁ classification from the commutator determinant

Status: derivation backbone. Each step is exhibited exactly on one
representative per class (checker `checkers/wp23b_derivation_representatives.py`,
certificate `results/wp23b_derivation_representatives.json`, ALL OK);
the full census over all 6,552 topologies is WP23a (ledger 1951).
A per-orbit write-up over the 18 orbits of entry 1054 is future work.

## 0. Universal frame

For 3×3 Yukawas with one phase edge, H_u and H_d are Hermitian
Laurent in z = e^{iφ} of degree ≤ 1, and C(z) = [H_u, H_d] is
traceless anti-Hermitian on |z| = 1. Hence

  det C = tr C³ / 3,     detC(z⁻¹) = −detC(z)

so only odd harmonics can appear; WP13/entry 1054 showed the support
is in fact exactly {±1} on every admissible support. WP23b derives
the coefficient a₁.

## 1. Diagonal class (representative 84_159)

Y_u has permutation support, so H_u = diag(a, b, c) is z-free and the
phase lives in the connected sector X = H_d. For any diagonal D and
matrix X, the commutator has zero diagonal and its determinant is the
two-3-cycle formula

  det[D, X] = −(a−b)(a−c)(b−c) · (x₁₂x₂₃x̄₁₃ − x₁₃x̄₁₂x̄₂₃).

The Vandermonde factor is exactly the WP22 "full gap product"
g₀₁g₀₂g₁₂. For the representative, the overlap entries are

  x₀₁ = d00d10·z + d01d11,   x₀₂ = d01d21,   x₁₂ = d11d21,

and the bracket telescopes:

  x₁₂x₂₃x̄₁₃ − x₁₃x̄₁₂x̄₂₃ = d00d01d10d11d21² · (z − z⁻¹).

The z-carrying factor x₀₁ is linear in z; the constant terms cancel
between the two 3-cycle products, leaving the anti-palindromic
first-harmonic difference. Therefore

  detC = −(g₀₁g₀₂g₁₂) · d00d01d10d11d21² · (z − z⁻¹),

i.e. a₁ = M·B with B = ±(gap product), W = ±1. ∎ (certified exactly)

## 2. Block-2+1 classes: the χ_b(s) factor

For all three block21 representatives the decomposed sector is
H_u = B ⊕ {s} with B the 2×2 block (rows {0,2}, singleton row 1 in
the representatives) and s = u11². The single determinant computation
factors as

  detC = ±M·(z − z⁻¹)·χ_b(s)·W,

where χ_b(λ) = λ² − tr(B)λ + det B and the remaining factor W is
read off class by class:

- **4cycle_trivial (85_87):** W = 1. The attachment structure of the
  connected sector supplies only the monomial M = d00d01²d11²d20u00u20.
- **4cycle_leafcol_diff (85_205):** W = d02² − d21², the difference
  of the two leaf columns' Gram norms, appearing as the difference of
  squares (d02−d21)(d02+d21) in the factorization.
- **6cycle_row_diff (85_94):** W = d01² + d02² − d20², the difference
  of the connected sector's row-Gram norms on the two cycle-touched
  rows.

All three are certified exactly by the checker: detC divided by
χ_b(s)·(z − z⁻¹) is ±(monomial)·W with the predicted W.

## 3. Unification with WP21

The diagonal Vandermonde and the block21 χ_b(s) are one mechanism:
diagonalizing B (a Q-side basis rotation, which leaves det[Hu, Hd]
invariant) gives D = diag(λ₁, λ₂, s) and

  (λ₁−λ₂)(λ₁−s)(λ₂−s) = ±(λ₁−λ₂)·χ_b(s),

with (λ₁−λ₂)² = disc_b — precisely the WP21 Vandermonde identity
D_sec² = disc_b·χ_b(s)². The diagonal class is the special case where
B is already diagonal in the texture frame. The class distinctions
(W-forms) live entirely in the connected sector's attachment to the
adapted frame: balanced attachment ⟹ W = 1; unbalanced pair ⟹
Gram-norm difference.

## 4. The CP-trivial class

The WP23a rule has the same reading: the bracket
x₁₂x₂₃x̄₁₃ − x₁₃x̄₁₂x̄₂₃ (diagonal case) needs all three Gram
off-diagonals nonzero; one disjoint row pair kills both 3-cycle
products. The block21 reduction distributes the bracket over fewer
overlap entries, so two disjoint pairs are needed. detC ≡ 0 is thus a
bracket-vanishing condition, exactly when the connected sector's
row-overlap graph is too sparse to form the required products.

## 5. What remains for a complete proof

- Per-orbit derivation over the 18 orbits of entry 1054 (the
  representatives above cover the four classes but not every support
  pattern within a class).
- Phase-placement independence of the class labels within a topology
  (support-level statement is entry 1054; class labels audited here
  only for the canonical placement).
