{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module LeastDyadicExponent where

open import Cubical.Foundations.Prelude
import Cubical.Data.Nat.Order as ℕOrder
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import DyadicallyBoundedCauchy
open import RationalArchimedean

least-dyadic-exponent-unique : (q : Q.ℚ) →
  (first second : LeastDyadicExponent q) →
  least-exponent first ≡ least-exponent second
least-dyadic-exponent-unique q first second =
  ℕOrder.≤-antisym
    (least-minimal first (least-exponent second)
      (least-dominates second))
    (least-minimal second (least-exponent first)
      (least-dominates first))

least-dyadic-exponent-isProp : (q : Q.ℚ) →
  isProp (LeastDyadicExponent q)
least-dyadic-exponent-isProp q first second i = record
  { least-exponent = exponentPath i
  ; least-dominates = dominatesPath i
  ; least-minimal = minimalPath i
  }
  where
  exponentPath : least-exponent first ≡ least-exponent second
  exponentPath = least-dyadic-exponent-unique q first second

  dominatesPath : PathP
    (λ i → q ≤ dyadicRadius (exponentPath i))
    (least-dominates first) (least-dominates second)
  dominatesPath = isProp→PathP
    (λ i → isProp≤ q (dyadicRadius (exponentPath i)))
    (least-dominates first) (least-dominates second)

  minimalPath : PathP
    (λ i → (m : _) → q ≤ dyadicRadius m →
      ℕOrder._≤_ (exponentPath i) m)
    (least-minimal first) (least-minimal second)
  minimalPath = isProp→PathP
    (λ i f g → funExt λ m → funExt λ proof →
      ℕOrder.isProp≤ (f m proof) (g m proof))
    (least-minimal first) (least-minimal second)
