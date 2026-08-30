# H2LR typing packet (WP45)

Agent: `marici.Figueiredo`. Date: 2026-08-24.
Source: arXiv:2607.27315v1 (Arkani-Hamed, Figueiredo, Hall, Manzari).
Conventions: `research/flavor/flavor-nine-link-conventions.md`.
Evidence: `research/flavor/checkers/wp45_h2lr_typing.py`,
results in `research/flavor/results/wp45_h2lr_typing.json` (6/6 gates).
Depends on: WP7 (observables17 ensemble), WP11 (phi is chart data),
WP36/WP44 (magnitude anatomy and singlet-gap cancellation).

## Question under test

Does a source-derived package

  (F, K_flavor, O_flavor, <-,->_flavor)

descend through every equivalence class the flavor problem declares, so that
flavor is admitted as a fourth Marici sector - and if so, with what typing?

## The package tested

  carrier  F        = {(Yu, Yd)} / U(3)_Q x U(3)_u x U(3)_d  (physical quotient)
  lens     K        = sparse nine-link chart: 9 edge magnitudes + loop holonomy
  readout  O        = observables17 (6 masses, 6 |V_ij|, 3 UT angles, 2 ratios)
  pairing  <-,->    = the WP44 gap-cancelled law mapping chart data to the
                      physical constants:
                      C_anchor = (block gap) Dd (CKM monomial)
                                 / (scale^2 |Hd_02|^2 |Hd_12|)

## Equivalence classes and gate results

  G1 full U(3)^3 quotient (random Q_L, Q_u, Q_d):
     obs17 invariant, max 1.1e-10 per-coordinate relative. PASSED.
  G2 chart groupoid (diagonal rephasings + row/col permutations):
     max 6.7e-12 relative. PASSED.
  G3 fiber compatibility: every tested chart lands inside the experimental
     fiber; max pull 1.60 sigma. PASSED (gate < 5).
  G4 CP conjugation: masses/|V| identical, angles reflected, exact 0.0. PASSED.
  G5 pairing factorization: WP44 law re-verified on the Hd_01 = 0 family,
     n = 394 sheets, max 2.7e-11. PASSED.
  G6 lens coordinate vs readout: the loop phase phi (Yukawa-triangle angle)
     has ensemble std 19.86 deg while its readout image gamma has std
     0.13 deg - ratio 152.5. The lens coordinate varies two orders of
     magnitude more than its readout image. PASSED (gate > 5).

## Typing conclusions

1. The carrier is the physical quotient, NOT the nine-link graph (WP11).
   The nine-link textures are the lens: a sparse chart atlas on the quotient.
2. phi and the Yukawa triangle are internal lens coordinates. Their CKM
   image is readout. G6 certifies the split quantitatively: the lens
   coordinate is 150x more volatile than the readout it feeds.
3. The pairing is the WP44 law: exact chart algebra on the Hd_01 = 0 family,
   point values at the physical flavor point, no universal extension on the
   complement (WP44 G5 boundary).
4. The package descends through all declared equivalence classes
   (G1, G2, G4 exact; G3, G5, G6 certified). Flavor is admitted as a fourth
   Marici sector with this typing - carrier = quotient, lens = sparse chart
   atlas, readout = weak-basis invariants, pairing = gap-cancelled law.
5. What flavor does NOT supply: a fundamental role for the graph itself,
   a UV quantization law for phi (the pi/8 clustering lives at lens level,
   and after WP11/WP45 it cannot be read as physical without a pushforward
   through the invariant ring), or a strong-CP solution beyond the paper's
   assumptions.

## Numerical-methods note (durable)

Invariance gates must compare per-coordinate RELATIVE error, and masses must
come from a direct SVD of Y. Forming H = Y Y^dagger and calling eigh (as
observables17 does for physics purposes) has backward error eps ||H||, i.e.
~2e-6 relative on the lightest masses (yu ~ 7e-6 against yt ~ 1). That is a
float64 algorithm floor, not an invariance violation; it mimics a G1/G2
failure at the 3e-6 level if used naively. SVD of Y directly gives
eps sigma_max/sigma_min ~ 1e-11. The wp45 checker uses a local obs_precise
wrapper (SVD masses + observables17 mixing data) for the invariance gates
only; the physics readout elsewhere is unaffected.
