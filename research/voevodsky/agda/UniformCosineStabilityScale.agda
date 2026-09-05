{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module UniformCosineStabilityScale where

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
open import UniformCosineSeedBounds
open import CosinePartialSumInputDifference
open import UniformExponentialDifferenceWeights
open import UniformExponentialStabilityScale using (six≤dyadicRadiusThree)

uniformCosineStabilityBase : ℕ → ℕ
uniformCosineStabilityBase d =
  cosinePartialSumDifferenceExponent d (dyadicNat (suc d))

uniformCosineStabilityCoreExponent : ℕ → ℕ
uniformCosineStabilityCoreExponent d =
  ℕ.max (uniformCosineStabilityBase d) (uniformCosineSeedExponent d)

uniformCosineStabilityExponent : ℕ → ℕ
uniformCosineStabilityExponent d =
  suc (suc (suc (uniformCosineStabilityCoreExponent d)))

module CosineStabilityScalePaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; _·_ to _·S_)

  initial-plus-extension-factor : (core one extension : fst R) →
    (core ·S one) +S (core ·S extension) ≡
      core ·S (one +S extension)
  initial-plus-extension-factor core one extension = solve! R

cosine-stability-weight-sum-scale≤radius : (d count : ℕ) →
  dyadicRadius (uniformCosineStabilityCoreExponent d) Q.·
    lateDifferenceWeightSum count ≤
  dyadicRadius (uniformCosineStabilityExponent d)
cosine-stability-weight-sum-scale≤radius d count =
  let coreExponent = uniformCosineStabilityCoreExponent d
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

cosine-stability-dominates-initial-plus-extension : (d count : ℕ) →
  let core = dyadicRadius (uniformCosineStabilityCoreExponent d)
  in
  core Q.+ (core Q.· lateExtensionWeightSum count) ≤
    dyadicRadius (uniformCosineStabilityExponent d)
cosine-stability-dominates-initial-plus-extension d count =
  let core = dyadicRadius (uniformCosineStabilityCoreExponent d)
      extension = lateExtensionWeightSum count
      factoredRaw = CosineStabilityScalePaths.initial-plus-extension-factor
        PreferredℚCommRing core 1 extension
      factored =
        cong (Q._+ (core Q.· extension)) (sym (Q.·IdR core)) ∙
        factoredRaw
      prefixPath = initial-plus-extension-weight-sum count
      prefixBound = cosine-stability-weight-sum-scale≤radius d (suc count)
  in
  subst (_≤ dyadicRadius (uniformCosineStabilityExponent d))
    (sym (cong (core Q.·_) prefixPath) ∙ sym factored)
    prefixBound

cosine-stability-extension-weight-sum-scale≤radius : (d count : ℕ) →
  dyadicRadius (uniformCosineStabilityCoreExponent d) Q.·
    lateExtensionWeightSum count ≤
  dyadicRadius (uniformCosineStabilityExponent d)
cosine-stability-extension-weight-sum-scale≤radius d count =
  isTrans≤
    (dyadicRadius (uniformCosineStabilityCoreExponent d) Q.·
      lateExtensionWeightSum count)
    (dyadicRadius (uniformCosineStabilityCoreExponent d) Q.·
      lateDifferenceWeightSum (suc count))
    (dyadicRadius (uniformCosineStabilityExponent d))
    (left-multiply-monotone
      (dyadicRadius (uniformCosineStabilityCoreExponent d))
      (lateExtensionWeightSum count) (lateDifferenceWeightSum (suc count))
      (dyadicRadius-nonnegative (uniformCosineStabilityCoreExponent d))
      (late-extension-weight-sum≤prefix count))
    (cosine-stability-weight-sum-scale≤radius d (suc count))
