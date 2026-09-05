{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module TaylorLiftContract where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import RationalTaylorApproximants
open import ExponentialSeedConstruction
open import CosineSeedConstruction
open import TaylorValuesAtZero
open import CompletionUnaryDescent

scheduledSeriesApproximation :
  (Q.ℚ → ℕ → Q.ℚ) →
  TaylorCutoffSchedule → RegularCauchy → ℕ → Q.ℚ
scheduledSeriesApproximation partialSum schedule x n =
  partialSum
    (approximation x (input-depth schedule n))
    (series-depth schedule n)

record ScheduledSeriesRegularity
  (partialSum : Q.ℚ → ℕ → Q.ℚ) : Type where
  field
    scheduleFor : RegularCauchy → TaylorCutoffSchedule
    closeSeriesForward : (x : RegularCauchy) (m n : ℕ) →
      scheduledSeriesApproximation partialSum (scheduleFor x) x m ≤
      (scheduledSeriesApproximation partialSum (scheduleFor x) x n Q.+
       precision m) Q.+ precision n
    closeSeriesBackward : (x : RegularCauchy) (m n : ℕ) →
      scheduledSeriesApproximation partialSum (scheduleFor x) x n ≤
      (scheduledSeriesApproximation partialSum (scheduleFor x) x m Q.+
       precision m) Q.+ precision n
open ScheduledSeriesRegularity public

scheduledSeriesRegular :
  {partialSum : Q.ℚ → ℕ → Q.ℚ} →
  ScheduledSeriesRegularity partialSum → RegularCauchy → RegularCauchy
scheduledSeriesRegular {partialSum} certificate x .approximation =
  scheduledSeriesApproximation partialSum (scheduleFor certificate x) x
scheduledSeriesRegular {partialSum} certificate x .close-forward =
  closeSeriesForward certificate x
scheduledSeriesRegular {partialSum} certificate x .close-backward =
  closeSeriesBackward certificate x

record ScheduledSeriesLiftCertificate
  (partialSum : Q.ℚ → ℕ → Q.ℚ) : Type where
  field
    regularity : ScheduledSeriesRegularity partialSum
    respectsSeriesMetric : (x y : RegularCauchy) →
      x ≈metric y →
      scheduledSeriesRegular regularity x ≈metric
      scheduledSeriesRegular regularity y
open ScheduledSeriesLiftCertificate public

metricLiftFromSeriesCertificate :
  {partialSum : Q.ℚ → ℕ → Q.ℚ} →
  ScheduledSeriesLiftCertificate partialSum → MetricUnaryLift
metricLiftFromSeriesCertificate certificate .onRepresentative =
  scheduledSeriesRegular (regularity certificate)
metricLiftFromSeriesCertificate certificate .respectsMetric =
  respectsSeriesMetric certificate

record ExponentialTaylorCertificate : Type where
  field
    exponentialSeriesCertificate :
      ScheduledSeriesLiftCertificate exponentialPartialSum
    exponentialAgreesOnRationals : (q : Q.ℚ) →
      descendMetricUnary
        (metricLiftFromSeriesCertificate exponentialSeriesCertificate)
        (embedMetricℚ q) ≡ rationalExponentialValue q
open ExponentialTaylorCertificate public

record CosineTaylorCertificate : Type where
  field
    cosineSeriesCertificate :
      ScheduledSeriesLiftCertificate cosinePartialSum
    cosineAgreesOnRationals : (q : Q.ℚ) →
      descendMetricUnary
        (metricLiftFromSeriesCertificate cosineSeriesCertificate)
        (embedMetricℚ q) ≡ rationalCosineValue q
open CosineTaylorCertificate public

analyticLiftsFromTaylorCertificates :
  ExponentialTaylorCertificate → CosineTaylorCertificate →
  AnalyticUnaryLifts
analyticLiftsFromTaylorCertificates exponentialCertificate cosineCertificate = record
  { exponentialLift = metricLiftFromSeriesCertificate
      (exponentialSeriesCertificate exponentialCertificate)
  ; cosineLift = metricLiftFromSeriesCertificate
      (cosineSeriesCertificate cosineCertificate)
  }

constructed-exponential-agrees-on-rationals :
  (exponentialCertificate : ExponentialTaylorCertificate) →
  (cosineCertificate : CosineTaylorCertificate) → (q : Q.ℚ) →
  descendedExponential
    (analyticLiftsFromTaylorCertificates
      exponentialCertificate cosineCertificate)
    (embedMetricℚ q) ≡ rationalExponentialValue q
constructed-exponential-agrees-on-rationals
  exponentialCertificate cosineCertificate q =
  exponentialAgreesOnRationals exponentialCertificate q

constructed-cosine-agrees-on-rationals :
  (exponentialCertificate : ExponentialTaylorCertificate) →
  (cosineCertificate : CosineTaylorCertificate) → (q : Q.ℚ) →
  descendedCosine
    (analyticLiftsFromTaylorCertificates
      exponentialCertificate cosineCertificate)
    (embedMetricℚ q) ≡ rationalCosineValue q
constructed-cosine-agrees-on-rationals
  exponentialCertificate cosineCertificate q =
  cosineAgreesOnRationals cosineCertificate q

constructed-exponential-at-zero :
  (exponentialCertificate : ExponentialTaylorCertificate) →
  (cosineCertificate : CosineTaylorCertificate) →
  descendedExponential
    (analyticLiftsFromTaylorCertificates
      exponentialCertificate cosineCertificate)
    (embedMetricℚ 0) ≡ embedMetricℚ 1
constructed-exponential-at-zero exponentialCertificate cosineCertificate =
  constructed-exponential-agrees-on-rationals
    exponentialCertificate cosineCertificate 0 ∙
  rationalExponentialValue-at-zero

constructed-cosine-at-zero :
  (exponentialCertificate : ExponentialTaylorCertificate) →
  (cosineCertificate : CosineTaylorCertificate) →
  descendedCosine
    (analyticLiftsFromTaylorCertificates
      exponentialCertificate cosineCertificate)
    (embedMetricℚ 0) ≡ embedMetricℚ 1
constructed-cosine-at-zero exponentialCertificate cosineCertificate =
  constructed-cosine-agrees-on-rationals
    exponentialCertificate cosineCertificate 0 ∙
  rationalCosineValue-at-zero
