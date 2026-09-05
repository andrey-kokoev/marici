{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module TaylorScheduleMonotonicity where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; zero; suc; _+_)
import Cubical.Data.Nat.Order as ℕOrder
open import DyadicallyBoundedCauchy
open import TaylorUniformSeedBounds
open import TaylorPartialSumInputDifference

monotone-from-successor :
  (f : ℕ → ℕ) →
  ((n : ℕ) → ℕOrder._≤_ (f n) (f (suc n))) →
  (m n : ℕ) → ℕOrder._≤_ m n → ℕOrder._≤_ (f m) (f n)
monotone-from-successor f step m n (extra , extra+m≡n) =
  subst (ℕOrder._≤_ (f m)) (cong f extra+m≡n)
    (advance extra m)
  where
  advance : (extra start : ℕ) →
    ℕOrder._≤_ (f start) (f (extra ℕ.+ start))
  advance zero start = ℕOrder.≤-refl
  advance (suc extra) start =
    ℕOrder.≤-trans (advance extra start) (step (extra ℕ.+ start))

termPowerExponent-step : (d n : ℕ) →
  ℕOrder._≤_ (termPowerExponent d n) (termPowerExponent d (suc n))
termPowerExponent-step d n = ℕOrder.≤SumLeft

termPowerExponent-monotone : (d m n : ℕ) →
  ℕOrder._≤_ m n →
  ℕOrder._≤_ (termPowerExponent d m) (termPowerExponent d n)
termPowerExponent-monotone d =
  monotone-from-successor (termPowerExponent d) (termPowerExponent-step d)

termDifferenceExponent-step : (d n : ℕ) →
  ℕOrder._≤_ (termDifferenceExponent d n)
    (termDifferenceExponent d (suc n))
termDifferenceExponent-step d n =
  let current = termDifferenceExponent d n
      power = termPowerExponent d n
      intoSum : ℕOrder._≤_ current ((current ℕ.+ d) ℕ.+ power)
      intoSum = subst (ℕOrder._≤_ current)
        (ℕ.+-assoc current d power) ℕOrder.≤SumLeft
  in
  ℕOrder.≤-trans intoSum ℕOrder.≤-sucℕ

termDifferenceExponent-monotone : (d m n : ℕ) →
  ℕOrder._≤_ m n →
  ℕOrder._≤_ (termDifferenceExponent d m)
    (termDifferenceExponent d n)
termDifferenceExponent-monotone d =
  monotone-from-successor
    (termDifferenceExponent d) (termDifferenceExponent-step d)

partialSumDifferenceExponent-step : (d n : ℕ) →
  ℕOrder._≤_ (partialSumDifferenceExponent d n)
    (partialSumDifferenceExponent d (suc n))
partialSumDifferenceExponent-step d n =
  ℕOrder.≤-trans ℕOrder.≤SumLeft ℕOrder.≤-sucℕ

partialSumDifferenceExponent-monotone : (d m n : ℕ) →
  ℕOrder._≤_ m n →
  ℕOrder._≤_ (partialSumDifferenceExponent d m)
    (partialSumDifferenceExponent d n)
partialSumDifferenceExponent-monotone d =
  monotone-from-successor
    (partialSumDifferenceExponent d)
    (partialSumDifferenceExponent-step d)

uniformExponentialCutoff-suc : (d n : ℕ) →
  uniformExponentialCutoff d (suc n) ≡
  suc (uniformExponentialCutoff d n)
uniformExponentialCutoff-suc d n =
  cong (dyadicNat (suc d) ℕ.+_)
    (ℕ.+-suc (uniformExponentialSeedExponent d) n) ∙
  ℕ.+-suc (dyadicNat (suc d))
    (uniformExponentialSeedExponent d ℕ.+ n)

uniformExponentialCutoff-step : (d n : ℕ) →
  ℕOrder._≤_ (uniformExponentialCutoff d n)
    (uniformExponentialCutoff d (suc n))
uniformExponentialCutoff-step d n =
  subst (ℕOrder._≤_ (uniformExponentialCutoff d n))
    (sym (uniformExponentialCutoff-suc d n))
    ℕOrder.≤-sucℕ

uniformExponentialCutoff-monotone : (d m n : ℕ) →
  ℕOrder._≤_ m n →
  ℕOrder._≤_ (uniformExponentialCutoff d m)
    (uniformExponentialCutoff d n)
uniformExponentialCutoff-monotone d =
  monotone-from-successor
    (uniformExponentialCutoff d) (uniformExponentialCutoff-step d)
