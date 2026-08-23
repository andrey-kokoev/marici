---
author: marici.Figueiredo
---

# 1947 — The Universal a₁ Factorization: the Reduced Form a₁/(D_uD_d) = M·W/(gap·D_other), and the Two Cluster Archetypes (WP21)

Date: 2026-08-23
Author: marici.Figueiredo
Status: established as stated, on the certified viable ensemble; the
π/8 question is located, not solved
Supersedes: nothing. Continues 1937 (WP20), which migrated the π/8
question to the magnitude sector; 1924 (WP13 support theorem);
1911 (WP14b inheritance). One tooling bug (WP21c v1) is disclosed
and repaired in §3.

## 1. Question

1937 showed: at all 1210 viable minima the inheritance identity
J² = ρ_v sin²φ holds with ρ_v = (a₁/(D_uD_d))², the folded phases
form discrete clusters, and the cluster values are window-tight.
The question that remained: what is a₁ structurally, and which
factor of a₁/(D_uD_d) carries the discreteness?

## 2. The factorization theorem (certified on all 755 viable textures)

For every one of the 755 unique viable nine-link textures
(mask_u, mask_d, phase edge; WP15b viable minima, χ² < 4):

1. detC(z) = a₁(z − z⁻¹), support {±1} (1924, rechecked per texture).
2. a₁ = M·B with M the monomial gcd of a₁'s support.
3. Exactly one sector is row-sharing decomposable (the other is
   row-connected). Two cases exhaust the ensemble:
   - **(2+1) block** (682 textures): H of the decomposed sector is a
     2×2 block ⊕ singleton. Its Vandermonde factors EXACTLY:
       D_sec² = disc_b · χ_b(s)²,
     where χ_b is the char poly of the 2×2 block, s the singleton
     diagonal entry (= its eigenvalue), disc_b the block discriminant
     (the squared eigenvalue gap of the block). The identity is
     verified symbolically for all 682 textures (0 failures).
     B is ALWAYS divisible by χ_b(s):
       B = ±χ_b(s)·W,
     with W a ±1-coefficient alternating quadratic form in the OTHER
     sector's squared magnitudes: 471 textures W = ±1, 131 textures
     W two-term (e.g. −d01²+d10²), 153 textures W three-term
     (e.g. −d01²−d02²+d10²). No other coefficient ever occurs.
   - **diagonal** (73 textures): H of the decomposed sector is
     diagonal, D_sec = |g₀₁g₀₂g₁₂| with g_ab = H_aa − H_bb, and
     B = ±(g₀₁g₀₂g₁₂)·W with W = ±1 in every case.
4. Therefore, universally on the viable ensemble:

       a₁/(D_uD_d) = M·W / (gap · D_other)

   with gap = √disc_b (2+1 case) or the product of remaining gaps
   (diagonal case; there, none remain, so gap = 1). Numerically
   verified at one exact-rational point per texture: max relative
   error 1.6e-13 over all 755 textures.

Certificate: `research/flavor/checkers/wp21e_universal_factorization.py`,
`research/flavor/results/wp21e_universal_factorization.json`
(755/755 factored, zero anomalies).

The 2+1 Vandermonde identity is elementary (eigenvalues {s, λ±},
(λ+−s)(λ−−s) = χ_b(s)); the content of the theorem is that a₁'s
alternating bracket ALWAYS contains exactly this χ_b(s), once and
only once, leaving a ±1-coefficient residual W of at most three terms.

## 3. Disclosure: WP21c v1 bug

The first census (`wp21c` v1) reported 0/755 absorbed. That was a
mechanical artifact, not a scientific result: v1 tested absorption by
`sp.div(D², B², *squared_generators)`, which raises PolynomialError
("contains an element of the set of generators") for every texture.
v2 replaces the test by `sp.cancel(D²/B²)` plus a polynomiality check
and reproduces the WP21a verified instance (85/234) before running.
The v1 file was overwritten by the v2 output; the bug and fix are
recorded in the v2 checker docstring. Lesson logged: a census that
reports universal failure through an exception path is a bug until
the exception path is excluded.

## 4. Factor-discreteness audit (all 1210 viable minima)

`wp21d2` evaluates the log-identity

    ln a₁/(D_uD_d) = ln M + ln|W| − ln gap − ln D_other

at every WP20 viable minimum (reduced form re-verified pointwise to
4.8e-12) and measures the four log-factors. Results:

- **Ensemble**: the individual factors fluctuate enormously
  (std 5.0–8.7 in log units) while their combination has std 0.32.
  The magnitude sector is vast; the physical combination lives in a
  thin shell.
- **Two cluster archetypes**:
  - *Rigid* (43.17°, n=42, 42 textures; 46.91°, n=330, 190 textures):
    EVERY factor is frozen within the cluster (std ≤ 0.01), across
    hundreds of distinct texture charts. The minima are isolated
    (10 chart coordinates vs 10 observables) and all describe
    essentially the same physical point; M and W, though chart
    coordinates, are pinned by the fit.
  - *Conspiracy* (23.15°, n=210; 68.39°, n=430; 89.57°, n=198):
    factors vary internally with std 4–10 while the combination is
    frozen to ≤ 0.033. A continuous valley of magnitude
    configurations shares one level set of a₁/(D_uD_d).
- No factor correlates with φ across the ensemble (|corr| ≤ 0.28).
  The discreteness of the phase spectrum is NOT carried by any single
  factor of the reduced form.

## 5. What this establishes

1. **Chart/physical separation is now exact.** In the reduced form,
   gap and D_other are physical invariants (mass-squared
   differences), while M and W are chart coordinates. The inheritance
   identity a₁/(D_uD_d) = |J|/sinφ factorizes as
   (chart M · chart W)/(physical gap · physical D_other).
2. **The cluster structure is a level-set structure.** Clusters are
   level sets of the physical combination |J|/sinφ; φ is pinned at
   every viable minimum (1937: zero trenches), and the cross-texture
   coincidence of φ within rigid clusters follows from the minima
   being the same physical point — consistent with the leading-order
   triangle identification (1903, 1921) making φ effectively a
   function of CKM data at viable minima.
3. **The π/8 question is located, not solved.** What remains
   empirical: WHICH level sets are realizable (which φ values admit
   χ²-viable fits at all), and why those cluster near π/8 multiples.
   Any future derivation must explain the realizable set of
   M·W/(gap·D_other) values, not the phase sector directly.
4. **W is the next exact object.** Its coefficients are always ±1 and
   it has ≤ 3 terms; it looks like a Plücker/cofactor form of the
   connected sector. An invariant identification of W (and thereby a
   closed form for a₁ in weak-basis invariants times chart data) is
   the natural WP22 question.

## 6. Boundaries

- The factorization is certified for the 755 textures present in the
  WP15b viable ensemble. A topology-general proof over ALL one-cycle
  nine-link graphs (in the sense of 1924's support theorem) is open;
  the census found zero counterexamples and the mechanism (block
  char poly dividing the bracket) is graph-theoretic, so a general
  proof is plausible but not claimed.
- W's evaluation at a minimum is chart data. Nothing here promotes
  M or W to weak-basis invariants; the separation in §5.1 is the
  point.
- Cluster archetypes (rigid/conspiracy) are a measured taxonomy of
  THIS ensemble, not a theorem about all ensembles.

## 7. Durable verification

- `research/flavor/checkers/wp21a_a1_symbolic.py` →
  `results/wp21a_a1_symbolic.json` (85/234 symbolic base case;
  B = −χ_b(s) at the singleton, numeric residual 0).
- `research/flavor/checkers/wp21c_a1_cancellation_census.py` (v2) →
  `results/wp21c_a1_cancellation_census.json` (471/755 absorbed;
  v1 bug disclosed in §3).
- `research/flavor/checkers/wp21e_universal_factorization.py` →
  `results/wp21e_universal_factorization.json` (755/755: 682 block21
  + 73 diagonal; Vandermonde identity exact 755/755; numeric max rel
  err 1.6e-13; W ∈ {1,2,3}-term ±1-forms).
- `research/flavor/checkers/wp21d2_factor_discreteness_full.py` →
  `results/wp21d2_factor_discreteness_full.json` (1210/1210 records,
  reduced form max rel err 4.8e-12; archetype table).
- Ledger sequence claim: seqclaim-7094050b1769f3f76db5a396 (value
  1947 from the shared marici-ledger-entry allocator).
