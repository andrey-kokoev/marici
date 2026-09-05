{-# OPTIONS --safe --cubical --no-import-sorts --guardedness --lossy-unification #-}
module CanonicalDirichletRegularPartialSum where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; zero; suc)
open import ConstructiveComplexCompletion
open import ComplexCauchyApproximation
open import ConstructiveZetaInterfaces
open import OperationalDirichletPartialSum
open import OperationalZetaPrimitives
open import CanonicalNegativePowerKernel

canonicalDirichletRegularPartialSum :
  RationalRightHalfPlanePoint → ℕ → ComplexRegular
canonicalDirichletRegularPartialSum s =
  complexRegularFiniteSum (canonicalNegativeSuccessorPower s)

canonicalDirichletRegularPartialSumIsFinitePowerSum :
  (s : RationalRightHalfPlanePoint) (included : ℕ) →
  canonicalDirichletRegularPartialSum s included ≡
  complexRegularFiniteSum
    (negativeSuccessorPower canonicalNegativeSuccessorPowerKernel s) included
canonicalDirichletRegularPartialSumIsFinitePowerSum s included = refl

canonicalDirichletRegularPartialSumClass :
  (s : RationalRightHalfPlanePoint) (included : ℕ) →
  complexRegularClass (canonicalDirichletRegularPartialSum s included) ≡
  canonicalOperationalDirichletPartialSum (rationalPointCompletion s) included
canonicalDirichletRegularPartialSumClass s zero =
  canonicalNegativeSuccessorPowerClass s zero
canonicalDirichletRegularPartialSumClass s (suc included) =
  cong₂ _+complex_
    (canonicalDirichletRegularPartialSumClass s included)
    (canonicalNegativeSuccessorPowerClass s (suc included))
