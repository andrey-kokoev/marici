{-# OPTIONS --safe --cubical --no-import-sorts --guardedness --lossy-unification #-}
module CanonicalComplexRegularExponential where

open import Cubical.Foundations.Prelude
open import Cubical.HITs.SetQuotients as SQ using ([_])
open import RegularCauchyStructure
open import ConstructiveComplexCompletion
open import ComplexCauchyApproximation
open import CauchyCompletionMultiplication
open import CompletionUnaryDescent
open import CanonicalExponentialRegularity
open import CanonicalCosineRegularity
open import CanonicalSineRegularity
open import OperationalExponentialMetric
open import OperationalCosineMetric
open import OperationalSineMetric
open import OperationalAnalyticZeroLaws
open import CanonicalRegularMultiplication

canonicalComplexRegularExponential : ComplexRegular → ComplexRegular
canonicalComplexRegularExponential (real , imaginary) =
  canonicalRegularProduct
    (canonicalExponentialRegular real) (canonicalCosineRegular imaginary)
  ,
  canonicalRegularProduct
    (canonicalExponentialRegular real) (canonicalSineRegular imaginary)

canonicalComplexRegularExponentialClass : (z : ComplexRegular) →
  complexRegularClass (canonicalComplexRegularExponential z) ≡
  operationalComplexExponential (complexRegularClass z)
canonicalComplexRegularExponentialClass (real , imaginary) =
  complex-ext _ _
    (canonicalRegularProductClass
      (canonicalExponentialRegular real) (canonicalCosineRegular imaginary) ∙
     cong₂ preferredCompletionMultiplication
       (sym (descendMetricUnary-on-representative
         canonicalExponentialMetricLift real))
       (sym (descendMetricUnary-on-representative
         canonicalCosineMetricLift imaginary)))
    (canonicalRegularProductClass
      (canonicalExponentialRegular real) (canonicalSineRegular imaginary) ∙
     cong₂ preferredCompletionMultiplication
       (sym (descendMetricUnary-on-representative
         canonicalExponentialMetricLift real))
       (sym (descendMetricUnary-on-representative
         canonicalSineMetricLift imaginary)))
