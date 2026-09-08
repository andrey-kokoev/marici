{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CompletionExponentialMultiplicationLaw where

open import Cubical.Foundations.Prelude
import Cubical.HITs.SetQuotients as SQ
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyAddition
open import CauchyAdditionCongruence
open import CauchyCompletionMultiplication
open import CanonicalExponentialRegularity
open import OperationalExponentialMetric
open import CompletedExponentialMultiplication
open import CompletionUnaryDescent

abstract
  completionExponentialOnRepresentative : (x : RegularCauchy) →
    completionExponential SQ.[ x ] ≡ SQ.[ canonicalExponentialRegular x ]
  completionExponentialOnRepresentative x =
    descendMetricUnary-on-representative canonicalExponentialMetricLift x ∙
    cong (λ r → SQ.[_] {R = _≈metric_} r)
      (regularCauchy-ext (onRepresentative canonicalExponentialMetricLift x)
        (canonicalExponentialRegular x) refl)

  completionAdditionOnRepresentatives : (x y : RegularCauchy) →
    (SQ.[ x ] +completion SQ.[ y ]) ≡ SQ.[ addRegular x y ]
  completionAdditionOnRepresentatives x y = refl

  representativeLaw : (x y : RegularCauchy) →
    preferredCompletionMultiplication (completionExponential SQ.[ x ])
      (completionExponential SQ.[ y ]) ≡
    completionExponential (SQ.[ x ] +completion SQ.[ y ])
  representativeLaw x y =
    cong₂ preferredCompletionMultiplication
      (completionExponentialOnRepresentative x) (completionExponentialOnRepresentative y) ∙
    exponentialMultiplicationOnRepresentatives x y ∙
    sym (completionExponentialOnRepresentative (addRegular x y)) ∙
    sym (cong completionExponential (completionAdditionOnRepresentatives x y))

completionExponentialMultiplication : (x y : MetricCompletionCandidate) →
  preferredCompletionMultiplication (completionExponential x) (completionExponential y) ≡
  completionExponential (x +completion y)
completionExponentialMultiplication = SQ.elimProp2
  {P = λ x y →
    preferredCompletionMultiplication (completionExponential x) (completionExponential y) ≡
    completionExponential (x +completion y)}
  (λ x y → metric-candidate-isSet
    (preferredCompletionMultiplication (completionExponential x) (completionExponential y))
    (completionExponential (x +completion y)))
  representativeLaw
