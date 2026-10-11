{-# OPTIONS --safe --cubical --guardedness #-}
module TickCayleyDyadicMesh where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as N using (ℕ; zero; suc)
import Cubical.Data.Nat.Order as NO
open import Cubical.Data.NatPlusOne using (1+_)
import Cubical.Data.NatPlusOne.Properties
import Cubical.Data.Int as Z
import Cubical.Data.Int.Order as ZO
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import Cubical.Tactics.NatSolver using (solveℕ!)
open import RationalAnalyticSubstrate using (PreferredℚCommRing; one-half)
open import RegularCauchyStructure using (precision; precision-nonnegative; precision-antitone; ≤-add-nonnegative)
open import DyadicallyBoundedCauchy using (natℚ; natℚ-representative; natℚ-add; dyadicNat; natℚ-dyadicNat; dyadicRadius-times-precision)
open import CauchyProductBounds
open import TaylorTermBounds using (nonnegative-bound-product; nonnegative-value-magnitude)
open import TickAtanDerivativeAlgebra using (positive-product; positive-fractions-equal)
open import TickCayleyGridIncrement using (gridValue; grid-value-nonnegative)

meshDenominator : ℕ → ℕ → ℕ
meshDenominator zero d = d
meshDenominator (suc n) d = suc (meshDenominator n d N.+ meshDenominator n d)

meshPoint : ℕ → ℕ → ℕ → ℕ → Q.ℚ
meshPoint N d n j = gridValue (j N.· N) (meshDenominator n d)

module Algebra {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; _·_ to _·S_; -_ to -S_)
  half-reorder : (j q p h : fst R) → ((j ·S q) ·S p) ·S h ≡ (j ·S q) ·S (p ·S h)
  half-reorder j q p h = solve! R
  endpoint : (j q p : fst R) → (j ·S q) ·S p ≡ q ·S (j ·S p)
  endpoint j q p = solve! R
  step : (j q p : fst R) → ((j +S 1r) ·S q) ·S p +S (-S ((j ·S q) ·S p)) ≡ q ·S p
  step j q p = solve! R
module R = Algebra PreferredℚCommRing

abstract
  halving-numerator : (a d : ℕ) → (a N.· suc zero) N.· suc (suc (d N.+ d)) ≡ a N.· suc (suc (d N.· suc (suc zero)))
  halving-numerator a d = solveℕ!

  unit-denominator : (a d : ℕ) → a N.· suc d ≡ a N.· suc (d N.+ zero)
  unit-denominator a d = solveℕ!

  grid-halving : (a d : ℕ) → gridValue a (suc (d N.+ d)) ≡ gridValue a d Q.· one-half
  grid-halving a d = sym (positive-product a 1 (1+ d) (1+ 1)
    ∙ positive-fractions-equal (a N.· 1) a ((1+ d) Cubical.Data.NatPlusOne.Properties.·₊₁ (1+ 1)) (1+ suc (d N.+ d)) (halving-numerator a d))

  mesh-formula : (N d n j : ℕ) → meshPoint N d n j ≡ (natℚ j Q.· gridValue N d) Q.· precision n
  mesh-formula N d zero j = sym (cong (Q._· gridValue N d) (natℚ-representative j)
    ∙ positive-product j N (1+ 0) (1+ d)
    ∙ positive-fractions-equal (j N.· N) (j N.· N) ((1+ 0) Cubical.Data.NatPlusOne.Properties.·₊₁ (1+ d)) (1+ d) (unit-denominator (j N.· N) d))
    ∙ sym (Q.·IdR (natℚ j Q.· gridValue N d))
  mesh-formula N d (suc n) j = grid-halving (j N.· N) (meshDenominator n d)
    ∙ cong (Q._· one-half) (mesh-formula N d n j) ∙ R.half-reorder (natℚ j) (gridValue N d) (precision n) one-half

  mesh-first : (N d n : ℕ) → meshPoint N d n zero ≡ 0
  mesh-first N d n = mesh-formula N d n zero
    ∙ cong (Q._· precision n) (Q.·AnnihilL (gridValue N d)) ∙ Q.·AnnihilL (precision n)

  mesh-last : (N d n : ℕ) → meshPoint N d n (dyadicNat n) ≡ gridValue N d
  mesh-last N d n = mesh-formula N d n (dyadicNat n) ∙ R.endpoint (natℚ (dyadicNat n)) (gridValue N d) (precision n)
    ∙ cong (gridValue N d Q.·_) (cong (Q._· precision n) (natℚ-dyadicNat n) ∙ dyadicRadius-times-precision n)
    ∙ Q.·IdR (gridValue N d)

  mesh-step : (N d n j : ℕ) → meshPoint N d n (suc j) Q.+ (Q.- meshPoint N d n j) ≡ gridValue N d Q.· precision n
  mesh-step N d n j = cong₂ Q._+_ (mesh-formula N d n (suc j)) (cong Q.-_ (mesh-formula N d n j))
    ∙ R.step (natℚ j) (gridValue N d) (precision n)

  nat-rational-nonnegative : (j : ℕ) → 0 ≤ natℚ j
  nat-rational-nonnegative j = subst (0 ≤_) (sym (natℚ-representative j)) (grid-value-nonnegative j 0)

  nat-rational-monotone : (j k : ℕ) → NO._≤_ j k → natℚ j ≤ natℚ k
  nat-rational-monotone j k (l , path) = subst (natℚ j ≤_) (sym (natℚ-add l j) ∙ cong natℚ path)
    (subst (natℚ j ≤_) (Q.+Comm (natℚ j) (natℚ l)) (≤-add-nonnegative (natℚ j) (natℚ l) (nat-rational-nonnegative l)))

  mesh≤endpoint : (N d n j : ℕ) → NO._≤_ j (dyadicNat n) → meshPoint N d n j ≤ gridValue N d
  mesh≤endpoint N d n j hj = subst2 _≤_ (sym (mesh-formula N d n j)) (sym (mesh-formula N d n (dyadicNat n)) ∙ mesh-last N d n)
    (≤-·o (natℚ j Q.· gridValue N d) (natℚ (dyadicNat n) Q.· gridValue N d) (precision n) (precision-nonnegative n)
      (≤-·o (natℚ j) (natℚ (dyadicNat n)) (gridValue N d) (grid-value-nonnegative N d) (nat-rational-monotone j (dyadicNat n) hj)))

  mesh-small : (N d : ℕ) → MagnitudeBound (gridValue N d) one-half → (n j : ℕ) → NO._≤_ j (dyadicNat n) →
    MagnitudeBound (meshPoint N d n j) one-half
  mesh-small N d h n j hj = nonnegative-value-magnitude (meshPoint N d n j) one-half
    (grid-value-nonnegative (j N.· N) (meshDenominator n d))
    (isTrans≤ (meshPoint N d n j) (gridValue N d) one-half (mesh≤endpoint N d n j hj) (positive-upper h)) (precision-nonnegative 1)

  mesh-step-bound : (N d : ℕ) → MagnitudeBound (gridValue N d) one-half → (n j : ℕ) →
    MagnitudeBound (meshPoint N d n (suc j) Q.+ (Q.- meshPoint N d n j)) (precision n)
  mesh-step-bound N d h n j = subst (λ q → MagnitudeBound q (precision n)) (sym (mesh-step N d n j))
    (nonnegative-value-magnitude (gridValue N d Q.· precision n) (precision n)
      (nonnegative-bound-product (gridValue N d) (precision n) (grid-value-nonnegative N d) (precision-nonnegative n))
      (subst (_≤ precision n) (Q.·Comm (precision n) (gridValue N d))
        (subst ((precision n Q.· gridValue N d) ≤_) (Q.·IdR (precision n))
          (left-multiply-monotone (precision n) (gridValue N d) 1 (precision-nonnegative n)
            (isTrans≤ (gridValue N d) one-half 1 (positive-upper h) (1 , refl))))) (precision-nonnegative n))
