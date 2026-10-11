{-# OPTIONS --safe --cubical --guardedness #-}
module TickCompletionRingContinuity where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Data.Nat as Nat using (ℕ; zero; suc; max)
import Cubical.Data.Nat.Order as N
open import Cubical.Data.Sigma using (Σ)
open import Cubical.HITs.PropositionalTruncation as PT
import Cubical.HITs.SetQuotients as SQ
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyAddition
open import CauchyAdditionCongruence
open import CauchyNegation
open import CauchyRationalDensity using (eventuallyWithin-weaken)
open import CanonicalDyadicallyBoundedCauchy
open import CanonicalRegularMultiplication
open import CauchyProductCongruence using (bounded-product-preserves-eventual)
open import CauchyCompletionMultiplication
open import TickCompletionMetric
open import TickLocalRadiusBound

JointMetricContinuous : (MetricCompletionCandidate → MetricCompletionCandidate → MetricCompletionCandidate) → Type
JointMetricContinuous F = (a b : MetricCompletionCandidate) (k : ℕ) →
  ∥ Σ ℕ (λ l → (a′ b′ : MetricCompletionCandidate) →
    CompletionWithin a a′ l → CompletionWithin b b′ l → CompletionWithin (F a b) (F a′ b′) k) ∥₁

negate-eventual : (x y : RegularCauchy) (k : ℕ) → EventuallyWithin x y k →
  EventuallyWithin (negateRegular x) (negateRegular y) k
negate-eventual x y k = PT.map λ { (n₀ , bounds) → n₀ , λ n hn →
  negate-one-error-bound (approximation y n) (approximation x n) (precision k) (snd (bounds n hn)) ,
  negate-one-error-bound (approximation x n) (approximation y n) (precision k) (fst (bounds n hn)) }

within-negate : (a b : MetricCompletionCandidate) (k : ℕ) → CompletionWithin a b k →
  CompletionWithin (-completion a) (-completion b) k
within-negate a b k = PT.map λ { (x , y , px , py , h) →
  negateRegular x , negateRegular y , cong -completion_ px , cong -completion_ py , negate-eventual x y k h }

within-add : (a a′ b b′ : MetricCompletionCandidate) (k : ℕ) →
  CompletionWithin a a′ (suc k) → CompletionWithin b b′ (suc k) →
  CompletionWithin (a +completion b) (a′ +completion b′) k
within-add a a′ b b′ k = PT.rec (isPropΠ λ _ → isPropPropTrunc)
  λ { (x , x′ , px , px′ , hx) → PT.map λ { (y , y′ , py , py′ , hy) →
    addRegular x y , addRegular x′ y′ , cong₂ _+completion_ px py , cong₂ _+completion_ px′ py′ ,
    addRegular-preserves-eventual x x′ y y′ k hx hy } }

addition-joint-continuous : JointMetricContinuous _+completion_
addition-joint-continuous a b k = ∣ suc k , (λ a′ b′ → within-add a a′ b b′ k) ∣₁

negation-metric-continuous : MetricContinuous -completion_
negation-metric-continuous a k = ∣ k , (λ b → within-negate a b k) ∣₁

lift-local-binary-continuity :
  (f : RegularCauchy → RegularCauchy → RegularCauchy)
  (F : MetricCompletionCandidate → MetricCompletionCandidate → MetricCompletionCandidate) →
  ((x y : RegularCauchy) → SQ.[ f x y ] ≡ F SQ.[ x ] SQ.[ y ]) →
  (depth : RegularCauchy → RegularCauchy → ℕ → ℕ) →
  ((x y x′ y′ : RegularCauchy) (k : ℕ) →
    EventuallyWithin x x′ (depth x y k) → EventuallyWithin y y′ (depth x y k) →
    EventuallyWithin (f x y) (f x′ y′) k) → JointMetricContinuous F
lift-local-binary-continuity f F bridge depth preserves = SQ.elimProp2
  (λ a b → isPropΠ λ k → isPropPropTrunc)
  (λ x y k → ∣ suc (suc (depth x y k)) ,
    SQ.elimProp2 (λ a′ b′ → isPropΠ λ hx → isPropΠ λ hy → isPropPropTrunc)
      (λ x′ y′ hx hy → subst2 (λ a b → CompletionWithin a b k) (bridge x y) (bridge x′ y′)
        (within-intro (f x y) (f x′ y′) k
          (preserves x y x′ y′ k
            (within-representatives x x′ (depth x y k) hx)
            (within-representatives y y′ (depth x y k) hy)))) ∣₁)

product-local-depth : RegularCauchy → RegularCauchy → ℕ → ℕ
product-local-depth x y k = suc (nearbyExponent x Nat.+ nearbyExponent y) Nat.+ suc (suc (suc k))

-- The radius and input precision depend only on the two centers. Nearby
-- canonical presentations, including their early samples, have bounded radii.
product-local-preserves : (x y x′ y′ : RegularCauchy) (k : ℕ) →
  EventuallyWithin x x′ (product-local-depth x y k) → EventuallyWithin y y′ (product-local-depth x y k) →
  EventuallyWithin (canonicalRegularProduct x y) (canonicalRegularProduct x′ y′) k
product-local-preserves x y x′ y′ k hx hy = bounded-product-preserves-eventual
  (canonicalDyadicallyBounded x) (canonicalDyadicallyBounded x′)
  (canonicalDyadicallyBounded y) (canonicalDyadicallyBounded y′) k
  (eventuallyWithin-weaken x x′ leftDepth (product-local-depth x y k) left≤ hx)
  (eventuallyWithin-weaken y y′ rightDepth (product-local-depth x y k) right≤ hy)
  where
  dx = canonicalDyadicExponent x
  dx′ = canonicalDyadicExponent x′
  dy = canonicalDyadicExponent y
  dy′ = canonicalDyadicExponent y′
  ex = nearbyExponent x
  ey = nearbyExponent y
  x′≤ : N._≤_ dx′ ex
  x′≤ = nearby-exponent-bound x x′ (eventuallyWithin-weaken x x′ zero (product-local-depth x y k) N.zero-≤ hx)
  y′≤ : N._≤_ dy′ ey
  y′≤ = nearby-exponent-bound y y′ (eventuallyWithin-weaken y y′ zero (product-local-depth x y k) N.zero-≤ hy)
  leftDepth rightDepth : ℕ
  leftDepth = suc (Nat.max dx dx′ Nat.+ Nat.max dy dy) Nat.+ suc (suc (suc k))
  rightDepth = suc (Nat.max dx′ dx′ Nat.+ Nat.max dy dy′) Nat.+ suc (suc (suc k))
  left≤ : N._≤_ leftDepth (product-local-depth x y k)
  left≤ = N.≤-+k (N.suc-≤-suc (N.≤-+-≤
    (max-bounded dx dx′ ex (center-exponent≤nearby x) x′≤)
    (max-bounded dy dy ey (center-exponent≤nearby y) (center-exponent≤nearby y))))
  right≤ : N._≤_ rightDepth (product-local-depth x y k)
  right≤ = N.≤-+k (N.suc-≤-suc (N.≤-+-≤
    (max-bounded dx′ dx′ ex x′≤ x′≤)
    (max-bounded dy dy′ ey (center-exponent≤nearby y) y′≤)))

multiplication-joint-continuous : JointMetricContinuous preferredCompletionMultiplication
multiplication-joint-continuous = lift-local-binary-continuity
  canonicalRegularProduct preferredCompletionMultiplication canonicalRegularProductClass
  product-local-depth product-local-preserves

identity-metric-continuous : MetricContinuous (λ a → a)
identity-metric-continuous a k = ∣ k , (λ b h → h) ∣₁

constant-metric-continuous : (a : MetricCompletionCandidate) → MetricContinuous (λ _ → a)
constant-metric-continuous a b k = ∣ zero , (λ c h → within-refl a k) ∣₁

joint-compose-continuous :
  (F : MetricCompletionCandidate → MetricCompletionCandidate → MetricCompletionCandidate)
  (f g : MetricCompletionCandidate → MetricCompletionCandidate) →
  JointMetricContinuous F → MetricContinuous f → MetricContinuous g → MetricContinuous (λ a → F (f a) (g a))
joint-compose-continuous F f g FC fc gc a k = PT.rec isPropPropTrunc
  (λ { (l , hl) → PT.rec isPropPropTrunc
    (λ { (m , hm) → PT.map (λ { (n , hn) → Nat.max m n , λ b h →
      hl (f b) (g b)
        (hm b (within-weaken a b m (Nat.max m n) N.left-≤-max h))
        (hn b (within-weaken a b n (Nat.max m n) N.right-≤-max h)) }) (gc a l) }) (fc a l) })
  (FC (f a) (g a) k)
