{-# OPTIONS --safe --cubical --guardedness #-}
module TickCayleyQuadraticBudgets where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Data.Sigma using (_×_)
import Cubical.Data.Int.Order as ZO
open import Cubical.Tactics.CommRingSolver
open import Cubical.Algebra.CommRing
open import TickAtanFirstOrderBounds using (eight)
open import RationalAnalyticSubstrate using (one-half; one-half-double)
open import RationalAnalyticSubstrate using (PreferredℚCommRing)
open import RegularCauchyStructure
open import CauchyProductBounds
open import TaylorTermBounds using (nonnegative-value-magnitude)
open import TickCayleyRotationalBracket using (realGridBudget; imaginaryGridBudget)

module BudgetAlgebra {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; _·_ to _·S_)
  two = 1r +S 1r
  four = two +S two
  sixteen = four ·S four
  real-factor : (e : fst R) →
    (1r +S e ·S e) ·S ((e +S e +S (e +S e)) ·S (e +S e +S (e +S e))) +S (e ·S e +S e ·S e) ≡
    (sixteen ·S (1r +S e ·S e) +S two) ·S (e ·S e)
  real-factor e = solve! R
  imaginary-factor : (c h e : fst R) →
    ((1r +S e ·S e) ·S ((e +S e +S (e +S e)) ·S (e +S e +S (e +S e))) +S
      (1r +S e ·S e) ·S (((c ·S (e ·S e) +S c ·S (e ·S e)) +S h ·S (e ·S e)) +S
        ((c ·S (e ·S e) +S c ·S (e ·S e)) +S h ·S (e ·S e)))) +S ((e +S e) ·S (e ·S e)) ≡
    (((sixteen +S four ·S c +S (h +S h)) ·S (1r +S e ·S e)) +S (e +S e)) ·S (e ·S e)
  imaginary-factor c h e = solve! R
module BA = BudgetAlgebra PreferredℚCommRing

abstract
  sixteen-normalizes : BA.sixteen ≡ 16
  sixteen-normalizes = Q.eq/ _ _ refl
  fortyNine-normalizes : (BA.sixteen Q.+ BA.four Q.· eight) Q.+ 1 ≡ 49
  fortyNine-normalizes = Q.eq/ _ _ refl

  real-budget-factor : (e : Q.ℚ) → realGridBudget e ≡ ((16 Q.· (1 Q.+ e Q.· e)) Q.+ 2) Q.· (e Q.· e)
  real-budget-factor e = BA.real-factor e
    ∙ cong (λ c → ((c Q.· (1 Q.+ e Q.· e)) Q.+ 2) Q.· (e Q.· e)) sixteen-normalizes

  imaginary-budget-factor : (e : Q.ℚ) → imaginaryGridBudget e ≡ ((49 Q.· (1 Q.+ e Q.· e)) Q.+ (e Q.+ e)) Q.· (e Q.· e)
  imaginary-budget-factor e = BA.imaginary-factor eight one-half e
    ∙ cong (λ h → ((((BA.sixteen Q.+ BA.four Q.· eight) Q.+ h) Q.· (1 Q.+ e Q.· e)) Q.+ (e Q.+ e)) Q.· (e Q.· e)) one-half-double
    ∙ cong (λ c → ((c Q.· (1 Q.+ e Q.· e)) Q.+ (e Q.+ e)) Q.· (e Q.· e)) fortyNine-normalizes

  grid-budget-domination : (e : Q.ℚ) → 0 ≤ e → e ≤ precision 6 →
    (realGridBudget e ≤ 34 Q.· (e Q.· e)) × (imaginaryGridBudget e ≤ 99 Q.· (e Q.· e))
  grid-budget-domination e eh small =
    subst (_≤ 34 Q.· (e Q.· e)) (sym (real-budget-factor e))
      (≤-·o ((16 Q.· (1 Q.+ e Q.· e)) Q.+ 2) 34 (e Q.· e) square≥0
        (≤Monotone+ (16 Q.· (1 Q.+ e Q.· e)) (16 Q.· 2) 2 2
          (left-multiply-monotone 16 (1 Q.+ e Q.· e) 2 sixteen≥0 denominator≤two) (isRefl≤ 2))) ,
    subst (_≤ 99 Q.· (e Q.· e)) (sym (imaginary-budget-factor e))
      (≤-·o ((49 Q.· (1 Q.+ e Q.· e)) Q.+ (e Q.+ e)) 99 (e Q.· e) square≥0
        (≤Monotone+ (49 Q.· (1 Q.+ e Q.· e)) (49 Q.· 2) (e Q.+ e) 1
          (left-multiply-monotone 49 (1 Q.+ e Q.· e) 2 fortyNine≥0 denominator≤two) doubled≤one))
    where
    sixteen≥0 : 0 ≤ 16
    sixteen≥0 = ZO.zero-≤pos
    fortyNine≥0 : 0 ≤ 49
    fortyNine≥0 = ZO.zero-≤pos
    e≤one : e ≤ 1
    e≤one = isTrans≤ e (precision 6) 1 small (precision-antitone 0 6 (6 , refl))
    e-bound : MagnitudeBound e 1
    e-bound = nonnegative-value-magnitude e 1 eh e≤one (precision-nonnegative 0)
    square-bound : MagnitudeBound (e Q.· e) 1
    square-bound = subst (MagnitudeBound (e Q.· e)) (Q.·IdR 1)
      (arbitrary-multiplier-bound e 1 e 1 (precision-nonnegative 0) (precision-nonnegative 0) e-bound e-bound)
    square≥0 : 0 ≤ e Q.· e
    square≥0 = TaylorTermBounds.nonnegative-bound-product e e eh eh
    denominator≤two : 1 Q.+ e Q.· e ≤ 2
    denominator≤two = ≤Monotone+ 1 1 (e Q.· e) 1 (isRefl≤ 1) (positive-upper square-bound)
    e≤half : e ≤ precision 1
    e≤half = isTrans≤ e (precision 6) (precision 1) small (precision-antitone 1 6 (5 , refl))
    doubled≤one : e Q.+ e ≤ 1
    doubled≤one = subst ((e Q.+ e) ≤_) (precision-refines-double 0)
      (≤Monotone+ e (precision 1) e (precision 1) e≤half e≤half)
