{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CompletionExponentialNaturalMultiples where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ; zero; suc)
open import CauchyMetricEquivalence
open import CauchyAdditionCongruence
open import CauchyCompletionAbGroup using (zeroCompletion)
open import CauchyCompletionCommRing using (oneCompletion)
open import CauchyCompletionMultiplication
open import OperationalExponentialMetric using (completionExponential)
open import OperationalAnalyticZeroLaws using (completion-exponential-zero)
open import CompletionExponentialMultiplicationLaw

-- Recursion is over natural multiplicity, not approximation depth.
completionNaturalMultiple : ℕ → MetricCompletionCandidate → MetricCompletionCandidate
completionNaturalMultiple zero x = zeroCompletion
completionNaturalMultiple (suc n) x = x +completion completionNaturalMultiple n x

completionNaturalPower : MetricCompletionCandidate → ℕ → MetricCompletionCandidate
completionNaturalPower x zero = oneCompletion
completionNaturalPower x (suc n) =
  preferredCompletionMultiplication x (completionNaturalPower x n)

completionExponentialNaturalMultiple : (n : ℕ) (x : MetricCompletionCandidate) →
  completionExponential (completionNaturalMultiple n x) ≡
  completionNaturalPower (completionExponential x) n
completionExponentialNaturalMultiple zero x = completion-exponential-zero
completionExponentialNaturalMultiple (suc n) x =
  sym (completionExponentialMultiplication x (completionNaturalMultiple n x)) ∙
  cong (preferredCompletionMultiplication (completionExponential x))
    (completionExponentialNaturalMultiple n x)
