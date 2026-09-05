{-# OPTIONS --safe --cubical --no-import-sorts --guardedness --lossy-unification #-}
module TaylorValuesAtZero where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (zero; suc)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.HITs.SetQuotients as SQ using ([_])
open import RegularCauchyStructure
open import DyadicallyBoundedCauchy
open import CauchyProductBounds
open import TaylorTermBounds
open import RationalTaylorApproximants
open import ExponentialTailSchedule
open import CosineTailSchedule
open import ExponentialSeedConstruction
open import CosineSeedConstruction
open import CauchyMetricEquivalence

zero-magnitude≤one : MagnitudeBound 0 1
zero-magnitude≤one =
  nonnegative-value-magnitude 0 1
    (isRefl≤ 0) (precision-nonnegative zero) (precision-nonnegative zero)

zero-exponential-seed-term-bound :
  MagnitudeBound (exponentialTerm 0 (dyadicNat (suc zero))) 1
zero-exponential-seed-term-bound =
  transport-magnitude
    (exponentialTerm 0 (dyadicNat (suc zero))) 0 1
    (exponentialTerm-at-zero (suc zero)) zero-magnitude≤one

zero-cosine-seed-term-bound :
  MagnitudeBound (cosineTerm 0 (dyadicNat (suc zero))) 1
zero-cosine-seed-term-bound =
  transport-magnitude
    (cosineTerm 0 (dyadicNat (suc zero))) 0 1
    (cosineTerm-at-zero (suc zero)) zero-magnitude≤one

zeroExponentialSeed : ExponentialTailSeed 0
zeroExponentialSeed = record
  { inputExponent = zero
  ; inputBound = zero-magnitude≤one
  ; seedExponent = zero
  ; seedBound = zero-exponential-seed-term-bound
  }

zeroCosineSeed : CosineTailSeed 0
zeroCosineSeed = record
  { inputExponent = zero
  ; inputBound = zero-magnitude≤one
  ; seedExponent = zero
  ; seedBound = zero-cosine-seed-term-bound
  }

zero-exponential-regular-is-one :
  absorbedExponentialRegular zeroExponentialSeed ≡ constantCauchy 1
zero-exponential-regular-is-one =
  regularCauchy-ext
    (absorbedExponentialRegular zeroExponentialSeed)
    (constantCauchy 1)
    (funExt λ n → exponentialPartialSum-at-zero
      (absorbedTaylorCutoff zeroExponentialSeed n))

zero-cosine-regular-is-one :
  absorbedCosineRegular zeroCosineSeed ≡ constantCauchy 1
zero-cosine-regular-is-one =
  regularCauchy-ext
    (absorbedCosineRegular zeroCosineSeed)
    (constantCauchy 1)
    (funExt λ n → cosinePartialSum-at-zero
      (absorbedCosineCutoff zeroCosineSeed n))

rationalExponentialValue-at-zero :
  rationalExponentialValue 0 ≡ embedMetricℚ 1
rationalExponentialValue-at-zero =
  rationalExponentialValue-zero-from-seed-path
    zeroExponentialSeed zero-exponential-regular-is-one

rationalCosineValue-at-zero :
  rationalCosineValue 0 ≡ embedMetricℚ 1
rationalCosineValue-at-zero =
  rationalCosineValue-zero-from-seed-path
    zeroCosineSeed zero-cosine-regular-is-one
