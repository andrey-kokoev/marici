{-# OPTIONS --safe --cubical --guardedness #-}
module TickCompletionProductMagnitude where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Data.Nat as N using (suc)
import Cubical.Data.Nat.Order as NO
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
import Cubical.HITs.SetQuotients as SQ
open import Cubical.HITs.PropositionalTruncation as PT
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyProductBounds
open import CauchyCompletionMultiplication using (preferredCompletionMultiplication)
open import TickCompletionMagnitudeBounds
open import TickCompletionScalarBounds
open import TickCompletionLimits
open import TickCompletionRingContinuity using (multiplication-joint-continuous)
open import TickSmallAngleDensity using (completion-bound-weaken)
open import TickAtanFirstOrderBounds using (errorOffset)
open import RationalArchimedean using (dominates)
import AutomaticRationalExponentialMultiplication as Auto
import AbsoluteTaylorSeriesMultiplication as A

abstract
  completion-product-bound : (a b : MetricCompletionCandidate) (A B : Q.ℚ) →
    0 ≤ A → 0 ≤ B → CompletionMagnitudeBound a A → CompletionMagnitudeBound b B →
    CompletionMagnitudeBound (preferredCompletionMultiplication a b) (A Q.· B)
  completion-product-bound = SQ.elimProp
    (λ a → isPropΠ λ b → isPropΠ λ A → isPropΠ λ B → isPropΠ λ Ah → isPropΠ λ Bh →
      isPropΠ λ ha → isPropΠ λ hb → completion-magnitude-isProp (preferredCompletionMultiplication a b) (A Q.· B))
    (λ x b A B Ah Bh ha hb → completion-limit-magnitude
      (λ n → preferredCompletionMultiplication (rational-approximants x n) b)
      (preferredCompletionMultiplication SQ.[ x ] b) (A Q.· B)
      (joint-continuous-limit preferredCompletionMultiplication multiplication-joint-continuous
        (rational-approximants x) (λ _ → b) SQ.[ x ] b (rational-approximants-converge x) (constant-converges b))
      (λ k → PT.map (λ { (threshold , bound) → threshold , λ n hn → completion-bound-weaken
        (preferredCompletionMultiplication (rational-approximants x n) b)
        ((A Q.+ precision (errorOffset B N.+ k)) Q.· B) ((A Q.· B) Q.+ precision k)
        (subst (_≤ (A Q.· B) Q.+ precision k)
          (sym (Q.·DistR+ A (precision (errorOffset B N.+ k)) B))
          (≤Monotone+ (A Q.· B) (A Q.· B) (precision (errorOffset B N.+ k) Q.· B) (precision k)
            (isRefl≤ (A Q.· B))
            (subst (_≤ precision k) (Q.·Comm B (precision (errorOffset B N.+ k)))
              (A.scaledCoefficientAbsorption B (errorOffset B) k (dominates (Auto.preferredExponent B))))))
        (completion-rational-multiplier-bound (approximation x (suc n)) (A Q.+ precision (errorOffset B N.+ k)) b B
          (subst (_≤ A Q.+ precision (errorOffset B N.+ k)) (Q.+IdL 0)
            (≤Monotone+ 0 A 0 (precision (errorOffset B N.+ k)) Ah (precision-nonnegative (errorOffset B N.+ k))))
          Bh (bound (suc n) (NO.≤-trans hn NO.≤-sucℕ)) hb) })
        (completion-bound-representative x A ha (errorOffset B N.+ k))))
