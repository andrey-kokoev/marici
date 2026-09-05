{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CanonicalExponentialRegularity where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; suc)
import Cubical.Data.Nat.Order as ℕOrder
open import Cubical.Data.Sum
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import RegularCauchyStructure
open import CauchyProductBounds
open import CauchyProductErrorBounds
open import CauchyProductCongruence using (single-difference-bound→directed)
open import CauchyProductRegularity using (difference-upper→directed)
open import Cubical.Algebra.CommRing
open import RationalAnalyticSubstrate
open import DyadicallyBoundedCauchy
open import CanonicalDyadicallyBoundedCauchy
open import RationalTaylorApproximants
open import ExponentialTailSchedule
open import TaylorUniformSeedBounds
open import TaylorPartialSumInputDifference
open import CanonicalExponentialSchedule
open import TaylorRegularityComposition
open import TaylorLiftContract

canonical-exponential-ordered-close-forward :
  (x : RegularCauchy) (m n : ℕ) → ℕOrder._≤_ m n →
  scheduledSeriesApproximation exponentialPartialSum
    (canonicalExponentialTaylorSchedule x) x m ≤
  (scheduledSeriesApproximation exponentialPartialSum
    (canonicalExponentialTaylorSchedule x) x n Q.+ precision m) Q.+ precision n
canonical-exponential-ordered-close-forward x m n m≤n =
  let d = canonicalDyadicExponent x
      inputM = canonicalExponentialInputDepth x m
      inputN = canonicalExponentialInputDepth x n
      seriesM = canonicalExponentialSeriesDepth x m
      qM = approximation x inputM
      qN = approximation x inputN
      qMBound = canonical-input-approximation-bound x inputM
      qNBound = canonical-input-approximation-bound x inputN
      inputError = precision inputM Q.+ precision inputN
      inputDifference = cauchy-difference-bound x inputM inputN
      rawInputBound = exponential-partial-sum-input-difference-bound
        qM qN inputError d seriesM
        (precision-sum-nonnegative inputM inputN)
        qMBound qNBound inputDifference
      inputBound = weaken-magnitude-bound _ _
        (precision (suc m) Q.+ precision (suc n))
        (canonical-exponential-paired-input-error-bound x m n m≤n)
        rawInputBound
      inputDirected = single-difference-bound→directed
        (exponentialPartialSum qM seriesM)
        (exponentialPartialSum qN seriesM)
        (precision (suc m) Q.+ precision (suc n))
        (positive-upper inputBound)
      seedN = uniformExponentialTailSeed qN d qNBound
      tailDirected = absorbed-partial-sum-close-forward seedN (suc m) (suc n)
  in
  compose-half-precision-pairs
    (exponentialPartialSum qM seriesM)
    (exponentialPartialSum qN seriesM)
    (exponentialPartialSum qN (canonicalExponentialSeriesDepth x n))
    m n inputDirected tailDirected

canonical-exponential-ordered-close-backward :
  (x : RegularCauchy) (m n : ℕ) → ℕOrder._≤_ m n →
  scheduledSeriesApproximation exponentialPartialSum
    (canonicalExponentialTaylorSchedule x) x n ≤
  (scheduledSeriesApproximation exponentialPartialSum
    (canonicalExponentialTaylorSchedule x) x m Q.+ precision m) Q.+ precision n
canonical-exponential-ordered-close-backward x m n m≤n =
  let d = canonicalDyadicExponent x
      inputM = canonicalExponentialInputDepth x m
      inputN = canonicalExponentialInputDepth x n
      seriesM = canonicalExponentialSeriesDepth x m
      seriesN = canonicalExponentialSeriesDepth x n
      qM = approximation x inputM
      qN = approximation x inputN
      qMBound = canonical-input-approximation-bound x inputM
      qNBound = canonical-input-approximation-bound x inputN
      inputError = precision inputM Q.+ precision inputN
      inputDifference = cauchy-difference-bound x inputM inputN
      rawInputBound = exponential-partial-sum-input-difference-bound
        qM qN inputError d seriesM
        (precision-sum-nonnegative inputM inputN)
        qMBound qNBound inputDifference
      inputBound = weaken-magnitude-bound _ _
        (precision (suc m) Q.+ precision (suc n))
        (canonical-exponential-paired-input-error-bound x m n m≤n)
        rawInputBound
      inputReverseDifference = subst
        (_≤ precision (suc m) Q.+ precision (suc n))
        (CauchyProductRegularity.DirectedPaths.reverse-difference
          PreferredℚCommRing
          (exponentialPartialSum qM seriesM)
          (exponentialPartialSum qN seriesM))
        (negative-upper inputBound)
      inputDirectedRaw = difference-upper→directed
        (exponentialPartialSum qN seriesM)
        (exponentialPartialSum qM seriesM)
        (precision (suc m)) (precision (suc n))
        inputReverseDifference
      inputDirected = inputDirectedRaw
      seedN = uniformExponentialTailSeed qN d qNBound
      tailDirectedRaw = close-backward (absorbedExponentialRegular seedN)
        (suc m) (suc n)
      tailDirected = subst
        (exponentialPartialSum qN seriesN ≤_)
        (sym (Q.+Assoc
          (exponentialPartialSum qN seriesM)
          (precision (suc m)) (precision (suc n))))
        tailDirectedRaw
  in
  compose-half-precision-pairs
    (exponentialPartialSum qN seriesN)
    (exponentialPartialSum qN seriesM)
    (exponentialPartialSum qM seriesM)
    m n tailDirected inputDirected

canonical-exponential-close-forward :
  (x : RegularCauchy) (m n : ℕ) →
  scheduledSeriesApproximation exponentialPartialSum
    (canonicalExponentialTaylorSchedule x) x m ≤
  (scheduledSeriesApproximation exponentialPartialSum
    (canonicalExponentialTaylorSchedule x) x n Q.+ precision m) Q.+ precision n
canonical-exponential-close-forward x m n with ℕOrder.splitℕ-≤ m n
... | inl m≤n = canonical-exponential-ordered-close-forward x m n m≤n
... | inr n≤m =
  subst
    (scheduledSeriesApproximation exponentialPartialSum
      (canonicalExponentialTaylorSchedule x) x m ≤_)
    (ExponentialSchedulePaths.swap-errors PreferredℚCommRing
      (scheduledSeriesApproximation exponentialPartialSum
        (canonicalExponentialTaylorSchedule x) x n)
      (precision m) (precision n))
    (canonical-exponential-ordered-close-backward x n m
      (ℕOrder.≤-trans ℕOrder.≤-sucℕ n≤m))

canonical-exponential-close-backward :
  (x : RegularCauchy) (m n : ℕ) →
  scheduledSeriesApproximation exponentialPartialSum
    (canonicalExponentialTaylorSchedule x) x n ≤
  (scheduledSeriesApproximation exponentialPartialSum
    (canonicalExponentialTaylorSchedule x) x m Q.+ precision m) Q.+ precision n
canonical-exponential-close-backward x m n with ℕOrder.splitℕ-≤ m n
... | inl m≤n = canonical-exponential-ordered-close-backward x m n m≤n
... | inr n≤m =
  subst
    (scheduledSeriesApproximation exponentialPartialSum
      (canonicalExponentialTaylorSchedule x) x n ≤_)
    (ExponentialSchedulePaths.swap-errors PreferredℚCommRing
      (scheduledSeriesApproximation exponentialPartialSum
        (canonicalExponentialTaylorSchedule x) x m)
      (precision m) (precision n))
    (canonical-exponential-ordered-close-forward x n m
      (ℕOrder.≤-trans ℕOrder.≤-sucℕ n≤m))

canonicalExponentialScheduledRegularity :
  ScheduledSeriesRegularity exponentialPartialSum
canonicalExponentialScheduledRegularity .scheduleFor =
  canonicalExponentialTaylorSchedule
canonicalExponentialScheduledRegularity .closeSeriesForward =
  canonical-exponential-close-forward
canonicalExponentialScheduledRegularity .closeSeriesBackward =
  canonical-exponential-close-backward

canonicalExponentialRegular : RegularCauchy → RegularCauchy
canonicalExponentialRegular =
  scheduledSeriesRegular canonicalExponentialScheduledRegularity
