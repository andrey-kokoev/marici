{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module OperationalSineMetric where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; suc; max)
import Cubical.Data.Nat.Order as ℕOrder
open import Cubical.Data.Rationals as Q
open import Cubical.HITs.PropositionalTruncation as PT
open import Cubical.HITs.SetQuotients as SQ using ([_])
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CompletionUnaryDescent
open import TaylorLiftContract
open import RationalTaylorApproximants
open import RationalSineTaylorApproximants
open import CanonicalSineSchedule
open import CanonicalDyadicallyBoundedCauchy
open import CanonicalSineRegularity
open import CanonicalSineComparisonSchedule
open import CanonicalSineUniformComparison
open import UniformSineInputStabilityContract
open import UniformSineLateDifference

sine-comparison-input-depth-above-output :
  (x y : RegularCauchy) (n : ℕ) →
  ℕOrder._≤_ n (comparisonSineInputDepth x y n)
sine-comparison-input-depth-above-output x y n =
  ℕOrder.≤-trans ℕOrder.≤-sucℕ ℕOrder.≤SumRight

canonical-sine-respects-metric :
  (x y : RegularCauchy) → x ≈metric y →
  canonicalSineRegular x ≈metric canonicalSineRegular y
canonical-sine-respects-metric x y relation k =
  let stability = operationalUniformSinePartialSumInputStability
      d = comparisonSineExponent x y
      k3 = suc (suc (suc k))
      metricDepth = uniformSineMetricDepth stability d k3
  in
  PT.rec isPropPropTrunc
    (λ { (N , inputBounds) →
      ∣ (ℕ.max N k3 , λ n threshold≤n →
        let N≤n = ℕOrder.≤-trans ℕOrder.left-≤-max threshold≤n
            k3≤n = ℕOrder.≤-trans ℕOrder.right-≤-max threshold≤n
            N≤input = ℕOrder.≤-trans N≤n
              (sine-comparison-input-depth-above-output x y n)
            input = inputBounds (comparisonSineInputDepth x y n) N≤input
        in
        canonical-sine-uniform-pointwise-forward
          stability x y k n k3≤n (fst input) (snd input) ,
        canonical-sine-uniform-pointwise-backward
          stability x y k n k3≤n (fst input) (snd input)) ∣₁ })
    (relation metricDepth)

canonicalSineSeriesLiftCertificate :
  ScheduledSeriesLiftCertificate sinePartialSum
canonicalSineSeriesLiftCertificate .regularity =
  canonicalSineScheduledRegularity
canonicalSineSeriesLiftCertificate .respectsSeriesMetric =
  canonical-sine-respects-metric

canonicalSineMetricLift : MetricUnaryLift
canonicalSineMetricLift =
  metricLiftFromSeriesCertificate canonicalSineSeriesLiftCertificate

completionSine : MetricCompletionCandidate → MetricCompletionCandidate
completionSine = descendMetricUnary canonicalSineMetricLift

sin : MetricCompletionCandidate → MetricCompletionCandidate
sin = completionSine
