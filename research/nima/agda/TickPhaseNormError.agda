{-# OPTIONS --safe --cubical --guardedness #-}
module TickPhaseNormError where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate
open import CauchyProductBounds

module Identity {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; _·_ to _·S_; -_ to -S_)
  norm-error : (a b c d : fst R) →
    ((a ·S a) +S (b ·S b)) +S (-S 1r) ≡
    (((a +S (-S c)) ·S (a +S c)) +S ((b +S (-S d)) ·S (b +S d))) +S
    (((c ·S c) +S (d ·S d)) +S (-S 1r))
  norm-error a b c d = solve! R

-- a,b: actual scheduled samples; c,d: common-input Taylor controls.
-- The output retains an explicit rational budget, avoiding analytic axioms.
norm-error-bound : (a b c d M ε δ : Q.ℚ) →
  0 ≤ M → 0 ≤ ε →
  MagnitudeBound a M → MagnitudeBound b M →
  MagnitudeBound c M → MagnitudeBound d M →
  MagnitudeBound (a Q.+ (Q.- c)) ε →
  MagnitudeBound (b Q.+ (Q.- d)) ε →
  MagnitudeBound (((c Q.· c) Q.+ (d Q.· d)) Q.+ (Q.- 1)) δ →
  MagnitudeBound (((a Q.· a) Q.+ (b Q.· b)) Q.+ (Q.- 1))
    (((ε Q.· (M Q.+ M)) Q.+ (ε Q.· (M Q.+ M))) Q.+ δ)
norm-error-bound a b c d M ε δ M≥0 ε≥0 aBound bBound cBound dBound ac bd residual =
  transport-magnitude _ _ _ (Identity.norm-error PreferredℚCommRing a b c d)
    (add-magnitude-bounds _ _ _ _
      (add-magnitude-bounds _ _ _ _
        (arbitrary-multiplier-bound _ ε _ (M Q.+ M)
          ε≥0 (subst (λ z → z ≤ M Q.+ M) (Q.+IdL 0) (≤Monotone+ 0 M 0 M M≥0 M≥0))
          ac (add-magnitude-bounds a M c M aBound cBound))
        (arbitrary-multiplier-bound _ ε _ (M Q.+ M)
          ε≥0 (subst (λ z → z ≤ M Q.+ M) (Q.+IdL 0) (≤Monotone+ 0 M 0 M M≥0 M≥0))
          bd (add-magnitude-bounds b M d M bBound dBound)))
      residual)
