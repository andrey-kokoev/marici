{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CanonicalComplexRegularMultiplication where

open import Cubical.Foundations.Prelude
open import Cubical.HITs.SetQuotients as SQ using ([_])
open import RegularCauchyStructure
open import CauchyAddition
open import CauchyCompletionAbGroup
open import CauchyAdditionCongruence
open import CauchyNegation
open import ConstructiveComplexCompletion
open import ComplexCauchyApproximation
open import CanonicalRegularMultiplication

differenceRegular : RegularCauchy → RegularCauchy → RegularCauchy
differenceRegular x y = addRegular x (negateRegular y)

canonicalComplexRegularProduct : ComplexRegular → ComplexRegular → ComplexRegular
canonicalComplexRegularProduct (ar , ai) (br , bi) =
  differenceRegular
    (canonicalRegularProduct ar br)
    (canonicalRegularProduct ai bi)
  ,
  addRegular
    (canonicalRegularProduct ar bi)
    (canonicalRegularProduct ai br)

canonicalComplexRegularProductClass : (z w : ComplexRegular) →
  complexRegularClass (canonicalComplexRegularProduct z w) ≡
  complexRegularClass z ·complex complexRegularClass w
canonicalComplexRegularProductClass (ar , ai) (br , bi) =
  complex-ext _ _
    (cong₂ (λ x y → x +completion y)
      (canonicalRegularProductClass ar br)
      (cong (λ x → -completion x) (canonicalRegularProductClass ai bi)))
    (cong₂ (λ x y → x +completion y)
      (canonicalRegularProductClass ar bi)
      (canonicalRegularProductClass ai br))
