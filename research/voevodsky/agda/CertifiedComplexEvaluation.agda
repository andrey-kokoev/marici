{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CertifiedComplexEvaluation where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Sum
open import Cubical.Data.Rationals.Order
open import RationalAnalyticSubstrate
open import RegularCauchyStructure
open import CauchyProductBounds
open import CauchyProductErrorBounds
open import ComplexCauchyApproximation

ComplexRegularMap : Type
ComplexRegularMap = ComplexRegular → ComplexRegular

record CertifiedComplexEvaluator (f : ComplexRegularMap) : Type where
  field
    inputDepth : ℕ → ℕ
    evaluate : RationalComplex → ℕ → RationalComplex
    evaluation-real-error : (z : ComplexRegular) (n : ℕ) →
      MagnitudeBound
        (rationalRealPart
          (evaluate (complexApproximation z (inputDepth n)) n) Q.+
         (Q.- rationalRealPart (complexApproximation (f z) n)))
        (precision n)
    evaluation-imaginary-error : (z : ComplexRegular) (n : ℕ) →
      MagnitudeBound
        (rationalImaginaryPart
          (evaluate (complexApproximation z (inputDepth n)) n) Q.+
         (Q.- rationalImaginaryPart (complexApproximation (f z) n)))
        (precision n)
open CertifiedComplexEvaluator public

certifiedEvaluationCenter :
  {f : ComplexRegularMap} → CertifiedComplexEvaluator f →
  ComplexRegular → ℕ → RationalComplex
certifiedEvaluationCenter evaluator z n =
  evaluate evaluator (complexApproximation z (inputDepth evaluator n)) n

certifiedEvaluationDisk :
  {f : ComplexRegularMap} → CertifiedComplexEvaluator f →
  ComplexRegular → ℕ → RationalComplexDisk
certifiedEvaluationDisk evaluator z n = rationalComplexDisk
  (certifiedEvaluationCenter evaluator z n)
  (precision n) (precision-nonnegative n)

certified-evaluation-disk-contains :
  {f : ComplexRegularMap} (evaluator : CertifiedComplexEvaluator f) →
  (z : ComplexRegular) (n : ℕ) →
  InsideBoxAt (f z) (certifiedEvaluationDisk evaluator z n) n
certified-evaluation-disk-contains {f = f} evaluator z n =
  let realError = evaluation-real-error evaluator z n
      imaginaryError = evaluation-imaginary-error evaluator z n
  in
  transport-magnitude _ _ (precision n)
    (sym (ProductSignPaths.negative-difference PreferredℚCommRing
      (rationalRealPart (certifiedEvaluationCenter evaluator z n))
      (rationalRealPart (complexApproximation (f z) n))))
    (negate-magnitude-bound _ _ realError) ,
  transport-magnitude _ _ (precision n)
    (sym (ProductSignPaths.negative-difference PreferredℚCommRing
      (rationalImaginaryPart (certifiedEvaluationCenter evaluator z n))
      (rationalImaginaryPart (complexApproximation (f z) n))))
    (negate-magnitude-bound _ _ imaginaryError)

certifiedEvaluationDiskName :
  {f : ComplexRegularMap} (evaluator : CertifiedComplexEvaluator f) →
  (z : ComplexRegular) → CertifiedDiskName (f z)
certifiedEvaluationDiskName evaluator z .diskAt =
  certifiedEvaluationDisk evaluator z
certifiedEvaluationDiskName evaluator z .containsAt =
  certified-evaluation-disk-contains evaluator z
certifiedEvaluationDiskName evaluator z .radius≤precision n =
  isRefl≤ (precision n)

record ComplexEvaluationExclusion
  {f : ComplexRegularMap} (evaluator : CertifiedComplexEvaluator f)
  (z : ComplexRegular) (n : ℕ) : Type where
  field
    coordinate :
      (precision n < rationalRealPart
        (certifiedEvaluationCenter evaluator z n)) ⊎
      ((rationalRealPart (certifiedEvaluationCenter evaluator z n) <
        Q.- precision n) ⊎
      ((precision n < rationalImaginaryPart
        (certifiedEvaluationCenter evaluator z n)) ⊎
      (rationalImaginaryPart (certifiedEvaluationCenter evaluator z n) <
        Q.- precision n)))
open ComplexEvaluationExclusion public
