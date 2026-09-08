{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module BoundedExponentialModulus where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ; suc)
import Cubical.Data.Nat.Order as NatOrder
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.HITs.PropositionalTruncation as PT
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CanonicalExponentialRegularity
open import CanonicalExponentialComparisonSchedule
open import UniformTaylorInputStabilityContract
open import UniformExponentialLateDifference
open import ExponentialPairwiseContinuity
open import AbsoluteTaylorSeriesMultiplication using
  (finitePrefixMaximum; finitePrefixMaximumDominates)

weakenEventuallyWithinDepth : (x y : RegularCauchy) (small large : ℕ) →
  NatOrder._≤_ small large → EventuallyWithin x y large → EventuallyWithin x y small
weakenEventuallyWithinDepth x y small large small≤large =
  PT.map λ { (N , bounds) → N , λ n N≤n →
    isTrans≤ (approximation x n) (approximation y n Q.+ precision large)
      (approximation y n Q.+ precision small) (fst (bounds n N≤n))
      (≤-o+ (precision large) (precision small) (approximation y n)
        (precision-antitone small large small≤large)) ,
    isTrans≤ (approximation y n) (approximation x n Q.+ precision large)
      (approximation x n Q.+ precision small) (snd (bounds n N≤n))
      (≤-o+ (precision large) (precision small) (approximation x n)
        (precision-antitone small large small≤large)) }

boundedExponentialDepth : ℕ → ℕ → ℕ
boundedExponentialDepth D k = finitePrefixMaximum
  (λ d → uniformExponentialMetricDepth
    operationalUniformExponentialPartialSumInputStability d (suc (suc (suc k)))) D

boundedExponentialEventuallyWithin : (x y : RegularCauchy) (D k : ℕ) →
  NatOrder._≤_ (comparisonExponentialExponent x y) D →
  EventuallyWithin x y (boundedExponentialDepth D k) →
  EventuallyWithin (canonicalExponentialRegular x) (canonicalExponentialRegular y) k
boundedExponentialEventuallyWithin x y D k exponentBound input =
  exponentialPairEventuallyWithin x y k
    (weakenEventuallyWithinDepth x y (exponentialPairDepth x y k)
      (boundedExponentialDepth D k)
      (finitePrefixMaximumDominates
        (λ d → uniformExponentialMetricDepth
          operationalUniformExponentialPartialSumInputStability d
          (suc (suc (suc k))))
        D (comparisonExponentialExponent x y) exponentBound)
      input)
