{-# OPTIONS --safe --cubical --guardedness #-}
module BadBaseOnlyExtensionComparison where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Unit.Base using (Unit)
open import Cubical.Data.Bool.Base using (Bool)
open import CoherentDependentExtensions

choices forgotten : Family ℓ-zero
Base choices = Unit
Witness choices _ = Bool
Base forgotten = Unit
Witness forgotten _ = Unit

-- The identity on bases cannot justify discarding a two-valued witness fiber.
bad : Comparison choices forgotten
baseEquiv bad = idEquiv Unit
witnessEquiv bad _ = idEquiv Bool
