{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module ConstructiveComplexCompletion where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Sigma
open import CauchyMetricEquivalence
open import CauchyAddition
open import CauchyAdditionCongruence
open import CauchyNegation
open import CauchyCompletionAbGroup
open import CauchyCompletionMultiplication
open import CauchyCompletionCommRing

ComplexCompletion : Type
ComplexCompletion = MetricCompletionCandidate × MetricCompletionCandidate

complex : MetricCompletionCandidate → MetricCompletionCandidate → ComplexCompletion
complex real imaginary = real , imaginary

realPart : ComplexCompletion → MetricCompletionCandidate
realPart = fst

imaginaryPart : ComplexCompletion → MetricCompletionCandidate
imaginaryPart = snd

complex-ext : (z w : ComplexCompletion) →
  realPart z ≡ realPart w → imaginaryPart z ≡ imaginaryPart w → z ≡ w
complex-ext (zr , zi) (wr , wi) realPath imaginaryPath =
  cong₂ _,_ realPath imaginaryPath

complex-isSet : isSet ComplexCompletion
complex-isSet = isSet× metric-candidate-isSet metric-candidate-isSet

zeroComplex : ComplexCompletion
zeroComplex = complex zeroCompletion zeroCompletion

oneComplex : ComplexCompletion
oneComplex = complex oneCompletion zeroCompletion

embedComplexℚ : Q.ℚ → ComplexCompletion
embedComplexℚ q = complex (embedMetricℚ q) zeroCompletion

infixl 6 _+complex_
_+complex_ : ComplexCompletion → ComplexCompletion → ComplexCompletion
(ar , ai) +complex (br , bi) =
  complex (ar +completion br) (ai +completion bi)

negComplex : ComplexCompletion → ComplexCompletion
negComplex (ar , ai) = complex (-completion ar) (-completion ai)

infixl 7 _·complex_
_·complex_ : ComplexCompletion → ComplexCompletion → ComplexCompletion
(ar , ai) ·complex (br , bi) =
  complex
    ((preferredCompletionMultiplication ar br) +completion
      (-completion (preferredCompletionMultiplication ai bi)))
    ((preferredCompletionMultiplication ar bi) +completion
      (preferredCompletionMultiplication ai br))

conjugateComplex : ComplexCompletion → ComplexCompletion
conjugateComplex (ar , ai) = complex ar (-completion ai)

IsComplexZero : ComplexCompletion → Type
IsComplexZero z = z ≡ zeroComplex

isComplexZero-isProp : (z : ComplexCompletion) → isProp (IsComplexZero z)
isComplexZero-isProp z = complex-isSet z zeroComplex
