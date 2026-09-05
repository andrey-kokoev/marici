{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CanonicalCosineRegularity where

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
open import CosineTailSchedule
open import UniformCosineSeedBounds
open import CosinePartialSumInputDifference
open import CanonicalCosineSchedule
open import TaylorRegularityComposition
open import TaylorLiftContract

canonical-cosine-ordered-close-forward :
  (x : RegularCauchy) (m n : ℕ) → ℕOrder._≤_ m n →
  scheduledSeriesApproximation cosinePartialSum
    (canonicalCosineTaylorSchedule x) x m ≤
  (scheduledSeriesApproximation cosinePartialSum
    (canonicalCosineTaylorSchedule x) x n Q.+ precision m) Q.+ precision n
canonical-cosine-ordered-close-forward x m n m≤n =
  let d = canonicalDyadicExponent x
      inputM = canonicalCosineInputDepth x m
      inputN = canonicalCosineInputDepth x n
      seriesM = canonicalCosineSeriesDepth x m
      qM = approximation x inputM
      qN = approximation x inputN
      qMBound = canonical-cosine-input-approximation-bound x inputM
      qNBound = canonical-cosine-input-approximation-bound x inputN
      inputError = precision inputM Q.+ precision inputN
      inputDifference = cauchy-difference-bound x inputM inputN
      rawInputBound = cosine-partial-sum-input-difference-bound
        qM qN inputError d seriesM
        (precision-sum-nonnegative inputM inputN)
        qMBound qNBound inputDifference
      inputBound = weaken-magnitude-bound _ _
        (precision (suc m) Q.+ precision (suc n))
        (canonical-cosine-paired-input-error-bound x m n m≤n)
        rawInputBound
      inputDirected = single-difference-bound→directed
        (cosinePartialSum qM seriesM)
        (cosinePartialSum qN seriesM)
        (precision (suc m) Q.+ precision (suc n))
        (positive-upper inputBound)
      seedN = uniformCosineTailSeed qN d qNBound
      tailDirected = absorbed-cosine-close-forward seedN (suc m) (suc n)
  in
  compose-half-precision-pairs
    (cosinePartialSum qM seriesM)
    (cosinePartialSum qN seriesM)
    (cosinePartialSum qN (canonicalCosineSeriesDepth x n))
    m n inputDirected tailDirected

canonical-cosine-ordered-close-backward :
  (x : RegularCauchy) (m n : ℕ) → ℕOrder._≤_ m n →
  scheduledSeriesApproximation cosinePartialSum
    (canonicalCosineTaylorSchedule x) x n ≤
  (scheduledSeriesApproximation cosinePartialSum
    (canonicalCosineTaylorSchedule x) x m Q.+ precision m) Q.+ precision n
canonical-cosine-ordered-close-backward x m n m≤n =
  let d = canonicalDyadicExponent x
      inputM = canonicalCosineInputDepth x m
      inputN = canonicalCosineInputDepth x n
      seriesM = canonicalCosineSeriesDepth x m
      seriesN = canonicalCosineSeriesDepth x n
      qM = approximation x inputM
      qN = approximation x inputN
      qMBound = canonical-cosine-input-approximation-bound x inputM
      qNBound = canonical-cosine-input-approximation-bound x inputN
      inputError = precision inputM Q.+ precision inputN
      inputDifference = cauchy-difference-bound x inputM inputN
      rawInputBound = cosine-partial-sum-input-difference-bound
        qM qN inputError d seriesM
        (precision-sum-nonnegative inputM inputN)
        qMBound qNBound inputDifference
      inputBound = weaken-magnitude-bound _ _
        (precision (suc m) Q.+ precision (suc n))
        (canonical-cosine-paired-input-error-bound x m n m≤n)
        rawInputBound
      inputReverseDifference = subst
        (_≤ precision (suc m) Q.+ precision (suc n))
        (CauchyProductRegularity.DirectedPaths.reverse-difference
          PreferredℚCommRing
          (cosinePartialSum qM seriesM)
          (cosinePartialSum qN seriesM))
        (negative-upper inputBound)
      inputDirectedRaw = difference-upper→directed
        (cosinePartialSum qN seriesM)
        (cosinePartialSum qM seriesM)
        (precision (suc m)) (precision (suc n))
        inputReverseDifference
      inputDirected = inputDirectedRaw
      seedN = uniformCosineTailSeed qN d qNBound
      tailDirectedRaw = close-backward (absorbedCosineRegular seedN)
        (suc m) (suc n)
      tailDirected = subst
        (cosinePartialSum qN seriesN ≤_)
        (sym (Q.+Assoc
          (cosinePartialSum qN seriesM)
          (precision (suc m)) (precision (suc n))))
        tailDirectedRaw
  in
  compose-half-precision-pairs
    (cosinePartialSum qN seriesN)
    (cosinePartialSum qN seriesM)
    (cosinePartialSum qM seriesM)
    m n tailDirected inputDirected

canonical-cosine-close-forward :
  (x : RegularCauchy) (m n : ℕ) →
  scheduledSeriesApproximation cosinePartialSum
    (canonicalCosineTaylorSchedule x) x m ≤
  (scheduledSeriesApproximation cosinePartialSum
    (canonicalCosineTaylorSchedule x) x n Q.+ precision m) Q.+ precision n
canonical-cosine-close-forward x m n with ℕOrder.splitℕ-≤ m n
... | inl m≤n = canonical-cosine-ordered-close-forward x m n m≤n
... | inr n≤m =
  subst
    (scheduledSeriesApproximation cosinePartialSum
      (canonicalCosineTaylorSchedule x) x m ≤_)
    (CosineSchedulePaths.swap-errors PreferredℚCommRing
      (scheduledSeriesApproximation cosinePartialSum
        (canonicalCosineTaylorSchedule x) x n)
      (precision m) (precision n))
    (canonical-cosine-ordered-close-backward x n m
      (ℕOrder.≤-trans ℕOrder.≤-sucℕ n≤m))

canonical-cosine-close-backward :
  (x : RegularCauchy) (m n : ℕ) →
  scheduledSeriesApproximation cosinePartialSum
    (canonicalCosineTaylorSchedule x) x n ≤
  (scheduledSeriesApproximation cosinePartialSum
    (canonicalCosineTaylorSchedule x) x m Q.+ precision m) Q.+ precision n
canonical-cosine-close-backward x m n with ℕOrder.splitℕ-≤ m n
... | inl m≤n = canonical-cosine-ordered-close-backward x m n m≤n
... | inr n≤m =
  subst
    (scheduledSeriesApproximation cosinePartialSum
      (canonicalCosineTaylorSchedule x) x n ≤_)
    (CosineSchedulePaths.swap-errors PreferredℚCommRing
      (scheduledSeriesApproximation cosinePartialSum
        (canonicalCosineTaylorSchedule x) x m)
      (precision m) (precision n))
    (canonical-cosine-ordered-close-forward x n m
      (ℕOrder.≤-trans ℕOrder.≤-sucℕ n≤m))

canonicalCosineScheduledRegularity :
  ScheduledSeriesRegularity cosinePartialSum
canonicalCosineScheduledRegularity .scheduleFor =
  canonicalCosineTaylorSchedule
canonicalCosineScheduledRegularity .closeSeriesForward =
  canonical-cosine-close-forward
canonicalCosineScheduledRegularity .closeSeriesBackward =
  canonical-cosine-close-backward

canonicalCosineRegular : RegularCauchy → RegularCauchy
canonicalCosineRegular =
  scheduledSeriesRegular canonicalCosineScheduledRegularity
