{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CanonicalSineComparisonSchedule where

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
open import RationalSineTaylorApproximants
open import SinePartialSumInputDifference
open import UniformSineInputStabilityContract
open import UniformSineSeedBounds
open import SineTailSchedule
open import CanonicalSineSchedule
open import CanonicalSineRegularity
open import TaylorRegularityComposition

comparisonSineExponent : RegularCauchy → RegularCauchy → ℕ
comparisonSineExponent x y =
  ℕ.max (canonicalDyadicExponent x) (canonicalDyadicExponent y)

comparisonSineInputScale : RegularCauchy → RegularCauchy → ℕ → ℕ
comparisonSineInputScale x y n =
  ℕ.max (canonicalSineInputScale x n)
        (canonicalSineInputScale y n)

comparisonSineInputDepth : RegularCauchy → RegularCauchy → ℕ → ℕ
comparisonSineInputDepth x y n =
  comparisonSineInputScale x y n ℕ.+ suc n

comparisonSineSeriesDepth : RegularCauchy → RegularCauchy → ℕ → ℕ
comparisonSineSeriesDepth x y n =
  ℕ.max (canonicalSineSeriesDepth x n)
        (canonicalSineSeriesDepth y n)

sine-left-input-scale≤comparison : (x y : RegularCauchy) (n : ℕ) →
  ℕOrder._≤_ (canonicalSineInputScale x n)
    (comparisonSineInputScale x y n)
sine-left-input-scale≤comparison x y n = ℕOrder.left-≤-max

sine-right-input-scale≤comparison : (x y : RegularCauchy) (n : ℕ) →
  ℕOrder._≤_ (canonicalSineInputScale y n)
    (comparisonSineInputScale x y n)
sine-right-input-scale≤comparison x y n = ℕOrder.right-≤-max

sine-left-input-depth≤comparison : (x y : RegularCauchy) (n : ℕ) →
  ℕOrder._≤_ (canonicalSineInputDepth x n)
    (comparisonSineInputDepth x y n)
sine-left-input-depth≤comparison x y n =
  ℕOrder.≤-+-≤ (sine-left-input-scale≤comparison x y n)
    ℕOrder.≤-refl

sine-right-input-depth≤comparison : (x y : RegularCauchy) (n : ℕ) →
  ℕOrder._≤_ (canonicalSineInputDepth y n)
    (comparisonSineInputDepth x y n)
sine-right-input-depth≤comparison x y n =
  ℕOrder.≤-+-≤ (sine-right-input-scale≤comparison x y n)
    ℕOrder.≤-refl

sine-left-series-depth≤comparison : (x y : RegularCauchy) (n : ℕ) →
  ℕOrder._≤_ (canonicalSineSeriesDepth x n)
    (comparisonSineSeriesDepth x y n)
sine-left-series-depth≤comparison x y n = ℕOrder.left-≤-max

sine-right-series-depth≤comparison : (x y : RegularCauchy) (n : ℕ) →
  ℕOrder._≤_ (canonicalSineSeriesDepth y n)
    (comparisonSineSeriesDepth x y n)
sine-right-series-depth≤comparison x y n = ℕOrder.right-≤-max

sine-sine-left-comparison-approximation-bound :
  (x y : RegularCauchy) (n : ℕ) →
  MagnitudeBound (approximation x n)
    (dyadicRadius (comparisonSineExponent x y))
sine-sine-left-comparison-approximation-bound x y n =
  weaken-magnitude-bound _ _
    (dyadicRadius (comparisonSineExponent x y))
    (dyadicRadius-monotone
      (canonicalDyadicExponent x) (comparisonSineExponent x y)
      ℕOrder.left-≤-max)
    (canonical-sine-input-approximation-bound x n)

sine-sine-right-comparison-approximation-bound :
  (x y : RegularCauchy) (n : ℕ) →
  MagnitudeBound (approximation y n)
    (dyadicRadius (comparisonSineExponent x y))
sine-sine-right-comparison-approximation-bound x y n =
  weaken-magnitude-bound _ _
    (dyadicRadius (comparisonSineExponent x y))
    (dyadicRadius-monotone
      (canonicalDyadicExponent y) (comparisonSineExponent x y)
      ℕOrder.right-≤-max)
    (canonical-sine-input-approximation-bound y n)

comparisonSineCrossScale : RegularCauchy → RegularCauchy → ℕ → ℕ
comparisonSineCrossScale x y n =
  sinePartialSumDifferenceExponent (comparisonSineExponent x y)
    (comparisonSineSeriesDepth x y n)

comparisonSineMetricDepth :
  RegularCauchy → RegularCauchy → ℕ → ℕ
comparisonSineMetricDepth x y n =
  comparisonSineCrossScale x y n ℕ.+ suc n

sine-sine-comparison-cross-error-cancels : (x y : RegularCauchy) (n : ℕ) →
  dyadicRadius (comparisonSineCrossScale x y n) Q.·
    precision (comparisonSineMetricDepth x y n) ≡
  precision (suc n)
sine-sine-comparison-cross-error-cancels x y n =
  radius-cancels-precision-shift
    (comparisonSineCrossScale x y n) (suc n)

sine-common-series-cross-bound :
  (x y : RegularCauchy) (n : ℕ) →
  let inputDepth = comparisonSineInputDepth x y n
      seriesDepth = comparisonSineSeriesDepth x y n
      metricDepth = comparisonSineMetricDepth x y n
  in
  approximation x inputDepth ≤
    approximation y inputDepth Q.+ precision metricDepth →
  approximation y inputDepth ≤
    approximation x inputDepth Q.+ precision metricDepth →
  MagnitudeBound
    (sinePartialSum (approximation x inputDepth) seriesDepth Q.+
     (Q.- sinePartialSum
       (approximation y inputDepth) seriesDepth))
    (precision (suc n))
sine-common-series-cross-bound x y n x≤y+error y≤x+error =
  let inputDepth = comparisonSineInputDepth x y n
      seriesDepth = comparisonSineSeriesDepth x y n
      metricDepth = comparisonSineMetricDepth x y n
      exponent = comparisonSineExponent x y
      difference = difference-magnitude-bound
        (approximation x inputDepth) (approximation y inputDepth)
        (precision metricDepth) x≤y+error y≤x+error
      raw = sine-partial-sum-input-difference-bound
        (approximation x inputDepth) (approximation y inputDepth)
        (precision metricDepth) exponent seriesDepth
        (precision-nonnegative metricDepth)
        (sine-sine-left-comparison-approximation-bound x y inputDepth)
        (sine-sine-right-comparison-approximation-bound x y inputDepth)
        difference
  in
  subst
    (MagnitudeBound
      (sinePartialSum (approximation x inputDepth) seriesDepth Q.+
       (Q.- sinePartialSum
         (approximation y inputDepth) seriesDepth)))
    (sine-sine-comparison-cross-error-cancels x y n) raw

uniform-sine-common-series-cross-bound :
  (stability : UniformSinePartialSumInputStability) →
  (x y : RegularCauchy) (n outputPrecision : ℕ) →
  let inputDepth = comparisonSineInputDepth x y n
      seriesDepth = comparisonSineSeriesDepth x y n
      metricDepth = uniformSineMetricDepth stability
        (comparisonSineExponent x y) outputPrecision
  in
  approximation x inputDepth ≤
    approximation y inputDepth Q.+ precision metricDepth →
  approximation y inputDepth ≤
    approximation x inputDepth Q.+ precision metricDepth →
  MagnitudeBound
    (sinePartialSum (approximation x inputDepth) seriesDepth Q.+
     (Q.- sinePartialSum
       (approximation y inputDepth) seriesDepth))
    (precision outputPrecision)
uniform-sine-common-series-cross-bound stability x y n outputPrecision
  x≤y+error y≤x+error =
  let inputDepth = comparisonSineInputDepth x y n
      seriesDepth = comparisonSineSeriesDepth x y n
      exponent = comparisonSineExponent x y
      metricDepth = uniformSineMetricDepth stability
        exponent outputPrecision
      difference = difference-magnitude-bound
        (approximation x inputDepth) (approximation y inputDepth)
        (precision metricDepth) x≤y+error y≤x+error
      raw = uniformSinePartialSumDifference stability
        (approximation x inputDepth) (approximation y inputDepth)
        (precision metricDepth) exponent seriesDepth
        (precision-nonnegative metricDepth)
        (sine-sine-left-comparison-approximation-bound x y inputDepth)
        (sine-sine-right-comparison-approximation-bound x y inputDepth)
        difference
  in
  subst
    (MagnitudeBound
      (sinePartialSum (approximation x inputDepth) seriesDepth Q.+
       (Q.- sinePartialSum
         (approximation y inputDepth) seriesDepth)))
    (uniform-sine-metric-error-cancels stability
      exponent outputPrecision)
    raw

sine-sine-comparison-input-error-cancels : (x y : RegularCauchy) (n : ℕ) →
  dyadicRadius (comparisonSineInputScale x y n) Q.·
    precision (comparisonSineInputDepth x y n) ≡
  precision (suc n)
sine-sine-comparison-input-error-cancels x y n =
  radius-cancels-precision-shift
    (comparisonSineInputScale x y n) (suc n)

sine-sine-left-common-input-error-bound : (x y : RegularCauchy) (n : ℕ) →
  dyadicRadius (canonicalSineInputScale x n) Q.·
    precision (comparisonSineInputDepth x y n) ≤
  precision (suc n)
sine-sine-left-common-input-error-bound x y n =
  subst
    ((dyadicRadius (canonicalSineInputScale x n) Q.·
      precision (comparisonSineInputDepth x y n)) ≤_)
    (sine-sine-comparison-input-error-cancels x y n)
    (≤-·o
      (dyadicRadius (canonicalSineInputScale x n))
      (dyadicRadius (comparisonSineInputScale x y n))
      (precision (comparisonSineInputDepth x y n))
      (precision-nonnegative (comparisonSineInputDepth x y n))
      (dyadicRadius-monotone
        (canonicalSineInputScale x n)
        (comparisonSineInputScale x y n)
        (sine-left-input-scale≤comparison x y n)))

sine-sine-right-common-input-error-bound : (x y : RegularCauchy) (n : ℕ) →
  dyadicRadius (canonicalSineInputScale y n) Q.·
    precision (comparisonSineInputDepth x y n) ≤
  precision (suc n)
sine-sine-right-common-input-error-bound x y n =
  subst
    ((dyadicRadius (canonicalSineInputScale y n) Q.·
      precision (comparisonSineInputDepth x y n)) ≤_)
    (sine-sine-comparison-input-error-cancels x y n)
    (≤-·o
      (dyadicRadius (canonicalSineInputScale y n))
      (dyadicRadius (comparisonSineInputScale x y n))
      (precision (comparisonSineInputDepth x y n))
      (precision-nonnegative (comparisonSineInputDepth x y n))
      (dyadicRadius-monotone
        (canonicalSineInputScale y n)
        (comparisonSineInputScale x y n)
        (sine-right-input-scale≤comparison x y n)))

module SineComparisonErrorPaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; _·_ to _·S_)

  distribute : (r a b : fst R) →
    r ·S (a +S b) ≡ (r ·S a) +S (r ·S b)
  distribute r a b = solve! R

combine-sine-comparison-input-errors :
  (scale : ℕ) (ownDepth commonDepth n : ℕ) →
  dyadicRadius scale Q.· precision ownDepth ≡ precision (suc n) →
  dyadicRadius scale Q.· precision commonDepth ≤ precision (suc n) →
  dyadicRadius scale Q.·
    (precision ownDepth Q.+ precision commonDepth) ≤ precision n
combine-sine-comparison-input-errors scale ownDepth commonDepth n ownCancels common≤ =
  let radius = dyadicRadius scale
      distributed = SineComparisonErrorPaths.distribute PreferredℚCommRing
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

sine-sine-left-comparison-input-error-bound : (x y : RegularCauchy) (n : ℕ) →
  dyadicRadius (canonicalSineInputScale x n) Q.·
    (precision (canonicalSineInputDepth x n) Q.+
     precision (comparisonSineInputDepth x y n)) ≤ precision n
sine-sine-left-comparison-input-error-bound x y n =
  combine-sine-comparison-input-errors
    (canonicalSineInputScale x n)
    (canonicalSineInputDepth x n)
    (comparisonSineInputDepth x y n) n
    (canonical-sine-input-error-cancels x n)
    (sine-sine-left-common-input-error-bound x y n)

sine-sine-right-comparison-input-error-bound : (x y : RegularCauchy) (n : ℕ) →
  dyadicRadius (canonicalSineInputScale y n) Q.·
    (precision (canonicalSineInputDepth y n) Q.+
     precision (comparisonSineInputDepth x y n)) ≤ precision n
sine-sine-right-comparison-input-error-bound x y n =
  combine-sine-comparison-input-errors
    (canonicalSineInputScale y n)
    (canonicalSineInputDepth y n)
    (comparisonSineInputDepth x y n) n
    (canonical-sine-input-error-cancels y n)
    (sine-sine-right-common-input-error-bound x y n)

sine-sine-left-scheduled-to-common-input-bound :
  (x y : RegularCauchy) (n : ℕ) →
  MagnitudeBound
    (sinePartialSum
      (approximation x (canonicalSineInputDepth x n))
      (canonicalSineSeriesDepth x n) Q.+
     (Q.- sinePartialSum
      (approximation x (comparisonSineInputDepth x y n))
      (canonicalSineSeriesDepth x n)))
    (precision n)
sine-sine-left-scheduled-to-common-input-bound x y n =
  let ownDepth = canonicalSineInputDepth x n
      commonDepth = comparisonSineInputDepth x y n
      seriesDepth = canonicalSineSeriesDepth x n
      error = precision ownDepth Q.+ precision commonDepth
      raw = sine-partial-sum-input-difference-bound
        (approximation x ownDepth) (approximation x commonDepth)
        error (canonicalDyadicExponent x) seriesDepth
        (precision-sum-nonnegative ownDepth commonDepth)
        (canonical-sine-input-approximation-bound x ownDepth)
        (canonical-sine-input-approximation-bound x commonDepth)
        (cauchy-difference-bound x ownDepth commonDepth)
  in
  weaken-magnitude-bound _ _ (precision n)
    (sine-sine-left-comparison-input-error-bound x y n) raw

sine-sine-right-scheduled-to-common-input-bound :
  (x y : RegularCauchy) (n : ℕ) →
  MagnitudeBound
    (sinePartialSum
      (approximation y (canonicalSineInputDepth y n))
      (canonicalSineSeriesDepth y n) Q.+
     (Q.- sinePartialSum
      (approximation y (comparisonSineInputDepth x y n))
      (canonicalSineSeriesDepth y n)))
    (precision n)
sine-sine-right-scheduled-to-common-input-bound x y n =
  let ownDepth = canonicalSineInputDepth y n
      commonDepth = comparisonSineInputDepth x y n
      seriesDepth = canonicalSineSeriesDepth y n
      error = precision ownDepth Q.+ precision commonDepth
      raw = sine-partial-sum-input-difference-bound
        (approximation y ownDepth) (approximation y commonDepth)
        error (canonicalDyadicExponent y) seriesDepth
        (precision-sum-nonnegative ownDepth commonDepth)
        (canonical-sine-input-approximation-bound y ownDepth)
        (canonical-sine-input-approximation-bound y commonDepth)
        (cauchy-difference-bound y ownDepth commonDepth)
  in
  weaken-magnitude-bound _ _ (precision n)
    (sine-sine-right-comparison-input-error-bound x y n) raw

sine-common-series-extension-bound :
  (q : Q.ℚ) (d n commonDepth : ℕ) →
  MagnitudeBound q (dyadicRadius d) →
  ℕOrder._≤_ (uniformSineCutoff d (suc n)) commonDepth →
  MagnitudeBound
    (sinePartialSum q commonDepth Q.+
     (Q.- sinePartialSum q
       (uniformSineCutoff d (suc n))))
    (precision (suc n))
sine-common-series-extension-bound q d n commonDepth qBound
  (count , count+scheduled≡common) =
  let seed = uniformSineTailSeed q d qBound
      scheduled+count≡common =
        cong (dyadicNat (suc d) ℕ.+_)
          (+-assoc (uniformSineSeedExponent d) (suc n) count) ∙
        +-assoc (dyadicNat (suc d))
          (uniformSineSeedExponent d ℕ.+ suc n) count ∙
        +-comm (uniformSineCutoff d (suc n)) count ∙
        count+scheduled≡common
  in
  subst
    (λ depth → MagnitudeBound
      (sinePartialSum q depth Q.+
       (Q.- sinePartialSum q
        (uniformSineCutoff d (suc n))))
      (precision (suc n)))
    scheduled+count≡common
    (absorbed-sine-forward-difference seed (suc n) count)

left-sine-common-series-extension-bound :
  (x y : RegularCauchy) (n : ℕ) →
  MagnitudeBound
    (sinePartialSum
      (approximation x (comparisonSineInputDepth x y n))
      (comparisonSineSeriesDepth x y n) Q.+
     (Q.- sinePartialSum
      (approximation x (comparisonSineInputDepth x y n))
      (canonicalSineSeriesDepth x n)))
    (precision (suc n))
left-sine-common-series-extension-bound x y n =
  sine-common-series-extension-bound
    (approximation x (comparisonSineInputDepth x y n))
    (canonicalDyadicExponent x) n
    (comparisonSineSeriesDepth x y n)
    (canonical-sine-input-approximation-bound x
      (comparisonSineInputDepth x y n))
    (sine-left-series-depth≤comparison x y n)

right-sine-common-series-extension-bound :
  (x y : RegularCauchy) (n : ℕ) →
  MagnitudeBound
    (sinePartialSum
      (approximation y (comparisonSineInputDepth x y n))
      (comparisonSineSeriesDepth x y n) Q.+
     (Q.- sinePartialSum
      (approximation y (comparisonSineInputDepth x y n))
      (canonicalSineSeriesDepth y n)))
    (precision (suc n))
right-sine-common-series-extension-bound x y n =
  sine-common-series-extension-bound
    (approximation y (comparisonSineInputDepth x y n))
    (canonicalDyadicExponent y) n
    (comparisonSineSeriesDepth x y n)
    (canonical-sine-input-approximation-bound y
      (comparisonSineInputDepth x y n))
    (sine-right-series-depth≤comparison x y n)

canonical-sine-pointwise-cross-forward :
  (x y : RegularCauchy) (k : ℕ) →
  let n = suc (suc (suc k))
      inputDepth = comparisonSineInputDepth x y n
      metricDepth = comparisonSineMetricDepth x y n
  in
  approximation x inputDepth ≤
    approximation y inputDepth Q.+ precision metricDepth →
  approximation y inputDepth ≤
    approximation x inputDepth Q.+ precision metricDepth →
  approximation (canonicalSineRegular x) n ≤
    approximation (canonicalSineRegular y) n Q.+ precision k
canonical-sine-pointwise-cross-forward x y k x≤y+error y≤x+error =
  let n = suc (suc (suc k))
      inputDepth = comparisonSineInputDepth x y n
      sx = canonicalSineSeriesDepth x n
      sy = canonicalSineSeriesDepth y n
      commonSeries = comparisonSineSeriesDepth x y n
      A = approximation (canonicalSineRegular x) n
      B = sinePartialSum (approximation x inputDepth) sx
      C = sinePartialSum (approximation x inputDepth) commonSeries
      D = sinePartialSum (approximation y inputDepth) commonSeries
      E = sinePartialSum (approximation y inputDepth) sy
      F = approximation (canonicalSineRegular y) n
      widenHalf : (u v : Q.ℚ) → u ≤ v Q.+ precision (suc n) →
        u ≤ v Q.+ precision n
      widenHalf u v bound = isTrans≤ u (v Q.+ precision (suc n))
        (v Q.+ precision n) bound
        (≤Monotone+ v v (precision (suc n)) (precision n)
          (isRefl≤ v) (precision-step≤ n))
      AB = magnitude-bound-forward A B (precision n)
        (sine-sine-left-scheduled-to-common-input-bound x y n)
      BC = widenHalf B C
        (magnitude-bound-backward C B (precision (suc n))
          (left-sine-common-series-extension-bound x y n))
      CD = widenHalf C D
        (magnitude-bound-forward C D (precision (suc n))
          (sine-common-series-cross-bound x y n x≤y+error y≤x+error))
      DE = widenHalf D E
        (magnitude-bound-forward D E (precision (suc n))
          (right-sine-common-series-extension-bound x y n))
      EF = magnitude-bound-backward F E (precision n)
        (sine-sine-right-scheduled-to-common-input-bound x y n)
  in
  compose-five-third-refinement A B C D E F k AB BC CD DE EF

canonical-sine-pointwise-cross-backward :
  (x y : RegularCauchy) (k : ℕ) →
  let n = suc (suc (suc k))
      inputDepth = comparisonSineInputDepth x y n
      metricDepth = comparisonSineMetricDepth x y n
  in
  approximation x inputDepth ≤
    approximation y inputDepth Q.+ precision metricDepth →
  approximation y inputDepth ≤
    approximation x inputDepth Q.+ precision metricDepth →
  approximation (canonicalSineRegular y) n ≤
    approximation (canonicalSineRegular x) n Q.+ precision k
canonical-sine-pointwise-cross-backward x y k x≤y+error y≤x+error =
  let n = suc (suc (suc k))
      inputDepth = comparisonSineInputDepth x y n
      sx = canonicalSineSeriesDepth x n
      sy = canonicalSineSeriesDepth y n
      commonSeries = comparisonSineSeriesDepth x y n
      A = approximation (canonicalSineRegular x) n
      B = sinePartialSum (approximation x inputDepth) sx
      C = sinePartialSum (approximation x inputDepth) commonSeries
      D = sinePartialSum (approximation y inputDepth) commonSeries
      E = sinePartialSum (approximation y inputDepth) sy
      F = approximation (canonicalSineRegular y) n
      widenHalf : (u v : Q.ℚ) → u ≤ v Q.+ precision (suc n) →
        u ≤ v Q.+ precision n
      widenHalf u v bound = isTrans≤ u (v Q.+ precision (suc n))
        (v Q.+ precision n) bound
        (≤Monotone+ v v (precision (suc n)) (precision n)
          (isRefl≤ v) (precision-step≤ n))
      FE = magnitude-bound-forward F E (precision n)
        (sine-sine-right-scheduled-to-common-input-bound x y n)
      ED = widenHalf E D
        (magnitude-bound-backward D E (precision (suc n))
          (right-sine-common-series-extension-bound x y n))
      DC = widenHalf D C
        (magnitude-bound-backward C D (precision (suc n))
          (sine-common-series-cross-bound x y n x≤y+error y≤x+error))
      CB = widenHalf C B
        (magnitude-bound-forward C B (precision (suc n))
          (left-sine-common-series-extension-bound x y n))
      BA = magnitude-bound-backward A B (precision n)
        (sine-sine-left-scheduled-to-common-input-bound x y n)
  in
  compose-five-third-refinement F E D C B A k FE ED DC CB BA

