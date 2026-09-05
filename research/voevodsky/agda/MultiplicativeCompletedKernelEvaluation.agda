{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module MultiplicativeCompletedKernelEvaluation where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Function using (_∘_)
open import Cubical.Algebra.AbGroup
open import AnalyticKernelEvaluation
open import SymbolicKernelCoefficients
open import CauchyMetricEquivalence
open import Cubical.Data.Rationals as Q
open import Cubical.HITs.SetQuotients as SQ using ([_])
open import RegularCauchyStructure
open import CauchyCompletionAbGroup
open import CauchyCompletionMultiplication
open import CauchyCompletionMultiplicativeLaws
open import CompletedKernelEvaluation
open import CompletionUnaryDescent
open import TaylorLiftContract

record RemainingTranscendentalOperations : Type₁ where
  field
    exponential : MetricCompletionCandidate → MetricCompletionCandidate
    cosine : MetricCompletionCandidate → MetricCompletionCandidate
open RemainingTranscendentalOperations public

multiplicative-remaining-operations :
  RationalDyadicArchimedean →
  RemainingTranscendentalOperations →
  RemainingAnalyticOperations
multiplicative-remaining-operations arch transcendental = record
  { multiply = completionMultiplication arch
  ; exponential = RemainingTranscendentalOperations.exponential transcendental
  ; cosine = RemainingTranscendentalOperations.cosine transcendental
  }

module MultiplicativeCompletedModel
  (arch : RationalDyadicArchimedean)
  (transcendental : RemainingTranscendentalOperations) where

  remaining : RemainingAnalyticOperations
  remaining = multiplicative-remaining-operations arch transcendental

  module Completed = CompletedModel remaining
  open Completed public

  multiplication-is-constructed :
    RemainingAnalyticOperations.multiply remaining ≡
    completionMultiplication arch
  multiplication-is-constructed = refl

  multiplicative-tail-evaluation :
    (p : Parameters) →
    Completed.E.evaluate (Syntax.tail p) ≡
    completionMultiplication arch (tau p) (H p)
  multiplicative-tail-evaluation = completed-tail-evaluates-to-tau-H

preferred-completion-multiplicative-laws :
  CompletionMultiplicativeLawFragment preferredCompletionMultiplication
preferred-completion-multiplicative-laws =
  preferred-completion-multiplicative-law-fragment

preferred-multiplicative-remaining-operations :
  RemainingTranscendentalOperations → RemainingAnalyticOperations
preferred-multiplicative-remaining-operations =
  multiplicative-remaining-operations preferredRationalDyadicArchimedean

transcendental-operations-from-lifts :
  AnalyticUnaryLifts → RemainingTranscendentalOperations
transcendental-operations-from-lifts lifts = record
  { exponential = descendedExponential lifts
  ; cosine = descendedCosine lifts
  }

preferred-remaining-operations-from-lifts :
  AnalyticUnaryLifts → RemainingAnalyticOperations
preferred-remaining-operations-from-lifts =
  preferred-multiplicative-remaining-operations ∘
  transcendental-operations-from-lifts

preferred-remaining-operations-from-Taylor-certificates :
  ExponentialTaylorCertificate → CosineTaylorCertificate →
  RemainingAnalyticOperations
preferred-remaining-operations-from-Taylor-certificates
  exponentialCertificate cosineCertificate =
  preferred-remaining-operations-from-lifts
    (analyticLiftsFromTaylorCertificates
      exponentialCertificate cosineCertificate)

module PreferredMultiplicativeCompletedModel
  (transcendental : RemainingTranscendentalOperations) where

  remaining : RemainingAnalyticOperations
  remaining = preferred-multiplicative-remaining-operations transcendental

  module Completed = CompletedModel remaining
  open Completed public

  preferred-multiplication-is-constructed :
    RemainingAnalyticOperations.multiply remaining ≡
    preferredCompletionMultiplication
  preferred-multiplication-is-constructed = refl

  preferred-multiplicative-tail-evaluation :
    (p : Parameters) →
    Completed.E.evaluate (Syntax.tail p) ≡
    preferredCompletionMultiplication (tau p) (H p)
  preferred-multiplicative-tail-evaluation = completed-tail-evaluates-to-tau-H

  preferred-rational-tail-evaluation :
    (p : Parameters) (q r : Q.ℚ) →
    tau p ≡ embedMetricℚ q →
    H p ≡ embedMetricℚ r →
    Completed.E.evaluate (Syntax.tail p) ≡ embedMetricℚ (q Q.· r)
  preferred-rational-tail-evaluation p q r tauPath HPath =
    preferred-multiplicative-tail-evaluation p ∙
    cong₂ preferredCompletionMultiplication tauPath HPath ∙
    preferredCompletionMultiplication-preserves-rationals q r

module PreferredLiftedCompletedModel (lifts : AnalyticUnaryLifts) where
  module Completed = CompletedModel (preferred-remaining-operations-from-lifts lifts)
  open Completed public

  exponential-computes-on-representatives : (x : RegularCauchy) →
    AnalyticOperations.exponential Completed.ops ([ x ]) ≡
    [ onRepresentative (exponentialLift lifts) x ]
  exponential-computes-on-representatives =
    descendMetricUnary-on-representative (exponentialLift lifts)

  cosine-computes-on-representatives : (x : RegularCauchy) →
    AnalyticOperations.cosine Completed.ops ([ x ]) ≡
    [ onRepresentative (cosineLift lifts) x ]
  cosine-computes-on-representatives =
    descendMetricUnary-on-representative (cosineLift lifts)

module PreferredTaylorCompletedModel
  (exponentialCertificate : ExponentialTaylorCertificate)
  (cosineCertificate : CosineTaylorCertificate) where

  lifts : AnalyticUnaryLifts
  lifts = analyticLiftsFromTaylorCertificates
    exponentialCertificate cosineCertificate

  module Lifted = PreferredLiftedCompletedModel lifts
  open Lifted public

  certified-exponential-at-zero :
    AnalyticOperations.exponential Lifted.Completed.ops (embedMetricℚ 0) ≡
    embedMetricℚ 1
  certified-exponential-at-zero =
    constructed-exponential-at-zero
      exponentialCertificate cosineCertificate

  certified-cosine-at-zero :
    AnalyticOperations.cosine Lifted.Completed.ops (embedMetricℚ 0) ≡
    embedMetricℚ 1
  certified-cosine-at-zero =
    constructed-cosine-at-zero
      exponentialCertificate cosineCertificate
