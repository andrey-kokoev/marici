{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CompletionUnaryDescent where

open import Cubical.Foundations.Prelude
open import Cubical.HITs.SetQuotients as SQ using ([_])
open import Cubical.HITs.SetQuotients.Properties as SQP
open import RegularCauchyStructure
open import CauchyMetricEquivalence

record MetricUnaryLift : Type where
  field
    onRepresentative : RegularCauchy → RegularCauchy
    respectsMetric : (x y : RegularCauchy) →
      x ≈metric y → onRepresentative x ≈metric onRepresentative y
open MetricUnaryLift public

descendMetricUnary :
  MetricUnaryLift → MetricCompletionCandidate → MetricCompletionCandidate
descendMetricUnary operation =
  SQP.setQuotUnaryOp
    (onRepresentative operation)
    (respectsMetric operation)

descendMetricUnary-on-representative :
  (operation : MetricUnaryLift) (x : RegularCauchy) →
  descendMetricUnary operation ([ x ]) ≡
  [ onRepresentative operation x ]
descendMetricUnary-on-representative operation x = refl

record AnalyticUnaryLifts : Type where
  field
    exponentialLift : MetricUnaryLift
    cosineLift : MetricUnaryLift
open AnalyticUnaryLifts public

descendedExponential :
  AnalyticUnaryLifts →
  MetricCompletionCandidate → MetricCompletionCandidate
descendedExponential lifts =
  descendMetricUnary (exponentialLift lifts)

descendedCosine :
  AnalyticUnaryLifts →
  MetricCompletionCandidate → MetricCompletionCandidate
descendedCosine lifts =
  descendMetricUnary (cosineLift lifts)
