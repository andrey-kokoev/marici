{-# OPTIONS --safe --cubical --guardedness #-}
module WitnessSelectionGenerator where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false)
open import Cubical.Data.Sum.Base using (_⊎_; inl; inr)
open import TypedGeneratorLayers using (Layer1)
import WitnessHistoryFamily as Hist
import NativeApplicationExtension as Application
import IndexedConstructorTables as Tables
import NativeTableRules as Rules

module E = Application.Extension ℓ-zero
module G = Tables.Core ℓ-zero
module N = Rules.Native ℓ-zero

-- A uniform certified-index policy: the family and an actual index package
-- are the only admitted inputs, never a selected output/history package.
index : Bool → G.Package
index b = N.pack (G.atom-node Bool) b

selection : Bool → E.Application
selection b = record
  { A = Bool
  ; B = λ i → Hist.H.History (Hist.start i) (Hist.H.at 2 (Hist.start i))
  ; argument-code = G.atom-node Bool
  ; result-code = λ i → G.atom-node
      (Hist.H.History (Hist.start i) (Hist.H.at 2 (Hist.start i)))
  ; function-code = G.P-node Bool (λ i → N.retained (Hist.component i))
  ; function = Hist.two-steps
  ; argument = b }

function-shape : (b : Bool) → E.function-input (selection b) ≡ Hist.history-family
function-shape b = refl
argument-shape : (b : Bool) → E.argument-input (selection b) ≡ index b
argument-shape b = refl

data Seed : G.Package → Type (ℓ-suc ℓ-zero) where
  family-seed : Seed Hist.history-family
  index-seed : (b : Bool) → Seed (index b)
module Runtime = E.Runtime Seed

-- The request carries actual derivations, not mere values of its packages.
record Request : Type (ℓ-suc ℓ-zero) where
  field
    chosen : Bool
    family-proof : Runtime.New.Resolve (E.function-input (selection chosen))
    index-proof : Runtime.New.Resolve (E.argument-input (selection chosen))

execute : (q : Request) → Runtime.New.Resolve (E.result (selection (Request.chosen q)))
execute q = Runtime.execute (selection (Request.chosen q))
  (Request.family-proof q) (Request.index-proof q)

-- The output contains a derivation and an explicit trace identifying it with
-- execution from these very premises. The witness also retains the request.
Answer : Request → Type (ℓ-suc ℓ-zero)
Answer q = Σ[ d ∈ Runtime.New.Resolve (E.result (selection (Request.chosen q))) ]
  (d ≡ execute q)

State : Type (ℓ-suc ℓ-zero)
State = Request ⊎ (Σ[ q ∈ Request ] Answer q)

data SelectionWitness : State → State → Type (ℓ-suc ℓ-zero) where
  selected : (q : Request) → SelectionWitness (inl q) (inr (q , (execute q , refl)))
  idle : (q : Request) (a : Answer q) → SelectionWitness (inr (q , a)) (inr (q , a))

select : (s : State) → Σ[ t ∈ State ] SelectionWitness s t
select (inl q) = inr (q , (execute q , refl)) , selected q
select (inr (q , a)) = inr (q , a) , idle q a

selection-WG : Layer1 (ℓ-suc ℓ-zero)
selection-WG = record { State = State ; Witness = SelectionWitness ; generate = select }

-- An actual nonempty-history fixture, with no selected-history seed.
request-false : Request
request-false = record
  { chosen = false
  ; family-proof = Runtime.New.seed family-seed
  ; index-proof = Runtime.New.seed (index-seed false) }

selection-retains-request : fst (select (inl request-false)) ≡
  inr (request-false , (execute request-false , refl))
selection-retains-request = refl

selected-history : N.value (E.result (selection false)) ≡ Hist.two-steps false
selected-history = refl
