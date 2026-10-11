{-# OPTIONS --safe --cubical --guardedness #-}
module TickTrigPartialSumTransfer where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as N using (ℕ; zero; suc)
import Cubical.Data.Nat.Order as NO
open import Cubical.Data.Rationals as Q
open import Cubical.HITs.PropositionalTruncation as PT
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyQuantitativeContinuity using (composeEventuallyWithin; eventuallyWithin-sym)
open import CauchyRationalDensity using (rational-approximation-dense; eventuallyWithin-weaken)
open import CauchyProductBounds
open import TaylorRegularityComposition using (magnitude-bound-forward; magnitude-bound-backward)
open import CanonicalDyadicallyBoundedCauchy using (canonicalDyadicExponent)
open import CanonicalCosineRegularity
open import CanonicalSineRegularity
open import CanonicalCosineSchedule
open import CanonicalSineSchedule
open import RationalTaylorApproximants using (cosinePartialSum)
open import RationalSineTaylorApproximants using (sinePartialSum)
open import OperationalCosineMetric using (completionCosine)
open import OperationalSineMetric using (completionSine)
import CanonicalCosineComparisonSchedule as CC
import CanonicalSineComparisonSchedule as SC
open import TickCompletionMetric using (CompletionWithin; within-intro)
-- Keep the finite addition estimates in this checkpoint's dependency closure.
import TickTrigAdditionResidual

constant-difference-eventual : (a b : Q.ℚ) (k : ℕ) →
  MagnitudeBound (a Q.+ (Q.- b)) (precision k) → EventuallyWithin (constantCauchy a) (constantCauchy b) k
constant-difference-eventual a b k h = ∣ zero , (λ n hn →
  magnitude-bound-forward a b (precision k) h , magnitude-bound-backward a b (precision k) h) ∣₁

-- Compare an arbitrary later cutoff with one native sample, then with the
-- actual regular sequence. No replacement trigonometric backend is defined.
later-partial-to-regular : (x : RegularCauchy) (value : Q.ℚ) (k : ℕ) →
  MagnitudeBound (value Q.+ (Q.- approximation x (suc (suc k)))) (precision (suc (suc (suc k)))) →
  EventuallyWithin x (constantCauchy value) k
later-partial-to-regular x value k h = composeEventuallyWithin x center (constantCauchy value) k
  (eventuallyWithin-sym center x (suc k) (rational-approximation-dense x (suc k)))
  (eventuallyWithin-weaken center (constantCauchy value) (suc k) (suc (suc (suc k)))
    (NO.≤-trans NO.≤-sucℕ NO.≤-sucℕ)
    (eventuallyWithin-sym (constantCauchy value) center (suc (suc (suc k)))
      (constant-difference-eventual value (approximation x (suc (suc k))) (suc (suc (suc k))) h)))
  where
  center : RegularCauchy
  center = constantCauchy (approximation x (suc (suc k)))

cosineTransferCutoff sineTransferCutoff : Q.ℚ → ℕ → ℕ
cosineTransferCutoff q k = canonicalCosineSeriesDepth (constantCauchy q) (suc (suc k))
sineTransferCutoff q k = canonicalSineSeriesDepth (constantCauchy q) (suc (suc k))

abstract
  cosine-partial-sum-to-operational : (q : Q.ℚ) (k n : ℕ) → NO._≤_ (cosineTransferCutoff q k) n →
    CompletionWithin (completionCosine (embedMetricℚ q)) (embedMetricℚ (cosinePartialSum q n)) k
  cosine-partial-sum-to-operational q k n hn =
    within-intro (canonicalCosineRegular (constantCauchy q)) (constantCauchy (cosinePartialSum q n)) k
      (later-partial-to-regular (canonicalCosineRegular (constantCauchy q)) (cosinePartialSum q n) k
        (CC.common-series-extension-bound q (canonicalDyadicExponent (constantCauchy q)) (suc (suc k)) n
          (canonical-cosine-input-approximation-bound (constantCauchy q) zero) hn))

  sine-partial-sum-to-operational : (q : Q.ℚ) (k n : ℕ) → NO._≤_ (sineTransferCutoff q k) n →
    CompletionWithin (completionSine (embedMetricℚ q)) (embedMetricℚ (sinePartialSum q n)) k
  sine-partial-sum-to-operational q k n hn =
    within-intro (canonicalSineRegular (constantCauchy q)) (constantCauchy (sinePartialSum q n)) k
      (later-partial-to-regular (canonicalSineRegular (constantCauchy q)) (sinePartialSum q n) k
        (SC.sine-common-series-extension-bound q (canonicalDyadicExponent (constantCauchy q)) (suc (suc k)) n
          (canonical-sine-input-approximation-bound (constantCauchy q) zero) hn))
