{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CanonicalExponentialUniformComparison where

open import Cubical.Data.Nat using (ℕ; suc)
import Cubical.Data.Nat.Order as ℕOrder
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import RegularCauchyStructure
open import RationalTaylorApproximants
open import UniformTaylorInputStabilityContract
open import CanonicalExponentialSchedule
open import CanonicalExponentialRegularity
open import CanonicalExponentialComparisonSchedule
open import TaylorRegularityComposition

canonical-exponential-uniform-pointwise-forward :
  (stability : UniformExponentialPartialSumInputStability) →
  (x y : RegularCauchy) (k n : ℕ) →
  ℕOrder._≤_ (suc (suc (suc k))) n →
  let inputDepth = comparisonExponentialInputDepth x y n
      metricDepth = uniformExponentialMetricDepth stability
        (comparisonExponentialExponent x y) (suc (suc (suc k)))
  in
  approximation x inputDepth ≤ approximation y inputDepth Q.+ precision metricDepth →
  approximation y inputDepth ≤ approximation x inputDepth Q.+ precision metricDepth →
  approximation (canonicalExponentialRegular x) n ≤
    approximation (canonicalExponentialRegular y) n Q.+ precision k
canonical-exponential-uniform-pointwise-forward stability x y k n k3≤n x≤y y≤x =
  let k3 = suc (suc (suc k)); input = comparisonExponentialInputDepth x y n
      sx = canonicalExponentialSeriesDepth x n; sy = canonicalExponentialSeriesDepth y n
      common = comparisonExponentialSeriesDepth x y n
      A = approximation (canonicalExponentialRegular x) n
      B = exponentialPartialSum (approximation x input) sx
      C = exponentialPartialSum (approximation x input) common
      D = exponentialPartialSum (approximation y input) common
      E = exponentialPartialSum (approximation y input) sy
      F = approximation (canonicalExponentialRegular y) n
      widen : (u v : Q.ℚ) → u ≤ v Q.+ precision n → u ≤ v Q.+ precision k3
      widen u v p = isTrans≤ u (v Q.+ precision n) (v Q.+ precision k3) p
        (≤Monotone+ v v (precision n) (precision k3) (isRefl≤ v)
          (precision-antitone k3 n k3≤n))
      half : (u v : Q.ℚ) → u ≤ v Q.+ precision (suc n) → u ≤ v Q.+ precision n
      half u v p = isTrans≤ u (v Q.+ precision (suc n)) (v Q.+ precision n) p
        (≤Monotone+ v v (precision (suc n)) (precision n) (isRefl≤ v) (precision-step≤ n))
      AB = widen A B (magnitude-bound-forward A B (precision n)
        (left-scheduled-to-common-input-bound x y n))
      BC = widen B C (half B C (magnitude-bound-backward C B (precision (suc n))
        (left-common-series-extension-bound x y n)))
      CD = magnitude-bound-forward C D (precision k3)
        (uniform-common-series-cross-bound stability x y n k3 x≤y y≤x)
      DE = widen D E (half D E (magnitude-bound-forward D E (precision (suc n))
        (right-common-series-extension-bound x y n)))
      EF = widen E F (magnitude-bound-backward F E (precision n)
        (right-scheduled-to-common-input-bound x y n))
  in compose-five-third-refinement A B C D E F k AB BC CD DE EF

canonical-exponential-uniform-pointwise-backward :
  (stability : UniformExponentialPartialSumInputStability) →
  (x y : RegularCauchy) (k n : ℕ) →
  ℕOrder._≤_ (suc (suc (suc k))) n →
  let inputDepth = comparisonExponentialInputDepth x y n
      metricDepth = uniformExponentialMetricDepth stability
        (comparisonExponentialExponent x y) (suc (suc (suc k)))
  in
  approximation x inputDepth ≤ approximation y inputDepth Q.+ precision metricDepth →
  approximation y inputDepth ≤ approximation x inputDepth Q.+ precision metricDepth →
  approximation (canonicalExponentialRegular y) n ≤
    approximation (canonicalExponentialRegular x) n Q.+ precision k
canonical-exponential-uniform-pointwise-backward stability x y k n k3≤n x≤y y≤x =
  let k3 = suc (suc (suc k)); input = comparisonExponentialInputDepth x y n
      sx = canonicalExponentialSeriesDepth x n; sy = canonicalExponentialSeriesDepth y n
      common = comparisonExponentialSeriesDepth x y n
      A = approximation (canonicalExponentialRegular x) n
      B = exponentialPartialSum (approximation x input) sx
      C = exponentialPartialSum (approximation x input) common
      D = exponentialPartialSum (approximation y input) common
      E = exponentialPartialSum (approximation y input) sy
      F = approximation (canonicalExponentialRegular y) n
      widen : (u v : Q.ℚ) → u ≤ v Q.+ precision n → u ≤ v Q.+ precision k3
      widen u v p = isTrans≤ u (v Q.+ precision n) (v Q.+ precision k3) p
        (≤Monotone+ v v (precision n) (precision k3) (isRefl≤ v)
          (precision-antitone k3 n k3≤n))
      half : (u v : Q.ℚ) → u ≤ v Q.+ precision (suc n) → u ≤ v Q.+ precision n
      half u v p = isTrans≤ u (v Q.+ precision (suc n)) (v Q.+ precision n) p
        (≤Monotone+ v v (precision (suc n)) (precision n) (isRefl≤ v) (precision-step≤ n))
      FE = widen F E (magnitude-bound-forward F E (precision n)
        (right-scheduled-to-common-input-bound x y n))
      ED = widen E D (half E D (magnitude-bound-backward D E (precision (suc n))
        (right-common-series-extension-bound x y n)))
      DC = magnitude-bound-backward C D (precision k3)
        (uniform-common-series-cross-bound stability x y n k3 x≤y y≤x)
      CB = widen C B (half C B (magnitude-bound-forward C B (precision (suc n))
        (left-common-series-extension-bound x y n)))
      BA = widen B A (magnitude-bound-backward A B (precision n)
        (left-scheduled-to-common-input-bound x y n))
  in compose-five-third-refinement F E D C B A k FE ED DC CB BA
