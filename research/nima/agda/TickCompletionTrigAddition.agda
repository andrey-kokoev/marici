{-# OPTIONS --safe --cubical --guardedness #-}
module TickCompletionTrigAddition where

open import Cubical.Foundations.Prelude
import Cubical.Data.Rationals as Q
open import CauchyMetricEquivalence
open import CauchyAdditionCongruence using (_+completion_)
open import CauchyNegation using (-completion_)
open import CauchyRationalEmbedding using (embedℚ-preserves-sum)
open import CauchyCompletionMultiplication
open import OperationalCosineMetric using (completionCosine)
open import OperationalSineMetric using (completionSine)
open import TickCompletionMetric
open import TickCompletionRingContinuity
open import TickCompletionLimits
open import TickRationalTrigAddition
open import TickPhaseMetricContinuity using
  (operational-cosine-metric-continuous; operational-sine-metric-continuous)

sum-continuous : {f g : MetricCompletionCandidate → MetricCompletionCandidate} →
  MetricContinuous f → MetricContinuous g → MetricContinuous (λ x → f x +completion g x)
sum-continuous {f} {g} = joint-compose-continuous _+completion_ f g addition-joint-continuous

product-continuous : {f g : MetricCompletionCandidate → MetricCompletionCandidate} →
  MetricContinuous f → MetricContinuous g → MetricContinuous (λ x → preferredCompletionMultiplication (f x) (g x))
product-continuous {f} {g} = joint-compose-continuous preferredCompletionMultiplication f g multiplication-joint-continuous

cosine-sum-continuous : (f g : MetricCompletionCandidate → MetricCompletionCandidate) →
  MetricContinuous f → MetricContinuous g → MetricContinuous (λ x → completionCosine (f x +completion g x))
cosine-sum-continuous f g fc gc = compose-metric-continuous operational-cosine-metric-continuous (sum-continuous fc gc)

sine-sum-continuous : (f g : MetricCompletionCandidate → MetricCompletionCandidate) →
  MetricContinuous f → MetricContinuous g → MetricContinuous (λ x → completionSine (f x +completion g x))
sine-sum-continuous f g fc gc = compose-metric-continuous operational-sine-metric-continuous (sum-continuous fc gc)

cosine-rhs-continuous : (f g : MetricCompletionCandidate → MetricCompletionCandidate) →
  MetricContinuous f → MetricContinuous g → MetricContinuous (λ x → cosineAdditionRHS (f x) (g x))
cosine-rhs-continuous f g fc gc = sum-continuous
  (product-continuous
    (compose-metric-continuous operational-cosine-metric-continuous fc)
    (compose-metric-continuous operational-cosine-metric-continuous gc))
  (compose-metric-continuous negation-metric-continuous
    (product-continuous
      (compose-metric-continuous operational-sine-metric-continuous fc)
      (compose-metric-continuous operational-sine-metric-continuous gc)))

sine-rhs-continuous : (f g : MetricCompletionCandidate → MetricCompletionCandidate) →
  MetricContinuous f → MetricContinuous g → MetricContinuous (λ x → sineAdditionRHS (f x) (g x))
sine-rhs-continuous f g fc gc = sum-continuous
  (product-continuous
    (compose-metric-continuous operational-sine-metric-continuous fc)
    (compose-metric-continuous operational-cosine-metric-continuous gc))
  (product-continuous
    (compose-metric-continuous operational-cosine-metric-continuous fc)
    (compose-metric-continuous operational-sine-metric-continuous gc))

-- Extend one input at a time. Both continuities refer to the same quotient
-- metric and the same operational functions as the rational-input theorem.
extend-rational-pairs :
  (F G : MetricCompletionCandidate → MetricCompletionCandidate → MetricCompletionCandidate) →
  ((b : MetricCompletionCandidate) → MetricContinuous (λ a → F a b)) →
  ((a : MetricCompletionCandidate) → MetricContinuous (F a)) →
  ((b : MetricCompletionCandidate) → MetricContinuous (λ a → G a b)) →
  ((a : MetricCompletionCandidate) → MetricContinuous (G a)) →
  ((p q : Q.ℚ) → F (embedMetricℚ p) (embedMetricℚ q) ≡ G (embedMetricℚ p) (embedMetricℚ q)) →
  (a b : MetricCompletionCandidate) → F a b ≡ G a b
extend-rational-pairs F G Fl Fr Gl Gr rational a = continuous-agree-on-rationals (F a) (G a) (Fr a) (Gr a)
  (λ q → continuous-agree-on-rationals (λ x → F x (embedMetricℚ q)) (λ x → G x (embedMetricℚ q))
    (Fl (embedMetricℚ q)) (Gl (embedMetricℚ q)) (λ p → rational p q) a)

abstract
  completion-cosine-addition : (x y : MetricCompletionCandidate) →
    completionCosine (x +completion y) ≡
      preferredCompletionMultiplication (completionCosine x) (completionCosine y) +completion
      (-completion (preferredCompletionMultiplication (completionSine x) (completionSine y)))
  completion-cosine-addition = extend-rational-pairs (λ x y → completionCosine (x +completion y)) cosineAdditionRHS
    (λ b → cosine-sum-continuous (λ a → a) (λ _ → b) identity-metric-continuous (constant-metric-continuous b))
    (λ a → cosine-sum-continuous (λ _ → a) (λ b → b) (constant-metric-continuous a) identity-metric-continuous)
    (λ b → cosine-rhs-continuous (λ a → a) (λ _ → b) identity-metric-continuous (constant-metric-continuous b))
    (λ a → cosine-rhs-continuous (λ _ → a) (λ b → b) (constant-metric-continuous a) identity-metric-continuous)
    (λ p q → cong completionCosine (sym (embedℚ-preserves-sum p q)) ∙ rational-cosine-addition p q)

  completion-sine-addition : (x y : MetricCompletionCandidate) →
    completionSine (x +completion y) ≡
      preferredCompletionMultiplication (completionSine x) (completionCosine y) +completion
      preferredCompletionMultiplication (completionCosine x) (completionSine y)
  completion-sine-addition = extend-rational-pairs (λ x y → completionSine (x +completion y)) sineAdditionRHS
    (λ b → sine-sum-continuous (λ a → a) (λ _ → b) identity-metric-continuous (constant-metric-continuous b))
    (λ a → sine-sum-continuous (λ _ → a) (λ b → b) (constant-metric-continuous a) identity-metric-continuous)
    (λ b → sine-rhs-continuous (λ a → a) (λ _ → b) identity-metric-continuous (constant-metric-continuous b))
    (λ a → sine-rhs-continuous (λ _ → a) (λ b → b) (constant-metric-continuous a) identity-metric-continuous)
    (λ p q → cong completionSine (sym (embedℚ-preserves-sum p q)) ∙ rational-sine-addition p q)
