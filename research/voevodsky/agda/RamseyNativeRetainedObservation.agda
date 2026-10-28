{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyNativeRetainedObservation where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty.Base using (⊥)
import IndexedConstructorTables as Tables
import NativeTableRules as Rules
import NativeTableResolution as Resolution
module G = Tables.Core ℓ-zero
module N = Rules.Native ℓ-zero

module Observations (Root Frame History State Observation : Type)
  (Valid : Root → Type) (end : History → Frame)
  (realize : Frame → Root → State) (observe : Frame → State → Observation) where
  base : (a : Root) → Valid a → G.Package
  base a valid = N.pack (G.atom-node (Σ Root Valid)) (a , valid)
  Admit : G.Package → Type (ℓ-suc ℓ-zero)
  Admit q = Σ Root (λ a → Σ (Valid a) (λ v → q ≡ base a v))
  module R = Resolution.Full ℓ-zero Admit
  base-proof : (a : Root) (v : Valid a) → R.Resolve (base a v)
  base-proof a v = R.seed (a , (v , refl))
  Index : Root → Type
  Index a = Σ History (λ h → Σ State (λ s → Σ (s ≡ realize (end h) a)
    (λ _ → Σ Observation (λ o → o ≡ observe (end h) s))))
  index : (a : Root) → History → Index a
  index a h = h , (realize (end h) a , (refl , (observe (end h) (realize (end h) a) , refl)))
  package : (a : Root) → Valid a → History → G.Package
  package a v h = N.E-package (Index a) (λ _ → base a v) (index a h)
  native : (a : Root) (v : Valid a) (h : History) → R.Resolve (package a v h)
  native a v h = R.apply (N.E-kind , Index a , (λ _ → base a v) , index a h)
    (λ { (lift _) → base-proof a v })
  retains-root : (a : Root) (v : Valid a) (h : History)
    → snd (N.value (package a v h)) ≡ (a , v)
  retains-root a v h = refl
  retains-history : (a : Root) (v : Valid a) (h : History)
    → fst (fst (N.value (package a v h))) ≡ h
  retains-history a v h = refl
  retains-derivation : (a : Root) (v : Valid a) (h : History)
    → R.premise (package a v h , native a v h) (lift (index a h)) ≡ (base a v , base-proof a v)
  retains-derivation a v h = refl
  view : History → Root → Observation
  view h a = observe (end h) (realize (end h) a)
  endpoint-readout : (a : Root) (h k : History) → end h ≡ end k → view h a ≡ view k a
  endpoint-readout a h k p = cong (λ f → observe f (realize f a)) p
  history-not-erased : (a : Root) (v : Valid a) (h k : History)
    → N.value (package a v h) ≡ N.value (package a v k) → h ≡ k
  history-not-erased a v h k p = cong (λ value → fst (fst value)) p
  no-compressed-update : (h k : History) (a b : Root) (va : Valid a) (vb : Valid b)
    → view h a ≡ view h b → (view k a ≡ view k b → ⊥)
    → (update : Observation → Observation)
    → ((x : Root) → Valid x → update (view h x) ≡ view k x) → ⊥
  no-compressed-update h k a b va vb same different update correct =
    different (sym (correct a va) ∙ cong update same ∙ correct b vb)
