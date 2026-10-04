{-# OPTIONS --safe --cubical --guardedness #-}
-- Generated from the search artifact, then checked against a cached proof.
module DiscoveredWolframFormula where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import AlgebraSynthesisSpecification
import GeneratedLowerRefutations
import BooleanNandEquivalence as B

found-equation : Equation
found-equation = (op (op (op (var 0) (var 1)) (var 2)) (op (var 0) (op (op (var 0) (var 2)) (var 0)))) , (var 2)
found-formula : Formula
found-formula = found-equation , refl
found-cost : cost found-equation ≡ 6
found-cost = refl

valid : {ℓ : Level} (A : Type ℓ) (boolean : B.BooleanStructure A)
  → Holds found-equation (B.ToWolfram.nand boolean)
valid A boolean env = B.ToWolfram.wolfram boolean (env 0) (env 1) (env 2)

module Recover {ℓ : Level} (A : Type ℓ) (setA : isSet A) (e : A)
  (stroke : A → A → A) (law : Holds found-equation stroke) where
  env : A → A → A → ℕ → A
  env a b c zero = a
  env a b c (suc zero) = b
  env a b c (suc (suc _)) = c
  W : (a b c : A) → stroke (stroke (stroke a b) c) (stroke a (stroke (stroke a c) a)) ≡ c
  W a b c = law (env a b c)
  module R = B.FromWolfram A setA e stroke W

adequate : {ℓ : Level} → Adequate {ℓ} found-equation
adequate = record
  { valid = valid
  ; reconstruct = λ A setA e stroke law →
      Recover.R.boolean A setA e stroke law , Recover.R.recovered-operation A setA e stroke law }

-- No inhabitant of Goal.Result is asserted: the finite minimum certificate is
-- replayed in Python; its enumeration coverage and reflection are not proved here.
