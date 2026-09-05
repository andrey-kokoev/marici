{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CanonicalCosineComparisonSchedule where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; suc; _+_; max; +-assoc; +-comm)
import Cubical.Data.Nat.Order as ℕOrder
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate
open import RegularCauchyStructure
open import CauchyProductBounds
open import CauchyProductErrorBounds
open import DyadicallyBoundedCauchy
open import CanonicalDyadicallyBoundedCauchy
open import RationalTaylorApproximants
open import CosinePartialSumInputDifference
open import UniformCosineInputStabilityContract
open import UniformCosineSeedBounds
open import CosineTailSchedule
open import CanonicalCosineSchedule
open import CanonicalCosineRegularity
open import TaylorRegularityComposition

comparisonCosineExponent : RegularCauchy → RegularCauchy → ℕ
comparisonCosineExponent x y =
  ℕ.max (canonicalDyadicExponent x) (canonicalDyadicExponent y)

comparisonCosineInputScale : RegularCauchy → RegularCauchy → ℕ → ℕ
comparisonCosineInputScale x y n =
  ℕ.max (canonicalCosineInputScale x n)
        (canonicalCosineInputScale y n)

comparisonCosineInputDepth : RegularCauchy → RegularCauchy → ℕ → ℕ
comparisonCosineInputDepth x y n =
  comparisonCosineInputScale x y n ℕ.+ suc n

comparisonCosineSeriesDepth : RegularCauchy → RegularCauchy → ℕ → ℕ
comparisonCosineSeriesDepth x y n =
  ℕ.max (canonicalCosineSeriesDepth x n)
        (canonicalCosineSeriesDepth y n)

left-input-scale≤comparison : (x y : RegularCauchy) (n : ℕ) →
  ℕOrder._≤_ (canonicalCosineInputScale x n)
    (comparisonCosineInputScale x y n)
left-input-scale≤comparison x y n = ℕOrder.left-≤-max

right-input-scale≤comparison : (x y : RegularCauchy) (n : ℕ) →
  ℕOrder._≤_ (canonicalCosineInputScale y n)
    (comparisonCosineInputScale x y n)
right-input-scale≤comparison x y n = ℕOrder.right-≤-max

left-input-depth≤comparison : (x y : RegularCauchy) (n : ℕ) →
  ℕOrder._≤_ (canonicalCosineInputDepth x n)
    (comparisonCosineInputDepth x y n)
left-input-depth≤comparison x y n =
  ℕOrder.≤-+-≤ (left-input-scale≤comparison x y n)
    ℕOrder.≤-refl

right-input-depth≤comparison : (x y : RegularCauchy) (n : ℕ) →
  ℕOrder._≤_ (canonicalCosineInputDepth y n)
    (comparisonCosineInputDepth x y n)
right-input-depth≤comparison x y n =
  ℕOrder.≤-+-≤ (right-input-scale≤comparison x y n)
    ℕOrder.≤-refl

left-series-depth≤comparison : (x y : RegularCauchy) (n : ℕ) →
  ℕOrder._≤_ (canonicalCosineSeriesDepth x n)
    (comparisonCosineSeriesDepth x y n)
left-series-depth≤comparison x y n = ℕOrder.left-≤-max

right-series-depth≤comparison : (x y : RegularCauchy) (n : ℕ) →
  ℕOrder._≤_ (canonicalCosineSeriesDepth y n)
    (comparisonCosineSeriesDepth x y n)
right-series-depth≤comparison x y n = ℕOrder.right-≤-max

left-comparison-approximation-bound :
  (x y : RegularCauchy) (n : ℕ) →
  MagnitudeBound (approximation x n)
    (dyadicRadius (comparisonCosineExponent x y))
left-comparison-approximation-bound x y n =
  weaken-magnitude-bound _ _
    (dyadicRadius (comparisonCosineExponent x y))
    (dyadicRadius-monotone
      (canonicalDyadicExponent x) (comparisonCosineExponent x y)
      ℕOrder.left-≤-max)
    (canonical-cosine-input-approximation-bound x n)

right-comparison-approximation-bound :
  (x y : RegularCauchy) (n : ℕ) →
  MagnitudeBound (approximation y n)
    (dyadicRadius (comparisonCosineExponent x y))
right-comparison-approximation-bound x y n =
  weaken-magnitude-bound _ _
    (dyadicRadius (comparisonCosineExponent x y))
    (dyadicRadius-monotone
      (canonicalDyadicExponent y) (comparisonCosineExponent x y)
      ℕOrder.right-≤-max)
    (canonical-cosine-input-approximation-bound y n)

comparisonCosineCrossScale : RegularCauchy → RegularCauchy → ℕ → ℕ
comparisonCosineCrossScale x y n =
  cosinePartialSumDifferenceExponent (comparisonCosineExponent x y)
    (comparisonCosineSeriesDepth x y n)

comparisonCosineMetricDepth :
  RegularCauchy → RegularCauchy → ℕ → ℕ
comparisonCosineMetricDepth x y n =
  comparisonCosineCrossScale x y n ℕ.+ suc n

comparison-cross-error-cancels : (x y : RegularCauchy) (n : ℕ) →
  dyadicRadius (comparisonCosineCrossScale x y n) Q.·
    precision (comparisonCosineMetricDepth x y n) ≡
  precision (suc n)
comparison-cross-error-cancels x y n =
  radius-cancels-precision-shift
    (comparisonCosineCrossScale x y n) (suc n)

common-series-cross-bound :
  (x y : RegularCauchy) (n : ℕ) →
  let inputDepth = comparisonCosineInputDepth x y n
      seriesDepth = comparisonCosineSeriesDepth x y n
      metricDepth = comparisonCosineMetricDepth x y n
  in
  approximation x inputDepth ≤
    approximation y inputDepth Q.+ precision metricDepth →
  approximation y inputDepth ≤
    approximation x inputDepth Q.+ precision metricDepth →
  MagnitudeBound
    (cosinePartialSum (approximation x inputDepth) seriesDepth Q.+
     (Q.- cosinePartialSum
       (approximation y inputDepth) seriesDepth))
    (precision (suc n))
common-series-cross-bound x y n x≤y+error y≤x+error =
  let inputDepth = comparisonCosineInputDepth x y n
      seriesDepth = comparisonCosineSeriesDepth x y n
      metricDepth = comparisonCosineMetricDepth x y n
      exponent = comparisonCosineExponent x y
      difference = difference-magnitude-bound
        (approximation x inputDepth) (approximation y inputDepth)
        (precision metricDepth) x≤y+error y≤x+error
      raw = cosine-partial-sum-input-difference-bound
        (approximation x inputDepth) (approximation y inputDepth)
        (precision metricDepth) exponent seriesDepth
        (precision-nonnegative metricDepth)
        (left-comparison-approximation-bound x y inputDepth)
        (right-comparison-approximation-bound x y inputDepth)
        difference
  in
  subst
    (MagnitudeBound
      (cosinePartialSum (approximation x inputDepth) seriesDepth Q.+
       (Q.- cosinePartialSum
         (approximation y inputDepth) seriesDepth)))
    (comparison-cross-error-cancels x y n) raw

uniform-common-series-cross-bound :
  (stability : UniformCosinePartialSumInputStability) →
  (x y : RegularCauchy) (n outputPrecision : ℕ) →
  let inputDepth = comparisonCosineInputDepth x y n
      seriesDepth = comparisonCosineSeriesDepth x y n
      metricDepth = uniformCosineMetricDepth stability
        (comparisonCosineExponent x y) outputPrecision
  in
  approximation x inputDepth ≤
    approximation y inputDepth Q.+ precision metricDepth →
  approximation y inputDepth ≤
    approximation x inputDepth Q.+ precision metricDepth →
  MagnitudeBound
    (cosinePartialSum (approximation x inputDepth) seriesDepth Q.+
     (Q.- cosinePartialSum
       (approximation y inputDepth) seriesDepth))
    (precision outputPrecision)
uniform-common-series-cross-bound stability x y n outputPrecision
  x≤y+error y≤x+error =
  let inputDepth = comparisonCosineInputDepth x y n
      seriesDepth = comparisonCosineSeriesDepth x y n
      exponent = comparisonCosineExponent x y
      metricDepth = uniformCosineMetricDepth stability
        exponent outputPrecision
      difference = difference-magnitude-bound
        (approximation x inputDepth) (approximation y inputDepth)
        (precision metricDepth) x≤y+error y≤x+error
      raw = uniformCosinePartialSumDifference stability
        (approximation x inputDepth) (approximation y inputDepth)
        (precision metricDepth) exponent seriesDepth
        (precision-nonnegative metricDepth)
        (left-comparison-approximation-bound x y inputDepth)
        (right-comparison-approximation-bound x y inputDepth)
        difference
  in
  subst
    (MagnitudeBound
      (cosinePartialSum (approximation x inputDepth) seriesDepth Q.+
       (Q.- cosinePartialSum
         (approximation y inputDepth) seriesDepth)))
    (uniform-cosine-metric-error-cancels stability
      exponent outputPrecision)
    raw

comparison-input-error-cancels : (x y : RegularCauchy) (n : ℕ) →
  dyadicRadius (comparisonCosineInputScale x y n) Q.·
    precision (comparisonCosineInputDepth x y n) ≡
  precision (suc n)
comparison-input-error-cancels x y n =
  radius-cancels-precision-shift
    (comparisonCosineInputScale x y n) (suc n)

left-common-input-error-bound : (x y : RegularCauchy) (n : ℕ) →
  dyadicRadius (canonicalCosineInputScale x n) Q.·
    precision (comparisonCosineInputDepth x y n) ≤
  precision (suc n)
left-common-input-error-bound x y n =
  subst
    ((dyadicRadius (canonicalCosineInputScale x n) Q.·
      precision (comparisonCosineInputDepth x y n)) ≤_)
    (comparison-input-error-cancels x y n)
    (≤-·o
      (dyadicRadius (canonicalCosineInputScale x n))
      (dyadicRadius (comparisonCosineInputScale x y n))
      (precision (comparisonCosineInputDepth x y n))
      (precision-nonnegative (comparisonCosineInputDepth x y n))
      (dyadicRadius-monotone
        (canonicalCosineInputScale x n)
        (comparisonCosineInputScale x y n)
        (left-input-scale≤comparison x y n)))

right-common-input-error-bound : (x y : RegularCauchy) (n : ℕ) →
  dyadicRadius (canonicalCosineInputScale y n) Q.·
    precision (comparisonCosineInputDepth x y n) ≤
  precision (suc n)
right-common-input-error-bound x y n =
  subst
    ((dyadicRadius (canonicalCosineInputScale y n) Q.·
      precision (comparisonCosineInputDepth x y n)) ≤_)
    (comparison-input-error-cancels x y n)
    (≤-·o
      (dyadicRadius (canonicalCosineInputScale y n))
      (dyadicRadius (comparisonCosineInputScale x y n))
      (precision (comparisonCosineInputDepth x y n))
      (precision-nonnegative (comparisonCosineInputDepth x y n))
      (dyadicRadius-monotone
        (canonicalCosineInputScale y n)
        (comparisonCosineInputScale x y n)
        (right-input-scale≤comparison x y n)))

module ComparisonErrorPaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; _·_ to _·S_)

  distribute : (r a b : fst R) →
    r ·S (a +S b) ≡ (r ·S a) +S (r ·S b)
  distribute r a b = solve! R

combine-comparison-input-errors :
  (scale : ℕ) (ownDepth commonDepth n : ℕ) →
  dyadicRadius scale Q.· precision ownDepth ≡ precision (suc n) →
  dyadicRadius scale Q.· precision commonDepth ≤ precision (suc n) →
  dyadicRadius scale Q.·
    (precision ownDepth Q.+ precision commonDepth) ≤ precision n
combine-comparison-input-errors scale ownDepth commonDepth n ownCancels common≤ =
  let radius = dyadicRadius scale
      distributed = ComparisonErrorPaths.distribute PreferredℚCommRing
        radius (precision ownDepth) (precision commonDepth)
      halves≤ = ≤Monotone+
        (radius Q.· precision ownDepth) (precision (suc n))
        (radius Q.· precision commonDepth) (precision (suc n))
        (subst ((radius Q.· precision ownDepth) ≤_)
          ownCancels (isRefl≤ (radius Q.· precision ownDepth)))
        common≤
  in
  subst (_≤ precision n) (sym distributed)
    (subst (((radius Q.· precision ownDepth) Q.+
      (radius Q.· precision commonDepth)) ≤_)
      (precision-refines-double n) halves≤)

left-comparison-input-error-bound : (x y : RegularCauchy) (n : ℕ) →
  dyadicRadius (canonicalCosineInputScale x n) Q.·
    (precision (canonicalCosineInputDepth x n) Q.+
     precision (comparisonCosineInputDepth x y n)) ≤ precision n
left-comparison-input-error-bound x y n =
  combine-comparison-input-errors
    (canonicalCosineInputScale x n)
    (canonicalCosineInputDepth x n)
    (comparisonCosineInputDepth x y n) n
    (canonical-cosine-input-error-cancels x n)
    (left-common-input-error-bound x y n)

right-comparison-input-error-bound : (x y : RegularCauchy) (n : ℕ) →
  dyadicRadius (canonicalCosineInputScale y n) Q.·
    (precision (canonicalCosineInputDepth y n) Q.+
     precision (comparisonCosineInputDepth x y n)) ≤ precision n
right-comparison-input-error-bound x y n =
  combine-comparison-input-errors
    (canonicalCosineInputScale y n)
    (canonicalCosineInputDepth y n)
    (comparisonCosineInputDepth x y n) n
    (canonical-cosine-input-error-cancels y n)
    (right-common-input-error-bound x y n)

left-scheduled-to-common-input-bound :
  (x y : RegularCauchy) (n : ℕ) →
  MagnitudeBound
    (cosinePartialSum
      (approximation x (canonicalCosineInputDepth x n))
      (canonicalCosineSeriesDepth x n) Q.+
     (Q.- cosinePartialSum
      (approximation x (comparisonCosineInputDepth x y n))
      (canonicalCosineSeriesDepth x n)))
    (precision n)
left-scheduled-to-common-input-bound x y n =
  let ownDepth = canonicalCosineInputDepth x n
      commonDepth = comparisonCosineInputDepth x y n
      seriesDepth = canonicalCosineSeriesDepth x n
      error = precision ownDepth Q.+ precision commonDepth
      raw = cosine-partial-sum-input-difference-bound
        (approximation x ownDepth) (approximation x commonDepth)
        error (canonicalDyadicExponent x) seriesDepth
        (precision-sum-nonnegative ownDepth commonDepth)
        (canonical-cosine-input-approximation-bound x ownDepth)
        (canonical-cosine-input-approximation-bound x commonDepth)
        (cauchy-difference-bound x ownDepth commonDepth)
  in
  weaken-magnitude-bound _ _ (precision n)
    (left-comparison-input-error-bound x y n) raw

right-scheduled-to-common-input-bound :
  (x y : RegularCauchy) (n : ℕ) →
  MagnitudeBound
    (cosinePartialSum
      (approximation y (canonicalCosineInputDepth y n))
      (canonicalCosineSeriesDepth y n) Q.+
     (Q.- cosinePartialSum
      (approximation y (comparisonCosineInputDepth x y n))
      (canonicalCosineSeriesDepth y n)))
    (precision n)
right-scheduled-to-common-input-bound x y n =
  let ownDepth = canonicalCosineInputDepth y n
      commonDepth = comparisonCosineInputDepth x y n
      seriesDepth = canonicalCosineSeriesDepth y n
      error = precision ownDepth Q.+ precision commonDepth
      raw = cosine-partial-sum-input-difference-bound
        (approximation y ownDepth) (approximation y commonDepth)
        error (canonicalDyadicExponent y) seriesDepth
        (precision-sum-nonnegative ownDepth commonDepth)
        (canonical-cosine-input-approximation-bound y ownDepth)
        (canonical-cosine-input-approximation-bound y commonDepth)
        (cauchy-difference-bound y ownDepth commonDepth)
  in
  weaken-magnitude-bound _ _ (precision n)
    (right-comparison-input-error-bound x y n) raw

common-series-extension-bound :
  (q : Q.ℚ) (d n commonDepth : ℕ) →
  MagnitudeBound q (dyadicRadius d) →
  ℕOrder._≤_ (uniformCosineCutoff d (suc n)) commonDepth →
  MagnitudeBound
    (cosinePartialSum q commonDepth Q.+
     (Q.- cosinePartialSum q
       (uniformCosineCutoff d (suc n))))
    (precision (suc n))
common-series-extension-bound q d n commonDepth qBound
  (count , count+scheduled≡common) =
  let seed = uniformCosineTailSeed q d qBound
      scheduled+count≡common =
        cong (dyadicNat (suc d) ℕ.+_)
          (+-assoc (uniformCosineSeedExponent d) (suc n) count) ∙
        +-assoc (dyadicNat (suc d))
          (uniformCosineSeedExponent d ℕ.+ suc n) count ∙
        +-comm (uniformCosineCutoff d (suc n)) count ∙
        count+scheduled≡common
  in
  subst
    (λ depth → MagnitudeBound
      (cosinePartialSum q depth Q.+
       (Q.- cosinePartialSum q
        (uniformCosineCutoff d (suc n))))
      (precision (suc n)))
    scheduled+count≡common
    (absorbed-cosine-forward-difference seed (suc n) count)

left-common-series-extension-bound :
  (x y : RegularCauchy) (n : ℕ) →
  MagnitudeBound
    (cosinePartialSum
      (approximation x (comparisonCosineInputDepth x y n))
      (comparisonCosineSeriesDepth x y n) Q.+
     (Q.- cosinePartialSum
      (approximation x (comparisonCosineInputDepth x y n))
      (canonicalCosineSeriesDepth x n)))
    (precision (suc n))
left-common-series-extension-bound x y n =
  common-series-extension-bound
    (approximation x (comparisonCosineInputDepth x y n))
    (canonicalDyadicExponent x) n
    (comparisonCosineSeriesDepth x y n)
    (canonical-cosine-input-approximation-bound x
      (comparisonCosineInputDepth x y n))
    (left-series-depth≤comparison x y n)

right-common-series-extension-bound :
  (x y : RegularCauchy) (n : ℕ) →
  MagnitudeBound
    (cosinePartialSum
      (approximation y (comparisonCosineInputDepth x y n))
      (comparisonCosineSeriesDepth x y n) Q.+
     (Q.- cosinePartialSum
      (approximation y (comparisonCosineInputDepth x y n))
      (canonicalCosineSeriesDepth y n)))
    (precision (suc n))
right-common-series-extension-bound x y n =
  common-series-extension-bound
    (approximation y (comparisonCosineInputDepth x y n))
    (canonicalDyadicExponent y) n
    (comparisonCosineSeriesDepth x y n)
    (canonical-cosine-input-approximation-bound y
      (comparisonCosineInputDepth x y n))
    (right-series-depth≤comparison x y n)

canonical-cosine-pointwise-cross-forward :
  (x y : RegularCauchy) (k : ℕ) →
  let n = suc (suc (suc k))
      inputDepth = comparisonCosineInputDepth x y n
      metricDepth = comparisonCosineMetricDepth x y n
  in
  approximation x inputDepth ≤
    approximation y inputDepth Q.+ precision metricDepth →
  approximation y inputDepth ≤
    approximation x inputDepth Q.+ precision metricDepth →
  approximation (canonicalCosineRegular x) n ≤
    approximation (canonicalCosineRegular y) n Q.+ precision k
canonical-cosine-pointwise-cross-forward x y k x≤y+error y≤x+error =
  let n = suc (suc (suc k))
      inputDepth = comparisonCosineInputDepth x y n
      sx = canonicalCosineSeriesDepth x n
      sy = canonicalCosineSeriesDepth y n
      commonSeries = comparisonCosineSeriesDepth x y n
      A = approximation (canonicalCosineRegular x) n
      B = cosinePartialSum (approximation x inputDepth) sx
      C = cosinePartialSum (approximation x inputDepth) commonSeries
      D = cosinePartialSum (approximation y inputDepth) commonSeries
      E = cosinePartialSum (approximation y inputDepth) sy
      F = approximation (canonicalCosineRegular y) n
      widenHalf : (u v : Q.ℚ) → u ≤ v Q.+ precision (suc n) →
        u ≤ v Q.+ precision n
      widenHalf u v bound = isTrans≤ u (v Q.+ precision (suc n))
        (v Q.+ precision n) bound
        (≤Monotone+ v v (precision (suc n)) (precision n)
          (isRefl≤ v) (precision-step≤ n))
      AB = magnitude-bound-forward A B (precision n)
        (left-scheduled-to-common-input-bound x y n)
      BC = widenHalf B C
        (magnitude-bound-backward C B (precision (suc n))
          (left-common-series-extension-bound x y n))
      CD = widenHalf C D
        (magnitude-bound-forward C D (precision (suc n))
          (common-series-cross-bound x y n x≤y+error y≤x+error))
      DE = widenHalf D E
        (magnitude-bound-forward D E (precision (suc n))
          (right-common-series-extension-bound x y n))
      EF = magnitude-bound-backward F E (precision n)
        (right-scheduled-to-common-input-bound x y n)
  in
  compose-five-third-refinement A B C D E F k AB BC CD DE EF

canonical-cosine-pointwise-cross-backward :
  (x y : RegularCauchy) (k : ℕ) →
  let n = suc (suc (suc k))
      inputDepth = comparisonCosineInputDepth x y n
      metricDepth = comparisonCosineMetricDepth x y n
  in
  approximation x inputDepth ≤
    approximation y inputDepth Q.+ precision metricDepth →
  approximation y inputDepth ≤
    approximation x inputDepth Q.+ precision metricDepth →
  approximation (canonicalCosineRegular y) n ≤
    approximation (canonicalCosineRegular x) n Q.+ precision k
canonical-cosine-pointwise-cross-backward x y k x≤y+error y≤x+error =
  let n = suc (suc (suc k))
      inputDepth = comparisonCosineInputDepth x y n
      sx = canonicalCosineSeriesDepth x n
      sy = canonicalCosineSeriesDepth y n
      commonSeries = comparisonCosineSeriesDepth x y n
      A = approximation (canonicalCosineRegular x) n
      B = cosinePartialSum (approximation x inputDepth) sx
      C = cosinePartialSum (approximation x inputDepth) commonSeries
      D = cosinePartialSum (approximation y inputDepth) commonSeries
      E = cosinePartialSum (approximation y inputDepth) sy
      F = approximation (canonicalCosineRegular y) n
      widenHalf : (u v : Q.ℚ) → u ≤ v Q.+ precision (suc n) →
        u ≤ v Q.+ precision n
      widenHalf u v bound = isTrans≤ u (v Q.+ precision (suc n))
        (v Q.+ precision n) bound
        (≤Monotone+ v v (precision (suc n)) (precision n)
          (isRefl≤ v) (precision-step≤ n))
      FE = magnitude-bound-forward F E (precision n)
        (right-scheduled-to-common-input-bound x y n)
      ED = widenHalf E D
        (magnitude-bound-backward D E (precision (suc n))
          (right-common-series-extension-bound x y n))
      DC = widenHalf D C
        (magnitude-bound-backward C D (precision (suc n))
          (common-series-cross-bound x y n x≤y+error y≤x+error))
      CB = widenHalf C B
        (magnitude-bound-forward C B (precision (suc n))
          (left-common-series-extension-bound x y n))
      BA = magnitude-bound-backward A B (precision n)
        (left-scheduled-to-common-input-bound x y n)
  in
  compose-five-third-refinement F E D C B A k FE ED DC CB BA

