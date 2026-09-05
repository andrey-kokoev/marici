{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module RegularCauchyTriangularEmbedding where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ)
import Cubical.Data.Nat.Order as ℕOrder
open import Cubical.Data.Rationals as Q
open import Cubical.HITs.SetQuotients as SQ using ([_]; eq/)
open import Cubical.Data.Rationals.Order
open import RegularCauchyStructure
open import CauchyProductBounds
open import CauchyMetricEquivalence
open import CauchyShift
open import CauchyProductErrorBounds
open import ConstructiveComplexCompletion
open import ComplexCauchyApproximation
open import ComplexSeriesCompletion
open import TriangularComplexSeriesCompletion

realRegularRationalComplex : RegularCauchy → ℕ → RationalComplex
realRegularRationalComplex x stage =
  rationalComplex (approximation x stage) 0

real-regular-complex-difference-bound : (x : RegularCauchy) (m n : ℕ) →
  ComplexMagnitudeBound
    (complexDifference
      (realRegularRationalComplex x m)
      (realRegularRationalComplex x n))
    (precision m Q.+ precision n)
real-regular-complex-difference-bound x m n .realBound =
  regular-approximation-difference-bound x m n
real-regular-complex-difference-bound x m n .imaginaryBound = record
  { positive-upper = precision-sum-nonnegative m n
  ; negative-upper = precision-sum-nonnegative m n
  }

shiftedRealRegularTriangularApproximation :
  RegularCauchy → TriangularComplexSeriesApproximation
shiftedRealRegularTriangularApproximation x .partialSumApproximation stage =
  realRegularRationalComplex x (ℕ.suc (ℕ.suc stage))
shiftedRealRegularTriangularApproximation x .includedThrough stage = stage
shiftedRealRegularTriangularApproximation x .approximationDepth stage =
  ℕ.suc (ℕ.suc stage)
shiftedRealRegularTriangularApproximation x .depthAtLeastTwoSteps stage =
  ℕOrder.≤-refl

shiftedRealRegularTriangularCofinal : (x : RegularCauchy) →
  CofinalTriangularSchedule (shiftedRealRegularTriangularApproximation x)
shiftedRealRegularTriangularCofinal x .includedThroughMonotone m n m≤n = m≤n
shiftedRealRegularTriangularCofinal x .eventuallyIncludes termIndex =
  termIndex , ℕOrder.≤-refl

shifted-real-regular-triangular-difference :
  (x : RegularCauchy) →
  TriangularDifferenceCertificate (shiftedRealRegularTriangularApproximation x)
shifted-real-regular-triangular-difference x .differenceBound m n =
  weaken-complex-magnitude-bound _
    (precision (ℕ.suc (ℕ.suc m)) Q.+ precision (ℕ.suc (ℕ.suc n)))
    (precision m Q.+ precision n)
    (≤Monotone+
      (precision (ℕ.suc (ℕ.suc m))) (precision m)
      (precision (ℕ.suc (ℕ.suc n))) (precision n)
      (precision-antitone m (ℕ.suc (ℕ.suc m))
        (2 , refl))
      (precision-antitone n (ℕ.suc (ℕ.suc n))
        (2 , refl)))
    (real-regular-complex-difference-bound x
      (ℕ.suc (ℕ.suc m)) (ℕ.suc (ℕ.suc n)))

shiftedRealRegularTriangularCertificate :
  (x : RegularCauchy) → TriangularComplexSeriesCertificate
shiftedRealRegularTriangularCertificate x .approximation =
  shiftedRealRegularTriangularApproximation x
shiftedRealRegularTriangularCertificate x .cofinalSchedule =
  shiftedRealRegularTriangularCofinal x
shiftedRealRegularTriangularCertificate x .cauchyDifference =
  shifted-real-regular-triangular-difference x

shiftedRealRegularTriangularValue : RegularCauchy → ComplexCompletion
shiftedRealRegularTriangularValue x =
  completedTriangularComplexSeries (shiftedRealRegularTriangularCertificate x)

shifted-triangular-real-path : (x : RegularCauchy) →
  triangularRealRegular
    (shiftedRealRegularTriangularApproximation x)
    (shifted-real-regular-triangular-difference x) ≡ iterateShift 2 x
shifted-triangular-real-path x = regularCauchy-ext _ _ refl

shifted-triangular-imaginary-zero : (x : RegularCauchy) →
  triangularImaginaryRegular
    (shiftedRealRegularTriangularApproximation x)
    (shifted-real-regular-triangular-difference x) ≡ constantCauchy 0
shifted-triangular-imaginary-zero x = regularCauchy-ext _ _ refl

shiftedRealRegularTriangularValueAgrees : (x : RegularCauchy) →
  shiftedRealRegularTriangularValue x ≡
  complexRegularClass (x , constantCauchy 0)
shiftedRealRegularTriangularValueAgrees x =
  complex-ext _ _
    (SQ.eq/ _ _
      (subst (_≈metric x) (sym (shifted-triangular-real-path x))
        (iterateShift-equivalent 2 x)))
    (cong SQ.[_] (shifted-triangular-imaginary-zero x))
