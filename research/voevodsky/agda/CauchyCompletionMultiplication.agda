{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CauchyCompletionMultiplication where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Function using (_∘_)
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Sigma
open import Cubical.HITs.SetQuotients.Properties as SQ
open import RegularCauchyStructure
open import RationallyBoundedCauchy
open import RationalArchimedean
open import CauchyMetricEquivalence
open import CauchyProductWitnessCoherence

record RationalDyadicArchimedean : Type where
  field
    dominates-all : (q : Q.ℚ) → DyadicDominates q
open RationalDyadicArchimedean public

naturalCeilingArchimedean :
  RationalNaturalCeilingPrinciple → RationalDyadicArchimedean
naturalCeilingArchimedean principle .dominates-all =
  natural-ceiling-principle-gives-dyadic-dominance principle

truncatedNaturalCeilingArchimedean :
  RationalTruncatedNaturalCeilingPrinciple → RationalDyadicArchimedean
truncatedNaturalCeilingArchimedean principle .dominates-all =
  truncated-ceiling-principle-gives-dyadic-dominance principle

rawNaturalCeilingArchimedean :
  RawRationalNaturalCeiling → RationalDyadicArchimedean
rawNaturalCeilingArchimedean =
  truncatedNaturalCeilingArchimedean ∘ raw-ceiling-gives-truncated-principle

preferredRationalDyadicArchimedean : RationalDyadicArchimedean
preferredRationalDyadicArchimedean =
  rawNaturalCeilingArchimedean preferred-raw-rational-natural-ceiling

representativeProductClass :
  RationalDyadicArchimedean →
  RegularCauchy → RegularCauchy → MetricCompletionCandidate
representativeProductClass arch x y =
  productClassFromDominance x y
    (dominates-all arch (canonicalRadius x))
    (dominates-all arch (canonicalRadius y))

representativeProductClass-congruent :
  (arch : RationalDyadicArchimedean) →
  (x x′ y y′ : RegularCauchy) →
  x ≈metric x′ → y ≈metric y′ →
  representativeProductClass arch x y ≡
  representativeProductClass arch x′ y′
representativeProductClass-congruent arch x x′ y y′ rx ry =
  productClassFromDominance-congruent x x′ y y′
    (dominates-all arch (canonicalRadius x))
    (dominates-all arch (canonicalRadius x′))
    (dominates-all arch (canonicalRadius y))
    (dominates-all arch (canonicalRadius y′))
    rx ry

completionMultiplication :
  RationalDyadicArchimedean →
  MetricCompletionCandidate → MetricCompletionCandidate →
  MetricCompletionCandidate
completionMultiplication arch =
  Iso.inv
    (SQ.setQuotUniversal2Iso
      metric-candidate-isSet ≈metric-refl ≈metric-refl)
    (representativeProductClass arch ,
     representativeProductClass-congruent arch)

completionMultiplication-on-representatives :
  (arch : RationalDyadicArchimedean) (x y : RegularCauchy) →
  completionMultiplication arch ([ x ]) ([ y ]) ≡
  representativeProductClass arch x y
completionMultiplication-on-representatives arch x y = refl

preferredCompletionMultiplication :
  MetricCompletionCandidate → MetricCompletionCandidate →
  MetricCompletionCandidate
preferredCompletionMultiplication =
  completionMultiplication preferredRationalDyadicArchimedean

preferredCompletionMultiplication-preserves-rationals :
  (q r : Q.ℚ) →
  preferredCompletionMultiplication (embedMetricℚ q) (embedMetricℚ r) ≡
  embedMetricℚ (q Q.· r)
preferredCompletionMultiplication-preserves-rationals q r =
  completionMultiplication-on-representatives
    preferredRationalDyadicArchimedean
    (constantCauchy q) (constantCauchy r) ∙
  productClassFromDominance-preserves-rationals q r
    (dominates-all preferredRationalDyadicArchimedean
      (canonicalRadius (constantCauchy q)))
    (dominates-all preferredRationalDyadicArchimedean
      (canonicalRadius (constantCauchy r)))
