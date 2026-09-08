{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CompletedExponentialMultiplication where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ; suc)
import Cubical.Data.Nat.Order as O
open import Cubical.Data.Rationals as Q
import Cubical.HITs.SetQuotients as SQ
open import RegularCauchyStructure
open import CauchyAddition
open import CauchyMetricEquivalence
open import CauchyQuantitativeContinuity
open import CanonicalDyadicallyBoundedCauchy
open import CanonicalExponentialRegularity
open import CauchyProductRegularity
open import CauchyCompletionMultiplication
open import CompletionProductPresentation
open import MetricCompletionEffectiveness
open import RationalExponentialProductRepresentative
open import ExponentialProductEventualApproximation
open import RawProductRefinementTransport

exponentialProductRegular : RegularCauchy → RegularCauchy → RegularCauchy
exponentialProductRegular x y = boundedProductRegular
  (canonicalDyadicallyBounded (canonicalExponentialRegular x))
  (canonicalDyadicallyBounded (canonicalExponentialRegular y))

abstract
  rationalProductMetric : (a b : Q.ℚ) →
    rationalProductRepresentative a b ≈metric
    canonicalExponentialRegular (constantCauchy (a Q.+ b))
  rationalProductMetric a b = quotientPathToMetric
    (rationalProductRepresentative a b)
    (canonicalExponentialRegular (constantCauchy (a Q.+ b)))
    (rationalProductRepresentativeClass a b)

exponentialMultiplicationMetric : (x y : RegularCauchy) →
  exponentialProductRegular x y ≈metric canonicalExponentialRegular (addRegular x y)
exponentialMultiplicationMetric x y k =
  composeEventuallyWithin (exponentialProductRegular x y)
    (rationalProductRepresentative a b) target k
    (T.rawToBoundedProducts (suc k) (E.productApproximation N O.≤-refl))
    (composeEventuallyWithin (rationalProductRepresentative a b)
      (canonicalExponentialRegular (constantCauchy (a Q.+ b))) target (suc k)
      (rationalProductMetric a b (suc (suc k)))
      (E.Sync.sumApproximation N O.≤-refl))
  where
  module E = ExponentialProduct x y (suc (suc (suc k))) (suc (suc k))
  N = E.Sync.commonCutoff
  a = approximation x (suc N)
  b = approximation y (suc N)
  target = canonicalExponentialRegular (addRegular x y)
  module T = Transport
    (canonicalDyadicallyBounded (canonicalExponentialRegular x))
    (canonicalDyadicallyBounded (canonicalExponentialRegular y))
    (canonicalDyadicallyBounded (canonicalExponentialRegular (constantCauchy a)))
    (canonicalDyadicallyBounded (canonicalExponentialRegular (constantCauchy b)))

abstract
  canonicalProductBridge : (x y : RegularCauchy) →
    preferredCompletionMultiplication SQ.[ x ] SQ.[ y ] ≡
    SQ.[ boundedProductRegular (canonicalDyadicallyBounded x) (canonicalDyadicallyBounded y) ]
  canonicalProductBridge x y = completionProductFromPresentations
    preferredRationalDyadicArchimedean x y
    (canonicalDyadicallyBounded x , refl) (canonicalDyadicallyBounded y , refl)

exponentialMultiplicationOnRepresentatives : (x y : RegularCauchy) →
  preferredCompletionMultiplication SQ.[ canonicalExponentialRegular x ]
    SQ.[ canonicalExponentialRegular y ] ≡
  SQ.[ canonicalExponentialRegular (addRegular x y) ]
exponentialMultiplicationOnRepresentatives x y =
  canonicalProductBridge (canonicalExponentialRegular x) (canonicalExponentialRegular y) ∙
  SQ.eq/ (exponentialProductRegular x y)
    (canonicalExponentialRegular (addRegular x y)) (exponentialMultiplicationMetric x y)
