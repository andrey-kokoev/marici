{-# OPTIONS --safe --cubical --guardedness #-}
module TickPhaseComposition where

open import Cubical.Foundations.Prelude
open import CauchyMetricEquivalence
open import CauchyAdditionCongruence using (_+completion_)
open import CauchyNegation using (-completion_)
open import CauchyCompletionAbGroup using (completion-+Comm)
open import CauchyCompletionMultiplication
open import CauchyCompletionMultiplicativeLaws using (preferred-completion-multiplication-distributive-right)
open import ConstructiveComplexCompletion
open import OperationalCosineMetric using (completionCosine)
open import OperationalSineMetric using (completionSine)
open import TickCompletionPhase
open import TickCompletionTrigAddition

-- A component presentation of the existing phase, not a new exponential.
phase-components : (p t : MetricCompletionCandidate) →
  phase p t ≡ complex (completionCosine (angle p t)) (completionSine (angle p t))
phase-components p t = complex-ext _ _ (phase-real p t) (phase-imaginary p t)

abstract
  operational-rotation-addition : (x y : MetricCompletionCandidate) →
    complex (completionCosine (x +completion y)) (completionSine (x +completion y)) ≡
    complex (completionCosine x) (completionSine x) ·complex complex (completionCosine y) (completionSine y)
  operational-rotation-addition x y = cong₂ complex (completion-cosine-addition x y)
    (completion-sine-addition x y ∙ completion-+Comm
      (preferredCompletionMultiplication (completionSine x) (completionCosine y))
      (preferredCompletionMultiplication (completionCosine x) (completionSine y)))

  operational-phase-addition : (p s t : MetricCompletionCandidate) →
    phase p (s +completion t) ≡ phase p s ·complex phase p t
  operational-phase-addition p s t = phase-components p (s +completion t)
    ∙ cong (λ a → complex (completionCosine a) (completionSine a))
      (preferred-completion-multiplication-distributive-right (-completion p) s t)
    ∙ operational-rotation-addition (angle p s) (angle p t)
    ∙ cong₂ _·complex_ (sym (phase-components p s)) (sym (phase-components p t))
