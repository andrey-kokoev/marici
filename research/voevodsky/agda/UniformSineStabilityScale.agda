{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module UniformSineStabilityScale where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; suc; max; _+_; +-comm)
import Cubical.Data.Nat.Order as ℕOrder
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate
open import RegularCauchyStructure
open import CauchyProductBounds
open import DyadicallyBoundedCauchy
open import UniformSineSeedBounds
open import SinePartialSumInputDifference
open import UniformExponentialDifferenceWeights
open import UniformExponentialStabilityScale using (six≤dyadicRadiusThree)

uniformSineStabilityBase : ℕ → ℕ
uniformSineStabilityBase d =
  sinePartialSumDifferenceExponent d (dyadicNat (suc d))

uniformSineStabilityCoreExponent : ℕ → ℕ
uniformSineStabilityCoreExponent d =
  ℕ.max (uniformSineStabilityBase d) (uniformSineSeedExponent d)

uniformSineStabilityExponent : ℕ → ℕ
uniformSineStabilityExponent d =
  suc (suc (suc (uniformSineStabilityCoreExponent d)))

module SineStabilityScalePaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; _·_ to _·S_)

  initial-plus-extension-factor : (core one extension : fst R) →
    (core ·S one) +S (core ·S extension) ≡
      core ·S (one +S extension)
  initial-plus-extension-factor core one extension = solve! R

sine-stability-weight-sum-scale≤radius : (d count : ℕ) →
  dyadicRadius (uniformSineStabilityCoreExponent d) Q.·
    lateDifferenceWeightSum count ≤
  dyadicRadius (uniformSineStabilityExponent d)
sine-stability-weight-sum-scale≤radius d count =
  let coreExponent = uniformSineStabilityCoreExponent d
      core = dyadicRadius coreExponent
      sum≤eight = isTrans≤ (lateDifferenceWeightSum count) 6
        (dyadicRadius 3) (late-difference-weight-sum≤six count)
        six≤dyadicRadiusThree
      scaled≤eight = left-multiply-monotone core
        (lateDifferenceWeightSum count) (dyadicRadius 3)
        (dyadicRadius-nonnegative coreExponent) sum≤eight
      productPath = sym (dyadicRadius-add coreExponent 3) ∙
        cong dyadicRadius (+-comm coreExponent 3)
  in
  subst ((core Q.· lateDifferenceWeightSum count) ≤_)
    productPath scaled≤eight

sine-stability-dominates-initial-plus-extension : (d count : ℕ) →
  let core = dyadicRadius (uniformSineStabilityCoreExponent d)
  in
  core Q.+ (core Q.· lateExtensionWeightSum count) ≤
    dyadicRadius (uniformSineStabilityExponent d)
sine-stability-dominates-initial-plus-extension d count =
  let core = dyadicRadius (uniformSineStabilityCoreExponent d)
      extension = lateExtensionWeightSum count
      factoredRaw = SineStabilityScalePaths.initial-plus-extension-factor
        PreferredℚCommRing core 1 extension
      factored =
        cong (Q._+ (core Q.· extension)) (sym (Q.·IdR core)) ∙
        factoredRaw
      prefixPath = initial-plus-extension-weight-sum count
      prefixBound = sine-stability-weight-sum-scale≤radius d (suc count)
  in
  subst (_≤ dyadicRadius (uniformSineStabilityExponent d))
    (sym (cong (core Q.·_) prefixPath) ∙ sym factored)
    prefixBound

sine-stability-extension-weight-sum-scale≤radius : (d count : ℕ) →
  dyadicRadius (uniformSineStabilityCoreExponent d) Q.·
    lateExtensionWeightSum count ≤
  dyadicRadius (uniformSineStabilityExponent d)
sine-stability-extension-weight-sum-scale≤radius d count =
  isTrans≤
    (dyadicRadius (uniformSineStabilityCoreExponent d) Q.·
      lateExtensionWeightSum count)
    (dyadicRadius (uniformSineStabilityCoreExponent d) Q.·
      lateDifferenceWeightSum (suc count))
    (dyadicRadius (uniformSineStabilityExponent d))
    (left-multiply-monotone
      (dyadicRadius (uniformSineStabilityCoreExponent d))
      (lateExtensionWeightSum count) (lateDifferenceWeightSum (suc count))
      (dyadicRadius-nonnegative (uniformSineStabilityCoreExponent d))
      (late-extension-weight-sum≤prefix count))
    (sine-stability-weight-sum-scale≤radius d (suc count))
