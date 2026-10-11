{-# OPTIONS --safe --cubical --guardedness #-}
module TickCompletionMetric where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Data.Nat using (ℕ; suc; max)
import Cubical.Data.Nat.Order as N
open import Cubical.Data.Sigma using (Σ; _×_)
open import Cubical.HITs.PropositionalTruncation as PT
import Cubical.HITs.SetQuotients as SQ
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyQuantitativeContinuity
open import CauchyRationalDensity using (eventuallyWithin-weaken)
open import MetricCompletionEffectiveness

-- Existential representative balls are predicates on the actual quotient.
-- EventuallyWithin itself must NOT be descended at a fixed precision: it
-- need not be invariant under changing representatives at a boundary.
CompletionWithin : MetricCompletionCandidate → MetricCompletionCandidate → ℕ → Type
CompletionWithin a b k = ∥ Σ RegularCauchy (λ x → Σ RegularCauchy (λ y →
  (SQ.[ x ] ≡ a) × (SQ.[ y ] ≡ b) × EventuallyWithin x y k)) ∥₁

within-intro : (x y : RegularCauchy) (k : ℕ) → EventuallyWithin x y k →
  CompletionWithin SQ.[ x ] SQ.[ y ] k
within-intro x y k h = ∣ x , y , refl , refl , h ∣₁

-- Any chosen representatives recover the bound with two bits of slack.
-- Thus these balls give the ordinary rational Cauchy uniformity, not merely
-- the topology of Agda path equality.
within-representatives : (x y : RegularCauchy) (k : ℕ) →
  CompletionWithin SQ.[ x ] SQ.[ y ] (suc (suc k)) → EventuallyWithin x y k
within-representatives x y k = PT.rec isPropPropTrunc
  λ { (a , b , ax , by , h) →
    composeEventuallyWithin x a y k
      (quotientPathToMetric x a (sym ax) (suc k))
      (composeEventuallyWithin a b y (suc k) h
        (quotientPathToMetric b y by (suc (suc k)))) }

within-weaken : (a b : MetricCompletionCandidate) (k l : ℕ) → N._≤_ k l →
  CompletionWithin a b l → CompletionWithin a b k
within-weaken a b k l kl = PT.map λ { (x , y , xa , yb , h) →
  x , y , xa , yb , eventuallyWithin-weaken x y k l kl h }

within-refl : (a : MetricCompletionCandidate) (k : ℕ) → CompletionWithin a a k
within-refl = SQ.elimProp (λ a → isPropΠ λ k → isPropPropTrunc)
  (λ x k → within-intro x x k (≈metric-refl x k))

within-sym : (a b : MetricCompletionCandidate) (k : ℕ) →
  CompletionWithin a b k → CompletionWithin b a k
within-sym a b k = PT.map λ { (x , y , xa , yb , h) →
  y , x , yb , xa , eventuallyWithin-sym x y k h }

within-triangle : (a b c : MetricCompletionCandidate) (k : ℕ) →
  CompletionWithin a b (suc (suc (suc k))) →
  CompletionWithin b c (suc (suc (suc k))) → CompletionWithin a c k
within-triangle = SQ.elimProp3
  (λ a b c → isPropΠ λ k → isPropΠ λ ab → isPropΠ λ bc → isPropPropTrunc)
  (λ x y z k ab bc → within-intro x z k
    (composeEventuallyWithin x y z k
      (within-representatives x y (suc k) ab)
      (within-representatives y z (suc k) bc)))

within-separated : (a b : MetricCompletionCandidate) →
  ((k : ℕ) → CompletionWithin a b k) → a ≡ b
within-separated = SQ.elimProp2
  (λ a b → isPropΠ λ h → metric-candidate-isSet a b)
  (λ x y h → SQ.eq/ x y (λ k → within-representatives x y k (h (suc (suc k)))))

MetricContinuous : (MetricCompletionCandidate → MetricCompletionCandidate) → Type
MetricContinuous f = (a : MetricCompletionCandidate) (k : ℕ) →
  ∥ Σ ℕ (λ l → (b : MetricCompletionCandidate) →
    CompletionWithin a b l → CompletionWithin (f a) (f b) k) ∥₁

metric-continuity-isProp : (f : MetricCompletionCandidate → MetricCompletionCandidate) →
  isProp (MetricContinuous f)
metric-continuity-isProp f = isPropΠ λ a → isPropΠ λ k → isPropPropTrunc

record LocallyContinuous (f : RegularCauchy → RegularCauchy) : Type where
  field
    localModulus : RegularCauchy → ℕ → ℕ
    localPreserves : (x y : RegularCauchy) (k : ℕ) →
      EventuallyWithin x y (localModulus x k) → EventuallyWithin (f x) (f y) k
open LocallyContinuous public

-- Allows a propositional, rather than definitional, representative bridge.
lift-local-continuity : (f : RegularCauchy → RegularCauchy)
  (F : MetricCompletionCandidate → MetricCompletionCandidate) →
  ((x : RegularCauchy) → SQ.[ f x ] ≡ F SQ.[ x ]) →
  LocallyContinuous f → MetricContinuous F
lift-local-continuity f F bridge continuity = SQ.elimProp
  (λ a → isPropΠ λ k → isPropPropTrunc)
  (λ x k → ∣ suc (suc (localModulus continuity x k)) ,
    SQ.elimProp (λ b → isPropΠ λ h → isPropPropTrunc)
      (λ y h → subst2 (λ a b → CompletionWithin a b k) (bridge x) (bridge y)
        (within-intro (f x) (f y) k
          (localPreserves continuity x y k
            (within-representatives x y (localModulus continuity x k) h)))) ∣₁)

compose-metric-continuous : {f g : MetricCompletionCandidate → MetricCompletionCandidate} →
  MetricContinuous f → MetricContinuous g → MetricContinuous (λ x → f (g x))
compose-metric-continuous {f} {g} fc gc a k = PT.rec isPropPropTrunc
  (λ { (l , fl) → PT.map (λ { (m , gm) → m , λ b h → fl (g b) (gm b h) })
    (gc a l) }) (fc (g a) k)
