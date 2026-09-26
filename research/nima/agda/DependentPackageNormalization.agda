{-# OPTIONS --safe --cubical --guardedness #-}
module DependentPackageNormalization where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Unit.Base using (Unit*; tt*)
open import Cubical.Data.Sigma.Properties using (Σ-cong-equiv-snd)
import WholePackageSigmaPi as Whole
import ProofRelevantCoherenceClosure as Witness

module Normalization (ℓ : Level) where
  open Whole.Universe ℓ

  -- Shapes, positions and witnesses are TYPES, with all their identities.
  -- No enumeration, decidable equality or truncation is used.
  record Container : Type (ℓ-suc ℓ) where
    constructor container
    field
      Shape : Type ℓ
      Position : Shape → Type ℓ
      Entry : (s : Shape) → Position s → Type ℓ
  open Container public

  Value : Container → Type ℓ
  Value C = Σ[ s ∈ Shape C ] ((p : Position C s) → Entry C s p)

  atomic : Type ℓ → Container
  atomic A = container Unit* (λ _ → Unit*) (λ _ _ → A)

  sum : (I : Type ℓ) → (I → Container) → Container
  sum I C = container
    (Σ[ i ∈ I ] Shape (C i))
    (λ s → Position (C (fst s)) (snd s))
    (λ s p → Entry (C (fst s)) (snd s) p)

  product : (I : Type ℓ) → (I → Container) → Container
  product I C = container
    ((i : I) → Shape (C i))
    (λ f → Σ[ i ∈ I ] Position (C i) (f i))
    (λ f p → Entry (C (fst p)) (f (fst p)) (snd p))

  atomic-equiv : (A : Type ℓ) → A ≃ Value (atomic A)
  atomic-equiv A = isoToEquiv
    (iso (λ x → tt* , (λ _ → x)) (λ v → snd v tt*) (λ _ → refl) (λ _ → refl))

  sum-equiv : (I : Type ℓ) (C : I → Container)
    → (Σ[ i ∈ I ] Value (C i)) ≃ Value (sum I C)
  sum-equiv I C = isoToEquiv
    (iso (λ { (i , s , w) → (i , s) , w })
         (λ { ((i , s) , w) → i , s , w }) (λ _ → refl) (λ _ → refl))

  product-equiv : (I : Type ℓ) (C : I → Container)
    → ((i : I) → Value (C i)) ≃ Value (product I C)
  product-equiv I C = isoToEquiv
    (iso (λ v → (λ i → fst (v i)) , (λ p → snd (v (fst p)) (snd p)))
         (λ { (f , w) i → f i , (λ p → w (i , p)) })
         (λ _ → refl) (λ _ → refl))

  normal : Code → Container
  normal (atom A) = atomic A
  normal (E I F) = sum I (λ i → normal (F i))
  normal (Pi I F) = product I (λ i → normal (F i))
  normal (retain Q q R) = normal R
  normal (maps Q R) = product (El Q) (λ _ → normal R)
  -- Full comparison/identity payloads are retained as higher-valued entries.
  -- Normalization here repackages them; it does not truncate their proofs.
  normal (paths Q x y) = atomic (x ≡ y)
  normal (equivalences Q R) = atomic (El Q ≃ El R)
  normal (comparison Q R e) = atomic (El (comparison Q R e))

  normalize-equiv : (Q : Code) → El Q ≃ Value (normal Q)
  normalize-equiv (atom A) = atomic-equiv A
  normalize-equiv (E I F) = compEquiv
    (Σ-cong-equiv-snd (λ i → normalize-equiv (F i))) (sum-equiv I (λ i → normal (F i)))
  normalize-equiv (Pi I F) = compEquiv
    (equivΠCod (λ i → normalize-equiv (F i))) (product-equiv I (λ i → normal (F i)))
  normalize-equiv (retain Q q R) = normalize-equiv R
  normalize-equiv (maps Q R) = compEquiv
    (equivΠCod (λ _ → normalize-equiv R)) (product-equiv (El Q) (λ _ → normal R))
  normalize-equiv (paths Q x y) = atomic-equiv (x ≡ y)
  normalize-equiv (equivalences Q R) = atomic-equiv (El Q ≃ El R)
  normalize-equiv (comparison Q R e) = atomic-equiv (El (comparison Q R e))

  normalize : (Q : Code) → El Q → Value (normal Q)
  normalize Q = equivFun (normalize-equiv Q)

  reconstruct : (Q : Code) → Value (normal Q) → El Q
  reconstruct Q = invEq (normalize-equiv Q)

  source-roundtrip : (Q : Code) (x : El Q) → reconstruct Q (normalize Q x) ≡ x
  source-roundtrip Q = retEq (normalize-equiv Q)

  normal-roundtrip : (Q : Code) (x : Value (normal Q)) → normalize Q (reconstruct Q x) ≡ x
  normal-roundtrip Q = secEq (normalize-equiv Q)

  reexpress : Container → Code
  reexpress C = E (Shape C) (λ s → Pi (Position C s) (λ p → atom (Entry C s p)))

  -- The normal form is itself an input to the very same dependent grammar.
  normalize-again : (Q : Code) → Value (normal Q)
    → Value (normal (reexpress (normal Q)))
  normalize-again Q = normalize (reexpress (normal Q))

  second-roundtrip : (Q : Code) (x : Value (normal Q))
    → reconstruct (reexpress (normal Q)) (normalize-again Q x) ≡ x
  second-roundtrip Q = source-roundtrip (reexpress (normal Q))

  path-equiv : (Q : Code) (x y : El Q)
    → (x ≡ y) ≃ (normalize Q x ≡ normalize Q y)
  path-equiv Q x y = Witness.pathLift (normalize-equiv Q)

  record Retained : Type (ℓ-suc ℓ) where
    constructor retained-normalization
    field
      source : Code
      original : El source
      normalized : Value (normal source)
      agrees : normalize source original ≡ normalized
      reconstructs : reconstruct source normalized ≡ original

  retain-normalization : (Q : Code) → El Q → Retained
  retain-normalization Q x = retained-normalization Q x (normalize Q x) refl (source-roundtrip Q x)

  reify-retained : Retained → Whole.Universe.Complete (ℓ-suc ℓ)
  reify-retained r = Whole.Universe.pack (Whole.Universe.atom Retained) r
