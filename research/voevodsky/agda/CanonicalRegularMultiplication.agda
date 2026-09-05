{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CanonicalRegularMultiplication where

open import Cubical.Foundations.Prelude
open import Cubical.HITs.SetQuotients as SQ using ([_])
open import RegularCauchyStructure
open import RationallyBoundedCauchy
open import CanonicalDyadicallyBoundedCauchy
open import CauchyProductRegularity
open import CauchyMetricEquivalence
open import RationalArchimedean
open import CauchyProductWitnessCoherence
open import CauchyCompletionMultiplication

canonicalRegularProduct : RegularCauchy → RegularCauchy → RegularCauchy
canonicalRegularProduct x y =
  boundedProductRegular
    (canonicalDyadicallyBounded x)
    (canonicalDyadicallyBounded y)

canonicalRegularProductClass : (x y : RegularCauchy) →
  SQ.[ canonicalRegularProduct x y ] ≡
  preferredCompletionMultiplication SQ.[ x ] SQ.[ y ]
canonicalRegularProductClass x y =
  canonical-bounded-product-class-agrees-with-dominance x y ∙
  productClassFromDominance-congruent x x y y
    (witness-gives-truncated (canonicalRadius x)
      (canonicalArchimedeanExponent x))
    (dominates-all preferredRationalDyadicArchimedean (canonicalRadius x))
    (witness-gives-truncated (canonicalRadius y)
      (canonicalArchimedeanExponent y))
    (dominates-all preferredRationalDyadicArchimedean (canonicalRadius y))
    (≈metric-refl x) (≈metric-refl y) ∙
  sym (completionMultiplication-on-representatives
    preferredRationalDyadicArchimedean x y)
