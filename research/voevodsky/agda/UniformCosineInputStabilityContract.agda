{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module UniformCosineInputStabilityContract where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; _+_)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import RegularCauchyStructure
open import CauchyProductBounds
open import DyadicallyBoundedCauchy
open import RationalTaylorApproximants

record UniformCosinePartialSumInputStability : Type where
  field
    uniformCosineDifferenceExponent : ℕ → ℕ
    uniformCosinePartialSumDifference :
      (q r error : Q.ℚ) (d truncation : ℕ) →
      0 ≤ error →
      MagnitudeBound q (dyadicRadius d) →
      MagnitudeBound r (dyadicRadius d) →
      MagnitudeBound (q Q.+ (Q.- r)) error →
      MagnitudeBound
        (cosinePartialSum q truncation Q.+
         (Q.- cosinePartialSum r truncation))
        (dyadicRadius (uniformCosineDifferenceExponent d) Q.· error)
open UniformCosinePartialSumInputStability public

uniformCosineMetricDepth :
  UniformCosinePartialSumInputStability → ℕ → ℕ → ℕ
uniformCosineMetricDepth stability d outputPrecision =
  uniformCosineDifferenceExponent stability d ℕ.+ outputPrecision

uniform-cosine-metric-error-cancels :
  (stability : UniformCosinePartialSumInputStability) →
  (d outputPrecision : ℕ) →
  dyadicRadius (uniformCosineDifferenceExponent stability d) Q.·
    precision (uniformCosineMetricDepth stability d outputPrecision) ≡
  precision outputPrecision
uniform-cosine-metric-error-cancels stability d outputPrecision =
  radius-cancels-precision-shift
    (uniformCosineDifferenceExponent stability d) outputPrecision
