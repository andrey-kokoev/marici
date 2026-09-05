{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module UniformTaylorInputStabilityContract where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; _+_)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import RegularCauchyStructure
open import CauchyProductBounds
open import DyadicallyBoundedCauchy
open import RationalTaylorApproximants

-- The existing finite-sum estimate uses a scale that grows with the truncation
-- depth.  Metric descent needs one scale for every truncation at a fixed input
-- radius; otherwise an EventuallyWithin witness would have to be selected at a
-- precision depending on every later output index.
record UniformExponentialPartialSumInputStability : Type where
  field
    uniformExponentialDifferenceExponent : ℕ → ℕ
    uniformExponentialPartialSumDifference :
      (q r error : Q.ℚ) (d truncation : ℕ) →
      0 ≤ error →
      MagnitudeBound q (dyadicRadius d) →
      MagnitudeBound r (dyadicRadius d) →
      MagnitudeBound (q Q.+ (Q.- r)) error →
      MagnitudeBound
        (exponentialPartialSum q truncation Q.+
         (Q.- exponentialPartialSum r truncation))
        (dyadicRadius (uniformExponentialDifferenceExponent d) Q.· error)
open UniformExponentialPartialSumInputStability public

uniformExponentialMetricDepth :
  UniformExponentialPartialSumInputStability → ℕ → ℕ → ℕ
uniformExponentialMetricDepth stability d outputPrecision =
  uniformExponentialDifferenceExponent stability d ℕ.+ outputPrecision

uniform-exponential-metric-error-cancels :
  (stability : UniformExponentialPartialSumInputStability) →
  (d outputPrecision : ℕ) →
  dyadicRadius (uniformExponentialDifferenceExponent stability d) Q.·
    precision (uniformExponentialMetricDepth stability d outputPrecision) ≡
  precision outputPrecision
uniform-exponential-metric-error-cancels stability d outputPrecision =
  radius-cancels-precision-shift
    (uniformExponentialDifferenceExponent stability d) outputPrecision
