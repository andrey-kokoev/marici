{-# OPTIONS --safe --cubical --guardedness #-}
module GeneratedWolframRefutations where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Equiv
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Relation.Nullary.Properties using (isProp¬)

module Construct {ℓ : Level} (A B C : Type ℓ) where
  N : Type ℓ → Type ℓ → Type ℓ
  N X Y = (X × Y) → ⊥
  W : Type ℓ
  W = N (N (N A B) C) (N A (N (N A C) A))
  D : Type ℓ
  D = (C → ⊥) → ⊥
  forward : W → D
  forward = (λ v0 → (λ v1 → (v0 ((λ v2 → (v1 (snd v2))) , (λ v4 → ((snd v4) ((λ v8 → (v1 (snd v8))) , (fst v4))))))))
  backward : D → W
  backward = (λ v0 → (λ v1 → (v0 (λ v2 → ((fst v1) ((λ v4 → ((snd v1) ((fst v4) , (λ v7 → ((fst v7) ((fst v4) , v2)))))) , v2))))))
  -- Search supplies the maps; propositionality supplies their inverse laws.
  equivalence : W ≃ D
  equivalence = isoToEquiv record
    { fun = forward ; inv = backward
    ; rightInv = λ d → isProp¬ (C → ⊥) _ d
    ; leftInv = λ w → isProp¬ ((N (N A B) C) × (N A (N (N A C) A))) _ w }
  -- A further request to the same search, without a theorem-specific rule.
  swap : N A B → N B A
  swap = (λ v0 → (λ v1 → (v0 ((snd v1) , (fst v1)))))
