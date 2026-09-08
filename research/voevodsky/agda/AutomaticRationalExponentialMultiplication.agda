{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module AutomaticRationalExponentialMultiplication where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ)
open import Cubical.Data.Rationals as Q
open import RationalArchimedean
open import RationalTaylorApproximants using (exponentialTerm)
open import LeastDyadicExponent
open import LeastDyadicExponentSearch
open import CauchyCompletionMultiplication
open import AbsoluteTaylorSeriesMultiplication
open import CanonicalRationalExponentialIdentification
open import CanonicalRationalExponentialMultiplication

preferredExponent : (q : Q.ℚ) → ArchimedeanExponent q
preferredExponent q = least-dyadic-gives-exponent q
  (select-least-dyadic preferred-least-dyadic-exponent-principle q)

preferredSignedFamily : (term : ℕ → Q.ℚ) → SignedArchimedeanFamily term
preferredSignedFamily term .positiveExponent n = preferredExponent (term n)
preferredSignedFamily term .negativeExponent n = preferredExponent (Q.- term n)

preferredExponentialMajorant : (q : Q.ℚ) → ExponentialGlobalMajorant q
preferredExponentialMajorant q = exponentialGlobalMajorantFromData q
  (uniformEarlyRadiusGivesGlobalMajorantData q
    (tailSeedAndSignedTermsGiveUniformEarlyRadiusData q
      (canonicalRationalTailSeed q)
      (preferredSignedFamily (exponentialTerm q))))

preferredMultiplicationSeed : (x y : Q.ℚ) → ExponentialMultiplicationSeed x y
preferredMultiplicationSeed x y = globalMajorantsGiveMultiplicationSeed x y
  (preferredExponentialMajorant x) (preferredExponentialMajorant y)
  (preferredExponent (fourfoldProductCoefficient
    (globalScale (preferredExponentialMajorant x))
    (globalScale (preferredExponentialMajorant y))))

rationalExponentialMultiplication : (x y : Q.ℚ) →
  preferredCompletionMultiplication
    (canonicalRationalExponentialClass x)
    (canonicalRationalExponentialClass y) ≡
  canonicalRationalExponentialClass (x Q.+ y)
rationalExponentialMultiplication x y =
  Multiplication.canonicalRationalMultiplication
    (preferredMultiplicationSeed x y)
    (canonicalRationalTailSeed x) (canonicalRationalTailSeed y)
    (canonicalRationalTailSeed (x Q.+ y))
    (preferredExponent (leftScale (preferredMultiplicationSeed x y) Q.+
      leftScale (preferredMultiplicationSeed x y)))
    (preferredExponent (rightScale (preferredMultiplicationSeed x y) Q.+
      rightScale (preferredMultiplicationSeed x y)))
