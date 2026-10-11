{-# OPTIONS --safe --cubical --guardedness #-}
module TickRationalProductLimits where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ)
open import Cubical.Data.Rationals as Q
open import CauchyMetricEquivalence
open import CauchyCompletionMultiplication
open import CauchyAdditionCongruence using (_+completion_)
open import CauchyNegation using (-completion_)
open import CauchyRationalEmbedding
open import TickCompletionRingContinuity
open import TickCompletionLimits

-- Keep the arguments neutral while checking the rational-product path.
-- Concrete series expressions are substituted only after this proof is opaque.
abstract
  rational-product-sequence-converges : (a : Q.ℚ) (r : ℕ → Q.ℚ)
    (b : MetricCompletionCandidate) →
    Converges (λ n → embedMetricℚ (r n)) b →
    Converges (λ n → embedMetricℚ (a Q.· r n))
      (preferredCompletionMultiplication (embedMetricℚ a) b)
  rational-product-sequence-converges a r b h =
    converges-pointwise-path
      (λ n → preferredCompletionMultiplication (embedMetricℚ a) (embedMetricℚ (r n)))
      (λ n → embedMetricℚ (a Q.· r n))
      (preferredCompletionMultiplication (embedMetricℚ a) b)
      (λ n → preferredCompletionMultiplication-preserves-rationals a (r n))
      (joint-continuous-limit preferredCompletionMultiplication multiplication-joint-continuous
        (λ _ → embedMetricℚ a) (λ n → embedMetricℚ (r n)) (embedMetricℚ a) b
        (constant-converges (embedMetricℚ a)) h)

  rational-sum-sequence-converges : (p q : ℕ → Q.ℚ) (a b : MetricCompletionCandidate) →
    Converges (λ n → embedMetricℚ (p n)) a → Converges (λ n → embedMetricℚ (q n)) b →
    Converges (λ n → embedMetricℚ (p n Q.+ q n)) (a +completion b)
  rational-sum-sequence-converges p q a b hp hq = converges-pointwise-path
    (λ n → embedMetricℚ (p n) +completion embedMetricℚ (q n))
    (λ n → embedMetricℚ (p n Q.+ q n)) (a +completion b)
    (λ n → sym (embedℚ-preserves-sum (p n) (q n)))
    (joint-continuous-limit _+completion_ addition-joint-continuous
      (λ n → embedMetricℚ (p n)) (λ n → embedMetricℚ (q n)) a b hp hq)

  rational-negative-sequence-converges : (p : ℕ → Q.ℚ) (a : MetricCompletionCandidate) →
    Converges (λ n → embedMetricℚ (p n)) a →
    Converges (λ n → embedMetricℚ (Q.- p n)) (-completion a)
  rational-negative-sequence-converges p a hp = converges-pointwise-path
    (λ n → -completion (embedMetricℚ (p n))) (λ n → embedMetricℚ (Q.- p n)) (-completion a)
    (λ n → embedℚ-preserves-negation (p n))
    (continuous-limit -completion_ negation-metric-continuous (λ n → embedMetricℚ (p n)) a hp)

  convergent-limits-equal : (u : ℕ → MetricCompletionCandidate) (a b : MetricCompletionCandidate) →
    Converges u a → Converges u b → a ≡ b
  convergent-limits-equal u a b ha hb = close-limits-equal u u a b ha hb
    (pointwise-close u u (λ _ → refl))
