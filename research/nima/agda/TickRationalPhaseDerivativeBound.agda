{-# OPTIONS --safe --cubical --guardedness #-}
module TickRationalPhaseDerivativeBound where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (zero)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.HITs.PropositionalTruncation as PT
open import RationalAnalyticSubstrate using (one-half)
open import RegularCauchyStructure using (precision; precision-nonnegative; ≤-add-nonnegative)
open import CauchyMetricEquivalence
open import CauchyProductBounds
open import CauchyAdditionCongruence using (_+completion_)
open import CauchyCompletionMultiplication using (preferredCompletionMultiplication)
open import ConstructiveComplexCompletion
open import RationalTaylorApproximants
open import RationalSineTaylorApproximants
open import TickCompletionDerivative
open import TickCompletionLimits
open import TickRationalProductLimits
open import TickCompletionOrderLimits
open import TickOperationalTrigFirstOrder using
  (cosineValue; sineValue; cosine-value-converges; sine-value-converges)
open import TickTrigRelativeRemainder

-- These values are the implemented trigonometric functions at embed(q),
-- identified by cosine-value-class / sine-value-class in FirstOrder.
rationalOperationalRemainder : Q.ℚ → ComplexCompletion
rationalOperationalRemainder q = complex
  (cosineValue q +completion embedMetricℚ (Q.- 1))
  (sineValue q +completion embedMetricℚ (Q.- q))

abstract
  cosine-residual-converges : (q : Q.ℚ) →
    Converges (λ n → embedMetricℚ (cosineResidual q n))
      (cosineValue q +completion embedMetricℚ (Q.- 1))
  cosine-residual-converges q = rational-sum-sequence-converges
    (cosinePartialSum q) (λ _ → Q.- 1) (cosineValue q) (embedMetricℚ (Q.- 1))
    (cosine-value-converges q) (constant-converges (embedMetricℚ (Q.- 1)))

  sine-residual-converges : (q : Q.ℚ) →
    Converges (λ n → embedMetricℚ (sineResidual q n))
      (sineValue q +completion embedMetricℚ (Q.- q))
  sine-residual-converges q = rational-sum-sequence-converges
    (sinePartialSum q) (λ _ → Q.- q) (sineValue q) (embedMetricℚ (Q.- q))
    (sine-value-converges q) (constant-converges (embedMetricℚ (Q.- q)))

  -- The relative rational estimate is now constructed, not an assumed
  -- all-cutoff bound. Only explicit scalar/radius budget hypotheses remain.
  rational-operational-relative-bound : (p h P d e : Q.ℚ) → 0 ≤ P → 0 ≤ d →
    MagnitudeBound p P → MagnitudeBound h d → MagnitudeBound (Q.- (p Q.· h)) one-half →
    squareℚ (squareℚ P) Q.· (squareℚ d Q.+ squareℚ d) ≤ squareℚ e →
    CompletionLE (complexNormSquared (rationalOperationalRemainder (Q.- (p Q.· h))))
      (preferredCompletionMultiplication (embedMetricℚ (squareℚ e)) (squareCompletion (embedMetricℚ h)))
  rational-operational-relative-bound p h P d e Ppositive dpositive pbound hbound small budget =
    rational-quadratic-bound-limit (cosineResidual q) (sineResidual q) (λ _ → h)
      (cosineValue q +completion embedMetricℚ (Q.- 1))
      (sineValue q +completion embedMetricℚ (Q.- q)) (embedMetricℚ h) e
      (cosine-residual-converges q) (sine-residual-converges q) (constant-converges (embedMetricℚ h))
      (λ k → ∣ zero , (λ n _ → isTrans≤
        (squareℚ (cosineResidual q n) Q.+ squareℚ (sineResidual q n))
        (squareℚ e Q.· squareℚ h) ((squareℚ e Q.· squareℚ h) Q.+ precision k)
        (scaled-relative-residual-bound p h P d e Ppositive dpositive pbound hbound small budget n n)
        (≤-add-nonnegative (squareℚ e Q.· squareℚ h) (precision k) (precision-nonnegative k))) ∣₁)
    where
    q : Q.ℚ
    q = Q.- (p Q.· h)
