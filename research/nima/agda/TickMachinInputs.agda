{-# OPTIONS --safe --cubical --guardedness #-}
module TickMachinInputs where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ)
open import Cubical.Data.Rationals as Q
open import RegularCauchyStructure
open import RationalTaylorApproximants using (reciprocalSuccessor)
open import TaylorTermBounds using (reciprocal-after-zero-magnitude≤half)
open import TickSmallArctangent

oneFifth : Q.ℚ
oneFifth = reciprocalSuccessor 4

one239th : Q.ℚ
one239th = reciprocalSuccessor 238

abstract
  atanFifthRegular : RegularCauchy
  atanFifthRegular = smallAtanRegular oneFifth (reciprocal-after-zero-magnitude≤half 3)

  atan239thRegular : RegularCauchy
  atan239thRegular = smallAtanRegular one239th (reciprocal-after-zero-magnitude≤half 237)

  atan-fifth-samples : (n : ℕ) → approximation atanFifthRegular n ≡ atanPartialSum oneFifth n
  atan-fifth-samples n = refl

  atan-239th-samples : (n : ℕ) → approximation atan239thRegular n ≡ atanPartialSum one239th n
  atan-239th-samples n = refl
