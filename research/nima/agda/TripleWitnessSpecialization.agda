{-# OPTIONS --safe --cubical --guardedness #-}
module TripleWitnessSpecialization where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism using (Iso; iso)
import MetaWitnessGenerator as Meta
import NestedWitnessSpecialization as Nested
import WitnessSelectionGenerator as Selection
import ReSpecializeWitnessSelection as First
open import Cubical.Data.Unit.Base using (Unit; tt)

-- Three compatible layers, each reusing the actual preceding generator.
-- Compare flattening the inner two first with flattening all three directly.
module Triple {ℓ : Level} (S : Type ℓ) (R : S → S → Type ℓ)
  (first : Meta.Specialize.Compatible S R) where
  module N = Nested.Nested S R first

  module AfterSecond (domain2 : N.M2.Domain)
    (agree2 : (v : N.C1.State) → fst (N.C1.generator v) ≡ N.M2.Domain.compute domain2 v)
    (closed2 : (v : N.C1.State) → N.M2.Domain.Allowed domain2 v
      → N.M2.Domain.Allowed domain2 (fst (N.C1.generator v))) where
    module Two = N.Followup domain2 agree2 closed2
    module M3 = Meta.Specialize Two.C2.State Two.C2.Relation

    module AfterThird (domain3 : M3.Domain)
      (agree3 : (v : Two.C2.State)
        → fst (Two.C2.generator v) ≡ M3.Domain.compute domain3 v)
      (closed3 : (v : Two.C2.State) → M3.Domain.Allowed domain3 v
        → M3.Domain.Allowed domain3 (fst (Two.C2.generator v))) where
      third : M3.Compatible
      third = record
        { domain = domain3 ; base = Two.C2.generator
        ; agrees = agree3 ; closed = closed3 }
      module C3 = M3.Compiled third
      open N.M1.Compatible first using (domain)
      open N.M1.Domain domain using (Allowed)
      open N.M2.Domain domain2 renaming (Allowed to Allowed2)
      open M3.Domain domain3 renaming (Allowed to Allowed3)

      LeftGrouped : Type ℓ
      LeftGrouped = Σ[ x ∈ Two.Flat ] Allowed3 (Two.unflatten x)
      RightGrouped : Type ℓ
      RightGrouped = Σ[ s ∈ S ] Σ[ p ∈ Allowed s ]
        Σ[ q ∈ Allowed2 (s , p) ] Allowed3 ((s , p) , q)

      left : C3.State → LeftGrouped
      left (v , r) = Two.flatten v , r
      right : C3.State → RightGrouped
      right (((s , p) , q) , r) = s , p , q , r
      reassociate : LeftGrouped → RightGrouped
      reassociate ((s , p , q) , r) = s , p , q , r
      left-as-right : (v : C3.State) → reassociate (left v) ≡ right v
      left-as-right (((s , p) , q) , r) = refl

      unright : RightGrouped → C3.State
      unright (s , p , q , r) = ((s , p) , q) , r
      right-iso : Iso C3.State RightGrouped
      right-iso = iso right unright (λ _ → refl) (λ _ → refl)

      -- The two parenthesizations agree on full generated steps, not only
      -- on state labels. Both use the same third-layer witness.
      StepLeft : (v : C3.State) → Type ℓ
      StepLeft v = Σ[ w ∈ LeftGrouped ] C3.Relation v (unright (reassociate w))
      StepRight : (v : C3.State) → Type ℓ
      StepRight v = Σ[ w ∈ RightGrouped ] C3.Relation v (unright w)
      step-reassociate : (v : C3.State) → Iso (StepLeft v) (StepRight v)
      step-reassociate v = iso
        (λ { (w , proof) → reassociate w , proof })
        (λ { (w , proof) → ((fst w , fst (snd w) , fst (snd (snd w))) ,
          snd (snd (snd w))) , proof })
        (λ { ((s , p , q , r) , proof) → refl })
        (λ { (((s , p , q) , r) , proof) → refl })

      generated-left-right : (v : C3.State)
        → reassociate (left (fst (C3.generator v))) ≡ right (fst (C3.generator v))
      generated-left-right (((s , p) , q) , r) = refl

      generated-left : (v : C3.State) → StepLeft v
      generated-left v = left (fst (C3.generator v)) , snd (C3.generator v)
      generated-right : (v : C3.State) → StepRight v
      generated-right v = right (fst (C3.generator v)) , snd (C3.generator v)
      generated-step-agrees : (v : C3.State)
        → Iso.fun (step-reassociate v) (generated-left v) ≡ generated-right v
      generated-step-agrees (((s , p) , q) , r) = refl

module SelectionExample where
  module A = Triple Selection.State Selection.SelectionWitness First.selection-pair
  module B = A.AfterSecond Nested.Example.second-domain (λ v → refl) (λ v ok → ok)
  third-domain : B.M3.Domain
  third-domain = record
    { compute = λ v → fst (B.Two.C2.generator v)
    ; Allowed = λ _ → Lift {j = ℓ-suc ℓ-zero} Unit
    ; LawInput = Lift {j = ℓ-suc ℓ-zero} Unit
    ; request = λ _ → Nested.Example.request
    ; expected = λ _ → fst (B.Two.C2.generator Nested.Example.request)
    ; law = λ _ → refl }
  module C = B.AfterThird third-domain (λ v → refl) (λ v ok → ok)
  example : C.C3.State
  example = Nested.Example.request , lift tt
  witnessed-reassociation :
    Iso.fun (C.step-reassociate example) (C.generated-left example)
      ≡ C.generated-right example
  witnessed-reassociation = C.generated-step-agrees example
