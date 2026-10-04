{-# OPTIONS --safe --cubical --guardedness #-}
module SynthesisBadFormula where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import AlgebraSynthesisSpecification
open import DiscoveredWolframFormula using (found-equation)

nand : Bool → Bool → Bool
nand false y = true
nand true false = true
nand true true = false
env : ℕ → Bool
env zero = false
env (suc zero) = false
env (suc (suc _)) = true
-- Mutating the discovered right-hand variable from x2 to x0 is false.
mutated : Equation
mutated = fst found-equation , var 0
bad : eval nand env (fst mutated) ≡ eval nand env (snd mutated)
bad = refl
