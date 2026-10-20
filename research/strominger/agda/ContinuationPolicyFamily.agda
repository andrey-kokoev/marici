{-# OPTIONS --safe --cubical --guardedness #-}
module ContinuationPolicyFamily where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Relation.Nullary.Base using (¬_)
open import NativeExtensionFamilyAudit using (Vertex; Seeds)
open import InternalSourceComparisons
import SynchronizedContinuationAdapter as Sync
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
open Whole.Universe ℓ-zero
open Resolution.Generators ℓ-zero hiding (output)

-- A declared bounded family of presentations, NOT all possible policies.
data Presentation : Type where
  target source synchronized : Presentation
mark : Presentation → Bool
mark target = true
mark source = false
mark synchronized = false
target-not-source : ¬ (target ≡ source)
target-not-source p = true≢false (cong mark p)

-- This selection condition is explicitly additional representation policy.
-- It is not inferred from source incidence, native admission or port data.
selected-tag : (chosen : Presentation) → isContr (Σ[ p ∈ Presentation ] p ≡ chosen)
selected-tag chosen .fst = chosen , refl
selected-tag chosen .snd (p , w) i = w (~ i) , (λ j → w (~ i ∨ j))

module Family (m : Mode) {v : Vertex} (a : Body v) (b : Body (act m v))
  (e : El (expression (package a)) ≃ El (expression (package b)))
  (p : equivFun e (value (package a)) ≡ value (package b))
  (h : (x : El (expression (package a))) → act m (reader a x) ≡ reader b (equivFun e x)) where
  module S = Sync.Adapter m a b e p h

  -- Common synchronized input fixes the request frame; no extra equivalence,
  -- reader, native proof or comparison filler is an evaluator parameter.
  output : (r : S.Request) → Presentation → Body (fst (S.route r))
  output r target = S.S.targetBody (fst r)
  output r source = S.S.sourceBody (fst r)
  output r synchronized = S.syncBody r
  native : (r : S.Request) (k : Presentation) → Resolve Seeds (package (output r k))
  native r k = derivation (output r k)
  toTarget : (r : S.Request) (k : Presentation)
    → El (expression (package (output r k))) ≃ El (expression (package (output r target)))
  toTarget r target = idEquiv _
  toTarget r source = S.S.attachmentEquiv (fst r)
  toTarget r synchronized = S.toTarget r
  point : (r : S.Request) (k : Presentation)
    → equivFun (toTarget r k) (value (package (output r k))) ≡ value (package (output r target))
  point r target = refl
  point r source = refl
  point r synchronized = refl
  ports : (r : S.Request) (k : Presentation) (x : El (expression (package (output r k))))
    → reader (output r k) x ≡ reader (output r target) (equivFun (toTarget r k) x)
  ports r target x = refl
  ports r source x = refl
  ports r synchronized x = refl
  policyComparison : (r : S.Request) (k : Presentation) → Body (fst (S.route r))
  policyComparison r k = compare stay (output r k) (output r target) (toTarget r k) (point r k) (ports r k)
  comparison-native : (r : S.Request) (k : Presentation) → Resolve Seeds (package (policyComparison r k))
  comparison-native r k = derivation (policyComparison r k)

  -- Port-only tasks are arbitrary supplied predicates, at any universe level.
  -- Nonuniqueness is about tagged presentations, NOT inequivalent outcomes.
  PortChoices : ∀ {ℓ} → (Vertex → Type ℓ) → S.Request → Type ℓ
  PortChoices Task r = Σ[ k ∈ Presentation ] Task (fst (S.route r))
  port-task-does-not-select : ∀ {ℓ} (Task : Vertex → Type ℓ) (r : S.Request)
    → Task (fst (S.route r)) → ¬ isProp (PortChoices Task r)
  port-task-does-not-select Task r witness unique = target-not-source
    (cong fst (unique (target , witness) (source , witness)))
