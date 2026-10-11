{-# OPTIONS --safe --cubical --guardedness #-}
module TickAtanOuterAngleBound where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ; zero)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import Cubical.HITs.PropositionalTruncation using (∣_∣₁)
open import RationalAnalyticSubstrate using (PreferredℚCommRing; one-half)
open import RegularCauchyStructure using (precision; precision-nonnegative; ≤-add-nonnegative)
open import CauchyMetricEquivalence
open import CauchyProductBounds
open import CauchyAdditionCongruence using (_+completion_)
open import TickCompletionMagnitudeBounds
open import TickAtanCompletionFirstOrder using (atanCompletion; atan-completion-converges)
open import TickSmallArctangent using (atanPartialSum; atan-segment-bound)
open import TickOperationalRotorIncrement using (gridAngle)
open import TickCayleyGridIncrement using (gridValue)
import AbsoluteTaylorSeriesMultiplication as A

module Algebra {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; -_ to -S_)
  restore : (a b : fst R) → (a +S (-S b)) +S b ≡ a
  restore a b = solve! R

abstract
  atan-partial-uniform-bound : (q : Q.ℚ) (h : MagnitudeBound q one-half) (n : ℕ) → MagnitudeBound (atanPartialSum q n) 2
  atan-partial-uniform-bound q h n = A.weakenMagnitudeBound (atanPartialSum q n) (1 Q.+ one-half) 2
    (subst (λ a → MagnitudeBound a (1 Q.+ one-half))
      (Algebra.restore PreferredℚCommRing (atanPartialSum q n) q)
      (add-magnitude-bounds (atanPartialSum q n Q.+ (Q.- q)) 1 q one-half (atan-segment-bound q h zero n) h))
    (1 , refl)

  atan-uniform-bound : (q : Q.ℚ) (h : MagnitudeBound q one-half) → CompletionMagnitudeBound (atanCompletion q h) 2
  atan-uniform-bound q h = rational-limit-magnitude (atanPartialSum q) (atanCompletion q h) 2
    (atan-completion-converges q h)
    (λ k → ∣ zero , (λ n hn → A.weakenMagnitudeBound (atanPartialSum q n) 2 (2 Q.+ precision k)
      (atan-partial-uniform-bound q h n) (≤-add-nonnegative 2 (precision k) (precision-nonnegative k))) ∣₁)

  grid-angle-uniform-bound : (n d : ℕ) (h : MagnitudeBound (gridValue n d) one-half) →
    CompletionMagnitudeBound (gridAngle n d h) 4
  grid-angle-uniform-bound n d h = completion-magnitude-add
    (atanCompletion (gridValue n d) h) (atanCompletion (gridValue n d) h) 2 2
    (atan-uniform-bound (gridValue n d) h) (atan-uniform-bound (gridValue n d) h)
