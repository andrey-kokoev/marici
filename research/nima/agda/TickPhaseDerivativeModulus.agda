{-# OPTIONS --safe --cubical --guardedness #-}
module TickPhaseDerivativeModulus where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as Nat using (ℕ; suc)
import Cubical.Data.Nat.Order as N
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate using (PreferredℚCommRing; one-half)
open import RegularCauchyStructure
open import DyadicallyBoundedCauchy
open import TickTrigRelativeRemainder using (squareℚ)

module Algebra {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; _·_ to _·S_)
  regroup-budget : (P d : fst R) → ((P ·S P) ·S (P ·S P)) ·S ((d ·S d) +S (d ·S d)) ≡
    ((P ·S (P ·S d)) ·S (P ·S (P ·S d))) +S ((P ·S (P ·S d)) ·S (P ·S (P ·S d)))
  regroup-budget P d = solve! R
  two-squares : (a : fst R) → (a ·S a) +S (a ·S a) ≡ a ·S (a +S a)
  two-squares a = solve! R
module R = Algebra PreferredℚCommRing

-- P=2^d, delta=2^-(2d+k+1). Two further bits are reserved for
-- arbitrary-representative comparison when extracting the completion ball.
residualDepth : ℕ → ℕ → ℕ
residualDepth d k = d Nat.+ (d Nat.+ suc k)

derivativeDepth : ℕ → ℕ → ℕ
derivativeDepth d k = suc (suc (residualDepth d k))

abstract
  modulus-small-angle : (d k : ℕ) → dyadicRadius d Q.· precision (residualDepth d k) ≤ one-half
  modulus-small-angle d k = subst (_≤ one-half) (sym (radius-cancels-precision-shift d (d Nat.+ suc k)))
    (precision-antitone 1 (d Nat.+ suc k) (N.≤-trans (N.suc-≤-suc N.zero-≤) N.≤SumRight))

  modulus-double-cancellation : (d k : ℕ) →
    dyadicRadius d Q.· (dyadicRadius d Q.· precision (residualDepth d k)) ≡ precision (suc k)
  modulus-double-cancellation d k =
    cong (dyadicRadius d Q.·_) (radius-cancels-precision-shift d (d Nat.+ suc k))
    ∙ radius-cancels-precision-shift d (suc k)

  modulus-quadratic-budget : (d k : ℕ) →
    squareℚ (squareℚ (dyadicRadius d)) Q.·
      (squareℚ (precision (residualDepth d k)) Q.+ squareℚ (precision (residualDepth d k))) ≤
    squareℚ (precision k)
  modulus-quadratic-budget d k = subst (_≤ squareℚ (precision k)) (sym budget-path)
    (≤-·o (precision (suc k)) (precision k) (precision k) (precision-nonnegative k)
      (precision-antitone k (suc k) N.≤-sucℕ))
    where
    budget-path : squareℚ (squareℚ (dyadicRadius d)) Q.·
      (squareℚ (precision (residualDepth d k)) Q.+ squareℚ (precision (residualDepth d k))) ≡
      precision (suc k) Q.· precision k
    budget-path = R.regroup-budget (dyadicRadius d) (precision (residualDepth d k))
      ∙ cong (λ a → squareℚ a Q.+ squareℚ a) (modulus-double-cancellation d k)
      ∙ R.two-squares (precision (suc k))
      ∙ cong (precision (suc k) Q.·_) (precision-refines-double k)
