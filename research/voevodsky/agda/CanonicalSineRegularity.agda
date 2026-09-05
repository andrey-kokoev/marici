{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CanonicalSineRegularity where

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
open import RationalSineTaylorApproximants
open import SineTailSchedule
open import UniformSineSeedBounds
open import SinePartialSumInputDifference
open import CanonicalSineSchedule
open import TaylorRegularityComposition
open import TaylorLiftContract

canonical-sine-ordered-close-forward :
  (x : RegularCauchy) (m n : ℕ) → ℕOrder._≤_ m n →
  scheduledSeriesApproximation sinePartialSum
    (canonicalSineTaylorSchedule x) x m ≤
  (scheduledSeriesApproximation sinePartialSum
    (canonicalSineTaylorSchedule x) x n Q.+ precision m) Q.+ precision n
canonical-sine-ordered-close-forward x m n m≤n =
  let d = canonicalDyadicExponent x
      inputM = canonicalSineInputDepth x m
      inputN = canonicalSineInputDepth x n
      seriesM = canonicalSineSeriesDepth x m
      qM = approximation x inputM
      qN = approximation x inputN
      qMBound = canonical-sine-input-approximation-bound x inputM
      qNBound = canonical-sine-input-approximation-bound x inputN
      inputError = precision inputM Q.+ precision inputN
      inputDifference = cauchy-difference-bound x inputM inputN
      rawInputBound = sine-partial-sum-input-difference-bound
        qM qN inputError d seriesM
        (precision-sum-nonnegative inputM inputN)
        qMBound qNBound inputDifference
      inputBound = weaken-magnitude-bound _ _
        (precision (suc m) Q.+ precision (suc n))
        (canonical-sine-paired-input-error-bound x m n m≤n)
        rawInputBound
      inputDirected = single-difference-bound→directed
        (sinePartialSum qM seriesM)
        (sinePartialSum qN seriesM)
        (precision (suc m) Q.+ precision (suc n))
        (positive-upper inputBound)
      seedN = uniformSineTailSeed qN d qNBound
      tailDirected = absorbed-sine-close-forward seedN (suc m) (suc n)
  in
  compose-half-precision-pairs
    (sinePartialSum qM seriesM)
    (sinePartialSum qN seriesM)
    (sinePartialSum qN (canonicalSineSeriesDepth x n))
    m n inputDirected tailDirected

canonical-sine-ordered-close-backward :
  (x : RegularCauchy) (m n : ℕ) → ℕOrder._≤_ m n →
  scheduledSeriesApproximation sinePartialSum
    (canonicalSineTaylorSchedule x) x n ≤
  (scheduledSeriesApproximation sinePartialSum
    (canonicalSineTaylorSchedule x) x m Q.+ precision m) Q.+ precision n
canonical-sine-ordered-close-backward x m n m≤n =
  let d = canonicalDyadicExponent x
      inputM = canonicalSineInputDepth x m
      inputN = canonicalSineInputDepth x n
      seriesM = canonicalSineSeriesDepth x m
      seriesN = canonicalSineSeriesDepth x n
      qM = approximation x inputM
      qN = approximation x inputN
      qMBound = canonical-sine-input-approximation-bound x inputM
      qNBound = canonical-sine-input-approximation-bound x inputN
      inputError = precision inputM Q.+ precision inputN
      inputDifference = cauchy-difference-bound x inputM inputN
      rawInputBound = sine-partial-sum-input-difference-bound
        qM qN inputError d seriesM
        (precision-sum-nonnegative inputM inputN)
        qMBound qNBound inputDifference
      inputBound = weaken-magnitude-bound _ _
        (precision (suc m) Q.+ precision (suc n))
        (canonical-sine-paired-input-error-bound x m n m≤n)
        rawInputBound
      inputReverseDifference = subst
        (_≤ precision (suc m) Q.+ precision (suc n))
        (CauchyProductRegularity.DirectedPaths.reverse-difference
          PreferredℚCommRing
          (sinePartialSum qM seriesM)
          (sinePartialSum qN seriesM))
        (negative-upper inputBound)
      inputDirectedRaw = difference-upper→directed
        (sinePartialSum qN seriesM)
        (sinePartialSum qM seriesM)
        (precision (suc m)) (precision (suc n))
        inputReverseDifference
      inputDirected = inputDirectedRaw
      seedN = uniformSineTailSeed qN d qNBound
      tailDirectedRaw = close-backward (absorbedSineRegular seedN)
        (suc m) (suc n)
      tailDirected = subst
        (sinePartialSum qN seriesN ≤_)
        (sym (Q.+Assoc
          (sinePartialSum qN seriesM)
          (precision (suc m)) (precision (suc n))))
        tailDirectedRaw
  in
  compose-half-precision-pairs
    (sinePartialSum qN seriesN)
    (sinePartialSum qN seriesM)
    (sinePartialSum qM seriesM)
    m n tailDirected inputDirected

canonical-sine-close-forward :
  (x : RegularCauchy) (m n : ℕ) →
  scheduledSeriesApproximation sinePartialSum
    (canonicalSineTaylorSchedule x) x m ≤
  (scheduledSeriesApproximation sinePartialSum
    (canonicalSineTaylorSchedule x) x n Q.+ precision m) Q.+ precision n
canonical-sine-close-forward x m n with ℕOrder.splitℕ-≤ m n
... | inl m≤n = canonical-sine-ordered-close-forward x m n m≤n
... | inr n≤m =
  subst
    (scheduledSeriesApproximation sinePartialSum
      (canonicalSineTaylorSchedule x) x m ≤_)
    (SineSchedulePaths.swap-errors PreferredℚCommRing
      (scheduledSeriesApproximation sinePartialSum
        (canonicalSineTaylorSchedule x) x n)
      (precision m) (precision n))
    (canonical-sine-ordered-close-backward x n m
      (ℕOrder.≤-trans ℕOrder.≤-sucℕ n≤m))

canonical-sine-close-backward :
  (x : RegularCauchy) (m n : ℕ) →
  scheduledSeriesApproximation sinePartialSum
    (canonicalSineTaylorSchedule x) x n ≤
  (scheduledSeriesApproximation sinePartialSum
    (canonicalSineTaylorSchedule x) x m Q.+ precision m) Q.+ precision n
canonical-sine-close-backward x m n with ℕOrder.splitℕ-≤ m n
... | inl m≤n = canonical-sine-ordered-close-backward x m n m≤n
... | inr n≤m =
  subst
    (scheduledSeriesApproximation sinePartialSum
      (canonicalSineTaylorSchedule x) x n ≤_)
    (SineSchedulePaths.swap-errors PreferredℚCommRing
      (scheduledSeriesApproximation sinePartialSum
        (canonicalSineTaylorSchedule x) x m)
      (precision m) (precision n))
    (canonical-sine-ordered-close-forward x n m
      (ℕOrder.≤-trans ℕOrder.≤-sucℕ n≤m))

canonicalSineScheduledRegularity :
  ScheduledSeriesRegularity sinePartialSum
canonicalSineScheduledRegularity .scheduleFor =
  canonicalSineTaylorSchedule
canonicalSineScheduledRegularity .closeSeriesForward =
  canonical-sine-close-forward
canonicalSineScheduledRegularity .closeSeriesBackward =
  canonical-sine-close-backward

canonicalSineRegular : RegularCauchy → RegularCauchy
canonicalSineRegular =
  scheduledSeriesRegular canonicalSineScheduledRegularity
