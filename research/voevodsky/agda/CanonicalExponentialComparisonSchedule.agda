{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CanonicalExponentialComparisonSchedule where

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
open import TaylorPartialSumInputDifference
open import UniformTaylorInputStabilityContract
open import TaylorUniformSeedBounds
open import ExponentialTailSchedule
open import CanonicalExponentialSchedule
open import CanonicalExponentialRegularity
open import TaylorRegularityComposition

comparisonExponentialExponent : RegularCauchy → RegularCauchy → ℕ
comparisonExponentialExponent x y =
  ℕ.max (canonicalDyadicExponent x) (canonicalDyadicExponent y)

comparisonExponentialInputScale : RegularCauchy → RegularCauchy → ℕ → ℕ
comparisonExponentialInputScale x y n =
  ℕ.max (canonicalExponentialInputScale x n)
        (canonicalExponentialInputScale y n)

comparisonExponentialInputDepth : RegularCauchy → RegularCauchy → ℕ → ℕ
comparisonExponentialInputDepth x y n =
  comparisonExponentialInputScale x y n ℕ.+ suc n

comparisonExponentialSeriesDepth : RegularCauchy → RegularCauchy → ℕ → ℕ
comparisonExponentialSeriesDepth x y n =
  ℕ.max (canonicalExponentialSeriesDepth x n)
        (canonicalExponentialSeriesDepth y n)

left-input-scale≤comparison : (x y : RegularCauchy) (n : ℕ) →
  ℕOrder._≤_ (canonicalExponentialInputScale x n)
    (comparisonExponentialInputScale x y n)
left-input-scale≤comparison x y n = ℕOrder.left-≤-max

right-input-scale≤comparison : (x y : RegularCauchy) (n : ℕ) →
  ℕOrder._≤_ (canonicalExponentialInputScale y n)
    (comparisonExponentialInputScale x y n)
right-input-scale≤comparison x y n = ℕOrder.right-≤-max

left-input-depth≤comparison : (x y : RegularCauchy) (n : ℕ) →
  ℕOrder._≤_ (canonicalExponentialInputDepth x n)
    (comparisonExponentialInputDepth x y n)
left-input-depth≤comparison x y n =
  ℕOrder.≤-+-≤ (left-input-scale≤comparison x y n)
    ℕOrder.≤-refl

right-input-depth≤comparison : (x y : RegularCauchy) (n : ℕ) →
  ℕOrder._≤_ (canonicalExponentialInputDepth y n)
    (comparisonExponentialInputDepth x y n)
right-input-depth≤comparison x y n =
  ℕOrder.≤-+-≤ (right-input-scale≤comparison x y n)
    ℕOrder.≤-refl

left-series-depth≤comparison : (x y : RegularCauchy) (n : ℕ) →
  ℕOrder._≤_ (canonicalExponentialSeriesDepth x n)
    (comparisonExponentialSeriesDepth x y n)
left-series-depth≤comparison x y n = ℕOrder.left-≤-max

right-series-depth≤comparison : (x y : RegularCauchy) (n : ℕ) →
  ℕOrder._≤_ (canonicalExponentialSeriesDepth y n)
    (comparisonExponentialSeriesDepth x y n)
right-series-depth≤comparison x y n = ℕOrder.right-≤-max

left-comparison-approximation-bound :
  (x y : RegularCauchy) (n : ℕ) →
  MagnitudeBound (approximation x n)
    (dyadicRadius (comparisonExponentialExponent x y))
left-comparison-approximation-bound x y n =
  weaken-magnitude-bound _ _
    (dyadicRadius (comparisonExponentialExponent x y))
    (dyadicRadius-monotone
      (canonicalDyadicExponent x) (comparisonExponentialExponent x y)
      ℕOrder.left-≤-max)
    (canonical-input-approximation-bound x n)

right-comparison-approximation-bound :
  (x y : RegularCauchy) (n : ℕ) →
  MagnitudeBound (approximation y n)
    (dyadicRadius (comparisonExponentialExponent x y))
right-comparison-approximation-bound x y n =
  weaken-magnitude-bound _ _
    (dyadicRadius (comparisonExponentialExponent x y))
    (dyadicRadius-monotone
      (canonicalDyadicExponent y) (comparisonExponentialExponent x y)
      ℕOrder.right-≤-max)
    (canonical-input-approximation-bound y n)

comparisonExponentialCrossScale : RegularCauchy → RegularCauchy → ℕ → ℕ
comparisonExponentialCrossScale x y n =
  partialSumDifferenceExponent (comparisonExponentialExponent x y)
    (comparisonExponentialSeriesDepth x y n)

comparisonExponentialMetricDepth :
  RegularCauchy → RegularCauchy → ℕ → ℕ
comparisonExponentialMetricDepth x y n =
  comparisonExponentialCrossScale x y n ℕ.+ suc n

comparison-cross-error-cancels : (x y : RegularCauchy) (n : ℕ) →
  dyadicRadius (comparisonExponentialCrossScale x y n) Q.·
    precision (comparisonExponentialMetricDepth x y n) ≡
  precision (suc n)
comparison-cross-error-cancels x y n =
  radius-cancels-precision-shift
    (comparisonExponentialCrossScale x y n) (suc n)

common-series-cross-bound :
  (x y : RegularCauchy) (n : ℕ) →
  let inputDepth = comparisonExponentialInputDepth x y n
      seriesDepth = comparisonExponentialSeriesDepth x y n
      metricDepth = comparisonExponentialMetricDepth x y n
  in
  approximation x inputDepth ≤
    approximation y inputDepth Q.+ precision metricDepth →
  approximation y inputDepth ≤
    approximation x inputDepth Q.+ precision metricDepth →
  MagnitudeBound
    (exponentialPartialSum (approximation x inputDepth) seriesDepth Q.+
     (Q.- exponentialPartialSum
       (approximation y inputDepth) seriesDepth))
    (precision (suc n))
common-series-cross-bound x y n x≤y+error y≤x+error =
  let inputDepth = comparisonExponentialInputDepth x y n
      seriesDepth = comparisonExponentialSeriesDepth x y n
      metricDepth = comparisonExponentialMetricDepth x y n
      exponent = comparisonExponentialExponent x y
      difference = difference-magnitude-bound
        (approximation x inputDepth) (approximation y inputDepth)
        (precision metricDepth) x≤y+error y≤x+error
      raw = exponential-partial-sum-input-difference-bound
        (approximation x inputDepth) (approximation y inputDepth)
        (precision metricDepth) exponent seriesDepth
        (precision-nonnegative metricDepth)
        (left-comparison-approximation-bound x y inputDepth)
        (right-comparison-approximation-bound x y inputDepth)
        difference
  in
  subst
    (MagnitudeBound
      (exponentialPartialSum (approximation x inputDepth) seriesDepth Q.+
       (Q.- exponentialPartialSum
         (approximation y inputDepth) seriesDepth)))
    (comparison-cross-error-cancels x y n) raw

uniform-common-series-cross-bound :
  (stability : UniformExponentialPartialSumInputStability) →
  (x y : RegularCauchy) (n outputPrecision : ℕ) →
  let inputDepth = comparisonExponentialInputDepth x y n
      seriesDepth = comparisonExponentialSeriesDepth x y n
      metricDepth = uniformExponentialMetricDepth stability
        (comparisonExponentialExponent x y) outputPrecision
  in
  approximation x inputDepth ≤
    approximation y inputDepth Q.+ precision metricDepth →
  approximation y inputDepth ≤
    approximation x inputDepth Q.+ precision metricDepth →
  MagnitudeBound
    (exponentialPartialSum (approximation x inputDepth) seriesDepth Q.+
     (Q.- exponentialPartialSum
       (approximation y inputDepth) seriesDepth))
    (precision outputPrecision)
uniform-common-series-cross-bound stability x y n outputPrecision
  x≤y+error y≤x+error =
  let inputDepth = comparisonExponentialInputDepth x y n
      seriesDepth = comparisonExponentialSeriesDepth x y n
      exponent = comparisonExponentialExponent x y
      metricDepth = uniformExponentialMetricDepth stability
        exponent outputPrecision
      difference = difference-magnitude-bound
        (approximation x inputDepth) (approximation y inputDepth)
        (precision metricDepth) x≤y+error y≤x+error
      raw = uniformExponentialPartialSumDifference stability
        (approximation x inputDepth) (approximation y inputDepth)
        (precision metricDepth) exponent seriesDepth
        (precision-nonnegative metricDepth)
        (left-comparison-approximation-bound x y inputDepth)
        (right-comparison-approximation-bound x y inputDepth)
        difference
  in
  subst
    (MagnitudeBound
      (exponentialPartialSum (approximation x inputDepth) seriesDepth Q.+
       (Q.- exponentialPartialSum
         (approximation y inputDepth) seriesDepth)))
    (uniform-exponential-metric-error-cancels stability
      exponent outputPrecision)
    raw

comparison-input-error-cancels : (x y : RegularCauchy) (n : ℕ) →
  dyadicRadius (comparisonExponentialInputScale x y n) Q.·
    precision (comparisonExponentialInputDepth x y n) ≡
  precision (suc n)
comparison-input-error-cancels x y n =
  radius-cancels-precision-shift
    (comparisonExponentialInputScale x y n) (suc n)

left-common-input-error-bound : (x y : RegularCauchy) (n : ℕ) →
  dyadicRadius (canonicalExponentialInputScale x n) Q.·
    precision (comparisonExponentialInputDepth x y n) ≤
  precision (suc n)
left-common-input-error-bound x y n =
  subst
    ((dyadicRadius (canonicalExponentialInputScale x n) Q.·
      precision (comparisonExponentialInputDepth x y n)) ≤_)
    (comparison-input-error-cancels x y n)
    (≤-·o
      (dyadicRadius (canonicalExponentialInputScale x n))
      (dyadicRadius (comparisonExponentialInputScale x y n))
      (precision (comparisonExponentialInputDepth x y n))
      (precision-nonnegative (comparisonExponentialInputDepth x y n))
      (dyadicRadius-monotone
        (canonicalExponentialInputScale x n)
        (comparisonExponentialInputScale x y n)
        (left-input-scale≤comparison x y n)))

right-common-input-error-bound : (x y : RegularCauchy) (n : ℕ) →
  dyadicRadius (canonicalExponentialInputScale y n) Q.·
    precision (comparisonExponentialInputDepth x y n) ≤
  precision (suc n)
right-common-input-error-bound x y n =
  subst
    ((dyadicRadius (canonicalExponentialInputScale y n) Q.·
      precision (comparisonExponentialInputDepth x y n)) ≤_)
    (comparison-input-error-cancels x y n)
    (≤-·o
      (dyadicRadius (canonicalExponentialInputScale y n))
      (dyadicRadius (comparisonExponentialInputScale x y n))
      (precision (comparisonExponentialInputDepth x y n))
      (precision-nonnegative (comparisonExponentialInputDepth x y n))
      (dyadicRadius-monotone
        (canonicalExponentialInputScale y n)
        (comparisonExponentialInputScale x y n)
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
  dyadicRadius (canonicalExponentialInputScale x n) Q.·
    (precision (canonicalExponentialInputDepth x n) Q.+
     precision (comparisonExponentialInputDepth x y n)) ≤ precision n
left-comparison-input-error-bound x y n =
  combine-comparison-input-errors
    (canonicalExponentialInputScale x n)
    (canonicalExponentialInputDepth x n)
    (comparisonExponentialInputDepth x y n) n
    (canonical-exponential-input-error-cancels x n)
    (left-common-input-error-bound x y n)

right-comparison-input-error-bound : (x y : RegularCauchy) (n : ℕ) →
  dyadicRadius (canonicalExponentialInputScale y n) Q.·
    (precision (canonicalExponentialInputDepth y n) Q.+
     precision (comparisonExponentialInputDepth x y n)) ≤ precision n
right-comparison-input-error-bound x y n =
  combine-comparison-input-errors
    (canonicalExponentialInputScale y n)
    (canonicalExponentialInputDepth y n)
    (comparisonExponentialInputDepth x y n) n
    (canonical-exponential-input-error-cancels y n)
    (right-common-input-error-bound x y n)

left-scheduled-to-common-input-bound :
  (x y : RegularCauchy) (n : ℕ) →
  MagnitudeBound
    (exponentialPartialSum
      (approximation x (canonicalExponentialInputDepth x n))
      (canonicalExponentialSeriesDepth x n) Q.+
     (Q.- exponentialPartialSum
      (approximation x (comparisonExponentialInputDepth x y n))
      (canonicalExponentialSeriesDepth x n)))
    (precision n)
left-scheduled-to-common-input-bound x y n =
  let ownDepth = canonicalExponentialInputDepth x n
      commonDepth = comparisonExponentialInputDepth x y n
      seriesDepth = canonicalExponentialSeriesDepth x n
      error = precision ownDepth Q.+ precision commonDepth
      raw = exponential-partial-sum-input-difference-bound
        (approximation x ownDepth) (approximation x commonDepth)
        error (canonicalDyadicExponent x) seriesDepth
        (precision-sum-nonnegative ownDepth commonDepth)
        (canonical-input-approximation-bound x ownDepth)
        (canonical-input-approximation-bound x commonDepth)
        (cauchy-difference-bound x ownDepth commonDepth)
  in
  weaken-magnitude-bound _ _ (precision n)
    (left-comparison-input-error-bound x y n) raw

right-scheduled-to-common-input-bound :
  (x y : RegularCauchy) (n : ℕ) →
  MagnitudeBound
    (exponentialPartialSum
      (approximation y (canonicalExponentialInputDepth y n))
      (canonicalExponentialSeriesDepth y n) Q.+
     (Q.- exponentialPartialSum
      (approximation y (comparisonExponentialInputDepth x y n))
      (canonicalExponentialSeriesDepth y n)))
    (precision n)
right-scheduled-to-common-input-bound x y n =
  let ownDepth = canonicalExponentialInputDepth y n
      commonDepth = comparisonExponentialInputDepth x y n
      seriesDepth = canonicalExponentialSeriesDepth y n
      error = precision ownDepth Q.+ precision commonDepth
      raw = exponential-partial-sum-input-difference-bound
        (approximation y ownDepth) (approximation y commonDepth)
        error (canonicalDyadicExponent y) seriesDepth
        (precision-sum-nonnegative ownDepth commonDepth)
        (canonical-input-approximation-bound y ownDepth)
        (canonical-input-approximation-bound y commonDepth)
        (cauchy-difference-bound y ownDepth commonDepth)
  in
  weaken-magnitude-bound _ _ (precision n)
    (right-comparison-input-error-bound x y n) raw

common-series-extension-bound :
  (q : Q.ℚ) (d n commonDepth : ℕ) →
  MagnitudeBound q (dyadicRadius d) →
  ℕOrder._≤_ (uniformExponentialCutoff d (suc n)) commonDepth →
  MagnitudeBound
    (exponentialPartialSum q commonDepth Q.+
     (Q.- exponentialPartialSum q
       (uniformExponentialCutoff d (suc n))))
    (precision (suc n))
common-series-extension-bound q d n commonDepth qBound
  (count , count+scheduled≡common) =
  let seed = uniformExponentialTailSeed q d qBound
      scheduled+count≡common =
        cong (dyadicNat (suc d) ℕ.+_)
          (+-assoc (uniformExponentialSeedExponent d) (suc n) count) ∙
        +-assoc (dyadicNat (suc d))
          (uniformExponentialSeedExponent d ℕ.+ suc n) count ∙
        +-comm (uniformExponentialCutoff d (suc n)) count ∙
        count+scheduled≡common
  in
  subst
    (λ depth → MagnitudeBound
      (exponentialPartialSum q depth Q.+
       (Q.- exponentialPartialSum q
        (uniformExponentialCutoff d (suc n))))
      (precision (suc n)))
    scheduled+count≡common
    (absorbed-partial-sum-forward-difference seed (suc n) count)

left-common-series-extension-bound :
  (x y : RegularCauchy) (n : ℕ) →
  MagnitudeBound
    (exponentialPartialSum
      (approximation x (comparisonExponentialInputDepth x y n))
      (comparisonExponentialSeriesDepth x y n) Q.+
     (Q.- exponentialPartialSum
      (approximation x (comparisonExponentialInputDepth x y n))
      (canonicalExponentialSeriesDepth x n)))
    (precision (suc n))
left-common-series-extension-bound x y n =
  common-series-extension-bound
    (approximation x (comparisonExponentialInputDepth x y n))
    (canonicalDyadicExponent x) n
    (comparisonExponentialSeriesDepth x y n)
    (canonical-input-approximation-bound x
      (comparisonExponentialInputDepth x y n))
    (left-series-depth≤comparison x y n)

right-common-series-extension-bound :
  (x y : RegularCauchy) (n : ℕ) →
  MagnitudeBound
    (exponentialPartialSum
      (approximation y (comparisonExponentialInputDepth x y n))
      (comparisonExponentialSeriesDepth x y n) Q.+
     (Q.- exponentialPartialSum
      (approximation y (comparisonExponentialInputDepth x y n))
      (canonicalExponentialSeriesDepth y n)))
    (precision (suc n))
right-common-series-extension-bound x y n =
  common-series-extension-bound
    (approximation y (comparisonExponentialInputDepth x y n))
    (canonicalDyadicExponent y) n
    (comparisonExponentialSeriesDepth x y n)
    (canonical-input-approximation-bound y
      (comparisonExponentialInputDepth x y n))
    (right-series-depth≤comparison x y n)

canonical-exponential-pointwise-cross-forward :
  (x y : RegularCauchy) (k : ℕ) →
  let n = suc (suc (suc k))
      inputDepth = comparisonExponentialInputDepth x y n
      metricDepth = comparisonExponentialMetricDepth x y n
  in
  approximation x inputDepth ≤
    approximation y inputDepth Q.+ precision metricDepth →
  approximation y inputDepth ≤
    approximation x inputDepth Q.+ precision metricDepth →
  approximation (canonicalExponentialRegular x) n ≤
    approximation (canonicalExponentialRegular y) n Q.+ precision k
canonical-exponential-pointwise-cross-forward x y k x≤y+error y≤x+error =
  let n = suc (suc (suc k))
      inputDepth = comparisonExponentialInputDepth x y n
      sx = canonicalExponentialSeriesDepth x n
      sy = canonicalExponentialSeriesDepth y n
      commonSeries = comparisonExponentialSeriesDepth x y n
      A = approximation (canonicalExponentialRegular x) n
      B = exponentialPartialSum (approximation x inputDepth) sx
      C = exponentialPartialSum (approximation x inputDepth) commonSeries
      D = exponentialPartialSum (approximation y inputDepth) commonSeries
      E = exponentialPartialSum (approximation y inputDepth) sy
      F = approximation (canonicalExponentialRegular y) n
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

canonical-exponential-pointwise-cross-backward :
  (x y : RegularCauchy) (k : ℕ) →
  let n = suc (suc (suc k))
      inputDepth = comparisonExponentialInputDepth x y n
      metricDepth = comparisonExponentialMetricDepth x y n
  in
  approximation x inputDepth ≤
    approximation y inputDepth Q.+ precision metricDepth →
  approximation y inputDepth ≤
    approximation x inputDepth Q.+ precision metricDepth →
  approximation (canonicalExponentialRegular y) n ≤
    approximation (canonicalExponentialRegular x) n Q.+ precision k
canonical-exponential-pointwise-cross-backward x y k x≤y+error y≤x+error =
  let n = suc (suc (suc k))
      inputDepth = comparisonExponentialInputDepth x y n
      sx = canonicalExponentialSeriesDepth x n
      sy = canonicalExponentialSeriesDepth y n
      commonSeries = comparisonExponentialSeriesDepth x y n
      A = approximation (canonicalExponentialRegular x) n
      B = exponentialPartialSum (approximation x inputDepth) sx
      C = exponentialPartialSum (approximation x inputDepth) commonSeries
      D = exponentialPartialSum (approximation y inputDepth) commonSeries
      E = exponentialPartialSum (approximation y inputDepth) sy
      F = approximation (canonicalExponentialRegular y) n
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

