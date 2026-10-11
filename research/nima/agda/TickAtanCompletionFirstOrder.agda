{-# OPTIONS --safe --cubical --guardedness #-}
module TickAtanCompletionFirstOrder where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as N using (ℕ)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.HITs.PropositionalTruncation as PT
open import RationalAnalyticSubstrate using (one-half)
open import CauchyMetricEquivalence
open import CauchyProductBounds
open import CauchyAdditionCongruence using (_+completion_)
open import CauchyNegation using (-completion_)
open import CauchyCompletionMultiplication using (preferredCompletionMultiplication)
open import TickCompletionLimits
open import TickRationalProductLimits
open import TickCompletionMagnitudeBounds
open import TickSmallArctangent
open import TickAtanFirstOrderBounds
open import TickAtanGeometricCompletion using (atan-sequence-converges)

-- Opaque presentation of the existing arctangent class, not a new backend.
abstract
  atanCompletion : (q : Q.ℚ) → MagnitudeBound q one-half → MetricCompletionCandidate
  atanCompletion = smallAtanValue

  atan-completion-class : (q : Q.ℚ) (h : MagnitudeBound q one-half) →
    atanCompletion q h ≡ smallAtanValue q h
  atan-completion-class q h = refl

  atan-completion-converges : (q : Q.ℚ) (h : MagnitudeBound q one-half) →
    Converges (λ n → embedMetricℚ (atanPartialSum q n)) (atanCompletion q h)
  atan-completion-converges = atan-sequence-converges

atanIncrement : (x y : Q.ℚ) → MagnitudeBound x one-half → MagnitudeBound y one-half → MetricCompletionCandidate
atanIncrement x y hx hy = atanCompletion y hy +completion (-completion (atanCompletion x hx))

clearedAtanRemainder : (x y : Q.ℚ) → MagnitudeBound x one-half → MagnitudeBound y one-half → MetricCompletionCandidate
clearedAtanRemainder x y hx hy =
  preferredCompletionMultiplication (embedMetricℚ (1 Q.+ x Q.· x)) (atanIncrement x y hx hy)
    +completion embedMetricℚ (Q.- (y Q.+ (Q.- x)))

-- These finite remainder approximants converge under the actual independently
-- scheduled completion operations. No same-cutoff multiplication is assumed.
cleared-remainder-converges : (x y : Q.ℚ) (hx : MagnitudeBound x one-half) (hy : MagnitudeBound y one-half) →
  Converges (λ n → embedMetricℚ (clearedRemainder x y n)) (clearedAtanRemainder x y hx hy)
cleared-remainder-converges x y hx hy = rational-sum-sequence-converges
  (λ n → (1 Q.+ x Q.· x) Q.· (atanPartialSum y n Q.+ (Q.- atanPartialSum x n)))
  (λ _ → Q.- (y Q.+ (Q.- x)))
  (preferredCompletionMultiplication (embedMetricℚ (1 Q.+ x Q.· x)) (atanIncrement x y hx hy))
  (embedMetricℚ (Q.- (y Q.+ (Q.- x))))
  (rational-product-sequence-converges (1 Q.+ x Q.· x)
    (λ n → atanPartialSum y n Q.+ (Q.- atanPartialSum x n)) (atanIncrement x y hx hy)
    (rational-sum-sequence-converges (atanPartialSum y) (λ n → Q.- atanPartialSum x n)
      (atanCompletion y hy) (-completion (atanCompletion x hx))
      (atan-completion-converges y hy)
      (rational-negative-sequence-converges (atanPartialSum x) (atanCompletion x hx) (atan-completion-converges x hx))))
  (constant-converges (embedMetricℚ (Q.- (y Q.+ (Q.- x)))))

-- Completion-level first-order estimate on small rational inputs, with a
-- quadratic bound independent of the cutoff. This is not yet a derivative
-- theorem on all completion-valued increments or a trigonometric Cayley law.
cleared-atan-completion-bound : (x y e : Q.ℚ) (hx : MagnitudeBound x one-half) (hy : MagnitudeBound y one-half) →
  0 ≤ e → MagnitudeBound (y Q.+ (Q.- x)) e →
  CompletionMagnitudeBound (clearedAtanRemainder x y hx hy) (quadraticBudget e)
cleared-atan-completion-bound x y e hx hy eh dh = rational-limit-magnitude
  (clearedRemainder x y) (clearedAtanRemainder x y hx hy) (quadraticBudget e)
  (cleared-remainder-converges x y hx hy)
  (λ k → ∣ errorOffset e N.+ k , (λ n hn → cleared-remainder-all-later x y e hx hy eh dh k n hn) ∣₁)
