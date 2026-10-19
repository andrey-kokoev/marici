{-# OPTIONS --safe --cubical --guardedness #-}
module TickCompletionCoefficientBound where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as Nat using (ℕ; zero; suc)
import Cubical.Data.Nat.Order as NO
open import Cubical.Data.Sigma using (Σ)
open import Cubical.HITs.PropositionalTruncation as PT
import Cubical.HITs.SetQuotients as SQ
open import Cubical.Data.Rationals as Q hiding (_+_; _·_; -_)
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate using (PreferredℚCommRing)
open import RegularCauchyStructure
open import DyadicallyBoundedCauchy
open import CanonicalDyadicallyBoundedCauchy
open import CauchyMetricEquivalence
open import CauchyCompletionCommRing using (CompletionCommRing)
open import CauchyCompletionMultiplication
open import TickCompletionDerivative
open import TickCompletionLimits
open import TickCompletionOrderLimits using (rational-limit-order)
open import TickCompletionOrderArithmetic using
  (embedded-nonnegative; rational-square-nonnegative; completion-square-nonnegative; completion-order-trans)
open import TickCompletionPositiveProduct using (completion-nonnegative-product; completion-multiply-monotone)

module Algebra (R : CommRing ℓ-zero) where
  open CommRingStr (snd R)
  abstract
    square-factor : (r e : fst R) → (e · e) · r ≡ (r · e) · e
    square-factor r e = solve! R
    commute : (a b : fst R) → a · b ≡ b · a
    commute a b = solve! R
    budget-factor : (r e h : fst R) → r · (e · h) ≡ (e · r) · h
    budget-factor r e h = solve! R
module QR = Algebra PreferredℚCommRing
module CR = Algebra CompletionCommRing

precisionSquared : ℕ → Q.ℚ
precisionSquared k = precision k Q.· precision k

abstract
  completion-dyadic-upper : (a : MetricCompletionCandidate) →
    ∥ Σ ℕ (λ d → CompletionLE a (embedMetricℚ (dyadicRadius d))) ∥₁
  completion-dyadic-upper = SQ.elimProp (λ _ → isPropPropTrunc)
    (λ x → ∣ canonicalDyadicExponent x , rational-limit-order
      (λ n → approximation x (suc n)) (λ _ → dyadicRadius (canonicalDyadicExponent x))
      SQ.[ x ] (embedMetricℚ (dyadicRadius (canonicalDyadicExponent x)))
      (rational-approximants-converge x) (constant-converges (embedMetricℚ (dyadicRadius (canonicalDyadicExponent x))))
      (λ k → ∣ zero , (λ n hn → isTrans≤ (approximation x (suc n)) (dyadicRadius (canonicalDyadicExponent x))
        (dyadicRadius (canonicalDyadicExponent x) Q.+ precision k)
        (upper-bound (canonicalDyadicallyBounded x) (suc n))
        (≤-add-nonnegative (dyadicRadius (canonicalDyadicExponent x)) (precision k) (precision-nonnegative k))) ∣₁) ∣₁)

  embedded-order : (a b : Q.ℚ) → a ≤ b → CompletionLE (embedMetricℚ a) (embedMetricℚ b)
  embedded-order a b ab = rational-limit-order (λ _ → a) (λ _ → b) (embedMetricℚ a) (embedMetricℚ b)
    (constant-converges (embedMetricℚ a)) (constant-converges (embedMetricℚ b))
    (λ k → ∣ zero , (λ n hn → isTrans≤ a b (b Q.+ precision k) ab
      (≤-add-nonnegative b (precision k) (precision-nonnegative k))) ∣₁)

  squared-precision-absorption : (d k : ℕ) → precisionSquared (d Nat.+ k) Q.· dyadicRadius d ≤ precisionSquared k
  squared-precision-absorption d k = subst (_≤ precisionSquared k)
    (sym (QR.square-factor (dyadicRadius d) (precision (d Nat.+ k))
      ∙ cong (Q._· precision (d Nat.+ k)) (radius-cancels-precision-shift d k)
      ∙ Q.·Comm (precision k) (precision (d Nat.+ k))))
    (≤-·o (precision (d Nat.+ k)) (precision k) (precision k) (precision-nonnegative k)
      (precision-antitone k (d Nat.+ k) NO.≤SumRight))

  coefficient-absorption : (c : MetricCompletionCandidate) (d k : ℕ) →
    CompletionLE c (embedMetricℚ (dyadicRadius d)) → (h : MetricCompletionCandidate) →
    CompletionLE
      (preferredCompletionMultiplication
        (preferredCompletionMultiplication (embedMetricℚ (precisionSquared (d Nat.+ k))) (squareCompletion h)) c)
      (preferredCompletionMultiplication (embedMetricℚ (precisionSquared k)) (squareCompletion h))
  coefficient-absorption c d k bound h = completion-order-trans
    (preferredCompletionMultiplication
      (preferredCompletionMultiplication (embedMetricℚ (precisionSquared (d Nat.+ k))) (squareCompletion h)) c)
    (preferredCompletionMultiplication (embedMetricℚ (precisionSquared (d Nat.+ k) Q.· dyadicRadius d)) (squareCompletion h))
    (preferredCompletionMultiplication (embedMetricℚ (precisionSquared k)) (squareCompletion h))
    (subst2 CompletionLE
      (CR.commute c (preferredCompletionMultiplication (embedMetricℚ (precisionSquared (d Nat.+ k))) (squareCompletion h)))
      (CR.budget-factor (embedMetricℚ (dyadicRadius d)) (embedMetricℚ (precisionSquared (d Nat.+ k))) (squareCompletion h)
        ∙ cong (λ e → preferredCompletionMultiplication e (squareCompletion h))
          (preferredCompletionMultiplication-preserves-rationals (precisionSquared (d Nat.+ k)) (dyadicRadius d)))
      (completion-multiply-monotone c (embedMetricℚ (dyadicRadius d))
        (preferredCompletionMultiplication (embedMetricℚ (precisionSquared (d Nat.+ k))) (squareCompletion h)) bound
        (completion-nonnegative-product (embedMetricℚ (precisionSquared (d Nat.+ k))) (squareCompletion h)
          (embedded-nonnegative (precisionSquared (d Nat.+ k)) (rational-square-nonnegative (precision (d Nat.+ k))))
          (completion-square-nonnegative h))))
    (completion-multiply-monotone (embedMetricℚ (precisionSquared (d Nat.+ k) Q.· dyadicRadius d))
      (embedMetricℚ (precisionSquared k)) (squareCompletion h)
      (embedded-order (precisionSquared (d Nat.+ k) Q.· dyadicRadius d) (precisionSquared k) (squared-precision-absorption d k))
      (completion-square-nonnegative h))
