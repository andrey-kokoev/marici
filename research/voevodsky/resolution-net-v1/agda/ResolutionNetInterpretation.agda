{-# OPTIONS --safe --cubical --guardedness #-}
module ResolutionNetInterpretation where

open import Cubical.Foundations.Prelude
open import CoherenceResolutionClosure

-- An interpretation gives mathematical operations to the rule witnesses.
-- No wire graph, scheduling policy, or concrete evaluator occurs here.
module Interpretation {ℓ : Level}
  (P : Type ℓ)
  (U : P → P → Type ℓ)
  (V : P → P → P → Type ℓ)
  (A : P → Type ℓ)
  (actU : {p q : P} → U p q → A p → A q)
  (actV : {p q r : P} → V p q r → A p → A q → A r) where

  open Closure P U V

  fold : {S : P → Type ℓ} → ((p : P) → S p → A p)
       → {p : P} → Resolve S p → A p
  fold f (seed s) = f _ s
  fold f (unary u d) = actU u (fold f d)
  fold f (binary v d e) = actV v (fold f d) (fold f e)

  -- Substitution is composition of computations with open inputs.
  bind : {S T : P → Type ℓ} → ((p : P) → S p → Resolve T p)
       → {p : P} → Resolve S p → Resolve T p
  bind k d = flatten (mapSeeds k d)

  -- Execute after substitution = substitute executed results and execute.
  fold-bind : {S T : P → Type ℓ}
    (k : (p : P) → S p → Resolve T p)
    (f : (p : P) → T p → A p)
    {p : P} (d : Resolve S p)
    → fold f (bind k d) ≡ fold (λ p s → fold f (k p s)) d
  fold-bind k f (seed s) = refl
  fold-bind k f (unary u d) = cong (actU u) (fold-bind k f d)
  fold-bind k f (binary v d e) i =
    actV v (fold-bind k f d i) (fold-bind k f e i)

  -- An operation-preserving interpretation is forced by its seed action.
  -- Pointwise uniqueness, not a claim that all higher homomorphism
  -- coherence data form a contractible type.
  unique : {S : P → Type ℓ}
    (f : (p : P) → S p → A p)
    (h : {p : P} → Resolve S p → A p)
    (on-seed : {p : P} (s : S p) → h (seed s) ≡ f p s)
    (on-unary : {p q : P} (u : U p q) (d : Resolve S p)
      → h (unary u d) ≡ actU u (h d))
    (on-binary : {p q r : P} (v : V p q r)
      (d : Resolve S p) (e : Resolve S q)
      → h (binary v d e) ≡ actV v (h d) (h e))
    {p : P} (d : Resolve S p) → h d ≡ fold f d
  unique f h on-seed on-unary on-binary (seed s) = on-seed s
  unique f h on-seed on-unary on-binary (unary u d) =
    on-unary u d ∙ cong (actU u) (unique f h on-seed on-unary on-binary d)
  unique f h on-seed on-unary on-binary (binary v d e) =
    on-binary v d e ∙ (λ i → actV v
      (unique f h on-seed on-unary on-binary d i)
      (unique f h on-seed on-unary on-binary e i))
