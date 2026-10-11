{-# OPTIONS --safe --cubical --guardedness #-}
module SigmaReassociation where

-- Ordinary reusable glue, with no graph, generator, source or WG concepts.
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism using (Iso; compIso; invIso)
open import Cubical.Data.Sigma.Properties using (Σ-assoc-Iso; Σ-cong-iso-snd)

-- Lift strict reassociation through an arbitrary dependent result family.
-- Avoid the transports introduced by general change-of-base along an Iso.
totalAssoc : ∀ {a b c d} {A : Type a} {B : A → Type b}
  {C : (x : A) → B x → Type c}
  {D : (Σ[ x ∈ A ] Σ[ y ∈ B x ] C x y) → Type d}
  → Iso (Σ[ xyz ∈ (Σ[ xy ∈ Σ A B ] C (fst xy) (snd xy)) ]
           D (fst (fst xyz) , snd (fst xyz) , snd xyz))
        (Σ[ xyz ∈ (Σ[ x ∈ A ] Σ[ y ∈ B x ] C x y) ] D xyz)
totalAssoc = compIso Σ-assoc-Iso
  (compIso Σ-assoc-Iso
    (compIso (Σ-cong-iso-snd (λ _ → invIso Σ-assoc-Iso)) (invIso Σ-assoc-Iso)))
