{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module OperationalAnalyticZeroLaws where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ)
open import Cubical.Data.Rationals as Q
open import Cubical.HITs.SetQuotients as SQ using ([_])
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyCompletionAbGroup
open import CauchyCompletionCommRing
open import CompletionUnaryDescent
open import TaylorLiftContract
open import RationalTaylorApproximants
open import RationalSineTaylorApproximants
open import CanonicalExponentialRegularity
open import CanonicalCosineRegularity
open import CanonicalSineRegularity
open import OperationalExponentialMetric
open import OperationalCosineMetric
open import OperationalSineMetric
open import ConstructiveComplexCompletion
open import ComplexExponentialAssembly

canonical-exponential-regular-zero :
  canonicalExponentialRegular (constantCauchy 0) ≡ constantCauchy 1
canonical-exponential-regular-zero =
  regularCauchy-ext _ _ (funExt λ n →
    exponentialPartialSum-at-zero
      (series-depth
        (scheduleFor canonicalExponentialScheduledRegularity
          (constantCauchy 0)) n))

canonical-cosine-regular-zero :
  canonicalCosineRegular (constantCauchy 0) ≡ constantCauchy 1
canonical-cosine-regular-zero =
  regularCauchy-ext _ _ (funExt λ n →
    cosinePartialSum-at-zero
      (series-depth
        (scheduleFor canonicalCosineScheduledRegularity
          (constantCauchy 0)) n))

completion-exponential-zero :
  completionExponential zeroCompletion ≡ oneCompletion
completion-exponential-zero =
  cong SQ.[_] canonical-exponential-regular-zero

canonical-sine-regular-zero :
  canonicalSineRegular (constantCauchy 0) ≡ constantCauchy 0
canonical-sine-regular-zero =
  regularCauchy-ext _ _ (funExt λ n →
    sinePartialSum-at-zero
      (series-depth
        (scheduleFor canonicalSineScheduledRegularity
          (constantCauchy 0)) n))

completion-sine-zero : completionSine zeroCompletion ≡ zeroCompletion
completion-sine-zero = cong SQ.[_] canonical-sine-regular-zero

operational-completion-sine : CompletionSine
operational-completion-sine .sinCompletion = completionSine
operational-completion-sine .sinZero = completion-sine-zero

completion-cosine-zero :
  completionCosine zeroCompletion ≡ oneCompletion
completion-cosine-zero =
  cong SQ.[_] canonical-cosine-regular-zero

operational-real-analytic-zero-laws : RealExponentialCosineZeroLaws
operational-real-analytic-zero-laws .exponentialZero =
  completion-exponential-zero
operational-real-analytic-zero-laws .cosineZero = completion-cosine-zero

operationalComplexExponential : ComplexCompletion → ComplexCompletion
operationalComplexExponential =
  complexExponentialFromSine operational-completion-sine

operational-complex-exponential-zero :
  operationalComplexExponential zeroComplex ≡ oneComplex
operational-complex-exponential-zero =
  complex-exponential-zero operational-completion-sine
    operational-real-analytic-zero-laws
