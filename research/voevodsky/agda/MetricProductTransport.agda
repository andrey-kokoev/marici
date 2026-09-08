{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module MetricProductTransport where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma
import Cubical.Data.Prod as Prod
import Cubical.HITs.SetQuotients as SQ
open import RegularCauchyStructure
open import DyadicallyBoundedCauchy
open import CauchyBoundPromotion
open import CauchyMetricEquivalence
open import CauchyProductRegularity
open import CauchyProductWitnessCoherence

abstract
  transportProductClass :
    (a b : DyadicallyBoundedRegularCauchy) (x y z : RegularCauchy) →
    (px : BoundedPresentation x) (py : BoundedPresentation y) →
    regular a ≈metric x → regular b ≈metric y →
    boundedProductRegular a b ≈metric z →
    boundedWitnessProductClass {x = x} {y = y} (Prod._,_ px py) ≡ SQ.[ z ]
  transportProductClass a b x y z px py ax by productZ =
    sym (boundedWitnessProductClass-congruent
      {x = regular a} {x′ = x} {y = regular b} {y′ = y}
      (a , refl) px (b , refl) py ax by) ∙
    SQ.eq/ (boundedProductRegular a b) z productZ
