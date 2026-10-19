{-# OPTIONS --safe --cubical --guardedness #-}
module TickComplexAffineDerivative where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as Nat using (ℕ)
open import Cubical.Data.Sigma using (Σ)
open import Cubical.HITs.PropositionalTruncation as PT
open import CauchyMetricEquivalence using (MetricCompletionCandidate; embedMetricℚ)
open import CauchyCompletionMultiplication using (preferredCompletionMultiplication)
open import ConstructiveComplexCompletion
open import TickCompletionDerivative
open import TickComplexAffineRemainder using (affineCurve; affine-remainder-norm)
open import TickCompletionCoefficientBound using (completion-dyadic-upper; precisionSquared; coefficient-absorption)
open import TickCompletionOrderArithmetic using (complex-norm-nonnegative; completion-order-trans)
open import TickCompletionPositiveProduct using (completion-multiply-monotone)

abstract
  -- No norm restriction on b, no rational-time restriction, no division by
  -- the increment. A truncated dyadic bound chooses the finer precision.
  affine-metric-derivative : (a b : ComplexCompletion)
    (f : MetricCompletionCandidate → ComplexCompletion) (t : MetricCompletionCandidate) (v : ComplexCompletion) →
    HasMetricDerivative f t v → HasMetricDerivative (affineCurve a b f) t (v ·complex b)
  affine-metric-derivative a b f t v derivative k = PT.rec isPropPropTrunc
    (λ { (d , bound) → PT.map (λ { (l , estimates) → l , λ h near →
      subst (λ n → CompletionLE n
        (preferredCompletionMultiplication (embedMetricℚ (precisionSquared k)) (squareCompletion h)))
        (sym (affine-remainder-norm a b f t v h))
        (completion-order-trans
          (preferredCompletionMultiplication (complexNormSquared (firstOrderRemainder f t v h)) (complexNormSquared b))
          (preferredCompletionMultiplication
            (preferredCompletionMultiplication (embedMetricℚ (precisionSquared (d Nat.+ k))) (squareCompletion h)) (complexNormSquared b))
          (preferredCompletionMultiplication (embedMetricℚ (precisionSquared k)) (squareCompletion h))
          (completion-multiply-monotone (complexNormSquared (firstOrderRemainder f t v h))
            (preferredCompletionMultiplication (embedMetricℚ (precisionSquared (d Nat.+ k))) (squareCompletion h))
            (complexNormSquared b) (estimates h near) (complex-norm-nonnegative b))
          (coefficient-absorption (complexNormSquared b) d k bound h)) }) (derivative (d Nat.+ k)) })
    (completion-dyadic-upper (complexNormSquared b))
