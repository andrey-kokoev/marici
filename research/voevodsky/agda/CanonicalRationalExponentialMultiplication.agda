{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CanonicalRationalExponentialMultiplication where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Rationals as Q
import Cubical.HITs.SetQuotients as SQ
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyCompletionMultiplication
open import CompletionProductPresentation
open import CanonicalDyadicallyBoundedCauchy
open import CanonicalExponentialRegularity
open import CanonicalRationalExponentialIdentification
open import ExponentialTailSchedule
open import RationalArchimedean
open import AbsoluteTaylorSeriesMultiplication
open import AbsorbedExponentialProductClass

canonicalRationalExponentialClass : Q.ℚ → MetricCompletionCandidate
canonicalRationalExponentialClass q =
  SQ.[ canonicalExponentialRegular (constantCauchy q) ]

canonicalRationalClassToSeed : (q : Q.ℚ) (tail : ExponentialTailSeed q) →
  canonicalRationalExponentialClass q ≡ SQ.[ absorbedExponentialRegular tail ]
canonicalRationalClassToSeed q tail = SQ.eq/
  (canonicalExponentialRegular (constantCauchy q))
  (absorbedExponentialRegular tail)
  (canonicalRationalExponentialSeedEquivalent q tail)

module Multiplication
  {x y : Q.ℚ} (seed : ExponentialMultiplicationSeed x y)
  (xTail : ExponentialTailSeed x) (yTail : ExponentialTailSeed y)
  (sumTail : ExponentialTailSeed (x Q.+ y))
  (xRadius : ArchimedeanExponent (leftScale seed Q.+ leftScale seed))
  (yRadius : ArchimedeanExponent (rightScale seed Q.+ rightScale seed))
  where

  module Absorbed = ProductClass seed xTail yTail sumTail xRadius yRadius

  absorbedMultiplication :
    preferredCompletionMultiplication
      SQ.[ absorbedExponentialRegular xTail ]
      SQ.[ absorbedExponentialRegular yTail ] ≡
    SQ.[ absorbedExponentialRegular sumTail ]
  absorbedMultiplication =
    completionProductFromPresentations preferredRationalDyadicArchimedean
      (absorbedExponentialRegular xTail) (absorbedExponentialRegular yTail)
      (canonicalDyadicPresentation (absorbedExponentialRegular xTail))
      (canonicalDyadicPresentation (absorbedExponentialRegular yTail)) ∙
    Absorbed.absorbedProductClassEquality
      (canonicalDyadicPresentation (absorbedExponentialRegular xTail))
      (canonicalDyadicPresentation (absorbedExponentialRegular yTail))

  canonicalRationalMultiplication :
    preferredCompletionMultiplication
      (canonicalRationalExponentialClass x)
      (canonicalRationalExponentialClass y) ≡
    canonicalRationalExponentialClass (x Q.+ y)
  canonicalRationalMultiplication =
    cong₂ preferredCompletionMultiplication
      (canonicalRationalClassToSeed x xTail)
      (canonicalRationalClassToSeed y yTail) ∙
    absorbedMultiplication ∙
    sym (canonicalRationalClassToSeed (x Q.+ y) sumTail)
