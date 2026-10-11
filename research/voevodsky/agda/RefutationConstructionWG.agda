{-# OPTIONS --safe --cubical --guardedness #-}
module RefutationConstructionWG where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ)
open import Cubical.Data.List.Base using (List; []; _∷_)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Sum.Base using (_⊎_; inl; inr)
open import Cubical.Data.Empty.Base using (⊥)
import DomainWitnessCompiler as DWC

-- Source formulas and intrinsically typed natural-deduction certificates.
data Formula : Type where
  atom : ℕ → Formula
  bottom : Formula
  product arrow : Formula → Formula → Formula

Context = List Formula

data Member (A : Formula) : Context → Type where
  here : {Γ : Context} → Member A (A ∷ Γ)
  there : {Γ : Context} {B : Formula} → Member A Γ → Member A (B ∷ Γ)

data Proof (Γ : Context) : Formula → Type where
  hypothesis : {A : Formula} → Member A Γ → Proof Γ A
  pair : {A B : Formula} → Proof Γ A → Proof Γ B → Proof Γ (product A B)
  first : {A B : Formula} → Proof Γ (product A B) → Proof Γ A
  second : {A B : Formula} → Proof Γ (product A B) → Proof Γ B
  abstraction : {A B : Formula} → Proof (A ∷ Γ) B → Proof Γ (arrow A B)
  application : {A B : Formula} → Proof Γ (arrow A B) → Proof Γ A → Proof Γ B

module Semantics {ℓ : Level} (interpret-atom : ℕ → Type ℓ) where
  Meaning : Formula → Type ℓ
  Meaning (atom n) = interpret-atom n
  Meaning bottom = Lift ⊥
  Meaning (product A B) = Meaning A × Meaning B
  Meaning (arrow A B) = Meaning A → Meaning B

  Environment : Context → Type ℓ
  Environment Γ = {A : Formula} → Member A Γ → Meaning A

  extend : {Γ : Context} {A : Formula} → Environment Γ → Meaning A → Environment (A ∷ Γ)
  extend ρ a here = a
  extend ρ a (there i) = ρ i

  evaluate : {Γ : Context} {A : Formula} → Proof Γ A → Environment Γ → Meaning A
  evaluate (hypothesis i) ρ = ρ i
  evaluate (pair p q) ρ = evaluate p ρ , evaluate q ρ
  evaluate (first p) ρ = fst (evaluate p ρ)
  evaluate (second p) ρ = snd (evaluate p ρ)
  evaluate (abstraction p) ρ = λ a → evaluate p (extend ρ a)
  evaluate (application f a) ρ = evaluate f ρ (evaluate a ρ)

-- A request describes ONE rule and its already-certified premises, not a
-- supplied proof of the requested conclusion. Even abstraction changes context.
data Frame (Γ : Context) : Formula → Type where
  lookup : {A : Formula} → Member A Γ → Frame Γ A
  pairing : {A B : Formula} → Proof Γ A → Proof Γ B → Frame Γ (product A B)
  project-left : {A B : Formula} → Proof Γ (product A B) → Frame Γ A
  project-right : {A B : Formula} → Proof Γ (product A B) → Frame Γ B
  bind : {A B : Formula} → Proof (A ∷ Γ) B → Frame Γ (arrow A B)
  apply : {A B : Formula} → Proof Γ (arrow A B) → Proof Γ A → Frame Γ B

assemble : {Γ : Context} {A : Formula} → Frame Γ A → Proof Γ A
assemble (lookup i) = hypothesis i
assemble (pairing p q) = pair p q
assemble (project-left p) = first p
assemble (project-right p) = second p
assemble (bind p) = abstraction p
assemble (apply f a) = application f a

module RuleWG (Γ : Context) (A : Formula) where
  presentation : DWC.Presentation ℓ-zero
  presentation = record
    { Input = Frame Γ A ; Output = λ _ → Proof Γ A ; compute = assemble }
  module G = DWC.Compile presentation

-- Rebuild the entire certificate by one WG invocation per constructor.
construct : {Γ : Context} {A : Formula} → Proof Γ A → Proof Γ A
construct {Γ} {A} (hypothesis i) = RuleWG.G.result Γ A (lookup i)
construct {Γ} {A} (pair p q) = RuleWG.G.result Γ A (pairing (construct p) (construct q))
construct {Γ} {A} (first p) = RuleWG.G.result Γ A (project-left (construct p))
construct {Γ} {A} (second p) = RuleWG.G.result Γ A (project-right (construct p))
construct {Γ} {A} (abstraction p) = RuleWG.G.result Γ A (bind (construct p))
construct {Γ} {A} (application f a) = RuleWG.G.result Γ A (apply (construct f) (construct a))

construct-correct : {Γ : Context} {A : Formula} (d : Proof Γ A) → construct d ≡ d
construct-correct (hypothesis i) = refl
construct-correct (pair p q) = cong₂ pair (construct-correct p) (construct-correct q)
construct-correct (first p) = cong first (construct-correct p)
construct-correct (second p) = cong second (construct-correct p)
construct-correct (abstraction p) = cong abstraction (construct-correct p)
construct-correct (application f a) = cong₂ application (construct-correct f) (construct-correct a)

-- The trace retains each actual compiler edge and every premise trace.
Edge : {Γ : Context} {A : Formula} → Frame Γ A → Type
Edge {Γ} {A} r = RuleWG.G.Witness Γ A (inl r) (inr (r , assemble r))

Trace : {Γ : Context} {A : Formula} → Proof Γ A → Type
Trace (hypothesis i) = Edge (lookup i)
Trace (pair p q) = Trace p × Trace q × Edge (pairing (construct p) (construct q))
Trace (first p) = Trace p × Edge (project-left (construct p))
Trace (second p) = Trace p × Edge (project-right (construct p))
Trace (abstraction p) = Trace p × Edge (bind (construct p))
Trace (application f a) = Trace f × Trace a × Edge (apply (construct f) (construct a))

step : {Γ : Context} {A : Formula} (r : Frame Γ A) → Edge r
step {Γ} {A} r = RuleWG.G.evaluated r

trace : {Γ : Context} {A : Formula} (d : Proof Γ A) → Trace d
trace (hypothesis i) = step (lookup i)
trace (pair p q) = trace p , trace q , step (pairing (construct p) (construct q))
trace (first p) = trace p , step (project-left (construct p))
trace (second p) = trace p , step (project-right (construct p))
trace (abstraction p) = trace p , step (bind (construct p))
trace (application f a) = trace f , trace a , step (apply (construct f) (construct a))

module Sound {ℓ : Level} (interpret-atom : ℕ → Type ℓ) where
  open Semantics interpret-atom
  execution-sound : {Γ : Context} {A : Formula} (d : Proof Γ A) (ρ : Environment Γ)
    → evaluate (construct d) ρ ≡ evaluate d ρ
  execution-sound d ρ = cong (λ p → evaluate p ρ) (construct-correct d)
