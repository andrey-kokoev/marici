{-# OPTIONS --safe --cubical --guardedness #-}
module TickCompletionDerivative where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ)
import Cubical.Data.Nat.Order as N
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Data.Sigma using (Σ; _×_)
open import Cubical.HITs.PropositionalTruncation as PT
import Cubical.HITs.SetQuotients as SQ
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyAdditionCongruence using (_+completion_)
open import CauchyNegation using (-completion_)
open import CauchyCompletionAbGroup using (zeroCompletion)
open import CauchyCompletionMultiplication using (preferredCompletionMultiplication)
open import ConstructiveComplexCompletion
open import TickCompletionMetric

-- Closed nonnegative cone: arbitrarily small additive rational slack.
EventuallyNonnegative : RegularCauchy → ℕ → Type
EventuallyNonnegative x k = ∥ Σ ℕ (λ threshold → (n : ℕ) → N._≤_ threshold n →
  Q.- precision k ≤ approximation x n) ∥₁

CompletionNonnegative : MetricCompletionCandidate → Type
CompletionNonnegative a = (k : ℕ) → ∥ Σ RegularCauchy (λ x →
  (SQ.[ x ] ≡ a) × EventuallyNonnegative x k) ∥₁

CompletionLE : MetricCompletionCandidate → MetricCompletionCandidate → Type
CompletionLE a b = CompletionNonnegative (b +completion (-completion a))

squareCompletion : MetricCompletionCandidate → MetricCompletionCandidate
squareCompletion a = preferredCompletionMultiplication a a

complexNormSquared : ComplexCompletion → MetricCompletionCandidate
complexNormSquared z = squareCompletion (realPart z) +completion squareCompletion (imaginaryPart z)

scaleComplex : MetricCompletionCandidate → ComplexCompletion → ComplexCompletion
scaleComplex h z = complex (preferredCompletionMultiplication h (realPart z))
  (preferredCompletionMultiplication h (imaginaryPart z))

firstOrderRemainder : (MetricCompletionCandidate → ComplexCompletion) →
  MetricCompletionCandidate → ComplexCompletion → MetricCompletionCandidate → ComplexCompletion
firstOrderRemainder f t v h = (f (t +completion h) +complex negComplex (f t)) +complex negComplex (scaleComplex h v)

-- All completion-valued increments, not just rational or sampled ones.
-- ||f(t+h)-f(t)-h*v||^2 <= epsilon^2 * h^2, without division/square roots.
HasMetricDerivative : (MetricCompletionCandidate → ComplexCompletion) →
  MetricCompletionCandidate → ComplexCompletion → Type
HasMetricDerivative f t v = (k : ℕ) → ∥ Σ ℕ (λ l → (h : MetricCompletionCandidate) →
  CompletionWithin zeroCompletion h l →
  CompletionLE (complexNormSquared (firstOrderRemainder f t v h))
    (preferredCompletionMultiplication (embedMetricℚ (precision k Q.· precision k)) (squareCompletion h))) ∥₁
