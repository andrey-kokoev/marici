{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CompletionProductPresentation where

open import Cubical.Foundations.Prelude
import Cubical.Data.Prod as Prod
import Cubical.HITs.SetQuotients as SQ
open import RegularCauchyStructure
open import RationallyBoundedCauchy
open import CauchyBoundPromotion
open import CauchyMetricEquivalence
open import CauchyProductWitnessCoherence
open import CauchyCompletionMultiplication

abstract
  completionProductFromPresentations :
    (arch : RationalDyadicArchimedean) (x y : RegularCauchy) →
    (px : BoundedPresentation x) (py : BoundedPresentation y) →
    completionMultiplication arch SQ.[ x ] SQ.[ y ] ≡
    boundedWitnessProductClass {x = x} {y = y} (Prod._,_ px py)
  completionProductFromPresentations arch x y px py =
    completionMultiplication-on-representatives arch x y ∙
    productClassFromDominance-from-presentations {x = x} {y = y}
      (dominates-all arch (canonicalRadius x))
      (dominates-all arch (canonicalRadius y)) px py
