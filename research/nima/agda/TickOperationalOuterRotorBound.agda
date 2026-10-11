{-# OPTIONS --safe --cubical --guardedness #-}
module TickOperationalOuterRotorBound where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ; zero; suc)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
import Cubical.Data.Int.Order as ZO
open import RegularCauchyStructure using (precision; precision-nonnegative; precision-refines-double)
open import RationalAnalyticSubstrate using (one-half)
open import CauchyMetricEquivalence
open import CauchyProductBounds
open import CauchyAdditionCongruence using (_+completion_)
open import CauchyNegation using (-completion_)
open import CauchyRationalEmbedding using (embedℚ-preserves-negation; embedℚ-preserves-sum)
open import CauchyCompletionMultiplication using (preferredCompletionMultiplication)
open import CauchyCompletionCommRing
open import OperationalCosineMetric using (completionCosine)
open import OperationalSineMetric using (completionSine)
open import TickCompletionMagnitudeBounds
open import TickCompletionScalarBounds
open import TickCompletionTrigSmallAngle
open import TickSmallAngleDensity using (completion-bound-weaken)
open import TickAtanFirstOrderBounds using (one-magnitude)
open import TickRotationDefectTransport using (RotorBound; rotor-product-bound)
open import TickOperationalRotorIncrement using (rotation; rotation-addition; gridAngle)
open import TickAtanOuterAngleBound using (grid-angle-uniform-bound)
open import TickCayleyGridIncrement using (gridValue)
open import TickCayleyRotationalBracket using (nonnegative-sum)
open import TaylorTermBounds using (nonnegative-value-magnitude; nonnegative-bound-product)

module Algebra {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; _·_ to _·S_; -_ to -S_)
  restore : (a b : fst R) → (a +S (-S b)) +S b ≡ a
  restore a b = solve! R
  double-scalar : (q a : fst R) → (q ·S a) +S (q ·S a) ≡ (q +S q) ·S a
  double-scalar q a = solve! R
module C = Algebra CompletionCommRing

abstract
  small-rotation-bound : (a : MetricCompletionCandidate) → CompletionMagnitudeBound a (precision 2) → RotorBound (rotation a) 2
  small-rotation-bound a ha = completion-bound-weaken (completionCosine a) ((precision 2 Q.· precision 2) Q.+ 1) 2 (15 , refl)
    (completion-bound-path (cosineRemainder a +completion embedMetricℚ 1) (completionCosine a) ((precision 2 Q.· precision 2) Q.+ 1)
      (cong (_+completion embedMetricℚ 1) (cosine-remainder-definition a)
        ∙ cong (λ z → (completionCosine a +completion z) +completion embedMetricℚ 1) (sym (embedℚ-preserves-negation 1))
        ∙ C.restore (completionCosine a) (embedMetricℚ 1))
      (completion-magnitude-add (cosineRemainder a) (embedMetricℚ 1) (precision 2 Q.· precision 2) 1
        (completion-cosine-small-remainder a (precision 2) (precision-nonnegative 2) (isRefl≤ (precision 2)) ha)
        (embedded-magnitude-bound 1 1 one-magnitude))) ,
    completion-bound-weaken (completionSine a) ((precision 2 Q.· precision 2) Q.+ precision 2) 2 (108 , refl)
      (completion-bound-path (sineRemainder a +completion a) (completionSine a) ((precision 2 Q.· precision 2) Q.+ precision 2)
        (cong (_+completion a) (sine-remainder-definition a) ∙ C.restore (completionSine a) a)
        (completion-magnitude-add (sineRemainder a) a (precision 2 Q.· precision 2) (precision 2)
          (completion-sine-small-remainder a (precision 2) (precision-nonnegative 2) (isRefl≤ (precision 2)) ha) ha))

double : MetricCompletionCandidate → MetricCompletionCandidate
double a = a +completion a
iterateDouble : ℕ → MetricCompletionCandidate → MetricCompletionCandidate
iterateDouble zero a = a
iterateDouble (suc n) a = double (iterateDouble n a)
iterateRationalDouble : ℕ → Q.ℚ → Q.ℚ
iterateRationalDouble zero q = q
iterateRationalDouble (suc n) q = iterateRationalDouble n q Q.+ iterateRationalDouble n q
rotorRadius : ℕ → Q.ℚ
rotorRadius zero = 2
rotorRadius (suc n) = (rotorRadius n Q.· rotorRadius n) Q.+ (rotorRadius n Q.· rotorRadius n)

abstract
  rotor-radius-nonnegative : (n : ℕ) → 0 ≤ rotorRadius n
  rotor-radius-nonnegative zero = ZO.zero-≤pos
  rotor-radius-nonnegative (suc n) = nonnegative-sum (rotorRadius n Q.· rotorRadius n) (rotorRadius n Q.· rotorRadius n)
    (nonnegative-bound-product (rotorRadius n) (rotorRadius n) (rotor-radius-nonnegative n) (rotor-radius-nonnegative n))
    (nonnegative-bound-product (rotorRadius n) (rotorRadius n) (rotor-radius-nonnegative n) (rotor-radius-nonnegative n))

  iterated-rotation-bound : (n : ℕ) (a : MetricCompletionCandidate) → RotorBound (rotation a) 2 →
    RotorBound (rotation (iterateDouble n a)) (rotorRadius n)
  iterated-rotation-bound zero a h = h
  iterated-rotation-bound (suc n) a h = subst (λ z → RotorBound z (rotorRadius (suc n)))
    (sym (rotation-addition (iterateDouble n a) (iterateDouble n a)))
    (rotor-product-bound (rotation (iterateDouble n a)) (rotation (iterateDouble n a)) (rotorRadius n) (rotorRadius n)
      (rotor-radius-nonnegative n) (rotor-radius-nonnegative n) (iterated-rotation-bound n a h) (iterated-rotation-bound n a h))

  iterated-scalar-path : (n : ℕ) (q : Q.ℚ) (a : MetricCompletionCandidate) →
    iterateDouble n (preferredCompletionMultiplication (embedMetricℚ q) a) ≡ preferredCompletionMultiplication (embedMetricℚ (iterateRationalDouble n q)) a
  iterated-scalar-path zero q a = refl
  iterated-scalar-path (suc n) q a = cong double (iterated-scalar-path n q a)
    ∙ C.double-scalar (embedMetricℚ (iterateRationalDouble n q)) a
    ∙ cong (λ z → preferredCompletionMultiplication z a) (sym (embedℚ-preserves-sum (iterateRationalDouble n q) (iterateRationalDouble n q)))

  four-doubles-restore : (a : MetricCompletionCandidate) → iterateDouble 4 (preferredCompletionMultiplication (embedMetricℚ (precision 4)) a) ≡ a
  four-doubles-restore a = cong (iterateDouble 3) (step 3)
    ∙ cong (iterateDouble 2) (step 2) ∙ cong double (step 1) ∙ step 0
    ∙ CommRingStr.·IdL (snd CompletionCommRing) a
    where
    step : (n : ℕ) → double (preferredCompletionMultiplication (embedMetricℚ (precision (suc n))) a) ≡
      preferredCompletionMultiplication (embedMetricℚ (precision n)) a
    step n = C.double-scalar (embedMetricℚ (precision (suc n))) a
      ∙ cong (λ z → preferredCompletionMultiplication z a)
        (sym (embedℚ-preserves-sum (precision (suc n)) (precision (suc n))) ∙ cong embedMetricℚ (precision-refines-double n))

  radius-four-rotation-bound : (a : MetricCompletionCandidate) → CompletionMagnitudeBound a 4 → RotorBound (rotation a) (rotorRadius 4)
  radius-four-rotation-bound a ha = subst (λ z → RotorBound (rotation z) (rotorRadius 4)) (four-doubles-restore a)
    (iterated-rotation-bound 4 (preferredCompletionMultiplication (embedMetricℚ (precision 4)) a)
      (small-rotation-bound (preferredCompletionMultiplication (embedMetricℚ (precision 4)) a)
        (subst (CompletionMagnitudeBound (preferredCompletionMultiplication (embedMetricℚ (precision 4)) a)) (Q.eq/ _ _ refl)
          (completion-rational-multiplier-bound (precision 4) (precision 4) a 4 (precision-nonnegative 4) ZO.zero-≤pos
            (nonnegative-value-magnitude (precision 4) (precision 4) (precision-nonnegative 4) (isRefl≤ (precision 4)) (precision-nonnegative 4)) ha))))

  grid-outer-rotation-bound : (n d : ℕ) (h : MagnitudeBound (gridValue n d) one-half) →
    RotorBound (rotation (gridAngle n d h)) (rotorRadius 4)
  grid-outer-rotation-bound n d h = radius-four-rotation-bound (gridAngle n d h) (grid-angle-uniform-bound n d h)
