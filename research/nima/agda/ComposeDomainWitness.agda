{-# OPTIONS --safe --cubical --guardedness #-}
module ComposeDomainWitness where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sum.Base using (_⊎_; inl; inr)
open import Cubical.Foundations.Isomorphism using (Iso; iso)
open import TypedGeneratorLayers using (Layer1)
import MetaWitnessGenerator as Meta
import NestedWitnessSpecialization as Nested
import WitnessSelectionGenerator as Selection
import ReSpecializeWitnessSelection as First
open import Cubical.Data.Unit.Base using (tt)

-- Compile two compatible domain presentations into ONE presentation over
-- the original WG. The combined input retains BOTH admission certificates;
-- its law index is the tagged union of the two source law indices.
module Composition {ℓ : Level} (S : Type ℓ) (R : S → S → Type ℓ)
  (first : Meta.Specialize.Compatible S R) where
  module N = Nested.Nested S R first
  module M = Meta.Specialize S R
  open M.Compatible first using (domain; base; agrees; closed)
  open M.Domain domain renaming
    (compute to compute1; Allowed to Allowed1; LawInput to Laws1;
     request to request1; expected to expected1; law to law1)

  module WithSecond (domain2 : N.M2.Domain)
    (agree2 : (v : N.C1.State)
      → fst (N.C1.generator v) ≡ N.M2.Domain.compute domain2 v)
    (closed2 : (v : N.C1.State) → N.M2.Domain.Allowed domain2 v
      → N.M2.Domain.Allowed domain2 (fst (N.C1.generator v))) where
    module Two = N.Followup domain2 agree2 closed2
    open N.M2.Domain domain2 renaming
      (Allowed to Allowed2; LawInput to Laws2; request to request2;
       expected to expected2; law to law2)

    combined-domain : M.Domain
    combined-domain = record
      { compute = compute1
      ; Allowed = λ s → Σ[ p ∈ Allowed1 s ] Allowed2 (s , p)
      ; LawInput = Laws1 ⊎ Laws2
      ; request = λ { (inl k) → request1 k ; (inr k) → fst (request2 k) }
      ; expected = λ { (inl k) → expected1 k ; (inr k) → fst (expected2 k) }
      ; law = λ
        { (inl k) → law1 k
        ; (inr k) →
          sym (agrees (fst (request2 k)))
          ∙ cong fst (agree2 (request2 k))
          ∙ cong fst (law2 k) } }

    combined-input : M.Compatible
    combined-input = record
      { domain = combined-domain ; base = base ; agrees = agrees
      ; closed = λ { s (p , q) → closed s p , closed2 (s , p) q } }
    module Direct = M.Compiled combined-input

    -- Faithful composition retains the intermediate state, both law-evidence
    -- families and the second compatibility path. The compressed Domain above
    -- is only its readout; it cannot replace this proof-relevant relation.
    FullState : Type ℓ
    FullState = Two.Flat
    FullRelation : FullState → FullState → Type ℓ
    FullRelation = Two.FlatRelation
    full-generator : (v : FullState) → Σ[ w ∈ FullState ] FullRelation v w
    full-generator = Two.direct-generator
    full-WG : Layer1 ℓ
    full-WG = Two.direct-WG

    flatten-admission : FullState → Direct.State
    flatten-admission (s , p , q) = s , (p , q)
    expand-admission : Direct.State → FullState
    expand-admission (s , (p , q)) = s , p , q
    admission-iso : Iso FullState Direct.State
    admission-iso = iso flatten-admission expand-admission
      (λ _ → refl) (λ _ → refl)

    -- The full step package has a two-sided equivalence to the actual nested
    -- step package. No law witness or intermediate comparison is projected.
    full-step-iso : (v : FullState)
      → Iso (Two.NestedStep v) (Two.DirectStep v)
    full-step-iso = Two.step-iso

    full-second-law : (k : Laws2) (ok : Allowed2 (request2 k))
      → fst (fst (Two.C2.generator (request2 k , ok))) ≡ expected2 k
    full-second-law = Two.C2.law-from-step

    record FullComposition : Type (ℓ-suc ℓ) where
      field
        first-source : M.Compatible
        second-source : N.M2.Domain
        second-agreement : (v : N.C1.State)
          → fst (N.C1.generator v) ≡ N.M2.Domain.compute second-source v
        second-closure : (v : N.C1.State)
          → N.M2.Domain.Allowed second-source v
          → N.M2.Domain.Allowed second-source (fst (N.C1.generator v))
        generated : Layer1 ℓ
        generated-correct : generated ≡ full-WG

    full-composition : FullComposition
    full-composition = record
      { first-source = first ; second-source = domain2
      ; second-agreement = agree2 ; second-closure = closed2
      ; generated = full-WG ; generated-correct = refl }

    recover-first : FullComposition.first-source full-composition ≡ first
    recover-first = refl
    recover-second : FullComposition.second-source full-composition ≡ domain2
    recover-second = refl

    -- Output states agree definitionally with the two-stage flat view.
    direct-output : (s : S) (p : Allowed1 s) (q : Allowed2 (s , p))
      → fst (Direct.generator (s , (p , q))) ≡
        Two.flatten (fst (Two.C2.generator ((s , p) , q)))
    direct-output s p q = refl

    -- The original R witness also survives. The two relation types are NOT
    -- identified: nested witnesses retain more intermediate comparisons.
    original-witness-agrees : (s : S) (p : Allowed1 s) (q : Allowed2 (s , p))
      → fst (snd (Direct.generator (s , (p , q)))) ≡
        Two.original-witness s p q
    original-witness-agrees s p q = refl

    first-law : (k : Laws1)
      → compute1 (request1 k) ≡ expected1 k
    first-law k = M.Domain.law combined-domain (inl k)
    second-law-projected : (k : Laws2)
      → compute1 (fst (request2 k)) ≡ fst (expected2 k)
    second-law-projected k = M.Domain.law combined-domain (inr k)

module SelectionExample where
  module C = Composition Selection.State Selection.SelectionWitness First.selection-pair
  module D = C.WithSecond Nested.Example.second-domain (λ v → refl) (λ v p → p)
  agrees-at-request :
    fst (D.Direct.generator
      (inl Selection.request-false , (lift tt , lift tt))) ≡
    D.Two.flatten (fst (D.Two.C2.generator
      ((inl Selection.request-false , lift tt) , lift tt)))
  agrees-at-request = D.direct-output (inl Selection.request-false) (lift tt) (lift tt)
