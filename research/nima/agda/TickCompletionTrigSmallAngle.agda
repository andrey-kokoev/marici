{-# OPTIONS --safe --cubical --guardedness #-}
module TickCompletionTrigSmallAngle where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import CauchyMetricEquivalence
open import RegularCauchyStructure
open import CauchyProductBounds
open import CauchyAdditionCongruence using (_+completion_)
open import CauchyNegation using (-completion_)
open import CauchyRationalEmbedding using (embedℚ-preserves-negation)
open import OperationalCosineMetric using (completionCosine)
open import OperationalSineMetric using (completionSine)
open import TickCompletionMetric
open import TickCompletionRingContinuity
open import TickPhaseMetricContinuity using (operational-cosine-metric-continuous; operational-sine-metric-continuous)
open import TickCompletionMagnitudeBounds
open import TickSmallAngleDensity
open import TickOperationalTrigFirstOrder
open import TickCompletionSumPaths

abstract
  cosineRemainder sineRemainder : MetricCompletionCandidate → MetricCompletionCandidate
  cosineRemainder a = completionCosine a +completion embedMetricℚ (Q.- 1)
  sineRemainder a = completionSine a +completion (-completion a)

  cosine-remainder-definition : (a : MetricCompletionCandidate) →
    cosineRemainder a ≡ completionCosine a +completion embedMetricℚ (Q.- 1)
  cosine-remainder-definition a = refl
  sine-remainder-definition : (a : MetricCompletionCandidate) →
    sineRemainder a ≡ completionSine a +completion (-completion a)
  sine-remainder-definition a = refl

  cosine-remainder-continuous : MetricContinuous cosineRemainder
  cosine-remainder-continuous = joint-compose-continuous _+completion_
    completionCosine (λ _ → embedMetricℚ (Q.- 1)) addition-joint-continuous
    operational-cosine-metric-continuous (constant-metric-continuous (embedMetricℚ (Q.- 1)))
  sine-remainder-continuous : MetricContinuous sineRemainder
  sine-remainder-continuous = joint-compose-continuous _+completion_
    completionSine -completion_ addition-joint-continuous
    operational-sine-metric-continuous negation-metric-continuous

cosine-remainder-rational : (q : Q.ℚ) →
  (cosineValue q +completion embedMetricℚ (Q.- 1)) ≡ cosineRemainder (embedMetricℚ q)
cosine-remainder-rational = constant-remainder-agreement cosineValue completionCosine cosineRemainder
  (Q.- 1) cosine-value-class cosine-remainder-definition

sine-remainder-rational : (q : Q.ℚ) →
  (sineValue q +completion embedMetricℚ (Q.- q)) ≡ sineRemainder (embedMetricℚ q)
sine-remainder-rational = linear-remainder-agreement sineValue completionSine sineRemainder
  sine-value-class sine-remainder-definition

-- The inputs here are arbitrary completion values, not just embedded
-- rationals. The public definition paths expose the actual operational
-- residuals, while keeping their schedules opaque during elaboration.
completion-cosine-small-remainder : (a : MetricCompletionCandidate) (e : Q.ℚ) →
  0 ≤ e → e ≤ precision 2 → CompletionMagnitudeBound a e →
  CompletionMagnitudeBound (cosineRemainder a) (e Q.· e)
completion-cosine-small-remainder = small-angle-density
  (λ q → cosineValue q +completion embedMetricℚ (Q.- 1)) cosineRemainder
  cosine-remainder-continuous cosine-remainder-rational cosine-value-small-remainder

completion-sine-small-remainder : (a : MetricCompletionCandidate) (e : Q.ℚ) →
  0 ≤ e → e ≤ precision 2 → CompletionMagnitudeBound a e →
  CompletionMagnitudeBound (sineRemainder a) (e Q.· e)
completion-sine-small-remainder = small-angle-density
  (λ q → sineValue q +completion embedMetricℚ (Q.- q)) sineRemainder
  sine-remainder-continuous sine-remainder-rational sine-value-small-remainder
