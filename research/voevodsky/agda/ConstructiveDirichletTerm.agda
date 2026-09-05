{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module ConstructiveDirichletTerm where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ)
open import Cubical.HITs.SetQuotients as SQ using ([_])
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyCompletionAbGroup
open import ConstructiveComplexCompletion
open import RationalLogConvergenceContract
open import AtanhPowerDecayContract
open import AtanhTailBounds

embedRegularReal : RegularCauchy → ComplexCompletion
embedRegularReal x = complex SQ.[ x ] zeroCompletion

negativeLogProduct : ComplexCompletion → RegularCauchy → ComplexCompletion
negativeLogProduct s logarithm =
  negComplex (s ·complex embedRegularReal logarithm)

positiveNaturalDirichletTerm :
  (ComplexCompletion → ComplexCompletion) →
  (n : ℕ) → PositiveNaturalLogEvaluationInput n →
  ComplexCompletion → ComplexCompletion
positiveNaturalDirichletTerm exponential n logarithmInput s =
  exponential
    (negativeLogProduct s
      (positiveNaturalLogRegularFromInput n logarithmInput))

positiveNaturalDirichletTermFromPowerPrinciple :
  (ComplexCompletion → ComplexCompletion) →
  DyadicGapHalfPowerPrinciple →
  (n : ℕ) → PositiveNaturalLogGapCertificate n →
  ComplexCompletion → ComplexCompletion
positiveNaturalDirichletTermFromPowerPrinciple exponential principle n gap s =
  exponential
    (negativeLogProduct s
      (positiveNaturalLogRegularFromPowerPrinciple principle n gap))

positiveNaturalDirichletTermOne :
  (ComplexCompletion → ComplexCompletion) →
  ComplexCompletion → ComplexCompletion
positiveNaturalDirichletTermOne exponential s =
  exponential (negativeLogProduct s positiveNaturalLogOneRegular)

positiveNaturalDirichletTermTwo :
  (ComplexCompletion → ComplexCompletion) →
  ComplexCompletion → ComplexCompletion
positiveNaturalDirichletTermTwo exponential s =
  exponential (negativeLogProduct s positiveNaturalLogTwoRegular)
