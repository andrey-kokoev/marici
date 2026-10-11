{-# OPTIONS --safe --cubical --guardedness #-}
module TickMachinReferenceSeries where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ)
import Cubical.Data.Nat.Order as NO
open import Cubical.Data.Rationals as Q
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate using (PreferredℚCommRing)
open import RegularCauchyStructure using (precision)
open import CauchyMetricEquivalence
import CauchyAdditionCongruence
open import CauchyNegation using (-completion_)
open import CauchyProductBounds
open import TickCompletionLimits using (Converges)
open import TickRationalProductLimits
open import TickAtanCompletionFirstOrder using (atanCompletion; atan-completion-converges)
open import TickMachinCayleyInputs using (fifth-small; small239; fifth-completion-agreement; completion239-agreement)
open import TickMachinPiCandidate using (atanFifth; atan239th; oneFifth; one239th; fourCompletion; machinPi; machin-pi-formula)
open import TickSmallArctangent using (atanPartialSum; atan-ordered-bound)

fourℚ : Q.ℚ → Q.ℚ
fourℚ q = (q Q.+ q) Q.+ (q Q.+ q)

machinPartialSum : ℕ → Q.ℚ
machinPartialSum n = fourℚ (fourℚ (atanPartialSum oneFifth n)) Q.+ (Q.- fourℚ (atanPartialSum one239th n))

module Algebra {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; _·_ to _·S_; -_ to -S_)
  four : fst R → fst R
  four q = (q +S q) +S (q +S q)
  coefficient = four (four 1r) +S four 1r
  difference : (a b c d : fst R) →
    (four (four a) +S (-S four b)) +S (-S (four (four c) +S (-S four d))) ≡
    four (four (a +S (-S c))) +S (-S four (b +S (-S d)))
  difference a b c d = solve! R
  budget : (p : fst R) → four (four p) +S four p ≡ coefficient ·S p
  budget p = solve! R
module R = Algebra PreferredℚCommRing

abstract
  four-magnitude : (q B : Q.ℚ) → MagnitudeBound q B → MagnitudeBound (fourℚ q) (fourℚ B)
  four-magnitude q B h = add-magnitude-bounds (q Q.+ q) (B Q.+ B) (q Q.+ q) (B Q.+ B)
    (add-magnitude-bounds q B q B h h) (add-magnitude-bounds q B q B h h)

  twenty-coefficient : R.coefficient ≡ 20
  twenty-coefficient = Q.eq/ _ _ refl

  machin-tail-bound : (n m : ℕ) → NO._≤_ n m →
    MagnitudeBound (machinPartialSum m Q.+ (Q.- machinPartialSum n)) (20 Q.· precision n)
  machin-tail-bound n m h = subst2 MagnitudeBound
    (sym (R.difference (atanPartialSum oneFifth m) (atanPartialSum one239th m)
      (atanPartialSum oneFifth n) (atanPartialSum one239th n)))
    (R.budget (precision n) ∙ cong (Q._· precision n) twenty-coefficient)
    (add-magnitude-bounds
      (fourℚ (fourℚ (atanPartialSum oneFifth m Q.+ (Q.- atanPartialSum oneFifth n)))) (fourℚ (fourℚ (precision n)))
      (Q.- fourℚ (atanPartialSum one239th m Q.+ (Q.- atanPartialSum one239th n))) (fourℚ (precision n))
      (four-magnitude (fourℚ (atanPartialSum oneFifth m Q.+ (Q.- atanPartialSum oneFifth n))) (fourℚ (precision n))
        (four-magnitude (atanPartialSum oneFifth m Q.+ (Q.- atanPartialSum oneFifth n)) (precision n)
          (atan-ordered-bound oneFifth fifth-small n m h)))
      (negate-magnitude-bound (fourℚ (atanPartialSum one239th m Q.+ (Q.- atanPartialSum one239th n))) (fourℚ (precision n))
        (four-magnitude (atanPartialSum one239th m Q.+ (Q.- atanPartialSum one239th n)) (precision n)
          (atan-ordered-bound one239th small239 n m h))))

  four-sequence-converges : (p : ℕ → Q.ℚ) (a : MetricCompletionCandidate) →
    Converges (λ n → embedMetricℚ (p n)) a → Converges (λ n → embedMetricℚ (fourℚ (p n))) (fourCompletion a)
  four-sequence-converges p a hp = rational-sum-sequence-converges
    (λ n → p n Q.+ p n) (λ n → p n Q.+ p n)
    (CauchyAdditionCongruence._+completion_ a a) (CauchyAdditionCongruence._+completion_ a a)
    (rational-sum-sequence-converges p p a a hp hp) (rational-sum-sequence-converges p p a a hp hp)

  convergence-target-path : (p : ℕ → Q.ℚ) (a b : MetricCompletionCandidate) → a ≡ b →
    Converges (λ n → embedMetricℚ (p n)) a → Converges (λ n → embedMetricℚ (p n)) b
  convergence-target-path p a b path h = subst (Converges (λ n → embedMetricℚ (p n))) path h

fifth-converges : Converges (λ n → embedMetricℚ (atanPartialSum oneFifth n)) atanFifth
fifth-converges = convergence-target-path (atanPartialSum oneFifth) (atanCompletion oneFifth fifth-small) atanFifth
  fifth-completion-agreement (atan-completion-converges oneFifth fifth-small)

converges239 : Converges (λ n → embedMetricℚ (atanPartialSum one239th n)) atan239th
converges239 = convergence-target-path (atanPartialSum one239th) (atanCompletion one239th small239) atan239th
  completion239-agreement (atan-completion-converges one239th small239)

machin-series-converges : Converges (λ n → embedMetricℚ (machinPartialSum n)) machinPi
machin-series-converges = convergence-target-path machinPartialSum
  (CauchyAdditionCongruence._+completion_ (fourCompletion (fourCompletion atanFifth)) (-completion (fourCompletion atan239th)))
  machinPi (sym machin-pi-formula)
  (rational-sum-sequence-converges (λ n → fourℚ (fourℚ (atanPartialSum oneFifth n))) (λ n → Q.- fourℚ (atanPartialSum one239th n))
    (fourCompletion (fourCompletion atanFifth)) (-completion (fourCompletion atan239th))
    (four-sequence-converges (λ n → fourℚ (atanPartialSum oneFifth n)) (fourCompletion atanFifth)
      (four-sequence-converges (atanPartialSum oneFifth) atanFifth fifth-converges))
    (rational-negative-sequence-converges (λ n → fourℚ (atanPartialSum one239th n)) (fourCompletion atan239th)
      (four-sequence-converges (atanPartialSum one239th) atan239th converges239)))

-- A reference backend must supply the convergence proof for its pi image.
-- This theorem does not supply or assume a standard-pi constant itself.
reference-series-identification : (referencePi : MetricCompletionCandidate) →
  Converges (λ n → embedMetricℚ (machinPartialSum n)) referencePi → machinPi ≡ referencePi
reference-series-identification referencePi h = convergent-limits-equal
  (λ n → embedMetricℚ (machinPartialSum n)) machinPi referencePi machin-series-converges h
