{-# OPTIONS --safe --cubical --guardedness #-}
module FourDomainPentagon where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism using (Iso; iso)
import MetaWitnessGenerator as Meta

-- Four dependent blocks. For domain specialization A is the first admitted
-- state, and B, C, D are the next three admission families.
module Pentagon {ℓ : Level} (A : Type ℓ) (B : A → Type ℓ)
  (C : (ab : Σ A B) → Type ℓ)
  (D : (abc : Σ (Σ A B) C) → Type ℓ) where
  P0 = Σ (Σ (Σ A B) C) D
  P1 = Σ (Σ[ a ∈ A ] Σ[ b ∈ B a ] C (a , b))
    (λ { (a , b , c) → D ((a , b) , c) })
  P2 = Σ[ a ∈ A ] Σ[ bc ∈ (Σ[ b ∈ B a ] C (a , b)) ]
    D ((a , fst bc) , snd bc)
  P3 = Σ[ a ∈ A ] Σ[ b ∈ B a ] Σ[ c ∈ C (a , b) ] D ((a , b) , c)
  P4 = Σ[ ab ∈ Σ A B ] Σ[ c ∈ C ab ] D (ab , c)

  e01 : Iso P0 P1
  e01 = iso (λ { (((a , b) , c) , d) → (a , b , c) , d })
    (λ { ((a , b , c) , d) → ((a , b) , c) , d })
    (λ _ → refl) (λ _ → refl)
  e12 : Iso P1 P2
  e12 = iso (λ { ((a , b , c) , d) → a , (b , c) , d })
    (λ { (a , (b , c) , d) → (a , b , c) , d })
    (λ _ → refl) (λ _ → refl)
  e23 : Iso P2 P3
  e23 = iso (λ { (a , (b , c) , d) → a , b , c , d })
    (λ { (a , b , c , d) → a , (b , c) , d })
    (λ _ → refl) (λ _ → refl)
  e04 : Iso P0 P4
  e04 = iso (λ { ((ab , c) , d) → ab , c , d })
    (λ { (ab , c , d) → (ab , c) , d })
    (λ _ → refl) (λ _ → refl)
  e43 : Iso P4 P3
  e43 = iso (λ { ((a , b) , c , d) → a , b , c , d })
    (λ { (a , b , c , d) → (a , b) , c , d })
    (λ _ → refl) (λ _ → refl)

  pentagon : (x : P0)
    → Iso.fun e23 (Iso.fun e12 (Iso.fun e01 x))
      ≡ Iso.fun e43 (Iso.fun e04 x)
  pentagon x = refl

  decode1 : P1 → P0
  decode1 = Iso.inv e01
  decode2 : P2 → P0
  decode2 x = decode1 (Iso.inv e12 x)
  decode3 : P3 → P0
  decode3 x = decode2 (Iso.inv e23 x)
  decode4 : P4 → P0
  decode4 = Iso.inv e04

  module Witnessed (R : P0 → P0 → Type ℓ)
    (g : (x : P0) → Σ[ y ∈ P0 ] R x y) (x : P0) where
    Step0 = Σ[ y ∈ P0 ] R x y
    Step1 = Σ[ y ∈ P1 ] R x (decode1 y)
    Step2 = Σ[ y ∈ P2 ] R x (decode2 y)
    Step3 = Σ[ y ∈ P3 ] R x (decode3 y)
    Step4 = Σ[ y ∈ P4 ] R x (decode4 y)
    s01 : Iso Step0 Step1
    s01 = iso (λ { (y , w) → Iso.fun e01 y , w })
      (λ { (y , w) → Iso.inv e01 y , w }) (λ _ → refl) (λ _ → refl)
    s12 : Iso Step1 Step2
    s12 = iso (λ { (y , w) → Iso.fun e12 y , w })
      (λ { (y , w) → Iso.inv e12 y , w }) (λ _ → refl) (λ _ → refl)
    s23 : Iso Step2 Step3
    s23 = iso (λ { (y , w) → Iso.fun e23 y , w })
      (λ { (y , w) → Iso.inv e23 y , w }) (λ _ → refl) (λ _ → refl)
    s04 : Iso Step0 Step4
    s04 = iso (λ { (y , w) → Iso.fun e04 y , w })
      (λ { (y , w) → Iso.inv e04 y , w }) (λ _ → refl) (λ _ → refl)
    s43 : Iso Step4 Step3
    s43 = iso (λ { (y , w) → Iso.fun e43 y , w })
      (λ { (y , w) → Iso.inv e43 y , w }) (λ _ → refl) (λ _ → refl)
    long short : Step0 → Step3
    long z = Iso.fun s23 (Iso.fun s12 (Iso.fun s01 z))
    short z = Iso.fun s43 (Iso.fun s04 z)
    full-pentagon : long ≡ short
    full-pentagon = refl
    generated-pentagon : long (g x) ≡ short (g x)
    generated-pentagon = refl

-- An arbitrary four-stage compatible chain. Each later base is explicitly
-- the preceding compiled generator; arbitrary unrelated WGs are not admitted.
module Domains {ℓ : Level} (S : Type ℓ) (R : S → S → Type ℓ)
  (first : Meta.Specialize.Compatible S R) where
  module M1 = Meta.Specialize S R
  module C1 = M1.Compiled first
  module M2 = Meta.Specialize C1.State C1.Relation
  module Second (d2 : M2.Domain)
    (a2 : (v : C1.State) → fst (C1.generator v) ≡ M2.Domain.compute d2 v)
    (c2 : (v : C1.State) → M2.Domain.Allowed d2 v → M2.Domain.Allowed d2 (fst (C1.generator v))) where
    module C2 = M2.Compiled (record { domain = d2 ; base = C1.generator ; agrees = a2 ; closed = c2 })
    module M3 = Meta.Specialize C2.State C2.Relation
    module Third (d3 : M3.Domain)
      (a3 : (v : C2.State) → fst (C2.generator v) ≡ M3.Domain.compute d3 v)
      (c3 : (v : C2.State) → M3.Domain.Allowed d3 v → M3.Domain.Allowed d3 (fst (C2.generator v))) where
      module C3 = M3.Compiled (record { domain = d3 ; base = C2.generator ; agrees = a3 ; closed = c3 })
      module M4 = Meta.Specialize C3.State C3.Relation
      module Fourth (d4 : M4.Domain)
        (a4 : (v : C3.State) → fst (C3.generator v) ≡ M4.Domain.compute d4 v)
        (c4 : (v : C3.State) → M4.Domain.Allowed d4 v → M4.Domain.Allowed d4 (fst (C3.generator v))) where
        module C4 = M4.Compiled (record { domain = d4 ; base = C3.generator ; agrees = a4 ; closed = c4 })
        module P = Pentagon C1.State (M2.Domain.Allowed d2)
          (M3.Domain.Allowed d3) (M4.Domain.Allowed d4)
        module Full = P.Witnessed C4.Relation C4.generator
