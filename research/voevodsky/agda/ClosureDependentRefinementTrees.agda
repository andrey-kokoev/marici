{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureDependentRefinementTrees where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Unit
open import Cubical.Data.Nat using (ℕ; suc)
open import Cubical.Data.Sum.Base using (_⊎_; inl; inr)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Sigma.Properties using (Σ-cong-equiv-snd)
open import ClosureReferenceNormalForm using (module Model)
import Cubical.HITs.Pushout.Base as PO
open import ClosurePushoutRefinement using (module Span)

-- The natural number is a DEPTH BOUND. Branch indices may be arbitrary small
-- types, including higher types. This does not assert a finite node count.
-- Node labels distinguish a selected dependent pair (Σ) from all components
-- of a dependent function (Π), or gluing over a shared boundary (pushout).
-- The semantics is not inferred from tree side.
data Tree (A : Type) : ℕ → Type₁ where
  leaf : {n : ℕ} → Tree A n
  sigmaNode : {n : ℕ} {I : Type} {B : I → Type} →
    (Σ I B) ≃ A → ((i : I) → Tree (B i) n) → Tree A (suc n)
  piNode : {n : ℕ} {I : Type} {B : I → Type} →
    ((i : I) → B i) ≃ A → ((i : I) → Tree (B i) n) → Tree A (suc n)
  glueNode : {n : ℕ} {L M R : Type} (f : M → L) (g : M → R) →
    PO.Pushout f g ≃ A → Tree L n → Tree M n → Tree R n → Tree A (suc n)

Cut : {A : Type} {n : ℕ} → Tree A n → Type
Cut leaf = Unit
Cut (sigmaNode {I = I} e children) = Unit ⊎ ((i : I) → Cut (children i))
Cut (piNode {I = I} e children) = Unit ⊎ ((i : I) → Cut (children i))
Cut (glueNode f g e l m r) = Unit ⊎ (Cut l × (Cut m × Cut r))

root full : {A : Type} {n : ℕ} (t : Tree A n) → Cut t
root leaf = tt
root (sigmaNode e children) = inl tt
root (piNode e children) = inl tt
root (glueNode f g e l m r) = inl tt
full leaf = tt
full (sigmaNode e children) = inr (λ i → full (children i))
full (piNode e children) = inr (λ i → full (children i))
full (glueNode f g e l m r) = inr (full l , (full m , full r))

-- At and frame are mutually recursive only on STRICTLY SMALLER subtrees.
-- A refined pushout needs the child frames to type its attachment maps.
mutual
  At : {A : Type} {n : ℕ} (t : Tree A n) → Cut t → Type
  At {A} leaf _ = A
  At {A} (sigmaNode e children) (inl tt) = A
  At (sigmaNode {I = I} e children) (inr cuts) = Σ[ i ∈ I ] At (children i) (cuts i)
  At {A} (piNode e children) (inl tt) = A
  At (piNode {I = I} e children) (inr cuts) = (i : I) → At (children i) (cuts i)
  At {A} (glueNode f g e l m r) (inl tt) = A
  At (glueNode f g e l m r) (inr (cl , (cm , cr))) =
    Span.Space f g (frame m cm) (frame l cl) (frame r cr)

  -- Global frames are derived, including the required attachment squares.
  frame : {A : Type} {n : ℕ} (t : Tree A n) (c : Cut t) → At t c ≃ A
  frame leaf _ = idEquiv _
  frame (sigmaNode e children) (inl tt) = idEquiv _
  frame (sigmaNode e children) (inr cuts) =
    compEquiv (Σ-cong-equiv-snd (λ i → frame (children i) (cuts i))) e
  frame (piNode e children) (inl tt) = idEquiv _
  frame (piNode e children) (inr cuts) =
    compEquiv (equivΠCod (λ i → frame (children i) (cuts i))) e
  frame (glueNode f g e l m r) (inl tt) = idEquiv _
  frame (glueNode f g e l m r) (inr (cl , (cm , cr))) =
    compEquiv (Span.comparison f g (frame m cm) (frame l cl) (frame r cr)) e

-- The selected base index of a Σ node is preserved by the expanded frame,
-- up to the node's explicit equivalence. No constant-fiber assumption enters.
sigmaObservation : {A I : Type} {B : I → Type} {n : ℕ}
  (e : (Σ I B) ≃ A) (children : (i : I) → Tree (B i) n)
  (cuts : (i : I) → Cut (children i))
  (z : At (sigmaNode e children) (inr cuts)) →
  fst (invEq e (equivFun (frame (sigmaNode e children) (inr cuts)) z)) ≡ fst z
sigmaObservation e children cuts (i , x) = cong fst
  (retEq e (i , equivFun (frame (children i) (cuts i)) x))

module Realization {A B : Type} {n m : ℕ}
  (inputs : Tree A n) (outputs : Tree B m) (operation : A → B) where
  Cuts : Type
  Cuts = Cut inputs × Cut outputs

  module Views = Model Cuts
    (λ c → At inputs (fst c)) (λ c → At outputs (snd c)) A B
    (λ c → frame inputs (fst c)) (λ c → frame outputs (snd c)) operation

  rootCut fullCut : Cuts
  rootCut = root inputs , root outputs
  fullCut = full inputs , full outputs

  realize : (c : Cuts) → At inputs (fst c) → At outputs (snd c)
  realize = Views.view

-- Dependent Σ/Π and homotopy-pushout nodes can occur in the same tree.
-- A glue node requires its actual span and a proved local realization
-- equivalence. This does not supply analytical spans, arbitrary comparison
-- maps between different trees, or unbounded-depth completions.
