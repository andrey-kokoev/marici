{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CauchyAdditiveLaws where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.HITs.PropositionalTruncation as PT
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyAddition
open import CauchyAdditionCongruence
open import CauchyNegation
open import CauchyShift

pointwise-equivalent : (x y : RegularCauchy) →
  ((n : ℕ) → approximation x n ≡ approximation y n) →
  x ≈metric y
pointwise-equivalent x y p k =
  ∣ (0 , λ n 0≤n →
    subst (λ z → approximation x n ≤ z Q.+ precision k)
      (p n)
      (≤-add-nonnegative (approximation x n) (precision k)
        (precision-nonnegative k)) ,
    subst (λ z → approximation y n ≤ z Q.+ precision k)
      (sym (p n))
      (≤-add-nonnegative (approximation y n) (precision k)
        (precision-nonnegative k))) ∣₁

zeroRegular : RegularCauchy
zeroRegular = constantCauchy 0

add-zero-right : (x : RegularCauchy) →
  addRegular x zeroRegular ≈metric x
add-zero-right x =
  ≈metric-trans (addRegular x zeroRegular) (shiftRegular x) x
    (pointwise-equivalent (addRegular x zeroRegular) (shiftRegular x)
      (λ n → Q.+IdR (approximation x (Cubical.Data.Nat.suc n))))
    (shift-equivalent x)

add-zero-left : (x : RegularCauchy) →
  addRegular zeroRegular x ≈metric x
add-zero-left x =
  ≈metric-trans (addRegular zeroRegular x) (shiftRegular x) x
    (pointwise-equivalent (addRegular zeroRegular x) (shiftRegular x)
      (λ n → Q.+IdL (approximation x (Cubical.Data.Nat.suc n))))
    (shift-equivalent x)

add-commutative : (x y : RegularCauchy) →
  addRegular x y ≈metric addRegular y x
add-commutative x y =
  pointwise-equivalent (addRegular x y) (addRegular y x)
    (λ n → Q.+Comm
      (approximation x (Cubical.Data.Nat.suc n))
      (approximation y (Cubical.Data.Nat.suc n)))

add-inverse-right : (x : RegularCauchy) →
  addRegular x (negateRegular x) ≈metric zeroRegular
add-inverse-right x =
  pointwise-equivalent (addRegular x (negateRegular x)) zeroRegular
    (λ n → Q.+InvR (approximation x (Cubical.Data.Nat.suc n)))

add-inverse-left : (x : RegularCauchy) →
  addRegular (negateRegular x) x ≈metric zeroRegular
add-inverse-left x =
  pointwise-equivalent (addRegular (negateRegular x) x) zeroRegular
    (λ n → Q.+InvL (approximation x (Cubical.Data.Nat.suc n)))

normalized-left normalized-right :
  RegularCauchy → RegularCauchy → RegularCauchy → RegularCauchy
normalized-left x y z =
  addRegular (shiftRegular (addRegular x y))
    (shiftRegular (shiftRegular z))
normalized-right x y z =
  addRegular (shiftRegular (shiftRegular x))
    (shiftRegular (addRegular y z))

shift²-equivalent : (x : RegularCauchy) →
  shiftRegular (shiftRegular x) ≈metric x
shift²-equivalent x =
  ≈metric-trans (shiftRegular (shiftRegular x)) (shiftRegular x) x
    (shift-equivalent (shiftRegular x)) (shift-equivalent x)

normalized-associative : (x y z : RegularCauchy) →
  normalized-left x y z ≈metric normalized-right x y z
normalized-associative x y z =
  pointwise-equivalent (normalized-left x y z) (normalized-right x y z)
    (λ n → sym (Q.+Assoc
      (approximation x (Cubical.Data.Nat.suc (Cubical.Data.Nat.suc (Cubical.Data.Nat.suc n))))
      (approximation y (Cubical.Data.Nat.suc (Cubical.Data.Nat.suc (Cubical.Data.Nat.suc n))))
      (approximation z (Cubical.Data.Nat.suc (Cubical.Data.Nat.suc (Cubical.Data.Nat.suc n))))))

add-associative : (x y z : RegularCauchy) →
  addRegular (addRegular x y) z ≈metric
  addRegular x (addRegular y z)
add-associative x y z =
  ≈metric-trans
    (addRegular (addRegular x y) z) (normalized-left x y z)
    (addRegular x (addRegular y z))
    (addRegular-cong (addRegular x y) (shiftRegular (addRegular x y))
      z (shiftRegular (shiftRegular z))
      (≈metric-sym (shiftRegular (addRegular x y)) (addRegular x y)
        (shift-equivalent (addRegular x y)))
      (≈metric-sym (shiftRegular (shiftRegular z)) z
        (shift²-equivalent z)))
    (≈metric-trans (normalized-left x y z) (normalized-right x y z)
      (addRegular x (addRegular y z)) (normalized-associative x y z)
      (≈metric-sym (addRegular x (addRegular y z)) (normalized-right x y z)
        (addRegular-cong x (shiftRegular (shiftRegular x))
          (addRegular y z) (shiftRegular (addRegular y z))
          (≈metric-sym (shiftRegular (shiftRegular x)) x
            (shift²-equivalent x))
          (≈metric-sym (shiftRegular (addRegular y z)) (addRegular y z)
            (shift-equivalent (addRegular y z))))))
