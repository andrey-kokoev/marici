{-# OPTIONS --safe --cubical --guardedness #-}
module TickRotationDefectTransport where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma using (_×_)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import CauchyMetricEquivalence
open import CauchyAdditionCongruence using (_+completion_)
open import CauchyNegation using (-completion_)
open import CauchyRationalEmbedding using (embedℚ-preserves-negation)
open import RegularCauchyStructure using (precision)
open import Cubical.Data.Nat using (ℕ)
import Cubical.Data.Int.Order as ZO
open import RationalAnalyticSubstrate using (one-half)
open import TickCayleyGridIncrement using (gridValue)
open import TickAtanGridSmallAngle using (doubledAtanIncrement)
open import TickAtanCayleyIncrement using (relativeParameter)
open import TickCayleyRelativeRotor using (relativeInverse)
import TickCayleyNormalizedBracket as Normalized
open import OperationalCosineMetric using (completionCosine)
open import OperationalSineMetric using (completionSine)
open import TickSmallAngleDensity using (completion-bound-weaken)
open import CauchyCompletionMultiplication using (preferredCompletionMultiplication)
open import CauchyCompletionCommRing
open import CauchyProductBounds
open import TickCompletionMagnitudeBounds
open import TickCompletionScalarBounds
open import TickCompletionProductMagnitude
open import TaylorTermBounds using (nonnegative-bound-product)
open import TickCayleyRotationalBracket using (nonnegative-sum)
open import TickAtanFirstOrderBounds using (one-magnitude)
open import RationalAnalyticSubstrate using (PreferredℚCommRing)

Rotor = MetricCompletionCandidate × MetricCompletionCandidate

infixl 7 _⊗_
_⊗_ : Rotor → Rotor → Rotor
(a , b) ⊗ (c , d) =
  (preferredCompletionMultiplication a c +completion (-completion (preferredCompletionMultiplication b d))) ,
  (preferredCompletionMultiplication a d +completion preferredCompletionMultiplication b c)

infixl 6 _⊖_
_⊖_ : Rotor → Rotor → Rotor
(a , b) ⊖ (c , d) = (a +completion (-completion c)) , (b +completion (-completion d))

RotorBound : Rotor → Q.ℚ → Type
RotorBound z B = CompletionMagnitudeBound (fst z) B × CompletionMagnitudeBound (snd z) B

module Algebra {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; _·_ to _·S_; -_ to -S_)
  negate-product : (a : fst R) → (-S 1r) ·S a ≡ -S a
  negate-product a = solve! R
  real-defect : (a b c d e f g h : fst R) →
    ((a ·S c +S (-S (b ·S d))) ·S g +S (-S ((a ·S d +S b ·S c) ·S h))) +S
      (-S ((a ·S e +S (-S (b ·S f))) ·S g +S (-S ((a ·S f +S b ·S e) ·S h)))) ≡
    ((a ·S (c +S (-S e)) +S (-S (b ·S (d +S (-S f))))) ·S g +S
      (-S ((a ·S (d +S (-S f)) +S b ·S (c +S (-S e))) ·S h)))
  real-defect a b c d e f g h = solve! R
  imaginary-defect : (a b c d e f g h : fst R) →
    ((a ·S c +S (-S (b ·S d))) ·S h +S ((a ·S d +S b ·S c) ·S g)) +S
      (-S ((a ·S e +S (-S (b ·S f))) ·S h +S ((a ·S f +S b ·S e) ·S g))) ≡
    ((a ·S (c +S (-S e)) +S (-S (b ·S (d +S (-S f))))) ·S h +S
      ((a ·S (d +S (-S f)) +S b ·S (c +S (-S e))) ·S g))
  imaginary-defect a b c d e f g h = solve! R
module C = Algebra CompletionCommRing

abstract
  completion-negation-bound : (a : MetricCompletionCandidate) (B : Q.ℚ) → 0 ≤ B →
    CompletionMagnitudeBound a B → CompletionMagnitudeBound (-completion a) B
  completion-negation-bound a B Bh ha = completion-bound-path
    (preferredCompletionMultiplication (embedMetricℚ (Q.- 1)) a) (-completion a) B
    (cong (λ z → preferredCompletionMultiplication z a) (sym (embedℚ-preserves-negation 1)) ∙ C.negate-product a)
    (subst (CompletionMagnitudeBound (preferredCompletionMultiplication (embedMetricℚ (Q.- 1)) a)) (Q.·IdL B)
      (completion-rational-multiplier-bound (Q.- 1) 1 a B
        (RegularCauchyStructure.precision-nonnegative 0) Bh (negate-magnitude-bound 1 1 one-magnitude) ha))

  rotor-product-bound : (u v : Rotor) (A B : Q.ℚ) → 0 ≤ A → 0 ≤ B →
    RotorBound u A → RotorBound v B → RotorBound (u ⊗ v) ((A Q.· B) Q.+ (A Q.· B))
  rotor-product-bound (a , b) (c , d) A B Ah Bh (ha , hb) (hc , hd) =
    completion-magnitude-add (preferredCompletionMultiplication a c) (-completion (preferredCompletionMultiplication b d))
      (A Q.· B) (A Q.· B) (completion-product-bound a c A B Ah Bh ha hc)
      (completion-negation-bound (preferredCompletionMultiplication b d) (A Q.· B)
        (nonnegative-bound-product A B Ah Bh) (completion-product-bound b d A B Ah Bh hb hd)) ,
    completion-magnitude-add (preferredCompletionMultiplication a d) (preferredCompletionMultiplication b c)
      (A Q.· B) (A Q.· B) (completion-product-bound a d A B Ah Bh ha hd) (completion-product-bound b c A B Ah Bh hb hc)

  factored-defect : (outer step reference right : Rotor) →
    ((outer ⊗ step) ⊗ right) ⊖ ((outer ⊗ reference) ⊗ right) ≡ (outer ⊗ (step ⊖ reference)) ⊗ right
  factored-defect (a , b) (c , d) (e , f) (g , h) =
    cong₂ _,_ (C.real-defect a b c d e f g h) (C.imaginary-defect a b c d e f g h)

transportBudget : Q.ℚ → Q.ℚ → Q.ℚ → Q.ℚ
transportBudget P Q B = (((P Q.· B) Q.+ (P Q.· B)) Q.· Q) Q.+ (((P Q.· B) Q.+ (P Q.· B)) Q.· Q)

abstract
  outer-rotation-transport : (outer step reference right : Rotor) (P Q B : Q.ℚ) →
    0 ≤ P → 0 ≤ Q → 0 ≤ B → RotorBound outer P → RotorBound right Q → RotorBound (step ⊖ reference) B →
    RotorBound (((outer ⊗ step) ⊗ right) ⊖ ((outer ⊗ reference) ⊗ right)) (transportBudget P Q B)
  outer-rotation-transport outer step reference right P Q B Ph Qh Bh ho hr hb =
    subst (λ z → RotorBound z (transportBudget P Q B)) (sym (factored-defect outer step reference right))
      (rotor-product-bound (outer ⊗ (step ⊖ reference)) right ((P Q.· B) Q.+ (P Q.· B)) Q
        (nonnegative-sum (P Q.· B) (P Q.· B) (nonnegative-bound-product P B Ph Bh) (nonnegative-bound-product P B Ph Bh)) Qh
        (rotor-product-bound outer (step ⊖ reference) P B Ph Bh ho hb) hr)

-- The inner bracket here is the actual operational rotation, not arbitrary
-- data supplied by the caller. Only the outer factor bounds remain inputs.
module Grid (n m d : ℕ) (e : Q.ℚ)
  (hx : MagnitudeBound (gridValue n d) one-half) (hy : MagnitudeBound (gridValue m d) one-half)
  (eh : 0 ≤ e) (small : e ≤ precision 6)
  (hd : MagnitudeBound (gridValue m d Q.+ (Q.- gridValue n d)) e) where
  module Local = Normalized.Grid n m d e hx hy eh small hd
  step : Rotor
  step = completionCosine (doubledAtanIncrement n m d hx hy) , completionSine (doubledAtanIncrement n m d hx hy)
  reference : Rotor
  reference =
    embedMetricℚ ((1 Q.+ (Q.- (relativeParameter n m d Q.· relativeParameter n m d))) Q.· relativeInverse n m d) ,
    embedMetricℚ ((relativeParameter n m d Q.+ relativeParameter n m d) Q.· relativeInverse n m d)

  bracket-bound : RotorBound (step ⊖ reference) (99 Q.· (e Q.· e))
  bracket-bound = completion-bound-weaken
    (completionCosine (doubledAtanIncrement n m d hx hy) +completion
      (-completion (embedMetricℚ ((1 Q.+ (Q.- (relativeParameter n m d Q.· relativeParameter n m d))) Q.· relativeInverse n m d))))
    (34 Q.· (e Q.· e)) (99 Q.· (e Q.· e))
    (≤-·o 34 99 (e Q.· e) (nonnegative-bound-product e e eh eh) (65 , refl))
    Local.uniform-real-bound , Local.uniform-imaginary-bound

  transported-grid-bracket : (outer right : Rotor) (P Q : Q.ℚ) →
    0 ≤ P → 0 ≤ Q → RotorBound outer P → RotorBound right Q →
    RotorBound (((outer ⊗ step) ⊗ right) ⊖ ((outer ⊗ reference) ⊗ right))
      (transportBudget P Q (99 Q.· (e Q.· e)))
  transported-grid-bracket outer right P Q Ph Qh ho hr = outer-rotation-transport outer step reference right
    P Q (99 Q.· (e Q.· e)) Ph Qh
    (nonnegative-bound-product 99 (e Q.· e) ZO.zero-≤pos (nonnegative-bound-product e e eh eh)) ho hr bracket-bound
