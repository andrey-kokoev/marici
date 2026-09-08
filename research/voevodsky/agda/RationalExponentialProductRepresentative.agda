{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module RationalExponentialProductRepresentative where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Rationals as Q
import Cubical.HITs.SetQuotients as SQ
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CanonicalExponentialRegularity
open import CanonicalDyadicallyBoundedCauchy
open import CauchyProductRegularity
open import CauchyCompletionMultiplication
open import CompletionProductPresentation
open import AutomaticRationalExponentialMultiplication

rationalProductRepresentative : (a b : Q.ℚ) → RegularCauchy
rationalProductRepresentative a b = boundedProductRegular
  (canonicalDyadicallyBounded (canonicalExponentialRegular (constantCauchy a)))
  (canonicalDyadicallyBounded (canonicalExponentialRegular (constantCauchy b)))

rationalProductRepresentativeClass : (a b : Q.ℚ) →
  Path MetricCompletionCandidate
    SQ.[ rationalProductRepresentative a b ]
    SQ.[ canonicalExponentialRegular (constantCauchy (a Q.+ b)) ]
rationalProductRepresentativeClass a b =
  sym (bridge (canonicalExponentialRegular (constantCauchy a))
    (canonicalExponentialRegular (constantCauchy b))) ∙
  rationalExponentialMultiplication a b
  where
  abstract
    bridge : (x y : RegularCauchy) →
      preferredCompletionMultiplication SQ.[ x ] SQ.[ y ] ≡
      SQ.[ boundedProductRegular (canonicalDyadicallyBounded x) (canonicalDyadicallyBounded y) ]
    bridge x y = completionProductFromPresentations preferredRationalDyadicArchimedean x y
      (canonicalDyadicallyBounded x , refl) (canonicalDyadicallyBounded y , refl)
