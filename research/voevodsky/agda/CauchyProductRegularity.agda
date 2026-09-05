{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CauchyProductRegularity where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; suc; _+_)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate
open import RegularCauchyStructure
open import DyadicallyBoundedCauchy
open import CauchyProductAlgebra
open import CauchyProductBounds
open import CauchyProductErrorBounds

module DirectedPaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; -_ to -S_)

  restore-right : (a b : fst R) →
    (a +S (-S b)) +S b ≡ a
  restore-right a b = solve! R

  error-to-directed : (b p q : fst R) →
    (p +S q) +S b ≡ (b +S p) +S q
  error-to-directed b p q = solve! R

  reverse-difference : (a b : fst R) →
    -S (a +S (-S b)) ≡ b +S (-S a)
  reverse-difference a b = solve! R

difference-upper→directed : (a b p q : Q.ℚ) →
  a Q.+ (Q.- b) ≤ p Q.+ q →
  a ≤ (b Q.+ p) Q.+ q
difference-upper→directed a b p q difference≤error =
  subst2 _≤_
    (DirectedPaths.restore-right PreferredℚCommRing a b)
    (DirectedPaths.error-to-directed PreferredℚCommRing b p q)
    (≤-+o (a Q.+ (Q.- b)) (p Q.+ q) b difference≤error)

refined-product-difference-bound :
  (x y : DyadicallyBoundedRegularCauchy) (m n : ℕ) →
  let d = suc (radius-exponent x ℕ.+ radius-exponent y)
      product = refinedProductApproximation d (regular x) (regular y)
  in
  MagnitudeBound
    (product m Q.+ (Q.- product n))
    (precision m Q.+ precision n)
refined-product-difference-bound x y m n =
  let d = suc (radius-exponent x ℕ.+ radius-exponent y)
  in
  transport-magnitude _ _ (precision m Q.+ precision n)
    (refined-product-difference d m n (regular x) (regular y))
    (refined-decomposed-product-error-bound x y m n)

boundedProductRegular :
  DyadicallyBoundedRegularCauchy →
  DyadicallyBoundedRegularCauchy →
  RegularCauchy
boundedProductRegular x y .approximation =
  refinedProductApproximation
    (suc (radius-exponent x ℕ.+ radius-exponent y))
    (regular x) (regular y)
boundedProductRegular x y .close-forward m n =
  difference-upper→directed
    (approximation (boundedProductRegular x y) m)
    (approximation (boundedProductRegular x y) n)
    (precision m) (precision n)
    (positive-upper (refined-product-difference-bound x y m n))
boundedProductRegular x y .close-backward m n =
  difference-upper→directed
    (approximation (boundedProductRegular x y) n)
    (approximation (boundedProductRegular x y) m)
    (precision m) (precision n)
    (subst (_≤ precision m Q.+ precision n)
      (DirectedPaths.reverse-difference PreferredℚCommRing
        (approximation (boundedProductRegular x y) m)
        (approximation (boundedProductRegular x y) n))
      (negative-upper (refined-product-difference-bound x y m n)))
