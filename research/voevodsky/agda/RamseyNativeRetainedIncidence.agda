{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyNativeRetainedIncidence where
open import Cubical.Foundations.Prelude
open import Agda.Builtin.String using (String)
import IndexedConstructorTables as Tables
import NativeTableRules as Rules
import NativeTableResolution as Resolution
module G = Tables.Core ℓ-zero
module N = Rules.Native ℓ-zero

module Incidence (Port Vertex : Type) (Permit : Port → Type)
  (Inside : Port → Vertex → Type)
  (packet : (p : Port) → Permit p → String) where
  FullPort : Type
  FullPort = Σ Port (λ p → Σ (Permit p) (λ _ → String))
  base : (p : Port) → Permit p → G.Package
  base p c = N.pack (G.atom-node FullPort) (p , (c , packet p c))
  Admit : G.Package → Type (ℓ-suc ℓ-zero)
  Admit q = Σ Port (λ p → Σ (Permit p) (λ c → q ≡ base p c))
  module R = Resolution.Full ℓ-zero Admit
  base-proof : (p : Port) (c : Permit p) → R.Resolve (base p c)
  base-proof p c = R.seed (p , (c , refl))
  Common : (I : Type) → (I → Port) → Type
  Common I parent = Σ Vertex (λ v → (i : I) → Inside (parent i) v)
  family : (I : Type) (parent : I → Port) → ((i : I) → Permit (parent i)) → G.Package
  family I parent cert = N.Pi-package I (λ i → base (parent i) (cert i))
  family-proof : (I : Type) (parent : I → Port) (cert : (i : I) → Permit (parent i))
    → R.Resolve (family I parent cert)
  family-proof I parent cert = R.apply (N.P-kind , I , (λ i → base (parent i) (cert i)))
    (λ { (lift i) → base-proof (parent i) (cert i) })
  selected : (I : Type) (parent : I → Port) (cert : (i : I) → Permit (parent i))
    → Common I parent → G.Package
  selected I parent cert w = N.E-package (Common I parent) (λ _ → family I parent cert) w
  selected-proof : (I : Type) (parent : I → Port) (cert : (i : I) → Permit (parent i))
    (w : Common I parent) → R.Resolve (selected I parent cert w)
  selected-proof I parent cert w = R.apply
    (N.E-kind , Common I parent , (λ _ → family I parent cert) , w)
    (λ { (lift _) → family-proof I parent cert })
  retained-support : (I : Type) (parent : I → Port) (cert : (i : I) → Permit (parent i))
    (w : Common I parent) → fst (N.value (selected I parent cert w)) ≡ w
  retained-support I parent cert w = refl
  retained-parent : (I : Type) (parent : I → Port) (cert : (i : I) → Permit (parent i))
    (w : Common I parent) (i : I)
    → snd (N.value (selected I parent cert w)) i ≡ (parent i , (cert i , packet (parent i) (cert i)))
  retained-parent I parent cert w i = refl
  retained-derivation : (I : Type) (parent : I → Port) (cert : (i : I) → Permit (parent i))
    (w : Common I parent) (i : I)
    → R.premise (R.premise (selected I parent cert w , selected-proof I parent cert w) (lift w)) (lift i)
      ≡ (base (parent i) (cert i) , base-proof (parent i) (cert i))
  retained-derivation I parent cert w i = refl
  restrict : {I J : Type} {parent : I → Port} (r : J → I)
    → Common I parent → Common J (λ j → parent (r j))
  restrict r (v , witness) = v , (λ j → witness (r j))
  restriction-composes : {I J K : Type} {parent : I → Port}
    (r : J → I) (s : K → J) (w : Common I parent)
    → restrict s (restrict r w) ≡ restrict (λ k → r (s k)) w
  restriction-composes r s w = refl
  selected-restriction-composes : (I J K : Type) (parent : I → Port)
    (cert : (i : I) → Permit (parent i)) (r : J → I) (s : K → J) (w : Common I parent)
    → selected K (λ k → parent (r (s k))) (λ k → cert (r (s k))) (restrict s (restrict r w))
      ≡ selected K (λ k → parent (r (s k))) (λ k → cert (r (s k))) (restrict (λ k → r (s k)) w)
  selected-restriction-composes I J K parent cert r s w = refl
