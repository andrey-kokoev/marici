{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module DyadicallyBoundedCauchyNegation where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import RegularCauchyStructure
open import CauchyNegation
open import CauchyProductBounds
open import CauchyProductErrorBounds
open import DyadicallyBoundedCauchy

negateDyadicallyBounded :
  DyadicallyBoundedRegularCauchy → DyadicallyBoundedRegularCauchy
negateDyadicallyBounded x .regular = negateRegular (regular x)
negateDyadicallyBounded x .radius-exponent = radius-exponent x
negateDyadicallyBounded x .upper-bound n =
  negative-upper (bounded-value x n)
negateDyadicallyBounded x .lower-bound n =
  subst (Q.- dyadicRadius (radius-exponent x) ≤_)
    (Q.+IdR (Q.- approximation (regular x) n))
    (negate-one-error-bound
      (approximation (regular x) n)
      (dyadicRadius (radius-exponent x)) 0
      (subst (approximation (regular x) n ≤_)
        (sym (Q.+IdR (dyadicRadius (radius-exponent x))))
        (upper-bound x n)))

negateDyadicallyBounded-regular :
  (x : DyadicallyBoundedRegularCauchy) →
  regular (negateDyadicallyBounded x) ≡ negateRegular (regular x)
negateDyadicallyBounded-regular x = refl

negateDyadicallyBounded-involutive-regular :
  (x : DyadicallyBoundedRegularCauchy) →
  regular (negateDyadicallyBounded (negateDyadicallyBounded x)) ≡ regular x
negateDyadicallyBounded-involutive-regular x =
  regularCauchy-ext _ _ (funExt λ n → Q.-Invol (approximation (regular x) n))
