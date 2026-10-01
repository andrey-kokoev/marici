{-# OPTIONS --safe --cubical --guardedness #-}
module SeedPointedTriangleBinding where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.List.Base using (List; []; _∷_)
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
import BoundaryGeneratedQuestions as Boundary

open Whole.Universe ℓ-zero
open Resolution.Generators ℓ-zero

-- Explicit source admission, unlike choosing canonical endpoint seeds here.
module Contract (Admit : Complete → Type₁) (Occurrence : Type) where
  module App = Boundary.Application Admit

  record Binding : Type₁ where
    field
      A B C : Complete
      admitted-A : Resolve Admit A
      admitted-B : Resolve Admit B
      admitted-C : Resolve Admit C
      AB : Boundary.Filler A B
      BC : Boundary.Filler B C
      CA : Boundary.Filler C A
      id-AB id-BC id-CA : Occurrence
      AB≠BC : id-AB ≡ id-BC → ⊥
      BC≠CA : id-BC ≡ id-CA → ⊥
      CA≠AB : id-CA ≡ id-AB → ⊥

  module Supplied (b : Binding) where
    open Binding b

    AB-derivation : Resolve Admit (output (App.rule {a = A} {b = B} AB))
    AB-derivation = App.perform {a = A} {b = B} AB admitted-A admitted-B
    BC-derivation : Resolve Admit (output (App.rule {a = B} {b = C} BC))
    BC-derivation = App.perform {a = B} {b = C} BC admitted-B admitted-C
    CA-derivation : Resolve Admit (output (App.rule {a = C} {b = A} CA))
    CA-derivation = App.perform {a = C} {b = A} CA admitted-C admitted-A

    holonomy : Boundary.Filler A A
    holonomy = Boundary.compose {a = A} {b = C} {c = A}
      (Boundary.compose {a = A} {b = B} {c = C} AB BC) CA

    fixes-mark : equivFun (fst holonomy) (value A) ≡ value A
    fixes-mark = snd holonomy

    -- The composite comparison is supplied to the existing rule with its
    -- endpoint premises. No claim that this replaces the edge derivations.
    composite-derivation : Resolve Admit (output (App.rule {a = A} {b = A} holonomy))
    composite-derivation = App.perform {a = A} {b = A} holonomy admitted-A admitted-A

    ordered-occurrences : List Occurrence
    ordered-occurrences = id-AB ∷ id-BC ∷ id-CA ∷ []

    retained-composite : Complete
    retained-composite = Boundary.retain-filler A A holonomy

    composite-recovered : value retained-composite ≡ holonomy
    composite-recovered = refl

  -- Retain the binding and its actual endpoint derivations. All three edge
  -- derivations and the composite above remain reconstructible from it.
  retained-binding : Binding → Whole.Universe.Complete (ℓ-suc ℓ-zero)
  retained-binding b = Whole.Universe.pack (Whole.Universe.atom Binding) b

  binding-recovered : (b : Binding) → Whole.Universe.value (retained-binding b) ≡ b
  binding-recovered b = refl

-- Existing general pointed loops are not forced to identity. This theorem
-- imports the source counterexample without assigning it to the seed.
pointed-nonflat-control : Boundary.identity Boundary.fourQ ≡ Boundary.swap-filler → ⊥
pointed-nonflat-control = Boundary.fillers-distinct
