{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module OperationalZetaPrimitives where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; zero)
open import Cubical.Data.Rationals as Q
open import Cubical.HITs.SetQuotients as SQ using ([_])
open import RegularCauchyStructure
open import CauchyCompletionAbGroup
open import ConstructiveComplexCompletion
open import OperationalAnalyticZeroLaws
open import RationalLogConvergenceContract
open import AtanhPowerDecayContract
open import AtanhTailBounds
open import ConstructiveDirichletTerm
open import OperationalDirichletTerm
open import OperationalDirichletPartialSum
open import ConstructiveZetaInterfaces

operationalPositiveSuccessorLog :
  PositiveNaturalLogEvaluationFamily → ℕ → ComplexCompletion
operationalPositiveSuccessorLog logarithms n =
  embedRegularReal (positiveNaturalLogRegularFromInput n (logarithms n))

zeroRational : Q.ℚ
zeroRational = 0

record OperationalZetaPrimitiveInput : Type₁ where
  field
    logarithms : PositiveNaturalLogEvaluationFamily
    logOneRegular :
      positiveNaturalLogRegularFromInput zero (logarithms zero) ≡
      constantCauchy zeroRational
open OperationalZetaPrimitiveInput public

operational-zeta-primitive-input :
  PositiveNaturalLogEvaluationFamily → OperationalZetaPrimitiveInput
operational-zeta-primitive-input logarithms .logarithms = logarithms
operational-zeta-primitive-input logarithms .logOneRegular =
  positive-natural-log-one-any-block-is-zero
    (gap (logarithms zero)) (halfBlock (logarithms zero))

operational-zeta-primitive-input-from-power-principle :
  DyadicGapHalfPowerPrinciple →
  ((n : ℕ) → PositiveNaturalLogGapCertificate n) →
  OperationalZetaPrimitiveInput
operational-zeta-primitive-input-from-power-principle principle gaps =
  operational-zeta-primitive-input
    (log-evaluation-family-from-power-principle principle gaps)

canonicalPositiveNaturalLogGapCertificates :
  (n : ℕ) → PositiveNaturalLogGapCertificate n
canonicalPositiveNaturalLogGapCertificates =
  reciprocal-bridge-gives-gap-certificate
    canonicalPositiveNaturalLogReciprocalBridge

operational-zeta-primitive-input-from-reciprocal-bridge :
  DyadicGapHalfPowerPrinciple → PositiveNaturalLogReciprocalBridge →
  OperationalZetaPrimitiveInput
operational-zeta-primitive-input-from-reciprocal-bridge principle bridge =
  operational-zeta-primitive-input-from-power-principle principle
    (reciprocal-bridge-gives-gap-certificate bridge)

operational-input-log-one : (input : OperationalZetaPrimitiveInput) →
  operationalPositiveSuccessorLog (logarithms input) zero ≡ zeroComplex
operational-input-log-one input =
  complex-ext _ _ (cong SQ.[_] (logOneRegular input)) refl

operationalNegativePowerExpression :
  OperationalZetaPrimitiveInput →
  RationalRightHalfPlanePoint → ℕ → ComplexCompletion
operationalNegativePowerExpression input s n =
  operationalPositiveNaturalDirichletTerm n (logarithms input n)
    (rationalPointCompletion s)

operationalCertifiedComplexExpNaturalLog :
  OperationalZetaPrimitiveInput → CertifiedComplexExpNaturalLog
operationalCertifiedComplexExpNaturalLog input .complexExp =
  operationalComplexExponential
operationalCertifiedComplexExpNaturalLog input .positiveSuccessorLog =
  operationalPositiveSuccessorLog (logarithms input)
operationalCertifiedComplexExpNaturalLog input .negativePowerExpression =
  operationalNegativePowerExpression input
operationalCertifiedComplexExpNaturalLog input .negativePowerExpressionLaw s n =
  operationalNegativePowerExpression input s n ≡
  operationalPositiveNaturalDirichletTerm n (logarithms input n)
    (rationalPointCompletion s)
operationalCertifiedComplexExpNaturalLog input .negativePowerExpressionLaw-isProp s n =
  complex-isSet _ _
operationalCertifiedComplexExpNaturalLog input .negativePowerExpressionIsExpNegProduct s n =
  refl
operationalCertifiedComplexExpNaturalLog input .expZero =
  operational-complex-exponential-zero
operationalCertifiedComplexExpNaturalLog input .logOne =
  operational-input-log-one input

operationalCertifiedPrimitivesFromBridges :
  DyadicGapHalfPowerPrinciple → PositiveNaturalLogReciprocalBridge →
  CertifiedComplexExpNaturalLog
operationalCertifiedPrimitivesFromBridges principle bridge =
  operationalCertifiedComplexExpNaturalLog
    (operational-zeta-primitive-input-from-reciprocal-bridge principle bridge)

canonicalOperationalZetaPrimitiveInput : OperationalZetaPrimitiveInput
canonicalOperationalZetaPrimitiveInput =
  operational-zeta-primitive-input canonicalPositiveNaturalLogEvaluationFamily

operational-zeta-primitive-input-from-half-blocks :
  PositiveNaturalLogHalfBlockFamily → OperationalZetaPrimitiveInput
operational-zeta-primitive-input-from-half-blocks blocks =
  operational-zeta-primitive-input
    (log-evaluation-family-from-half-blocks blocks)

operational-zeta-primitive-input-from-half-power :
  DyadicGapHalfPowerPrinciple → OperationalZetaPrimitiveInput
operational-zeta-primitive-input-from-half-power principle =
  operational-zeta-primitive-input-from-power-principle principle
    canonicalPositiveNaturalLogGapCertificates

record OperationalZetaConstructionAssumptions : Type where
  field
    logarithmArithmetic : PositiveNaturalLogArithmeticBridge
    halfPower : DyadicGapHalfPowerPrinciple
open OperationalZetaConstructionAssumptions public

canonicalOperationalCertifiedPrimitives : CertifiedComplexExpNaturalLog
canonicalOperationalCertifiedPrimitives =
  operationalCertifiedComplexExpNaturalLog canonicalOperationalZetaPrimitiveInput

operationalCertifiedPrimitivesFromHalfBlocks :
  PositiveNaturalLogHalfBlockFamily → CertifiedComplexExpNaturalLog
operationalCertifiedPrimitivesFromHalfBlocks blocks =
  operationalCertifiedComplexExpNaturalLog
    (operational-zeta-primitive-input-from-half-blocks blocks)

operationalCertifiedPrimitivesFromHalfPower :
  DyadicGapHalfPowerPrinciple → CertifiedComplexExpNaturalLog
operationalCertifiedPrimitivesFromHalfPower principle =
  operationalCertifiedComplexExpNaturalLog
    (operational-zeta-primitive-input-from-half-power principle)

operationalCertifiedPrimitivesFromArithmeticBridge :
  DyadicGapHalfPowerPrinciple → PositiveNaturalLogArithmeticBridge →
  CertifiedComplexExpNaturalLog
operationalCertifiedPrimitivesFromArithmeticBridge principle arithmetic =
  operationalCertifiedPrimitivesFromBridges principle
    (arithmetic-bridge-gives-reciprocal-bridge arithmetic)

operationalCertifiedPrimitives :
  OperationalZetaConstructionAssumptions → CertifiedComplexExpNaturalLog
operationalCertifiedPrimitives assumptions =
  operationalCertifiedPrimitivesFromArithmeticBridge
    (halfPower assumptions) (logarithmArithmetic assumptions)
