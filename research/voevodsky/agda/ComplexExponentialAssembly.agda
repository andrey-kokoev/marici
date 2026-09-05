{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module ComplexExponentialAssembly where

open import Cubical.Foundations.Prelude
open import CauchyMetricEquivalence
open import CauchyCompletionAbGroup
open import CauchyCompletionCommRing
open import CauchyCompletionMultiplication
open import CauchyCompletionMultiplicativeLaws
open import ConstructiveComplexCompletion
open import OperationalExponentialMetric
open import OperationalCosineMetric

record CompletionSine : Type₁ where
  field
    sinCompletion : MetricCompletionCandidate → MetricCompletionCandidate
    sinZero : sinCompletion zeroCompletion ≡ zeroCompletion
open CompletionSine public

complexExponentialFromSine :
  CompletionSine → ComplexCompletion → ComplexCompletion
complexExponentialFromSine sine (real , imaginary) =
  complex
    (preferredCompletionMultiplication
      (completionExponential real) (completionCosine imaginary))
    (preferredCompletionMultiplication
      (completionExponential real) (sinCompletion sine imaginary))

complex-exponential-real-part :
  (sine : CompletionSine) (z : ComplexCompletion) →
  realPart (complexExponentialFromSine sine z) ≡
  preferredCompletionMultiplication
    (completionExponential (realPart z))
    (completionCosine (imaginaryPart z))
complex-exponential-real-part sine (real , imaginary) = refl

complex-exponential-imaginary-part :
  (sine : CompletionSine) (z : ComplexCompletion) →
  imaginaryPart (complexExponentialFromSine sine z) ≡
  preferredCompletionMultiplication
    (completionExponential (realPart z))
    (sinCompletion sine (imaginaryPart z))
complex-exponential-imaginary-part sine (real , imaginary) = refl

record RealExponentialCosineZeroLaws : Type where
  field
    exponentialZero : completionExponential zeroCompletion ≡ oneCompletion
    cosineZero : completionCosine zeroCompletion ≡ oneCompletion
open RealExponentialCosineZeroLaws public

complex-exponential-zero :
  (sine : CompletionSine) → RealExponentialCosineZeroLaws →
  complexExponentialFromSine sine zeroComplex ≡ oneComplex
complex-exponential-zero sine laws =
  complex-ext _ _
    (cong₂ preferredCompletionMultiplication
      (exponentialZero laws) (cosineZero laws) ∙
      preferred-completion-multiplication-left-unit oneCompletion)
    (cong₂ preferredCompletionMultiplication
      (exponentialZero laws) (sinZero sine) ∙
      preferred-completion-multiplication-right-zero oneCompletion)
