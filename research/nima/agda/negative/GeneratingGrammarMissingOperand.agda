{-# OPTIONS --safe --cubical --guardedness #-}
module negative.GeneratingGrammarMissingOperand where
open import Cubical.Foundations.Prelude
import IndexedConstructorTables as Tables
import GeneratingGrammarMacros as Macros

module Bad (ℓ : Level)
  (Admit : Tables.Core.Package ℓ → Type (ℓ-suc ℓ)) where
  module M = Macros.Retained ℓ Admit
  -- A left-operand derivation is not authority for an arbitrary right operand.
  bad : (a b : M.G.Package) → M.Run.Resolve a → M.Run.Resolve (M.pair a b)
  bad a b da = M.pair-run a b da da
