{-# OPTIONS --safe --cubical --guardedness #-}
module RetainedObservationFibers where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Int.Base using (ℤ; pos)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)
import Cubical.Foundations.Equiv.Fiberwise as FW
import TypedPhysicalComparisons as T
import ObservationRespectingBoundary as Boundary
import ActionChartComparison as Action

-- A may be the COMPLETE admitted source/history object, not a scalar payload.
-- No set truncation, propositional truncation, quotient, or choice of one fiber.
module Retain {ℓ ℓ'} {A : Type ℓ} {V : Type ℓ'} (r : A → V) where
  Fiber : V → Type (ℓ-max ℓ ℓ')
  Fiber v = Σ A (λ a → r a ≡ v)
  Total : Type (ℓ-max ℓ ℓ')
  Total = Σ V Fiber
  reassemble : Iso A Total
  Iso.fun reassemble a = r a , a , refl
  Iso.inv reassemble (v , a , p) = a
  Iso.rightInv reassemble (v , a , p) i = p i , a , (λ j → p (i ∧ j))
  Iso.leftInv reassemble a = refl
  source-recovered : (a : A) → Iso.inv reassemble (Iso.fun reassemble a) ≡ a
  source-recovered a = refl
  all-fiber-data-recovered : (t : Total) → Iso.fun reassemble (Iso.inv reassemble t) ≡ t
  all-fiber-data-recovered = Iso.rightInv reassemble

-- Coarsening keeps the old index AND its entire fiber as the payload.
module Regroup {ℓA ℓV ℓW} {A : Type ℓA} {V : Type ℓV} {W : Type ℓW}
  (r : A → V) (q : V → W) where
  module Original = Retain r
  module Coarse = Retain (λ (t : Original.Total) → q (fst t))
  Grouped : W → Type _
  Grouped = Coarse.Fiber
  original-index : {w : W} → Grouped w → V
  original-index t = fst (fst t)
  original-fiber-data : {w : W} (t : Grouped w) → Original.Fiber (original-index t)
  original-fiber-data t = snd (fst t)
  -- Grouped w consists of ((v,a,p:r a=v), h:q v=w).
  -- In particular neither a nor v nor either witness is discarded.
  all-groups : A ≃ Coarse.Total
  all-groups = compEquiv (isoToEquiv Original.reassemble) (isoToEquiv Coarse.reassemble)
  recovered : (a : A) → invEq all-groups (equivFun all-groups a) ≡ a
  recovered = retEq all-groups
  regrouped-data-recovered : (t : Coarse.Total)
    → equivFun all-groups (invEq all-groups t) ≡ t
  regrouped-data-recovered = secEq all-groups
  no-source-erasure : {a b : A} → equivFun all-groups a ≡ equivFun all-groups b → a ≡ b
  no-source-erasure {a} {b} p = sym (retEq all-groups a) ∙ cong (invEq all-groups) p ∙ retEq all-groups b

-- Precise criterion for a FIXED map and supplied commuting square.
module Criterion {ℓA ℓB ℓV} (A : Type ℓA) (B : Type ℓB) (V : Type ℓV)
  (r : A → V) (s : B → V) (f : A → B)
  (commutes : (a : A) → s (f a) ≡ r a) where
  module R = Retain r
  module S = Retain s
  on-fiber : (v : V) → R.Fiber v → S.Fiber v
  on-fiber v (a , p) = f a , commutes a ∙ p
  total : R.Total → S.Total
  total (v , a) = v , on-fiber v a
  forward : isEquiv f → (v : V) → isEquiv (on-fiber v)
  forward ef = FW.fiberEquiv R.Fiber S.Fiber on-fiber total-is-equiv
    where
    canonical : R.Total ≃ S.Total
    canonical = compEquiv (invEquiv (isoToEquiv R.reassemble))
      (compEquiv (f , ef) (isoToEquiv S.reassemble))
    canonical-to-total : equivFun canonical ≡ total
    canonical-to-total = funExt λ t → Iso.rightInv S.reassemble (total t)
    total-is-equiv : isEquiv total
    total-is-equiv = subst isEquiv canonical-to-total (snd canonical)
  backward : ((v : V) → isEquiv (on-fiber v)) → isEquiv f
  backward each = snd (compEquiv (isoToEquiv R.reassemble)
    (compEquiv (total , FW.totalEquiv R.Fiber S.Fiber on-fiber each)
      (invEquiv (isoToEquiv S.reassemble))))

-- Conversely, supplied equivalences on EVERY fiber reconstruct an observed
-- presentation. The marked-point requirement is explicit, not inferred merely
-- from equivalence of unmarked fibers.
module Assemble {V : Type} (X Y : T.Over.Object V)
  (each : (v : V) → Retain.Fiber (T.Over.Object.readout X) v
                     ≃ Retain.Fiber (T.Over.Object.readout Y) v) where
  module M = T.Over V
  module R = Retain (M.Object.readout X)
  module S = Retain (M.Object.readout Y)
  total-map : R.Total → S.Total
  total-map (v , x) = v , equivFun (each v) x
  total-equiv : R.Total ≃ S.Total
  total-equiv = total-map , FW.totalEquiv R.Fiber S.Fiber (λ v → equivFun (each v)) (λ v → snd (each v))
  underlying : M.Object.Carrier X ≃ M.Object.Carrier Y
  underlying = compEquiv (isoToEquiv R.reassemble)
    (compEquiv total-equiv (invEquiv (isoToEquiv S.reassemble)))
  pointed : equivFun underlying (M.Object.point X) ≡ M.Object.point Y → M.Presentation X Y
  pointed p = M.presentation (M.map (equivFun underlying) p
    (λ x → snd (equivFun (each (M.Object.readout X x)) (x , refl)))) (snd underlying)

module FromTyped {V : Type} (X Y : T.Over.Object V) (p : T.Over.Presentation V X Y) where
  module M = T.Over V
  f = M.Presentation.forward p
  module C = Criterion (M.Object.Carrier X) (M.Object.Carrier Y) V
    (M.Object.readout X) (M.Object.readout Y) (M.Map.run f) (M.Map.commutes f)
  each : (v : V) → C.R.Fiber v ≃ C.S.Fiber v
  each v = C.on-fiber v , C.forward (M.Presentation.invertible p) v
  -- The original marked comparison and commuting witnesses remain supplied.
  marked : M.Map.run f (M.Object.point X) ≡ M.Object.point Y
  marked = M.Map.marked f

module Charts (c : Action.Chart) = FromTyped
  (T.Boundary.object (Action.package Action.angle) Action.observe)
  (T.Boundary.object (Action.package c) Action.observe)
  (T.chart-presentation c)

-- The full target remains available even when the inclusion is not invertible.
-- Recovery applies to ALL target points, including off-plane points.
module FullTargetRetention = Retain {A = T.Plane.Full} fst
module PlaneCriterion = Criterion ℤ T.Plane.Full ℤ (λ x → x) fst
  (T.Plane.A.Map.run T.Plane.inclusion) (T.Plane.A.Map.commutes T.Plane.inclusion)
no-zero-fiber-equivalence : isEquiv (PlaneCriterion.on-fiber (pos 0)) → ⊥
no-zero-fiber-equivalence e = T.Plane.zero-not-one
  (cong (λ z → fst (snd (fst z)))
    (secEq (PlaneCriterion.on-fiber (pos 0) , e) ((pos 0 , pos 1 , pos 0) , refl)))

-- Every fiber is retained as an indexed type, including empty fibers. This
-- does not assert an inhabitant (or admission seed) in every fiber.
module EmptyControl where
  reader : Bool → Bool
  reader _ = false
  module R = Retain reader
  empty-fiber : R.Fiber true → ⊥
  empty-fiber x = false≢true (snd x)
  no-global-choice : ((v : Bool) → R.Fiber v) → ⊥
  no-global-choice choose = empty-fiber (choose true)

-- Direct application to the owner's COMPLETE proof-relevant resolution
-- histories, for any supplied admission policy and observation function.
module HistoryRetention {ℓV} (V : Type ℓV)
  (Seeds : Boundary.O.Complete → Type₁)
  (r : Boundary.R.Closure Seeds → V) = Retain r
