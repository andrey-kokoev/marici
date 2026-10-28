{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyAtomicSeedPaths where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Univalence using (ua; ua-gluePath)
open import Cubical.Data.Bool.Base using (Bool; false; true; not)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty.Base using (⊥)
import IndexedConstructorTables as Tables
import NativeTableRules as Rules
import NativeTableResolution as Resolution
module G = Tables.Core ℓ-zero
module N = Rules.Native ℓ-zero

atom : (A : Type) → A → G.Package
atom A x = N.pack (G.atom-node A) x
atom-path : {A B : Type} (e : A ≃ B) (x : A) (y : B)
  → equivFun e x ≡ y → atom A x ≡ atom B y
atom-path e x y alignment i = (ua e i , G.atom-node (ua e i)) , ua-gluePath e alignment i
flip : Iso Bool Bool
Iso.fun flip = not
Iso.inv flip = not
Iso.rightInv flip false = refl
Iso.rightInv flip true = refl
Iso.leftInv flip false = refl
Iso.leftInv flip true = refl
swapped : atom Bool false ≡ atom Bool true
swapped = atom-path (isoToEquiv flip) false true refl

-- The same path-closed equality pattern used by native span admission.
Admit : G.Package → Type (ℓ-suc ℓ-zero)
Admit q = q ≡ atom Bool false
module R = Resolution.Full ℓ-zero Admit
swapped-admission : Admit (atom Bool true)
swapped-admission = sym swapped
swapped-seed : R.Resolve (atom Bool true)
swapped-seed = R.seed swapped-admission

no-rigid-bool-readout : (observe : G.Package → Bool)
  → ((b : Bool) → observe (atom Bool b) ≡ b) → ⊥
no-rigid-bool-readout observe agrees = false≢true
  (sym (agrees false) ∙ cong observe swapped ∙ agrees true)

no-fixed-carrier-reflection :
  ((x y : Bool) → atom Bool x ≡ atom Bool y → x ≡ y) → ⊥
no-fixed-carrier-reflection reflects = false≢true (reflects false true swapped)
