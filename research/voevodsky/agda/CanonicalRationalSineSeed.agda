{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CanonicalRationalSineSeed where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ)
open import Cubical.Data.Rationals as Q
open import Cubical.HITs.SetQuotients as SQ using ([_])
open import CauchyMetricEquivalence
open import CauchyCompletionAbGroup
open import CauchyNegation
open import RegularCauchyStructure
open import CauchyProductBounds
open import CauchyProductErrorBounds
open import DyadicallyBoundedCauchy
open import CanonicalDyadicallyBoundedCauchy
open import RationalSineTaylorApproximants
open import SineTailSchedule
open import SineSeedCoherence
open import SineSeedNegation

canonical-constant-value-bound : (q : Q.ℚ) →
  MagnitudeBound q
    (dyadicRadius (canonicalDyadicExponent (constantCauchy q)))
canonical-constant-value-bound q =
  bounded-value (canonicalDyadicallyBounded (constantCauchy q)) ℕ.zero

abstract
  canonicalRationalSineSeed : (q : Q.ℚ) → SineTailSeed q
  canonicalRationalSineSeed q .inputExponent =
    canonicalDyadicExponent (constantCauchy q)
  canonicalRationalSineSeed q .inputBound = canonical-constant-value-bound q
  canonicalRationalSineSeed q .seedExponent =
    canonicalDyadicExponent
      (constantCauchy
        (sineTerm q
          (dyadicNat (ℕ.suc
            (canonicalDyadicExponent (constantCauchy q))))))
  canonicalRationalSineSeed q .seedBound =
    canonical-constant-value-bound
      (sineTerm q
        (dyadicNat (ℕ.suc
          (canonicalDyadicExponent (constantCauchy q)))))

canonicalRationalSineRegular : Q.ℚ → RegularCauchy
canonicalRationalSineRegular q =
  absorbedSineRegular (canonicalRationalSineSeed q)

canonical-rational-sine-approximation-zero : (n : ℕ) →
  approximation (canonicalRationalSineRegular 0) n ≡ 0
canonical-rational-sine-approximation-zero n =
  sinePartialSum-at-zero
    (absorbedSineCutoff (canonicalRationalSineSeed 0) n)

canonical-rational-sine-zero :
  canonicalRationalSineRegular 0 ≡ constantCauchy 0
canonical-rational-sine-zero =
  regularCauchy-ext _ _
    (funExt canonical-rational-sine-approximation-zero)

rationalSineValue : Q.ℚ → MetricCompletionCandidate
rationalSineValue q = SQ.[ canonicalRationalSineRegular q ]

rational-sine-value-zero :
  rationalSineValue 0 ≡ zeroCompletion
rational-sine-value-zero = cong SQ.[_] canonical-rational-sine-zero

rational-sine-value-from-seed : {q : Q.ℚ} → (seed : SineTailSeed q) →
  rationalSineValue q ≡ SQ.[ absorbedSineRegular seed ]
rational-sine-value-from-seed seed =
  SQ.eq/ _ _
    (sine-seeds-metric-equivalent (canonicalRationalSineSeed _) seed)

rational-sine-value-odd : (q : Q.ℚ) →
  rationalSineValue (Q.- q) ≡ -completion rationalSineValue q
rational-sine-value-odd q =
  rational-sine-value-from-seed
    (negateSineTailSeed (canonicalRationalSineSeed q)) ∙
  cong SQ.[_] (negated-seed-regular (canonicalRationalSineSeed q))
