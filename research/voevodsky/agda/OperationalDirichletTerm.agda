{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module OperationalDirichletTerm where

open import Cubical.Data.Nat using (ℕ)
open import ConstructiveComplexCompletion
open import OperationalAnalyticZeroLaws
open import RationalLogConvergenceContract
open import AtanhPowerDecayContract
open import AtanhTailBounds
open import ConstructiveDirichletTerm

operationalPositiveNaturalDirichletTerm :
  (n : ℕ) → PositiveNaturalLogEvaluationInput n →
  ComplexCompletion → ComplexCompletion
operationalPositiveNaturalDirichletTerm =
  positiveNaturalDirichletTerm operationalComplexExponential

operationalPositiveNaturalDirichletTermFromPowerPrinciple :
  DyadicGapHalfPowerPrinciple →
  (n : ℕ) → PositiveNaturalLogGapCertificate n →
  ComplexCompletion → ComplexCompletion
operationalPositiveNaturalDirichletTermFromPowerPrinciple =
  positiveNaturalDirichletTermFromPowerPrinciple operationalComplexExponential

operationalDirichletTermOne : ComplexCompletion → ComplexCompletion
operationalDirichletTermOne =
  positiveNaturalDirichletTermOne operationalComplexExponential

operationalDirichletTermTwo : ComplexCompletion → ComplexCompletion
operationalDirichletTermTwo =
  positiveNaturalDirichletTermTwo operationalComplexExponential
