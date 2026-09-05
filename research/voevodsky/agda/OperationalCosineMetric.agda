{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module OperationalCosineMetric where

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
open import CanonicalCosineSchedule
open import CanonicalDyadicallyBoundedCauchy
open import CanonicalCosineRegularity
open import CanonicalCosineComparisonSchedule
open import CanonicalCosineUniformComparison
open import UniformCosineInputStabilityContract
open import UniformCosineLateDifference
open import UniformCosineSeedBounds
open import CosineTailSchedule
open import CosineSeedConstruction
open import CauchyShift

cosine-comparison-input-depth-above-output :
  (x y : RegularCauchy) (n : ℕ) →
  ℕOrder._≤_ n (comparisonCosineInputDepth x y n)
cosine-comparison-input-depth-above-output x y n =
  ℕOrder.≤-trans ℕOrder.≤-sucℕ ℕOrder.≤SumRight

canonical-cosine-respects-metric :
  (x y : RegularCauchy) → x ≈metric y →
  canonicalCosineRegular x ≈metric canonicalCosineRegular y
canonical-cosine-respects-metric x y relation k =
  let stability = operationalUniformCosinePartialSumInputStability
      d = comparisonCosineExponent x y
      k3 = suc (suc (suc k))
      metricDepth = uniformCosineMetricDepth stability d k3
  in
  PT.rec isPropPropTrunc
    (λ { (N , inputBounds) →
      ∣ (ℕ.max N k3 , λ n threshold≤n →
        let N≤n = ℕOrder.≤-trans ℕOrder.left-≤-max threshold≤n
            k3≤n = ℕOrder.≤-trans ℕOrder.right-≤-max threshold≤n
            N≤input = ℕOrder.≤-trans N≤n
              (cosine-comparison-input-depth-above-output x y n)
            input = inputBounds (comparisonCosineInputDepth x y n) N≤input
        in
        canonical-cosine-uniform-pointwise-forward
          stability x y k n k3≤n (fst input) (snd input) ,
        canonical-cosine-uniform-pointwise-backward
          stability x y k n k3≤n (fst input) (snd input)) ∣₁ })
    (relation metricDepth)

canonicalCosineSeriesLiftCertificate :
  ScheduledSeriesLiftCertificate cosinePartialSum
canonicalCosineSeriesLiftCertificate .regularity =
  canonicalCosineScheduledRegularity
canonicalCosineSeriesLiftCertificate .respectsSeriesMetric =
  canonical-cosine-respects-metric

canonicalCosineMetricLift : MetricUnaryLift
canonicalCosineMetricLift =
  metricLiftFromSeriesCertificate canonicalCosineSeriesLiftCertificate

completionCosine : MetricCompletionCandidate → MetricCompletionCandidate
completionCosine = descendMetricUnary canonicalCosineMetricLift

cos : MetricCompletionCandidate → MetricCompletionCandidate
cos = completionCosine

canonicalRationalCosineSeed : (q : Q.ℚ) → CosineTailSeed q
canonicalRationalCosineSeed q =
  uniformCosineTailSeed q
    (canonicalDyadicExponent (constantCauchy q))
    (canonical-cosine-input-approximation-bound (constantCauchy q) 0)

canonical-rational-cosine-shift-path : (q : Q.ℚ) →
  canonicalCosineRegular (constantCauchy q) ≡
  shiftRegular (absorbedCosineRegular
    (canonicalRationalCosineSeed q))
canonical-rational-cosine-shift-path q =
  regularCauchy-ext _ _ (funExt λ n → refl)

canonical-rational-cosine-metric : (q : Q.ℚ) →
  canonicalCosineRegular (constantCauchy q) ≈metric
  absorbedCosineRegular (canonicalRationalCosineSeed q)
canonical-rational-cosine-metric q =
  subst (_≈metric absorbedCosineRegular
    (canonicalRationalCosineSeed q))
    (sym (canonical-rational-cosine-shift-path q))
    (shift-equivalent
      (absorbedCosineRegular (canonicalRationalCosineSeed q)))

completion-cosine-agrees-on-rationals : (q : Q.ℚ) →
  completionCosine (embedMetricℚ q) ≡ rationalCosineValue q
completion-cosine-agrees-on-rationals q =
  SQ.eq/ _ _ (canonical-rational-cosine-metric q) ∙
  sym (rationalCosineValue-from-seed q
    (canonicalRationalCosineSeed q))

operationalCosineTaylorCertificate : CosineTaylorCertificate
operationalCosineTaylorCertificate .cosineSeriesCertificate =
  canonicalCosineSeriesLiftCertificate
operationalCosineTaylorCertificate .cosineAgreesOnRationals =
  completion-cosine-agrees-on-rationals
