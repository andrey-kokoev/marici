{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module UniformExponentialStabilityScale where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; zero; suc; max; _+_; +-comm)
import Cubical.Data.Nat.Order as ℕOrder
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
import Cubical.Data.Int.Order as ℤOrder
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate
open import RegularCauchyStructure
open import CauchyProductBounds
open import DyadicallyBoundedCauchy
open import TaylorTermBounds
open import TaylorPartialSumInputDifference
open import TaylorInputDifference
open import TaylorUniformSeedBounds
open import UniformExponentialDifferenceWeights

term-difference-exponent≤partial-sum-exponent : (d n : ℕ) →
  ℕOrder._≤_ (termDifferenceExponent d n)
    (partialSumDifferenceExponent d n)
term-difference-exponent≤partial-sum-exponent d zero = ℕOrder.≤-refl
term-difference-exponent≤partial-sum-exponent d (suc n) =
  ℕOrder.≤-trans ℕOrder.≤SumRight ℕOrder.≤-sucℕ

uniformExponentialStabilityBase : ℕ → ℕ
uniformExponentialStabilityBase d =
  partialSumDifferenceExponent d (dyadicNat (suc d))

uniformExponentialStabilityExponent : ℕ → ℕ
uniformExponentialStabilityCoreExponent : ℕ → ℕ
uniformExponentialStabilityCoreExponent d =
  ℕ.max (uniformExponentialStabilityBase d)
        (uniformExponentialSeedExponent d)

uniformExponentialStabilityExponent d =
  suc (suc (suc (uniformExponentialStabilityCoreExponent d)))

initial-term-difference-scale≤stability-core : (d : ℕ) →
  dyadicRadius
    (termDifferenceExponent d (dyadicNat (suc d))) ≤
  dyadicRadius (uniformExponentialStabilityCoreExponent d)
initial-term-difference-scale≤stability-core d =
  dyadicRadius-monotone
    (termDifferenceExponent d (dyadicNat (suc d)))
    (uniformExponentialStabilityCoreExponent d)
    (ℕOrder.≤-trans
      (term-difference-exponent≤partial-sum-exponent d
        (dyadicNat (suc d)))
      ℕOrder.left-≤-max)

module StabilityScalePaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; _·_ to _·S_)

  initial-plus-extension-factor : (core one extension : fst R) →
    (core ·S one) +S (core ·S extension) ≡
      core ·S (one +S extension)
  initial-plus-extension-factor core one extension = solve! R

uniform-stability-dominates-double-base : (d : ℕ) →
  dyadicRadius (uniformExponentialStabilityBase d) Q.+
  dyadicRadius (uniformExponentialStabilityBase d) ≤
  dyadicRadius (uniformExponentialStabilityExponent d)
uniform-stability-dominates-double-base d =
  let base = uniformExponentialStabilityBase d
      common = ℕ.max base (uniformExponentialSeedExponent d)
      base≤common = dyadicRadius-monotone base common ℕOrder.left-≤-max
  in
  let double≤firstSuccessor = subst
        ((dyadicRadius base Q.+ dyadicRadius base) ≤_)
        refl
        (≤Monotone+ (dyadicRadius base) (dyadicRadius common)
          (dyadicRadius base) (dyadicRadius common) base≤common base≤common)
  in
  isTrans≤ (dyadicRadius base Q.+ dyadicRadius base)
    (dyadicRadius (suc common))
    (dyadicRadius (suc (suc (suc common))))
    double≤firstSuccessor
    (dyadicRadius-monotone (suc common) (suc (suc (suc common)))
      (ℕOrder.≤-trans ℕOrder.≤-sucℕ ℕOrder.≤-sucℕ))

sixℚ : Q.ℚ
sixℚ = 6

six-plus-two≡eight : sixℚ Q.+ dyadicRadius 1 ≡ dyadicRadius 3
six-plus-two≡eight = refl

six≤dyadicRadiusThree : sixℚ ≤ dyadicRadius 3
six≤dyadicRadiusThree =
  subst (sixℚ ≤_) six-plus-two≡eight
    (≤-add-nonnegative sixℚ (dyadicRadius 1)
      (dyadicRadius-nonnegative 1))

stability-weight-sum-scale≤radius : (d count : ℕ) →
  dyadicRadius (uniformExponentialStabilityCoreExponent d) Q.·
    lateDifferenceWeightSum count ≤
  dyadicRadius (uniformExponentialStabilityExponent d)
stability-weight-sum-scale≤radius d count =
  let coreExponent = uniformExponentialStabilityCoreExponent d
      core = dyadicRadius coreExponent
      sum≤eight = isTrans≤ (lateDifferenceWeightSum count) sixℚ
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

uniform-stability-dominates-initial-plus-extension : (d count : ℕ) →
  let core = dyadicRadius (uniformExponentialStabilityCoreExponent d)
  in
  core Q.+ (core Q.· lateExtensionWeightSum count) ≤
    dyadicRadius (uniformExponentialStabilityExponent d)
uniform-stability-dominates-initial-plus-extension d count =
  let core = dyadicRadius (uniformExponentialStabilityCoreExponent d)
      extension = lateExtensionWeightSum count
      factoredRaw = StabilityScalePaths.initial-plus-extension-factor
        PreferredℚCommRing core 1 extension
      factored =
        cong (Q._+ (core Q.· extension)) (sym (Q.·IdR core)) ∙
        factoredRaw
      prefixPath = initial-plus-extension-weight-sum count
      prefixBound = stability-weight-sum-scale≤radius d (suc count)
  in
  subst (_≤ dyadicRadius (uniformExponentialStabilityExponent d))
    (sym (cong (core Q.·_) prefixPath) ∙ sym factored)
    prefixBound

stability-extension-weight-sum-scale≤radius : (d count : ℕ) →
  dyadicRadius (uniformExponentialStabilityCoreExponent d) Q.·
    lateExtensionWeightSum count ≤
  dyadicRadius (uniformExponentialStabilityExponent d)
stability-extension-weight-sum-scale≤radius d count =
  let coreExponent = uniformExponentialStabilityCoreExponent d
      core = dyadicRadius coreExponent
      scaled≤prefix = left-multiply-monotone core
        (lateExtensionWeightSum count)
        (lateDifferenceWeightSum (suc count))
        (dyadicRadius-nonnegative coreExponent)
        (late-extension-weight-sum≤prefix count)
  in
  isTrans≤ (core Q.· lateExtensionWeightSum count)
    (core Q.· lateDifferenceWeightSum (suc count))
    (dyadicRadius (uniformExponentialStabilityExponent d))
    scaled≤prefix (stability-weight-sum-scale≤radius d (suc count))

uniform-stability-dominates-double-seed : (d : ℕ) →
  dyadicRadius (uniformExponentialSeedExponent d) Q.+
  dyadicRadius (uniformExponentialSeedExponent d) ≤
  dyadicRadius (uniformExponentialStabilityExponent d)
uniform-stability-dominates-double-seed d =
  let seed = uniformExponentialSeedExponent d
      common = ℕ.max (uniformExponentialStabilityBase d) seed
      seed≤common = dyadicRadius-monotone seed common ℕOrder.right-≤-max
  in
  let double≤firstSuccessor = subst
        ((dyadicRadius seed Q.+ dyadicRadius seed) ≤_)
        refl
        (≤Monotone+ (dyadicRadius seed) (dyadicRadius common)
          (dyadicRadius seed) (dyadicRadius common) seed≤common seed≤common)
  in
  isTrans≤ (dyadicRadius seed Q.+ dyadicRadius seed)
    (dyadicRadius (suc common))
    (dyadicRadius (suc (suc (suc common))))
    double≤firstSuccessor
    (dyadicRadius-monotone (suc common) (suc (suc (suc common)))
      (ℕOrder.≤-trans ℕOrder.≤-sucℕ ℕOrder.≤-sucℕ))
