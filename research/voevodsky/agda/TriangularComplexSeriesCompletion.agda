{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module TriangularComplexSeriesCompletion where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ)
import Cubical.Data.Nat.Order as ℕOrder
open import Cubical.Data.Sigma
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import RationalAnalyticSubstrate
open import RegularCauchyStructure
open import CauchyProductBounds
open import CauchyProductCongruence
open import ConstructiveComplexCompletion
open import ComplexCauchyApproximation
open import ComplexSeriesCompletion

triangular-stage-budget : (stage : ℕ) →
  (precision (ℕ.suc stage) Q.+ precision (ℕ.suc (ℕ.suc stage))) Q.+
    precision (ℕ.suc (ℕ.suc stage)) ≡ precision stage
triangular-stage-budget stage =
  sym (Q.+Assoc
    (precision (ℕ.suc stage))
    (precision (ℕ.suc (ℕ.suc stage)))
    (precision (ℕ.suc (ℕ.suc stage)))) ∙
  cong (precision (ℕ.suc stage) Q.+_)
    (half-double (precision (ℕ.suc stage))) ∙
  half-double (precision stage)

triangular-paired-stage-budget : (m n : ℕ) →
  ((precision (ℕ.suc m) Q.+ precision (ℕ.suc (ℕ.suc m))) Q.+
      precision (ℕ.suc (ℕ.suc m))) Q.+
    ((precision (ℕ.suc n) Q.+ precision (ℕ.suc (ℕ.suc n))) Q.+
      precision (ℕ.suc (ℕ.suc n))) ≡
  precision m Q.+ precision n
triangular-paired-stage-budget m n =
  cong₂ Q._+_ (triangular-stage-budget m) (triangular-stage-budget n)

record TriangularComplexSeriesApproximation : Type where
  field
    partialSumApproximation : ℕ → RationalComplex
    includedThrough : ℕ → ℕ
    approximationDepth : ℕ → ℕ
    depthAtLeastTwoSteps : (stage : ℕ) →
      ℕOrder._≤_ (ℕ.suc (ℕ.suc stage)) (approximationDepth stage)
open TriangularComplexSeriesApproximation public

record CofinalTriangularSchedule
  (approximation : TriangularComplexSeriesApproximation) : Type where
  field
    includedThroughMonotone : (m n : ℕ) → ℕOrder._≤_ m n →
      ℕOrder._≤_ (includedThrough approximation m)
        (includedThrough approximation n)
    eventuallyIncludes : (termIndex : ℕ) →
      Σ[ stage ∈ ℕ ]
        ℕOrder._≤_ termIndex (includedThrough approximation stage)
open CofinalTriangularSchedule public

record TriangularDifferenceCertificate
  (approximation : TriangularComplexSeriesApproximation) : Type where
  field
    differenceBound : (m n : ℕ) →
      ComplexMagnitudeBound
        (complexDifference
          (partialSumApproximation approximation m)
          (partialSumApproximation approximation n))
        (precision m Q.+ precision n)
open TriangularDifferenceCertificate public

triangularRealRegular :
  (approximation : TriangularComplexSeriesApproximation) →
  TriangularDifferenceCertificate approximation → RegularCauchy
triangularRealRegular approximation certificate .approximation n =
  rationalRealPart (partialSumApproximation approximation n)
triangularRealRegular approximation certificate .close-forward m n =
  split-error-directed
    (rationalRealPart (partialSumApproximation approximation m))
    (rationalRealPart (partialSumApproximation approximation n))
    (precision m) (precision n)
    (positive-upper (realBound (differenceBound certificate m n)))
triangularRealRegular approximation certificate .close-backward m n =
  split-error-directed
    (rationalRealPart (partialSumApproximation approximation n))
    (rationalRealPart (partialSumApproximation approximation m))
    (precision m) (precision n)
    (subst
      (λ bound →
        rationalRealPart (partialSumApproximation approximation n) Q.+
          (Q.- rationalRealPart (partialSumApproximation approximation m)) ≤ bound)
      (Q.+Comm (precision n) (precision m))
      (positive-upper (realBound (differenceBound certificate n m))))

triangularImaginaryRegular :
  (approximation : TriangularComplexSeriesApproximation) →
  TriangularDifferenceCertificate approximation → RegularCauchy
triangularImaginaryRegular approximation certificate .approximation n =
  rationalImaginaryPart (partialSumApproximation approximation n)
triangularImaginaryRegular approximation certificate .close-forward m n =
  split-error-directed
    (rationalImaginaryPart (partialSumApproximation approximation m))
    (rationalImaginaryPart (partialSumApproximation approximation n))
    (precision m) (precision n)
    (positive-upper (imaginaryBound (differenceBound certificate m n)))
triangularImaginaryRegular approximation certificate .close-backward m n =
  split-error-directed
    (rationalImaginaryPart (partialSumApproximation approximation n))
    (rationalImaginaryPart (partialSumApproximation approximation m))
    (precision m) (precision n)
    (subst
      (λ bound →
        rationalImaginaryPart (partialSumApproximation approximation n) Q.+
          (Q.- rationalImaginaryPart (partialSumApproximation approximation m)) ≤ bound)
      (Q.+Comm (precision n) (precision m))
      (positive-upper (imaginaryBound (differenceBound certificate n m))))

record TriangularComplexSeriesCertificate : Type₁ where
  field
    approximation : TriangularComplexSeriesApproximation
    cofinalSchedule : CofinalTriangularSchedule approximation
    cauchyDifference : TriangularDifferenceCertificate approximation
open TriangularComplexSeriesCertificate public

triangularComplexRegular :
  TriangularComplexSeriesCertificate → ComplexRegular
triangularComplexRegular certificate =
  triangularRealRegular (approximation certificate) (cauchyDifference certificate) ,
  triangularImaginaryRegular (approximation certificate) (cauchyDifference certificate)

completedTriangularComplexSeries :
  TriangularComplexSeriesCertificate → ComplexCompletion
completedTriangularComplexSeries certificate =
  complexRegularClass (triangularComplexRegular certificate)
