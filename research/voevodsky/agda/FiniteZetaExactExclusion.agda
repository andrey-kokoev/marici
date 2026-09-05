{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module FiniteZetaExactExclusion where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; zero; suc)
import Cubical.Data.Nat.Order as ℕOrder
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
import Cubical.Data.Int.Order as ℤOrder
open import Cubical.Data.Sum
open import Cubical.Relation.Nullary
open import RationalAnalyticSubstrate
open import RegularCauchyStructure
open import ConstructiveComplexCompletion
open import CauchyProductBounds
open import ComplexCauchyApproximation
open import CertifiedComplexEvaluation
open import ExactComplexZeroExclusion
open import RationalDirichletZeta

finiteZetaRegularMap : ℕ → ℕ → ComplexRegularMap
finiteZetaRegularMap exponent cutoff z =
  constantCauchy (rationalZetaPartialSum exponent cutoff) ,
  constantCauchy 0

finiteZetaRationalEvaluator : ℕ → ℕ → RationalComplex → ℕ → RationalComplex
finiteZetaRationalEvaluator exponent cutoff input precisionIndex =
  rationalComplex (rationalZetaPartialSum exponent cutoff) 0

finite-zeta-evaluation-real-error :
  (exponent cutoff : ℕ) (z : ComplexRegular) (n : ℕ) →
  MagnitudeBound
    (rationalRealPart
      (finiteZetaRationalEvaluator exponent cutoff
        (complexApproximation z 0) n) Q.+
     (Q.- rationalRealPart
       (complexApproximation (finiteZetaRegularMap exponent cutoff z) n)))
    (precision n)
finite-zeta-evaluation-real-error exponent cutoff z n =
  transport-magnitude _ 0 (precision n)
    (Q.+InvR (rationalZetaPartialSum exponent cutoff))
    (zero-magnitude-at-nonnegative-radius
      (precision n) (precision-nonnegative n))

finite-zeta-evaluation-imaginary-error :
  (exponent cutoff : ℕ) (z : ComplexRegular) (n : ℕ) →
  MagnitudeBound
    (rationalImaginaryPart
      (finiteZetaRationalEvaluator exponent cutoff
        (complexApproximation z 0) n) Q.+
     (Q.- rationalImaginaryPart
       (complexApproximation (finiteZetaRegularMap exponent cutoff z) n)))
    (precision n)
finite-zeta-evaluation-imaginary-error exponent cutoff z n =
  transport-magnitude _ 0 (precision n) (Q.+InvR 0)
    (zero-magnitude-at-nonnegative-radius
      (precision n) (precision-nonnegative n))

finiteZetaCertifiedEvaluator : (exponent cutoff : ℕ) →
  CertifiedComplexEvaluator (finiteZetaRegularMap exponent cutoff)
finiteZetaCertifiedEvaluator exponent cutoff .inputDepth n = 0
finiteZetaCertifiedEvaluator exponent cutoff .evaluate =
  finiteZetaRationalEvaluator exponent cutoff
finiteZetaCertifiedEvaluator exponent cutoff .evaluation-real-error =
  finite-zeta-evaluation-real-error exponent cutoff
finiteZetaCertifiedEvaluator exponent cutoff .evaluation-imaginary-error =
  finite-zeta-evaluation-imaginary-error exponent cutoff

one-half<one : one-half < 1
one-half<one = ℤOrder.isRefl≤

finite-zeta-center-separated : (exponent cutoff n : ℕ) →
  precision (suc zero) < rationalRealPart
    (certifiedEvaluationCenter
      (finiteZetaCertifiedEvaluator exponent cutoff)
      (embedRationalComplexRegular zeroRationalComplex) n)
finite-zeta-center-separated exponent cutoff n =
  isTrans<≤ one-half 1 (rationalZetaPartialSum exponent cutoff)
    one-half<one (rational-zeta-partial-sum-at-least-one exponent cutoff)

finiteZetaExactZeroExclusion : (exponent cutoff : ℕ) →
  CertifiedExactZeroExclusion
    (finiteZetaCertifiedEvaluator exponent cutoff)
    (embedRationalComplexRegular zeroRationalComplex)
finiteZetaExactZeroExclusion exponent cutoff .precisionIndex = suc zero
finiteZetaExactZeroExclusion exponent cutoff .separationThreshold = suc (suc zero)
finiteZetaExactZeroExclusion exponent cutoff .precisionSuccessor≤threshold =
  ℕOrder.≤-refl
finiteZetaExactZeroExclusion exponent cutoff .separatedCoordinate n threshold≤n =
  inl (finite-zeta-center-separated exponent cutoff n)

finite-zeta-completion-value-nonzero : (exponent cutoff : ℕ) →
  ¬ (complexRegularClass
      (finiteZetaRegularMap exponent cutoff
        (embedRationalComplexRegular zeroRationalComplex)) ≡ zeroComplex)
finite-zeta-completion-value-nonzero exponent cutoff =
  certified-exact-zero-exclusion-sound
    (finiteZetaCertifiedEvaluator exponent cutoff)
    (embedRationalComplexRegular zeroRationalComplex)
    (finiteZetaExactZeroExclusion exponent cutoff)
