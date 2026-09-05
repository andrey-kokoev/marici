{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module OperationalExponentialMetric where

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
open import CanonicalExponentialSchedule
open import CanonicalDyadicallyBoundedCauchy
open import CanonicalExponentialRegularity
open import CanonicalExponentialComparisonSchedule
open import CanonicalExponentialUniformComparison
open import UniformTaylorInputStabilityContract
open import UniformExponentialLateDifference
open import TaylorUniformSeedBounds
open import ExponentialTailSchedule
open import ExponentialSeedConstruction
open import CauchyShift

comparison-input-depth-above-output :
  (x y : RegularCauchy) (n : ℕ) →
  ℕOrder._≤_ n (comparisonExponentialInputDepth x y n)
comparison-input-depth-above-output x y n =
  ℕOrder.≤-trans ℕOrder.≤-sucℕ ℕOrder.≤SumRight

canonical-exponential-respects-metric :
  (x y : RegularCauchy) → x ≈metric y →
  canonicalExponentialRegular x ≈metric canonicalExponentialRegular y
canonical-exponential-respects-metric x y relation k =
  let stability = operationalUniformExponentialPartialSumInputStability
      d = comparisonExponentialExponent x y
      k3 = suc (suc (suc k))
      metricDepth = uniformExponentialMetricDepth stability d k3
  in
  PT.rec isPropPropTrunc
    (λ { (N , inputBounds) →
      ∣ (ℕ.max N k3 , λ n threshold≤n →
        let N≤n = ℕOrder.≤-trans ℕOrder.left-≤-max threshold≤n
            k3≤n = ℕOrder.≤-trans ℕOrder.right-≤-max threshold≤n
            N≤input = ℕOrder.≤-trans N≤n
              (comparison-input-depth-above-output x y n)
            input = inputBounds (comparisonExponentialInputDepth x y n) N≤input
        in
        canonical-exponential-uniform-pointwise-forward
          stability x y k n k3≤n (fst input) (snd input) ,
        canonical-exponential-uniform-pointwise-backward
          stability x y k n k3≤n (fst input) (snd input)) ∣₁ })
    (relation metricDepth)

canonicalExponentialSeriesLiftCertificate :
  ScheduledSeriesLiftCertificate exponentialPartialSum
canonicalExponentialSeriesLiftCertificate .regularity =
  canonicalExponentialScheduledRegularity
canonicalExponentialSeriesLiftCertificate .respectsSeriesMetric =
  canonical-exponential-respects-metric

canonicalExponentialMetricLift : MetricUnaryLift
canonicalExponentialMetricLift =
  metricLiftFromSeriesCertificate canonicalExponentialSeriesLiftCertificate

completionExponential : MetricCompletionCandidate → MetricCompletionCandidate
completionExponential = descendMetricUnary canonicalExponentialMetricLift

exp : MetricCompletionCandidate → MetricCompletionCandidate
exp = completionExponential

canonicalRationalExponentialSeed : (q : Q.ℚ) → ExponentialTailSeed q
canonicalRationalExponentialSeed q =
  uniformExponentialTailSeed q
    (canonicalDyadicExponent (constantCauchy q))
    (canonical-input-approximation-bound (constantCauchy q) 0)

canonical-rational-exponential-shift-path : (q : Q.ℚ) →
  canonicalExponentialRegular (constantCauchy q) ≡
  shiftRegular (absorbedExponentialRegular
    (canonicalRationalExponentialSeed q))
canonical-rational-exponential-shift-path q =
  regularCauchy-ext _ _ (funExt λ n → refl)

canonical-rational-exponential-metric : (q : Q.ℚ) →
  canonicalExponentialRegular (constantCauchy q) ≈metric
  absorbedExponentialRegular (canonicalRationalExponentialSeed q)
canonical-rational-exponential-metric q =
  subst (_≈metric absorbedExponentialRegular
    (canonicalRationalExponentialSeed q))
    (sym (canonical-rational-exponential-shift-path q))
    (shift-equivalent
      (absorbedExponentialRegular (canonicalRationalExponentialSeed q)))

completion-exponential-agrees-on-rationals : (q : Q.ℚ) →
  completionExponential (embedMetricℚ q) ≡ rationalExponentialValue q
completion-exponential-agrees-on-rationals q =
  SQ.eq/ _ _ (canonical-rational-exponential-metric q) ∙
  sym (rationalExponentialValue-from-seed q
    (canonicalRationalExponentialSeed q))

operationalExponentialTaylorCertificate : ExponentialTaylorCertificate
operationalExponentialTaylorCertificate .exponentialSeriesCertificate =
  canonicalExponentialSeriesLiftCertificate
operationalExponentialTaylorCertificate .exponentialAgreesOnRationals =
  completion-exponential-agrees-on-rationals
