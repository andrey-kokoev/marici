{-# OPTIONS --safe --cubical --guardedness #-}
module TickSmallAngleDensity where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Data.Nat as N using (ℕ; suc; max)
import Cubical.Data.Nat.Order as NO
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import Cubical.HITs.PropositionalTruncation as PT
import Cubical.HITs.SetQuotients as SQ
open import RationalAnalyticSubstrate using (one-half; PreferredℚCommRing)
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyProductBounds
open import CauchyProductErrorBounds using (weaken-magnitude-bound)
open import TickCompletionMetric
open import TickCompletionLimits
open import TickCompletionMagnitudeBounds

module Paths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; _·_ to _·S_)
  square-slack : (e p : fst R) → (e +S p) ·S (e +S p) ≡ (e ·S e) +S p ·S ((e +S p) +S e)
  square-slack e p = solve! R
  double : (p : fst R) → p ·S (1r +S 1r) ≡ p +S p
  double p = solve! R

slackDepth : ℕ → ℕ
slackDepth k = N.max 2 (suc k)

slack-small : (e : Q.ℚ) (k : ℕ) → e ≤ precision 2 → e Q.+ precision (slackDepth k) ≤ one-half
slack-small e k he = subst ((e Q.+ precision (slackDepth k)) ≤_) (precision-refines-double 1)
  (≤Monotone+ e (precision 2) (precision (slackDepth k)) (precision 2) he
    (precision-antitone 2 (slackDepth k) (NO.left-≤-max {m = 2} {n = suc k})))

squared-slack : (e : Q.ℚ) (k : ℕ) → e ≤ precision 2 →
  (e Q.+ precision (slackDepth k)) Q.· (e Q.+ precision (slackDepth k)) ≤ (e Q.· e) Q.+ precision k
squared-slack e k he = subst (_≤ (e Q.· e) Q.+ precision k)
  (sym (Paths.square-slack PreferredℚCommRing e p))
  (≤Monotone+ (e Q.· e) (e Q.· e) (p Q.· ((e Q.+ p) Q.+ e)) (precision k)
    (isRefl≤ (e Q.· e))
    (isTrans≤ (p Q.· ((e Q.+ p) Q.+ e)) (p Q.· (1 Q.+ 1)) (precision k)
      (left-multiply-monotone p ((e Q.+ p) Q.+ e) (1 Q.+ 1) (precision-nonnegative (slackDepth k))
        (≤Monotone+ (e Q.+ p) 1 e 1
          (isTrans≤ (e Q.+ p) one-half 1 (slack-small e k he) (precision-step≤ 0))
          (isTrans≤ e (precision 2) 1 he (precision-antitone 0 2 NO.zero-≤))))
      (subst (_≤ precision k) (sym (Paths.double PreferredℚCommRing p))
        (subst ((p Q.+ p) ≤_) (precision-refines-double k)
          (≤Monotone+ p (precision (suc k)) p (precision (suc k))
            (precision-antitone (suc k) (slackDepth k) (NO.right-≤-max {n = suc k} {m = 2}))
            (precision-antitone (suc k) (slackDepth k) (NO.right-≤-max {n = suc k} {m = 2})))))))
  where p = precision (slackDepth k)

abstract
  completion-bound-weaken : (a : MetricCompletionCandidate) (A B : Q.ℚ) → A ≤ B →
    CompletionMagnitudeBound a A → CompletionMagnitudeBound a B
  completion-bound-weaken a A B h bound = subst (λ P → P)
    (sym (completion-magnitude-definition a B))
    (λ k → PT.map (λ { (x , path , hb) → x , path , eventually-map
      (λ n hn → weaken-magnitude-bound (approximation x n) (A Q.+ precision k) (B Q.+ precision k)
        (≤Monotone+ A B (precision k) (precision k) h (isRefl≤ (precision k))) hn) hb })
      (subst (λ P → P) (completion-magnitude-definition a A) bound k))

  -- Density extension with a strict working radius: e <= 1/4 leaves room
  -- for approximant slack while invoking the rational bound at radius 1/2.
  small-angle-density : (f : Q.ℚ → MetricCompletionCandidate)
    (F : MetricCompletionCandidate → MetricCompletionCandidate) → MetricContinuous F →
    ((q : Q.ℚ) → f q ≡ F (embedMetricℚ q)) →
    ((q r : Q.ℚ) → MagnitudeBound q one-half → 0 ≤ r → MagnitudeBound q r →
      CompletionMagnitudeBound (f q) (r Q.· r)) →
    (a : MetricCompletionCandidate) (e : Q.ℚ) → 0 ≤ e → e ≤ precision 2 →
    CompletionMagnitudeBound a e → CompletionMagnitudeBound (F a) (e Q.· e)
  small-angle-density f F fc path rational = SQ.elimProp
    (λ a → isPropΠ (λ e → isPropΠ (λ eh → isPropΠ (λ small → isPropΠ
      (λ bound → completion-magnitude-isProp (F a) (e Q.· e))))))
    (λ x e eh small bound → completion-limit-magnitude
      (λ n → f (approximation x (suc n))) (F SQ.[ x ]) (e Q.· e)
      (converges-pointwise-path (λ n → F (rational-approximants x n))
        (λ n → f (approximation x (suc n))) (F SQ.[ x ])
        (λ n → sym (path (approximation x (suc n))))
        (continuous-limit F fc (rational-approximants x) SQ.[ x ] (rational-approximants-converge x)))
      (λ k → PT.map (λ { (threshold , hb) → threshold , λ n hn →
        completion-bound-weaken (f (approximation x (suc n)))
          ((e Q.+ precision (slackDepth k)) Q.· (e Q.+ precision (slackDepth k)))
          ((e Q.· e) Q.+ precision k) (squared-slack e k small)
          (rational (approximation x (suc n)) (e Q.+ precision (slackDepth k))
            (weaken-magnitude-bound _ _ one-half (slack-small e k small) (hb (suc n)
              (NO.≤-trans hn NO.≤-sucℕ)))
            (subst (_≤ e Q.+ precision (slackDepth k)) (Q.+IdL 0)
              (≤Monotone+ 0 e 0 (precision (slackDepth k)) eh (precision-nonnegative (slackDepth k))))
            (hb (suc n) (NO.≤-trans hn NO.≤-sucℕ))) })
        (completion-bound-representative x e bound (slackDepth k))))
