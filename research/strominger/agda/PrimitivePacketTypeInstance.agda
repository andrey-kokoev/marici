{-# OPTIONS --safe --cubical --guardedness #-}
module PrimitivePacketTypeInstance where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Empty.Base using (⊥)
import NativeTableRules
module N = NativeTableRules.Native ℓ-zero
module G = N.G

-- A selected finite native family, not an assumed chronological phase cycle.
atom : G.Package
atom = N.pack (G.atom-node Bool) false
family : Bool → G.Package
family _ = atom
selected : Bool → G.Package
selected i = N.E-package Bool family i
assembled : G.Package
assembled = N.Pi-package Bool family
stable : G.Package
stable = N.identity-comparison atom
reconciled : G.Package
reconciled = N.Congruence.Pi-comparison Bool family family (λ _ → idEquiv Bool) (λ _ → refl)

-- Explicit carrier adapters: these are types, not polynomial degrees.
selected-carrier : (i : Bool) → N.Ty (selected i) ≡ (Bool × Bool)
selected-carrier _ = refl
assembly-carrier : N.Ty assembled ≡ (Bool → Bool)
assembly-carrier = refl
stable-carrier : N.Ty stable ≡ G.Compare Bool Bool (idEquiv Bool)
stable-carrier = refl
reconciled-carrier : N.Ty reconciled ≡ G.Compare (Bool → Bool) (Bool → Bool) (idEquiv (Bool → Bool))
reconciled-carrier = refl

mark-retained : (i : Bool) → fst (N.value (selected i)) ≡ i
mark-retained _ = refl
payload-retained : (i : Bool) → snd (N.value (selected i)) ≡ false
payload-retained _ = refl
assembled-at : (i : Bool) → N.value assembled i ≡ false
assembled-at _ = refl
stable-witness : snd (snd (N.value stable)) ≡ refl
stable-witness = refl
reconciliation-at : (i : Bool) → cong (λ f → f i) (snd (snd (N.value reconciled))) ≡ refl
reconciliation-at _ = refl

-- Equal payloads do not make selected occurrences identical.
mark-erasure-hostile : N.value (selected true) ≡ N.value (selected false) → ⊥
mark-erasure-hostile path = true≢false (cong fst path)

-- State change is not automatically witnessed equivalence transport.
reset : Bool → Bool
reset _ = false
reset-has-no-left-inverse : (undo : Bool → Bool)
  → ((b : Bool) → undo (reset b) ≡ b) → ⊥
reset-has-no-left-inverse undo law = true≢false (sym (law true) ∙ law false)

-- A unary native output may be a comparison, not identity on the input carrier.
-- E and Pi rules also admit the same Bool input domain with different carriers.
-- These definally checked adapters specify what the finite candidate presents;
-- they do not make the packet itself the universe Type.
