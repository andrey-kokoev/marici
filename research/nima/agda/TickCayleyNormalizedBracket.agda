{-# OPTIONS --safe --cubical --guardedness #-}
module TickCayleyNormalizedBracket where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate using (one-half)
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyProductBounds
open import CauchyAdditionCongruence using (_+completion_)
open import CauchyNegation using (-completion_)
open import CauchyCompletionMultiplication using (preferredCompletionMultiplication)
open import CauchyCompletionCommRing
open import TaylorTermBounds using (nonnegative-value-magnitude; nonnegative-bound-product)
open import OperationalCosineMetric using (completionCosine)
open import OperationalSineMetric using (completionSine)
open import TickCompletionMagnitudeBounds
open import TickCompletionScalarBounds
open import TickCayleyGridSlope using (rational-product-equation)
open import TickCayleyGridIncrement using (gridValue)
open import TickAtanGridSmallAngle using (doubledAtanIncrement)
open import TickAtanCayleyIncrement using (relativeParameter)
open import TickCayleyRelativeRotor using
  (relativeInverse; relative-inverse-law; relative-inverse-nonnegative; relative-inverse≤one; relativeCosine; relativeSine)
import TickCayleyRotationalBracket as Bracket
open import TickCayleyQuadraticBudgets using (grid-budget-domination)
open import TickSmallAngleDensity using (completion-bound-weaken)

module Algebra {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; _·_ to _·S_; -_ to -S_)
  distribute : (u d a b : fst R) → u ·S ((d ·S a) +S (-S b)) ≡ ((u ·S d) ·S a) +S (-S (u ·S b))
  distribute u d a b = solve! R
module C = Algebra CompletionCommRing

abstract
  normalization-path : (a : MetricCompletionCandidate) (u d b : Q.ℚ) → d Q.· u ≡ 1 →
    preferredCompletionMultiplication (embedMetricℚ u)
      (preferredCompletionMultiplication (embedMetricℚ d) a +completion (-completion (embedMetricℚ b))) ≡
    a +completion (-completion (embedMetricℚ (b Q.· u)))
  normalization-path a u d b law = C.distribute (embedMetricℚ u) (embedMetricℚ d) a (embedMetricℚ b)
    ∙ cong₂ _+completion_
      (cong (λ z → preferredCompletionMultiplication z a) (rational-product-equation u d 1 (Q.·Comm u d ∙ law))
        ∙ CommRingStr.·IdL (snd CompletionCommRing) a)
      (cong -completion_ (rational-product-equation u b (b Q.· u) (Q.·Comm u b)))

  normalize-bracket-bound : (a r : MetricCompletionCandidate) (u d b B : Q.ℚ) →
    d Q.· u ≡ 1 → 0 ≤ u → u ≤ 1 → 0 ≤ B →
    (preferredCompletionMultiplication (embedMetricℚ d) a +completion (-completion (embedMetricℚ b))) ≡ r →
    CompletionMagnitudeBound r B → CompletionMagnitudeBound (a +completion (-completion (embedMetricℚ (b Q.· u)))) B
  normalize-bracket-bound a r u d b B law uh u≤ Bh definition bound = completion-bound-path
    (preferredCompletionMultiplication (embedMetricℚ u) r)
    (a +completion (-completion (embedMetricℚ (b Q.· u)))) B
    (cong (preferredCompletionMultiplication (embedMetricℚ u)) (sym definition) ∙ normalization-path a u d b law)
    (subst (λ q → CompletionMagnitudeBound (preferredCompletionMultiplication (embedMetricℚ u) r) q) (Q.·IdL B)
      (completion-rational-multiplier-bound u 1 r B (precision-nonnegative 0) Bh
        (nonnegative-value-magnitude u 1 uh u≤ (precision-nonnegative 0)) bound))

  grid-cleared-real : (n m d : ℕ) (e : Q.ℚ)
    (hx : MagnitudeBound (gridValue n d) one-half) (hy : MagnitudeBound (gridValue m d) one-half)
    (eh : 0 ≤ e) (small : e ≤ precision 6) (hd : MagnitudeBound (gridValue m d Q.+ (Q.- gridValue n d)) e) →
    CompletionMagnitudeBound (Bracket.realBracket (doubledAtanIncrement n m d hx hy) (relativeParameter n m d)) (Bracket.realGridBudget e)
  grid-cleared-real = Bracket.Grid.real-grid-bracket-bound

  grid-cleared-imaginary : (n m d : ℕ) (e : Q.ℚ)
    (hx : MagnitudeBound (gridValue n d) one-half) (hy : MagnitudeBound (gridValue m d) one-half)
    (eh : 0 ≤ e) (small : e ≤ precision 6) (hd : MagnitudeBound (gridValue m d Q.+ (Q.- gridValue n d)) e) →
    CompletionMagnitudeBound (Bracket.imaginaryBracket (doubledAtanIncrement n m d hx hy) (relativeParameter n m d)) (Bracket.imaginaryGridBudget e)
  grid-cleared-imaginary = Bracket.Grid.imaginary-grid-bracket-bound

  real-definition : (a : MetricCompletionCandidate) (t : Q.ℚ) →
    preferredCompletionMultiplication (embedMetricℚ (1 Q.+ t Q.· t)) (completionCosine a)
      +completion (-completion (embedMetricℚ (1 Q.+ (Q.- (t Q.· t))))) ≡ Bracket.realBracket a t
  real-definition = Bracket.real-bracket-definition
  imaginary-definition : (a : MetricCompletionCandidate) (t : Q.ℚ) →
    preferredCompletionMultiplication (embedMetricℚ (1 Q.+ t Q.· t)) (completionSine a)
      +completion (-completion (embedMetricℚ (t Q.+ t))) ≡ Bracket.imaginaryBracket a t
  imaginary-definition = Bracket.imaginary-bracket-definition

module Grid (n m d : ℕ) (e : Q.ℚ)
  (hx : MagnitudeBound (gridValue n d) one-half) (hy : MagnitudeBound (gridValue m d) one-half)
  (eh : 0 ≤ e) (small : e ≤ precision 6) (hd : MagnitudeBound (gridValue m d Q.+ (Q.- gridValue n d)) e) where
  module Cleared = Bracket.Grid n m d e hx hy eh small hd
  angle = doubledAtanIncrement n m d hx hy
  t = relativeParameter n m d
  u = relativeInverse n m d
  e²h = nonnegative-bound-product e e eh eh
  fourh = Bracket.nonnegative-sum (e Q.+ e) (e Q.+ e) (Bracket.nonnegative-sum e e eh eh) (Bracket.nonnegative-sum e e eh eh)
  Dh = Bracket.nonnegative-sum 1 (e Q.· e) (precision-nonnegative 0) e²h
  mainh = nonnegative-bound-product (1 Q.+ e Q.· e)
    (TickAtanGridSmallAngle.fourStep e Q.· TickAtanGridSmallAngle.fourStep e) Dh
    (nonnegative-bound-product (TickAtanGridSmallAngle.fourStep e) (TickAtanGridSmallAngle.fourStep e) fourh fourh)
  realBudget≥0 : 0 ≤ Bracket.realGridBudget e
  realBudget≥0 = Bracket.nonnegative-sum ((1 Q.+ e Q.· e) Q.· (TickAtanGridSmallAngle.fourStep e Q.· TickAtanGridSmallAngle.fourStep e))
    ((e Q.· e) Q.+ (e Q.· e)) mainh (Bracket.nonnegative-sum (e Q.· e) (e Q.· e) e²h e²h)
  imaginaryBudget≥0 : 0 ≤ Bracket.imaginaryGridBudget e
  imaginaryBudget≥0 = Bracket.nonnegative-sum
    (((1 Q.+ e Q.· e) Q.· (TickAtanGridSmallAngle.fourStep e Q.· TickAtanGridSmallAngle.fourStep e)) Q.+
      (1 Q.+ e Q.· e) Q.· (TickAtanCayleyIncrement.relativeBudget e Q.+ TickAtanCayleyIncrement.relativeBudget e))
    ((e Q.+ e) Q.· (e Q.· e))
    (Bracket.nonnegative-sum ((1 Q.+ e Q.· e) Q.· (TickAtanGridSmallAngle.fourStep e Q.· TickAtanGridSmallAngle.fourStep e))
      ((1 Q.+ e Q.· e) Q.· (TickAtanCayleyIncrement.relativeBudget e Q.+ TickAtanCayleyIncrement.relativeBudget e)) mainh
      (nonnegative-bound-product (1 Q.+ e Q.· e)
        (TickAtanCayleyIncrement.relativeBudget e Q.+ TickAtanCayleyIncrement.relativeBudget e) Dh Cleared.Bh))
    (nonnegative-bound-product (e Q.+ e) (e Q.· e) (Bracket.nonnegative-sum e e eh eh) e²h)

  normalized-real-bound : CompletionMagnitudeBound
    (completionCosine (doubledAtanIncrement n m d hx hy) +completion
      (-completion (embedMetricℚ ((1 Q.+ (Q.- (relativeParameter n m d Q.· relativeParameter n m d))) Q.· relativeInverse n m d))))
    (Bracket.realGridBudget e)
  normalized-real-bound = normalize-bracket-bound
    (completionCosine (doubledAtanIncrement n m d hx hy))
    (Bracket.realBracket (doubledAtanIncrement n m d hx hy) (relativeParameter n m d))
    (relativeInverse n m d) (1 Q.+ relativeParameter n m d Q.· relativeParameter n m d)
    (1 Q.+ (Q.- (relativeParameter n m d Q.· relativeParameter n m d))) (Bracket.realGridBudget e)
    (relative-inverse-law n m d) (relative-inverse-nonnegative n m d) (relative-inverse≤one n m d) realBudget≥0
    (real-definition (doubledAtanIncrement n m d hx hy) (relativeParameter n m d)) (grid-cleared-real n m d e hx hy eh small hd)

  normalized-imaginary-bound : CompletionMagnitudeBound
    (completionSine (doubledAtanIncrement n m d hx hy) +completion
      (-completion (embedMetricℚ ((relativeParameter n m d Q.+ relativeParameter n m d) Q.· relativeInverse n m d))))
    (Bracket.imaginaryGridBudget e)
  normalized-imaginary-bound = normalize-bracket-bound
    (completionSine (doubledAtanIncrement n m d hx hy))
    (Bracket.imaginaryBracket (doubledAtanIncrement n m d hx hy) (relativeParameter n m d))
    (relativeInverse n m d) (1 Q.+ relativeParameter n m d Q.· relativeParameter n m d)
    (relativeParameter n m d Q.+ relativeParameter n m d) (Bracket.imaginaryGridBudget e)
    (relative-inverse-law n m d) (relative-inverse-nonnegative n m d) (relative-inverse≤one n m d) imaginaryBudget≥0
    (imaginary-definition (doubledAtanIncrement n m d hx hy) (relativeParameter n m d)) (grid-cleared-imaginary n m d e hx hy eh small hd)

  uniform-real-bound : CompletionMagnitudeBound
    (completionCosine (doubledAtanIncrement n m d hx hy) +completion
      (-completion (embedMetricℚ ((1 Q.+ (Q.- (relativeParameter n m d Q.· relativeParameter n m d))) Q.· relativeInverse n m d))))
    (34 Q.· (e Q.· e))
  uniform-real-bound = completion-bound-weaken
    (completionCosine (doubledAtanIncrement n m d hx hy) +completion
      (-completion (embedMetricℚ ((1 Q.+ (Q.- (relativeParameter n m d Q.· relativeParameter n m d))) Q.· relativeInverse n m d))))
    (Bracket.realGridBudget e) (34 Q.· (e Q.· e)) (fst (grid-budget-domination e eh small)) normalized-real-bound

  uniform-imaginary-bound : CompletionMagnitudeBound
    (completionSine (doubledAtanIncrement n m d hx hy) +completion
      (-completion (embedMetricℚ ((relativeParameter n m d Q.+ relativeParameter n m d) Q.· relativeInverse n m d))))
    (99 Q.· (e Q.· e))
  uniform-imaginary-bound = completion-bound-weaken
    (completionSine (doubledAtanIncrement n m d hx hy) +completion
      (-completion (embedMetricℚ ((relativeParameter n m d Q.+ relativeParameter n m d) Q.· relativeInverse n m d))))
    (Bracket.imaginaryGridBudget e) (99 Q.· (e Q.· e)) (snd (grid-budget-domination e eh small)) normalized-imaginary-bound
