{-# OPTIONS --safe --cubical --guardedness #-}
module ResolutionNetDependentMachine where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; true; false; not)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Sigma.Base using (Σ; _,_; fst; snd)

-- First-order OPEN syntax. No host-language callback is a constructor.
data Index (V : Type) : Type where
  var : V → Index V
  lit : Bool → Index V
  flip : Index V → Index V

replace : {V W : Type} → (V → Index W) → Index V → Index W
replace σ (var v) = σ v
replace σ (lit b) = lit b
replace σ (flip b) = flip (replace σ b)

replace-id : {V : Type} (b : Index V) → replace var b ≡ b
replace-id (var v) = refl
replace-id (lit b) = refl
replace-id (flip b) = cong flip (replace-id b)

replace-compose : {V W X : Type} (σ : V → Index W) (τ : W → Index X)
  (b : Index V) → replace τ (replace σ b) ≡ replace (λ v → replace τ (σ v)) b
replace-compose σ τ (var v) = refl
replace-compose σ τ (lit b) = refl
replace-compose σ τ (flip b) = cong flip (replace-compose σ τ b)

-- A syntactic family: output terms carry their actual index expression.
-- Its interpretation will be Unit at true, and Nat at false.
data Output {V : Type} : Index V → Type where
  unit : Output (lit true)
  number : ℕ → Output (lit false)
  choose : (b : Index V) → ℕ → Output b

Config : Type → Type
Config V = Σ (Index V) Output

replace-output : {V W : Type} (σ : V → Index W) {b : Index V}
  → Output b → Output (replace σ b)
replace-output σ unit = unit
replace-output σ (number n) = number n
replace-output σ (choose b n) = choose (replace σ b) n

replace-config : {V W : Type} → (V → Index W) → Config V → Config W
replace-config σ (b , d) = replace σ b , replace-output σ d

-- Directed rules, independent of the denotational interpreter below.
data IndexStep {V : Type} : Index V → Index V → Type where
  flip-true : IndexStep (flip (lit true)) (lit false)
  flip-false : IndexStep (flip (lit false)) (lit true)
  under-flip : {b c : Index V} → IndexStep b c → IndexStep (flip b) (flip c)

data Step {V : Type} : Config V → Config V → Type where
  demand : {b c : Index V} (n : ℕ) → IndexStep b c
    → Step (b , choose b n) (c , choose c n)
  select-true : (n : ℕ) → Step (lit true , choose (lit true) n) (lit true , unit)
  select-false : (n : ℕ) → Step (lit false , choose (lit false) n) (lit false , number n)

-- Object-level reduction is stable under object-level substitution.
replace-index-step : {V W : Type} (σ : V → Index W) {b c : Index V}
  → IndexStep b c → IndexStep (replace σ b) (replace σ c)
replace-index-step σ flip-true = flip-true
replace-index-step σ flip-false = flip-false
replace-index-step σ (under-flip s) = under-flip (replace-index-step σ s)

replace-step : {V W : Type} (σ : V → Index W) {c d : Config V}
  → Step c d → Step (replace-config σ c) (replace-config σ d)
replace-step σ (demand n s) = demand n (replace-index-step σ s)
replace-step σ (select-true n) = select-true n
replace-step σ (select-false n) = select-false n

-- A closed one-step machine computes from syntax, not from eval-index.
data IndexProgress : Index ⊥ → Type where
  ready : (b : Bool) → IndexProgress (lit b)
  advance-index : {b c : Index ⊥} → IndexStep b c → IndexProgress b

index-progress : (b : Index ⊥) → IndexProgress b
index-progress (var ())
index-progress (lit b) = ready b
index-progress (flip b) with index-progress b
... | ready true = advance-index flip-true
... | ready false = advance-index flip-false
... | advance-index s = advance-index (under-flip s)

data Value : Config ⊥ → Type where
  unit-value : Value (lit true , unit)
  number-value : (n : ℕ) → Value (lit false , number n)

data Progress (c : Config ⊥) : Type where
  halt : Value c → Progress c
  advance : {d : Config ⊥} → Step c d → Progress c

progress : (c : Config ⊥) → Progress c
progress (_ , unit) = halt unit-value
progress (_ , number n) = halt (number-value n)
progress (b , choose .b n) with index-progress b
... | ready true = advance (select-true n)
... | ready false = advance (select-false n)
... | advance-index s = advance (demand n s)

-- Separate mathematical interpretation, used to prove soundness.
Family : Bool → Type
Family true = Unit
Family false = ℕ

eval-index : {V : Type} → Index V → (V → Bool) → Bool
eval-index (var v) ρ = ρ v
eval-index (lit b) ρ = b
eval-index (flip b) ρ = not (eval-index b ρ)

branch : (b : Bool) → ℕ → Family b
branch true n = tt
branch false n = n

eval-output : {V : Type} {b : Index V} → Output b → (ρ : V → Bool) → Family (eval-index b ρ)
eval-output unit ρ = tt
eval-output (number n) ρ = n
eval-output (choose b n) ρ = branch (eval-index b ρ) n

observe : {V : Type} → Config V → (V → Bool) → Σ Bool Family
observe (b , d) ρ = eval-index b ρ , eval-output d ρ

index-sound : {V : Type} {b c : Index V} → IndexStep b c
  → (ρ : V → Bool) → eval-index b ρ ≡ eval-index c ρ
index-sound flip-true ρ = refl
index-sound flip-false ρ = refl
index-sound (under-flip s) ρ = cong not (index-sound s ρ)

-- Equality is of dependent pairs, not untyped output observations.
step-sound : {V : Type} {c d : Config V} → Step c d
  → (ρ : V → Bool) → observe c ρ ≡ observe d ρ
step-sound (demand n s) ρ = cong (λ b → b , branch b n) (index-sound s ρ)
step-sound (select-true n) ρ = refl
step-sound (select-false n) ρ = refl

index-substitution : {V W : Type} (σ : V → Index W) (b : Index V) (ρ : W → Bool)
  → eval-index (replace σ b) ρ ≡ eval-index b (λ v → eval-index (σ v) ρ)
index-substitution σ (var v) ρ = refl
index-substitution σ (lit b) ρ = refl
index-substitution σ (flip b) ρ = cong not (index-substitution σ b ρ)

substitution-sound : {V W : Type} (σ : V → Index W) (c : Config V) (ρ : W → Bool)
  → observe (replace-config σ c) ρ ≡ observe c (λ v → eval-index (σ v) ρ)
substitution-sound σ (_ , unit) ρ = refl
substitution-sound σ (_ , number n) ρ = refl
substitution-sound σ (b , choose .b n) ρ =
  cong (λ b → b , branch b n) (index-substitution σ b ρ)

-- Concrete open program, with two explicitly witnessed machine steps.
program : Config Unit
program = flip (var tt) , choose (flip (var tt)) (suc zero)

supplied : Config ⊥
supplied = replace-config (λ _ → lit true) program

first-step : Step supplied (lit false , choose (lit false) (suc zero))
first-step = demand (suc zero) flip-true

second-step : Step {V = ⊥} (lit false , choose (lit false) (suc zero)) (lit false , number (suc zero))
second-step = select-false (suc zero)

machine-first : progress supplied ≡ advance first-step
machine-first = refl

machine-second : progress (lit false , choose (lit false) (suc zero)) ≡ advance second-step
machine-second = refl

machine-halts : progress (lit false , number (suc zero)) ≡ halt (number-value (suc zero))
machine-halts = refl
