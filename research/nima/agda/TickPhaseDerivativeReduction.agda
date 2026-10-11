{-# OPTIONS --safe --cubical --guardedness #-}
module TickPhaseDerivativeReduction where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ)
open import Cubical.Data.Sigma using (Σ; _,_)
open import Cubical.HITs.PropositionalTruncation as PT
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
import Cubical.Data.Rationals as Q
open import RegularCauchyStructure using (precision)
open import CauchyMetricEquivalence
open import CauchyAdditionCongruence using (_+completion_)
open import CauchyNegation using (-completion_)
open import CauchyCompletionAbGroup using (zeroCompletion)
open import CauchyCompletionCommRing
open import CauchyCompletionMultiplication using (preferredCompletionMultiplication)
open import CauchyCompletionMultiplicativeLaws using (preferred-completion-multiplication-left-unit)
open import ConstructiveComplexCompletion
open import OperationalCosineMetric using (completionCosine)
open import OperationalSineMetric using (completionSine)
open import TickCompletionMetric
open import TickCompletionPhase
open import TickPhaseComposition
open import TickPhaseMetricRegularity
open import TickConstructedScheduledNorm using (operational-phase-unit-norm)

module Algebra {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R)
  factor-real : (u v c s g h : fst R) →
    ((u · c + (- (v · s))) + (- u)) + (- (h · (0r · u + (- (g · v))))) ≡
    u · (c + (- 1r)) + (- (v · (s + (- (g · h)))))
  factor-real u v c s g h = solve! R
  factor-imaginary : (u v c s g h : fst R) →
    ((u · s + v · c) + (- v)) + (- (h · (0r · v + g · u))) ≡
    u · (s + (- (g · h))) + v · (c + (- 1r))
  factor-imaginary u v c s g h = solve! R
  norm-product : (u v r s : fst R) →
    (u · r + (- (v · s))) · (u · r + (- (v · s))) +
    (u · s + v · r) · (u · s + v · r) ≡
    (u · u + v · v) · (r · r + s · s)
  norm-product u v r s = solve! R
module C = Algebra CompletionCommRing

-- A residual at the small angle -p*h, with no dependence on the centre t.
phaseLocalRemainder : MetricCompletionCandidate → MetricCompletionCandidate → ComplexCompletion
phaseLocalRemainder p h = complex
  (completionCosine (angle p h) +completion (-completion oneCompletion))
  (completionSine (angle p h) +completion (-completion (angle p h)))

abstract
  phase-remainder-factor : (p t h : MetricCompletionCandidate) →
    firstOrderRemainder (phase p) t (phaseGenerator p t) h ≡
    phase p t ·complex phaseLocalRemainder p h
  phase-remainder-factor p t h =
    cong (λ z → (z +complex negComplex (phase p t)) +complex
      negComplex (scaleComplex h (phaseGenerator p t)))
      (operational-phase-addition p t h ∙ cong (phase p t ·complex_) (phase-components p h))
    ∙ complex-ext _ _
      (C.factor-real (realPart (phase p t)) (imaginaryPart (phase p t))
        (completionCosine (angle p h)) (completionSine (angle p h)) (-completion p) h)
      (C.factor-imaginary (realPart (phase p t)) (imaginaryPart (phase p t))
        (completionCosine (angle p h)) (completionSine (angle p h)) (-completion p) h)

  complex-norm-product : (z w : ComplexCompletion) →
    complexNormSquared (z ·complex w) ≡
    preferredCompletionMultiplication (complexNormSquared z) (complexNormSquared w)
  complex-norm-product z w = C.norm-product (realPart z) (imaginaryPart z) (realPart w) (imaginaryPart w)

  phase-remainder-norm-local : (p t h : MetricCompletionCandidate) →
    complexNormSquared (firstOrderRemainder (phase p) t (phaseGenerator p t) h) ≡
    complexNormSquared (phaseLocalRemainder p h)
  phase-remainder-norm-local p t h = cong complexNormSquared (phase-remainder-factor p t h)
    ∙ complex-norm-product (phase p t) (phaseLocalRemainder p h)
    ∙ cong (λ a → preferredCompletionMultiplication a (complexNormSquared (phaseLocalRemainder p h)))
      (operational-phase-unit-norm p t)
    ∙ preferred-completion-multiplication-left-unit (complexNormSquared (phaseLocalRemainder p h))

-- This remaining analytic input is NOT supplied by the algebraic reduction.
-- It still quantifies over every completion-valued increment, including zero.
LocalPhaseDerivativeBound : MetricCompletionCandidate → Type
LocalPhaseDerivativeBound p = (k : ℕ) → ∥ Σ ℕ (λ l → (h : MetricCompletionCandidate) →
  CompletionWithin zeroCompletion h l →
  CompletionLE (complexNormSquared (phaseLocalRemainder p h))
    (preferredCompletionMultiplication (embedMetricℚ (precision k Q.· precision k)) (squareCompletion h))) ∥₁

abstract
  local-bound-to-phase-derivative : (p : MetricCompletionCandidate) → LocalPhaseDerivativeBound p →
    (t : MetricCompletionCandidate) → HasMetricDerivative (phase p) t (phaseGenerator p t)
  local-bound-to-phase-derivative p bound t k = PT.map
    (λ { (l , estimate) → l , λ h near → subst
      (λ a → CompletionLE a (preferredCompletionMultiplication
        (embedMetricℚ (precision k Q.· precision k)) (squareCompletion h)))
      (sym (phase-remainder-norm-local p t h)) (estimate h near) }) (bound k)

  phase-derivative-to-local-bound : (p : MetricCompletionCandidate) →
    HasMetricDerivative (phase p) zeroCompletion (phaseGenerator p zeroCompletion) → LocalPhaseDerivativeBound p
  phase-derivative-to-local-bound p derivative k = PT.map
    (λ { (l , estimate) → l , λ h near → subst
      (λ a → CompletionLE a (preferredCompletionMultiplication
        (embedMetricℚ (precision k Q.· precision k)) (squareCompletion h)))
      (phase-remainder-norm-local p zeroCompletion h) (estimate h near) }) (derivative k)

  origin-derivative-to-all-times : (p : MetricCompletionCandidate) →
    HasMetricDerivative (phase p) zeroCompletion (phaseGenerator p zeroCompletion) →
    (t : MetricCompletionCandidate) → HasMetricDerivative (phase p) t (phaseGenerator p t)
  origin-derivative-to-all-times p derivative =
    local-bound-to-phase-derivative p (phase-derivative-to-local-bound p derivative)
