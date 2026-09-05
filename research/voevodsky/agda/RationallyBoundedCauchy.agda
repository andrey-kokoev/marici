{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module RationallyBoundedCauchy where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ)
import Cubical.Data.Nat.Order as ℕOrder
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import RegularCauchyStructure
open import CauchyShift
open import CauchyNegation

rationalTwo : Q.ℚ
rationalTwo = 1 Q.+ 1

precision-pair≤two : (n : ℕ) →
  precision n Q.+ precision 0 ≤ rationalTwo
precision-pair≤two n =
  ≤Monotone+ (precision n) 1 (precision 0) 1
    (precision-antitone 0 n ℕOrder.zero-≤)
    (isRefl≤ 1)

record RationallyBoundedRegularCauchy : Type where
  field
    regular : RegularCauchy
    radius : Q.ℚ
    positive-upper : (n : ℕ) → approximation regular n ≤ radius
    negative-upper : (n : ℕ) → Q.- approximation regular n ≤ radius
open RationallyBoundedRegularCauchy public

canonicalRadius : RegularCauchy → Q.ℚ
canonicalRadius x =
  Q.max (approximation x 0) (Q.- approximation x 0) Q.+ rationalTwo

regular-is-rationally-bounded :
  (x : RegularCauchy) → RationallyBoundedRegularCauchy
regular-is-rationally-bounded x .regular = x
regular-is-rationally-bounded x .radius = canonicalRadius x
regular-is-rationally-bounded x .positive-upper n =
  isTrans≤ (approximation x n)
    (approximation x 0 Q.+ rationalTwo) (canonicalRadius x)
    (tighten-two-errors
      (approximation x n) (approximation x 0)
      (precision n) (precision 0) rationalTwo
      (precision-pair≤two n) (close-forward x n 0))
    (≤-+o (approximation x 0)
      (Q.max (approximation x 0) (Q.- approximation x 0))
      rationalTwo
      (≤max (approximation x 0) (Q.- approximation x 0)))
regular-is-rationally-bounded x .negative-upper n =
  isTrans≤ (Q.- approximation x n)
    (Q.- approximation x 0 Q.+ rationalTwo) (canonicalRadius x)
    (tighten-two-errors
      (Q.- approximation x n) (Q.- approximation x 0)
      (precision n) (precision 0) rationalTwo
      (precision-pair≤two n)
      (negate-two-error-bound
        (approximation x 0) (approximation x n)
        (precision n) (precision 0) (close-backward x n 0)))
    (≤-+o (Q.- approximation x 0)
      (Q.max (approximation x 0) (Q.- approximation x 0))
      rationalTwo
      (subst (Q.- approximation x 0 ≤_)
        (Q.maxComm (Q.- approximation x 0) (approximation x 0))
        (≤max (Q.- approximation x 0) (approximation x 0))))
