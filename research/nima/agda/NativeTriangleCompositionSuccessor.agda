{-# OPTIONS --safe --cubical --guardedness #-}
module NativeTriangleCompositionSuccessor where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.List.Base using (List; []; _∷_; _++_; map; length)
open import Cubical.Data.Maybe.Base using (Maybe; nothing; just)
import SeedAttachedObserver as Seed
import IndexedConstructorTables as Tables
import NativeTableRules as Rules
import NativeApplicationExtension as Application
open Seed using (Vertex; A; B; C; D)

Edge : Type
Edge = Σ Vertex Seed.Out
end : Edge → Vertex
end e = Seed.target (snd e)

match : (x y : Vertex) → Maybe (x ≡ y)
match A A = just refl
match B B = just refl
match C C = just refl
match D D = just refl
match _ _ = nothing

record Joined : Type where
  constructor joined
  field
    first second : Edge
    seam : end first ≡ fst second

sew : (a b : Edge) → List Joined
sew a b with match (end a) (fst b)
... | nothing = []
... | just p = joined a b p ∷ []

row : Edge → List Edge → List Joined
row a [] = []
row a (b ∷ bs) = sew a b ++ row a bs
compose : List Edge → List Edge → List Joined
compose [] ys = []
compose (x ∷ xs) ys = row x ys ++ compose xs ys

Input : Type
Input = List Edge × List Edge
record Next : Type where
  constructor next
  field
    parents : Input
    words : List Joined
    constructed : words ≡ compose (fst parents) (snd parents)

construct : Input → Next
construct p = next p (compose (fst p) (snd p)) refl
recover-parents : (p : Input) → Next.parents (construct p) ≡ p
recover-parents p = refl

targets : Next → List Vertex
targets n = map (λ w → end (Joined.second w)) (Next.words n)

left right : List Edge
left = (A , Seed.AB) ∷ (B , Seed.BC) ∷ (C , Seed.CA) ∷ []
right = (B , Seed.BA) ∷ (A , Seed.AD) ∷ (D , Seed.DB) ∷ []
LR RL : Next
LR = construct (left , right)
RL = construct (right , left)
LR-targets : targets LR ≡ A ∷ D ∷ []
LR-targets = refl
RL-targets : targets RL ≡ B ∷ C ∷ []
RL-targets = refl
LR-count : length (Next.words LR) ≡ 2
LR-count = refl
RL-count : length (Next.words RL) ≡ 2
RL-count = refl

-- Admission is explicit: input, composition function and reader are seeds.
-- The joined output and the retained next derivation are NOT seeds.
module Native (p : Input) where
  module G = Tables.Core ℓ-zero
  module N = Rules.Native ℓ-zero
  module E = Application.Extension ℓ-zero
  build : E.Application
  build = record
    { A = Input ; B = λ _ → Next
    ; argument-code = G.atom-node Input ; result-code = λ _ → G.atom-node Next
    ; function-code = G.atom-node (Input → Next)
    ; function = construct ; argument = p }
  read-next : E.Application
  read-next = record
    { A = Next ; B = λ _ → List Vertex
    ; argument-code = N.expression (E.result build)
    ; result-code = λ _ → G.atom-node (List Vertex)
    ; function-code = G.atom-node (Next → List Vertex)
    ; function = targets ; argument = N.value (E.result build) }
  data SeedBasis : G.Package → Type₁ where
    initial : SeedBasis (E.argument-input build)
    operation : SeedBasis (E.function-input build)
    reader : SeedBasis (E.function-input read-next)
  module Run = E.Runtime SeedBasis
  derived : Run.New.Resolve (E.result build)
  derived = Run.execute build (Run.New.seed operation) (Run.New.seed initial)
  observed : Run.New.Resolve (E.result read-next)
  observed = Run.execute read-next (Run.New.seed reader) derived
  promoted : Run.UpG.Package
  promoted = Run.reify (E.result build , derived)
  derivation-recovered : snd (Run.UpN.value promoted) ≡ derived
  derivation-recovered = refl

module Forward = Native (left , right)
module Reverse = Native (right , left)
