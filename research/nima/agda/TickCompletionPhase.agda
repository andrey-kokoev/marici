{-# OPTIONS --safe --cubical --guardedness #-}
module TickCompletionPhase where

open import Cubical.Foundations.Prelude
open import CauchyMetricEquivalence
open import CauchyNegation
open import CauchyCompletionAbGroup
open import CauchyCompletionCommRing
open import CauchyCompletionMultiplication
open import CauchyCompletionMultiplicativeLaws
open import ConstructiveComplexCompletion
open import OperationalAnalyticZeroLaws
open import OperationalCosineMetric using (completionCosine)
open import OperationalSineMetric using (completionSine)

-- The angular scale is explicit until a completion-valued pi and its
-- trigonometric endpoint laws have been constructed.
angle : MetricCompletionCandidate → MetricCompletionCandidate → MetricCompletionCandidate
angle p t = preferredCompletionMultiplication (-completion p) t

phase : MetricCompletionCandidate → MetricCompletionCandidate → ComplexCompletion
phase p t = operationalComplexExponential (complex zeroCompletion (angle p t))

phase-start : (p : MetricCompletionCandidate) → phase p zeroCompletion ≡ oneComplex
phase-start p =
  cong (λ a → operationalComplexExponential (complex zeroCompletion a))
    (preferred-completion-multiplication-right-zero (-completion p))
  ∙ operational-complex-exponential-zero

phase-real : (p t : MetricCompletionCandidate)
  → realPart (phase p t) ≡ completionCosine (angle p t)
phase-real p t =
  cong (λ a → preferredCompletionMultiplication a (completionCosine (angle p t)))
    completion-exponential-zero
  ∙ preferred-completion-multiplication-left-unit (completionCosine (angle p t))

phase-imaginary : (p t : MetricCompletionCandidate)
  → imaginaryPart (phase p t) ≡ completionSine (angle p t)
phase-imaginary p t =
  cong (λ a → preferredCompletionMultiplication a (completionSine (angle p t)))
    completion-exponential-zero
  ∙ preferred-completion-multiplication-left-unit (completionSine (angle p t))

phase-finish-components : (p : MetricCompletionCandidate)
  → phase p oneCompletion ≡ complex (completionCosine (-completion p)) (completionSine (-completion p))
phase-finish-components p = complex-ext _ _
  (phase-real p oneCompletion ∙ cong completionCosine
    (preferred-completion-multiplication-right-unit (-completion p)))
  (phase-imaginary p oneCompletion ∙ cong completionSine
    (preferred-completion-multiplication-right-unit (-completion p)))
