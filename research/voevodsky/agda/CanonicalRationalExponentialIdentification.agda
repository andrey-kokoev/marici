{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CanonicalRationalExponentialIdentification where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Rationals as Q
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyShift
open import CanonicalDyadicallyBoundedCauchy
open import CanonicalExponentialSchedule
open import CanonicalExponentialRegularity
open import TaylorUniformSeedBounds
open import ExponentialTailSchedule
open import ExponentialSeedCoherence

canonicalRationalTailSeed : (q : Q.ℚ) → ExponentialTailSeed q
canonicalRationalTailSeed q = uniformExponentialTailSeed q
  (canonicalDyadicExponent (constantCauchy q))
  (canonical-input-approximation-bound (constantCauchy q) 0)

canonicalRationalExponentialPath : (q : Q.ℚ) →
  canonicalExponentialRegular (constantCauchy q) ≡
  shiftRegular (absorbedExponentialRegular (canonicalRationalTailSeed q))
canonicalRationalExponentialPath q = regularCauchy-ext _ _ refl

canonicalRationalExponentialSeedEquivalent : (q : Q.ℚ) →
  (seed : ExponentialTailSeed q) →
  canonicalExponentialRegular (constantCauchy q) ≈metric
    absorbedExponentialRegular seed
canonicalRationalExponentialSeedEquivalent q seed =
  ≈metric-trans
    (canonicalExponentialRegular (constantCauchy q))
    (shiftRegular (absorbedExponentialRegular (canonicalRationalTailSeed q)))
    (absorbedExponentialRegular seed)
    (regular-path→metric _ _ (canonicalRationalExponentialPath q))
    (≈metric-trans
      (shiftRegular (absorbedExponentialRegular (canonicalRationalTailSeed q)))
      (absorbedExponentialRegular (canonicalRationalTailSeed q))
      (absorbedExponentialRegular seed)
      (shift-equivalent (absorbedExponentialRegular (canonicalRationalTailSeed q)))
      (exponential-seeds-metric-equivalent (canonicalRationalTailSeed q) seed))
