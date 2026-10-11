{-# OPTIONS --safe --cubical --guardedness #-}
module TickCompletionSumPaths where

open import Cubical.Foundations.Prelude
open import CauchyMetricEquivalence
open import CauchyAdditionCongruence using (_+completion_)
open import Cubical.Data.Rationals as Q
open import CauchyNegation using (-completion_)
open import CauchyRationalEmbedding using (embedℚ-preserves-negation)

abstract
  sum-to-defined : (a b c d z : MetricCompletionCandidate) →
    a ≡ b → c ≡ d → z ≡ b +completion d → a +completion c ≡ z
  sum-to-defined a b c d z p q definition = cong₂ _+completion_ p q ∙ sym definition

  constant-remainder-agreement : (f : Q.ℚ → MetricCompletionCandidate)
    (F R : MetricCompletionCandidate → MetricCompletionCandidate) (c : Q.ℚ) →
    ((q : Q.ℚ) → f q ≡ F (embedMetricℚ q)) →
    ((a : MetricCompletionCandidate) → R a ≡ F a +completion embedMetricℚ c) →
    (q : Q.ℚ) → f q +completion embedMetricℚ c ≡ R (embedMetricℚ q)
  constant-remainder-agreement f F R c path definition q = cong
    (λ a → a +completion embedMetricℚ c) (path q) ∙ sym (definition (embedMetricℚ q))

  linear-remainder-agreement : (f : Q.ℚ → MetricCompletionCandidate)
    (F R : MetricCompletionCandidate → MetricCompletionCandidate) →
    ((q : Q.ℚ) → f q ≡ F (embedMetricℚ q)) →
    ((a : MetricCompletionCandidate) → R a ≡ F a +completion (-completion a)) →
    (q : Q.ℚ) → f q +completion embedMetricℚ (Q.- q) ≡ R (embedMetricℚ q)
  linear-remainder-agreement f F R path definition q = cong₂ _+completion_
    (path q) (sym (embedℚ-preserves-negation q)) ∙ sym (definition (embedMetricℚ q))
