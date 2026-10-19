{-# OPTIONS --safe --cubical --guardedness #-}
module TickCompletionPositiveProduct where

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
open import MetricCompletionEffectiveness using (quotientPathToMetric)
open import CauchyAdditionCongruence using (_+completion_)
open import CauchyNegation using (-completion_)
open import CauchyCompletionCommRing using (CompletionCommRing)
open import CauchyCompletionMultiplication using (preferredCompletionMultiplication)
open import TaylorTermBounds using (nonnegative-bound-product)
open import TickCompletionMetric
open import TickCompletionDerivative
open import TickCompletionLimits
open import TickCompletionOrderLimits using
  (completion-nonnegative-isProp; lower-transfer; rational-limit-nonnegative; rational-moving-product-converges)
open import TickCompletionOrderArithmetic using (rational-lower-slack)

module Algebra (R : CommRing ℓ-zero) where
  open CommRingStr (snd R)
  abstract
    cancel : (e : fst R) → (- e) + e ≡ 0r
    cancel e = solve! R
    difference-product : (a b c : fst R) → (b + (- a)) · c ≡ b · c + (- (a · c))
    difference-product a b c = solve! R
module QR = Algebra PreferredℚCommRing
module CR = Algebra CompletionCommRing

-- Recover the lower bound on any fixed representative, spending one bit
-- for the cone witness and one comparison at that same precision.
abstract
  nonnegative-representative : (x : RegularCauchy) → CompletionNonnegative SQ.[ x ] →
    (k : ℕ) → EventuallyNonnegative x k
  nonnegative-representative x positive k = PT.rec isPropPropTrunc
    (λ { (y , path , lower) → eventually-zip (λ n hy near →
      subst (λ e → Q.- e ≤ approximation x n) (precision-refines-double k)
        (lower-transfer (approximation y n) (approximation x n) (precision (suc k)) hy (fst near)))
      lower (quotientPathToMetric y x path (suc k)) }) (positive (suc k))

positivePart : Q.ℚ → Q.ℚ
positivePart q with <Dec q 0
... | yes _ = 0
... | no _ = q

positivePart-nonnegative : (q : Q.ℚ) → 0 ≤ positivePart q
positivePart-nonnegative q with <Dec q 0
... | yes _ = isRefl≤ 0
... | no h = ≮→≥ q 0 h

positivePart-within : (q : Q.ℚ) (k : ℕ) → Q.- precision k ≤ q →
  CompletionWithin (embedMetricℚ q) (embedMetricℚ (positivePart q)) k
positivePart-within q k lower with <Dec q 0
... | no _ = within-refl (embedMetricℚ q) k
... | yes negative = within-intro (constantCauchy q) (constantCauchy 0) k
  ∣ zero , (λ n hn →
    isTrans≤ q 0 (0 Q.+ precision k) (<Weaken≤ q 0 negative)
      (≤-add-nonnegative 0 (precision k) (precision-nonnegative k)) ,
    subst (_≤ q Q.+ precision k) (QR.cancel (precision k))
      (≤-+o (Q.- precision k) q (precision k) lower)) ∣₁

positive-approximant : RegularCauchy → ℕ → Q.ℚ
positive-approximant x n = positivePart (approximation x (suc n))

abstract
  positive-approximants-converge : (x : RegularCauchy) → CompletionNonnegative SQ.[ x ] →
    Converges (λ n → embedMetricℚ (positive-approximant x n)) SQ.[ x ]
  positive-approximants-converge x positive k = eventually-zip
    (λ n near lower → within-triangle SQ.[ x ] (rational-approximants x n)
      (embedMetricℚ (positive-approximant x n)) k near
      (positivePart-within (approximation x (suc n)) (suc (suc (suc k))) lower))
    (rational-approximants-converge x (suc (suc (suc k))))
    (PT.map (λ { (threshold , lower) → threshold , λ n hn → lower (suc n) (NO.≤-trans hn NO.≤-sucℕ) })
      (nonnegative-representative x positive (suc (suc (suc k)))))

  completion-nonnegative-product : (a b : MetricCompletionCandidate) →
    CompletionNonnegative a → CompletionNonnegative b → CompletionNonnegative (preferredCompletionMultiplication a b)
  completion-nonnegative-product = SQ.elimProp2
    (λ a b → isPropΠ λ _ → isPropΠ λ _ → completion-nonnegative-isProp (preferredCompletionMultiplication a b))
    (λ x y hx hy → rational-limit-nonnegative
      (λ n → positive-approximant x n Q.· positive-approximant y n)
      (preferredCompletionMultiplication SQ.[ x ] SQ.[ y ])
      (rational-moving-product-converges (positive-approximant x) (positive-approximant y) SQ.[ x ] SQ.[ y ]
        (positive-approximants-converge x hx) (positive-approximants-converge y hy))
      (λ k → ∣ zero , (λ n hn → rational-lower-slack
        (positive-approximant x n Q.· positive-approximant y n) (precision k)
        (nonnegative-bound-product (positive-approximant x n) (positive-approximant y n)
          (positivePart-nonnegative (approximation x (suc n)))
          (positivePart-nonnegative (approximation y (suc n)))) (precision-nonnegative k)) ∣₁))

  completion-multiply-monotone : (a b c : MetricCompletionCandidate) → CompletionLE a b → CompletionNonnegative c →
    CompletionLE (preferredCompletionMultiplication a c) (preferredCompletionMultiplication b c)
  completion-multiply-monotone a b c hab hc = subst CompletionNonnegative (CR.difference-product a b c)
    (completion-nonnegative-product (b +completion (-completion a)) c hab hc)
