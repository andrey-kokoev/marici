{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyAtomicSeedPathBadReflection where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (false; true)
open import RamseyAtomicSeedPaths
-- The package path does not give a path in the fixed Bool carrier.
bad : false ≡ true
bad = swapped
