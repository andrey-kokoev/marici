{-# OPTIONS --safe --cubical --guardedness #-}
module TickCompletionLimits where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Data.Nat as Nat using (ℕ; zero; suc; max)
import Cubical.Data.Nat.Order as N
open import Cubical.Data.Sigma using (Σ)
import Cubical.Data.Rationals as Q
open import Cubical.HITs.PropositionalTruncation as PT
import Cubical.HITs.SetQuotients as SQ
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyRationalDensity using (rational-approximation-eventually-within)
open import TickCompletionMetric
open import TickCompletionRingContinuity

Eventually : (ℕ → Type) → Type
Eventually P = ∥ Σ ℕ (λ n₀ → (n : ℕ) → N._≤_ n₀ n → P n) ∥₁

eventually-map : {P Q : ℕ → Type} → ((n : ℕ) → P n → Q n) → Eventually P → Eventually Q
eventually-map f = PT.map λ { (n₀ , h) → n₀ , λ n hn → f n (h n hn) }

eventually-zip : {P Q R : ℕ → Type} → ((n : ℕ) → P n → Q n → R n) →
  Eventually P → Eventually Q → Eventually R
eventually-zip f = PT.rec (isPropΠ λ _ → isPropPropTrunc)
  λ { (m , hm) → PT.map λ { (n , hn) → Nat.max m n , λ j hj →
    f j (hm j (N.≤-trans N.left-≤-max hj)) (hn j (N.≤-trans N.right-≤-max hj)) } }

eventually-constant : {P : Type} → isProp P → Eventually (λ _ → P) → P
eventually-constant prop = PT.rec prop λ { (n , h) → h n N.≤-refl }

Converges : (ℕ → MetricCompletionCandidate) → MetricCompletionCandidate → Type
Converges u a = (k : ℕ) → Eventually (λ n → CompletionWithin a (u n) k)

AsymptoticallyClose : (ℕ → MetricCompletionCandidate) → (ℕ → MetricCompletionCandidate) → Type
AsymptoticallyClose u v = (k : ℕ) → Eventually (λ n → CompletionWithin (u n) (v n) k)

constant-converges : (a : MetricCompletionCandidate) → Converges (λ _ → a) a
constant-converges a k = ∣ zero , (λ n hn → within-refl a k) ∣₁

continuous-limit : (f : MetricCompletionCandidate → MetricCompletionCandidate) → MetricContinuous f →
  (u : ℕ → MetricCompletionCandidate) (a : MetricCompletionCandidate) → Converges u a → Converges (λ n → f (u n)) (f a)
continuous-limit f fc u a h k = PT.rec isPropPropTrunc
  (λ { (l , hl) → eventually-map (λ n → hl (u n)) (h l) }) (fc a k)

joint-continuous-limit :
  (F : MetricCompletionCandidate → MetricCompletionCandidate → MetricCompletionCandidate) → JointMetricContinuous F →
  (u v : ℕ → MetricCompletionCandidate) (a b : MetricCompletionCandidate) →
  Converges u a → Converges v b → Converges (λ n → F (u n) (v n)) (F a b)
joint-continuous-limit F FC u v a b ha hb k = PT.rec isPropPropTrunc
  (λ { (l , hl) → eventually-zip (λ n → hl (u n) (v n)) (ha l) (hb l) }) (FC a b k)

converges-pointwise-path : (u v : ℕ → MetricCompletionCandidate) (a : MetricCompletionCandidate) →
  ((n : ℕ) → u n ≡ v n) → Converges u a → Converges v a
converges-pointwise-path u v a p h k = eventually-map (λ n → subst (λ b → CompletionWithin a b k) (p n)) (h k)

pointwise-close : (u v : ℕ → MetricCompletionCandidate) → ((n : ℕ) → u n ≡ v n) → AsymptoticallyClose u v
pointwise-close u v p k = ∣ zero , (λ n hn → subst (λ b → CompletionWithin (u n) b k) (p n) (within-refl (u n) k)) ∣₁

close-limits-equal : (u v : ℕ → MetricCompletionCandidate) (a b : MetricCompletionCandidate) →
  Converges u a → Converges v b → AsymptoticallyClose u v → a ≡ b
close-limits-equal u v a b ha hb huv = within-separated a b λ k → eventually-constant isPropPropTrunc
  (eventually-zip (λ n au ub → within-triangle a (u n) b k au ub) (ha (suc (suc (suc k))))
    (eventually-zip (λ n uv bv → within-triangle (u n) (v n) b (suc (suc (suc k)))
      uv (within-sym b (v n) (suc (suc (suc (suc (suc (suc k)))))) bv))
      (huv (suc (suc (suc (suc (suc (suc k))))))) (hb (suc (suc (suc (suc (suc (suc k)))))))))

rational-approximants : RegularCauchy → ℕ → MetricCompletionCandidate
rational-approximants x n = embedMetricℚ (approximation x (suc n))

rational-approximants-converge : (x : RegularCauchy) → Converges (rational-approximants x) SQ.[ x ]
rational-approximants-converge x k = ∣ k , (λ n hn → within-sym (rational-approximants x n) SQ.[ x ] k
  (within-intro (constantCauchy (approximation x (suc n))) x k
    (rational-approximation-eventually-within x k (suc n) (N.suc-≤-suc hn)))) ∣₁

-- Density and metric continuity, not path equality used as a topology.
continuous-agree-on-rationals : (f g : MetricCompletionCandidate → MetricCompletionCandidate) →
  MetricContinuous f → MetricContinuous g → ((q : Q.ℚ) → f (embedMetricℚ q) ≡ g (embedMetricℚ q)) →
  (a : MetricCompletionCandidate) → f a ≡ g a
continuous-agree-on-rationals f g fc gc h = SQ.elimProp (λ a → metric-candidate-isSet (f a) (g a))
  λ x → close-limits-equal (λ n → f (rational-approximants x n)) (λ n → g (rational-approximants x n)) (f SQ.[ x ]) (g SQ.[ x ])
    (continuous-limit f fc (rational-approximants x) SQ.[ x ] (rational-approximants-converge x))
    (continuous-limit g gc (rational-approximants x) SQ.[ x ] (rational-approximants-converge x))
    (pointwise-close (λ n → f (rational-approximants x n)) (λ n → g (rational-approximants x n))
      (λ n → h (approximation x (suc n))))
