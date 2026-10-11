{-# OPTIONS --safe --cubical --guardedness #-}
module TickCayleyRotationalBracket where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate using (PreferredℚCommRing; one-half)
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyProductBounds
open import CauchyRationalEmbedding
open import CauchyAdditionCongruence using (_+completion_)
open import CauchyNegation using (-completion_)
open import CauchyCompletionMultiplication using (preferredCompletionMultiplication)
open import CauchyCompletionCommRing
open import OperationalCosineMetric using (completionCosine)
open import OperationalSineMetric using (completionSine)
open import TaylorTermBounds using (nonnegative-bound-product)
open import TickCompletionMagnitudeBounds
open import TickCompletionScalarBounds
open import TickCompletionTrigSmallAngle
open import TickAtanCompletionFirstOrder using (atanIncrement)
open import TickAtanCayleyIncrement using (relativeParameter; relativeBudget; relative-atan-grid-bound)
open import TickAtanGridSmallAngle using (fourStep; doubledAtanIncrement; doubled-atan-grid-bound; four-step-small; relative-parameter-bound)
open import TickCayleyGridIncrement using (gridValue)
open import TickCayleyGridSlope using (rational-product-equation)
open import TickAtanFirstOrderBounds using (one-magnitude; scale-nonnegative)

module Algebra {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; _·_ to _·S_; -_ to -S_)
  real-split : (u D B K : fst R) → D ·S u +S (-S B) ≡ D ·S (u +S K) +S ((-S (D ·S K)) +S (-S B))
  real-split u D B K = solve! R
  imaginary-split : (u a D B : fst R) → D ·S u +S (-S B) ≡
    (D ·S (u +S (-S a)) +S D ·S (a +S (-S B))) +S ((D ·S B) +S (-S B))
  imaginary-split u a D B = solve! R
  double-difference : (a b : fst R) → (a +S (-S b)) +S (a +S (-S b)) ≡ (a +S a) +S (-S (b +S b))
  double-difference a b = solve! R
  real-correction : (t : fst R) → (-S ((1r +S t ·S t) ·S (-S 1r))) +S (-S (1r +S (-S (t ·S t)))) ≡ (t ·S t) +S (t ·S t)
  real-correction t = solve! R
  imaginary-correction : (t : fst R) → ((1r +S t ·S t) ·S (t +S t)) +S (-S (t +S t)) ≡ (t +S t) ·S (t ·S t)
  imaginary-correction t = solve! R
module C = Algebra CompletionCommRing
module R = Algebra PreferredℚCommRing

abstract
  grid-clock-input : (n m d : ℕ) (e : Q.ℚ)
    (hx : MagnitudeBound (gridValue n d) one-half) (hy : MagnitudeBound (gridValue m d) one-half) →
    0 ≤ e → MagnitudeBound (gridValue m d Q.+ (Q.- gridValue n d)) e →
    CompletionMagnitudeBound (atanIncrement (gridValue n d) (gridValue m d) hx hy +completion
      (-completion (embedMetricℚ (relativeParameter n m d)))) (relativeBudget e)
  grid-clock-input = relative-atan-grid-bound

  grid-angle-input : (n m d : ℕ) (e : Q.ℚ)
    (hx : MagnitudeBound (gridValue n d) one-half) (hy : MagnitudeBound (gridValue m d) one-half) →
    0 ≤ e → e ≤ precision 6 → MagnitudeBound (gridValue m d Q.+ (Q.- gridValue n d)) e →
    CompletionMagnitudeBound (doubledAtanIncrement n m d hx hy) (fourStep e)
  grid-angle-input = doubled-atan-grid-bound

  grid-parameter-input : (n m d : ℕ) (e : Q.ℚ) → 0 ≤ e →
    MagnitudeBound (gridValue m d Q.+ (Q.- gridValue n d)) e → MagnitudeBound (relativeParameter n m d) e
  grid-parameter-input = relative-parameter-bound

  real-clearing-path : (u r : MetricCompletionCandidate) (d b k : Q.ℚ) → r ≡ u +completion embedMetricℚ k →
    preferredCompletionMultiplication (embedMetricℚ d) u +completion (-completion (embedMetricℚ b)) ≡
    preferredCompletionMultiplication (embedMetricℚ d) r +completion embedMetricℚ ((Q.- (d Q.· k)) Q.+ (Q.- b))
  real-clearing-path u r d b k definition = C.real-split u (embedMetricℚ d) (embedMetricℚ b) (embedMetricℚ k)
    ∙ cong₂ _+completion_
      (cong (preferredCompletionMultiplication (embedMetricℚ d)) (sym definition))
      (cong₂ _+completion_
        (cong -completion_ (rational-product-equation d k (d Q.· k) refl) ∙ embedℚ-preserves-negation (d Q.· k))
        (embedℚ-preserves-negation b)
        ∙ sym (embedℚ-preserves-sum (Q.- (d Q.· k)) (Q.- b)))

  imaginary-clearing-path : (u a r : MetricCompletionCandidate) (d b : Q.ℚ) → r ≡ u +completion (-completion a) →
    preferredCompletionMultiplication (embedMetricℚ d) u +completion (-completion (embedMetricℚ b)) ≡
    (preferredCompletionMultiplication (embedMetricℚ d) r +completion
      preferredCompletionMultiplication (embedMetricℚ d) (a +completion (-completion (embedMetricℚ b))))
      +completion embedMetricℚ ((d Q.· b) Q.+ (Q.- b))
  imaginary-clearing-path u a r d b definition = C.imaginary-split u a (embedMetricℚ d) (embedMetricℚ b)
    ∙ cong₂ _+completion_
      (cong (λ z → preferredCompletionMultiplication (embedMetricℚ d) z +completion
        preferredCompletionMultiplication (embedMetricℚ d) (a +completion (-completion (embedMetricℚ b)))) (sym definition))
      (cong₂ _+completion_ (rational-product-equation d b (d Q.· b) refl) (embedℚ-preserves-negation b)
        ∙ sym (embedℚ-preserves-sum (d Q.· b) (Q.- b)))

  doubled-clock-bound : (a : MetricCompletionCandidate) (t B : Q.ℚ) →
    CompletionMagnitudeBound (a +completion (-completion (embedMetricℚ t))) B →
    CompletionMagnitudeBound ((a +completion a) +completion (-completion (embedMetricℚ (t Q.+ t)))) (B Q.+ B)
  doubled-clock-bound a t B bound = completion-bound-path
    ((a +completion (-completion (embedMetricℚ t))) +completion (a +completion (-completion (embedMetricℚ t))))
    ((a +completion a) +completion (-completion (embedMetricℚ (t Q.+ t)))) (B Q.+ B)
    (C.double-difference a (embedMetricℚ t)
      ∙ cong (λ b → (a +completion a) +completion (-completion b)) (sym (embedℚ-preserves-sum t t)))
    (completion-magnitude-add (a +completion (-completion (embedMetricℚ t)))
      (a +completion (-completion (embedMetricℚ t))) B B bound bound)

realBracket imaginaryBracket : MetricCompletionCandidate → Q.ℚ → MetricCompletionCandidate
realBracket a t = preferredCompletionMultiplication (embedMetricℚ (1 Q.+ t Q.· t)) (cosineRemainder a)
  +completion embedMetricℚ ((t Q.· t) Q.+ (t Q.· t))
imaginaryBracket a t =
  (preferredCompletionMultiplication (embedMetricℚ (1 Q.+ t Q.· t)) (sineRemainder a) +completion
    preferredCompletionMultiplication (embedMetricℚ (1 Q.+ t Q.· t)) (a +completion (-completion (embedMetricℚ (t Q.+ t)))))
  +completion embedMetricℚ ((t Q.+ t) Q.· (t Q.· t))

-- Public paths to the actual denominator-cleared rotation-versus-Cayley
-- differences. The bound below is on these expressions, not a new backend.
real-bracket-definition : (a : MetricCompletionCandidate) (t : Q.ℚ) →
  preferredCompletionMultiplication (embedMetricℚ (1 Q.+ t Q.· t)) (completionCosine a)
    +completion (-completion (embedMetricℚ (1 Q.+ (Q.- (t Q.· t))))) ≡ realBracket a t
real-bracket-definition a t = real-clearing-path (completionCosine a) (cosineRemainder a)
  (1 Q.+ t Q.· t) (1 Q.+ (Q.- (t Q.· t))) (Q.- 1) (cosine-remainder-definition a)
  ∙ cong (λ q → preferredCompletionMultiplication (embedMetricℚ (1 Q.+ t Q.· t)) (cosineRemainder a)
    +completion embedMetricℚ q) (R.real-correction t)

imaginary-bracket-definition : (a : MetricCompletionCandidate) (t : Q.ℚ) →
  preferredCompletionMultiplication (embedMetricℚ (1 Q.+ t Q.· t)) (completionSine a)
    +completion (-completion (embedMetricℚ (t Q.+ t))) ≡ imaginaryBracket a t
imaginary-bracket-definition a t = imaginary-clearing-path (completionSine a) a (sineRemainder a)
  (1 Q.+ t Q.· t) (t Q.+ t) (sine-remainder-definition a)
  ∙ cong (λ q → (preferredCompletionMultiplication (embedMetricℚ (1 Q.+ t Q.· t)) (sineRemainder a)
      +completion preferredCompletionMultiplication (embedMetricℚ (1 Q.+ t Q.· t))
        (a +completion (-completion (embedMetricℚ (t Q.+ t))))) +completion embedMetricℚ q)
    (R.imaginary-correction t)

nonnegative-sum : (a b : Q.ℚ) → 0 ≤ a → 0 ≤ b → 0 ≤ a Q.+ b
nonnegative-sum a b ha hb = subst (_≤ a Q.+ b) (Q.+IdL 0) (≤Monotone+ 0 a 0 b ha hb)

module BoundAt (a : MetricCompletionCandidate) (t E e B : Q.ℚ)
  (Eh : 0 ≤ E) (eh : 0 ≤ e) (Bh : 0 ≤ B) (small : E ≤ precision 2)
  (angle : CompletionMagnitudeBound a E) (ht : MagnitudeBound t e)
  (clock : CompletionMagnitudeBound (a +completion (-completion (embedMetricℚ (t Q.+ t)))) B) where
  D = 1 Q.+ t Q.· t
  Dbound = 1 Q.+ e Q.· e
  e²h = nonnegative-bound-product e e eh eh
  E²h = nonnegative-bound-product E E Eh Eh
  Dh = nonnegative-sum 1 (e Q.· e) (precision-nonnegative 0) e²h
  denominator-bound : MagnitudeBound D Dbound
  denominator-bound = add-magnitude-bounds 1 1 (t Q.· t) (e Q.· e) one-magnitude
    (arbitrary-multiplier-bound t e t e eh eh ht ht)

  real-bound : CompletionMagnitudeBound (realBracket a t) ((Dbound Q.· (E Q.· E)) Q.+ ((e Q.· e) Q.+ (e Q.· e)))
  real-bound = completion-magnitude-add
    (preferredCompletionMultiplication (embedMetricℚ D) (cosineRemainder a))
    (embedMetricℚ ((t Q.· t) Q.+ (t Q.· t))) (Dbound Q.· (E Q.· E)) ((e Q.· e) Q.+ (e Q.· e))
    (completion-rational-multiplier-bound D Dbound (cosineRemainder a) (E Q.· E) Dh E²h denominator-bound
      (completion-cosine-small-remainder a E Eh small angle))
    (embedded-magnitude-bound ((t Q.· t) Q.+ (t Q.· t)) ((e Q.· e) Q.+ (e Q.· e))
      (add-magnitude-bounds (t Q.· t) (e Q.· e) (t Q.· t) (e Q.· e)
        (arbitrary-multiplier-bound t e t e eh eh ht ht) (arbitrary-multiplier-bound t e t e eh eh ht ht)))

  imaginary-bound : CompletionMagnitudeBound (imaginaryBracket a t)
    (((Dbound Q.· (E Q.· E)) Q.+ Dbound Q.· B) Q.+ ((e Q.+ e) Q.· (e Q.· e)))
  imaginary-bound = completion-magnitude-add
    (preferredCompletionMultiplication (embedMetricℚ D) (sineRemainder a) +completion
      preferredCompletionMultiplication (embedMetricℚ D) (a +completion (-completion (embedMetricℚ (t Q.+ t)))))
    (embedMetricℚ ((t Q.+ t) Q.· (t Q.· t)))
    ((Dbound Q.· (E Q.· E)) Q.+ Dbound Q.· B) ((e Q.+ e) Q.· (e Q.· e))
    (completion-magnitude-add
      (preferredCompletionMultiplication (embedMetricℚ D) (sineRemainder a))
      (preferredCompletionMultiplication (embedMetricℚ D) (a +completion (-completion (embedMetricℚ (t Q.+ t)))))
      (Dbound Q.· (E Q.· E)) (Dbound Q.· B)
      (completion-rational-multiplier-bound D Dbound (sineRemainder a) (E Q.· E) Dh E²h denominator-bound
        (completion-sine-small-remainder a E Eh small angle))
      (completion-rational-multiplier-bound D Dbound (a +completion (-completion (embedMetricℚ (t Q.+ t)))) B
        Dh Bh denominator-bound clock))
    (embedded-magnitude-bound ((t Q.+ t) Q.· (t Q.· t)) ((e Q.+ e) Q.· (e Q.· e))
      (arbitrary-multiplier-bound (t Q.+ t) (e Q.+ e) (t Q.· t) (e Q.· e)
        (nonnegative-sum e e eh eh) e²h (add-magnitude-bounds t e t e ht ht)
        (arbitrary-multiplier-bound t e t e eh eh ht ht)))

abstract
  real-bracket-bound : (a : MetricCompletionCandidate) (t E e B : Q.ℚ) →
    0 ≤ E → 0 ≤ e → 0 ≤ B → E ≤ precision 2 → CompletionMagnitudeBound a E → MagnitudeBound t e →
    CompletionMagnitudeBound (a +completion (-completion (embedMetricℚ (t Q.+ t)))) B →
    CompletionMagnitudeBound (realBracket a t)
      (((1 Q.+ e Q.· e) Q.· (E Q.· E)) Q.+ ((e Q.· e) Q.+ (e Q.· e)))
  real-bracket-bound = BoundAt.real-bound

  imaginary-bracket-bound : (a : MetricCompletionCandidate) (t E e B : Q.ℚ) →
    0 ≤ E → 0 ≤ e → 0 ≤ B → E ≤ precision 2 → CompletionMagnitudeBound a E → MagnitudeBound t e →
    CompletionMagnitudeBound (a +completion (-completion (embedMetricℚ (t Q.+ t)))) B →
    CompletionMagnitudeBound (imaginaryBracket a t)
      ((((1 Q.+ e Q.· e) Q.· (E Q.· E)) Q.+ (1 Q.+ e Q.· e) Q.· B) Q.+ ((e Q.+ e) Q.· (e Q.· e)))
  imaginary-bracket-bound = BoundAt.imaginary-bound

realGridBudget imaginaryGridBudget : Q.ℚ → Q.ℚ
realGridBudget e = ((1 Q.+ e Q.· e) Q.· (fourStep e Q.· fourStep e)) Q.+ ((e Q.· e) Q.+ (e Q.· e))
imaginaryGridBudget e = (((1 Q.+ e Q.· e) Q.· (fourStep e Q.· fourStep e)) Q.+
  (1 Q.+ e Q.· e) Q.· (relativeBudget e Q.+ relativeBudget e)) Q.+ ((e Q.+ e) Q.· (e Q.· e))

module Grid (n m d : ℕ) (e : Q.ℚ)
  (hx : MagnitudeBound (gridValue n d) one-half) (hy : MagnitudeBound (gridValue m d) one-half)
  (eh : 0 ≤ e) (small : e ≤ precision 6) (hd : MagnitudeBound (gridValue m d Q.+ (Q.- gridValue n d)) e) where
  angle = doubledAtanIncrement n m d hx hy
  t = relativeParameter n m d
  Eh : 0 ≤ fourStep e
  Eh = nonnegative-sum (e Q.+ e) (e Q.+ e) (nonnegative-sum e e eh eh) (nonnegative-sum e e eh eh)
  e²h : 0 ≤ e Q.· e
  e²h = nonnegative-bound-product e e eh eh
  relativeBudget≥0 : 0 ≤ relativeBudget e
  relativeBudget≥0 = nonnegative-sum (TickAtanFirstOrderBounds.scale e Q.+ TickAtanFirstOrderBounds.scale e) (one-half Q.· (e Q.· e))
    (nonnegative-sum (TickAtanFirstOrderBounds.scale e) (TickAtanFirstOrderBounds.scale e) (scale-nonnegative e eh) (scale-nonnegative e eh))
    (nonnegative-bound-product one-half (e Q.· e) one-half-nonnegative e²h)
  Bh : 0 ≤ relativeBudget e Q.+ relativeBudget e
  Bh = nonnegative-sum (relativeBudget e) (relativeBudget e) relativeBudget≥0 relativeBudget≥0
  clock : CompletionMagnitudeBound (doubledAtanIncrement n m d hx hy +completion
    (-completion (embedMetricℚ (relativeParameter n m d Q.+ relativeParameter n m d))))
    (relativeBudget e Q.+ relativeBudget e)
  clock = doubled-clock-bound (atanIncrement (gridValue n d) (gridValue m d) hx hy) (relativeParameter n m d)
    (relativeBudget e) (grid-clock-input n m d e hx hy eh hd)
  real-grid-bracket-bound : CompletionMagnitudeBound
    (realBracket (doubledAtanIncrement n m d hx hy) (relativeParameter n m d)) (realGridBudget e)
  real-grid-bracket-bound = real-bracket-bound (doubledAtanIncrement n m d hx hy) (relativeParameter n m d)
    (fourStep e) e (relativeBudget e Q.+ relativeBudget e)
    Eh eh Bh (four-step-small e small) (grid-angle-input n m d e hx hy eh small hd)
    (grid-parameter-input n m d e eh hd) clock

  imaginary-grid-bracket-bound : CompletionMagnitudeBound
    (imaginaryBracket (doubledAtanIncrement n m d hx hy) (relativeParameter n m d)) (imaginaryGridBudget e)
  imaginary-grid-bracket-bound = imaginary-bracket-bound (doubledAtanIncrement n m d hx hy) (relativeParameter n m d)
    (fourStep e) e (relativeBudget e Q.+ relativeBudget e)
    Eh eh Bh (four-step-small e small) (grid-angle-input n m d e hx hy eh small hd)
    (grid-parameter-input n m d e eh hd) clock
