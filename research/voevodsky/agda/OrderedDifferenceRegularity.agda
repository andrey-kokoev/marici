{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module OrderedDifferenceRegularity where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ)
import Cubical.Data.Nat.Order as ℕOrder
open import Cubical.Data.Sum
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate
open import RegularCauchyStructure
open import CauchyProductBounds

module DifferenceRegularityPaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; -_ to -S_)
  forward : (a b e : fst R) → a +S (-S b) +S b ≡ a
  forward a b e = solve! R
  backward : (a b : fst R) → -S (a +S (-S b)) +S a ≡ b
  backward a b = solve! R
  swap-errors : (a em en : fst R) →
    (a +S en) +S em ≡ (a +S em) +S en
  swap-errors a em en = solve! R

ordered-difference-forward :
  (a : ℕ → Q.ℚ) →
  ((m n : ℕ) → ℕOrder._≤_ m n →
    MagnitudeBound (a n Q.+ (Q.- a m)) (precision m)) →
  (m n : ℕ) → ℕOrder._≤_ m n →
  a m ≤ (a n Q.+ precision m) Q.+ precision n
ordered-difference-forward a bound m n m≤n =
  let negative = negative-upper (bound m n m≤n)
      translated = ≤-+o
        (Q.- (a n Q.+ (Q.- a m))) (precision m) (a n) negative
      direct = subst2 _≤_
        (DifferenceRegularityPaths.backward PreferredℚCommRing (a n) (a m))
        (Q.+Comm (precision m) (a n)) translated
  in isTrans≤ (a m) (a n Q.+ precision m)
       ((a n Q.+ precision m) Q.+ precision n) direct
       (≤-add-nonnegative (a n Q.+ precision m) (precision n)
         (precision-nonnegative n))

ordered-difference-backward :
  (a : ℕ → Q.ℚ) →
  ((m n : ℕ) → ℕOrder._≤_ m n →
    MagnitudeBound (a n Q.+ (Q.- a m)) (precision m)) →
  (m n : ℕ) → ℕOrder._≤_ m n →
  a n ≤ (a m Q.+ precision m) Q.+ precision n
ordered-difference-backward a bound m n m≤n =
  let positive = positive-upper (bound m n m≤n)
      translated = ≤-+o
        (a n Q.+ (Q.- a m)) (precision m) (a m) positive
      direct = subst2 _≤_
        (DifferenceRegularityPaths.forward PreferredℚCommRing (a n) (a m) (precision m))
        (Q.+Comm (precision m) (a m)) translated
  in isTrans≤ (a n) (a m Q.+ precision m)
       ((a m Q.+ precision m) Q.+ precision n) direct
       (≤-add-nonnegative (a m Q.+ precision m) (precision n)
         (precision-nonnegative n))

regular-from-ordered-differences :
  (a : ℕ → Q.ℚ) →
  ((m n : ℕ) → ℕOrder._≤_ m n →
    MagnitudeBound (a n Q.+ (Q.- a m)) (precision m)) →
  RegularCauchy
regular-from-ordered-differences a bound .approximation = a
regular-from-ordered-differences a bound .close-forward m n
  with ℕOrder.splitℕ-≤ m n
... | inl m≤n = ordered-difference-forward a bound m n m≤n
... | inr n<m = subst (a m ≤_)
  (DifferenceRegularityPaths.swap-errors PreferredℚCommRing
    (a n) (precision m) (precision n))
  (ordered-difference-backward a bound n m
    (ℕOrder.≤-trans ℕOrder.≤-sucℕ n<m))
regular-from-ordered-differences a bound .close-backward m n
  with ℕOrder.splitℕ-≤ m n
... | inl m≤n = ordered-difference-backward a bound m n m≤n
... | inr n<m = subst (a n ≤_)
  (DifferenceRegularityPaths.swap-errors PreferredℚCommRing
    (a m) (precision m) (precision n))
  (ordered-difference-forward a bound n m
    (ℕOrder.≤-trans ℕOrder.≤-sucℕ n<m))
