{-# OPTIONS --safe --cubical --guardedness #-}
module TickCompletionMagnitudeBounds where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Data.Nat using (ℕ; suc)
import Cubical.Data.Nat.Order as NO
open import Cubical.Data.Sigma using (Σ; _×_)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.HITs.PropositionalTruncation as PT
import Cubical.HITs.SetQuotients as SQ
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyProductBounds
open import CauchyNegation using (negate-one-error-bound)
open import MetricCompletionEffectiveness using (quotientPathToMetric)
open import CauchyProductErrorBounds using (weaken-magnitude-bound)
open import TaylorRegularityComposition using (magnitude-bound-forward; magnitude-bound-backward)
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate using (PreferredℚCommRing)
open import TickCompletionMetric
open import TickCompletionLimits
open import TickRationalProductLimits
open import CauchyAdditionCongruence using (_+completion_)

-- A closed bound on the actual quotient, with arbitrarily small rational
-- slack. Representatives are existential: no boundary-sensitive predicate
-- is incorrectly descended at a fixed precision.
RepresentativeMagnitudeBound : MetricCompletionCandidate → Q.ℚ → Type
RepresentativeMagnitudeBound a r = (k : ℕ) → ∥ Σ RegularCauchy (λ x →
  (SQ.[ x ] ≡ a) × Eventually (λ n → MagnitudeBound (approximation x n) (r Q.+ precision k))) ∥₁

abstract
  CompletionMagnitudeBound : MetricCompletionCandidate → Q.ℚ → Type
  CompletionMagnitudeBound = RepresentativeMagnitudeBound

  completion-magnitude-definition : (a : MetricCompletionCandidate) (r : Q.ℚ) →
    CompletionMagnitudeBound a r ≡ RepresentativeMagnitudeBound a r
  completion-magnitude-definition a r = refl

  completion-magnitude-isProp : (a : MetricCompletionCandidate) (r : Q.ℚ) →
    isProp (CompletionMagnitudeBound a r)
  completion-magnitude-isProp a r = isPropΠ (λ _ → isPropPropTrunc)

-- Transfer a rational bound through a directed representative comparison.
approximation-bound : (a b r e : Q.ℚ) →
  a ≤ b Q.+ e → b ≤ a Q.+ e → MagnitudeBound b r → MagnitudeBound a (r Q.+ e)
approximation-bound a b r e ab ba h .positive-upper =
  isTrans≤ a (b Q.+ e) (r Q.+ e) ab (≤-+o b r e (positive-upper h))
approximation-bound a b r e ab ba h .negative-upper =
  isTrans≤ (Q.- a) ((Q.- b) Q.+ e) (r Q.+ e)
    (negate-one-error-bound b a e ba) (≤-+o (Q.- b) r e (negative-upper h))

module ZeroPaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; -_ to -S_)
  difference-zero : (a : fst R) → a +S (-S 0r) ≡ a
  difference-zero a = solve! R
  sum-budget : (a b p : fst R) → (a +S p) +S (b +S p) ≡ (a +S b) +S (p +S p)
  sum-budget a b p = solve! R

abstract
  completion-bound-path : (a b : MetricCompletionCandidate) (B : Q.ℚ) → a ≡ b →
    CompletionMagnitudeBound a B → CompletionMagnitudeBound b B
  completion-bound-path a b B p h = subst (λ z → CompletionMagnitudeBound z B) p h

  completion-remainder-bound-path : (a b : MetricCompletionCandidate) (c B : Q.ℚ) → a ≡ b →
    CompletionMagnitudeBound (a +completion embedMetricℚ c) B →
    CompletionMagnitudeBound (b +completion embedMetricℚ c) B
  completion-remainder-bound-path a b c B p h = subst
    (λ z → CompletionMagnitudeBound (z +completion embedMetricℚ c) B) p h

  rational-limit-magnitude : (r : ℕ → Q.ℚ) (a : MetricCompletionCandidate) (B : Q.ℚ) →
    Converges (λ n → embedMetricℚ (r n)) a →
    ((k : ℕ) → Eventually (λ n → MagnitudeBound (r n) (B Q.+ precision k))) →
    CompletionMagnitudeBound a B
  rational-limit-magnitude r = SQ.elimProp
    (λ a → isPropΠ (λ B → isPropΠ (λ h → isPropΠ (λ bounds → completion-magnitude-isProp a B))))
    (λ x B h bounds k → PT.rec isPropPropTrunc
      (λ { (threshold , evidence) →
        let n = threshold
            near = fst (evidence n NO.≤-refl)
            bounded = snd (evidence n NO.≤-refl)
        in PT.map (λ { (t , comparison) →
          x , refl , ∣ t , (λ j hj → subst (MagnitudeBound (approximation x j))
            (sym (Q.+Assoc B (precision (suc k)) (precision (suc k)))
              ∙ cong (B Q.+_) (precision-refines-double k))
            (approximation-bound (approximation x j) (r n) (B Q.+ precision (suc k)) (precision (suc k))
              (fst (comparison j hj)) (snd (comparison j hj)) bounded)) ∣₁ })
          (within-representatives x (constantCauchy (r n)) (suc k) near) })
      (eventually-zip (λ n near bounded → near , bounded)
        (h (suc (suc (suc k)))) (bounds (suc k))))

  embedded-magnitude-bound : (q B : Q.ℚ) → MagnitudeBound q B → CompletionMagnitudeBound (embedMetricℚ q) B
  embedded-magnitude-bound q B h = rational-limit-magnitude (λ _ → q) (embedMetricℚ q) B
    (constant-converges (embedMetricℚ q)) (λ k → eventually-map
      (λ n hn → weaken-magnitude-bound q B (B Q.+ precision k)
        (≤-add-nonnegative B (precision k) (precision-nonnegative k)) h)
      (constant-converges (embedMetricℚ q) k))

  completion-bound-representative : (x : RegularCauchy) (B : Q.ℚ) →
    CompletionMagnitudeBound SQ.[ x ] B →
    (k : ℕ) → Eventually (λ n → MagnitudeBound (approximation x n) (B Q.+ precision k))
  completion-bound-representative x B bound k = PT.rec isPropPropTrunc
    (λ { (y , path , bounded) →
      PT.rec isPropPropTrunc (λ { (threshold , comparison) →
        eventually-zip (λ n hb hn → subst (MagnitudeBound (approximation x n))
          (sym (Q.+Assoc B (precision (suc k)) (precision (suc k)))
            ∙ cong (B Q.+_) (precision-refines-double k))
          (approximation-bound (approximation x n) (approximation y n) (B Q.+ precision (suc k)) (precision (suc k))
            (fst (comparison n hn)) (snd (comparison n hn)) hb)) bounded
          ∣ threshold , (λ n hn → hn) ∣₁ })
        (quotientPathToMetric x y (sym path) (suc k)) })
    (bound (suc k))

  completion-limit-magnitude : (u : ℕ → MetricCompletionCandidate) (a : MetricCompletionCandidate) (B : Q.ℚ) →
    Converges u a →
    ((k : ℕ) → Eventually (λ n → CompletionMagnitudeBound (u n) (B Q.+ precision k))) →
    CompletionMagnitudeBound a B
  completion-limit-magnitude u = SQ.elimProp
    (λ a → isPropΠ (λ B → isPropΠ (λ h → isPropΠ (λ bounds → completion-magnitude-isProp a B))))
    (λ x B h bounds k → PT.rec isPropPropTrunc
      (λ { (threshold , evidence) →
        let n = threshold
            near = fst (evidence n NO.≤-refl)
            bounded = snd (evidence n NO.≤-refl)
        in PT.rec isPropPropTrunc
          (λ { (y , path , hb) → PT.map (λ { (t , comparison) →
            x , refl , eventually-zip (λ j hj hy → subst (MagnitudeBound (approximation x j))
              (cong (Q._+ precision (suc k))
                (sym (Q.+Assoc B (precision (suc (suc k))) (precision (suc (suc k))))
                  ∙ cong (B Q.+_) (precision-refines-double (suc k)))
                ∙ sym (Q.+Assoc B (precision (suc k)) (precision (suc k)))
                ∙ cong (B Q.+_) (precision-refines-double k))
              (approximation-bound (approximation x j) (approximation y j)
                ((B Q.+ precision (suc (suc k))) Q.+ precision (suc (suc k))) (precision (suc k))
                (fst (comparison j hj)) (snd (comparison j hj)) hy))
              ∣ t , (λ j hj → hj) ∣₁ hb })
            (within-representatives x y (suc k)
              (subst (λ b → CompletionWithin SQ.[ x ] b (suc (suc (suc k)))) (sym path) near)) })
          (bounded (suc (suc k))) })
      (eventually-zip (λ n near bounded → near , bounded)
        (h (suc (suc (suc k)))) (bounds (suc (suc k)))))

  completion-magnitude-add : (a b : MetricCompletionCandidate) (A B : Q.ℚ) →
    CompletionMagnitudeBound a A → CompletionMagnitudeBound b B →
    CompletionMagnitudeBound (a +completion b) (A Q.+ B)
  completion-magnitude-add = SQ.elimProp2
    (λ a b → isPropΠ (λ A → isPropΠ (λ B → isPropΠ (λ ha → isPropΠ
      (λ hb → completion-magnitude-isProp (a +completion b) (A Q.+ B))))))
    (λ x y A B ha hb → rational-limit-magnitude
      (λ n → approximation x (suc n) Q.+ approximation y (suc n)) (SQ.[ x ] +completion SQ.[ y ]) (A Q.+ B)
      (rational-sum-sequence-converges (λ n → approximation x (suc n)) (λ n → approximation y (suc n))
        SQ.[ x ] SQ.[ y ] (rational-approximants-converge x) (rational-approximants-converge y))
      (λ k → PT.map (λ { (threshold , bounds) → threshold , λ n hn →
        subst (MagnitudeBound (approximation x (suc n) Q.+ approximation y (suc n)))
          (ZeroPaths.sum-budget PreferredℚCommRing A B (precision (suc k))
            ∙ cong ((A Q.+ B) Q.+_) (precision-refines-double k))
          (add-magnitude-bounds (approximation x (suc n)) (A Q.+ precision (suc k))
            (approximation y (suc n)) (B Q.+ precision (suc k))
            (fst (bounds (suc n) (NO.≤-trans hn NO.≤-sucℕ)))
            (snd (bounds (suc n) (NO.≤-trans hn NO.≤-sucℕ)))) })
        (eventually-zip (λ n hx hy → hx , hy)
          (completion-bound-representative x A ha (suc k)) (completion-bound-representative y B hb (suc k)))))

  completion-magnitude-shrinks : (a : MetricCompletionCandidate) →
    ((k : ℕ) → CompletionMagnitudeBound a (precision k)) → a ≡ embedMetricℚ 0
  completion-magnitude-shrinks a bounds = within-separated a (embedMetricℚ 0) (λ k → PT.map
    (λ { (x , path , hb) → x , constantCauchy 0 , path , refl , eventually-map
      (λ n hn →
        let bounded = subst (MagnitudeBound (approximation x n)) (precision-refines-double k) hn
            difference = transport-magnitude (approximation x n Q.+ (Q.- 0)) (approximation x n) (precision k)
              (ZeroPaths.difference-zero PreferredℚCommRing (approximation x n)) bounded
        in magnitude-bound-forward (approximation x n) 0 (precision k) difference ,
           magnitude-bound-backward (approximation x n) 0 (precision k) difference) hb })
    (bounds (suc k) (suc k)))

  rational-remainder-limit-magnitude : (r : ℕ → Q.ℚ) (a : MetricCompletionCandidate) (b B : Q.ℚ) →
    Converges (λ n → embedMetricℚ (r n)) a →
    ((k : ℕ) → Eventually (λ n → MagnitudeBound (r n Q.+ (Q.- b)) (B Q.+ precision k))) →
    CompletionMagnitudeBound (a +completion embedMetricℚ (Q.- b)) B
  rational-remainder-limit-magnitude r a b B h bounds = rational-limit-magnitude
    (λ n → r n Q.+ (Q.- b)) (a +completion embedMetricℚ (Q.- b)) B
    (rational-sum-sequence-converges r (λ _ → Q.- b) a (embedMetricℚ (Q.- b))
      h (constant-converges (embedMetricℚ (Q.- b)))) bounds
