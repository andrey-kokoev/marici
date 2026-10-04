{-# OPTIONS --safe --cubical --guardedness #-}
module BarycentricRefinementCoherence where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Empty.Base using (⊥)
import BarycentricWitnessPacket as B
import GradedBoundaryCoherence as Higher

-- A carrier chooses the source cell for each refined cell. The geometry
-- checker separately verifies minimality, incidence and carrier composition.
-- This theorem covers typed annotations along FIXED carrier maps.
pull : {ℓ : Level} {I J : Type} (T : I → Type ℓ)
  → ((i : I) → T i) → (c : J → I) → (j : J) → T (c j)
pull T w c j = w (c j)

Preservation : {ℓ : Level} {I J : Type} (T : I → Type ℓ)
  (w : (i : I) → T i) (c : J → I) → Type ℓ
Preservation {J = J} T w c =
  Σ[ v ∈ ((j : J) → T (c j)) ] ((j : J) → w (c j) ≡ v j)

canonical : {ℓ : Level} {I J : Type} (T : I → Type ℓ)
  (w : (i : I) → T i) (c : J → I) → Preservation T w c
canonical T w c = pull T w c , λ j → refl

unique : {ℓ : Level} {I J : Type} (T : I → Type ℓ)
  (w : (i : I) → T i) (c : J → I) → isContr (Preservation T w c)
unique T w c = canonical T w c , λ { (v , p) i →
  (λ j → p j i) , (λ j k → p j (i ∧ k)) }

higher : {ℓ : Level} {I J : Type} (T : I → Type ℓ)
  (w : (i : I) → T i) (c : J → I) → isContr (isContr (Preservation T w c))
higher T w c = unique T w c , isPropIsContr (unique T w c)

module Compose {ℓ : Level} {I J K : Type} (T : I → Type ℓ)
  (w : (i : I) → T i) (c : J → I) (d : K → J) where

  composite : K → I
  composite k = c (d k)

  -- Type and term pullback are definitionally compatible with composition.
  pull-composes : pull (λ j → T (c j)) (pull T w c) d ≡ pull T w composite
  pull-composes = refl

  combine : (a : Preservation T w c)
    → Preservation (λ j → T (c j)) (fst a) d
    → Preservation T w composite
  combine a b = fst b , λ k → snd a (d k) ∙ snd b k

  comparison : (a : Preservation T w c)
    (b : Preservation (λ j → T (c j)) (fst a) d)
    → canonical T w composite ≡ combine a b
  comparison a b = snd (unique T w composite) (combine a b)

  -- Two alternative preservation routes admit a comparison in the SAME
  -- result type, including their comparison witnesses.
  routes-agree : (a b : Preservation T w composite) → a ≡ b
  routes-agree a b = sym (snd (unique T w composite) a) ∙ snd (unique T w composite) b

  comparisons-contractible : (a b : Preservation T w composite) → isContr (a ≡ b)
  comparisons-contractible a b = routes-agree a b , λ p →
    isProp→isSet (isContr→isProp (unique T w composite)) a b (routes-agree a b) p

-- Apply the general result to the actual generated tetrahedral packet.
module PacketRefinement {ℓ : Level} (S : Type ℓ)
  (G : (s : S) → Σ[ t ∈ S ] (s ≡ t)) (s : S)
  (J : Type) (carrier : J → B.Face) where
  module P = B.Packet S G s

  certificate : isContr (Preservation P.CellType P.cell carrier)
  certificate = unique P.CellType P.cell carrier

  retained : (j : J) → Σ[ f ∈ B.Face ] P.CellType f
  retained j = carrier j , fst (fst certificate) j

  mark-recovered : (j : J) → fst (retained j) ≡ carrier j
  mark-recovered j = refl

  witness-preserved : (j : J) → P.cell (carrier j) ≡ snd (retained j)
  witness-preserved j = snd (fst certificate) j

-- Geometry and a supplied type alone do not contract its annotation choices.
no-unconditional-label-contraction : isContr (Unit → Bool) → ⊥
no-unconditional-label-contraction c = false≢true
  (cong (λ f → f tt) (sym (snd c (λ _ → false)) ∙ snd c (λ _ → true)))

no-arbitrary-preservation : ((v : Unit → Bool) → (j : Unit) → false ≡ v j) → ⊥
no-arbitrary-preservation supply = false≢true (supply (λ _ → true) tt)

-- If both annotation values are fixed, their comparison space can retain
-- automorphisms. Contractibility above varies value AND comparison together.
module FixedAnnotations where
  Comparison : Type₁
  Comparison = (j : Unit) → Path (Type ℓ-zero) Bool Bool

  plain twisted : Comparison
  plain j = refl
  twisted j = Higher.twisted-filler

  distinct : plain ≡ twisted → ⊥
  distinct p = Higher.marked-fillers-distinct (cong (λ f → f tt) p)

  not-contractible : isContr Comparison → ⊥
  not-contractible c = distinct (sym (snd c plain) ∙ snd c twisted)

module BoolSource where
  T : Unit → Type
  T _ = Bool
  w : (i : Unit) → T i
  w _ = false
  carrier : Unit → Unit
  carrier i = i
  good : Preservation T w carrier
  good = canonical T w carrier
