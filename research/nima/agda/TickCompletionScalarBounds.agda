{-# OPTIONS --safe --cubical --guardedness #-}
module TickCompletionScalarBounds where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Data.Nat as N using (ℕ; suc)
import Cubical.Data.Nat.Order as NO
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.HITs.PropositionalTruncation as PT
import Cubical.HITs.SetQuotients as SQ
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyProductBounds
open import CauchyCompletionMultiplication using (preferredCompletionMultiplication)
open import TaylorTermBounds using (nonnegative-bound-product)
open import RationalArchimedean using (dominates)
import AutomaticRationalExponentialMultiplication as Auto
import AbsoluteTaylorSeriesMultiplication as A
open import TickAtanFirstOrderBounds using (errorOffset)
open import TickCompletionMagnitudeBounds
open import TickCompletionLimits
open import TickRationalProductLimits

abstract
  completion-rational-multiplier-bound : (c C : Q.ℚ) (a : MetricCompletionCandidate) (B : Q.ℚ) →
    0 ≤ C → 0 ≤ B → MagnitudeBound c C → CompletionMagnitudeBound a B →
    CompletionMagnitudeBound (preferredCompletionMultiplication (embedMetricℚ c) a) (C Q.· B)
  completion-rational-multiplier-bound c C = SQ.elimProp
    (λ a → isPropΠ (λ B → isPropΠ (λ Ch → isPropΠ (λ Bh → isPropΠ (λ hc → isPropΠ
      (λ bound → completion-magnitude-isProp (preferredCompletionMultiplication (embedMetricℚ c) a) (C Q.· B)))))))
    (λ x B Ch Bh hc bound → rational-limit-magnitude
      (λ n → c Q.· approximation x (suc n))
      (preferredCompletionMultiplication (embedMetricℚ c) SQ.[ x ]) (C Q.· B)
      (rational-product-sequence-converges c (λ n → approximation x (suc n)) SQ.[ x ] (rational-approximants-converge x))
      (λ k → PT.map (λ { (threshold , hb) → threshold , λ n hn →
        A.weakenMagnitudeBound (c Q.· approximation x (suc n)) (C Q.· (B Q.+ precision (errorOffset C N.+ k)))
          ((C Q.· B) Q.+ precision k)
          (arbitrary-multiplier-bound c C (approximation x (suc n)) (B Q.+ precision (errorOffset C N.+ k))
            Ch (subst (_≤ B Q.+ precision (errorOffset C N.+ k)) (Q.+IdL 0)
              (≤Monotone+ 0 B 0 (precision (errorOffset C N.+ k)) Bh (precision-nonnegative (errorOffset C N.+ k))))
            hc (hb (suc n) (NO.≤-trans hn NO.≤-sucℕ)))
          (subst (_≤ (C Q.· B) Q.+ precision k) (sym (Q.·DistL+ C B (precision (errorOffset C N.+ k))))
            (≤Monotone+ (C Q.· B) (C Q.· B) (C Q.· precision (errorOffset C N.+ k)) (precision k)
              (isRefl≤ (C Q.· B))
              (A.scaledCoefficientAbsorption C (errorOffset C) k (dominates (Auto.preferredExponent C))))) })
        (completion-bound-representative x B bound (errorOffset C N.+ k))))
