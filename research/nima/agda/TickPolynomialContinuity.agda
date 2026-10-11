{-# OPTIONS --safe --cubical --guardedness #-}
module TickPolynomialContinuity where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels using (isPropΠ)
open import Cubical.Data.Nat as ℕ using (ℕ; zero; suc; max; _+_)
import Cubical.Data.Nat.Order as Order
open import Cubical.HITs.PropositionalTruncation as PT
open import Cubical.HITs.SetQuotients using ([_])
open import CauchyMetricEquivalence
open import CauchyRationalDensity using (eventuallyWithin-weaken)
open import CauchyAdditionCongruence
open import CauchyNegation
open import CauchyQuantitativeContinuity using (preservesEventuallyWithin)
open import CauchyCompletionCommRing using (oneCompletion)
open import CauchyCompletionMultiplication
open import DyadicallyBoundedCauchy
open import DyadicallyBoundedCauchyAddition
open import DyadicallyBoundedCauchyNegation
open import TickCompletionContinuity using (negate-continuous)
open import TickBoundedProductContinuity

weaken : {d k m : ℕ} {u v : MetricCompletionCandidate}
  → Order._≤_ k m → BoundedNear d m u v → BoundedNear d k u v
weaken {k = k} {m = m} le = PT.map
  λ { (x , y , dx , dy , px , py , h) →
    x , y , dx , dy , px , py , eventuallyWithin-weaken (regular x) (regular y) k m le h }

add-near : (d e k : ℕ) (u u′ v v′ : MetricCompletionCandidate)
  → BoundedNear d (suc k) u u′ → BoundedNear e (suc k) v v′
  → BoundedNear (suc (d + e)) k (u +completion v) (u′ +completion v′)
add-near d e k u u′ v v′ = PT.rec (isPropΠ λ _ → isPropPropTrunc)
  λ { (x , x′ , dx , dx′ , px , px′ , hx) → PT.map
    λ { (y , y′ , ey , ey′ , py , py′ , hy) →
      addDyadicallyBounded x y , addDyadicallyBounded x′ y′ ,
      cong suc (cong₂ _+_ dx ey) , cong suc (cong₂ _+_ dx′ ey′) ,
      cong₂ _+completion_ px py , cong₂ _+completion_ px′ py′ ,
      addRegular-preserves-eventual (regular x) (regular x′) (regular y) (regular y′) k hx hy } }

negate-near : (d k : ℕ) (u v : MetricCompletionCandidate)
  → BoundedNear d k u v → BoundedNear d k (-completion u) (-completion v)
negate-near d k u v = PT.map
  λ { (x , y , dx , dy , px , py , h) →
    negateDyadicallyBounded x , negateDyadicallyBounded y , dx , dy ,
    cong -completion_ px , cong -completion_ py ,
    preservesEventuallyWithin negate-continuous (regular x) (regular y) k h }

one-near : (k : ℕ) → BoundedNear zero k oneCompletion oneCompletion
one-near k = ∣ boundedOne , boundedOne , refl , refl , refl , refl ,
  ≈metric-refl (regular boundedOne) k ∣₁

-- A syntax-directed proof for finite polynomial circuits over completion
-- scalars. Precision demand is computed for each input variable separately.
module Circuit (Var : Type) where
  data Expr : Type where
    input : Var → Expr
    one : Expr
    plus times : Expr → Expr → Expr
    negative : Expr → Expr

  eval : Expr → (Var → MetricCompletionCandidate) → MetricCompletionCandidate
  eval (input i) env = env i
  eval one env = oneCompletion
  eval (plus f g) env = eval f env +completion eval g env
  eval (times f g) env = preferredCompletionMultiplication (eval f env) (eval g env)
  eval (negative f) env = -completion (eval f env)

  radius : Expr → (Var → ℕ) → ℕ
  radius (input i) bounds = bounds i
  radius one bounds = zero
  radius (plus f g) bounds = suc (radius f bounds + radius g bounds)
  radius (times f g) bounds = radius f bounds + radius g bounds
  radius (negative f) bounds = radius f bounds

  demand : Expr → (Var → ℕ) → ℕ → Var → ℕ
  demand (input i) bounds k j = k
  demand one bounds k j = zero
  demand (plus f g) bounds k j = max (demand f bounds (suc k) j) (demand g bounds (suc k) j)
  demand (times f g) bounds k j =
    let p = product-precision (radius f bounds) (radius g bounds) k
    in max (demand f bounds p j) (demand g bounds p j)
  demand (negative f) bounds k j = demand f bounds k j

  continuous : (f : Expr) (bounds : Var → ℕ) (k : ℕ)
    (env env′ : Var → MetricCompletionCandidate)
    → ((i : Var) → BoundedNear (bounds i) (demand f bounds k i) (env i) (env′ i))
    → BoundedNear (radius f bounds) k (eval f env) (eval f env′)
  continuous (input i) bounds k env env′ h = h i
  continuous one bounds k env env′ h = one-near k
  continuous (plus f g) bounds k env env′ h =
    add-near (radius f bounds) (radius g bounds) k _ _ _ _
      (continuous f bounds (suc k) env env′ (λ i → weaken {k = demand f bounds (suc k) i} {m = demand (plus f g) bounds k i} Order.left-≤-max (h i)))
      (continuous g bounds (suc k) env env′ (λ i → weaken {k = demand g bounds (suc k) i} {m = demand (plus f g) bounds k i} Order.right-≤-max (h i)))
  continuous (times f g) bounds k env env′ h =
    let p = product-precision (radius f bounds) (radius g bounds) k
    in product-retains-bounded-near (radius f bounds) (radius g bounds) k _ _ _ _
      (continuous f bounds p env env′ (λ i → weaken {k = demand f bounds p i} {m = demand (times f g) bounds k i} Order.left-≤-max (h i)))
      (continuous g bounds p env env′ (λ i → weaken {k = demand g bounds p i} {m = demand (times f g) bounds k i} Order.right-≤-max (h i)))
  continuous (negative f) bounds k env env′ h =
    negate-near (radius f bounds) k _ _ (continuous f bounds k env env′ h)
