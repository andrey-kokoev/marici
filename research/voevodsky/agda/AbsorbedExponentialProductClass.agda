{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module AbsorbedExponentialProductClass where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Rationals as Q
import Cubical.Data.Prod as Prod
import Cubical.HITs.SetQuotients as SQ
open import CauchyBoundPromotion
open import CauchyProductWitnessCoherence
open import ExponentialTailSchedule
open import RationalArchimedean
open import MetricProductTransport
open import AbsoluteTaylorSeriesMultiplication

module ProductClass
  {x y : Q.ℚ} (seed : ExponentialMultiplicationSeed x y)
  (xTail : ExponentialTailSeed x) (yTail : ExponentialTailSeed y)
  (sumTail : ExponentialTailSeed (x Q.+ y))
  (xRadius : ArchimedeanExponent (leftScale seed Q.+ leftScale seed))
  (yRadius : ArchimedeanExponent (rightScale seed Q.+ rightScale seed))
  where

  open AlignedExponentialProduct seed xTail yTail sumTail xRadius yRadius

  absorbedProductClassEquality :
    (px : BoundedPresentation (absorbedExponentialRegular xTail)) →
    (py : BoundedPresentation (absorbedExponentialRegular yTail)) →
    boundedWitnessProductClass
      {x = absorbedExponentialRegular xTail}
      {y = absorbedExponentialRegular yTail} (Prod._,_ px py) ≡
    SQ.[ absorbedExponentialRegular sumTail ]
  absorbedProductClassEquality px py =
    transportProductClass leftFactor rightFactor
      (absorbedExponentialRegular xTail) (absorbedExponentialRegular yTail)
      (absorbedExponentialRegular sumTail) px py
      (alignedAbsorbedExponentialEquivalent xTail commonBase xDominance)
      (alignedAbsorbedExponentialEquivalent yTail commonBase yDominance)
      productToAbsorbedSum
