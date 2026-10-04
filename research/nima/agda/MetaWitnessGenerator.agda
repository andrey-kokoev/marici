{-# OPTIONS --safe --cubical --guardedness #-}
module MetaWitnessGenerator where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sum.Base using (_⊎_; inl; inr)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Bool.Base using (Bool; false; true; not)
open import TypedGeneratorLayers using (Layer1; module Histories)

-- A bounded meta-generator: the base WG and the desired operation share a
-- state type. Compatibility and closure of admitted states are explicit data.
module Specialize {ℓ : Level} (S : Type ℓ) (R : S → S → Type ℓ) where
  WG : Type ℓ
  WG = (s : S) → Σ[ t ∈ S ] R s t

  record Domain : Type (ℓ-suc ℓ) where
    field
      compute : S → S
      Allowed : S → Type ℓ
      LawInput : Type ℓ
      request : LawInput → S
      expected : LawInput → S
      law : (k : LawInput) → compute (request k) ≡ expected k

  record Compatible : Type (ℓ-suc ℓ) where
    field
      domain : Domain
      base : WG
      agrees : (s : S) → fst (base s) ≡ Domain.compute domain s
      closed : (s : S) → Domain.Allowed domain s
        → Domain.Allowed domain (fst (base s))

  module Compiled (input : Compatible) where
    open Compatible input
    open Domain domain
    State : Type ℓ
    State = Σ[ s ∈ S ] Allowed s
    LawEvidence : S → Type ℓ
    LawEvidence s = (k : LawInput) → request k ≡ s → compute s ≡ expected k

    evidence : (s : S) → LawEvidence s
    evidence s k p = cong compute (sym p) ∙ law k

    Relation : State → State → Type ℓ
    Relation (s , _) (t , _) = R s t × ((t ≡ compute s) × LawEvidence s)

    generator : (v : State) → Σ[ w ∈ State ] Relation v w
    generator (s , ok) =
      (fst (base s) , closed s ok) ,
      (snd (base s) , (agrees s , evidence s))

    domain-WG : Layer1 ℓ
    domain-WG = record { State = State ; Witness = Relation ; generate = generator }
    module H = Histories domain-WG

    -- The law used to compare a step with its expected result is read from
    -- the actual step witness, not from a second, detached certificate.
    law-from-step : (k : LawInput) (ok : Allowed (request k))
      → fst (fst (generator (request k , ok))) ≡ expected k
    law-from-step k ok =
      fst (snd (snd (generator (request k , ok)))) ∙
      snd (snd (snd (generator (request k , ok)))) k refl

    law-history : (k : LawInput) (ok : Allowed (request k))
      → H.History (request k , ok) (fst (generator (request k , ok)))
    law-history k ok = H.single (snd (generator (request k , ok)))

    -- These projections retain both the domain specification and the base WG.
    output : Type (ℓ-suc ℓ)
    output = Σ[ original ∈ Compatible ] Layer1 ℓ
    compiled : output
    compiled = input , domain-WG
    source-recovered : fst compiled ≡ input
    source-recovered = refl
    law-certificate : (k : LawInput) → compute (request k) ≡ expected k
    law-certificate = law

  -- The meta-level is itself a WG: it accepts a *certified pair* of desired
  -- domain and WG, and produces their specialization plus an origin witness.
  MetaState : Type (ℓ-suc ℓ)
  MetaState = Compatible ⊎ (Σ[ input ∈ Compatible ] Layer1 ℓ)

  data MetaWitness : MetaState → MetaState → Type (ℓ-suc ℓ) where
    specialized : (input : Compatible)
      → MetaWitness (inl input) (inr (input , Compiled.domain-WG input))
    retained : (input : Compatible) (L : Layer1 ℓ)
      → MetaWitness (inr (input , L)) (inr (input , L))

  meta-generate : (v : MetaState) → Σ[ w ∈ MetaState ] MetaWitness v w
  meta-generate (inl input) = inr (input , Compiled.domain-WG input) , specialized input
  meta-generate (inr (input , L)) = inr (input , L) , retained input L

  meta-WG : Layer1 (ℓ-suc ℓ)
  meta-WG = record { State = MetaState ; Witness = MetaWitness ; generate = meta-generate }

  meta-retains-input : (input : Compatible)
    → fst (meta-generate (inl input)) ≡ inr (input , Compiled.domain-WG input)
  meta-retains-input input = refl

-- Non-identity example: specialize the Boolean-negation WG to an admitted
-- domain whose requested law is double negation. The base generator is used
-- as the actual transition; it is not replaced by the domain operation.
module BooleanExample = Specialize Bool (λ s t → t ≡ not s)
boolean-domain : BooleanExample.Domain
boolean-domain = record
  { compute = not ; Allowed = λ _ → Bool
  ; LawInput = Bool ; request = not ; expected = λ b → b
  ; law = λ { false → refl ; true → refl } }
boolean-base : BooleanExample.WG
boolean-base s = not s , refl
boolean-pair : BooleanExample.Compatible
boolean-pair = record
  { domain = boolean-domain ; base = boolean-base
  ; agrees = λ s → refl ; closed = λ s ok → ok }
module BooleanSpecialized = BooleanExample.Compiled boolean-pair
boolean-specialization-test :
  fst (BooleanSpecialized.generator (false , true)) ≡ (true , true)
boolean-specialization-test = refl

-- The two-step law is read from the generated transition at request(false)=true.
boolean-law-from-history :
  fst (fst (BooleanSpecialized.generator (true , true))) ≡ false
boolean-law-from-history = BooleanSpecialized.law-from-step false true

boolean-retained-law-history :
  BooleanSpecialized.H.History (true , true)
    (fst (BooleanSpecialized.generator (true , true)))
boolean-retained-law-history = BooleanSpecialized.law-history false true
