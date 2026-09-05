{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CanonicalSineUniformComparison where

open import Cubical.Data.Nat using (ℕ; suc)
import Cubical.Data.Nat.Order as ℕOrder
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import RegularCauchyStructure
open import RationalTaylorApproximants
open import RationalSineTaylorApproximants
open import UniformSineInputStabilityContract
open import CanonicalSineSchedule
open import CanonicalSineRegularity
open import CanonicalSineComparisonSchedule
open import TaylorRegularityComposition

canonical-sine-uniform-pointwise-forward :
  (stability : UniformSinePartialSumInputStability) →
  (x y : RegularCauchy) (k n : ℕ) →
  ℕOrder._≤_ (suc (suc (suc k))) n →
  let inputDepth = comparisonSineInputDepth x y n
      metricDepth = uniformSineMetricDepth stability
        (comparisonSineExponent x y) (suc (suc (suc k)))
  in
  approximation x inputDepth ≤ approximation y inputDepth Q.+ precision metricDepth →
  approximation y inputDepth ≤ approximation x inputDepth Q.+ precision metricDepth →
  approximation (canonicalSineRegular x) n ≤
    approximation (canonicalSineRegular y) n Q.+ precision k
canonical-sine-uniform-pointwise-forward stability x y k n k3≤n x≤y y≤x =
  let k3 = suc (suc (suc k)); input = comparisonSineInputDepth x y n
      sx = canonicalSineSeriesDepth x n; sy = canonicalSineSeriesDepth y n
      common = comparisonSineSeriesDepth x y n
      A = approximation (canonicalSineRegular x) n
      B = sinePartialSum (approximation x input) sx
      C = sinePartialSum (approximation x input) common
      D = sinePartialSum (approximation y input) common
      E = sinePartialSum (approximation y input) sy
      F = approximation (canonicalSineRegular y) n
      widen : (u v : Q.ℚ) → u ≤ v Q.+ precision n → u ≤ v Q.+ precision k3
      widen u v p = isTrans≤ u (v Q.+ precision n) (v Q.+ precision k3) p
        (≤Monotone+ v v (precision n) (precision k3) (isRefl≤ v)
          (precision-antitone k3 n k3≤n))
      half : (u v : Q.ℚ) → u ≤ v Q.+ precision (suc n) → u ≤ v Q.+ precision n
      half u v p = isTrans≤ u (v Q.+ precision (suc n)) (v Q.+ precision n) p
        (≤Monotone+ v v (precision (suc n)) (precision n) (isRefl≤ v) (precision-step≤ n))
      AB = widen A B (magnitude-bound-forward A B (precision n)
        (sine-sine-left-scheduled-to-common-input-bound x y n))
      BC = widen B C (half B C (magnitude-bound-backward C B (precision (suc n))
        (left-sine-common-series-extension-bound x y n)))
      CD = magnitude-bound-forward C D (precision k3)
        (uniform-sine-common-series-cross-bound stability x y n k3 x≤y y≤x)
      DE = widen D E (half D E (magnitude-bound-forward D E (precision (suc n))
        (right-sine-common-series-extension-bound x y n)))
      EF = widen E F (magnitude-bound-backward F E (precision n)
        (sine-sine-right-scheduled-to-common-input-bound x y n))
  in compose-five-third-refinement A B C D E F k AB BC CD DE EF

canonical-sine-uniform-pointwise-backward :
  (stability : UniformSinePartialSumInputStability) →
  (x y : RegularCauchy) (k n : ℕ) →
  ℕOrder._≤_ (suc (suc (suc k))) n →
  let inputDepth = comparisonSineInputDepth x y n
      metricDepth = uniformSineMetricDepth stability
        (comparisonSineExponent x y) (suc (suc (suc k)))
  in
  approximation x inputDepth ≤ approximation y inputDepth Q.+ precision metricDepth →
  approximation y inputDepth ≤ approximation x inputDepth Q.+ precision metricDepth →
  approximation (canonicalSineRegular y) n ≤
    approximation (canonicalSineRegular x) n Q.+ precision k
canonical-sine-uniform-pointwise-backward stability x y k n k3≤n x≤y y≤x =
  let k3 = suc (suc (suc k)); input = comparisonSineInputDepth x y n
      sx = canonicalSineSeriesDepth x n; sy = canonicalSineSeriesDepth y n
      common = comparisonSineSeriesDepth x y n
      A = approximation (canonicalSineRegular x) n
      B = sinePartialSum (approximation x input) sx
      C = sinePartialSum (approximation x input) common
      D = sinePartialSum (approximation y input) common
      E = sinePartialSum (approximation y input) sy
      F = approximation (canonicalSineRegular y) n
      widen : (u v : Q.ℚ) → u ≤ v Q.+ precision n → u ≤ v Q.+ precision k3
      widen u v p = isTrans≤ u (v Q.+ precision n) (v Q.+ precision k3) p
        (≤Monotone+ v v (precision n) (precision k3) (isRefl≤ v)
          (precision-antitone k3 n k3≤n))
      half : (u v : Q.ℚ) → u ≤ v Q.+ precision (suc n) → u ≤ v Q.+ precision n
      half u v p = isTrans≤ u (v Q.+ precision (suc n)) (v Q.+ precision n) p
        (≤Monotone+ v v (precision (suc n)) (precision n) (isRefl≤ v) (precision-step≤ n))
      FE = widen F E (magnitude-bound-forward F E (precision n)
        (sine-sine-right-scheduled-to-common-input-bound x y n))
      ED = widen E D (half E D (magnitude-bound-backward D E (precision (suc n))
        (right-sine-common-series-extension-bound x y n)))
      DC = magnitude-bound-backward C D (precision k3)
        (uniform-sine-common-series-cross-bound stability x y n k3 x≤y y≤x)
      CB = widen C B (half C B (magnitude-bound-forward C B (precision (suc n))
        (left-sine-common-series-extension-bound x y n)))
      BA = widen B A (magnitude-bound-backward A B (precision n)
        (sine-sine-left-scheduled-to-common-input-bound x y n))
  in compose-five-third-refinement F E D C B A k FE ED DC CB BA
