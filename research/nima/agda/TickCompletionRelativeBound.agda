{-# OPTIONS --safe --cubical --guardedness #-}
module TickCompletionRelativeBound where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ; suc)
import Cubical.HITs.SetQuotients as SQ
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import RationalAnalyticSubstrate using (one-half)
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyProductBounds
open import CauchyProductErrorBounds using (weaken-magnitude-bound)
open import CauchyAdditionCongruence using (_+completion_)
open import CauchyNegation using (-completion_)
open import CauchyCompletionMultiplication using (preferredCompletionMultiplication)
open import ConstructiveComplexCompletion
open import TickCompletionDerivative
open import TickCompletionLimits
open import TickCompletionRingContinuity
open import TickRationalProductLimits
open import TickCompletionOrderLimits
open import TickCompletionClosedOrder
open import TickCompletionTrigSmallAngle
open import TickOperationalTrigFirstOrder using (cosineValue; sineValue)
open import TickTrigRelativeRemainder
open import TickRationalPhaseDerivativeBound

localResidualNorm : MetricCompletionCandidate → MetricCompletionCandidate → MetricCompletionCandidate
localResidualNorm p h = complexNormSquared (complex
  (cosineRemainder (-completion (preferredCompletionMultiplication p h)))
  (sineRemainder (-completion (preferredCompletionMultiplication p h))))

abstract
  square-limit : (u : ℕ → MetricCompletionCandidate) (a : MetricCompletionCandidate) →
    Converges u a → Converges (λ n → squareCompletion (u n)) (squareCompletion a)
  square-limit u a hu = joint-continuous-limit preferredCompletionMultiplication multiplication-joint-continuous u u a a hu hu

  norm-limit : (u v : ℕ → MetricCompletionCandidate) (a b : MetricCompletionCandidate) →
    Converges u a → Converges v b →
    Converges (λ n → complexNormSquared (complex (u n) (v n))) (complexNormSquared (complex a b))
  norm-limit u v a b hu hv = joint-continuous-limit _+completion_ addition-joint-continuous
    (λ n → squareCompletion (u n)) (λ n → squareCompletion (v n))
    (squareCompletion a) (squareCompletion b) (square-limit u a hu) (square-limit v b hv)

  -- Arbitrary completion inputs presented by arbitrary representatives.
  -- Radius/budget selection remains explicit; no rationality of the limits.
  bounded-completion-relative-bound : (P d e : Q.ℚ) → 0 ≤ P → 0 ≤ d → P Q.· d ≤ one-half →
    squareℚ (squareℚ P) Q.· (squareℚ d Q.+ squareℚ d) ≤ squareℚ e →
    (x y : RegularCauchy) →
    Eventually (λ n → MagnitudeBound (approximation x (suc n)) P) →
    Eventually (λ n → MagnitudeBound (approximation y (suc n)) d) →
    CompletionLE (localResidualNorm SQ.[ x ] SQ.[ y ])
      (preferredCompletionMultiplication (embedMetricℚ (squareℚ e)) (squareCompletion SQ.[ y ]))
  bounded-completion-relative-bound P d e Ppositive dpositive small budget x y hx hy =
    completion-limit-order
      (λ n → complexNormSquared (rationalOperationalRemainder (q n)))
      (λ n → preferredCompletionMultiplication (embedMetricℚ (squareℚ e)) (squareCompletion (embedMetricℚ (h n))))
      (localResidualNorm SQ.[ x ] SQ.[ y ])
      (preferredCompletionMultiplication (embedMetricℚ (squareℚ e)) (squareCompletion SQ.[ y ]))
      (norm-limit (λ n → cosineValue (q n) +completion embedMetricℚ (Q.- 1))
        (λ n → sineValue (q n) +completion embedMetricℚ (Q.- q n))
        (cosineRemainder a) (sineRemainder a)
        (converges-pointwise-path (λ n → cosineRemainder (embedMetricℚ (q n)))
          (λ n → cosineValue (q n) +completion embedMetricℚ (Q.- 1)) (cosineRemainder a)
          (λ n → sym (cosine-remainder-rational (q n)))
          (continuous-limit cosineRemainder cosine-remainder-continuous (λ n → embedMetricℚ (q n)) a q-limit))
        (converges-pointwise-path (λ n → sineRemainder (embedMetricℚ (q n)))
          (λ n → sineValue (q n) +completion embedMetricℚ (Q.- q n)) (sineRemainder a)
          (λ n → sym (sine-remainder-rational (q n)))
          (continuous-limit sineRemainder sine-remainder-continuous (λ n → embedMetricℚ (q n)) a q-limit)))
      (joint-continuous-limit preferredCompletionMultiplication multiplication-joint-continuous
        (λ _ → embedMetricℚ (squareℚ e)) (λ n → squareCompletion (embedMetricℚ (h n)))
        (embedMetricℚ (squareℚ e)) (squareCompletion SQ.[ y ])
        (constant-converges (embedMetricℚ (squareℚ e)))
        (square-limit (rational-approximants y) SQ.[ y ] (rational-approximants-converge y)))
      (eventually-zip (λ n px hy → rational-operational-relative-bound (p n) (h n) P d e
        Ppositive dpositive px hy
        (weaken-magnitude-bound (q n) (P Q.· d) one-half small
          (negate-magnitude-bound (p n Q.· h n) (P Q.· d)
            (arbitrary-multiplier-bound (p n) P (h n) d Ppositive dpositive px hy))) budget) hx hy)
    where
    p h q : ℕ → Q.ℚ
    p n = approximation x (suc n)
    h n = approximation y (suc n)
    q n = Q.- (p n Q.· h n)
    a : MetricCompletionCandidate
    a = -completion (preferredCompletionMultiplication SQ.[ x ] SQ.[ y ])
    q-limit : Converges (λ n → embedMetricℚ (q n)) a
    q-limit = rational-negative-sequence-converges (λ n → p n Q.· h n)
      (preferredCompletionMultiplication SQ.[ x ] SQ.[ y ])
      (rational-moving-product-converges p h SQ.[ x ] SQ.[ y ]
        (rational-approximants-converge x) (rational-approximants-converge y))
