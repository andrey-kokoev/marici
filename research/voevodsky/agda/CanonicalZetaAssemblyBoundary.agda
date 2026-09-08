{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CanonicalZetaAssemblyBoundary where

open import Cubical.Foundations.Prelude
open import ConstructiveZetaInterfaces
open import TriangularComplexSeriesCompletion
open import CanonicalNegativePowerKernel
open import CanonicalDirichletRegularPartialSum
open import CanonicalDirichletTriangularApproximation

-- Dependency probe only: no inhabitant of this boundary is asserted.
CanonicalDirichletCauchyBoundary : Type
CanonicalDirichletCauchyBoundary =
  (s : RationalRightHalfPlanePoint) →
  TriangularDifferenceCertificate (canonicalDirichletTriangularApproximation s)

assembleCanonicalDirichletConditionally :
  CanonicalDirichletCauchyBoundary → CertifiedRightHalfPlaneDirichletSeries
assembleCanonicalDirichletConditionally bound .powerKernel =
  canonicalNegativeSuccessorPowerKernel
assembleCanonicalDirichletConditionally bound .dirichletPartialSumTarget =
  canonicalDirichletRegularPartialSum
assembleCanonicalDirichletConditionally bound .dirichletPartialSumTargetIsFinitePowerSum =
  canonicalDirichletRegularPartialSumIsFinitePowerSum
assembleCanonicalDirichletConditionally bound .dirichletApproximation =
  canonicalDirichletTriangularApproximation
assembleCanonicalDirichletConditionally bound .partialSumApproximationError =
  canonicalDirichletPartialSumApproximationError
assembleCanonicalDirichletConditionally bound .cofinality =
  canonicalDirichletTriangularCofinal
assembleCanonicalDirichletConditionally bound .cauchyDifference = bound
