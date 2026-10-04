{-# OPTIONS --safe --cubical --guardedness #-}
module DomainWitnessCompiler where

open import Cubical.Foundations.Prelude hiding (comp)
open import Cubical.Data.Sum.Base using (_⊎_; inl; inr)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Bool.Base using (Bool; not; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty.Base using (⊥)
open import TypedGeneratorLayers using (Layer1; module Histories)
open import OrdinaryYoneda using (Category)

-- The same compiler accepts any supplied dependent computation. Its output
-- value and beta witness are computed, not independently admitted as seeds.
record Presentation (ℓ : Level) : Type (ℓ-suc ℓ) where
  field
    Input : Type ℓ
    Output : Input → Type ℓ
    compute : (i : Input) → Output i

module Compile {ℓ : Level} (P : Presentation ℓ) where
  open Presentation P

  State : Type ℓ
  State = Input ⊎ (Σ[ i ∈ Input ] Output i)

  data Witness : State → State → Type ℓ where
    evaluated : (i : Input) → Witness (inl i) (inr (i , compute i))
    idle : (i : Input) (y : Output i) → Witness (inr (i , y)) (inr (i , y))

  run : (s : State) → Σ[ t ∈ State ] Witness s t
  run (inl i) = inr (i , compute i) , evaluated i
  run (inr (i , y)) = inr (i , y) , idle i y

  layer : Layer1 ℓ
  layer = record { State = State ; Witness = Witness ; generate = run }

  result : (i : Input) → Output i
  result = compute

  result-beta : (i : Input) → result i ≡ compute i
  result-beta i = refl

  -- The output state retains the exact request index, even when its value
  -- differs from the index. No inverse computation is asserted.
  retained-input : (i : Input) → fst (run (inl i)) ≡ inr (i , compute i)
  retained-input i = refl

-- An admission policy restricts requests without adding a result seed.
-- The certificate is retained as part of the request index.
module Admitted {ℓ : Level} (P : Presentation ℓ)
  (Allowed : Presentation.Input P → Type ℓ) where
  open Presentation P
  restricted : Presentation ℓ
  restricted = record
    { Input = Σ[ i ∈ Input ] Allowed i
    ; Output = λ { (i , _) → Output i }
    ; compute = λ { (i , _) → compute i } }
  module Generated = Compile restricted
  restricted-beta : (i : Input) (ok : Allowed i)
    → Generated.result (i , ok) ≡ compute i
  restricted-beta i ok = refl

-- A domain law is a supplied equation, not an equality inferred from types.
-- Compilation records the exact law input and its proof in a typed package.
record LawPresentation (ℓ : Level) : Type (ℓ-suc ℓ) where
  field
    Context : Type ℓ
    Carrier : Context → Type ℓ
    left right : (k : Context) → Carrier k
    law : (k : Context) → left k ≡ right k

module CompileLaw {ℓ : Level} (L : LawPresentation ℓ) where
  open LawPresentation L
  law-presentation : Presentation ℓ
  law-presentation = record
    { Input = Context ; Output = λ k → left k ≡ right k ; compute = law }
  module Generated = Compile law-presentation
  Certificate : Type ℓ
  Certificate = Σ[ k ∈ Context ] (left k ≡ right k)
  certify : Context → Certificate
  certify k = k , Generated.result k
  recover-context : (k : Context) → fst (certify k) ≡ k
  recover-context k = refl
  recover-law : (k : Context) → snd (certify k) ≡ law k
  recover-law k = refl

-- One presentation now links admission and a law to the SAME operation.
-- The law's left side is necessarily computed by the operation, not a
-- separately supplied expression. Its proof remains supplied domain data.
record DomainPresentation (ℓ : Level) : Type (ℓ-suc ℓ) where
  field
    operation : Presentation ℓ
  open Presentation operation public
  field
    Allowed : Input → Type ℓ
    LawInput : Type ℓ
    request : LawInput → Σ[ i ∈ Input ] Allowed i
    expected : (k : LawInput) → Output (fst (request k))
    law : (k : LawInput) → compute (fst (request k)) ≡ expected k

module CompileDomain {ℓ : Level} (D : DomainPresentation ℓ) where
  open DomainPresentation D
  module Restricted = Admitted operation Allowed
  module G = Restricted.Generated
  module H = Histories G.layer

  execute-law : (k : LawInput)
    → Σ[ t ∈ G.State ]
        (G.Witness (inl (request k)) t ×
         (G.result (request k) ≡ expected k))
  execute-law k = fst (G.run (inl (request k))) ,
    (snd (G.run (inl (request k))) , law k)

  retained-history : (k : LawInput)
    → H.History (inl (request k)) (fst (G.run (inl (request k))))
  retained-history k = H.single (snd (G.run (inl (request k))))

  law-beta : (k : LawInput) → G.result (request k) ≡ expected k
  law-beta = law

bool-presentation : Presentation ℓ-zero
bool-presentation = record
  { Input = Bool ; Output = λ _ → Bool ; compute = not }
module Boolean = Compile bool-presentation
boolean-test : Boolean.result false ≡ true
boolean-test = refl

identity-presentation : Presentation ℓ-zero
identity-presentation = record
  { Input = Bool ; Output = λ _ → Bool ; compute = λ b → b }
module BooleanIdentity = Compile identity-presentation
same-signature-different-operation :
  BooleanIdentity.result false ≡ Boolean.result false → ⊥
same-signature-different-operation p = false≢true p

-- Only admitted false requests may enter this restricted instance.
module AdmittedBoolean = Admitted bool-presentation (λ b → b ≡ false)
admitted-boolean-test : AdmittedBoolean.Generated.result (false , refl) ≡ true
admitted-boolean-test = refl

bool-involution : Bool → Bool
bool-involution false = false
bool-involution true = true
bool-law : LawPresentation ℓ-zero
bool-law = record
  { Context = Bool ; Carrier = λ _ → Bool
  ; left = λ b → not (not b) ; right = bool-involution
  ; law = λ { false → refl ; true → refl } }
module BooleanLaw = CompileLaw bool-law

boolean-domain : DomainPresentation ℓ-zero
boolean-domain = record
  { operation = bool-presentation ; Allowed = λ _ → Bool
  ; LawInput = Bool ; request = λ b → not b , true
  ; expected = λ b → b
  ; law = λ { false → refl ; true → refl } }
module BooleanDomain = CompileDomain boolean-domain
boolean-domain-test : BooleanDomain.G.result (false , true) ≡ true
boolean-domain-test = refl

-- The categorical instance takes a *supplied* lawful category. The compiler
-- is unchanged: it specializes the typed composable pair into its composite.
module Composition {ℓ : Level} (C : Category ℓ ℓ)
  (a b c : Category.Ob C) where
  open Category C
  presentation : Presentation ℓ
  presentation = record
    { Input = Hom b c × Hom a b
    ; Output = λ _ → Hom a c
    ; compute = λ { (g , f) → comp g f } }
  module Generated = Compile presentation
  composite : Hom b c → Hom a b → Hom a c
  composite g f = Generated.result (g , f)
  composite-beta : (g : Hom b c) (f : Hom a b) → composite g f ≡ comp g f
  composite-beta g f = Generated.result-beta (g , f)

-- Unit is an equation about the very same composition operation, with the
-- same input admission policy. Composition and its proof are not duplicated.
module CategoryUnitDomain {ℓ : Level} (C : Category ℓ ℓ)
  (a b : Category.Ob C) where
  open Category C
  module Op = Composition C a b b
  domain : DomainPresentation ℓ
  domain = record
    { operation = Op.presentation ; Allowed = λ _ → Hom a b
    ; LawInput = Hom a b
    ; request = λ f → (unit , f) , f
    ; expected = λ f → f
    ; law = λ f → unitL f }
  module Generated = CompileDomain domain
  unit-history : (f : Hom a b)
    → Generated.H.History (inl ((unit , f) , f))
        (fst (Generated.G.run (inl ((unit , f) , f))))
  unit-history f = Generated.retained-history f

module CategoryAssociativity {ℓ : Level} (C : Category ℓ ℓ)
  (a b c d : Category.Ob C) where
  open Category C
  presentation : LawPresentation ℓ
  presentation = record
    { Context = Hom c d × (Hom b c × Hom a b)
    ; Carrier = λ _ → Hom a d
    ; left = λ { (k , (g , f)) → comp k (comp g f) }
    ; right = λ { (k , (g , f)) → comp (comp k g) f }
    ; law = λ { (k , (g , f)) → assoc k g f } }
  module Generated = CompileLaw presentation
  law-input-retained : (k : Hom c d) (g : Hom b c) (f : Hom a b)
    → fst (Generated.certify (k , (g , f))) ≡ (k , (g , f))
  law-input-retained k g f = refl
