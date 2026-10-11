{-# OPTIONS --safe --cubical --guardedness #-}
module TickAtanCompletionSlope where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as N using (ℕ; zero; suc)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.HITs.PropositionalTruncation as PT
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate using (one-half; PreferredℚCommRing)
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyProductBounds
open import CauchyProductErrorBounds using (weaken-magnitude-bound)
open import CauchyAdditionCongruence using (_+completion_)
open import CauchyNegation using (-completion_)
open import CauchyCompletionMultiplication using (preferredCompletionMultiplication)
open import TickCompletionLimits
open import TickCompletionMagnitudeBounds
open import TickRationalProductLimits
open import TickSmallArctangent
open import TickAtanDerivativeAlgebra using (geometricSum)
open import TickAtanFirstOrderBounds
open import TickAtanGeometricCompletion
open import TickAtanCompletionFirstOrder

atanSlope : (x : Q.ℚ) → MagnitudeBound x one-half → MetricCompletionCandidate
atanSlope = geometricValue

atanSlopeRemainder : (x y : Q.ℚ) → MagnitudeBound x one-half → MagnitudeBound y one-half → MetricCompletionCandidate
atanSlopeRemainder x y hx hy = atanIncrement x y hx hy +completion
  (-completion (preferredCompletionMultiplication (embedMetricℚ (y Q.+ (Q.- x))) (atanSlope x hx)))

slope-remainder-converges : (x y : Q.ℚ) (hx : MagnitudeBound x one-half) (hy : MagnitudeBound y one-half) →
  Converges (λ n → embedMetricℚ (partialRemainder x y n)) (atanSlopeRemainder x y hx hy)
slope-remainder-converges x y hx hy = rational-sum-sequence-converges
  (λ n → atanPartialSum y n Q.+ (Q.- atanPartialSum x n))
  (λ n → Q.- ((y Q.+ (Q.- x)) Q.· geometricSum x n))
  (atanIncrement x y hx hy)
  (-completion (preferredCompletionMultiplication (embedMetricℚ (y Q.+ (Q.- x))) (atanSlope x hx)))
  (rational-sum-sequence-converges (atanPartialSum y) (λ n → Q.- atanPartialSum x n)
    (atanCompletion y hy) (-completion (atanCompletion x hx))
    (atan-completion-converges y hy)
    (rational-negative-sequence-converges (atanPartialSum x) (atanCompletion x hx) (atan-completion-converges x hx)))
  (rational-negative-sequence-converges (λ n → (y Q.+ (Q.- x)) Q.· geometricSum x n)
    (preferredCompletionMultiplication (embedMetricℚ (y Q.+ (Q.- x))) (atanSlope x hx))
    (rational-product-sequence-converges (y Q.+ (Q.- x)) (geometricSum x) (atanSlope x hx)
      (geometric-sequence-converges x hx)))

-- A denominator-free completion estimate, with the constructed inverse of
-- 1+x² as slope. Still restricted to rational inputs in the small interval.
abstract
  atan-slope-completion-bound : (x y e : Q.ℚ) (hx : MagnitudeBound x one-half) (hy : MagnitudeBound y one-half) →
    0 ≤ e → MagnitudeBound (y Q.+ (Q.- x)) e →
    CompletionMagnitudeBound (atanSlopeRemainder x y hx hy) (scale e Q.+ scale e)
  atan-slope-completion-bound x y e hx hy eh dh = rational-limit-magnitude
    (partialRemainder x y) (atanSlopeRemainder x y hx hy) (scale e Q.+ scale e)
    (slope-remainder-converges x y hx hy)
    (λ k → ∣ zero , (λ n hn → weaken-magnitude-bound (partialRemainder x y n)
      (scale e Q.+ scale e) ((scale e Q.+ scale e) Q.+ precision k)
      (≤-add-nonnegative (scale e Q.+ scale e) (precision k) (precision-nonnegative k))
      (partial-remainder-bound x y e hx hy eh dh n)) ∣₁)

atan-slope-inverse : (x : Q.ℚ) (hx : MagnitudeBound x one-half) →
  preferredCompletionMultiplication (embedMetricℚ (1 Q.+ x Q.· x)) (atanSlope x hx) ≡ embedMetricℚ 1
atan-slope-inverse = geometric-completion-inverse

module Paths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_·_ to _·S_; -_ to -S_)
  zero-step : (a r : fst R) → -S (((a ·S 0r) ·S 0r) ·S r) ≡ 0r
  zero-step a r = solve! R

abstract
  atan-term-zero : (n : ℕ) → atanTerm 0 n ≡ 0
  atan-term-zero zero = refl
  atan-term-zero (suc n) = Paths.zero-step PreferredℚCommRing (atanTerm 0 n) _

  atan-partial-zero : (n : ℕ) → atanPartialSum 0 n ≡ 0
  atan-partial-zero zero = refl
  atan-partial-zero (suc n) = cong₂ Q._+_ (atan-partial-zero n) (atan-term-zero (suc n)) ∙ Q.+IdL 0

-- Fixes the initial value required for a future uniqueness argument.
atan-completion-zero : (h : MagnitudeBound 0 one-half) → atanCompletion 0 h ≡ embedMetricℚ 0
atan-completion-zero h = convergent-limits-equal (λ n → embedMetricℚ (atanPartialSum 0 n))
  (atanCompletion 0 h) (embedMetricℚ 0) (atan-completion-converges 0 h)
  (converges-pointwise-path (λ _ → embedMetricℚ 0) (λ n → embedMetricℚ (atanPartialSum 0 n)) (embedMetricℚ 0)
    (λ n → cong embedMetricℚ (sym (atan-partial-zero n))) (constant-converges (embedMetricℚ 0)))
