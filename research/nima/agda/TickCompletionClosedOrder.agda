{-# OPTIONS --safe --cubical --guardedness #-}
module TickCompletionClosedOrder where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Data.Nat using (ℕ; suc)
import Cubical.Data.Nat.Order as N
open import Cubical.Data.Sigma using (Σ; _×_)
open import Cubical.HITs.PropositionalTruncation as PT
import Cubical.HITs.SetQuotients as SQ
import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyProductBounds
open import CauchyAdditionCongruence using (_+completion_)
open import CauchyNegation using (-completion_)
open import TickCompletionMetric
open import TickCompletionDerivative
open import TickCompletionLimits
open import TickCompletionRingContinuity
open import TickCompletionOrderLimits

abstract
  -- Completion-valued, not just rational, limits preserve the closed cone.
  -- Each tolerance chooses one sequence value and one representative only.
  completion-limit-nonnegative : (u : ℕ → MetricCompletionCandidate) (a : MetricCompletionCandidate) →
    Converges u a → Eventually (λ n → CompletionNonnegative (u n)) → CompletionNonnegative a
  completion-limit-nonnegative u = SQ.elimProp
    (λ a → isPropΠ (λ _ → isPropΠ (λ _ → completion-nonnegative-isProp a)))
    (λ x converges positive k → PT.rec isPropPropTrunc
      (λ { (threshold , evidence) →
        let n = threshold
            near = fst (evidence n N.≤-refl)
            nonnegative = snd (evidence n N.≤-refl)
        in PT.rec isPropPropTrunc (λ { (y , path , lower) →
          PT.map (λ bound → x , refl , ∣ bound ∣₁)
            (eventually-zip (λ j comparison lower-bound →
              subst (λ e → Q.- e ≤ approximation x j) (precision-refines-double k)
                (lower-transfer (approximation y j) (approximation x j) (precision (suc k))
                  lower-bound (snd comparison)))
              (within-representatives x y (suc k)
                (subst (λ b → CompletionWithin SQ.[ x ] b (suc (suc (suc k)))) (sym path) near))
              lower) }) (nonnegative (suc k)) })
      (eventually-zip (λ n near positive → near , positive)
        (converges (suc (suc (suc k)))) positive))

  completion-limit-order : (u v : ℕ → MetricCompletionCandidate) (a b : MetricCompletionCandidate) →
    Converges u a → Converges v b → Eventually (λ n → CompletionLE (u n) (v n)) → CompletionLE a b
  completion-limit-order u v a b hu hv = completion-limit-nonnegative
    (λ n → v n +completion (-completion (u n))) (b +completion (-completion a))
    (joint-continuous-limit _+completion_ addition-joint-continuous
      v (λ n → -completion (u n)) b (-completion a) hv
      (continuous-limit -completion_ negation-metric-continuous u a hu))

  -- Two independent moving inputs. The domain condition is only eventual,
  -- so approximants can use a larger rational radius than the limiting ball.
  joint-continuous-order-limit :
    (F G : MetricCompletionCandidate → MetricCompletionCandidate → MetricCompletionCandidate) →
    JointMetricContinuous F → JointMetricContinuous G →
    (u v : ℕ → MetricCompletionCandidate) (a b : MetricCompletionCandidate) →
    Converges u a → Converges v b →
    Eventually (λ n → CompletionLE (F (u n) (v n)) (G (u n) (v n))) →
    CompletionLE (F a b) (G a b)
  joint-continuous-order-limit F G fc gc u v a b hu hv = completion-limit-order
    (λ n → F (u n) (v n)) (λ n → G (u n) (v n)) (F a b) (G a b)
    (joint-continuous-limit F fc u v a b hu hv)
    (joint-continuous-limit G gc u v a b hu hv)

  bounded-rational-order-density :
    (F G : MetricCompletionCandidate → MetricCompletionCandidate → MetricCompletionCandidate) →
    JointMetricContinuous F → JointMetricContinuous G →
    (P d : Q.ℚ) →
    ((p h : Q.ℚ) → MagnitudeBound p P → MagnitudeBound h d →
      CompletionLE (F (embedMetricℚ p) (embedMetricℚ h)) (G (embedMetricℚ p) (embedMetricℚ h))) →
    (x y : RegularCauchy) →
    Eventually (λ n → MagnitudeBound (approximation x (suc n)) P) →
    Eventually (λ n → MagnitudeBound (approximation y (suc n)) d) →
    CompletionLE (F SQ.[ x ] SQ.[ y ]) (G SQ.[ x ] SQ.[ y ])
  bounded-rational-order-density F G fc gc P d rational-bound x y hx hy =
    joint-continuous-order-limit F G fc gc (rational-approximants x) (rational-approximants y)
      SQ.[ x ] SQ.[ y ] (rational-approximants-converge x) (rational-approximants-converge y)
      (eventually-zip (λ n px hy → rational-bound (approximation x (suc n)) (approximation y (suc n)) px hy) hx hy)
