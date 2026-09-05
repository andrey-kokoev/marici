{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module UniformSineInputStabilityContract where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; _+_)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import RegularCauchyStructure
open import CauchyProductBounds
open import DyadicallyBoundedCauchy
open import RationalTaylorApproximants
open import RationalSineTaylorApproximants

record UniformSinePartialSumInputStability : Type where
  field
    uniformSineDifferenceExponent : ℕ → ℕ
    uniformSinePartialSumDifference :
      (q r error : Q.ℚ) (d truncation : ℕ) →
      0 ≤ error →
      MagnitudeBound q (dyadicRadius d) →
      MagnitudeBound r (dyadicRadius d) →
      MagnitudeBound (q Q.+ (Q.- r)) error →
      MagnitudeBound
        (sinePartialSum q truncation Q.+
         (Q.- sinePartialSum r truncation))
        (dyadicRadius (uniformSineDifferenceExponent d) Q.· error)
open UniformSinePartialSumInputStability public

uniformSineMetricDepth :
  UniformSinePartialSumInputStability → ℕ → ℕ → ℕ
uniformSineMetricDepth stability d outputPrecision =
  uniformSineDifferenceExponent stability d ℕ.+ outputPrecision

uniform-sine-metric-error-cancels :
  (stability : UniformSinePartialSumInputStability) →
  (d outputPrecision : ℕ) →
  dyadicRadius (uniformSineDifferenceExponent stability d) Q.·
    precision (uniformSineMetricDepth stability d outputPrecision) ≡
  precision outputPrecision
uniform-sine-metric-error-cancels stability d outputPrecision =
  radius-cancels-precision-shift
    (uniformSineDifferenceExponent stability d) outputPrecision
