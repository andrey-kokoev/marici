{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CanonicalCosineSchedule where

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
open import UniformCosineSeedBounds
open import CosinePartialSumInputDifference
open import TaylorScheduleMonotonicity

canonicalCosineSeriesDepth : RegularCauchy → ℕ → ℕ
canonicalCosineSeriesDepth x n =
  uniformCosineCutoff (canonicalDyadicExponent x) (suc n)

canonicalCosineInputScale : RegularCauchy → ℕ → ℕ
canonicalCosineInputScale x n =
  cosinePartialSumDifferenceExponent
    (canonicalDyadicExponent x) (canonicalCosineSeriesDepth x n)

canonicalCosineInputDepth : RegularCauchy → ℕ → ℕ
canonicalCosineInputDepth x n = canonicalCosineInputScale x n ℕ.+ suc n

canonicalCosineTaylorSchedule : RegularCauchy → TaylorCutoffSchedule
canonicalCosineTaylorSchedule x .input-depth = canonicalCosineInputDepth x
canonicalCosineTaylorSchedule x .series-depth = canonicalCosineSeriesDepth x

canonical-cosine-input-approximation-bound :
  (x : RegularCauchy) (n : ℕ) →
  MagnitudeBound (approximation x n)
    (dyadicRadius (canonicalDyadicExponent x))
canonical-cosine-input-approximation-bound x n =
  bounded-value (canonicalDyadicallyBounded x) n

canonical-cosine-input-error-cancels : (x : RegularCauchy) (n : ℕ) →
  dyadicRadius (canonicalCosineInputScale x n) Q.·
    precision (canonicalCosineInputDepth x n) ≡ precision (suc n)
canonical-cosine-input-error-cancels x n =
  radius-cancels-precision-shift (canonicalCosineInputScale x n) (suc n)

uniformCosineCutoff-suc : (d n : ℕ) →
  uniformCosineCutoff d (suc n) ≡ suc (uniformCosineCutoff d n)
uniformCosineCutoff-suc d n =
  cong (dyadicNat (suc d) ℕ.+_)
    (ℕ.+-suc (uniformCosineSeedExponent d) n) ∙
  ℕ.+-suc (dyadicNat (suc d))
    (uniformCosineSeedExponent d ℕ.+ n)

uniformCosineCutoff-monotone : (d m n : ℕ) →
  ℕOrder._≤_ m n →
  ℕOrder._≤_ (uniformCosineCutoff d m) (uniformCosineCutoff d n)
uniformCosineCutoff-monotone d =
  monotone-from-successor (uniformCosineCutoff d)
    (λ n → subst (ℕOrder._≤_ (uniformCosineCutoff d n))
      (sym (uniformCosineCutoff-suc d n)) ℕOrder.≤-sucℕ)

canonical-cosine-series-depth-monotone :
  (x : RegularCauchy) (m n : ℕ) → ℕOrder._≤_ m n →
  ℕOrder._≤_ (canonicalCosineSeriesDepth x m)
    (canonicalCosineSeriesDepth x n)
canonical-cosine-series-depth-monotone x m n m≤n =
  uniformCosineCutoff-monotone (canonicalDyadicExponent x)
    (suc m) (suc n) (ℕOrder.suc-≤-suc m≤n)

canonical-cosine-input-scale-monotone :
  (x : RegularCauchy) (m n : ℕ) → ℕOrder._≤_ m n →
  ℕOrder._≤_ (canonicalCosineInputScale x m)
    (canonicalCosineInputScale x n)
canonical-cosine-input-scale-monotone x m n m≤n =
  cosinePartialSumDifferenceExponent-monotone
    (canonicalDyadicExponent x)
    (canonicalCosineSeriesDepth x m) (canonicalCosineSeriesDepth x n)
    (canonical-cosine-series-depth-monotone x m n m≤n)

canonical-cosine-input-depth-monotone :
  (x : RegularCauchy) (m n : ℕ) → ℕOrder._≤_ m n →
  ℕOrder._≤_ (canonicalCosineInputDepth x m)
    (canonicalCosineInputDepth x n)
canonical-cosine-input-depth-monotone x m n m≤n =
  ℕOrder.≤-+-≤ (canonical-cosine-input-scale-monotone x m n m≤n)
    (ℕOrder.suc-≤-suc m≤n)

canonical-cosine-later-input-error-bound :
  (x : RegularCauchy) (m n : ℕ) → ℕOrder._≤_ m n →
  dyadicRadius (canonicalCosineInputScale x m) Q.·
    precision (canonicalCosineInputDepth x n) ≤ precision (suc n)
canonical-cosine-later-input-error-bound x m n m≤n =
  let scaleM = canonicalCosineInputScale x m
      scaleN = canonicalCosineInputScale x n
      inputN = canonicalCosineInputDepth x n
      scale≤ = dyadicRadius-monotone scaleM scaleN
        (canonical-cosine-input-scale-monotone x m n m≤n)
  in
  subst ((dyadicRadius scaleM Q.· precision inputN) ≤_)
    (canonical-cosine-input-error-cancels x n)
    (≤-·o (dyadicRadius scaleM) (dyadicRadius scaleN)
      (precision inputN) (precision-nonnegative inputN) scale≤)

canonical-cosine-paired-input-error-bound :
  (x : RegularCauchy) (m n : ℕ) → ℕOrder._≤_ m n →
  dyadicRadius (canonicalCosineInputScale x m) Q.·
    (precision (canonicalCosineInputDepth x m) Q.+
     precision (canonicalCosineInputDepth x n)) ≤
  precision (suc m) Q.+ precision (suc n)
canonical-cosine-paired-input-error-bound x m n m≤n =
  let scale = dyadicRadius (canonicalCosineInputScale x m)
      inputM = canonicalCosineInputDepth x m
      inputN = canonicalCosineInputDepth x n
  in
  subst (_≤ precision (suc m) Q.+ precision (suc n))
    (sym (Q.·DistL+ scale (precision inputM) (precision inputN)))
    (≤Monotone+
      (scale Q.· precision inputM) (precision (suc m))
      (scale Q.· precision inputN) (precision (suc n))
      (subst (scale Q.· precision inputM ≤_)
        (canonical-cosine-input-error-cancels x m)
        (isRefl≤ (scale Q.· precision inputM)))
      (canonical-cosine-later-input-error-bound x m n m≤n))
