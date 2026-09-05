{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module ExactComplexZeroExclusion where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; suc; max)
import Cubical.Data.Nat.Order as ℕOrder
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Data.Sum
import Cubical.Data.Sum as Sum
open import Cubical.Data.Sigma
open import Cubical.Data.Empty
open import Cubical.HITs.PropositionalTruncation as PT
open import Cubical.HITs.SetQuotients as SQ using ([_])
open import Cubical.HITs.SetQuotients.Properties as SQP
open import Cubical.Relation.Nullary
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyAddition
open import CauchyProductBounds
open import CauchyProductErrorBounds
open import CauchyProductCongruence
open import CauchyProductRegularity
open import CauchyShift
open import ConstructiveComplexCompletion
open import ComplexCauchyApproximation
open import CertifiedComplexEvaluation

completion-path-gives-metric : (x y : RegularCauchy) →
  SQ.[ x ] ≡ SQ.[ y ] → x ≈metric y
completion-path-gives-metric x y =
  SQP.effective (λ a b → ≈metric-isProp a b) ≈metric-isEquivRel x y

complex-class-zero-gives-coordinate-metric : (z : ComplexRegular) →
  complexRegularClass z ≡ zeroComplex →
  (fst z ≈metric constantCauchy 0) ×
  (snd z ≈metric constantCauchy 0)
complex-class-zero-gives-coordinate-metric z path =
  completion-path-gives-metric (fst z) (constantCauchy 0)
    (cong fst path) ,
  completion-path-gives-metric (snd z) (constantCauchy 0)
    (cong snd path)

module ExactZeroOrderPaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; -_ to -S_)

  reverse-left : (center precision : fst R) →
    ((-S center) +S precision) +S center ≡ precision
  reverse-left center precision = solve! R

  reverse-right : (center precision : fst R) →
    ((-S center) +S precision) +S (-S precision) ≡ -S center
  reverse-right center precision = solve! R

  negated-error : (center output : fst R) →
    (-S center) +S (-S (-S output)) ≡
      -S (center +S (-S output))
  negated-error center output = solve! R

  subtract-zero : (value : fst R) → value +S (-S 0r) ≡ value
  subtract-zero value = solve! R

negative-reverses-< : (center precision : Q.ℚ) →
  center < Q.- precision → precision < Q.- center
negative-reverses-< center precision center<negativePrecision =
  subst2 _<_
    (ExactZeroOrderPaths.reverse-left PreferredℚCommRing center precision)
    (ExactZeroOrderPaths.reverse-right PreferredℚCommRing center precision)
    (<-o+ center (Q.- precision) ((Q.- center) Q.+ precision)
      center<negativePrecision)

record CertifiedExactZeroExclusion
  {f : ComplexRegularMap} (evaluator : CertifiedComplexEvaluator f)
  (z : ComplexRegular) : Type where
  field
    precisionIndex : ℕ
    separationThreshold : ℕ
    precisionSuccessor≤threshold :
      ℕOrder._≤_ (suc precisionIndex) separationThreshold
    separatedCoordinate : (n : ℕ) →
      ℕOrder._≤_ separationThreshold n →
      (precision precisionIndex < rationalRealPart
        (certifiedEvaluationCenter evaluator z n)) ⊎
      ((rationalRealPart (certifiedEvaluationCenter evaluator z n) <
          Q.- precision precisionIndex) ⊎
      ((precision precisionIndex < rationalImaginaryPart
        (certifiedEvaluationCenter evaluator z n)) ⊎
      (rationalImaginaryPart (certifiedEvaluationCenter evaluator z n) <
          Q.- precision precisionIndex)))
open CertifiedExactZeroExclusion public

positive-center-contradiction :
  (center output : Q.ℚ) (k n : ℕ) →
  ℕOrder._≤_ (suc k) n →
  MagnitudeBound (center Q.+ (Q.- output)) (precision n) →
  output ≤ precision (suc k) →
  precision k < center → ⊥
positive-center-contradiction center output k n sk≤n error output≤half
  precision<Center =
  let center≤output+error =
        single-difference-bound→directed center output (precision n)
          (positive-upper error)
      error≤half = precision-antitone (suc k) n sk≤n
      center≤doubleHalf = isTrans≤ center (output Q.+ precision n)
        (precision (suc k) Q.+ precision (suc k)) center≤output+error
        (≤Monotone+ output (precision (suc k)) (precision n)
          (precision (suc k)) output≤half error≤half)
      center≤precision = subst (center ≤_)
        (precision-refines-double k) center≤doubleHalf
  in isIrrefl< (precision k)
    (isTrans<≤ (precision k) center (precision k)
      precision<Center center≤precision)

negative-center-contradiction :
  (center output : Q.ℚ) (k n : ℕ) →
  ℕOrder._≤_ (suc k) n →
  MagnitudeBound (center Q.+ (Q.- output)) (precision n) →
  Q.- output ≤ precision (suc k) →
  center < Q.- precision k → ⊥
negative-center-contradiction center output k n sk≤n error negOutput≤half
  center<negativePrecision =
  positive-center-contradiction (Q.- center) (Q.- output) k n sk≤n
    (transport-magnitude _ _ _
      (ExactZeroOrderPaths.negated-error PreferredℚCommRing center output)
      (negate-magnitude-bound _ _ error))
    negOutput≤half
    (negative-reverses-< center (precision k)
      center<negativePrecision)

certified-exact-zero-exclusion-sound :
  {f : ComplexRegularMap} (evaluator : CertifiedComplexEvaluator f) →
  (z : ComplexRegular) → CertifiedExactZeroExclusion evaluator z →
  ¬ (complexRegularClass (f z) ≡ zeroComplex)
certified-exact-zero-exclusion-sound {f = f} evaluator z exclusion zeroPath =
  let k = precisionIndex exclusion
      separationN = separationThreshold exclusion
      metric = complex-class-zero-gives-coordinate-metric (f z) zeroPath
  in
  PT.rec isProp⊥
    (λ { (realN , realBounds) →
      PT.rec isProp⊥
        (λ { (imaginaryN , imaginaryBounds) →
          let n = ℕ.max (ℕ.max realN imaginaryN) separationN
              realN≤inner : ℕOrder._≤_ realN (ℕ.max realN imaginaryN)
              realN≤inner = ℕOrder.left-≤-max
              imaginaryN≤inner :
                ℕOrder._≤_ imaginaryN (ℕ.max realN imaginaryN)
              imaginaryN≤inner = ℕOrder.right-≤-max
              inner≤n : ℕOrder._≤_ (ℕ.max realN imaginaryN) n
              inner≤n = ℕOrder.left-≤-max
              realN≤n : ℕOrder._≤_ realN n
              realN≤n = ℕOrder.≤-trans realN≤inner inner≤n
              imaginaryN≤n : ℕOrder._≤_ imaginaryN n
              imaginaryN≤n = ℕOrder.≤-trans imaginaryN≤inner inner≤n
              separationN≤n : ℕOrder._≤_ separationN n
              separationN≤n = ℕOrder.right-≤-max
              sk≤n = ℕOrder.≤-trans
                (precisionSuccessor≤threshold exclusion) separationN≤n
              realMetricBounds = realBounds n realN≤n
              imaginaryMetricBounds = imaginaryBounds n imaginaryN≤n
              realOutput = rationalRealPart (complexApproximation (f z) n)
              imaginaryOutput = rationalImaginaryPart (complexApproximation (f z) n)
              realOutputMagnitude = transport-magnitude _ _ (precision (suc k))
                (sym (ExactZeroOrderPaths.subtract-zero
                  PreferredℚCommRing realOutput))
                (difference-magnitude-bound realOutput 0 (precision (suc k))
                  (fst realMetricBounds) (snd realMetricBounds))
              imaginaryOutputMagnitude = transport-magnitude _ _ (precision (suc k))
                (sym (ExactZeroOrderPaths.subtract-zero
                  PreferredℚCommRing imaginaryOutput))
                (difference-magnitude-bound imaginaryOutput 0 (precision (suc k))
                  (fst imaginaryMetricBounds) (snd imaginaryMetricBounds))
              realError = evaluation-real-error evaluator z n
              imaginaryError = evaluation-imaginary-error evaluator z n
          in
          Sum.rec
            (λ positiveReal → positive-center-contradiction
              (rationalRealPart (certifiedEvaluationCenter evaluator z n))
              realOutput k n sk≤n realError
              (positive-upper realOutputMagnitude) positiveReal)
            (Sum.rec
              (λ negativeReal → negative-center-contradiction
                (rationalRealPart (certifiedEvaluationCenter evaluator z n))
                realOutput k n sk≤n realError
                (negative-upper realOutputMagnitude) negativeReal)
              (Sum.rec
                (λ positiveImaginary → positive-center-contradiction
                  (rationalImaginaryPart
                    (certifiedEvaluationCenter evaluator z n))
                  imaginaryOutput k n sk≤n imaginaryError
                  (positive-upper imaginaryOutputMagnitude) positiveImaginary)
                (λ negativeImaginary → negative-center-contradiction
                  (rationalImaginaryPart
                    (certifiedEvaluationCenter evaluator z n))
                  imaginaryOutput k n sk≤n imaginaryError
                  (negative-upper imaginaryOutputMagnitude) negativeImaginary)))
            (separatedCoordinate exclusion n separationN≤n) })
        (snd metric (suc k)) })
    (fst metric (suc k))
