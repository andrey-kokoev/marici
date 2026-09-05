{-# OPTIONS --safe --cubical --no-import-sorts --guardedness --lossy-unification #-}
module CanonicalNegativePowerKernel where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ)
open import Cubical.Data.Rationals as Q
open import RegularCauchyStructure
open import CauchyNegation
open import ConstructiveComplexCompletion
open import ComplexCauchyApproximation
open import ConstructiveZetaInterfaces
open import AtanhTailBounds
open import OperationalAnalyticZeroLaws
open import OperationalDirichletPartialSum
open import OperationalZetaPrimitives
open import CanonicalComplexRegularMultiplication
open import CanonicalComplexRegularExponential

negateComplexRegular : ComplexRegular → ComplexRegular
negateComplexRegular (real , imaginary) =
  negateRegular real , negateRegular imaginary

negateComplexRegularClass : (z : ComplexRegular) →
  complexRegularClass (negateComplexRegular z) ≡ negComplex (complexRegularClass z)
negateComplexRegularClass z = refl

kernelZeroRational : Q.ℚ
kernelZeroRational = 0

embedRegularRealSource : RegularCauchy → ComplexRegular
embedRegularRealSource real = real , constantCauchy kernelZeroRational

canonicalNegativeSuccessorPower :
  RationalRightHalfPlanePoint → ℕ → ComplexRegular
canonicalNegativeSuccessorPower s n =
  canonicalComplexRegularExponential
    (negateComplexRegular
      (canonicalComplexRegularProduct
        (embedRationalComplexRegular (rationalPoint s))
        (embedRegularRealSource
          (positiveNaturalLogRegularFromInput n
            (canonicalPositiveNaturalLogEvaluationFamily n)))))

canonicalNegativeSuccessorPowerClass :
  (s : RationalRightHalfPlanePoint) (n : ℕ) →
  complexRegularClass (canonicalNegativeSuccessorPower s n) ≡
  operationalNegativePowerExpression canonicalOperationalZetaPrimitiveInput s n
canonicalNegativeSuccessorPowerClass s n =
  canonicalComplexRegularExponentialClass _ ∙
  cong operationalComplexExponential
    (negateComplexRegularClass _ ∙
     cong negComplex
       (canonicalComplexRegularProductClass
         (embedRationalComplexRegular (rationalPoint s))
         (embedRegularRealSource
           (positiveNaturalLogRegularFromInput n
             (canonicalPositiveNaturalLogEvaluationFamily n)))))

canonicalNegativeSuccessorPowerKernel : CertifiedNegativeSuccessorPowerKernel
canonicalNegativeSuccessorPowerKernel .primitives =
  canonicalOperationalCertifiedPrimitives
canonicalNegativeSuccessorPowerKernel .negativeSuccessorPower =
  canonicalNegativeSuccessorPower
canonicalNegativeSuccessorPowerKernel .negativeSuccessorPowerSatisfiesExpression =
  canonicalNegativeSuccessorPowerClass
