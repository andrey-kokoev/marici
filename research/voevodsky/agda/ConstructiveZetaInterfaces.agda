{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module ConstructiveZetaInterfaces where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import RegularCauchyStructure
open import CauchyAddition
open import ComplexCauchyApproximation
open import ConstructiveComplexCompletion
open import ComplexSeriesCompletion
open import TriangularComplexSeriesCompletion

record RationalRightHalfPlanePoint : Type where
  field
    rationalPoint : RationalComplex
    realPartAboveOne : 1 < rationalRealPart rationalPoint
open RationalRightHalfPlanePoint public

addComplexRegular : ComplexRegular → ComplexRegular → ComplexRegular
addComplexRegular (zr , zi) (wr , wi) =
  addRegular zr wr , addRegular zi wi

complexRegularFiniteSum : (ℕ → ComplexRegular) → ℕ → ComplexRegular
complexRegularFiniteSum summand ℕ.zero = summand ℕ.zero
complexRegularFiniteSum summand (ℕ.suc n) =
  addComplexRegular (complexRegularFiniteSum summand n) (summand (ℕ.suc n))

rationalPointCompletion : RationalRightHalfPlanePoint → ComplexCompletion
rationalPointCompletion s =
  complexRegularClass (embedRationalComplexRegular (rationalPoint s))

record CertifiedComplexExpNaturalLog : Type₁ where
  field
    complexExp : ComplexCompletion → ComplexCompletion
    positiveSuccessorLog : ℕ → ComplexCompletion
    negativePowerExpression :
      RationalRightHalfPlanePoint → ℕ → ComplexCompletion
    negativePowerExpressionLaw :
      RationalRightHalfPlanePoint → ℕ → Type
    negativePowerExpressionLaw-isProp :
      (s : RationalRightHalfPlanePoint) (n : ℕ) →
      isProp (negativePowerExpressionLaw s n)
    negativePowerExpressionIsExpNegProduct :
      (s : RationalRightHalfPlanePoint) (n : ℕ) →
      negativePowerExpressionLaw s n
    expZero : complexExp zeroComplex ≡ oneComplex
    logOne : positiveSuccessorLog ℕ.zero ≡ zeroComplex
open CertifiedComplexExpNaturalLog public

negativeSuccessorPowerExpression :
  CertifiedComplexExpNaturalLog → RationalRightHalfPlanePoint → ℕ →
  ComplexCompletion
negativeSuccessorPowerExpression primitives s n =
  negativePowerExpression primitives s n

record CertifiedNegativeSuccessorPowerKernel : Type₁ where
  field
    primitives : CertifiedComplexExpNaturalLog
    negativeSuccessorPower :
      RationalRightHalfPlanePoint → ℕ → ComplexRegular
    negativeSuccessorPowerSatisfiesExpression :
      (s : RationalRightHalfPlanePoint) (n : ℕ) →
      complexRegularClass (negativeSuccessorPower s n) ≡
      negativeSuccessorPowerExpression primitives s n
open CertifiedNegativeSuccessorPowerKernel public

record CertifiedRightHalfPlaneDirichletSeries : Type₁ where
  field
    powerKernel : CertifiedNegativeSuccessorPowerKernel
    dirichletPartialSumTarget :
      RationalRightHalfPlanePoint → ℕ → ComplexRegular
    dirichletPartialSumTargetIsFinitePowerSum :
      (s : RationalRightHalfPlanePoint) (included : ℕ) →
      dirichletPartialSumTarget s included ≡
      complexRegularFiniteSum (negativeSuccessorPower powerKernel s) included

    dirichletApproximation :
      RationalRightHalfPlanePoint → TriangularComplexSeriesApproximation
    partialSumApproximationError :
      (s : RationalRightHalfPlanePoint) (stage : ℕ) →
      ComplexMagnitudeBound
        (complexDifference
          (partialSumApproximation (dirichletApproximation s) stage)
          (complexApproximation
            (dirichletPartialSumTarget s
              (includedThrough (dirichletApproximation s) stage))
            (approximationDepth (dirichletApproximation s) stage)))
        (precision (ℕ.suc (ℕ.suc stage)))
    cofinality : (s : RationalRightHalfPlanePoint) →
      CofinalTriangularSchedule (dirichletApproximation s)
    cauchyDifference : (s : RationalRightHalfPlanePoint) →
      TriangularDifferenceCertificate (dirichletApproximation s)
open CertifiedRightHalfPlaneDirichletSeries public

rightHalfPlaneCompletionCertificate :
  (evaluator : CertifiedRightHalfPlaneDirichletSeries) →
  RationalRightHalfPlanePoint → TriangularComplexSeriesCertificate
rightHalfPlaneCompletionCertificate evaluator s .approximation =
  dirichletApproximation evaluator s
rightHalfPlaneCompletionCertificate evaluator s .cofinalSchedule =
  cofinality evaluator s
rightHalfPlaneCompletionCertificate evaluator s .cauchyDifference =
  cauchyDifference evaluator s

rightHalfPlaneZetaValue :
  CertifiedRightHalfPlaneDirichletSeries →
  RationalRightHalfPlanePoint → ComplexCompletion
rightHalfPlaneZetaValue evaluator s =
  completedTriangularComplexSeries
    (rightHalfPlaneCompletionCertificate evaluator s)

record AnalyticContinuationInterface
  (evaluator : CertifiedRightHalfPlaneDirichletSeries) : Type₁ where
  field
    ContinuationDomain : Type
    continuationPoint : ContinuationDomain → ComplexCompletion
    continuationValue : ContinuationDomain → ComplexCompletion

    AnalyticValueFamily : (ContinuationDomain → ComplexCompletion) → Type
    analyticValueFamily-isProp :
      (value : ContinuationDomain → ComplexCompletion) →
      isProp (AnalyticValueFamily value)
    continuationIsAnalytic : AnalyticValueFamily continuationValue

    OverlapWitness : Type
    overlapHalfPlanePoint : OverlapWitness → RationalRightHalfPlanePoint
    overlapContinuationPoint : OverlapWitness → ContinuationDomain
    overlapPointAgreement : (w : OverlapWitness) →
      continuationPoint (overlapContinuationPoint w) ≡
      complexRegularClass
        (embedRationalComplexRegular
          (rationalPoint (overlapHalfPlanePoint w)))
    overlapValueAgreement : (w : OverlapWitness) →
      continuationValue (overlapContinuationPoint w) ≡
      rightHalfPlaneZetaValue evaluator (overlapHalfPlanePoint w)
open AnalyticContinuationInterface public

AgreesWithDirichletOnOverlap :
  {evaluator : CertifiedRightHalfPlaneDirichletSeries} →
  (continuation : AnalyticContinuationInterface evaluator) →
  (ContinuationDomain continuation → ComplexCompletion) → Type
AgreesWithDirichletOnOverlap {evaluator = evaluator} continuation candidate =
  (w : OverlapWitness continuation) →
    candidate (overlapContinuationPoint continuation w) ≡
    rightHalfPlaneZetaValue evaluator (overlapHalfPlanePoint continuation w)

record CertifiedAnalyticContinuation
  {evaluator : CertifiedRightHalfPlaneDirichletSeries}
  (continuation : AnalyticContinuationInterface evaluator) : Type₁ where
  field
    uniqueness :
      (candidate : ContinuationDomain continuation → ComplexCompletion) →
      AnalyticValueFamily continuation candidate →
      AgreesWithDirichletOnOverlap continuation candidate →
      candidate ≡ continuationValue continuation
open CertifiedAnalyticContinuation public

record CriticalStripInterface
  {evaluator : CertifiedRightHalfPlaneDirichletSeries}
  (continuation : AnalyticContinuationInterface evaluator) : Type₁ where
  field
    certifiedContinuation : CertifiedAnalyticContinuation continuation
    CriticalStripPoint : Type
    asContinuationPoint : CriticalStripPoint → ContinuationDomain continuation
    certifiedCriticalStrip : CriticalStripPoint → Type
    certifiedCriticalStrip-isProp : (s : CriticalStripPoint) →
      isProp (certifiedCriticalStrip s)
open CriticalStripInterface public

criticalStripZetaValue :
  {evaluator : CertifiedRightHalfPlaneDirichletSeries} →
  {continuation : AnalyticContinuationInterface evaluator} →
  (strip : CriticalStripInterface continuation) →
  CriticalStripPoint strip → ComplexCompletion
criticalStripZetaValue {continuation = continuation} strip s =
  continuationValue continuation (asContinuationPoint strip s)
