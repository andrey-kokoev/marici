{-# OPTIONS --safe --cubical --guardedness #-}
module NestedWitnessSpecialization where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism using (Iso; iso)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Sum.Base using (inl)
import MetaWitnessGenerator as Meta
import WitnessSelectionGenerator as Selection
import ReSpecializeWitnessSelection as First
open import TypedGeneratorLayers using (Layer1)

-- Two compatible specializations of the SAME underlying WG. The second
-- consumes the actual output of the first, not an unrelated replacement WG.
module Nested {ℓ : Level} (S : Type ℓ) (R : S → S → Type ℓ)
  (first : Meta.Specialize.Compatible S R) where
  module M1 = Meta.Specialize S R
  module C1 = M1.Compiled first
  module M2 = Meta.Specialize C1.State C1.Relation

  module Followup (domain2 : M2.Domain)
    (agreement2 : (v : C1.State)
      → fst (C1.generator v) ≡ M2.Domain.compute domain2 v)
    (closure2 : (v : C1.State) → M2.Domain.Allowed domain2 v
      → M2.Domain.Allowed domain2 (fst (C1.generator v))) where
    second : M2.Compatible
    second = record
      { domain = domain2 ; base = C1.generator
      ; agrees = agreement2 ; closed = closure2 }
    module C2 = M2.Compiled second
    open M1.Compatible first using (domain)
    open M1.Domain domain using (Allowed)
    open M2.Domain domain2 renaming (Allowed to Allowed2)

    -- Nested dependent admission is only reassociation, not erasure.
    Flat : Type ℓ
    Flat = Σ[ s ∈ S ] Σ[ ok ∈ Allowed s ] Allowed2 (s , ok)

    flatten : C2.State → Flat
    flatten ((s , ok) , proof) = s , ok , proof
    unflatten : Flat → C2.State
    unflatten (s , ok , proof) = (s , ok) , proof
    flat-iso : Iso C2.State Flat
    flat-iso = iso flatten unflatten (λ _ → refl) (λ _ → refl)

    FlatRelation : Flat → Flat → Type ℓ
    FlatRelation x y = C2.Relation (unflatten x) (unflatten y)

    -- Compile the flattened view directly from the first witnessed step and
    -- the second admission/compatibility data, not by repacking C2.generator.
    direct-generator : (x : Flat) → Σ[ y ∈ Flat ] FlatRelation x y
    direct-generator (s , ok , p) =
      (fst (fst t) , snd (fst t) , closure2 (s , ok) p) ,
      (snd t , (agreement2 (s , ok) , C2.evidence (s , ok)))
      where
        t = C1.generator (s , ok)

    direct-WG : Layer1 ℓ
    direct-WG = record
      { State = Flat ; Witness = FlatRelation ; generate = direct-generator }

    direct-vs-nested : (x : Flat)
      → flatten (fst (C2.generator (unflatten x))) ≡ fst (direct-generator x)
    direct-vs-nested (s , ok , p) = refl

    direct-witness-vs-nested : (s : S) (ok : Allowed s)
      (p : Allowed2 (s , ok))
      → snd (direct-generator (s , ok , p)) ≡
        snd (C2.generator ((s , ok) , p))
    direct-witness-vs-nested s ok p = refl

    NestedStep : Flat → Type ℓ
    NestedStep x = Σ[ y ∈ C2.State ] C2.Relation (unflatten x) y
    DirectStep : Flat → Type ℓ
    DirectStep x = Σ[ y ∈ Flat ] FlatRelation x y
    step-iso : (x : Flat) → Iso (NestedStep x) (DirectStep x)
    step-iso x = iso
      (λ { (y , w) → flatten y , w })
      (λ { (y , w) → unflatten y , w })
      (λ { (y , w) → refl })
      (λ { (y , w) → refl })

    -- After two steps, project the original R witness out of both shells.
    -- This states a preservation law, not a universal filler theorem.
    original-witness : (s : S) (ok : Allowed s) (p : Allowed2 (s , ok))
      → R s (fst (fst (fst (C2.generator ((s , ok) , p)))))
    original-witness s ok p = fst (fst (snd (C2.generator ((s , ok) , p))))

    same-base-transition : (s : S) (ok : Allowed s) (p : Allowed2 (s , ok))
      → fst (fst (C2.generator ((s , ok) , p))) ≡ fst (C1.generator (s , ok))
    same-base-transition s ok p = refl

    recovered-second-input : fst C2.compiled ≡ second
    recovered-second-input = C2.source-recovered

-- A concrete third-stage wrapper around certified selection. The first
-- specialization requires the execution trace; this stage retains it and
-- adds an independent admitted layer without changing the original step.
module Example where
  module N = Nested Selection.State Selection.SelectionWitness First.selection-pair
  second-domain : N.M2.Domain
  second-domain = record
    { compute = λ v → fst (N.C1.generator v)
    ; Allowed = λ _ → Lift {j = ℓ-suc ℓ-zero} Unit
    ; LawInput = Selection.Request
    ; request = λ q → inl q , lift tt
    ; expected = λ q → fst (N.C1.generator (inl q , lift tt))
    ; law = λ q → refl }
  module T = N.Followup second-domain (λ v → refl) (λ v ok → ok)
  request : T.C2.State
  request = (inl Selection.request-false , lift tt) , lift tt
  underlying : Selection.SelectionWitness (inl Selection.request-false)
    (fst (fst (fst (T.C2.generator request))))
  underlying = T.original-witness (inl Selection.request-false) (lift tt) (lift tt)
