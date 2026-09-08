{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module ExponentialPairwiseContinuity where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; suc; max)
import Cubical.Data.Nat.Order as ℕOrder
open import Cubical.HITs.PropositionalTruncation as PT
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CanonicalExponentialRegularity
open import CanonicalExponentialComparisonSchedule
open import CanonicalExponentialUniformComparison
open import UniformTaylorInputStabilityContract
open import UniformExponentialLateDifference
open import OperationalExponentialMetric using (comparison-input-depth-above-output)

exponentialPairDepth : RegularCauchy → RegularCauchy → ℕ → ℕ
exponentialPairDepth x y k =
  uniformExponentialMetricDepth operationalUniformExponentialPartialSumInputStability
    (comparisonExponentialExponent x y) (suc (suc (suc k)))

exponentialPairEventuallyWithin : (x y : RegularCauchy) (k : ℕ) →
  EventuallyWithin x y (exponentialPairDepth x y k) →
  EventuallyWithin (canonicalExponentialRegular x) (canonicalExponentialRegular y) k
exponentialPairEventuallyWithin x y k inputRelation =
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
          operationalUniformExponentialPartialSumInputStability
          x y k n k3≤n (fst input) (snd input) ,
        canonical-exponential-uniform-pointwise-backward
          operationalUniformExponentialPartialSumInputStability
          x y k n k3≤n (fst input) (snd input)) ∣₁ })
    inputRelation
  where
  k3 = suc (suc (suc k))
