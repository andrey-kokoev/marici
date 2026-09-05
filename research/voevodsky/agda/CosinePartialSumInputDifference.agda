{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CosinePartialSumInputDifference where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; zero; suc; _+_)
import Cubical.Data.Nat.Order as ℕOrder
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import RationalAnalyticSubstrate
open import RegularCauchyStructure
open import DyadicallyBoundedCauchy
open import CauchyProductBounds
open import CauchyProductErrorBounds
open import RationalTaylorApproximants
open import TaylorTermBounds
open import TaylorPartialSumInputDifference
open import TaylorScheduleMonotonicity
open import CosineInputDifference

cosinePartialSumDifferenceExponent : ℕ → ℕ → ℕ
cosinePartialSumDifferenceExponent d zero = zero
cosinePartialSumDifferenceExponent d (suc n) =
  suc (cosinePartialSumDifferenceExponent d n ℕ.+
    cosineTermDifferenceExponent d (suc n))

cosine-partial-sum-difference-scale-step : (d n : ℕ) →
  dyadicRadius (cosinePartialSumDifferenceExponent d n) Q.+
  dyadicRadius (cosineTermDifferenceExponent d (suc n)) ≤
  dyadicRadius (cosinePartialSumDifferenceExponent d (suc n))
cosine-partial-sum-difference-scale-step d n =
  radius-sum≤successor-combined
    (cosinePartialSumDifferenceExponent d n)
    (cosineTermDifferenceExponent d (suc n))

cosine-partial-sum-difference-step : (q r : Q.ℚ) (n : ℕ) →
  cosinePartialSum q (suc n) Q.+
    (Q.- cosinePartialSum r (suc n)) ≡
  (cosinePartialSum q n Q.+ (Q.- cosinePartialSum r n)) Q.+
  (cosineTerm q (suc n) Q.+ (Q.- cosineTerm r (suc n)))
cosine-partial-sum-difference-step q r n =
  PartialSumDifferencePaths.sum-difference PreferredℚCommRing
    (cosinePartialSum q n) (cosineTerm q (suc n))
    (cosinePartialSum r n) (cosineTerm r (suc n))

cosine-partial-sum-input-difference-bound :
  (q r error : Q.ℚ) (d n : ℕ) →
  0 ≤ error →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound r (dyadicRadius d) →
  MagnitudeBound (q Q.+ (Q.- r)) error →
  MagnitudeBound
    (cosinePartialSum q n Q.+ (Q.- cosinePartialSum r n))
    (dyadicRadius (cosinePartialSumDifferenceExponent d n) Q.· error)
cosine-partial-sum-input-difference-bound q r error d zero
  errorNonnegative qBound rBound differenceBound =
  let zeroBound = nonnegative-value-magnitude 0 error
        (isRefl≤ 0) errorNonnegative errorNonnegative
      scaled = subst (MagnitudeBound 0) (sym (Q.·IdL error)) zeroBound
  in transport-magnitude _ 0 _ (Q.+InvR 1) scaled
cosine-partial-sum-input-difference-bound q r error d (suc n)
  errorNonnegative qBound rBound differenceBound =
  let partialExponent = cosinePartialSumDifferenceExponent d n
      termExponent = cosineTermDifferenceExponent d (suc n)
      partialDifference = cosinePartialSum q n Q.+
        (Q.- cosinePartialSum r n)
      termDifference = cosineTerm q (suc n) Q.+
        (Q.- cosineTerm r (suc n))
      partialBound = cosine-partial-sum-input-difference-bound
        q r error d n errorNonnegative qBound rBound differenceBound
      termBound = cosine-term-input-difference-bound
        q r error d (suc n) errorNonnegative qBound rBound differenceBound
      combined = add-magnitude-bounds _ _ _ _ partialBound termBound
      factored = subst (MagnitudeBound (partialDifference Q.+ termDifference))
        (PartialSumDifferencePaths.factor-error PreferredℚCommRing
          (dyadicRadius partialExponent) (dyadicRadius termExponent) error)
        combined
      scale≤ = ≤-·o
        (dyadicRadius partialExponent Q.+ dyadicRadius termExponent)
        (dyadicRadius (cosinePartialSumDifferenceExponent d (suc n)))
        error errorNonnegative (cosine-partial-sum-difference-scale-step d n)
      weakened = weaken-magnitude-bound _ _ _ scale≤ factored
  in
  transport-magnitude _ _ _
    (cosine-partial-sum-difference-step q r n) weakened

term-difference-exponent≤cosine-partial-sum : (d n : ℕ) →
  ℕOrder._≤_ (cosineTermDifferenceExponent d n)
    (cosinePartialSumDifferenceExponent d n)
term-difference-exponent≤cosine-partial-sum d zero = ℕOrder.≤-refl
term-difference-exponent≤cosine-partial-sum d (suc n) =
  ℕOrder.≤-trans ℕOrder.≤SumRight ℕOrder.≤-sucℕ

cosinePartialSumDifferenceExponent-step : (d n : ℕ) →
  ℕOrder._≤_ (cosinePartialSumDifferenceExponent d n)
    (cosinePartialSumDifferenceExponent d (suc n))
cosinePartialSumDifferenceExponent-step d n =
  ℕOrder.≤-trans ℕOrder.≤SumLeft ℕOrder.≤-sucℕ

cosinePartialSumDifferenceExponent-monotone : (d m n : ℕ) →
  ℕOrder._≤_ m n →
  ℕOrder._≤_ (cosinePartialSumDifferenceExponent d m)
    (cosinePartialSumDifferenceExponent d n)
cosinePartialSumDifferenceExponent-monotone d =
  monotone-from-successor (cosinePartialSumDifferenceExponent d)
    (cosinePartialSumDifferenceExponent-step d)
