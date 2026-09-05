{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CanonicalDyadicallyBoundedCauchy where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ)
open import RegularCauchyStructure
open import RationallyBoundedCauchy
open import RationalArchimedean
open import LeastDyadicExponent
open import LeastDyadicExponentSearch
open import DyadicallyBoundedCauchy
open import CauchyBoundPromotion

canonicalLeastDyadicExponent :
  (x : RegularCauchy) → LeastDyadicExponent (canonicalRadius x)
canonicalLeastDyadicExponent x =
  select-least-dyadic preferred-least-dyadic-exponent-principle
    (canonicalRadius x)

canonicalArchimedeanExponent :
  (x : RegularCauchy) → ArchimedeanExponent (canonicalRadius x)
canonicalArchimedeanExponent x =
  least-dyadic-gives-exponent (canonicalRadius x)
    (canonicalLeastDyadicExponent x)

canonicalDyadicallyBounded :
  RegularCauchy → DyadicallyBoundedRegularCauchy
canonicalDyadicallyBounded x =
  promote-regular-with-witness x (canonicalArchimedeanExponent x)

canonicalDyadicPresentation :
  (x : RegularCauchy) → BoundedPresentation x
canonicalDyadicPresentation x =
  promote-regular-presentation-with-witness x
    (canonicalArchimedeanExponent x)

canonicalDyadicallyBounded-regular :
  (x : RegularCauchy) → regular (canonicalDyadicallyBounded x) ≡ x
canonicalDyadicallyBounded-regular x = refl

canonicalDyadicExponent : RegularCauchy → ℕ
canonicalDyadicExponent x =
  radius-exponent (canonicalDyadicallyBounded x)

canonicalDyadicExponent-is-least :
  (x : RegularCauchy) →
  canonicalDyadicExponent x ≡
  least-exponent (canonicalLeastDyadicExponent x)
canonicalDyadicExponent-is-least x = refl
