{-# OPTIONS --safe --cubical --guardedness #-}
module CompositionalWitnessCompiler where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Sum.Base using (inl; inr)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc; _+_)
import DomainWitnessCompiler as DWC

-- Syntax is independent of the carrier and its operation.
data Expr : Type where
  var : ℕ → Expr
  fork : Expr → Expr → Expr

nodes : Expr → ℕ
nodes (var n) = zero
nodes (fork s t) = suc (nodes s + nodes t)

module Execute {ℓ : Level} (A : Type ℓ) (op : A → A → A) where
  binary : DWC.Presentation ℓ
  binary = record
    { Input = A × A ; Output = λ _ → A
    ; compute = λ { (x , y) → op x y } }
  module G = DWC.Compile binary

  eval : (ℕ → A) → Expr → A
  eval ρ (var n) = ρ n
  eval ρ (fork s t) = op (eval ρ s) (eval ρ t)

  -- This is a tree of composable data dependencies, not a history on
  -- G.State: G itself has no transition from a response to a new request.
  -- Each internal node retains an actual binary compiler witness.
  data Execution (ρ : ℕ → A) : Expr → A → Type ℓ where
    input : (n : ℕ) → Execution ρ (var n) (ρ n)
    call : {s t : Expr} {x y z : A}
      → Execution ρ s x → Execution ρ t y
      → G.Witness (inl (x , y)) (inr ((x , y) , z))
      → Execution ρ (fork s t) z

  execute : (ρ : ℕ → A) (t : Expr) → Σ[ v ∈ A ] Execution ρ t v
  execute ρ (var n) = ρ n , input n
  execute ρ (fork s t) with execute ρ s | execute ρ t
  ... | x , sx | y , ty =
    G.result (x , y) , call sx ty (G.evaluated (x , y))

  state-value : G.State → A
  state-value (inl (x , y)) = op x y
  state-value (inr (p , z)) = z

  witness-sound : {s t : G.State} → G.Witness s t
    → state-value t ≡ state-value s
  witness-sound (G.evaluated _) = refl
  witness-sound (G.idle _ _) = refl

  binary-sound : {x y z : A}
    → G.Witness (inl (x , y)) (inr ((x , y) , z))
    → z ≡ op x y
  binary-sound = witness-sound

  -- Soundness covers every certificate, not only execute's output.
  sound : {ρ : ℕ → A} {t : Expr} {v : A}
    → Execution ρ t v → v ≡ eval ρ t
  sound (input n) = refl
  sound (call sx ty w) =
    binary-sound w ∙ cong₂ op (sound sx) (sound ty)

  compiler-correct : (ρ : ℕ → A) (t : Expr)
    → fst (execute ρ t) ≡ eval ρ t
  compiler-correct ρ t = sound (snd (execute ρ t))

  calls : {ρ : ℕ → A} {t : Expr} {v : A} → Execution ρ t v → ℕ
  calls (input n) = zero
  calls (call sx ty w) = suc (calls sx + calls ty)

  calls-correct : {ρ : ℕ → A} {t : Expr} {v : A}
    → (r : Execution ρ t v) → calls r ≡ nodes t
  calls-correct (input n) = refl
  calls-correct (call sx ty w) =
    cong suc (cong₂ _+_ (calls-correct sx) (calls-correct ty))

-- ((a | b) | c) | (a | ((a | c) | a)): six binary calls,
-- with no common-subexpression elimination.
wolfram : Expr
wolfram = fork (fork (fork (var 0) (var 1)) (var 2))
  (fork (var 0) (fork (fork (var 0) (var 2)) (var 0)))

module WolframExecution {ℓ : Level} (A : Type ℓ) (op : A → A → A) where
  open Execute A op public

  environment : A → A → A → ℕ → A
  environment a b c zero = a
  environment a b c (suc zero) = b
  environment a b c (suc (suc n)) = c

  six-calls : (a b c : A)
    → calls (snd (execute (environment a b c) wolfram)) ≡ 6
  six-calls a b c = calls-correct (snd (execute (environment a b c) wolfram))

  -- Only this corollary requires the algebraic identity. Generic compiler
  -- soundness above neither assumes nor discovers it.
  identity-result :
    (W : (a b c : A) → op (op (op a b) c) (op a (op (op a c) a)) ≡ c)
    → (a b c : A) → fst (execute (environment a b c) wolfram) ≡ c
  identity-result W a b c =
    compiler-correct (environment a b c) wolfram ∙ W a b c
