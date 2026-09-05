{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module SinePartialSumInputDifference where

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
open import RationalSineTaylorApproximants
open import TaylorTermBounds
open import TaylorPartialSumInputDifference
open import TaylorScheduleMonotonicity
open import SineInputDifference

sinePartialSumDifferenceExponent : ℕ → ℕ → ℕ
sinePartialSumDifferenceExponent d zero = zero
sinePartialSumDifferenceExponent d (suc n) =
  suc (sinePartialSumDifferenceExponent d n ℕ.+
    sineTermDifferenceExponent d (suc n))

sine-partial-sum-difference-scale-step : (d n : ℕ) →
  dyadicRadius (sinePartialSumDifferenceExponent d n) Q.+
  dyadicRadius (sineTermDifferenceExponent d (suc n)) ≤
  dyadicRadius (sinePartialSumDifferenceExponent d (suc n))
sine-partial-sum-difference-scale-step d n =
  radius-sum≤successor-combined
    (sinePartialSumDifferenceExponent d n)
    (sineTermDifferenceExponent d (suc n))

sine-partial-sum-difference-step : (q r : Q.ℚ) (n : ℕ) →
  sinePartialSum q (suc n) Q.+
    (Q.- sinePartialSum r (suc n)) ≡
  (sinePartialSum q n Q.+ (Q.- sinePartialSum r n)) Q.+
  (sineTerm q (suc n) Q.+ (Q.- sineTerm r (suc n)))
sine-partial-sum-difference-step q r n =
  PartialSumDifferencePaths.sum-difference PreferredℚCommRing
    (sinePartialSum q n) (sineTerm q (suc n))
    (sinePartialSum r n) (sineTerm r (suc n))

sine-partial-sum-input-difference-bound :
  (q r error : Q.ℚ) (d n : ℕ) →
  0 ≤ error →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound r (dyadicRadius d) →
  MagnitudeBound (q Q.+ (Q.- r)) error →
  MagnitudeBound
    (sinePartialSum q n Q.+ (Q.- sinePartialSum r n))
    (dyadicRadius (sinePartialSumDifferenceExponent d n) Q.· error)
sine-partial-sum-input-difference-bound q r error d zero
  errorNonnegative qBound rBound differenceBound =
  subst (MagnitudeBound (q Q.+ (Q.- r)))
    (sym (Q.·IdL error)) differenceBound
sine-partial-sum-input-difference-bound q r error d (suc n)
  errorNonnegative qBound rBound differenceBound =
  let partialExponent = sinePartialSumDifferenceExponent d n
      termExponent = sineTermDifferenceExponent d (suc n)
      partialDifference = sinePartialSum q n Q.+
        (Q.- sinePartialSum r n)
      termDifference = sineTerm q (suc n) Q.+
        (Q.- sineTerm r (suc n))
      partialBound = sine-partial-sum-input-difference-bound
        q r error d n errorNonnegative qBound rBound differenceBound
      termBound = sine-term-input-difference-bound
        q r error d (suc n) errorNonnegative qBound rBound differenceBound
      combined = add-magnitude-bounds _ _ _ _ partialBound termBound
      factored = subst (MagnitudeBound (partialDifference Q.+ termDifference))
        (PartialSumDifferencePaths.factor-error PreferredℚCommRing
          (dyadicRadius partialExponent) (dyadicRadius termExponent) error)
        combined
      scale≤ = ≤-·o
        (dyadicRadius partialExponent Q.+ dyadicRadius termExponent)
        (dyadicRadius (sinePartialSumDifferenceExponent d (suc n)))
        error errorNonnegative (sine-partial-sum-difference-scale-step d n)
      weakened = weaken-magnitude-bound _ _ _ scale≤ factored
  in
  transport-magnitude _ _ _
    (sine-partial-sum-difference-step q r n) weakened

term-difference-exponent≤sine-partial-sum : (d n : ℕ) →
  ℕOrder._≤_ (sineTermDifferenceExponent d n)
    (sinePartialSumDifferenceExponent d n)
term-difference-exponent≤sine-partial-sum d zero = ℕOrder.≤-refl
term-difference-exponent≤sine-partial-sum d (suc n) =
  ℕOrder.≤-trans ℕOrder.≤SumRight ℕOrder.≤-sucℕ

sinePartialSumDifferenceExponent-step : (d n : ℕ) →
  ℕOrder._≤_ (sinePartialSumDifferenceExponent d n)
    (sinePartialSumDifferenceExponent d (suc n))
sinePartialSumDifferenceExponent-step d n =
  ℕOrder.≤-trans ℕOrder.≤SumLeft ℕOrder.≤-sucℕ

sinePartialSumDifferenceExponent-monotone : (d m n : ℕ) →
  ℕOrder._≤_ m n →
  ℕOrder._≤_ (sinePartialSumDifferenceExponent d m)
    (sinePartialSumDifferenceExponent d n)
sinePartialSumDifferenceExponent-monotone d =
  monotone-from-successor (sinePartialSumDifferenceExponent d)
    (sinePartialSumDifferenceExponent-step d)
