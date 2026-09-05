{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CanonicalSineSchedule where

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
open import RationalSineTaylorApproximants
open import UniformSineSeedBounds
open import SinePartialSumInputDifference
open import TaylorScheduleMonotonicity

canonicalSineSeriesDepth : RegularCauchy → ℕ → ℕ
canonicalSineSeriesDepth x n =
  uniformSineCutoff (canonicalDyadicExponent x) (suc n)

canonicalSineInputScale : RegularCauchy → ℕ → ℕ
canonicalSineInputScale x n =
  sinePartialSumDifferenceExponent
    (canonicalDyadicExponent x) (canonicalSineSeriesDepth x n)

canonicalSineInputDepth : RegularCauchy → ℕ → ℕ
canonicalSineInputDepth x n = canonicalSineInputScale x n ℕ.+ suc n

canonicalSineTaylorSchedule : RegularCauchy → TaylorCutoffSchedule
canonicalSineTaylorSchedule x .input-depth = canonicalSineInputDepth x
canonicalSineTaylorSchedule x .series-depth = canonicalSineSeriesDepth x

canonical-sine-input-approximation-bound :
  (x : RegularCauchy) (n : ℕ) →
  MagnitudeBound (approximation x n)
    (dyadicRadius (canonicalDyadicExponent x))
canonical-sine-input-approximation-bound x n =
  bounded-value (canonicalDyadicallyBounded x) n

canonical-sine-input-error-cancels : (x : RegularCauchy) (n : ℕ) →
  dyadicRadius (canonicalSineInputScale x n) Q.·
    precision (canonicalSineInputDepth x n) ≡ precision (suc n)
canonical-sine-input-error-cancels x n =
  radius-cancels-precision-shift (canonicalSineInputScale x n) (suc n)

uniformSineCutoff-suc : (d n : ℕ) →
  uniformSineCutoff d (suc n) ≡ suc (uniformSineCutoff d n)
uniformSineCutoff-suc d n =
  cong (dyadicNat (suc d) ℕ.+_)
    (ℕ.+-suc (uniformSineSeedExponent d) n) ∙
  ℕ.+-suc (dyadicNat (suc d))
    (uniformSineSeedExponent d ℕ.+ n)

uniformSineCutoff-monotone : (d m n : ℕ) →
  ℕOrder._≤_ m n →
  ℕOrder._≤_ (uniformSineCutoff d m) (uniformSineCutoff d n)
uniformSineCutoff-monotone d =
  monotone-from-successor (uniformSineCutoff d)
    (λ n → subst (ℕOrder._≤_ (uniformSineCutoff d n))
      (sym (uniformSineCutoff-suc d n)) ℕOrder.≤-sucℕ)

canonical-sine-series-depth-monotone :
  (x : RegularCauchy) (m n : ℕ) → ℕOrder._≤_ m n →
  ℕOrder._≤_ (canonicalSineSeriesDepth x m)
    (canonicalSineSeriesDepth x n)
canonical-sine-series-depth-monotone x m n m≤n =
  uniformSineCutoff-monotone (canonicalDyadicExponent x)
    (suc m) (suc n) (ℕOrder.suc-≤-suc m≤n)

canonical-sine-input-scale-monotone :
  (x : RegularCauchy) (m n : ℕ) → ℕOrder._≤_ m n →
  ℕOrder._≤_ (canonicalSineInputScale x m)
    (canonicalSineInputScale x n)
canonical-sine-input-scale-monotone x m n m≤n =
  sinePartialSumDifferenceExponent-monotone
    (canonicalDyadicExponent x)
    (canonicalSineSeriesDepth x m) (canonicalSineSeriesDepth x n)
    (canonical-sine-series-depth-monotone x m n m≤n)

canonical-sine-input-depth-monotone :
  (x : RegularCauchy) (m n : ℕ) → ℕOrder._≤_ m n →
  ℕOrder._≤_ (canonicalSineInputDepth x m)
    (canonicalSineInputDepth x n)
canonical-sine-input-depth-monotone x m n m≤n =
  ℕOrder.≤-+-≤ (canonical-sine-input-scale-monotone x m n m≤n)
    (ℕOrder.suc-≤-suc m≤n)

canonical-sine-later-input-error-bound :
  (x : RegularCauchy) (m n : ℕ) → ℕOrder._≤_ m n →
  dyadicRadius (canonicalSineInputScale x m) Q.·
    precision (canonicalSineInputDepth x n) ≤ precision (suc n)
canonical-sine-later-input-error-bound x m n m≤n =
  let scaleM = canonicalSineInputScale x m
      scaleN = canonicalSineInputScale x n
      inputN = canonicalSineInputDepth x n
      scale≤ = dyadicRadius-monotone scaleM scaleN
        (canonical-sine-input-scale-monotone x m n m≤n)
  in
  subst ((dyadicRadius scaleM Q.· precision inputN) ≤_)
    (canonical-sine-input-error-cancels x n)
    (≤-·o (dyadicRadius scaleM) (dyadicRadius scaleN)
      (precision inputN) (precision-nonnegative inputN) scale≤)

canonical-sine-paired-input-error-bound :
  (x : RegularCauchy) (m n : ℕ) → ℕOrder._≤_ m n →
  dyadicRadius (canonicalSineInputScale x m) Q.·
    (precision (canonicalSineInputDepth x m) Q.+
     precision (canonicalSineInputDepth x n)) ≤
  precision (suc m) Q.+ precision (suc n)
canonical-sine-paired-input-error-bound x m n m≤n =
  let scale = dyadicRadius (canonicalSineInputScale x m)
      inputM = canonicalSineInputDepth x m
      inputN = canonicalSineInputDepth x n
  in
  subst (_≤ precision (suc m) Q.+ precision (suc n))
    (sym (Q.·DistL+ scale (precision inputM) (precision inputN)))
    (≤Monotone+
      (scale Q.· precision inputM) (precision (suc m))
      (scale Q.· precision inputN) (precision (suc n))
      (subst (scale Q.· precision inputM ≤_)
        (canonical-sine-input-error-cancels x m)
        (isRefl≤ (scale Q.· precision inputM)))
      (canonical-sine-later-input-error-bound x m n m≤n))
