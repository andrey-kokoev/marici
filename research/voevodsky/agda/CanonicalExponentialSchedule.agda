{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CanonicalExponentialSchedule where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; suc; _+_)
import Cubical.Data.Nat.Order as ℕOrder
open import Cubical.Data.Rationals as Q
open import RegularCauchyStructure
open import Cubical.Data.Rationals.Order
open import CauchyProductBounds
open import CauchyProductErrorBounds
open import DyadicallyBoundedCauchy
open import CanonicalDyadicallyBoundedCauchy
open import RationalTaylorApproximants
open import TaylorUniformSeedBounds
open import TaylorPartialSumInputDifference
open import TaylorScheduleMonotonicity

canonicalExponentialSeriesDepth : RegularCauchy → ℕ → ℕ
canonicalExponentialSeriesDepth x n =
  uniformExponentialCutoff (canonicalDyadicExponent x) (suc n)

canonicalExponentialInputScale : RegularCauchy → ℕ → ℕ
canonicalExponentialInputScale x n =
  partialSumDifferenceExponent
    (canonicalDyadicExponent x)
    (canonicalExponentialSeriesDepth x n)

canonicalExponentialInputDepth : RegularCauchy → ℕ → ℕ
canonicalExponentialInputDepth x n =
  canonicalExponentialInputScale x n ℕ.+ suc n

canonicalExponentialTaylorSchedule :
  RegularCauchy → TaylorCutoffSchedule
canonicalExponentialTaylorSchedule x .input-depth =
  canonicalExponentialInputDepth x
canonicalExponentialTaylorSchedule x .series-depth =
  canonicalExponentialSeriesDepth x

canonical-exponential-series-depth-formula :
  (x : RegularCauchy) (n : ℕ) →
  series-depth (canonicalExponentialTaylorSchedule x) n ≡
  uniformExponentialCutoff (canonicalDyadicExponent x) (suc n)
canonical-exponential-series-depth-formula x n = refl

canonical-exponential-input-depth-formula :
  (x : RegularCauchy) (n : ℕ) →
  input-depth (canonicalExponentialTaylorSchedule x) n ≡
  canonicalExponentialInputScale x n ℕ.+ suc n
canonical-exponential-input-depth-formula x n = refl

canonical-input-approximation-bound :
  (x : RegularCauchy) (n : ℕ) →
  MagnitudeBound
    (approximation x n)
    (dyadicRadius (canonicalDyadicExponent x))
canonical-input-approximation-bound x n =
  bounded-value (canonicalDyadicallyBounded x) n

canonical-exponential-input-error-cancels :
  (x : RegularCauchy) (n : ℕ) →
  dyadicRadius (canonicalExponentialInputScale x n) Q.·
  precision (canonicalExponentialInputDepth x n) ≡ precision (suc n)
canonical-exponential-input-error-cancels x n =
  radius-cancels-precision-shift
    (canonicalExponentialInputScale x n) (suc n)

canonical-exponential-series-depth-monotone :
  (x : RegularCauchy) (m n : ℕ) → ℕOrder._≤_ m n →
  ℕOrder._≤_ (canonicalExponentialSeriesDepth x m)
    (canonicalExponentialSeriesDepth x n)
canonical-exponential-series-depth-monotone x m n m≤n =
  uniformExponentialCutoff-monotone (canonicalDyadicExponent x)
    (suc m) (suc n) (ℕOrder.suc-≤-suc m≤n)

canonical-exponential-input-scale-monotone :
  (x : RegularCauchy) (m n : ℕ) → ℕOrder._≤_ m n →
  ℕOrder._≤_ (canonicalExponentialInputScale x m)
    (canonicalExponentialInputScale x n)
canonical-exponential-input-scale-monotone x m n m≤n =
  partialSumDifferenceExponent-monotone
    (canonicalDyadicExponent x)
    (canonicalExponentialSeriesDepth x m)
    (canonicalExponentialSeriesDepth x n)
    (canonical-exponential-series-depth-monotone x m n m≤n)

canonical-exponential-input-depth-monotone :
  (x : RegularCauchy) (m n : ℕ) → ℕOrder._≤_ m n →
  ℕOrder._≤_ (canonicalExponentialInputDepth x m)
    (canonicalExponentialInputDepth x n)
canonical-exponential-input-depth-monotone x m n m≤n =
  ℕOrder.≤-+-≤
    (canonical-exponential-input-scale-monotone x m n m≤n)
    (ℕOrder.suc-≤-suc m≤n)

canonical-exponential-later-input-error-bound :
  (x : RegularCauchy) (m n : ℕ) → ℕOrder._≤_ m n →
  dyadicRadius (canonicalExponentialInputScale x m) Q.·
    precision (canonicalExponentialInputDepth x n) ≤ precision (suc n)
canonical-exponential-later-input-error-bound x m n m≤n =
  let scaleM = canonicalExponentialInputScale x m
      scaleN = canonicalExponentialInputScale x n
      inputN = canonicalExponentialInputDepth x n
      scale≤ = dyadicRadius-monotone scaleM scaleN
        (canonical-exponential-input-scale-monotone x m n m≤n)
  in
  subst ((dyadicRadius scaleM Q.· precision inputN) ≤_)
    (canonical-exponential-input-error-cancels x n)
    (≤-·o (dyadicRadius scaleM) (dyadicRadius scaleN)
      (precision inputN) (precision-nonnegative inputN) scale≤)

canonical-exponential-paired-input-error-bound :
  (x : RegularCauchy) (m n : ℕ) → ℕOrder._≤_ m n →
  dyadicRadius (canonicalExponentialInputScale x m) Q.·
    (precision (canonicalExponentialInputDepth x m) Q.+
     precision (canonicalExponentialInputDepth x n)) ≤
  precision (suc m) Q.+ precision (suc n)
canonical-exponential-paired-input-error-bound x m n m≤n =
  let scale = dyadicRadius (canonicalExponentialInputScale x m)
      inputM = canonicalExponentialInputDepth x m
      inputN = canonicalExponentialInputDepth x n
  in
  subst (_≤ precision (suc m) Q.+ precision (suc n))
    (sym (Q.·DistL+ scale (precision inputM) (precision inputN)))
    (≤Monotone+
      (scale Q.· precision inputM) (precision (suc m))
      (scale Q.· precision inputN) (precision (suc n))
      (subst (scale Q.· precision inputM ≤_)
        (canonical-exponential-input-error-cancels x m)
        (isRefl≤ (scale Q.· precision inputM)))
      (canonical-exponential-later-input-error-bound x m n m≤n))
