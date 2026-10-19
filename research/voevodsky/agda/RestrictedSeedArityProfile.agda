{-# OPTIONS --safe --cubical --guardedness #-}
module RestrictedSeedArityProfile where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Nat.Base using (ℕ; suc; _+_)
import WholePackageSigmaPi as W
import WholePackageResolution as R
open W.Universe ℓ-zero
module G = R.Generators ℓ-zero

-- Admission is a command language fixed before evaluating any output.
data SeedName : Type where
  false-seed : SeedName

data Term : Type where
  literal : SeedName → Term
  identity : Term → Term
  pair : Term → Term → Term
  select : Bool → Term → Term → Term

family : Complete → Complete → Bool → Complete
family a b false = a
family a b true = b

base : Complete
base = pack (atom Bool) false

eval : Term → Complete
eval (literal false-seed) = base
eval (identity t) = G.output (G.identity-rule (eval t))
eval (pair t u) = G.output (G.Pi-rule Bool (family (eval t) (eval u)))
eval (select b t u) = G.output (G.E-rule Bool (family (eval t) (eval u)) b)

-- Original seed relation is only a target for the compiler. No claim that
-- its entire path-closed semantic closure equals this syntactic fragment.
data Seed : Complete → Type₁ where
  admitted-false : Seed base

compile : (t : Term) → G.Resolve Seed (eval t)
compile (literal false-seed) = G.seed admitted-false
compile (identity t) = G.apply (G.identity-rule (eval t)) (λ _ → compile t)
compile (pair t u) = G.apply (G.Pi-rule Bool (family (eval t) (eval u)))
  (λ { (lift false) → compile t ; (lift true) → compile u })
compile (select b t u) = G.apply (G.E-rule Bool (family (eval t) (eval u)) b)
  (λ { (lift false) → compile t ; (lift true) → compile u })

-- Explicit finite arity: even selecting a sum retains BOTH input branches.
cost : Term → ℕ
cost (literal false-seed) = 1
cost (identity t) = suc (cost t)
cost (pair t u) = suc (cost t + cost u)
cost (select b t u) = suc (cost t + cost u)

Retained : Type₁
Retained = Σ[ t ∈ Term ] G.Resolve Seed (eval t)

run : Term → Retained
run t = t , compile t

source-recovered : (t : Term) → fst (run t) ≡ t
source-recovered t = refl

selected-example : Term
selected-example = select false (literal false-seed) (identity (literal false-seed))

unselected-branch-counted : cost selected-example ≡ 4
unselected-branch-counted = refl

example-endpoint : fst (value (G.output (G.E-rule Bool
  (family base (G.output (G.identity-rule base))) false))) ≡ false
example-endpoint = refl
