{-# OPTIONS --safe --cubical --guardedness #-}
module TickPhaseNormTransfer where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Rationals as Q
import Cubical.HITs.SetQuotients as SQ
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyAddition
open import CauchyAdditionCongruence
open import CauchyCompletionCommRing
open import CauchyCompletionMultiplication
open import CanonicalRegularMultiplication
open import CanonicalCosineRegularity
open import CanonicalSineRegularity
open import OperationalCosineMetric
open import OperationalSineMetric
open import CompletionUnaryDescent
open import ConstructiveComplexCompletion
open import TickCompletionPhase

square : MetricCompletionCandidate → MetricCompletionCandidate
square x = preferredCompletionMultiplication x x

normSquared : ComplexCompletion → MetricCompletionCandidate
normSquared z = square (realPart z) +completion square (imaginaryPart z)

trigNorm : MetricCompletionCandidate → MetricCompletionCandidate
trigNorm x = square (completionCosine x) +completion square (completionSine x)

-- These are the ACTUAL independently scheduled operational representatives,
-- including the shifted samples used by canonical completion multiplication.
normRepresentative : RegularCauchy → RegularCauchy
normRepresentative x = addRegular
  (canonicalRegularProduct (canonicalCosineRegular x) (canonicalCosineRegular x))
  (canonicalRegularProduct (canonicalSineRegular x) (canonicalSineRegular x))

abstract
  norm-representative-class : (x : RegularCauchy)
    → SQ.[ normRepresentative x ] ≡ trigNorm SQ.[ x ]
  norm-representative-class x = cong₂ _+completion_
    (canonicalRegularProductClass (canonicalCosineRegular x) (canonicalCosineRegular x)
      ∙ cong square (sym (descendMetricUnary-on-representative canonicalCosineMetricLift x)))
    (canonicalRegularProductClass (canonicalSineRegular x) (canonicalSineRegular x)
      ∙ cong square (sym (descendMetricUnary-on-representative canonicalSineMetricLift x)))

-- The remaining analytic obligation, not an assumed global instance.
ScheduledNormBound : Type
ScheduledNormBound = (x : RegularCauchy) → normRepresentative x ≈metric constantCauchy 1

representative-unit-norm : ScheduledNormBound → (x : RegularCauchy)
  → trigNorm SQ.[ x ] ≡ oneCompletion
representative-unit-norm bounds x =
  sym (norm-representative-class x) ∙ SQ.eq/ _ _ (bounds x)

completion-unit-norm : ScheduledNormBound → (x : MetricCompletionCandidate)
  → trigNorm x ≡ oneCompletion
completion-unit-norm bounds = SQ.elimProp
  (λ x → metric-candidate-isSet (trigNorm x) oneCompletion)
  (representative-unit-norm bounds)

phase-norm-reduction : (p t : MetricCompletionCandidate)
  → normSquared (phase p t) ≡ trigNorm (angle p t)
phase-norm-reduction p t = cong₂ _+completion_
  (cong square (phase-real p t)) (cong square (phase-imaginary p t))

phase-unit-norm : ScheduledNormBound → (p t : MetricCompletionCandidate)
  → normSquared (phase p t) ≡ oneCompletion
phase-unit-norm bounds p t = phase-norm-reduction p t
  ∙ completion-unit-norm bounds (angle p t)
