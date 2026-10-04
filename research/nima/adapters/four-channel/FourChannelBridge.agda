{-# OPTIONS --safe --cubical --guardedness #-}
module FourChannelBridge where

open import Cubical.Foundations.Prelude hiding (comp)
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Sum.Base using (_⊎_; inl; inr)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Bool.Base using (Bool; false; true; _or_)
import Cubical.Data.Bool.Properties as B
open import Cubical.Data.Empty.Base using (⊥)
import Cubical.Data.Graph.Base as Graph
import Cubical.Categories.Category.Base as Cat
import Cubical.Categories.Constructions.Free.Category.Base as Free
import Cubical.Categories.UnderlyingGraph as Underlying
import RetainedComparisonStructure as R
open import OrdinaryYoneda
import NativeYoneda

-- Proposed interface, NOT an identification with every Marici transport.
-- These are four families of typed edges, with no multiplication selector.
record Channels (ℓ : Level) : Type (ℓ-suc ℓ) where
  field
    O R : Type ℓ
    OO : O → O → Type ℓ
    OR : O → R → Type ℓ
    RO : R → O → Type ℓ
    RR : R → R → Type ℓ

module Generated {ℓ : Level} (S : Channels ℓ) where
  open Channels S
  vertices : Type ℓ
  vertices = O ⊎ R
  edges : vertices → vertices → Type ℓ
  edges (inl a) (inl b) = OO a b
  edges (inl a) (inr b) = OR a b
  edges (inr a) (inl b) = RO a b
  edges (inr a) (inr b) = RR a b
  graph : Graph.Graph ℓ ℓ
  graph = record { Node = vertices ; Edge = edges }
  module Paths = Free.FreeCategory graph

  -- This ADDS freely generated identities/composition, modulo category laws.
  -- It does not infer which source arrows should be identified as composites.
  category : Category ℓ ℓ
  category = record
    { Ob = vertices ; Hom = Paths.Exp ; hom-set = λ _ _ → Paths.isSetExp
    ; unit = Paths.idₑ ; comp = λ g f → Paths._⋆ₑ_ f g
    ; unitL = Paths.⋆ₑIdR ; unitR = Paths.⋆ₑIdL
    ; assoc = λ k g f → Paths.⋆ₑAssoc f g k }
  module Yoneda = Theorem category

  -- The library proves existence AND uniqueness of the interpreting functor
  -- for each supplied graph interpretation into an existing target category.
  module Universal {a b : Level} (D : Cat.Category a b)
    (interpretation : Graph.GraphHom graph (Underlying.Cat→Graph D)) where
    open Paths.Semantics D interpretation public
      using (sem; sem-extends-ı; sem-uniq; sem-contr)

module Native (S : Channels ℓ-zero) where
  module G = Generated S
  module Retained = NativeYoneda.Adapter G.category

-- All four channel families are nonempty (two arrows in each).
-- Same endpoint sorts, arrows AND identities; different lawful composition.
xor-category or-category : Category ℓ-zero ℓ-zero
xor-category = record
  { Ob = Bool ; Hom = λ _ _ → Bool ; hom-set = λ _ _ → B.isSetBool
  ; unit = false ; comp = R.xor
  ; unitL = λ _ → refl ; unitR = R.xor-unitR ; assoc = R.xor-assoc }
or-category = record
  { Ob = Bool ; Hom = λ _ _ → Bool ; hom-set = λ _ _ → B.isSetBool
  ; unit = false ; comp = _or_
  ; unitL = λ _ → refl ; unitR = B.or-identityʳ ; assoc = B.or-assoc }

signature : (C : Category ℓ-zero ℓ-zero) → Category.Ob C → Category.Ob C → Channels ℓ-zero
signature C a b = record
  { O = Unit ; R = Unit
  ; OO = λ _ _ → Category.Hom C a a
  ; OR = λ _ _ → Category.Hom C a b
  ; RO = λ _ _ → Category.Hom C b a
  ; RR = λ _ _ → Category.Hom C b b }
same-channels : signature xor-category false true ≡ signature or-category false true
same-channels = refl
same-identity : Category.unit xor-category {false} ≡ Category.unit or-category {false}
same-identity = refl

-- No decoder from this signature can recover the marked loop multiplication
-- of both categories. Equality of channels even with marked units is insufficient.
no-composition-recovery :
  (decode : Channels ℓ-zero → Bool → Bool → Bool)
  → decode (signature xor-category false true) ≡ R.xor
  → decode (signature or-category false true) ≡ _or_
  → ⊥
no-composition-recovery decode recover-xor recover-or = B.false≢true
  (cong (λ op → op true true) (sym recover-xor ∙ cong decode same-channels ∙ recover-or))

-- Actual application, not just a reference to an unused construction.
module Example = Generated (signature xor-category false true)
free-yoneda : (F : Example.Yoneda.Presheaf ℓ-zero) (a : Example.vertices)
  → Example.Yoneda.At.Natural F a ≃ Example.Yoneda.Presheaf.Obj F a
free-yoneda F a = isoToEquiv (Example.Yoneda.At.yoneda F a)

-- Interpret the SAME free construction in the two incompatible source models.
to-library : {o h : Level} → Category o h → Cat.Category o h
to-library C = record
  { ob = Category.Ob C ; Hom[_,_] = Category.Hom C
  ; id = Category.unit C ; _⋆_ = λ f g → Category.comp C g f
  ; ⋆IdL = Category.unitR C ; ⋆IdR = Category.unitL C
  ; ⋆Assoc = λ f g k → Category.assoc C k g f
  ; isSetHom = Category.hom-set C _ _ }

vertex-label : Example.vertices → Bool
vertex-label (inl _) = false
vertex-label (inr _) = true
edge-label : {a b : Example.vertices} → Example.edges a b → Bool
edge-label {inl a} {inl b} e = e
edge-label {inl a} {inr b} e = e
edge-label {inr a} {inl b} e = e
edge-label {inr a} {inr b} e = e
or-interpretation : Graph.GraphHom Example.graph (Underlying.Cat→Graph (to-library or-category))
or-interpretation = record { _$g_ = vertex-label ; _<$g>_ = λ {x} {y} e → edge-label {x} {y} e }
xor-interpretation : Graph.GraphHom Example.graph (Underlying.Cat→Graph (to-library xor-category))
xor-interpretation = record { _$g_ = vertex-label ; _<$g>_ = λ {x} {y} e → edge-label {x} {y} e }
module OrEval = Example.Paths.Semantics (to-library or-category) or-interpretation
module XorEval = Example.Paths.Semantics (to-library xor-category) xor-interpretation

v : Example.vertices
v = inl tt
loop square : Example.Paths.Exp v v
loop = Example.Paths.↑ true
square = Example.Paths._⋆ₑ_ loop loop
free-square-not-unit : square ≡ Example.Paths.idₑ → ⊥
free-square-not-unit p = B.true≢false (cong OrEval.⟦_⟧ p)
xor-collapses-square : XorEval.⟦ square ⟧ ≡ XorEval.⟦ Example.Paths.idₑ {v} ⟧
xor-collapses-square = refl

-- A concrete witness that freely completing the edge signature does not
-- recover either source multiplication: the same path evaluates differently.
source-compositions-disagree : XorEval.⟦ square ⟧ ≡ OrEval.⟦ square ⟧ → ⊥
source-compositions-disagree p = B.false≢true p

-- A functor into xor identifies square with the unit, whereas a functor into
-- or separates them. These claims concern the free category of the weak
-- channel signature, not the original retained twelve-rule resolution.
