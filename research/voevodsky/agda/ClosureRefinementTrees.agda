{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureRefinementTrees where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Unit
open import Cubical.Data.Nat using (ℕ; zero; suc; _+_)
open import Cubical.Data.Nat.Properties using (max)
open import Cubical.Data.Sum.Base using (_⊎_; inl; inr)
open import Cubical.Data.Sum.Properties using (⊎-equiv)
open import Cubical.Data.Sigma.Base using (_×_)
open import ClosureReferenceNormalForm using (module Model)

-- Trees carry LOCAL realization equivalences. Merely supplying a binary
-- shape would not justify a decomposition of an arbitrary root type.
-- Input branches are alternatives (sum), not jointly consumed products.
data InputTree : Type → Type₁ where
  inputLeaf : {A : Type} → InputTree A
  inputFork : {A L R : Type} → (L ⊎ R) ≃ A →
    InputTree L → InputTree R → InputTree A

data OutputTree : Type → Type₁ where
  outputLeaf : {B : Type} → OutputTree B
  outputFork : {B L R : Type} → B ≃ (L × R) →
    OutputTree L → OutputTree R → OutputTree B

-- A cut is a pruning: stop at a node, or expose both children and choose
-- their cuts independently. For each FIXED tree, its cuts are a small type.
InputCut : {A : Type} → InputTree A → Type
InputCut inputLeaf = Unit
InputCut (inputFork e l r) = Unit ⊎ (InputCut l × InputCut r)

OutputCut : {B : Type} → OutputTree B → Type
OutputCut outputLeaf = Unit
OutputCut (outputFork e l r) = Unit ⊎ (OutputCut l × OutputCut r)

inputRoot inputFull : {A : Type} (t : InputTree A) → InputCut t
inputRoot inputLeaf = tt
inputRoot (inputFork e l r) = inl tt
inputFull inputLeaf = tt
inputFull (inputFork e l r) = inr (inputFull l , inputFull r)

outputRoot outputFull : {B : Type} (t : OutputTree B) → OutputCut t
outputRoot outputLeaf = tt
outputRoot (outputFork e l r) = inl tt
outputFull outputLeaf = tt
outputFull (outputFork e l r) = inr (outputFull l , outputFull r)

InputAt : {A : Type} (t : InputTree A) → InputCut t → Type
InputAt {A} inputLeaf _ = A
InputAt {A} (inputFork e l r) (inl tt) = A
InputAt (inputFork e l r) (inr (cl , cr)) = InputAt l cl ⊎ InputAt r cr

OutputAt : {B : Type} (t : OutputTree B) → OutputCut t → Type
OutputAt {B} outputLeaf _ = B
OutputAt {B} (outputFork e l r) (inl tt) = B
OutputAt (outputFork e l r) (inr (cl , cr)) = OutputAt l cl × OutputAt r cr

private
  productEquiv : {A B C D : Type} → A ≃ B → C ≃ D → (A × C) ≃ (B × D)
  productEquiv e f = isoToEquiv (iso
    (λ p → equivFun e (fst p) , equivFun f (snd p))
    (λ p → invEq e (fst p) , invEq f (snd p))
    (λ p i → secEq e (fst p) i , secEq f (snd p) i)
    (λ p i → retEq e (fst p) i , retEq f (snd p) i))

-- Global frames are DERIVED recursively from the local node equivalences.
inputFrame : {A : Type} (t : InputTree A) (c : InputCut t) → InputAt t c ≃ A
inputFrame inputLeaf _ = idEquiv _
inputFrame (inputFork e l r) (inl tt) = idEquiv _
inputFrame (inputFork e l r) (inr (cl , cr)) =
  compEquiv (⊎-equiv (inputFrame l cl) (inputFrame r cr)) e

outputFrame : {B : Type} (t : OutputTree B) (c : OutputCut t) → OutputAt t c ≃ B
outputFrame outputLeaf _ = idEquiv _
outputFrame (outputFork e l r) (inl tt) = idEquiv _
outputFrame (outputFork e l r) (inr (cl , cr)) =
  compEquiv (productEquiv (outputFrame l cl) (outputFrame r cr)) (invEquiv e)

inputDepth : {A : Type} → InputTree A → ℕ
inputDepth inputLeaf = zero
inputDepth (inputFork e l r) = suc (max (inputDepth l) (inputDepth r))

outputDepth : {B : Type} → OutputTree B → ℕ
outputDepth outputLeaf = zero
outputDepth (outputFork e l r) = suc (max (outputDepth l) (outputDepth r))

inputWidth : {A : Type} (t : InputTree A) → InputCut t → ℕ
inputWidth inputLeaf _ = 1
inputWidth (inputFork e l r) (inl tt) = 1
inputWidth (inputFork e l r) (inr (cl , cr)) = inputWidth l cl + inputWidth r cr

outputWidth : {B : Type} (t : OutputTree B) → OutputCut t → ℕ
outputWidth outputLeaf _ = 1
outputWidth (outputFork e l r) (inl tt) = 1
outputWidth (outputFork e l r) (inr (cl , cr)) = outputWidth l cl + outputWidth r cr

module Realization {A B : Type} (inputs : InputTree A) (outputs : OutputTree B)
  (operation : A → B) where
  Cut : Type
  Cut = InputCut inputs × OutputCut outputs

  module Views = Model Cut
    (λ c → InputAt inputs (fst c)) (λ c → OutputAt outputs (snd c)) A B
    (λ c → inputFrame inputs (fst c)) (λ c → outputFrame outputs (snd c)) operation

  root full : Cut
  root = inputRoot inputs , outputRoot outputs
  full = inputFull inputs , outputFull outputs

  realize : (c : Cut) → InputAt inputs (fst c) → OutputAt outputs (snd c)
  realize = Views.view

-- Arbitrary finite BINARY trees, with independently pruned branches, are
-- supported. No homotopy dimension is inferred from tree depth. Dependent
-- or infinite branching and analytical node equivalences are not supplied
-- merely by these constructors.
