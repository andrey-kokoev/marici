{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyObservedBadGuard where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Bool.Base using (Bool)
import RamseyAtomicSeedPaths as Atom
open import RamseyObservedComparisons
bad : ObservedEquiv Bool Bool Bool (λ b → b) (λ b → b)
bad = isoToEquiv Atom.flip , (λ b → refl)
