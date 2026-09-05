{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module DyadicBoundNormalization where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (max)
import Cubical.Data.Nat.Order as ℕOrder
open import RegularCauchyStructure
open import DyadicallyBoundedCauchy

commonExponent :
  DyadicallyBoundedRegularCauchy →
  DyadicallyBoundedRegularCauchy → ℕ.ℕ
commonExponent x y = ℕ.max (radius-exponent x) (radius-exponent y)

normalizeLeft :
  (x y : DyadicallyBoundedRegularCauchy) →
  DyadicallyBoundedRegularCauchy
normalizeLeft x y =
  widenDyadicBound x (commonExponent x y) ℕOrder.left-≤-max

normalizeRight :
  (x y : DyadicallyBoundedRegularCauchy) →
  DyadicallyBoundedRegularCauchy
normalizeRight x y =
  widenDyadicBound y (commonExponent x y) ℕOrder.right-≤-max

normalizeLeft-regular :
  (x y : DyadicallyBoundedRegularCauchy) →
  regular (normalizeLeft x y) ≡ regular x
normalizeLeft-regular x y = refl

normalizeRight-regular :
  (x y : DyadicallyBoundedRegularCauchy) →
  regular (normalizeRight x y) ≡ regular y
normalizeRight-regular x y = refl

normalized-exponents-agree :
  (x y : DyadicallyBoundedRegularCauchy) →
  radius-exponent (normalizeLeft x y) ≡
  radius-exponent (normalizeRight x y)
normalized-exponents-agree x y = refl
