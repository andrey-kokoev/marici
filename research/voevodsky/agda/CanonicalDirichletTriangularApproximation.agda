{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CanonicalDirichletTriangularApproximation where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ)
import Cubical.Data.Nat.Order as ℕOrder
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import RegularCauchyStructure
open import CauchyProductBounds
open import ConstructiveComplexCompletion
open import ComplexCauchyApproximation
open import ComplexSeriesCompletion
open import TriangularComplexSeriesCompletion
open import ConstructiveZetaInterfaces
open import RationalLogConvergenceContract
open import CanonicalDirichletRegularPartialSum

canonicalDirichletTriangularApproximation :
  RationalRightHalfPlanePoint → TriangularComplexSeriesApproximation
canonicalDirichletTriangularApproximation s .partialSumApproximation stage =
  complexApproximation
    (canonicalDirichletRegularPartialSum s (dyadicReciprocalIndex (ℕ.suc stage)))
    (ℕ.suc (ℕ.suc stage))
canonicalDirichletTriangularApproximation s .includedThrough stage =
  dyadicReciprocalIndex (ℕ.suc stage)
canonicalDirichletTriangularApproximation s .approximationDepth stage =
  ℕ.suc (ℕ.suc stage)
canonicalDirichletTriangularApproximation s .depthAtLeastTwoSteps stage =
  ℕOrder.≤-refl

self-complex-difference-bound : (z : RationalComplex) (bound : Q.ℚ) →
  0 ≤ bound → ComplexMagnitudeBound (complexDifference z z) bound
self-complex-difference-bound z bound 0≤bound .realBound =
  subst (λ value → MagnitudeBound value bound)
    (sym (Q.+InvR (rationalRealPart z)))
    (record { positive-upper = 0≤bound ; negative-upper = 0≤bound })
self-complex-difference-bound z bound 0≤bound .imaginaryBound =
  subst (λ value → MagnitudeBound value bound)
    (sym (Q.+InvR (rationalImaginaryPart z)))
    (record { positive-upper = 0≤bound ; negative-upper = 0≤bound })

canonicalDirichletPartialSumApproximationError :
  (s : RationalRightHalfPlanePoint) (stage : ℕ) →
  ComplexMagnitudeBound
    (complexDifference
      (partialSumApproximation (canonicalDirichletTriangularApproximation s) stage)
      (complexApproximation
        (canonicalDirichletRegularPartialSum s
          (includedThrough (canonicalDirichletTriangularApproximation s) stage))
        (approximationDepth (canonicalDirichletTriangularApproximation s) stage)))
    (precision (ℕ.suc (ℕ.suc stage)))
canonicalDirichletPartialSumApproximationError s stage =
  self-complex-difference-bound
    (complexApproximation
      (canonicalDirichletRegularPartialSum s
        (dyadicReciprocalIndex (ℕ.suc stage)))
      (ℕ.suc (ℕ.suc stage)))
    (precision (ℕ.suc (ℕ.suc stage)))
    (precision-nonnegative (ℕ.suc (ℕ.suc stage)))

canonicalDirichletTriangularCofinal :
  (s : RationalRightHalfPlanePoint) →
  CofinalTriangularSchedule (canonicalDirichletTriangularApproximation s)
canonicalDirichletTriangularCofinal s .includedThroughMonotone m n m≤n =
  dyadic-reciprocal-index-monotone (ℕ.suc m) (ℕ.suc n)
    (ℕOrder.suc-≤-suc m≤n)
canonicalDirichletTriangularCofinal s .eventuallyIncludes termIndex =
  termIndex ,
  ℕOrder.pred-≤-pred
    (subst (ℕOrder._≤_ (ℕ.suc termIndex))
      (sym (dyadic-reciprocal-index-denominator (ℕ.suc termIndex)))
      (natural-index≤dyadic-index (ℕ.suc termIndex)))
