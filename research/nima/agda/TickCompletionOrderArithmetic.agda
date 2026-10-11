{-# OPTIONS --safe --cubical --guardedness #-}
module TickCompletionOrderArithmetic where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Data.Nat using (ℕ; zero; suc)
import Cubical.Data.Nat.Order as NO
open import Cubical.Data.Sigma using (Σ; _×_)
open import Cubical.HITs.PropositionalTruncation as PT
import Cubical.HITs.SetQuotients as SQ
open import Cubical.Data.Rationals as Q hiding (_+_; _·_; -_)
open import Cubical.Data.Rationals.Order
open import Cubical.Relation.Nullary using (yes; no)
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate using (PreferredℚCommRing)
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyAddition using (addRegular)
open import CauchyAdditionCongruence using (_+completion_)
open import CauchyNegation using (-completion_)
open import CauchyCompletionAbGroup using (zeroCompletion)
open import CauchyCompletionCommRing using (CompletionCommRing)
open import CauchyProductBounds
open import TaylorTermBounds using (nonnegative-bound-product)
open import ConstructiveComplexCompletion using (ComplexCompletion; realPart; imaginaryPart)
open import TickCompletionDerivative
open import TickCompletionLimits
open import TickCompletionOrderLimits using
  (completion-nonnegative-isProp; rational-limit-nonnegative; rational-moving-product-converges)

module Algebra (R : CommRing ℓ-zero) where
  open CommRingStr (snd R)
  abstract
    minus-sum : (e : fst R) → (- e) + (- e) ≡ - (e + e)
    minus-sum e = solve! R
    cancel : (e : fst R) → (- e) + e ≡ 0r
    cancel e = solve! R
    difference-self : (a : fst R) → a + (- a) ≡ 0r
    difference-self a = solve! R
    differences-compose : (a b c : fst R) → (b + (- a)) + (c + (- b)) ≡ c + (- a)
    differences-compose a b c = solve! R
module QR = Algebra PreferredℚCommRing
module CR = Algebra CompletionCommRing

abstract
  rational-lower-slack : (q e : Q.ℚ) → 0 ≤ q → 0 ≤ e → Q.- e ≤ q
  rational-lower-slack q e positive slack = isTrans≤ (Q.- e) 0 q
    (subst (Q.- e ≤_) (QR.cancel e) (≤-add-nonnegative (Q.- e) e slack)) positive

  rational-lower-sum : (x y e : Q.ℚ) → Q.- e ≤ x → Q.- e ≤ y → Q.- (e Q.+ e) ≤ x Q.+ y
  rational-lower-sum x y e hx hy = subst (_≤ x Q.+ y) (QR.minus-sum e)
    (isTrans≤ ((Q.- e) Q.+ (Q.- e)) (x Q.+ (Q.- e)) (x Q.+ y)
      (≤-+o (Q.- e) x (Q.- e) hx) (≤-o+ (Q.- e) y x hy))

rational-square-nonnegative : (q : Q.ℚ) → 0 ≤ q Q.· q
rational-square-nonnegative q with <Dec q 0
... | no h = nonnegative-bound-product q q (≮→≥ q 0 h) (≮→≥ q 0 h)
... | yes h = subst (0 ≤_) (sym (ProductSignPaths.double-negative-product PreferredℚCommRing q q))
  (nonnegative-bound-product (Q.- q) (Q.- q)
    (nonpositive→negative-nonnegative q (<Weaken≤ q 0 h))
    (nonpositive→negative-nonnegative q (<Weaken≤ q 0 h)))

abstract
  completion-nonnegative-add : (a b : MetricCompletionCandidate) →
    CompletionNonnegative a → CompletionNonnegative b → CompletionNonnegative (a +completion b)
  completion-nonnegative-add a b ha hb k = PT.rec isPropPropTrunc
    (λ { (x , px , hx) → PT.map (λ { (y , py , hy) →
      addRegular x y , cong₂ _+completion_ px py ,
      PT.map (λ { (threshold , bounds) → threshold , λ n hn →
        subst (λ e → Q.- e ≤ approximation (addRegular x y) n) (precision-refines-double k)
          (rational-lower-sum (approximation x (suc n)) (approximation y (suc n)) (precision (suc k))
            (fst (bounds (suc n) (NO.≤-trans hn NO.≤-sucℕ)))
            (snd (bounds (suc n) (NO.≤-trans hn NO.≤-sucℕ)))) })
        (eventually-zip (λ n lowerX lowerY → lowerX , lowerY) hx hy) }) (hb (suc k)) }) (ha (suc k))

  embedded-nonnegative : (q : Q.ℚ) → 0 ≤ q → CompletionNonnegative (embedMetricℚ q)
  embedded-nonnegative q positive = rational-limit-nonnegative (λ _ → q) (embedMetricℚ q)
    (constant-converges (embedMetricℚ q))
    (λ k → ∣ zero , (λ n hn → rational-lower-slack q (precision k) positive (precision-nonnegative k)) ∣₁)

  completion-zero-nonnegative : CompletionNonnegative zeroCompletion
  completion-zero-nonnegative = embedded-nonnegative 0 (isRefl≤ 0)

  completion-order-refl : (a : MetricCompletionCandidate) → CompletionLE a a
  completion-order-refl a = subst CompletionNonnegative (sym (CR.difference-self a)) completion-zero-nonnegative

  completion-order-trans : (a b c : MetricCompletionCandidate) → CompletionLE a b → CompletionLE b c → CompletionLE a c
  completion-order-trans a b c hab hbc = subst CompletionNonnegative (CR.differences-compose a b c)
    (completion-nonnegative-add (b +completion (-completion a)) (c +completion (-completion b)) hab hbc)

  completion-square-nonnegative : (a : MetricCompletionCandidate) → CompletionNonnegative (squareCompletion a)
  completion-square-nonnegative = SQ.elimProp (λ a → completion-nonnegative-isProp (squareCompletion a))
    (λ x → rational-limit-nonnegative (λ n → approximation x (suc n) Q.· approximation x (suc n))
      (squareCompletion SQ.[ x ])
      (rational-moving-product-converges (λ n → approximation x (suc n)) (λ n → approximation x (suc n))
        SQ.[ x ] SQ.[ x ] (rational-approximants-converge x) (rational-approximants-converge x))
      (λ k → ∣ zero , (λ n hn → rational-lower-slack
        (approximation x (suc n) Q.· approximation x (suc n)) (precision k)
        (rational-square-nonnegative (approximation x (suc n))) (precision-nonnegative k)) ∣₁))

  complex-norm-nonnegative : (z : ComplexCompletion) → CompletionNonnegative (complexNormSquared z)
  complex-norm-nonnegative z = completion-nonnegative-add
    (squareCompletion (realPart z)) (squareCompletion (imaginaryPart z))
    (completion-square-nonnegative (realPart z)) (completion-square-nonnegative (imaginaryPart z))
