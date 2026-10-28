{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyObservedComparisons where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Empty.Base using (⊥)
import RamseyAtomicSeedPaths as Atom

ObservedEquiv : (A B O : Type) → (A → O) → (B → O) → Type
ObservedEquiv A B O observeA observeB =
  Σ (A ≃ B) (λ e → (x : A) → observeB (equivFun e x) ≡ observeA x)
identity-guard : (A O : Type) (observe : A → O) → ObservedEquiv A A O observe observe
identity-guard A O observe = idEquiv A , (λ x → refl)
compose-guard : {A B C O : Type} {a : A → O} {b : B → O} {c : C → O}
  → ObservedEquiv A B O a b → ObservedEquiv B C O b c → ObservedEquiv A C O a c
compose-guard (e , preservesE) (f , preservesF) = compEquiv e f ,
  (λ x → preservesF (equivFun e x) ∙ preservesE x)
inverse-guard : {A B O : Type} {a : A → O} {b : B → O}
  → ObservedEquiv A B O a b → ObservedEquiv B A O b a
inverse-guard {b = b} (e , preserves) = invEquiv e ,
  (λ y → sym (preserves (invEq e y)) ∙ cong b (secEq e y))
endpoint-observation : {A B O : Type} {a : A → O} {b : B → O}
  (e : ObservedEquiv A B O a b) (x : A) (y : B)
  → equivFun (fst e) x ≡ y → a x ≡ b y
endpoint-observation {b = b} (e , preserves) x y aligned = sym (preserves x) ∙ cong b aligned

-- The fixed observation is external to the universe-varying native package.
Tagged : (O : Type) → Type (ℓ-suc ℓ-zero)
Tagged O = Σ O (λ _ → Atom.G.Package)
tagged-atom : {A O : Type} → (A → O) → A → Tagged O
tagged-atom {A} observe x = observe x , Atom.atom A x
guarded-package-path : {A B O : Type} {a : A → O} {b : B → O}
  (e : ObservedEquiv A B O a b) (x : A) (y : B)
  (aligned : equivFun (fst e) x ≡ y)
  → tagged-atom a x ≡ tagged-atom b y
guarded-package-path {a = a} {b = b} e x y aligned i =
  endpoint-observation {a = a} {b = b} e x y aligned i , Atom.atom-path (fst e) x y aligned i

no-visible-change : (e : ObservedEquiv Bool Bool Bool (λ b → b) (λ b → b))
  → equivFun (fst e) false ≡ true → ⊥
no-visible-change e aligned = false≢true (endpoint-observation {a = λ b → b} {b = λ b → b} e false true aligned)
no-tagged-swap : tagged-atom (λ (b : Bool) → b) false ≡ tagged-atom (λ b → b) true → ⊥
no-tagged-swap path = false≢true (cong fst path)

-- A deliberately lossy observation still admits the swap. No hidden rigidity.
constant-observation-flip : ObservedEquiv Bool Bool Unit (λ _ → tt) (λ _ → tt)
constant-observation-flip = isoToEquiv Atom.flip , (λ _ → refl)
constant-observation-path : tagged-atom (λ (_ : Bool) → tt) false ≡ tagged-atom (λ (_ : Bool) → tt) true
constant-observation-path = guarded-package-path {a = λ _ → tt} {b = λ _ → tt} constant-observation-flip false true refl
