{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module DyadicallyBoundedCauchyShift where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; _+_)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyShift
open import DyadicallyBoundedCauchy

shiftDyadicallyBounded :
  ℕ → DyadicallyBoundedRegularCauchy → DyadicallyBoundedRegularCauchy
shiftDyadicallyBounded extra x .regular = iterateShift extra (regular x)
shiftDyadicallyBounded extra x .radius-exponent = radius-exponent x
shiftDyadicallyBounded extra x .lower-bound n =
  subst ((Q.- dyadicRadius (radius-exponent x)) ≤_)
    (sym (iterateShift-approximation extra n (regular x)))
    (lower-bound x (extra ℕ.+ n))
shiftDyadicallyBounded extra x .upper-bound n =
  subst (_≤ dyadicRadius (radius-exponent x))
    (sym (iterateShift-approximation extra n (regular x)))
    (upper-bound x (extra ℕ.+ n))

shiftDyadicallyBounded-regular :
  (extra : ℕ) (x : DyadicallyBoundedRegularCauchy) →
  regular (shiftDyadicallyBounded extra x) ≡ iterateShift extra (regular x)
shiftDyadicallyBounded-regular extra x = refl

shiftDyadicallyBounded-equivalent :
  (extra : ℕ) (x : DyadicallyBoundedRegularCauchy) →
  regular (shiftDyadicallyBounded extra x) ≈metric regular x
shiftDyadicallyBounded-equivalent extra x =
  iterateShift-equivalent extra (regular x)

shiftDyadicallyBounded-preserves-exponent :
  (extra : ℕ) (x : DyadicallyBoundedRegularCauchy) →
  radius-exponent (shiftDyadicallyBounded extra x) ≡ radius-exponent x
shiftDyadicallyBounded-preserves-exponent extra x = refl
