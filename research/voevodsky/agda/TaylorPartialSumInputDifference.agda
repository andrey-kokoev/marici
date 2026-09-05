{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module TaylorPartialSumInputDifference where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; zero; suc; _+_)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate
open import RationalTaylorApproximants
open import DyadicallyBoundedCauchy
open import CauchyProductBounds
open import CauchyProductErrorBounds
open import TaylorTermBounds
open import TaylorUniformSeedBounds
open import TaylorInputDifference

module PartialSumDifferencePaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R)
    renaming (_+_ to _+S_; _·_ to _·S_; -_ to -S_)

  sum-difference : (a b c d : fst R) →
    (a +S b) +S (-S (c +S d)) ≡
    (a +S (-S c)) +S (b +S (-S d))
  sum-difference a b c d = solve! R

  factor-error : (A B e : fst R) →
    (A ·S e) +S (B ·S e) ≡ (A +S B) ·S e
  factor-error A B e = solve! R

partialSumDifferenceExponent : ℕ → ℕ → ℕ
partialSumDifferenceExponent d zero = zero
partialSumDifferenceExponent d (suc n) =
  suc (partialSumDifferenceExponent d n ℕ.+ termDifferenceExponent d (suc n))

partial-sum-difference-scale-step : (d n : ℕ) →
  dyadicRadius (partialSumDifferenceExponent d n) Q.+
  dyadicRadius (termDifferenceExponent d (suc n)) ≤
  dyadicRadius (partialSumDifferenceExponent d (suc n))
partial-sum-difference-scale-step d n =
  radius-sum≤successor-combined
    (partialSumDifferenceExponent d n) (termDifferenceExponent d (suc n))

exponential-partial-sum-difference-step :
  (q r : Q.ℚ) (n : ℕ) →
  exponentialPartialSum q (suc n) Q.+
    (Q.- exponentialPartialSum r (suc n)) ≡
  (exponentialPartialSum q n Q.+
    (Q.- exponentialPartialSum r n)) Q.+
  (exponentialTerm q (suc n) Q.+ (Q.- exponentialTerm r (suc n)))
exponential-partial-sum-difference-step q r n =
  PartialSumDifferencePaths.sum-difference PreferredℚCommRing
    (exponentialPartialSum q n) (exponentialTerm q (suc n))
    (exponentialPartialSum r n) (exponentialTerm r (suc n))

exponential-partial-sum-input-difference-bound :
  (q r e : Q.ℚ) (d n : ℕ) →
  0 ≤ e →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound r (dyadicRadius d) →
  MagnitudeBound (q Q.+ (Q.- r)) e →
  MagnitudeBound
    (exponentialPartialSum q n Q.+ (Q.- exponentialPartialSum r n))
    (dyadicRadius (partialSumDifferenceExponent d n) Q.· e)
exponential-partial-sum-input-difference-bound q r e d zero
    eNonnegative qBound rBound differenceBound =
  let zeroBound = nonnegative-value-magnitude 0 e
        (isRefl≤ 0) eNonnegative eNonnegative
      scaledZeroBound = subst (MagnitudeBound 0)
        (sym (Q.·IdL e)) zeroBound
  in
  transport-magnitude _ 0 _ (Q.+InvR 1) scaledZeroBound
exponential-partial-sum-input-difference-bound q r e d (suc n)
    eNonnegative qBound rBound differenceBound =
  let partialScale = dyadicRadius (partialSumDifferenceExponent d n)
      termScale = dyadicRadius (termDifferenceExponent d (suc n))
      partialDifference = exponentialPartialSum q n Q.+
        (Q.- exponentialPartialSum r n)
      termDifference = exponentialTerm q (suc n) Q.+
        (Q.- exponentialTerm r (suc n))
      partialBound = exponential-partial-sum-input-difference-bound
        q r e d n eNonnegative qBound rBound differenceBound
      termBound = exponential-term-input-difference-bound
        q r e d (suc n) eNonnegative qBound rBound differenceBound
      combined = add-magnitude-bounds
        partialDifference (partialScale Q.· e)
        termDifference (termScale Q.· e)
        partialBound termBound
      factored = subst (MagnitudeBound (partialDifference Q.+ termDifference))
        (PartialSumDifferencePaths.factor-error PreferredℚCommRing
          partialScale termScale e)
        combined
      targetScale = dyadicRadius (partialSumDifferenceExponent d (suc n))
      scaleBound = subst2 _≤_
        (Q.·Comm e (partialScale Q.+ termScale))
        (Q.·Comm e targetScale)
        (left-multiply-monotone e (partialScale Q.+ termScale) targetScale
          eNonnegative (partial-sum-difference-scale-step d n))
      weakened = weaken-magnitude-bound _ _ (targetScale Q.· e)
        scaleBound factored
  in
  transport-magnitude _ _ _
    (exponential-partial-sum-difference-step q r n) weakened
